import { useState, useEffect, useRef } from 'react';
import {
  LiveKitRoom,
  RoomAudioRenderer,
  BarVisualizer,
  useVoiceAssistant,
  useTranscriptions,
  VideoTrack,
  useRoomContext,
} from '@livekit/components-react';
import {
  Mic,
  MicOff,
  Phone,
  PhoneOff,
  Calendar,
  Clock,
  User,
  Check,
  X,
  Activity,
  FileText,
  Trash2,
  CalendarDays,
} from 'lucide-react';
import './App.css';

interface UserProfile {
  id: number;
  name: string;
  phone: string;
}

interface Appointment {
  id: number;
  slot_id: number;
  date: string;
  time: string;
  status: string;
  doctor_name?: string;
  doctor_specialty?: string;
}

interface Slot {
  id: number;
  time: string;
  available: boolean;
  doctor_name?: string;
  doctor_specialty?: string;
}

// Helper to get next N days for the calendar
const getNextNDays = (n: number) => {
  const days = [];
  for (let i = 0; i < n; i++) {
    const d = new Date();
    d.setDate(d.getDate() + i);
    days.push({
      dateString: d.toISOString().split('T')[0], // YYYY-MM-DD
      dayNumber: d.getDate(),
      dayName: d.toLocaleDateString('en-US', { weekday: 'short' }),
      monthName: d.toLocaleDateString('en-US', { month: 'short' })
    });
  }
  return days;
};

// WebRTC data packet listener for active call
function RoomEventListener({
  onUserIdentified,
  onToolCall,
  onCallStarted,
  onCallEnded
}: {
  onUserIdentified: (user: any) => void;
  onToolCall: (status: any) => void;
  onCallStarted: (callId: string) => void;
  onCallEnded: () => void;
}) {
  const room = useRoomContext();

  useEffect(() => {
    if (!room) return;

    const handleDataReceived = (payload: Uint8Array, _participant: any, _kind: any, topic?: string) => {
      const decoder = new TextDecoder();
      const text = decoder.decode(payload);
      try {
        const data = JSON.parse(text);
        if (topic === 'tool_call') {
          onToolCall(data);
        } else if (topic === 'user_identified') {
          onUserIdentified(data);
        } else if (topic === 'call_started') {
          onCallStarted(data.call_id);
        } else if (topic === 'call_ended') {
          onCallEnded();
        }
      } catch (e) {
        console.error('Error decoding WebRTC data packet:', e);
      }
    };

    room.on('dataReceived', handleDataReceived);
    return () => {
      room.off('dataReceived', handleDataReceived);
    };
  }, [room, onUserIdentified, onToolCall, onCallStarted, onCallEnded]);

  return null;
}

function App() {
  const [userProfile, setUserProfile] = useState<UserProfile | null>(null);
  const [roomToken, setRoomToken] = useState<string | null>(null);
  const [roomName, setRoomName] = useState<string | null>(null);
  const [isConnecting, setIsConnecting] = useState(false);
  const [appointments, setAppointments] = useState<Appointment[]>([]);
  const [isLoadingAppointments, setIsLoadingAppointments] = useState(false);
  const [isRescheduling, setIsRescheduling] = useState<Appointment | null>(null);
  const [availableSlots, setAvailableSlots] = useState<Slot[]>([]);
  const [isLoadingSlots, setIsLoadingSlots] = useState(false);
  const [slotDate, setSlotDate] = useState('');
  const [selectedSlotId, setSelectedSlotId] = useState<number | null>(null);
  const [_error, setError] = useState<string | null>(null);

  // New session & call summary states
  const [currentCallId, setCurrentCallId] = useState<string | null>(null);
  const [activeToolStatus, setActiveToolStatus] = useState<{ tool: string; status: string; message: string } | null>(null);
  const [callSummary, setCallSummary] = useState<{
    summary: string;
    preferences: string;
    user: { name: string; phone: string };
    appointments: Appointment[];
    timestamp: string;
  } | null>(null);
  const [isGeneratingSummary, setIsGeneratingSummary] = useState(false);

  // Calendar panel states
  const [selectedDate, setSelectedDate] = useState<string>(new Date().toISOString().split('T')[0]);
  const [selectedDoctorId, setSelectedDoctorId] = useState<number | 'all'>('all');
  const [calendarSlots, setCalendarSlots] = useState<Slot[]>([]);
  const [isLoadingCalendarSlots, setIsLoadingCalendarSlots] = useState(false);
  const [highlightedApptId, setHighlightedApptId] = useState<number | null>(null);

  // Fetch appointments for identified user
  const fetchAppointments = async (phone: string) => {
    try {
      setIsLoadingAppointments(true);
      const res = await fetch(`https://carevoice-token-server.onrender.com/api/appointments?phone=${encodeURIComponent(phone)}`);
      if (res.ok) {
        const data = await res.json();
        setAppointments(data.appointments || []);
      }
    } catch (err) {
      console.error('Error fetching appointments:', err);
    } finally {
      setIsLoadingAppointments(false);
    }
  };

  // Fetch calendar slots
  const fetchCalendarSlots = async (date: string) => {
    try {
      setIsLoadingCalendarSlots(true);
      const res = await fetch(`https://carevoice-token-server.onrender.com/api/slots?date=${encodeURIComponent(date)}`);
      if (res.ok) {
        const data = await res.json();
        setCalendarSlots(data.slots || []);
      }
    } catch (err) {
      console.error('Error fetching calendar slots:', err);
    } finally {
      setIsLoadingCalendarSlots(false);
    }
  };

  useEffect(() => {
    if (selectedDate) {
      fetchCalendarSlots(selectedDate);
    }
  }, [selectedDate]);

  // Book a slot directly from calendar
  const handleBookCalendarSlot = async (slotId: number) => {
    if (!userProfile) {
      alert('Please enter your details in the profile card or start a consultation to identify yourself.');
      return;
    }

    if (!window.confirm('Are you sure you want to book this appointment slot?')) return;

    try {
      const res = await fetch('https://carevoice-token-server.onrender.com/api/appointments/book', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ user_id: userProfile.id, slot_id: slotId }),
      });

      if (res.ok) {
        // Refresh available slots for selected date & active appointments list
        fetchCalendarSlots(selectedDate);
        fetchAppointments(userProfile.phone);
      } else {
        const err = await res.json();
        alert(err.error || 'Failed to book slot');
      }
    } catch (err) {
      console.error('Error booking slot:', err);
      alert('Network error trying to book slot');
    }
  };

  // Scroll to and highlight appointment on date/doctor click
  useEffect(() => {
    if (!appointments || appointments.length === 0) return;

    const matched = appointments.find((appt) => {
      const dateMatch = appt.date === selectedDate;
      const doctorMatch = selectedDoctorId === 'all' || 
        (selectedDoctorId === 1 && appt.doctor_name?.includes('Jenkins')) ||
        (selectedDoctorId === 2 && appt.doctor_name?.includes('Stone')) ||
        (selectedDoctorId === 3 && appt.doctor_name?.includes('Vance'));
      return dateMatch && doctorMatch;
    });

    if (matched) {
      setHighlightedApptId(matched.id);
      const el = document.getElementById(`appt-card-${matched.id}`);
      if (el) {
        el.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      }
      
      const timer = setTimeout(() => {
        setHighlightedApptId(null);
      }, 2500);
      return () => clearTimeout(timer);
    }
  }, [selectedDate, selectedDoctorId, appointments]);

  // Start Call (anonymous start)
  const handleStartCall = async () => {
    setIsConnecting(true);
    setError(null);
    setActiveToolStatus(null);
    setCallSummary(null);
    setIsGeneratingSummary(false);
    setCurrentCallId(null);

    // Generate fresh anonymous room details
    const randomSuffix = Math.random().toString(36).substring(7);
    const generatedRoom = `room-${randomSuffix}`;
    setRoomName(generatedRoom);

    try {
      const res = await fetch(
        `https://carevoice-token-server.onrender.com/token?room=${encodeURIComponent(generatedRoom)}&identity=${encodeURIComponent(
          "patient-" + randomSuffix
        )}`
      );
      if (res.ok) {
        const data = await res.json();
        setRoomToken(data.token);
        // Reset user info for new anonymous session
        setUserProfile(null);
        setAppointments([]);
      } else {
        const errData = await res.json();
        setError(errData.error || 'Failed to generate access token');
        setIsConnecting(false);
      }
    } catch (err) {
      console.error('Error fetching token:', err);
      setError('Connection error to token server');
      setIsConnecting(false);
    }
  };

  // End Call
  const handleEndCall = () => {
    setRoomToken(null);
    setRoomName(null);
    setIsConnecting(false);
    setActiveToolStatus(null);

    // Start fetching summary — delay 3s to allow agent worker time to
    // generate and persist the summary after the room disconnects
    if (currentCallId) {
      setTimeout(() => pollCallSummary(currentCallId), 3000);
    }
  };

  // Poll Call Summary from Backend
  const pollCallSummary = async (callId: string) => {
    setIsGeneratingSummary(true);
    let attempts = 0;
    const maxAttempts = 15; // up to 15 seconds

    const interval = setInterval(async () => {
      attempts++;
      try {
        const res = await fetch(`https://carevoice-token-server.onrender.com/api/summary?call_id=${encodeURIComponent(callId)}`);
        if (res.ok) {
          const data = await res.json();
          if (data.status === 'completed') {
            clearInterval(interval);
            setIsGeneratingSummary(false);

            // If patient identified during call, set userProfile
            if (data.user && data.user.phone && data.user.phone !== 'Not provided') {
              const resolvedProfile = {
                id: data.user.user_id || 0,
                name: data.user.name !== 'Anonymous Patient' ? data.user.name : (userProfile?.name || 'Anonymous Patient'),
                phone: data.user.phone
              };
              setUserProfile(resolvedProfile);

              // Always fetch FRESH appointments directly from API (summary may have been
              // generated before appointments were booked during the call)
              try {
                const apptRes = await fetch(`https://carevoice-token-server.onrender.com/api/appointments?phone=${encodeURIComponent(data.user.phone)}`);
                if (apptRes.ok) {
                  const apptData = await apptRes.json();
                  const freshAppointments = apptData.appointments || [];
                  setAppointments(freshAppointments);
                  // Inject fresh appointments into the summary card too
                  setCallSummary({ ...data, appointments: freshAppointments });
                  return;
                }
              } catch (apptErr) {
                console.error('Error fetching fresh appointments after summary:', apptErr);
              }
            }

            setCallSummary(data);
          }
        }
      } catch (err) {
        console.error('Error polling call summary:', err);
      }

      if (attempts >= maxAttempts) {
        clearInterval(interval);
        setIsGeneratingSummary(false);
        setCallSummary({
          summary: "Consultation ended. AI summary generation timed out, but your active appointments and profile are synced.",
          preferences: "None",
          user: {
            name: userProfile?.name || "Anonymous Patient",
            phone: userProfile?.phone || "Not provided"
          },
          appointments: appointments,
          timestamp: new Date().toISOString()
        });
      }
    }, 1000);
  };

  // Cancel Appointment
  const handleCancelAppointment = async (appointmentId: number) => {
    if (!window.confirm('Are you sure you want to cancel this appointment?')) return;

    try {
      const res = await fetch('https://carevoice-token-server.onrender.com/api/appointments/cancel', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ appointment_id: appointmentId }),
      });

      if (res.ok) {
        if (userProfile) fetchAppointments(userProfile.phone);
        fetchCalendarSlots(selectedDate);
      } else {
        const errData = await res.json();
        alert(errData.error || 'Failed to cancel appointment');
      }
    } catch (err) {
      console.error('Error cancelling appointment:', err);
      alert('Network error trying to cancel appointment');
    }
  };

  // Open Reschedule Modal
  const handleOpenReschedule = (appointment: Appointment) => {
    setIsRescheduling(appointment);
    setSelectedSlotId(null);
    
    const today = new Date().toISOString().split('T')[0];
    const defaultDate = appointment.date >= today ? appointment.date : today;
    setSlotDate(defaultDate);
    fetchAvailableSlots(defaultDate);
  };

  // Fetch Slots for date (Reschedule Modal)
  const fetchAvailableSlots = async (date: string) => {
    try {
      setIsLoadingSlots(true);
      const res = await fetch(`https://carevoice-token-server.onrender.com/api/slots?date=${encodeURIComponent(date)}`);
      if (res.ok) {
        const data = await res.json();
        setAvailableSlots(data.slots || []);
      }
    } catch (err) {
      console.error('Error fetching slots:', err);
    } finally {
      setIsLoadingSlots(false);
    }
  };

  // Trigger slot fetch on date change (Reschedule Modal)
  const handleDateChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const newDate = e.target.value;
    setSlotDate(newDate);
    fetchAvailableSlots(newDate);
    setSelectedSlotId(null);
  };

  // Submit Reschedule
  const handleRescheduleSubmit = async () => {
    if (!isRescheduling || !selectedSlotId) return;

    try {
      const res = await fetch('https://carevoice-token-server.onrender.com/api/appointments/modify', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          appointment_id: isRescheduling.id,
          new_slot_id: selectedSlotId,
        }),
      });

      if (res.ok) {
        setIsRescheduling(null);
        setSelectedSlotId(null);
        if (userProfile) fetchAppointments(userProfile.phone);
        fetchCalendarSlots(selectedDate);
      } else {
        const errData = await res.json();
        alert(errData.error || 'Failed to reschedule appointment');
      }
    } catch (err) {
      console.error('Error rescheduling appointment:', err);
      alert('Network error trying to reschedule');
    }
  };

  // Logout/Reset
  const handleLogout = () => {
    setUserProfile(null);
    setRoomToken(null);
    setRoomName(null);
    setAppointments([]);
    setCallSummary(null);
    setIsGeneratingSummary(false);
    setCurrentCallId(null);
    setActiveToolStatus(null);
  };

  const handleResetSession = () => {
    setCallSummary(null);
    setUserProfile(null);
    setAppointments([]);
  };

  return (
    <div className="app-container">
      <header className="header">
        <div className="brand">
          <Activity size={24} className="brand-icon" />
          <h2 className="brand-title">CareVoice Health Dashboard</h2>
        </div>
        <div style={{ display: 'flex', gap: '12px', alignItems: 'center' }}>
          <span className="status-badge">
            <span className={`status-dot ${roomToken ? 'active' : ''}`} />
            {roomToken ? 'Live Connection' : 'Offline'}
          </span>
          <button
            onClick={handleLogout}
            style={{
              background: 'transparent',
              border: '1px solid var(--border-color)',
              color: 'var(--text-secondary)',
              padding: '6px 12px',
              borderRadius: '8px',
              cursor: 'pointer',
              fontSize: '13px',
              fontWeight: 500,
            }}
          >
            Reset
          </button>
        </div>
      </header>

      {roomToken && roomName ? (
        <LiveKitRoom
          serverUrl="wss://voicerhealth-77yely9v.livekit.cloud"
          token={roomToken}
          connect={true}
          audio={true}
          video={false}
          onDisconnected={handleEndCall}
          className="livekit-room-wrapper"
        >
          <RoomAudioRenderer />
          <RoomEventListener
            onCallStarted={(callId) => setCurrentCallId(callId)}
            onUserIdentified={(user) => {
              setUserProfile({
                id: user.user_id,
                name: user.name,
                phone: user.phone
              });
              fetchAppointments(user.phone);
            }}
            onToolCall={(status) => {
              setActiveToolStatus(status);
              if (status.status === 'completed' || status.status === 'failed') {
                setTimeout(() => {
                  setActiveToolStatus((prev) => prev?.tool === status.tool ? null : prev);
                }, 3500);
              }
            }}
            onCallEnded={handleEndCall}
          />
          <DashboardContent
            userProfile={userProfile}
            setUserProfile={setUserProfile}
            appointments={appointments}
            isLoadingAppointments={isLoadingAppointments}
            isActiveCall={true}
            isConnecting={false}
            onStartCall={handleStartCall}
            onEndCall={handleEndCall}
            onCancelAppointment={handleCancelAppointment}
            onOpenReschedule={handleOpenReschedule}
            activeToolStatus={activeToolStatus}
            callSummary={callSummary}
            isGeneratingSummary={isGeneratingSummary}
            onResetSession={handleResetSession}
            selectedDate={selectedDate}
            setSelectedDate={setSelectedDate}
            selectedDoctorId={selectedDoctorId}
            setSelectedDoctorId={setSelectedDoctorId}
            calendarSlots={calendarSlots}
            isLoadingCalendarSlots={isLoadingCalendarSlots}
            highlightedApptId={highlightedApptId}
            onBookCalendarSlot={handleBookCalendarSlot}
            fetchAppointments={fetchAppointments}
          />
        </LiveKitRoom>
      ) : (
        <DashboardContent
          userProfile={userProfile}
          setUserProfile={setUserProfile}
          appointments={appointments}
          isLoadingAppointments={isLoadingAppointments}
          isActiveCall={false}
          isConnecting={isConnecting}
          onStartCall={handleStartCall}
          onEndCall={handleEndCall}
          onCancelAppointment={handleCancelAppointment}
          onOpenReschedule={handleOpenReschedule}
          activeToolStatus={activeToolStatus}
          callSummary={callSummary}
          isGeneratingSummary={isGeneratingSummary}
          onResetSession={handleResetSession}
          selectedDate={selectedDate}
          setSelectedDate={setSelectedDate}
          selectedDoctorId={selectedDoctorId}
          setSelectedDoctorId={setSelectedDoctorId}
          calendarSlots={calendarSlots}
          isLoadingCalendarSlots={isLoadingCalendarSlots}
          highlightedApptId={highlightedApptId}
          onBookCalendarSlot={handleBookCalendarSlot}
          fetchAppointments={fetchAppointments}
        />
      )}

      {/* Reschedule Modal */}
      {isRescheduling && (
        <div className="modal-overlay">
          <div className="modal-content">
            <div className="modal-header">
              <h3 className="modal-title">Reschedule Appointment</h3>
              <button className="btn-close" onClick={() => setIsRescheduling(null)}>
                <X size={20} />
              </button>
            </div>
            
            <div className="form-group" style={{ marginBottom: '16px' }}>
              <label className="form-label">Select Date</label>
              <input
                type="date"
                className="form-input"
                value={slotDate}
                min={new Date().toISOString().split('T')[0]}
                onChange={handleDateChange}
              />
            </div>

            <label className="form-label">Available Slots</label>
            {isLoadingSlots ? (
              <div style={{ textAlign: 'center', padding: '20px', color: 'var(--text-secondary)' }}>
                Loading slots...
              </div>
            ) : (
              <div className="slot-grid">
                {availableSlots.length === 0 ? (
                  <div className="no-slots-message">No slots available for this date.</div>
                ) : (
                  availableSlots.map((slot) => (
                    <button
                      key={slot.id}
                      className={`slot-btn ${selectedSlotId === slot.id ? 'selected' : ''}`}
                      disabled={!slot.available}
                      onClick={() => setSelectedSlotId(slot.id)}
                      style={{ fontSize: '11px', display: 'flex', flexDirection: 'column', alignItems: 'center', gap: '2px' }}
                    >
                      <strong style={{ fontSize: '13px' }}>{slot.time}</strong>
                      <span style={{ opacity: 0.8, fontSize: '10px' }}>{slot.doctor_name?.split(' ').pop()}</span>
                    </button>
                  ))
                )}
              </div>
            )}

            <div className="modal-actions">
              <button className="btn-modal btn-modal-cancel" onClick={() => setIsRescheduling(null)}>
                Cancel
              </button>
              <button
                className="btn-modal btn-modal-confirm"
                disabled={!selectedSlotId}
                onClick={handleRescheduleSubmit}
              >
                Confirm Reschedule
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

interface DashboardContentProps {
  userProfile: UserProfile | null;
  setUserProfile: (profile: UserProfile | null) => void;
  appointments: Appointment[];
  isLoadingAppointments: boolean;
  isActiveCall: boolean;
  isConnecting: boolean;
  onStartCall: () => void;
  onEndCall: () => void;
  onCancelAppointment: (id: number) => void;
  onOpenReschedule: (appointment: Appointment) => void;
  activeToolStatus: { tool: string; status: string; message: string } | null;
  callSummary: any;
  isGeneratingSummary: boolean;
  onResetSession: () => void;
  selectedDate: string;
  setSelectedDate: (date: string) => void;
  selectedDoctorId: number | 'all';
  setSelectedDoctorId: (id: number | 'all') => void;
  calendarSlots: Slot[];
  isLoadingCalendarSlots: boolean;
  highlightedApptId: number | null;
  onBookCalendarSlot: (slotId: number) => void;
  fetchAppointments: (phone: string) => void;
}

function DashboardContent({
  userProfile,
  setUserProfile,
  appointments,
  isLoadingAppointments,
  isActiveCall,
  isConnecting,
  onStartCall,
  onEndCall,
  onCancelAppointment,
  onOpenReschedule,
  activeToolStatus,
  callSummary,
  isGeneratingSummary,
  onResetSession,
  selectedDate,
  setSelectedDate,
  selectedDoctorId,
  setSelectedDoctorId,
  calendarSlots,
  isLoadingCalendarSlots,
  highlightedApptId,
  onBookCalendarSlot,
  fetchAppointments,
}: DashboardContentProps) {
  const displayProfile = userProfile || { id: 0, name: 'Anonymous Patient', phone: 'Not identified yet' };

  // Manual Profile identification inputs in Right Panel
  const [isEditingProfile, setIsEditingProfile] = useState(false);
  const [manualName, setManualName] = useState('');
  const [manualPhone, setManualPhone] = useState('');
  const [manualNameError, setManualNameError] = useState<string | null>(null);
  const [manualPhoneError, setManualPhoneError] = useState<string | null>(null);

  const handleManualIdentifySubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setManualNameError(null);
    setManualPhoneError(null);

    let hasError = false;
    const trimmedName = manualName.trim();
    if (trimmedName.length < 2) {
      setManualNameError('Name must be at least 2 characters.');
      hasError = true;
    } else if (!/^[a-zA-Z\s]+$/.test(trimmedName)) {
      setManualNameError('Name can only contain letters and spaces.');
      hasError = true;
    }

    const trimmedPhone = manualPhone.trim();
    const digitCount = trimmedPhone.replace(/\D/g, '').length;
    if (digitCount < 7) {
      setManualPhoneError('Phone must contain at least 7 digits.');
      hasError = true;
    } else if (!/^[0-9\s()+-]+$/.test(trimmedPhone)) {
      setManualPhoneError('Invalid phone number characters.');
      hasError = true;
    }

    if (hasError) return;

    try {
      const res = await fetch('https://carevoice-token-server.onrender.com/api/identify', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name: trimmedName, phone: trimmedPhone }),
      });

      if (res.ok) {
        const data = await res.json();
        setUserProfile({
          id: data.user_id,
          name: data.name,
          phone: data.phone,
        });
        setIsEditingProfile(false);
        fetchAppointments(data.phone);
      } else {
        const errData = await res.json();
        alert(errData.error || 'Failed to identify user');
      }
    } catch (err) {
      console.error('Error identifying user:', err);
      alert('Error connecting to backend server');
    }
  };

  const filteredCalendarSlots = () => {
    return calendarSlots.filter((slot) => {
      if (!slot.available) return false;
      if (selectedDoctorId === 'all') return true;
      if (selectedDoctorId === 1 && slot.doctor_name?.includes('Jenkins')) return true;
      if (selectedDoctorId === 2 && slot.doctor_name?.includes('Stone')) return true;
      if (selectedDoctorId === 3 && slot.doctor_name?.includes('Vance')) return true;
      return false;
    });
  };

  return (
    <div className="dashboard-grid">
      {/* LEFT PANEL: Voice Assistant Control */}
      <div className="panel assistant-panel animate-slide-in-left">
        <div className="assistant-info">
          <h3 className="assistant-title">Virtual Assistant</h3>
          <p className="assistant-desc">
            Speak naturally to book, reschedule, or cancel your healthcare appointments.
          </p>
        </div>

        {isActiveCall ? (
          <ActiveVoiceControl onEndCall={onEndCall} />
        ) : (
          <OfflineVoiceControl isConnecting={isConnecting} onStartCall={onStartCall} />
        )}

        {/* Real-time Tool Execution Indicator */}
        {isActiveCall && activeToolStatus && (
          <div className={`tool-status-container ${activeToolStatus.status}`}>
            <div className="tool-status-icon">
              {activeToolStatus.status === 'started' ? (
                <Clock size={16} className="tool-status-icon running" />
              ) : activeToolStatus.status === 'completed' ? (
                <Check size={16} className="tool-status-icon completed" />
              ) : (
                <X size={16} className="tool-status-icon failed" />
              )}
            </div>
            <div className="tool-status-text">
              {activeToolStatus.message}
            </div>
          </div>
        )}
      </div>

      {/* CENTER PANEL: Live Transcripts / Call Summary */}
      <div className="panel transcript-panel animate-fade-in">
        <div className="panel-header" style={{ flexShrink: 0 }}>
          <h3 className="panel-title">
            <FileText size={18} className="panel-title-icon" /> Real-time Consultation
          </h3>
        </div>

        {isGeneratingSummary ? (
          <div className="transcript-scroll-area">
            <div className="transcript-empty">
              <Clock size={48} className="transcript-empty-icon animate-pulse" />
              <p style={{ margin: 0, fontWeight: 500 }}>Generating Consultation Summary...</p>
              <p style={{ fontSize: '12px', margin: 0 }}>Processing voice transcripts with AI (max 10s)...</p>
            </div>
          </div>
        ) : callSummary ? (
          <div className="summary-panel">
            <div className="summary-card-wrapper">
              <div className="summary-header">
                <FileText size={22} style={{ color: 'var(--color-primary)' }} />
                <h3 className="summary-title">Consultation Summary</h3>
              </div>
              
              <div className="summary-section">
                <div className="summary-section-title">Patient Profile</div>
                <div className="summary-text" style={{ fontWeight: 600 }}>
                  {callSummary.user.name} ({callSummary.user.phone})
                </div>
              </div>

              <div className="summary-section">
                <div className="summary-section-title">Conversation Summary</div>
                <div className="summary-text">{callSummary.summary}</div>
              </div>

              <div className="summary-section">
                <div className="summary-section-title">User Preferences</div>
                <div className="summary-pref">
                  {callSummary.preferences}
                </div>
              </div>

              <div className="summary-section">
                <div className="summary-section-title">Appointments Status</div>
                <div className="summary-appointments-list">
                  {callSummary.appointments.length === 0 ? (
                    <div style={{ fontSize: '13px', color: 'var(--text-secondary)' }}>No active appointments.</div>
                  ) : (
                    callSummary.appointments.map((appt: any) => (
                      <div key={appt.id} className="summary-appt-item">
                        <div>
                          <strong>{appt.time}</strong> on <strong>{appt.date}</strong>
                          <div style={{ fontSize: '11px', color: 'var(--text-secondary)' }}>
                            {appt.doctor_name} ({appt.doctor_specialty})
                          </div>
                        </div>
                        <span className="appointment-status scheduled" style={{ margin: 0 }}>Booked</span>
                      </div>
                    ))
                  )}
                </div>
              </div>

              <div className="summary-footer">
                Call ended at {new Date(callSummary.timestamp).toLocaleString()}
              </div>

              <button className="btn-new-session" onClick={onResetSession}>
                Start New Session
              </button>
            </div>
          </div>
        ) : !isActiveCall ? (
          <div className="transcript-scroll-area">
            <div className="transcript-empty">
              <Mic size={48} className="transcript-empty-icon" />
              <p style={{ margin: 0, fontWeight: 500 }}>No Active Session</p>
              <p style={{ fontSize: '13px', margin: 0 }}>
                Start a voice consultation to view real-time medical conversation transcription.
              </p>
            </div>
          </div>
        ) : (
          <ActiveTranscripts userProfile={displayProfile} />
        )}
      </div>

      {/* RIGHT PANEL: Profile, Interactive Calendar & Appointments */}
      <div className="panel appointments-panel animate-slide-in-right">
        <div className="profile-card">
          {isEditingProfile ? (
            <form onSubmit={handleManualIdentifySubmit} style={{ width: '100%', display: 'flex', flexDirection: 'column', gap: '8px' }}>
              <div style={{ fontSize: '11px', fontWeight: 700, textTransform: 'uppercase', color: 'var(--color-primary)' }}>
                Confirm Patient Profile
              </div>
              <input
                type="text"
                className="form-input"
                placeholder="Patient Full Name"
                value={manualName}
                onChange={(e) => setManualName(e.target.value)}
                style={{ padding: '8px', fontSize: '13px', background: 'rgba(0,0,0,0.2)' }}
                required
              />
              {manualNameError && <span className="inline-error" style={{ margin: 0, fontSize: '10px' }}>{manualNameError}</span>}
              <input
                type="tel"
                className="form-input"
                placeholder="Phone Number (to sync)"
                value={manualPhone}
                onChange={(e) => setManualPhone(e.target.value)}
                style={{ padding: '8px', fontSize: '13px', background: 'rgba(0,0,0,0.2)' }}
                required
              />
              {manualPhoneError && <span className="inline-error" style={{ margin: 0, fontSize: '10px' }}>{manualPhoneError}</span>}
              <div style={{ display: 'flex', gap: '8px', marginTop: '4px' }}>
                <button
                  type="submit"
                  className="btn-action"
                  style={{ flex: 1, padding: '8px', background: 'var(--color-primary)', border: 'none', color: '#fff', fontSize: '12px' }}
                >
                  Confirm
                </button>
                <button
                  type="button"
                  className="btn-action"
                  onClick={() => setIsEditingProfile(false)}
                  style={{ flex: 1, padding: '8px', fontSize: '12px' }}
                >
                  Cancel
                </button>
              </div>
            </form>
          ) : (
            <>
              <div className="profile-avatar">
                <User size={24} />
              </div>
              <div className="profile-info" style={{ flex: 1 }}>
                <span className="profile-name">{displayProfile.name}</span>
                <span className="profile-phone">{displayProfile.phone}</span>
              </div>
              <button
                onClick={() => {
                  setManualName(userProfile?.name || '');
                  setManualPhone(userProfile?.phone || '');
                  setManualNameError(null);
                  setManualPhoneError(null);
                  setIsEditingProfile(true);
                }}
                style={{
                  background: 'rgba(255,255,255,0.04)',
                  border: '1px solid var(--border-color)',
                  color: 'var(--text-secondary)',
                  padding: '6px 12px',
                  borderRadius: '8px',
                  fontSize: '12px',
                  fontWeight: 500,
                  cursor: 'pointer',
                  transition: 'all 0.2s',
                }}
              >
                {userProfile ? 'Edit' : 'Add Info'}
              </button>
            </>
          )}
        </div>

        {/* Calendar & Doctor Filter Section */}
        <div className="calendar-section">
          <div className="doctor-chips">
            <button
              className={`doctor-chip ${selectedDoctorId === 'all' ? 'active' : ''}`}
              onClick={() => setSelectedDoctorId('all')}
            >
              All
            </button>
            <button
              className={`doctor-chip ${selectedDoctorId === 1 ? 'active' : ''}`}
              onClick={() => setSelectedDoctorId(1)}
            >
              Dr. Jenkins
            </button>
            <button
              className={`doctor-chip ${selectedDoctorId === 2 ? 'active' : ''}`}
              onClick={() => setSelectedDoctorId(2)}
            >
              Dr. Stone
            </button>
            <button
              className={`doctor-chip ${selectedDoctorId === 3 ? 'active' : ''}`}
              onClick={() => setSelectedDoctorId(3)}
            >
              Dr. Vance
            </button>
          </div>

          <div className="days-row">
            {getNextNDays(10).map((day) => (
              <button
                key={day.dateString}
                className={`day-tile ${selectedDate === day.dateString ? 'active' : ''}`}
                onClick={() => setSelectedDate(day.dateString)}
              >
                <span className="day-tile-name">{day.dayName}</span>
                <span className="day-tile-number">{day.dayNumber}</span>
                <span className="day-tile-month">{day.monthName}</span>
              </button>
            ))}
          </div>

          {/* Show available slots for selected date & doctor */}
          <div className="calendar-slots-title">Available Slots ({selectedDate})</div>
          {isLoadingCalendarSlots ? (
            <div style={{ fontSize: '11px', color: 'var(--text-secondary)', textAlign: 'center', padding: '6px' }}>
              Loading slots...
            </div>
          ) : (
            <div className="calendar-slots-grid">
              {filteredCalendarSlots().length === 0 ? (
                <div className="calendar-no-slots">No slots available.</div>
              ) : (
                filteredCalendarSlots().map((slot) => (
                  <button
                    key={slot.id}
                    className="calendar-slot-btn"
                    onClick={() => onBookCalendarSlot(slot.id)}
                  >
                    <strong>{slot.time}</strong>
                    <span style={{ fontSize: '9px', opacity: 0.8 }}>
                      {slot.doctor_name?.split(' ').pop()}
                    </span>
                  </button>
                ))
              )}
            </div>
          )}
        </div>

        <div className="section-label">Your Scheduled Appointments</div>

        <div className="appointments-scroll-area">
          {isLoadingAppointments ? (
            <div style={{ textAlign: 'center', padding: '40px', color: 'var(--text-secondary)' }}>
              Loading appointments...
            </div>
          ) : appointments.length === 0 ? (
            <div className="appointments-empty">
              <CalendarDays size={36} />
              <p style={{ margin: 0, fontWeight: 500 }}>No appointments scheduled</p>
              <p style={{ fontSize: '12px', margin: 0 }}>
                {userProfile 
                  ? 'Ask the voice assistant or select a slot from the calendar to book one.'
                  : 'Start a voice consultation or confirm details above to book appointments.'}
              </p>
            </div>
          ) : (
            appointments.map((appt) => (
              <div
                key={appt.id}
                id={`appt-card-${appt.id}`}
                className={`appointment-card ${highlightedApptId === appt.id ? 'highlighted' : ''}`}
              >
                <div className="appointment-info">
                  <div className="appointment-icon-wrapper">
                    <Calendar size={18} />
                  </div>
                  <div className="appointment-details">
                    <div className="appointment-time">{appt.time}</div>
                    <div className="appointment-date">{appt.date}</div>
                    {appt.doctor_name && (
                      <div style={{ fontSize: '12px', color: 'var(--color-primary)', marginTop: '2px', fontWeight: 500 }}>
                        {appt.doctor_name} ({appt.doctor_specialty})
                      </div>
                    )}
                    <span className={`appointment-status ${appt.status.toLowerCase()}`}>
                      {appt.status}
                    </span>
                  </div>
                </div>
                <div className="appointment-actions">
                  <button
                    className="btn-action btn-action-cancel"
                    onClick={() => onCancelAppointment(appt.id)}
                  >
                    <Trash2 size={13} /> Cancel
                  </button>
                  <button
                    className="btn-action btn-action-reschedule"
                    onClick={() => onOpenReschedule(appt)}
                  >
                    <Clock size={13} /> Reschedule
                  </button>
                </div>
              </div>
            ))
          )}
        </div>
      </div>
    </div>
  );
}

function ActiveVoiceControl({ onEndCall }: { onEndCall: () => void }) {
  const voiceAssistant = useVoiceAssistant();
  const assistantState = voiceAssistant?.state || 'disconnected';
  const audioTrack = voiceAssistant?.audioTrack;
  const videoTrack = voiceAssistant?.videoTrack;

  return (
    <>
      <div className={`orb-container ${videoTrack ? 'has-video' : ''}`} style={{ overflow: 'hidden' }}>
        {videoTrack ? (
          <VideoTrack
            trackRef={videoTrack}
            style={{ width: '100%', height: '100%', objectFit: 'cover', borderRadius: '18px' }}
          />
        ) : (
          <>
            <div
              className={`orb-ring active ${
                assistantState === 'listening' || assistantState === 'speaking' ? 'success' : ''
              }`}
            />
            <div
              className={`orb-core ${
                assistantState === 'listening'
                  ? 'listening'
                  : assistantState === 'thinking'
                  ? 'thinking'
                  : assistantState === 'speaking'
                  ? 'speaking'
                  : ''
              }`}
            >
              <Mic size={40} />
            </div>
          </>
        )}
      </div>

      <div className="audio-visualizer-container">
        {audioTrack ? (
          <BarVisualizer
            state={assistantState}
            trackRef={audioTrack}
            style={{ width: '100%', height: '100%' }}
          />
        ) : (
          <>
            <div className="visualizer-bar" />
            <div className="visualizer-bar" />
            <div className="visualizer-bar" />
            <div className="visualizer-bar" />
            <div className="visualizer-bar" />
          </>
        )}
      </div>

      <div className="call-controls">
        <button className="btn-call btn-call-disconnect" onClick={onEndCall}>
          <PhoneOff size={18} /> End Consultation
        </button>
      </div>
    </>
  );
}

interface OfflineVoiceControlProps {
  isConnecting: boolean;
  onStartCall: () => void;
}

function OfflineVoiceControl({ isConnecting, onStartCall }: OfflineVoiceControlProps) {
  return (
    <>
      <div className="orb-container">
        <div className="orb-ring" />
        <div className="orb-core">
          <MicOff size={40} />
        </div>
      </div>

      <div className="audio-visualizer-container">
        <div className="visualizer-bar" />
        <div className="visualizer-bar" />
        <div className="visualizer-bar" />
        <div className="visualizer-bar" />
        <div className="visualizer-bar" />
      </div>

      <div className="call-controls">
        <button className="btn-call btn-call-connect" disabled={isConnecting} onClick={onStartCall}>
          {isConnecting ? (
            'Connecting...'
          ) : (
            <>
              <Phone size={18} /> Start Voice Consultation
            </>
          )}
        </button>
      </div>
    </>
  );
}

function ActiveTranscripts({ userProfile: _userProfile }: { userProfile: UserProfile }) {
  const rawTranscriptions = useTranscriptions();
  const scrollRef = useRef<HTMLDivElement>(null);
  const transcriptItems = rawTranscriptions || [];
  const room = useRoomContext();

  useEffect(() => {
    if (scrollRef.current) {
      scrollRef.current.scrollTop = scrollRef.current.scrollHeight;
    }
  }, [transcriptItems.length]);

  if (transcriptItems.length === 0) {
    return (
      <div className="transcript-empty">
        <Activity size={48} className="transcript-empty-icon" />
        <p style={{ margin: 0, fontWeight: 500 }}>Say "hello" to begin...</p>
        <p style={{ fontSize: '13px', margin: 0 }}>
          Listening for audio stream. The agent will greet you.
        </p>
      </div>
    );
  }

  return (
    <div className="transcript-scroll-area" ref={scrollRef}>
      {transcriptItems.map((item, idx) => {
        const isAgent = item.participantInfo?.identity !== room.localParticipant?.identity;
        return (
          <div
            key={idx}
            className={`transcript-message ${isAgent ? 'agent' : 'user'} animate-slide-up`}
          >
            <span className="message-sender">{isAgent ? 'Assistant' : 'You'}</span>
            <div className="message-bubble">{item.text}</div>
          </div>
        );
      })}
    </div>
  );
}

export default App;
