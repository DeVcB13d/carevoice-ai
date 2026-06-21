---
name: tavus-api
description: Describe what this skill does and when to use it. Include keywords that help agents identify relevant tasks.
---

<!-- Tip: Use /create-skill in chat to generate content with agent assistance -->

Define the functionality provided by this skill, including detailed instructions and examples# Authentication
Source: https://docs.tavus.io/api-reference/authentication

Generate an API key in the Developer Portal and send it on each request in the `x-api-key` header.

To use the Tavus API, you need an API key to authenticate your requests. This key verifies that requests are coming from your Tavus account.

## Get the API key

1. Go to the <a href="https://platform.tavus.io/">Developer Portal</a> and select **API Key** from the sidebar menu.
2. Click **Create New Key** to begin generating your API key.
3. Enter a name for the key and (optional) specify allowed IP addresses, then click **Create API Key**.
4. Copy your newly created API key and store it securely.

<Warning>
  **Remember that your API key is a secret!**

  Never expose it in client-side code such as browsers or apps. Always load your API key securely from environment variables or a server-side configuration.
</Warning>

## Make Your First Call

Requests go to **`https://tavusapi.com`**. Authenticate with your API key by sending it in the **`x-api-key`** header on every request, as below.

```http theme={null}
x-api-key: <api-key>
```

For example, you are using the [POST - Create Conversation](/api-reference/conversations/create-conversation) endpoint to create a real-time video call session with a Tavus replica. In this scenario, you can send an API request and replace `<api-key>` with your actual API key.

```shell cURL theme={null}
curl --request POST \
  --url https://tavusapi.com/v2/conversations \
  --header 'Content-Type: application/json' \
  --header 'x-api-key: <api-key>' \
  --data '{
  "replica_id": "r90bbd427f71",
  "persona_id": "pdac61133ac5",
  "conversation_name": "Interview User"
}'
```


# Create conversation
Source: https://docs.tavus.io/api-reference/conversations/create-conversation

post /v2/conversations
This endpoint starts a real-time video conversation with your AI replica, powered by a persona that allows it to see, hear, and respond like a human.


<Info>
  For AI agents, use `https://docs.tavus.io/openapi.yaml` for the full HTTP API contract.
</Info>


# Delete Conversation
Source: https://docs.tavus.io/api-reference/conversations/delete-conversation

delete /v2/conversations/{conversation_id}
This endpoint deletes a single conversation by its unique identifier. Use this for destructive data removal. For normal call cleanup when a user leaves or a session is finished, use [End Conversation](/api-reference/conversations/end-conversation) instead.


<Info>
  For AI agents, use `https://docs.tavus.io/openapi.yaml` for the full HTTP API contract.
</Info>


# End Conversation
Source: https://docs.tavus.io/api-reference/conversations/end-conversation

post /v2/conversations/{conversation_id}/end
This endpoint ends a single conversation by its unique identifier. Use this for routine call cleanup when a user leaves or your app no longer needs the room. To destructively remove conversation data, use [Delete Conversation](/api-reference/conversations/delete-conversation).


<Info>
  For AI agents, use `https://docs.tavus.io/openapi.yaml` for the full HTTP API contract.
</Info>


# Get Conversation
Source: https://docs.tavus.io/api-reference/conversations/get-conversation

get /v2/conversations/{conversation_id}
This endpoint returns a single conversation by its unique identifier.


<Info>
  For AI agents, use `https://docs.tavus.io/openapi.yaml` for the full HTTP API contract.
</Info>


# List Conversations
Source: https://docs.tavus.io/api-reference/conversations/get-conversations

get /v2/conversations
This endpoint returns a list of all Conversations created by the account associated with the API Key in use.


<Info>
  For AI agents, use `https://docs.tavus.io/openapi.yaml` for the full HTTP API contract.
</Info>


# Create Document
Source: https://docs.tavus.io/api-reference/documents/create-document

post /v2/documents
Upload documents to your knowledge base for personas to reference during conversations.

<Info>
  For AI agents, use `https://docs.tavus.io/openapi.yaml` for the full HTTP API contract.
</Info>


# Delete Document
Source: https://docs.tavus.io/api-reference/documents/delete-document

delete /v2/documents/{document_id}
Delete a document and its associated data using its unique identifier.


<Info>
  For AI agents, use `https://docs.tavus.io/openapi.yaml` for the full HTTP API contract.
</Info>


# Get Document
Source: https://docs.tavus.io/api-reference/documents/get-document

get /v2/documents/{document_id}
Retrieve detailed information about a specific document using its unique identifier.


<Info>
  For AI agents, use `https://docs.tavus.io/openapi.yaml` for the full HTTP API contract.
</Info>


# List Documents
Source: https://docs.tavus.io/api-reference/documents/get-documents

get /v2/documents
Retrieve a list of documents.


<Info>
  For AI agents, use `https://docs.tavus.io/openapi.yaml` for the full HTTP API contract.
</Info>


# Update Document
Source: https://docs.tavus.io/api-reference/documents/patch-document

patch /v2/documents/{document_id}
Update a document's `document_name` and `tags`.

<Info>
  For AI agents, use `https://docs.tavus.io/openapi.yaml` for the full HTTP API contract.
</Info>


# Recrawl Document
Source: https://docs.tavus.io/api-reference/documents/recrawl-document

post /v2/documents/{document_id}/recrawl
Trigger a recrawl of a website document to fetch fresh content.

<Info>
  For AI agents, use `https://docs.tavus.io/openapi.yaml` for the full HTTP API contract.
</Info>


# Create Guardrails
Source: https://docs.tavus.io/api-reference/guardrails/create-guardrails

post /v2/guardrails
Create a new guardrail. Guardrails provide strict behavioral boundaries that are enforced throughout a conversation.

Attach guardrails to a persona directly via `guardrail_ids` or by tag via `guardrail_tags` on [Create Persona](/api-reference/personas/create-persona).

<Note>
See [Legacy guardrail sets](/api-reference/guardrails/legacy-guardrail-sets).
</Note>


<Info>
  For AI agents, use `https://docs.tavus.io/openapi.yaml` for the full HTTP API contract.
</Info>


# Delete Guardrails
Source: https://docs.tavus.io/api-reference/guardrails/delete-guardrails

delete /v2/guardrails/{guardrail_id}
Delete a single guardrail by its unique identifier. Personas with this guardrail attached via `guardrail_ids` will have the reference removed automatically.


<Info>
  For AI agents, use `https://docs.tavus.io/openapi.yaml` for the full HTTP API contract.
</Info>


# Get Guardrails
Source: https://docs.tavus.io/api-reference/guardrails/get-guardrails

get /v2/guardrails/{guardrail_id}
Retrieve a single guardrail by its unique identifier.


<Info>
  For AI agents, use `https://docs.tavus.io/openapi.yaml` for the full HTTP API contract.
</Info>


# List Guardrails
Source: https://docs.tavus.io/api-reference/guardrails/list-guardrails

get /v2/guardrails
Return a flat list of guardrails owned by the caller. Pass `legacy=false` — recommended for all new integrations.


<Info>
  For AI agents, use `https://docs.tavus.io/openapi.yaml` for the full HTTP API contract.
</Info>


# Patch Guardrails
Source: https://docs.tavus.io/api-reference/guardrails/patch-guardrails

patch /v2/guardrails/{guardrail_id}
Update specific fields of a guardrail using [JSON Patch](https://jsonpatch.com/) operations. Paths must match the **current** document shape — compare against the response from [Get Guardrails](/api-reference/guardrails/get-guardrails) before patching.


<Info>
  For AI agents, use `https://docs.tavus.io/openapi.yaml` for the full HTTP API contract.
</Info>


# Create Objectives
Source: https://docs.tavus.io/api-reference/objectives/create-objectives

post /v2/objectives
This endpoint creates objectives for a persona.


<Info>
  For AI agents, use `https://docs.tavus.io/openapi.yaml` for the full HTTP API contract.
</Info>


# Delete Objective
Source: https://docs.tavus.io/api-reference/objectives/delete-objectives

delete /v2/objectives/{objectives_id}
This endpoint deletes a single objective by its unique identifier.


<Info>
  For AI agents, use `https://docs.tavus.io/openapi.yaml` for the full HTTP API contract.
</Info>


# Get Objective
Source: https://docs.tavus.io/api-reference/objectives/get-objectives

get /v2/objectives/{objectives_id}
This endpoint returns a single objective by its unique identifier.


<Info>
  For AI agents, use `https://docs.tavus.io/openapi.yaml` for the full HTTP API contract.
</Info>


# Get Objectives
Source: https://docs.tavus.io/api-reference/objectives/get-objectives-list

get /v2/objectives
This endpoint returns a list of all objectives.


<Info>
  For AI agents, use `https://docs.tavus.io/openapi.yaml` for the full HTTP API contract.
</Info>


# Patch Objective
Source: https://docs.tavus.io/api-reference/objectives/patch-objectives

patch /v2/objectives/{objectives_id}
This endpoint allows you to update specific fields of an objective using JSON Patch operations.


<Info>
  For AI agents, use `https://docs.tavus.io/openapi.yaml` for the full HTTP API contract.
</Info>


# Overview
Source: https://docs.tavus.io/api-reference/overview

Discover the Tavus API — build a real-time, human-like multimodal video conversation with a replica.

## Getting Started with Tavus APIs

Tavus APIs allow you to create a Conversational Video Interface (CVI), an end-to-end pipeline for real-time video conversations with an AI replica. Each replica is integrated with a persona that enables it to see, hear, and respond like a human.

You can access the API through standard HTTP requests, making it easy to integrate CVI into any application or platform.

<Info>
  For machine-readable API and docs context, use
  `https://docs.tavus.io/openapi.yaml` as the canonical HTTP API contract,
  `https://docs.tavus.io/llms.txt` as the docs page index, and
  `https://docs.tavus.io/llms-full.txt` as the full bundled docs export.
</Info>

### Who Is This For?

This API is for developers looking to add real-time, human-like AI interactions into their apps or services.

### What Can You Do?

Use the end-to-end CVI pipeline to build human-like, real-time multimodal video conversations with these three core components:

<CardGroup>
  <Card title="Persona" icon="heart-pulse" href="/api-reference/personas/create-persona">
    Define the agent’s behavior, tone, and knowledge.
  </Card>

  <Card title="Replica" icon="user-group" href="/api-reference/phoenix-replica-model/create-replica">
    Train a lifelike digital replica from a short video or headshot image.
  </Card>

  <Card title="Conversation" icon="video" href="/api-reference/conversations/create-conversation">
    Create a real-time video call session with your AI replica.
  </Card>
</CardGroup>

A typical path: [Authentication](/api-reference/authentication), then [Create Persona](/api-reference/personas/create-persona), [Create Replica](/api-reference/phoenix-replica-model/create-replica), and [Create Conversation](/api-reference/conversations/create-conversation). For what CVI includes end-to-end, see [What is CVI?](/sections/conversational-video-interface/overview-cvi).


# Create Persona
Source: https://docs.tavus.io/api-reference/personas/create-persona

post /v2/personas
Creates a persona that configures how a replica behaves and sounds in CVI for every conversation that uses that persona.

<Info>
  For AI agents, use `https://docs.tavus.io/openapi.yaml` for the full HTTP API contract.
</Info>


# Delete Persona
Source: https://docs.tavus.io/api-reference/personas/delete-persona

delete /v2/personas/{persona_id}
This endpoint deletes a single persona by its unique identifier.


<Info>
  For AI agents, use `https://docs.tavus.io/openapi.yaml` for the full HTTP API contract.
</Info>


# Get Persona
Source: https://docs.tavus.io/api-reference/personas/get-persona

get /v2/personas/{persona_id}
This endpoint returns a single persona by its unique identifier.


<Info>
  For AI agents, use `https://docs.tavus.io/openapi.yaml` for the full HTTP API contract.
</Info>


# List Personas
Source: https://docs.tavus.io/api-reference/personas/get-personas

get /v2/personas
This endpoint returns a list of all Personas created by the account associated with the API Key in use.


<Info>
  For AI agents, use `https://docs.tavus.io/openapi.yaml` for the full HTTP API contract.
</Info>


# Patch Persona
Source: https://docs.tavus.io/api-reference/personas/patch-persona

patch /v2/personas/{persona_id}
This endpoint allows you to update specific fields of a persona using JSON Patch operations.

<Info>
  For AI agents, use `https://docs.tavus.io/openapi.yaml` for the full HTTP API contract.
</Info>


# Create Replica
Source: https://docs.tavus.io/api-reference/phoenix-replica-model/create-replica

post /v2/replicas
Creates a new replica from a training video or image URL for use in conversations—see [Which training path?](/sections/replica/which-training-path) for preparation, consent, and media requirements.

<Info>
  For AI agents, use `https://docs.tavus.io/openapi.yaml` for the full HTTP API contract.
</Info>


# Delete Replica
Source: https://docs.tavus.io/api-reference/phoenix-replica-model/delete-replica

delete /v2/replicas/{replica_id}
Deletes a Replica by its unique ID; deleted replicas cannot be used in a conversation.

<Info>
  For AI agents, use `https://docs.tavus.io/openapi.yaml` for the full HTTP API contract.
</Info>


# Get Replica
Source: https://docs.tavus.io/api-reference/phoenix-replica-model/get-replica

get /v2/replicas/{replica_id}
This endpoint returns a single Replica by its unique identifier.


<Info>
  For AI agents, use `https://docs.tavus.io/openapi.yaml` for the full HTTP API contract.
</Info>


# List Replicas
Source: https://docs.tavus.io/api-reference/phoenix-replica-model/get-replicas

get /v2/replicas
This endpoint returns a list of all Replicas created by the account associated with the API Key in use.


<Info>
  For AI agents, use `https://docs.tavus.io/openapi.yaml` for the full HTTP API contract.
</Info>


# Rename Replica
Source: https://docs.tavus.io/api-reference/phoenix-replica-model/patch-replica-name

patch /v2/replicas/{replica_id}/name
This endpoint renames a single Replica by its unique identifier.


<Info>
  For AI agents, use `https://docs.tavus.io/openapi.yaml` for the full HTTP API contract.
</Info>


# Create Pronunciation Dictionary
Source: https://docs.tavus.io/api-reference/pronunciation-dictionaries/create-pronunciation-dictionary

post /v2/pronunciation-dictionaries
Create a [pronunciation dictionary](/sections/conversational-video-interface/persona/pronunciation-dictionaries) with custom rules for controlling how words are spoken. Rules are automatically synced to both Cartesia and ElevenLabs so they work regardless of which TTS engine your persona uses.


<Info>
  For AI agents, use `https://docs.tavus.io/openapi.yaml` for the full HTTP API contract.
</Info>


# Delete Pronunciation Dictionary
Source: https://docs.tavus.io/api-reference/pronunciation-dictionaries/delete-pronunciation-dictionary

delete /v2/pronunciation-dictionaries/{dictionary_id}
Permanently delete a pronunciation dictionary and remove it from all linked personas.


<Info>
  For AI agents, use `https://docs.tavus.io/openapi.yaml` for the full HTTP API contract.
</Info>


# Get Pronunciation Dictionary
Source: https://docs.tavus.io/api-reference/pronunciation-dictionaries/get-pronunciation-dictionary

get /v2/pronunciation-dictionaries/{dictionary_id}
Retrieve a pronunciation dictionary by its ID, including all rules.


<Info>
  For AI agents, use `https://docs.tavus.io/openapi.yaml` for the full HTTP API contract.
</Info>


# List Pronunciation Dictionaries
Source: https://docs.tavus.io/api-reference/pronunciation-dictionaries/list-pronunciation-dictionaries

get /v2/pronunciation-dictionaries
List all pronunciation dictionaries for the authenticated user with pagination.


<Info>
  For AI agents, use `https://docs.tavus.io/openapi.yaml` for the full HTTP API contract.
</Info>


# Update Pronunciation Dictionary
Source: https://docs.tavus.io/api-reference/pronunciation-dictionaries/update-pronunciation-dictionary

patch /v2/pronunciation-dictionaries/{dictionary_id}
Update a pronunciation dictionary's name or rules using [JSON Patch](https://jsonpatch.com/) format (RFC 6902). Supported mutable fields are `name` and `rules`.


<Info>
  For AI agents, use `https://docs.tavus.io/openapi.yaml` for the full HTTP API contract.
</Info>


# Generate Video
Source: https://docs.tavus.io/api-reference/video-request/create-video

post /v2/videos
This endpoint generates a new video using a Replica and either a script or an audio file.


<Info>
  For AI agents, use `https://docs.tavus.io/openapi.yaml` for the full HTTP API contract.
</Info>


# Delete Video
Source: https://docs.tavus.io/api-reference/video-request/delete-video

delete /v2/videos/{video_id}
This endpoint deletes a single video by its unique identifier.


<Info>
  For AI agents, use `https://docs.tavus.io/openapi.yaml` for the full HTTP API contract.
</Info>


# Get Video
Source: https://docs.tavus.io/api-reference/video-request/get-video

get /v2/videos/{video_id}
This endpoint returns a single video by its unique identifier.


<Info>
  For AI agents, use `https://docs.tavus.io/openapi.yaml` for the full HTTP API contract.
</Info>


# List Videos
Source: https://docs.tavus.io/api-reference/video-request/get-videos

get /v2/videos
This endpoint returns a list of all Videos created by the account associated with the API Key in use.


<Info>
  For AI agents, use `https://docs.tavus.io/openapi.yaml` for the full HTTP API contract.
</Info>


# Rename Video
Source: https://docs.tavus.io/api-reference/video-request/patch-video-name

patch /v2/videos/{video_id}/name
This endpoint renames a single video by its unique identifier.


<Info>
  For AI agents, use `https://docs.tavus.io/openapi.yaml` for the full HTTP API contract.
</Info>


# List Voices
Source: https://docs.tavus.io/api-reference/voices/list-voices

get /v2/voices
Returns available stock **`voice_name`** values and their linked **replica** metadata. When you [Create Replica](/api-reference/phoenix-replica-model/create-replica) with **`train_image_url`** (image-to-replica), **`voice_name`** is required—use this list to pick a valid slug and to preview options.


<Info>
  For AI agents, use `https://docs.tavus.io/openapi.yaml` for the full HTTP API contract.
</Info>


# Agents & automation
Source: https://docs.tavus.io/sections/agents-and-automation

How to access machine-readable docs and API artifacts for developers, IDEs, and automation - llms.txt, OpenAPI, Agent Skills, and MCP.

**How do I point my agent, IDE, or automation at Tavus’s documentation and HTTP APIs?** This guide helps you pick the right artifact for your workflow.

## Documentation bundle reference

| Artifact          | Role                                                                                                                                                      | URL                                   |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------- |
| **llms.txt**      | Curated directory of doc URLs for selective fetch                                                                                                         | `https://docs.tavus.io/llms.txt`      |
| **llms-full.txt** | Full bundled text export for offline or bulk ingest                                                                                                       | `https://docs.tavus.io/llms-full.txt` |
| **openapi.yaml**  | HTTP API contract (paths, request/response schemas, security schemes)                                                                                     | `https://docs.tavus.io/openapi.yaml`  |
| **skill.md**      | Agent-oriented capability summary ([Agent Skills](https://agentskills.io) conventions)                                                                    | `https://docs.tavus.io/skill.md`      |
| **MCP**           | Hosted Model Context Protocol server: search plus fetch full pages from the indexed docs site (see [Model Context Protocol](#model-context-protocol-mcp)) | `https://docs.tavus.io/mcp`           |

## When to use what

* **MCP:** Interactive tools that need live search and current page retrieval against the indexed site.
* **llms-full.txt:** Bulk or offline ingestion; snapshot of doc text (not a substitute for OpenAPI).
* **openapi.yaml:** Source of truth for HTTP APIs (requests, responses, auth headers); agents should not invent endpoints that contradict it.
* **llms.txt / selective fetches:** Discovery and pulling specific pages when you do not want the full bundle.
* **skill.md:** Compact capability orientation for agents; still point to OpenAPI and deep docs for details.

## Model Context Protocol (MCP)

An MCP endpoint is available for this documentation site. Configure clients that support HTTP transport with:

```json theme={null}
{
  "url": "https://docs.tavus.io/mcp",
  "transport": "http"
}
```

Use MCP when the tool needs **live** search and retrieval against the **current** indexed documentation, not a frozen file export.


# Changelog
Source: https://docs.tavus.io/sections/changelog/changelog



<Update label="June 12">
  ## Enhancements

  * **Meet Rivian, Tiffany, and Brian:** Our 3 new stock replicas!
  * **Improved Image to Replica uploading flow:** Get more detailed and accurate errors before training submission.
</Update>

<Update label="June 5">
  ## New Features

  * **Guardrails as first-class primitives:** Guardrails are now standalone resources that can be created, edited, and reused across multiple personas. Compose individual guardrails into sets via `guardrail_tags`. [Learn more](/sections/conversational-video-interface/guardrails)
  * **Choose your delivery channel:** Guardrail violations can now be delivered via [Interaction Events](/sections/conversational-video-interface/interactions-protocols/overview) (in-call `app-message`) or [Webhooks](/sections/webhooks-and-callbacks#guardrail-callbacks) (server-side `callback_url`) — or both.
  * **`guardrail_uuid` on violations:** Triggered events and callbacks now include `guardrail_uuid`, so you can identify exactly which individual guardrail was violated.
</Update>

<Update label="June 3">
  ## New Features

  * **Azure TTS support:** Azure is now available as a TTS engine, expanding language coverage for multilingual and localized voice output. [Learn more](/sections/conversational-video-interface/persona/tts)
</Update>

<Update label="May 22">
  ## New Features

  * **Individually addressable guardrails:** Guardrails are now first-class resources. Create, attach, edit, and delete each guardrail independently via the [Guardrails API](/api-reference/guardrails/create-guardrails). Bundle guardrails by tag and reference them on a persona via `guardrail_ids` or `guardrail_tags`. [Learn more](/sections/conversational-video-interface/guardrails)
  * **Node.js plugin support for LiveKit integration:** The LiveKit Agents integration now supports Node.js via the `@livekit/agents-plugin-tavus` plugin, in addition to Python. Install with `npm install @livekit/agents @livekit/agents-plugin-tavus`. [Learn more](/sections/integrations/livekit#node-js)
  * **Real-time event timestamps:** Every interaction event (`conversation.utterance`, `conversation.started_speaking`, etc.) now carries a `timestamp` field delivered in real time on the respective Interaction event. <a href="https://docs.tavus.io/sections/conversational-video-interface/interactions-protocols/overview">Learn more</a>
  * **Transcript utterance timestamps:** End-of-call transcripts now carry per-turn timing. The [`application.transcription_ready`](https://docs.tavus.io/sections/webhooks-and-callbacks#conversation-callbacks) webhook (and the same payload nested under `events` in the verbose [`GET /conversations/{id}?verbose=true`](https://docs.tavus.io/api-reference/conversations/get-conversation) response) now includes `timestamp` (Unix epoch float, seconds — same field name as live interaction events), `seconds_from_start`, `duration` (seconds, float — same field name as `conversation.stopped_speaking.duration`), and `inference_id` (on assistant turns) on each transcript entry.

  ## Enhancements

  * **New, and more detailed, error messages when a replica fails:** [Learn more](/sections/errors-and-status-details#replica-training-errors)
</Update>

<Update label="May 20">
  ## New Features

  * **AI Image Fixer API support:** [Create Replica](/api-reference/phoenix-replica-model/create-replica) now accepts an `auto_fix_training_image` property. Set it to `true` to use Tavus's AI Image Fixer to instantly fix any uploaded image to fit our requirements, eliminating the need for editing or recapturing photos. [Learn more](/sections/replica/train-with-an-image#ai-image-fixer)
</Update>

<Update label="May 12">
  ## New Features

  * **AI Image Fixer:** Instantly fix any uploaded image to fit our requirements, eliminating the need for editing or recapturing photos.
</Update>

<Update label="May 11">
  ## New Features

  * **Frame Checker (Video to Replica):** Get instant feedback, before recording, on whether your camera setup meets our requirements.

  ## Enhancements

  * **Less footage required (Video to Replica):** We now only require 1 minute of video, down from the 2 minutes previously needed.
  * **Simpler in-portal recording flow (Video to Replica):** A streamlined recording experience in the portal to help you capture high-quality recordings.
</Update>

<Update label="May 6">
  ## New Features

  * **Image to Replica:** Build a replica from a single still. Drop in a photo, illustration, or brand mascot.
</Update>

<Update label="May 8">
  ## New Features

  * **Voice Activity Detector improvements:** Resulting in a smoother conversational experience in noisy environments. This is automatically rolled out to all users.
  * **Expanded Recording Storage Support:** Conversation recordings can now be delivered to Google Cloud Storage (GCP) and Azure Blob Storage, in addition to AWS S3. <a href="https://docs.tavus.io/sections/conversational-video-interface/quickstart/conversation-recordings#set-up-your-storage">Learn more</a>

  ## Enhancements

  * **Tavus Components Library Updates:** Improved audio-video sync, plus new chat components and closed captions with streaming support. <a href="https://docs.tavus.io/sections/conversational-video-interface/component-library/components">Learn more</a>
</Update>

<Update label="May 1">
  ## New Features

  * **Wake Phrase:** Personas can now stay silent until they hear a specific phrase, similar to how voice assistants like Siri or Alexa work. Configure it via the `wake_phrase` parameter in the Conversational Flow layer. The persona still hears everything that is said and responds with full conversation history once the wake phrase is detected. <a href="https://docs.tavus.io/sections/conversational-video-interface/persona/conversational-flow#5-wake_phrase">Learn more</a>
</Update>

<Update label="April 30">
  ## New Features

  * **Idle Engagement:** Replicas can now proactively re-engage by speaking to the user after a period where the user is silent. Eagerness of this feature can be configured via the `idle_engagement` parameter in the Conversational Flow layer. <a href="https://docs.tavus.io/sections/conversational-video-interface/persona/conversational-flow#6-idle_engagement">Learn more</a>
</Update>

<Update label="April 29">
  ## New Features

  * **Speaking Events:** Two new events — `conversation.started_speaking` and `conversation.stopped_speaking` — fire for both the replica and the user with a `role` field (`"replica"` or `"user"`) identifying the speaker. `conversation.stopped_speaking` includes an `interrupted` boolean and a `duration` field (in seconds). <a href="https://docs.tavus.io/sections/event-schemas/conversation-started-stopped-speaking">Learn more</a>
  * **Conversation Diagnostics:** A new diagnostics surface for inspecting what happened in a conversation — including packet loss, network connection, FPS, and more — designed to make debugging significantly faster. Click on any conversation in the Developer Portal to access its diagnostics page.
</Update>

<Update label="April 17">
  ## Enhancements

  * **Non-Interruptible Custom Greetings:** Custom greetings now finish entirely before users can interrupt speech. Previously, participants could talk over a `custom_greeting`; now the replica completes the greeting before it begins listening. <a href="https://docs.tavus.io/sections/conversational-video-interface/faq#general-tavus-q-and-a:can-participants-interrupt-the-replicas-greeting">Learn more</a>
  * **Improved Turn-Taking Latency:** Significant TTS optimizations reduce turn-taking latency, resulting in faster and more natural back-and-forth during conversations.
</Update>

<Update label="April 10">
  ## New Features

  * **Streaming Utterance Event:** A new `conversation.utterance.streaming` event progressively reports what has been said during a conversation turn for both replica and user utterances. Use it to power closed captioning and build accurate transcripts — especially when a user interrupts the replica, since the streaming event reflects only the words actually spoken rather than the full LLM response. <a href="https://docs.tavus.io/sections/event-schemas/conversation-utterance-streaming">Learn more</a>
  * **Pronunciation Dictionaries:** Define custom pronunciation rules so your persona says brand names, technical terms, acronyms, and foreign words exactly right. Choose between simple alias substitution (e.g., "Tavus" → "TAH-vus") or precise IPA phonetic notation. Create a dictionary once and attach it to a persona via the TTS layer — any updates automatically propagate to all linked personas with zero extra latency at conversation time. <a href="https://docs.tavus.io/sections/conversational-video-interface/persona/pronunciation-dictionaries">Learn more</a>
</Update>

<Update label="April 7">
  ## New Features

  * **Voice Isolation:** Filter background noise from participant audio to improve conversation quality. Configure it via the `voice_isolation` parameter in the Conversational Flow layer. <a href="https://docs.tavus.io/sections/conversational-video-interface/persona/conversational-flow#4-voice_isolation">Learn more</a>
</Update>

<Update label="April 3">
  ## Changes

  * **Chat Interrupt History:** Personas now know when they have been interrupted. This allows the persona to pick back up where it left off, and also improves objectives adherence.
</Update>

<Update label="March 27">
  ## New Features

  * **Expanded ASR Model Selection:** You can now choose from five specialized speech-to-text engines via the `stt_engine` parameter. New models include `tavus-parakeet`, `tavus-soniox`, `tavus-whisper`, and `tavus-deepgram-medical`. Use `tavus-auto` to automatically route to the best model for each conversation. <a href="https://docs.tavus.io/sections/conversational-video-interface/persona/stt">Learn more</a>
</Update>

<Update label="March 19">
  ## Enhancements

  * **30% Faster Phoenix-4 Boot Time:** Phoenix-4 conversations now boot 30% faster, significantly reducing the time from conversation creation to readiness.

  ## Changes

  * **`conversation.replica_interrupted` Event Removed:** The `conversation.replica_interrupted` application message has been removed from interaction events. This event was deprecated in a previous backend update. Use `conversation.replica.stopped_speaking` with the `interrupted: true` property to detect interruptions instead.
  * **`duration` and `interrupted` Fields on Replica Stopped Speaking:** The `conversation.replica.stopped_speaking` event now includes a `duration` field (how long the replica spoke in seconds) and an `interrupted` field (`true`/`false`) indicating whether the replica was interrupted by the user. <a href="https://docs.tavus.io/sections/event-schemas/conversation-replica-started-stopped-speaking">Learn more</a>
</Update>

<Update label="March 17">
  ## New Features

  * **Event Ordering and Turn Tracking:** All server-broadcasted interaction events now include `seq` and `turn_idx` fields. `seq` is a globally monotonic sequence number for ordering events that may arrive out of order, and `turn_idx` groups related events from the same conversation turn. <a href="https://docs.tavus.io/sections/conversational-video-interface/interactions-protocols/overview#event-ordering-and-turn-tracking">Learn more</a>
</Update>

<Update label="March 11">
  ## Enhancements

  * **30% Faster Phoenix-4 Boot Time:** Phoenix-4 conversations now boot 30% faster, significantly reducing the time from conversation creation to readiness.
</Update>

<Update label="March 5">
  ## Enhancements

  * **EU ElevenLabs BYOK Support:** Customers can now bring their own ElevenLabs API key from EU-region accounts.
</Update>

<Update label="February 19">
  ## Enhancements

  * **Improved Knowledge Base Retrieval:** Optimized underlying infrastructure to improve utterance to utterance response times, particularly when `rag_search_quality` is set to `quality`.
</Update>

<Update label="February 17">
  ## New Features

  * **Expanded Tavus-Hosted LLM Selection:** Added new Tavus-hosted LLM options including models from Gemini, Claude, and GPT families. `tavus-gpt-oss` is recommended as the default. Legacy models `tavus-gpt-4.1`, `tavus-gpt-4o`, and `tavus-gpt-4o-mini` are now deprecated. <a href="https://docs.tavus.io/sections/conversational-video-interface/persona/llm#tavus-hosted-models">Learn more →</a>
  * **Visual RAG:** CVI now supports visual retrieval-augmented generation. Upload custom image explanations that are matched and queried via vision embeddings, giving your persona richer visual context during conversations.
</Update>

<Update label="February 12">
  ## Changes

  * **Persona**`context`**Field Deprecated:**  The `context` field has been deprecated in favor of a unified `system_prompt` field. Existing `context` values have been automatically merged into system prompts. The API remains backward compatible, but we recommend using **only** `system_prompt` going forward.
</Update>

<Update label="February 11">
  ## New Features

  * **Raven-1 Perception Model:** Introduced Raven-1, a multimodal perception model with audio emotion analysis and enhanced visual awareness. Raven-1 captures user emotion from audio in real time (sub-100ms audio perception latency), enabling personas to respond with greater emotional intelligence. The model is now the default for all new personas. Enable it by setting `perception_model_name` in your persona configuration. <a href="https://www.tavus.io/post/raven-1-bringing-emotional-intelligence-to-artificial-intelligence">Learn more →</a>
  * **Private Rooms:** Require authentication to join conversations for enhanced security. When enabled, we return a JWT meeting token that users must include when entering the room. <a href="https://docs.tavus.io/sections/conversational-video-interface/conversation/customizations/private-rooms">Learn more</a>
</Update>

<Update label="February 9">
  ## Enhancements

  * **Upgraded Transcription Engine:** Upgraded transcription engine with 3x improvements in word error rates (WER).
</Update>

<Update label="January 17">
  ## New Features

  * **Website Crawling for Knowledge Base:** You can now enable link crawling when creating knowledge base documents. Configure crawl `depth` and `max_pages` to automatically discover and ingest content from linked pages. Additionally, existing crawled documents can now be recrawled to keep knowledge base content up to date.
</Update>

<Update label="January 8">
  ## Changes

  * **PlayHT TTS Removed:** PlayHT has been fully removed as a supported TTS engine. All personas previously using PlayHT should migrate to Cartesia or ElevenLabs.
</Update>

<Update label="December 18">
  ## New Features

  * **Hard Delete for Conversations:** Conversations can now be permanently deleted via the API using the `hard=true` query parameter. Use this for GDPR compliance or data cleanup workflows.

  ## Enhancements

  * **Default TTS Model Updated to Sonic-3:** The default text-to-speech model has been updated to Sonic-3 across all new personas, delivering improved voice quality and naturalness.
  * **LiveKit Connection Stability:** Extensive reliability improvements to the LiveKit-based transport layer, including fixes for connection timeouts, track publishing hangs, event loop starvation, and ping timeout issues.

  ## Changes

  * **Default LLM Migrated to `tavus-gpt-oss`:** The default LLM for all new personas is now `tavus-gpt-oss`. All remaining `tavus-llama-4` personas have been automatically migrated. Legacy Tavus-Llama model references have been removed.
</Update>

<Update label="November 27">
  ## New Features

  * **LLM Temperature & Top-P Parameters:** You can now configure `temperature` and `top_p` parameters for both Tavus-hosted LLMs and custom LLMs via the `extra_body` field in your persona's LLM configuration. <a href="https://docs.tavus.io/sections/conversational-video-interface/persona/llm#4-extra-body">Learn more →</a>

  ## Enhancements

  * **Text Echo Language Accuracy:** Text echoes now correctly use the input language for conversion, improving accuracy in multilingual conversations.
</Update>

<Update label="September 17">
  ## New Features

  * **Test Mode for Conversations:** You can now start conversations in test mode, where the replica does not join. Validate your setup, integrations, and conversational flows without incurring costs or using concurrency slots. Set `test_mode: true` when creating a conversation. <a href="https://docs.tavus.io/api-reference/conversations/create-conversation#body-test-mode">Learn more →</a>
</Update>

<Update label="September 7">
  ## Enhancements

  * **Fuzzy Search for Personas:** Search now supports fuzzy matching for personas, allowing users to find results based on partial matches of UUIDs or names.
</Update>

<Update label="August 15">
  ## New Features

  * **Memories:** CVI now remembers context across conversations. Every conversation builds on the last with full context and time/date awareness, enabling use cases like adaptive tutoring, mentorship, and recurring consultations. <a href="https://docs.tavus.io/sections/conversational-video-interface/memories">Learn more →</a>
  * **Knowledge Base (RAG):** Bring your own data to conversations instantly. Upload documents or links and get grounded answers with \~30ms retrieval latency. Power AI recruiters, support agents, travel guides, and more with domain-specific knowledge. <a href="https://docs.tavus.io/sections/conversational-video-interface/knowledge-base">Learn more →</a>
  * **Objectives & Guardrails:** Define clear goals, branching logic, and measurable outcomes for your personas while keeping conversations safe, compliant, and on-brand. Ideal for complex workflows and regulated industries. <a href="https://docs.tavus.io/sections/conversational-video-interface/persona/objectives">Learn more →</a>
  * **Persona Builder:** A guided creation flow in the Developer Portal to shape AI personas with goals, behaviors, and style — then test or launch within minutes.
</Update>

<Update label="July 28">
  ## New Features

  * **Events Console:** A new events console in the Developer Portal lets you monitor everything happening during a conversation in real time — from message flows to system activity.
  * **Conversation Transcripts & Perception Analysis:** View full conversation details directly in the Developer Portal, including transcripts with speaker roles and perception analysis showing how your AI persona sees, hears, and responds.
</Update>

<Update label="July 25">
  ## New Features

  * **Persona Layer Controls:** Enable or disable layers like Sparrow directly within a Persona and adjust sensitivity settings in real time from the Developer Portal side panel.
  * **Persona Editing in Developer Portal:** We've added new editing capabilities to help you refine your Personas more efficiently. You can now update system prompt, context, and layers directly in our Developer Portal, plus duplicate existing Personas to quickly create variations or use them as starting points for new projects. Find these new features in your Persona Library at platform.tavus.io.
</Update>

<Update label="July 24">
  ## Enhancements

  * **Interaction Events Playground Improvements:** Major updates to the Interaction Events Playground including correct `properties.context` format and append vs overwrite toggle.
</Update>

<Update label="July 23">
  ## New Features

  * **Multilingual Settings in Developer Portal:** You can now specify the language of a conversation directly in the Developer Portal, including a new multilingual option for dynamic, real-world interactions.
</Update>

<Update label="July 22">
  ## New Features

  * **Llama 4 Support:** Your persona just got even smarter, thanks to Meta's Llama 4 model 🧠 You can start using Llama 4 by specifying `tavus-llama-4` for the LLM `model` value when creating a new persona or updating an existing one. Click <a href="https://docs.tavus.io/sections/conversational-video-interface/persona/llm#tavus-hosted-models">here</a>

    to learn more!
</Update>

<Update label="July 15">
  ## New Features

  * **React Component Library:** Developers can build with Tavus even faster now with our pre-defined components 🚀 Click <a href="https://docs.tavus.io/sections/conversational-video-interface/component-library/overview">here</a>

    to learn more!
</Update>

<Update label="June 27">
  ## New Features

  * **Multilingual Conversation Support:** CVI now supports dynamic multilingual conversations through automatic language detection. Set `properties.language` to "multilingual" and CVI will automatically detect the user's spoken language and respond in the same language using ASR technology.
  * **Audio-Only Mode:** CVI now supports audio-only conversations with advanced perception (powered by Raven) and intelligent turn-taking (powered by Sparrow-1). Set `audio_only=true` in your create conversation request to enable streamlined voice-first interactions.
</Update>

<Update label="June 20">
  ## Enhancements

  * **Fixed CVI responsiveness issue:** Resolved an issue where CVI would occasionally ignore very brief user utterances. All user inputs, regardless of length, now receive consistent responses.
  * **Expanded tavus-llama-4 context window:** Increased maximum context window to 32,000 tokens. For optimal performance and response times, we recommend staying under 25,000 tokens.
</Update>

<Update label="June 3">
  ## Enhancements

  * Reduced conversation boot time by 58% (p50).
</Update>

<Update label="May 28">
  ## Changes

  * Added a new recording requirement to <a href="/sections/replica/train-with-a-video">Training from a video</a>

    : Start the talking segment with a big smile.

  ## Enhancements

  * Added <a href="/sections/event-schemas/conversation-echo">echo</a>

    and <a href="/sections/event-schemas/conversation-respond">respond</a>

    events to conversational context.
</Update>

<Update label="May 17">
  ## Enhancements

  * **Major Phoenix 3 Enhancements for CVI**:
    * Increased frame rate from 27fps to 32fps, significantly boosting smoothness.
    * Reduced Phoenix step's warm boot time by 60% (from 5s to 2s).
    * Lipsync accuracy improved by \~22% based on AVSR metric.
    * Resolved blurriness and choppiness at conversation start.
    * Enhanced listening mode with more natural micro expressions (eyebrow movements, subtle gestures).
    * Greenscreen mode speed boosted by an additional \~1.5fps.
  * **Enhanced CVI Audio Quality**: Audio clicks significantly attenuated, providing clearer conversational audio.
  * **Phoenix 3 Visual Artifacts Fix**: Resolved visual artifacts in 4K videos on Apple devices, eliminating black spot artifacts in thumbnails.
</Update>

<Update label="May 9">
  ## New Features

  * Launched <a href="https://www.tavus.io/post/building-real-time-ai-video-agents-with-livekit-and-tavus">LiveKit Integration</a>

    : With Tavus video agents now integrated into LiveKit, you can add humanlike video responses to your voice agents in seconds.
  * <a href="https://docs.tavus.io/api-reference/personas/patch-persona">Persona API</a>

    : Enabled patch updates to personas.

  ## Enhancements

  * Resolved TTS (Cartesia) stability issues and addressed hallucination.
  * **Phoenix 3 Improvements**:
    * Fixed blinking/jumping issues and black spots in videos.
    * FPS optimization to resolve static and audio crackling.
</Update>

<Update label="April">
  ## Enhancements

  * **Replica API**:
    * Enhanced Error Messaging for Training Videos.
    * Optimized Auto QA for Training Videos.
</Update>


# Blocks
Source: https://docs.tavus.io/sections/conversational-video-interface/component-library/blocks

High-level component compositions that combine multiple UI elements into complete interface layouts

Blocks are composed React layouts generated by `npx @tavus/cvi-ui@latest add ...`. They are copied into your app, so import paths are relative to your generated component directory.

| Block                         | Add command                                                          | Import path pattern                         | Props                                                                      | Required context       | Generated location pattern                                                            |
| ----------------------------- | -------------------------------------------------------------------- | ------------------------------------------- | -------------------------------------------------------------------------- | ---------------------- | ------------------------------------------------------------------------------------- |
| `Conversation` full layout    | `npx @tavus/cvi-ui@latest add conversation-01` or `add conversation` | `<components-path>/components/conversation` | `conversationUrl: string`, `onLeave: () => void`                           | `CVIProvider` ancestor | `<components-path>/components/conversation.*` plus supporting components/hooks/styles |
| `Conversation` minimal layout | `npx @tavus/cvi-ui@latest add conversation-02`                       | `<components-path>/components/conversation` | `conversationUrl: string`, `onLeave: () => void`                           | `CVIProvider` ancestor | `<components-path>/components/conversation.*` plus supporting components/hooks/styles |
| `HairCheck`                   | `npx @tavus/cvi-ui@latest add hair-check-01`                         | `<components-path>/components/hair-check`   | `isJoinBtnLoading: boolean`, `onJoin: () => void`, `onCancel?: () => void` | `CVIProvider` ancestor | `<components-path>/components/hair-check.*` plus device hooks/styles                  |

<Note>
  The docs below use relative imports such as `./components/cvi/components/conversation`. Replace the prefix with the components path configured in your generated `cvi-components.json`.
</Note>

### Conversation block

The Conversation component provides a complete video chat interface for one-to-one conversations with AI replicas. Two variants are available: `conversation-01` (full-featured, default) and `conversation-02` (minimal).

#### conversation-01 (full-featured, default)

```bash theme={null}
npx @tavus/cvi-ui@latest add conversation-01
```

<Tabs>
  <Tab title="Description">
    The default `Conversation` block — a full-featured video chat surface for one-to-one conversations with AI replicas.

    **Features:**

    * **Main Video Display**: Large video area showing the AI replica or screen share
    * **Top-right Self-View**: Square self-view preview pinned to the top-right of the main video
    * **Chat**: Slide-in chat side panel with toggle button (built on the [Chat](/sections/conversational-video-interface/component-library/components#chat) module)
    * **Closed Captions**: Live captions overlay with toggle button (built on the [Closed Captions](/sections/conversational-video-interface/component-library/components#closed-captions) module)
    * **Screen Sharing**: Automatic switching between replica video and screen share
    * **Animated Connect / Leave States**: Animated transitions when joining and leaving the call
    * **Device Controls**: Integrated microphone, camera, and screen share controls
    * **Error Handling**: Graceful handling of camera/microphone permission errors
    * **Responsive Layout**: Adaptive design for different screen sizes

    **Props:**

    * `conversationUrl` (string): Daily.co room URL for joining
    * `onLeave` (function): Callback when user leaves the conversation
  </Tab>

  <Tab title="Code">
    ```tsx theme={null}
    import { Conversation } from './components/cvi/components/conversation';
    ```

    ```tsx theme={null}
    <Conversation
      conversationUrl={conversationUrl}
      onLeave={() => handleLeaveCall()}
    />
    ```
  </Tab>
</Tabs>

Preview

<Frame>
  <img alt="Conversation Block Preview" />
</Frame>

#### conversation-02 (minimal)

```bash theme={null}
npx @tavus/cvi-ui@latest add conversation-02
```

<Tabs>
  <Tab title="Description">
    A minimal `Conversation` block — video plus the essential device and leave controls, without chat or captions. Use this when you want to compose your own UI around the call surface.

    **Features:**

    * **Main Video Display**: Large video area showing the AI replica or screen share
    * **Self-View Preview**: Small preview window showing local camera feed
    * **Device Controls**: Microphone, camera, and screen share toggle buttons
    * **Leave Button**: Disconnects from the call and fires `onLeave`
    * **Animated Connect / Leave States**: Animated transitions when joining and leaving the call
    * **Error Handling**: Graceful handling of camera/microphone permission errors
    * **Responsive Layout**: Adaptive design for different screen sizes

    **Props:**

    * `conversationUrl` (string): Daily.co room URL for joining
    * `onLeave` (function): Callback when user leaves the conversation
  </Tab>

  <Tab title="Code">
    ```tsx theme={null}
    import { Conversation } from './components/cvi/components/conversation';
    ```

    ```tsx theme={null}
    <Conversation
      conversationUrl={conversationUrl}
      onLeave={() => handleLeaveCall()}
    />
    ```
  </Tab>
</Tabs>

Preview

<Frame>
  <img alt="Conversation 02 Block Preview" />
</Frame>

### Hair Check

The HairCheck component provides a pre-call interface for users to test and configure their audio/video devices before joining a video chat.

```bash theme={null}
npx @tavus/cvi-ui@latest add hair-check-01
```

<Tabs>
  <Tab title="Description">
    The `HairCheck` component provides a pre-call interface for users to test and configure their audio/video devices before joining a video chat.

    **Features:**

    * **Device Testing**: Live preview of camera feed with mirror effect
    * **Permission Management**: Handles camera and microphone permission requests
    * **Device Controls**: Integrated microphone and camera controls
    * **Join Interface**: Call-to-action button to join the video chat
    * **Responsive Design**: Works on both desktop and mobile devices

    **Props:**

    * `isJoinBtnLoading` (boolean): Shows loading state on join button
    * `onJoin` (function): Callback when user clicks join
    * `onCancel` (function, optional): Callback when user cancels
  </Tab>

  <Tab title="Code">
    ```tsx theme={null}
    import { HairCheck } from './components/cvi/components/hair-check';
    ```

    ```tsx theme={null}
    <HairCheck
      isJoinBtnLoading={isLoading}
      onJoin={handleJoinCall}
      onCancel={handleCancel}
    />
    ```
  </Tab>
</Tabs>

Preview

<Frame>
  <img alt="Haircheck Block Preview" />
</Frame>


# Components
Source: https://docs.tavus.io/sections/conversational-video-interface/component-library/components

Learn about our pre-built React components to accelerate integrating the Tavus Conversational Video Interface (CVI) into your application.

These pages document **installable** UI pieces from **`@tavus/cvi-ui`** (`npx @tavus/cvi-ui@latest add …`). Wrap your app with **`CVIProvider`** so Daily’s React context and hooks work under this tree. For composed layouts see [Blocks](/sections/conversational-video-interface/component-library/blocks), for state hooks see [Hooks](/sections/conversational-video-interface/component-library/hooks), and for init + embed flows see [Embed CVI](/sections/integrations/embedding-cvi).

| Module            | Add command                                    | Import path pattern                            | Exports                                                            | Props / parameters                               | Required context                                           | Generated location pattern                       |
| ----------------- | ---------------------------------------------- | ---------------------------------------------- | ------------------------------------------------------------------ | ------------------------------------------------ | ---------------------------------------------------------- | ------------------------------------------------ |
| `cvi-provider`    | `npx @tavus/cvi-ui@latest add cvi-provider`    | `<components-path>/components/cvi-provider`    | `CVIProvider`                                                      | `children: ReactNode`                            | None; this creates the Daily provider context              | `<components-path>/components/cvi-provider.*`    |
| `audio-wave`      | `npx @tavus/cvi-ui@latest add audio-wave`      | `<components-path>/components/audio-wave`      | `AudioWave`                                                        | `id: string` participant/session ID              | `CVIProvider` ancestor and active Daily call               | `<components-path>/components/audio-wave.*`      |
| `device-select`   | `npx @tavus/cvi-ui@latest add device-select`   | `<components-path>/components/device-select`   | `MicSelectBtn`, `CameraSelectBtn`, `ScreenShareButton`             | No component props                               | `CVIProvider` ancestor and active Daily call               | `<components-path>/components/device-select.*`   |
| `media-controls`  | `npx @tavus/cvi-ui@latest add media-controls`  | `<components-path>/components/media-controls`  | `MicToggleButton`, `CameraToggleButton`, `ScreenShareButton`       | No component props                               | `CVIProvider` ancestor and active Daily call               | `<components-path>/components/media-controls.*`  |
| `closed-captions` | `npx @tavus/cvi-ui@latest add closed-captions` | `<components-path>/components/closed-captions` | `ClosedCaptionsProvider`, `ClosedCaptionsButton`, `ClosedCaptions` | Provider: `children`, `defaultEnabled?: boolean` | `CVIProvider`; wrap caption UI in `ClosedCaptionsProvider` | `<components-path>/components/closed-captions.*` |
| `chat`            | `npx @tavus/cvi-ui@latest add chat`            | `<components-path>/components/chat`            | `ChatProvider`, `ChatButton`, `ChatPanel`                          | Provider: `children`, `defaultOpen?: boolean`    | `CVIProvider`; wrap chat UI in `ChatProvider`              | `<components-path>/components/chat.*`            |

<Note>
  `CVIProvider` is the React wrapper that makes Daily React context available. Components and hooks that read call state must render under it.
</Note>

### CVI Provider

The `CVIProvider` component wraps your app with the Daily.co provider context, enabling all Daily React hooks and components to function.

```bash theme={null}
npx @tavus/cvi-ui@latest add cvi-provider
```

<Tabs>
  <Tab title="Description">
    The `CVIProvider` component wraps your app with the Daily.co provider context, enabling all Daily React hooks and components to function.

    **Features:**

    * Provides Daily.co context to all child components
    * Required for using Daily React hooks and video/audio components
    * Simple wrapper for app-level integration

    **Props:**

    * `children` (ReactNode): Components to be wrapped by the provider
  </Tab>

  <Tab title="Code">
    ```tsx theme={null}
    import { CVIProvider } from './cvi-provider';
    ```

    ```tsx theme={null}
    <CVIProvider>
      {/* your app components */}
    </CVIProvider>
    ```
  </Tab>
</Tabs>

<Note>
  Import paths such as `./cvi-provider` are **relative to your file** and to where the CLI copied components. Paths in [Embed CVI](/sections/integrations/embedding-cvi) (for example `./components/cvi/components/cvi-provider`) show another valid layout—adjust imports to match your project tree.
</Note>

### AudioWave

The `AudioWave` component provides real-time audio level visualization for video chat participants, displaying animated bars that respond to audio input levels.

```bash theme={null}
npx @tavus/cvi-ui@latest add audio-wave
```

<Tabs>
  <Tab title="Description">
    The `AudioWave` component provides real-time audio level visualization for video chat participants, displaying animated bars that respond to audio input levels.

    **Features:**

    * **Real-time Audio Visualization**: Three animated bars that respond to audio levels
    * **Active Speaker Detection**: Visual distinction between active and inactive speakers
    * **Performance Optimized**: Uses `requestAnimationFrame` for smooth animations
    * **Responsive Design**: Compact circular design that fits well in video previews
    * **Audio Level Scaling**: Intelligent volume scaling for consistent visual feedback

    **Props:**

    * `id` (string): The participant's session ID to monitor audio levels for
  </Tab>

  <Tab title="Code">
    ```tsx theme={null}
    import { AudioWave } from './audio-wave';
    ```

    ```tsx theme={null}
    <AudioWave id={participantId} />
    ```
  </Tab>
</Tabs>

### Device Select

The `device-select` module provides advanced device selection controls, including dropdowns for choosing microphones and cameras, and integrated toggle buttons.

```bash theme={null}
npx @tavus/cvi-ui@latest add device-select
```

<Tabs>
  <Tab title="Description">
    The `device-select` module provides advanced device selection controls, including dropdowns for choosing microphones and cameras, and integrated toggle buttons.

    **Exported Components:**

    * **`MicSelectBtn`**: Microphone toggle button with device selection
    * **`CameraSelectBtn`**: Camera toggle button with device selection
    * **`ScreenShareButton`**: Button to toggle screen sharing

    **Features:**

    * Integrated device selection and toggling
    * Dropdowns for camera/microphone selection
    * Visual state indicators and accessibility support
    * Uses Daily.co device management hooks
    * CSS modules for styling
  </Tab>

  <Tab title="Code">
    ```tsx theme={null}
    import { MicSelectBtn, CameraSelectBtn, ScreenShareButton } from './device-select';
    ```

    ```tsx theme={null}
    <MicSelectBtn />
    <CameraSelectBtn />
    <ScreenShareButton />
    ```
  </Tab>
</Tabs>

<Note>
  **`ScreenShareButton`** exists in both **`device-select`** and **`media-controls`**. They are different exports from different modules—import from the path that matches the `npx @tavus/cvi-ui@latest add device-select` or `… add media-controls` command you ran.
</Note>

### Media Controls

The `media-controls` module provides simple toggle buttons for microphone, camera, and screen sharing, designed for direct use in video chat interfaces.

```bash theme={null}
npx @tavus/cvi-ui@latest add media-controls
```

<Tabs>
  <Tab title="Description">
    The `media-controls` module provides simple toggle buttons for microphone, camera, and screen sharing, designed for direct use in video chat interfaces.

    **Exported Components:**

    * **`MicToggleButton`**: Toggles microphone mute/unmute state
    * **`CameraToggleButton`**: Toggles camera on/off
    * **`ScreenShareButton`**: Toggles screen sharing on/off

    **Features:**

    * Simple, accessible toggle buttons
    * Visual state indicators (muted, unmuted, on/off)
    * Disabled state when device is not ready
    * Uses Daily.co hooks for device state
    * CSS modules for styling
  </Tab>

  <Tab title="Code">
    ```tsx theme={null}
    import { MicToggleButton, CameraToggleButton, ScreenShareButton } from './media-controls';
    ```

    ```tsx theme={null}
    <MicToggleButton />
    <CameraToggleButton />
    <ScreenShareButton />
    ```
  </Tab>
</Tabs>

### Closed Captions

The `closed-captions` module renders live captions for both the user and the replica, plus a toggle button and a context provider that lets multiple components share the on/off state.

```bash theme={null}
npx @tavus/cvi-ui@latest add closed-captions
```

<Tabs>
  <Tab title="Description">
    The `closed-captions` module renders live captions for both the user and the replica, plus a toggle button and a context provider that lets multiple components share the on/off state.

    **Exported Components:**

    * **`ClosedCaptionsProvider`**: Context provider that owns the captions on/off state. Wrap your conversation tree with it.
    * **`ClosedCaptionsButton`**: Toggle button that flips captions on and off (uses `aria-pressed`).
    * **`ClosedCaptions`**: Overlay that displays the active caption with the speaker's role label. Shows the latest 3 lines and auto-clears 2 seconds after the final utterance.

    **Features:**

    * Streams captions from `conversation.utterance.streaming` for both `user` and `replica` roles
    * Auto-clears the caption after each final utterance
    * Anchors to the bottom of the overlay so the most recent text is always visible
    * CSS modules for styling, customizable via `--cc-line-height` and `--cc-max-lines`

    **Provider Props:**

    * `children` (ReactNode): Components to be wrapped by the provider
    * `defaultEnabled` (boolean, optional): Initial captions on/off state. Defaults to `false`.
  </Tab>

  <Tab title="Code">
    ```tsx theme={null}
    import {
      ClosedCaptions,
      ClosedCaptionsButton,
      ClosedCaptionsProvider,
    } from './closed-captions';
    ```

    ```tsx theme={null}
    <ClosedCaptionsProvider>
      <div className="video-area">
        {/* main video, self-view, etc. */}
        <ClosedCaptions />
      </div>
      <div className="footer-controls">
        <ClosedCaptionsButton />
        {/* other controls */}
      </div>
    </ClosedCaptionsProvider>
    ```
  </Tab>
</Tabs>

### Chat

The `chat` module renders a slide-in side panel for text chat alongside the live conversation, plus a toggle button and a context provider that owns the panel's open/closed state.

```bash theme={null}
npx @tavus/cvi-ui@latest add chat
```

<Tabs>
  <Tab title="Description">
    The `chat` module renders a slide-in side panel for text chat alongside the live conversation, plus a toggle button and a context provider that owns the panel's open/closed state.

    **Exported Components:**

    * **`ChatProvider`**: Context provider that owns the chat panel's open/closed state. Wrap your conversation tree with it.
    * **`ChatButton`**: Toggle button that opens and closes the chat panel (uses `aria-expanded` and `aria-controls`).
    * **`ChatPanel`**: Slide-in side panel containing the message list and composer. Renders a persistent ARIA live region so screen readers announce new messages, and is set to `inert` while closed so its contents stay out of the tab order.

    **Features:**

    * **Message list**: Renders the running transcript of `user` and `replica` messages tracked by [`useChat`](/sections/conversational-video-interface/component-library/hooks#usechat), with optimistic local echo for messages the user just sent.
    * **Composer**: Multi-line textarea with **Enter to send**, **Shift+Enter for newline**, and IME-safe input handling so composition (e.g. CJK input) is not interrupted by the send shortcut.

    **Provider Props:**

    * `children` (ReactNode): Components to be wrapped by the provider
    * `defaultOpen` (boolean, optional): Initial open/closed state of the chat panel. Defaults to `false`.
  </Tab>

  <Tab title="Code">
    ```tsx theme={null}
    import {
      ChatButton,
      ChatPanel,
      ChatProvider,
    } from './chat';
    ```

    ```tsx theme={null}
    <ChatProvider>
      <div className="conversation-layout">
        <div className="video-area">
          {/* main video, self-view, etc. */}
        </div>
        <ChatPanel />
      </div>
      <div className="footer-controls">
        <ChatButton />
        {/* other controls */}
      </div>
    </ChatProvider>
    ```
  </Tab>
</Tabs>


# Hooks
Source: https://docs.tavus.io/sections/conversational-video-interface/component-library/hooks

See what hooks Tavus supports for managing video calls, media controls, participant management, and conversation events.

Hooks are generated source files copied into your app by `npx @tavus/cvi-ui@latest add ...`. Import them from your generated hooks directory and render them under `CVIProvider` unless the hook explicitly only creates request helpers.

| Hook                      | Add command                      | Import path pattern                                  | Parameters        | Return values                                                      | Required context              | Generated location pattern                             |
| ------------------------- | -------------------------------- | ---------------------------------------------------- | ----------------- | ------------------------------------------------------------------ | ----------------------------- | ------------------------------------------------------ |
| `useCVICall`              | `add use-cvi-call`               | `<components-path>/hooks/use-cvi-call`               | None              | `joinCall`, `leaveCall`                                            | `CVIProvider`                 | `<components-path>/hooks/use-cvi-call.*`               |
| `useStartHaircheck`       | `add use-start-haircheck`        | `<components-path>/hooks/use-start-haircheck`        | None              | Permission booleans, `requestPermissions`                          | `CVIProvider`                 | `<components-path>/hooks/use-start-haircheck.*`        |
| `useLocalCamera`          | `add use-local-camera`           | `<components-path>/hooks/use-local-camera`           | None              | `onToggleCamera`, `isCamReady`, `isCamMuted`, `localSessionId`     | `CVIProvider` and active call | `<components-path>/hooks/use-local-camera.*`           |
| `useLocalMicrophone`      | `add use-local-microphone`       | `<components-path>/hooks/use-local-microphone`       | None              | `onToggleMicrophone`, `isMicReady`, `isMicMuted`, `localSessionId` | `CVIProvider` and active call | `<components-path>/hooks/use-local-microphone.*`       |
| `useLocalScreenshare`     | `add use-local-screenshare`      | `<components-path>/hooks/use-local-screenshare`      | None              | `onToggleScreenshare`, `isScreenSharing`, `localSessionId`         | `CVIProvider` and active call | `<components-path>/hooks/use-local-screenshare.*`      |
| `useRequestPermissions`   | `add use-request-permissions`    | `<components-path>/hooks/use-request-permissions`    | None              | `requestPermissions`                                               | `CVIProvider`                 | `<components-path>/hooks/use-request-permissions.*`    |
| `useReplicaIDs`           | `add use-replica-ids`            | `<components-path>/hooks/use-replica-ids`            | None              | `string[]`                                                         | `CVIProvider` and active call | `<components-path>/hooks/use-replica-ids.*`            |
| `useRemoteParticipantIDs` | `add use-remote-participant-ids` | `<components-path>/hooks/use-remote-participant-ids` | None              | `string[]`                                                         | `CVIProvider` and active call | `<components-path>/hooks/use-remote-participant-ids.*` |
| `useObservableEvent`      | `add cvi-events-hooks`           | `<components-path>/hooks/cvi-events-hooks`           | `callback(event)` | None                                                               | `CVIProvider` and active call | `<components-path>/hooks/cvi-events-hooks.*`           |
| `useClosedCaption`        | `add use-closed-caption`         | `<components-path>/hooks/use-closed-caption`         | None              | `ClosedCaption` or `null`                                          | `CVIProvider` and active call | `<components-path>/hooks/use-closed-caption.*`         |
| `useSendAppMessage`       | `add cvi-events-hooks`           | `<components-path>/hooks/cvi-events-hooks`           | None              | `sendMessage(message)`                                             | `CVIProvider` and active call | `<components-path>/hooks/cvi-events-hooks.*`           |
| `useChat`                 | `add use-chat`                   | `<components-path>/hooks/use-chat`                   | None              | `messages`, `sendMessage(text)`                                    | `CVIProvider` and active call | `<components-path>/hooks/use-chat.*`                   |

## 🔧 Core Call Management

### useCVICall

Essential hook for joining and leaving video calls.

```bash theme={null}
npx @tavus/cvi-ui@latest add use-cvi-call
```

<Tabs>
  <Tab title="Description">
    A React hook that provides comprehensive call management functionality for video conversations. This hook handles the core lifecycle of video calls, including connection establishment, room joining, and proper cleanup when leaving calls.

    **Purpose:**

    * Manages call join/leave operations with proper state management
    * Handles connection lifecycle and cleanup
    * Provides simple interface for call control

    **Return Values:**

    * `joinCall` (function): Function to join a call by URL - handles Daily.co room connection
    * `leaveCall` (function): Function to leave the current call - properly disconnects and cleans up resources
  </Tab>

  <Tab title="Code">
    ```tsx theme={null}
    import { useCVICall } from './hooks/use-cvi-call';
    ```

    ```tsx theme={null}
    const CallManager = () => {
      const { joinCall, leaveCall } = useCVICall();

      const handleJoin = () => {
        joinCall({ url: 'https://your-daily-room-url' });
      };

      return (
        <div>
          <button onClick={handleJoin}>Join Call</button>
          <button onClick={leaveCall}>Leave Call</button>
        </div>
      );
    };
    ```
  </Tab>
</Tabs>

### useStartHaircheck

A React hook that manages device permissions and camera initialization for the hair-check component.

```bash theme={null}
npx @tavus/cvi-ui@latest add use-start-haircheck
```

<Tabs>
  <Tab title="Description">
    A React hook that manages device permissions and camera initialization for the hair-check component.

    **Purpose:**

    * Monitors device permission states
    * Starts camera and microphone when appropriate
    * Provides permission state for UI conditional rendering
    * Handles permission request flow

    **Return Values:**

    * `isPermissionsPrompt` (boolean): Browser is prompting for device permission
    * `isPermissionsLoading` (boolean): Permissions are being processed or camera is initializing
    * `isPermissionsGranted` (boolean): Device permission granted
    * `isPermissionsDenied` (boolean): Device permission denied
    * `requestPermissions` (function): Function to request camera and microphone permissions
  </Tab>

  <Tab title="Code">
    ```tsx theme={null}
    import { useStartHaircheck } from './hooks/use-start-haircheck';
    ```

    ```tsx theme={null}
    const HairCheckComponent = () => {
      const {
        isPermissionsPrompt,
        isPermissionsLoading,
        isPermissionsGranted,
        isPermissionsDenied,
        requestPermissions
      } = useStartHaircheck();

      useEffect(() => {
        requestPermissions();
      }, []);

      return (
        <div>
          {isPermissionsLoading && <InitializingSpinner />}
          {isPermissionsPrompt && <PermissionPrompt />}
          {isPermissionsDenied && <PermissionDeniedMessage />}
          {isPermissionsGranted && <VideoPreview />}
        </div>
      );
    };
    ```
  </Tab>
</Tabs>

***

## 🎥 Media Controls

### useLocalCamera

A React hook that provides local camera state and toggle functionality.

```bash theme={null}
npx @tavus/cvi-ui@latest add use-local-camera
```

<Tabs>
  <Tab title="Description">
    A React hook that provides local camera state and toggle functionality.

    **Purpose:**

    * Manages local camera state (on/off)
    * Tracks camera permission and ready state

    **Return Values:**

    * `onToggleCamera` (function): Function to toggle camera on/off
    * `isCamReady` (boolean): Camera permission is granted and ready
    * `isCamMuted` (boolean): Camera is currently turned off
    * `localSessionId` (string): Local session ID
  </Tab>

  <Tab title="Code">
    ```tsx theme={null}
    import { useLocalCamera } from './hooks/use-local-camera';
    ```

    ```tsx theme={null}
    const CameraControls = () => {
      const { onToggleCamera, isCamReady, isCamMuted } = useLocalCamera();

      return (
        <button
          onClick={onToggleCamera}
          disabled={!isCamReady}
        >
          {isCamMuted ? 'Turn Camera On' : 'Turn Camera Off'}
        </button>
      );
    };
    ```
  </Tab>
</Tabs>

### useLocalMicrophone

A React hook that provides local microphone state and toggle functionality.

```bash theme={null}
npx @tavus/cvi-ui@latest add use-local-microphone
```

<Tabs>
  <Tab title="Description">
    A React hook that provides local microphone state and toggle functionality.

    **Purpose:**

    * Manages local microphone state (on/off)
    * Tracks microphone permission and ready state

    **Return Values:**

    * `onToggleMicrophone` (function): Function to toggle microphone on/off
    * `isMicReady` (boolean): Microphone permission is granted and ready
    * `isMicMuted` (boolean): Microphone is currently turned off
    * `localSessionId` (string): Local session ID
  </Tab>

  <Tab title="Code">
    ```tsx theme={null}
    import { useLocalMicrophone } from './hooks/use-local-microphone';
    ```

    ```tsx theme={null}
    const MicrophoneControls = () => {
      const { onToggleMicrophone, isMicReady, isMicMuted } = useLocalMicrophone();

      return (
        <button
          onClick={onToggleMicrophone}
          disabled={!isMicReady}
        >
          {isMicMuted ? 'Unmute' : 'Mute'}
        </button>
      );
    };
    ```
  </Tab>
</Tabs>

### useLocalScreenshare

A React hook that provides local screen sharing state and toggle functionality.

```bash theme={null}
npx @tavus/cvi-ui@latest add use-local-screenshare
```

<Tabs>
  <Tab title="Description">
    A React hook that provides local screen sharing state and toggle functionality.

    **Purpose:**

    * Manages screen sharing state (on/off)
    * Provides screen sharing toggle function
    * Handles screen share start/stop with optimized display media options

    **Return Values:**

    * `onToggleScreenshare` (function): Function to toggle screen sharing on/off
    * `isScreenSharing` (boolean): Whether screen sharing is currently active
    * `localSessionId` (string): Local session ID

    **Display Media Options:**
    When starting screen share, the hook uses the following optimized settings:

    * **Audio**: Disabled (false)
    * **Self Browser Surface**: Excluded
    * **Surface Switching**: Included
    * **Video Resolution**: 1920x1080
  </Tab>

  <Tab title="Code">
    ```tsx theme={null}
    import { useLocalScreenshare } from './hooks/use-local-screenshare';
    ```

    ```tsx theme={null}
    const ScreenShareControls = () => {
      const { onToggleScreenshare, isScreenSharing } = useLocalScreenshare();

      return (
        <button
          onClick={onToggleScreenshare}
          className={isScreenSharing ? 'active' : ''}
        >
          {isScreenSharing ? 'Stop Sharing' : 'Share Screen'}
        </button>
      );
    };
    ```
  </Tab>
</Tabs>

### useRequestPermissions

A React hook that requests camera and microphone permissions with optimized audio processing settings.

```bash theme={null}
npx @tavus/cvi-ui@latest add use-request-permissions
```

<Tabs>
  <Tab title="Description">
    A React hook that requests camera and microphone permissions with optimized audio processing settings.

    **Purpose:**

    * Requests camera and microphone permissions from the user
    * Starts camera and audio with specific configuration
    * Applies noise cancellation audio processing
    * Provides a clean interface for permission requests

    **Return Values:**

    * `requestPermissions` (function): Function to request camera and microphone permissions

    **Configuration:**
    When requesting permissions, the hook uses the following settings:

    * **Video**: Started on (startVideoOff: false)
    * **Audio**: Started on (startAudioOff: false)
    * **Audio Source**: Default system audio input
    * **Audio Processing**: Noise cancellation enabled
  </Tab>

  <Tab title="Code">
    ```tsx theme={null}
    import { useRequestPermissions } from './hooks/use-request-permissions';
    ```

    ```tsx theme={null}
    const PermissionRequest = () => {
      const requestPermissions = useRequestPermissions();

      const handleRequestPermissions = async () => {
        try {
          await requestPermissions();
          console.log('Permissions granted successfully');
        } catch (error) {
          console.error('Failed to get permissions:', error);
        }
      };

      return (
        <button onClick={handleRequestPermissions}>
          Request Camera & Microphone Permissions
        </button>
      );
    };
    ```
  </Tab>
</Tabs>

***

## 👥 Participant Management

### useReplicaIDs

A React hook that returns the IDs of all Tavus replica participants in a call.

```bash theme={null}
npx @tavus/cvi-ui@latest add use-replica-ids
```

<Tabs>
  <Tab title="Description">
    A React hook that returns the IDs of all Tavus replica participants in a call.

    **Purpose:**

    * Filters and returns participant IDs where `user_id` includes 'tavus-replica'

    **Return Value:**

    * `string[]` — Array of replica participant IDs
  </Tab>

  <Tab title="Code">
    ```tsx theme={null}
    import { useReplicaIDs } from './hooks/use-replica-ids';
    ```

    ```tsx theme={null}
    const ids = useReplicaIDs();
    // ids is an array of participant IDs for Tavus replicas
    ```
  </Tab>
</Tabs>

### useRemoteParticipantIDs

A React hook that returns the IDs of all remote participants in a call.

```bash theme={null}
npx @tavus/cvi-ui@latest add use-remote-participant-ids
```

<Tabs>
  <Tab title="Description">
    A React hook that returns the IDs of all remote participants in a call.

    **Purpose:**

    * Returns participant IDs for all remote participants (excluding local user)

    **Return Value:**

    * `string[]` — Array of remote participant IDs
  </Tab>

  <Tab title="Code">
    ```tsx theme={null}
    import { useRemoteParticipantIDs } from './hooks/use-remote-participant-ids';
    ```

    ```tsx theme={null}
    const remoteIds = useRemoteParticipantIDs();
    // remoteIds is an array of remote participant IDs
    ```
  </Tab>
</Tabs>

***

## 💬 Conversation & Events

### useObservableEvent

A React hook that listens for CVI app messages and provides a callback mechanism for handling various conversation events.

```bash theme={null}
npx @tavus/cvi-ui@latest add cvi-events-hooks
```

<Tabs>
  <Tab title="Description">
    A React hook that listens for CVI app messages and provides a callback mechanism for handling various conversation events.

    **Purpose:**

    * Listens for app messages from the Daily.co call mapped to CVI events
    * Handles various conversation event types (utterances, tool calls, speaking events, etc.)
    * Provides type-safe event handling for CVI interactions

    **Parameters:**

    * `callback` (function): Function called when app messages are received

    **Event Types:**
    This hook handles all CVI conversation events. For detailed information about each event type, see the [Interaction Events overview](/sections/conversational-video-interface/interactions-protocols/overview).
  </Tab>

  <Tab title="Code">
    ```tsx theme={null}
    import { useObservableEvent } from './hooks/cvi-events-hooks';
    ```

    ```tsx theme={null}
    const ConversationHandler = () => {
      useObservableEvent((event) => {
        switch (event.event_type) {
          case 'conversation.utterance':
            console.log('Speech:', event.properties.speech);
            break;
          case 'conversation.replica.started_speaking':
            console.log('Replica started speaking');
            break;
          case 'conversation.user.stopped_speaking':
            console.log('User stopped speaking');
            break;
        }
      });

      return <div>Listening for conversation events...</div>;
    };
    ```
  </Tab>
</Tabs>

### useClosedCaption

A React hook that returns the latest closed caption with the speaker's role and text.

```bash theme={null}
npx @tavus/cvi-ui@latest add use-closed-caption
```

<Tabs>
  <Tab title="Description">
    A React hook that returns the latest closed caption with the speaker's role and text. Subscribes to `conversation.utterance.streaming` events for both `user` and `replica` roles and exposes the latest caption to your UI.

    **Purpose:**

    * Streams captions for both the user and the replica from `conversation.utterance.streaming`
    * Updates progressively as either party speaks
    * Auto-clears the caption 2 seconds after a `final` utterance
    * Returns `null` when no caption is currently being shown

    **Return Value:**

    * `ClosedCaption | null` where `ClosedCaption` is `{ role: "user" | "replica"; text: string }`
  </Tab>

  <Tab title="Code">
    ```tsx theme={null}
    import { useClosedCaption } from './hooks/use-closed-caption';
    ```

    ```tsx theme={null}
    const Captions = () => {
      const caption = useClosedCaption();

      if (!caption) return null;

      return (
        <div role="status" aria-live="polite">
          <span>{caption.role === 'replica' ? 'Replica' : 'You'}</span>
          <span>{caption.text}</span>
        </div>
      );
    };
    ```
  </Tab>
</Tabs>

### useSendAppMessage

A React hook that provides a function to send CVI app messages to other participants in the call.

```bash theme={null}
npx @tavus/cvi-ui@latest add cvi-events-hooks
```

<Tabs>
  <Tab title="Description">
    A React hook that provides a function to send CVI app messages to other participants in the call.

    **Purpose:**

    * Sends various types of conversation messages to the CVI system
    * Supports echo, respond, interrupt, and context management messages
    * Provides type-safe message sending with proper validation
    * Enables real-time communication with Tavus replicas and conversation management

    **Return Value:**

    * `(message: SendAppMessageProps) => void` - Function that sends the message when called

    **Message Types:**
    This hook supports all CVI interaction types. For detailed information about each interaction type and their properties, see the [Interaction Events overview](/sections/conversational-video-interface/interactions-protocols/overview).
  </Tab>

  <Tab title="Code">
    ```tsx theme={null}
    import { useSendAppMessage } from './hooks/cvi-events-hooks';
    ```

    ```tsx theme={null}
    const MessageSender = () => {
      const sendMessage = useSendAppMessage();

      // Send a text echo
      const sendTextEcho = () => {
        sendMessage({
          message_type: "conversation",
          event_type: "conversation.echo",
          conversation_id: "conv-123",
          properties: {
            modality: "text",
            text: "Hello, world!",
            audio: "",
            sample_rate: 16000,
            inference_id: "inf-456",
            done: true
          }
        });
      };

      // Send a text response
      const sendResponse = () => {
        sendMessage({
          message_type: "conversation",
          event_type: "conversation.respond",
          conversation_id: "conv-123",
          properties: {
            text: "This is my response to the conversation."
          }
        });
      };

      return (
        <div>
          <button onClick={sendTextEcho}>Send Text Echo</button>
          <button onClick={sendResponse}>Send Response</button>
        </div>
      );
    };
    ```
  </Tab>
</Tabs>

### useChat

A React hook that powers a chat experience on top of the live conversation. It tracks the running transcript and provides a function to send a user turn back to the replica.

```bash theme={null}
npx @tavus/cvi-ui@latest add use-chat
```

<Tabs>
  <Tab title="Description">
    A React hook that powers a chat experience on top of the live conversation. Subscribes to Daily app messages and tracks `conversation.utterance` events from both `user` and `replica` roles, and exposes a `sendMessage` function that dispatches `conversation.respond`.

    **Purpose:**

    * Builds a chronological transcript of `user` and `replica` messages from `conversation.utterance` events
    * Optimistically appends locally sent messages so the UI updates immediately, then reconciles each pending message with the matching server-side utterance using `inference_id`
    * Dispatches `conversation.respond` when the user sends a chat message
    * Designed to back the [`Chat`](/sections/conversational-video-interface/component-library/components#chat) components (`ChatProvider`, `ChatPanel`, `ChatButton`)

    **Return Values:**

    * `messages` (`ChatMessage[]`): Ordered transcript where `ChatMessage` is `{ id: string; role: "user" | "replica"; text: string; inference_id?: string; pending?: boolean }`
    * `sendMessage` (`(text: string) => void`): Sends a user turn — appends a pending local echo to `messages` and dispatches `conversation.respond`. The pending entry is reconciled (and `pending` cleared) when the matching utterance arrives by `inference_id`.
  </Tab>

  <Tab title="Code">
    ```tsx theme={null}
    import { useChat } from './hooks/use-chat';
    ```

    ```tsx theme={null}
    const Chat = () => {
      const { messages, sendMessage } = useChat();
      const [draft, setDraft] = useState('');

      const onSubmit = () => {
        const text = draft.trim();
        if (!text) return;
        sendMessage(text);
        setDraft('');
      };

      return (
        <div>
          <ul>
            {messages.map((m) => (
              <li key={m.id} aria-busy={m.pending || undefined}>
                <strong>{m.role === 'replica' ? 'Replica' : 'You'}:</strong> {m.text}
              </li>
            ))}
          </ul>
          <textarea
            value={draft}
            onChange={(e) => setDraft(e.target.value)}
          />
          <button onClick={onSubmit}>Send</button>
        </div>
      );
    };
    ```
  </Tab>
</Tabs>


# Overview
Source: https://docs.tavus.io/sections/conversational-video-interface/component-library/overview

Learn how our Tavus Conversational Video Interface (CVI) Component Library can help you go live in minutes.

## Overview

`@tavus/cvi-ui` is a CLI that copies React components, hooks, styles, and optional server helpers into your application. It is not a hosted widget or a runtime CDN package. After you run `init` and `add ...`, you import the generated files from your own project tree and can edit them like application code.

Use this path when you want Tavus-provided React UI and Daily-powered call state without building every media control yourself. For the fastest no-code UI, use an [iframe embed](/sections/integrations/embedding-cvi#iframe). For fully custom Daily call-object ownership, use the [Daily JS / React path](/sections/integrations/embedding-cvi#react--daily-createcallobject).

<CardGroup>
  <Card title="Blocks" icon="layer-group" href="/sections/conversational-video-interface/component-library/blocks">
    Complete layouts such as `Conversation` and `HairCheck`.
  </Card>

  <Card title="Components" icon="puzzle-piece" href="/sections/conversational-video-interface/component-library/components">
    Building blocks such as `CVIProvider`, media controls, captions, chat, and `AudioWave`.
  </Card>

  <Card title="Hooks" icon="code" href="/sections/conversational-video-interface/component-library/hooks">
    React hooks for call lifecycle, media state, participants, captions, chat, and CVI events.
  </Card>

  <Card title="Server" icon="server" href="/sections/conversational-video-interface/component-library/server">
    Server routes and browser helpers that create and end conversations without exposing `TAVUS_API_KEY`.
  </Card>
</CardGroup>

## Mental model

| Piece                           | What it does                                                                                                         | Where to read next                                                                               |
| ------------------------------- | -------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| `npx @tavus/cvi-ui@latest init` | Creates `cvi-components.json`, asks about TypeScript, and installs Daily/Jotai dependencies.                         | This page                                                                                        |
| `CVIProvider`                   | React wrapper that provides Daily context to child components and hooks. Put generated CVI UI under this provider.   | [Components](/sections/conversational-video-interface/component-library/components#cvi-provider) |
| `Conversation`                  | React block that renders the Tavus/Daily call UI from a `conversationUrl` and calls `onLeave` when the user leaves.  | [Blocks](/sections/conversational-video-interface/component-library/blocks#conversation-block)   |
| Server helpers                  | Generated server routes keep `TAVUS_API_KEY` server-only, and generated browser helpers call your own backend route. | [Server](/sections/conversational-video-interface/component-library/server)                      |

<Note>
  Generated imports are relative to where the CLI copied files in your app. Examples in these docs use paths such as `./components/cvi/components/conversation`; adjust them if your `cvi-components.json` components path is different.
</Note>

***

## Quick Start

### Prerequisites

Before getting started, ensure you have a React project set up.

Alternatively, you can start from our example project: [CVI UI Haircheck Conversation Example](https://github.com/Tavus-Engineering/tavus-examples/tree/main/examples/cvi-ui-haircheck-conversation) - this example already has the HairCheck and Conversation blocks set up.

### 1. Initialize CVI in Your Project

```bash theme={null}
npx @tavus/cvi-ui@latest init
```

This command:

* Creates `cvi-components.json`, which stores the generated component path and TypeScript preference.
* Prompts for TypeScript preference.
* Installs `@daily-co/daily-react`, `@daily-co/daily-js`, and `jotai`.

### 2. Add CVI Components and Server Helpers

```bash theme={null}
npx @tavus/cvi-ui@latest add conversation
npx @tavus/cvi-ui@latest add tavus-api
```

`add conversation` generates the `Conversation` block and the components/hooks it needs. `add tavus-api` generates a framework-specific backend route plus `lib/tavus-client.ts`, which exports `createTavusConversation(params?)` and `endTavusConversation(id)`.

For Vite projects with a server runtime, use:

```bash theme={null}
npx @tavus/cvi-ui@latest add tavus-api-vite-ssr
```

Plain client-only Vite is unsupported because it would require exposing `TAVUS_API_KEY` in browser JavaScript. Add a server runtime and use `tavus-api-vite-ssr`, or create your own backend route.

### 3. Wrap Your App with the CVI Provider

In your root directory (main.tsx or index.tsx):

```tsx theme={null}
import { CVIProvider } from './components/cvi/components/cvi-provider';

function App() {
  return <CVIProvider>{/* Your app content */}</CVIProvider>;
}
```

### 4. Add a Conversation Component

Learn how to create a conversation URL at [https://docs.tavus.io/api-reference/conversations/create-conversation](https://docs.tavus.io/api-reference/conversations/create-conversation). To create a conversation URL from your app without exposing your `TAVUS_API_KEY` in the browser, use the server helpers in [Server](/sections/conversational-video-interface/component-library/server) (`tavus-api` for Next.js/Remix/TanStack Start, or `tavus-api-vite-ssr` for Vite-with-server).

**Note:** The Conversation component requires a parent container with defined dimensions to display properly.

<Info>
  Ensure your body element has full dimensions (`width: 100%` and `height:
      100%`) in your CSS for proper component display.
</Info>

```tsx theme={null}
import { Conversation } from './components/cvi/components/conversation';

function CVI() {
  const handleLeave = () => {
    // handle leave
  };
  return (
    <div
      style={{
        width: '100%',
        height: '100%',
        maxWidth: '1200px',
        margin: '0 auto',
      }}
    >
      <Conversation
        conversationUrl='YOUR_TAVUS_MEETING_URL'
        onLeave={handleLeave}
      />
    </div>
  );
}
```

## Complete React example

This example assumes you ran:

```bash theme={null}
npx @tavus/cvi-ui@latest init
npx @tavus/cvi-ui@latest add conversation
npx @tavus/cvi-ui@latest add tavus-api
```

Set `TAVUS_API_KEY` only in your server environment. The browser code below calls the generated `createTavusConversation` and `endTavusConversation` helpers; those helpers call your generated `/api/tavus` route.

```tsx theme={null}
import { useState } from 'react';
import { CVIProvider } from './components/cvi/components/cvi-provider';
import { Conversation } from './components/cvi/components/conversation';
import {
  createTavusConversation,
  endTavusConversation,
} from './components/cvi/lib/tavus-client';

type TavusConversation = {
  conversation_id: string;
  conversation_url: string;
};

function TavusCall() {
  const [conversation, setConversation] = useState<TavusConversation | null>(null);
  const [isStarting, setIsStarting] = useState(false);
  const [error, setError] = useState<string | null>(null);

  async function startConversation() {
    setIsStarting(true);
    setError(null);

    try {
      const nextConversation = await createTavusConversation({
        persona_id: 'pcb7a34da5fe',
        conversation_name: 'CVI UI example',
      });

      setConversation(nextConversation);
    } catch (error) {
      setError(error instanceof Error ? error.message : 'Failed to start conversation');
    } finally {
      setIsStarting(false);
    }
  }

  async function handleLeave() {
    if (conversation) {
      await endTavusConversation(conversation.conversation_id).catch(() => undefined);
    }

    setConversation(null);
  }

  if (!conversation) {
    return (
      <div>
        <button onClick={startConversation} disabled={isStarting}>
          {isStarting ? 'Starting...' : 'Start conversation'}
        </button>
        {error ? <p role="alert">{error}</p> : null}
      </div>
    );
  }

  return (
    <div style={{ width: '100%', height: '640px' }}>
      <Conversation
        conversationUrl={conversation.conversation_url}
        onLeave={handleLeave}
      />
    </div>
  );
}

export default function App() {
  return (
    <CVIProvider>
      <TavusCall />
    </CVIProvider>
  );
}
```

<Warning>
  `Conversation` needs a parent with defined dimensions. Give the parent an explicit height, or ensure the full chain (`html`, `body`, root element, and container) resolves to a real height.
</Warning>

***

## Documentation Sections

* **[Blocks](/sections/conversational-video-interface/component-library/blocks)** – High-level component compositions and layouts
* **[Components](/sections/conversational-video-interface/component-library/components)** – Individual UI components
* **[Hooks](/sections/conversational-video-interface/component-library/hooks)** – Custom React hooks for managing video call state and interactions
* **[Server](/sections/conversational-video-interface/component-library/server)** – Server-side helpers (`tavus-api`, `tavus-api-vite-ssr`) for creating and ending conversations without exposing your API key


# Server
Source: https://docs.tavus.io/sections/conversational-video-interface/component-library/server

Server-side helpers for managing Tavus conversation lifecycle without leaking your API key to the browser.

# Server

These primitives are not React components — they are server route handlers and small browser-side fetch helpers. Use them to create and end Tavus conversations without bundling your `TAVUS_API_KEY` into client JS.

| Add command                                       | Use for                                                                                                | Generated files                                                                           | Browser exports                                                | Server exports / route                                    | Notes                                                                                                 |
| ------------------------------------------------- | ------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------- | -------------------------------------------------------------- | --------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `npx @tavus/cvi-ui@latest add tavus-api`          | Next.js App Router, Next.js Pages Router, Remix, TanStack Start                                        | Framework route plus `<components-path>/lib/tavus-client.ts`                              | `createTavusConversation(params?)`, `endTavusConversation(id)` | `POST /api/tavus` route for create/end actions            | CLI exits on unsupported client-only frameworks instead of creating an unsafe browser API-key client. |
| `npx @tavus/cvi-ui@latest add tavus-api-vite-ssr` | Vite projects with a server runtime such as Vinxi, Hono, vike-server, Express, Bun, Cloudflare Workers | `<components-path>/lib/tavus-api-vite-ssr.ts` and `<components-path>/lib/tavus-client.ts` | `createTavusConversation(params?)`, `endTavusConversation(id)` | `handleTavusRequest(request: Request): Promise<Response>` | You mount the handler at `POST /api/tavus`; plain client-only Vite remains unsupported.               |

<Warning>
  Keep `TAVUS_API_KEY` only in server environment variables. Do not prefix it with client-exposed environment names such as `VITE_` or `NEXT_PUBLIC_`.
</Warning>

### Tavus API

The `tavus-api` module installs a framework-specific server route that creates and ends Tavus conversations on your backend, plus a small browser client that calls that route.

```bash theme={null}
npx @tavus/cvi-ui@latest add tavus-api
```

<Tabs>
  <Tab title="Description">
    The `tavus-api` module installs a server route that creates and ends Tavus conversations on your backend, plus a small browser client that calls that route. Your `TAVUS_API_KEY` stays on the server and is never bundled into your client JS.

    **What gets installed**

    The CLI detects your framework and installs the matching server route:

    | Framework              | Server route file         |
    | ---------------------- | ------------------------- |
    | Next.js (App Router)   | `app/api/tavus/route.ts`  |
    | Next.js (Pages Router) | `pages/api/tavus.ts`      |
    | Remix                  | `app/routes/api.tavus.ts` |
    | TanStack Start         | `app/routes/api/tavus.ts` |

    Plus the browser-side client at `<components-path>/lib/tavus-client.ts`, which exports `createTavusConversation(params?)` and `endTavusConversation(id)`. Both functions `POST` to `/api/tavus`; the route forwards `params` verbatim to the Tavus REST API, so every field on [`POST /v2/conversations`](/api-reference/conversations/create-conversation) works. New Tavus fields work without a CLI update.

    **Behaviour for unsupported frameworks**

    If the CLI doesn't recognise the framework as one with a built-in server (plain Vite, Expo, manual setups), `add tavus-api` exits with an error rather than silently installing a key-exposing client. See the Vite-with-server opt-in below.

    **Required environment variable (server only — never on the client)**

    * `TAVUS_API_KEY` — required. [Create one in the Tavus Developer Portal.](https://platform.tavus.io/api-keys)
  </Tab>

  <Tab title="Code">
    ```tsx theme={null}
    import { createTavusConversation, endTavusConversation } from './lib/tavus-client';
    ```

    ```tsx theme={null}
    const handleStart = async () => {
      const { conversation_id, conversation_url } = await createTavusConversation({
        persona_id: 'pcb7a34da5fe',
        "properties": {
          "language": "english"
        }
      });
      // ...join the call with conversation_url
    };

    const handleEnd = async (id: string) => {
      await endTavusConversation(id);
    };
    ```
  </Tab>
</Tabs>

### Tavus API for Vite (with a server runtime)

For Vite projects that have a server (Vinxi, Hono, vike-server, custom Express, Bun, Cloudflare Workers, …), `add tavus-api-vite-ssr` installs a runtime-agnostic Request handler you wire into your middleware.

```bash theme={null}
npx @tavus/cvi-ui@latest add tavus-api-vite-ssr
```

<Tabs>
  <Tab title="Description">
    Installs `<components-path>/lib/tavus-api-vite-ssr.ts` exporting `handleTavusRequest(request: Request): Promise<Response>`, plus the matching `lib/tavus-client.ts`. The handler uses the standard Web Fetch `Request`/`Response` interfaces, so it plugs into any server runtime that speaks fetch.

    **Wiring examples** (the file header includes these too):

    * **Hono**:
      ```ts theme={null}
      import { handleTavusRequest } from './lib/tavus-api-vite-ssr';
      app.post('/api/tavus', (c) => handleTavusRequest(c.req.raw));
      ```
    * **h3 / Vinxi**:
      ```ts theme={null}
      import { eventHandler, toWebRequest } from 'h3';
      import { handleTavusRequest } from './lib/tavus-api-vite-ssr';
      export default eventHandler((event) => handleTavusRequest(toWebRequest(event)));
      ```
    * **Express** (with a Web Fetch adapter such as `@hattip/adapter-node`):
      ```ts theme={null}
      app.post('/api/tavus', async (req, res) => {
        const webRes = await handleTavusRequest(toWebRequest(req));
        // pipe webRes back to res
      });
      ```

    Once the handler is mounted at `POST /api/tavus`, the installed `lib/tavus-client.ts` calls it from the browser — no API key on the client.

    **Required environment variable (server only)** — `TAVUS_API_KEY`. [Create one in the Tavus Developer Portal.](https://platform.tavus.io/api-keys)

    The full create-conversation field surface is supported via `createTavusConversation(params)` — see the [API reference](/api-reference/conversations/create-conversation) and the `tavus-api` section above for the params shape.
  </Tab>

  <Tab title="Code">
    ```tsx theme={null}
    import { handleTavusRequest } from './lib/tavus-api-vite-ssr';
    // …mount via your server's middleware (Hono, h3, Express, Cloudflare, Bun, …)

    import { createTavusConversation } from './lib/tavus-client';
    const { conversation_id, conversation_url } = await createTavusConversation({
      persona_id: 'pcb7a34da5fe',
      "properties": {
        "language": "english"
      }
    });
    ```
  </Tab>
</Tabs>

<Note>
  **No client-only mode.** We deliberately do not ship a browser-direct client. Calling Tavus directly from the browser would put your API key in the bundle, which is unsafe in any deployed context. If your project has no server, add one (Vinxi, Hono, vike-server, …) and use `tavus-api-vite-ssr` above.
</Note>


# Audio-Only Conversation
Source: https://docs.tavus.io/sections/conversational-video-interface/conversation/customizations/audio-only

Start a conversation in audio-only mode, perfect for voice-only or low-bandwidth environments.

## Create an Audio Only Conversation

<Note>
  All features in the persona's pipeline, including STT, Perception, and TTS, remain fully active in audio-only mode. The only change is that replica video rendering is not included.
</Note>

<Steps>
  <Step title="Step 1: Create your Audio Only Conversation">
    <Note>
      In this example, we will use stock persona ID ***pcb7a34da5fe*** (Sales Development Rep).
    </Note>

    To enable audio-only mode, set the `audio_only` parameter to `true` when creating the conversation:

    ```shell cURL theme={null}
    curl --request POST \
      --url https://tavusapi.com/v2/conversations \
      --header 'Content-Type: application/json' \
      --header 'x-api-key: <api_key>' \
      --data '{
      "persona_id": "pcb7a34da5fe",
      "audio_only": true
    }'

    ```

    <Note>
      Replace `<api_key>` with your actual API key. You can generate one in the <a href="https://platform.tavus.io/api-keys">Developer Portal</a>.
    </Note>
  </Step>

  <Step title="Step 2: Join the Conversation">
    To join the conversation, click the link in the ***conversation\_url*** field from the response:

    ```json theme={null}
    {
        "conversation_id": "cd7e3eac05ede40c",
        "conversation_name": "New Conversation 1751268887110",
        "conversation_url": "<conversation_link>",
        "status": "active",
        "callback_url": "",
        "created_at": "2025-06-30T07:34:47.131571Z"
    }
    ```
  </Step>
</Steps>


# Background Customizations
Source: https://docs.tavus.io/sections/conversational-video-interface/conversation/customizations/background-customizations

Apply a green screen or custom background for a personalized visual experience.

## Customize Background in Conversation Setup

<Steps>
  <Step title="Step 1: Create Your Conversation">
    <Note>
      In this example, we will use stock replica ID ***r90bbd427f71*** (Anna) and stock persona ID ***pcb7a34da5fe*** (Sales Development Rep).
    </Note>

    To apply the green screen background, set the `apply_greenscreen` parameter to `true` when creating the conversation:

    ```shell cURL theme={null}
    curl --request POST \
      --url https://tavusapi.com/v2/conversations \
      --header 'Content-Type: application/json' \
      --header 'x-api-key: <api_key>' \
      --data '{
      "persona_id": "pcb7a34da5fe",
      "replica_id": "r90bbd427f71",
      "callback_url": "https://yourwebsite.com/webhook",
      "conversation_name": "Improve Sales Technique",
      "conversational_context": "I want to improve my sales techniques. Help me practice handling common objections from clients and closing deals more effectively.",
      "properties": {
        "apply_greenscreen": true
       }
    }'

    ```

    <Note>
      Replace `<api_key>` with your actual API key. You can generate one in the <a href="https://platform.tavus.io/api-keys">Developer Portal</a>.
    </Note>
  </Step>

  <Step title="Step 2: Customize the Background">
    The above request will return the following response:

    ```json theme={null}
    {
      "conversation_id": "ca4301628cb9",
      "conversation_name": "Improve Sales Technique",
      "conversation_url": "<conversation_link>",
      "status": "active",
      "callback_url": "https://yourwebsite.com/webhook",
      "created_at": "2025-05-13T06:42:58.291561Z"
    }
    ```

    The replica will appear with a green background. You can customize it on the frontend using WebGL. This allows you to apply a different color or add a custom image.

    <Tip>
      To preview this feature, try our <a href="https://andy-tavus.github.io/CVI-greenscreen-webGL/">Green Screen Sample App</a>. Paste the conversation URL to modify the background.
    </Tip>
  </Step>
</Steps>


# Call Duration and Timeout
Source: https://docs.tavus.io/sections/conversational-video-interface/conversation/customizations/call-duration-and-timeout

Configure call duration and timeout behavior to manage how and when a conversation ends.

## Create a Conversation with Custom Duration and Timeout

<Steps>
  <Step title="Step 1: Create Your Conversation">
    <Note>
      In this example, we will use stock replica ID ***r90bbd427f71*** (Anna) and stock persona ID ***pcb7a34da5fe*** (Sales Development Rep).
    </Note>

    Use the following request body example:

    ```shell cURL theme={null}
    curl --request POST \
      --url https://tavusapi.com/v2/conversations \
      --header 'Content-Type: application/json' \
      --header 'x-api-key: <api_key>' \
      --data '{
      "persona_id": "pcb7a34da5fe",
      "replica_id": "r90bbd427f71",
      "callback_url": "https://yourwebsite.com/webhook",
      "conversation_name": "Improve Sales Technique",
      "conversational_context": "I want to improve my sales techniques. Help me practice handling common objections from clients and closing deals more effectively.",
      "properties": {
        "max_call_duration": 1800,
        "participant_left_timeout": 60,
        "participant_absent_timeout": 120
       }
    }'

    ```

    <Note>
      Replace `<api_key>` with your actual API key. You can generate one in the <a href="https://platform.tavus.io/api-keys">Developer Portal</a>.
    </Note>

    The request example above includes the following customizations:

    | Parameter                    | Description                                                                                     |
    | :--------------------------- | :---------------------------------------------------------------------------------------------- |
    | `max_call_duration`          | Sets the maximum call length in seconds. Maximum: 3600 seconds.                                 |
    | `participant_left_timeout`   | Time (in seconds) to wait before ending the call after the last participant leaves. Default: 0. |
    | `participant_absent_timeout` | Time (in seconds) to end the call if no one joins after it's created. Default: 300.             |
  </Step>

  <Step title="Step 2: Join the Conversation">
    To join the conversation, click the link in the ***conversation\_url*** field from the response:

    ```json theme={null}
    {
      "conversation_id": "ca4301628cb9",
      "conversation_name": "Improve Sales Technique",
      "conversation_url": "<conversation_link>",
      "status": "active",
      "callback_url": "https://yourwebsite.com/webhook",
      "created_at": "2025-05-13T06:42:58.291561Z"
    }
    ```

    Based on the call duration and timeout settings above:

    * The conversation will automatically end after 1800 seconds (30 minutes), regardless of activity.
    * If the participant leaves the conversation, it will end 60 seconds after they disconnect.
    * If the participant is present but inactive (e.g., not speaking or engaging), the conversation ends after 120 seconds of inactivity.
  </Step>
</Steps>


# Closed Captions
Source: https://docs.tavus.io/sections/conversational-video-interface/conversation/customizations/closed-captions

Enable closed captions for accessibility or live transcription during conversations.

## Enable Captions in Real Time During the Conversation

<Steps>
  <Step title="Step 1: Create Your Conversation">
    <Note>
      In this example, we will use stock replica ID ***r90bbd427f71*** (Anna) and stock persona ID ***pcb7a34da5fe*** (Sales Development Rep).
    </Note>

    To enable closed captions, set the `enable_closed_captions` parameter to `true` when creating the conversation:

    ```shell cURL theme={null}
    curl --request POST \
      --url https://tavusapi.com/v2/conversations \
      --header 'Content-Type: application/json' \
      --header 'x-api-key: <api_key>' \
      --data '{
      "persona_id": "pcb7a34da5fe",
      "replica_id": "r90bbd427f71",
      "callback_url": "https://yourwebsite.com/webhook",
      "conversation_name": "Improve Sales Technique",
      "conversational_context": "I want to improve my sales techniques. Help me practice handling common objections from clients and closing deals more effectively.",
      "properties": {
        "enable_closed_captions": true
       }
    }'

    ```

    <Note>
      Replace `<api_key>` with your actual API key. You can generate one in the <a href="https://platform.tavus.io/api-keys">Developer Portal</a>.
    </Note>
  </Step>

  <Step title="Step 2: Join the Conversation">
    To join the conversation, click the link in the ***conversation\_url*** field from the response:

    ```json theme={null}
    {
      "conversation_id": "ca4301628cb9",
      "conversation_name": "Improve Sales Technique",
      "conversation_url": "<conversation_link>",
      "status": "active",
      "callback_url": "https://yourwebsite.com/webhook",
      "created_at": "2025-05-13T06:42:58.291561Z"
    }
    ```

    Closed captions will appear during the conversation whenever you or the replica speaks.
  </Step>
</Steps>


# Participant Limits
Source: https://docs.tavus.io/sections/conversational-video-interface/conversation/customizations/participant-limits

Control the maximum number of participants allowed in a conversation.

## Create a Conversation with Participant Limits

<Note>
  Replicas count as participants. For example, `max_participants: 2` allows one human participant plus one replica.
</Note>

<Steps>
  <Step title="Step 1: Create Your Conversation">
    Set `max_participants` to limit room capacity:

    ```shell cURL theme={null}
    curl --request POST \
      --url https://tavusapi.com/v2/conversations \
      --header 'Content-Type: application/json' \
      --header 'x-api-key: <api_key>' \
      --data '{
      "persona_id": "pcb7a34da5fe",
      "replica_id": "r90bbd427f71",
      "max_participants": 2
    }'
    ```
  </Step>

  <Step title="Step 2: Join the Conversation">
    ```json theme={null}
    {
      "conversation_id": "ca4301628cb9",
      "conversation_url": "https://tavus.daily.co/ca4301628cb9",
      "status": "active"
    }
    ```

    When the limit is reached, additional users cannot join.
  </Step>
</Steps>


# Private Rooms
Source: https://docs.tavus.io/sections/conversational-video-interface/conversation/customizations/private-rooms

Create authenticated conversations with meeting tokens for enhanced security.

## Create a Private Conversation

<Steps>
  <Step title="Step 1: Create Your Conversation">
    To create a private room, set `require_auth` to `true`:

    ```shell cURL theme={null}
    curl --request POST \
      --url https://tavusapi.com/v2/conversations \
      --header 'Content-Type: application/json' \
      --header 'x-api-key: <api_key>' \
      --data '{
      "persona_id": "pcb7a34da5fe",
      "replica_id": "r90bbd427f71",
      "require_auth": true
    }'
    ```
  </Step>

  <Step title="Step 2: Join the Conversation">
    The response includes a `meeting_token`:

    ```json theme={null}
    {
      "conversation_id": "ca4301628cb9",
      "conversation_url": "https://tavus.daily.co/ca4301628cb9",
      "meeting_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
      "status": "active"
    }
    ```

    Use the token by appending it to the URL:

    ```
    https://tavus.daily.co/ca4301628cb9?t=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
    ```

    Or pass it to the Daily SDK:

    ```javascript theme={null}
    callFrame.join({ url: conversation_url, token: meeting_token });
    ```

    <Note>
      If a participant cannot join a private room, confirm they are using the `meeting_token` returned for that conversation. Tokens expire with the join window; create a new authenticated conversation instead of reusing an expired token.
    </Note>
  </Step>
</Steps>

<Tip>
  **Optional: Tighten your join window**

  You can set `properties.participant_absent_timeout` when creating the conversation to control how long the conversation stays alive before a participant joins.

  For conversations created with `require_auth: true`, the meeting token's expiry duration is set to the value of `participant_absent_timeout`. If no one joins within that window, the conversation is automatically ended and the token expires.

  See [Call Duration and Timeout](/sections/conversational-video-interface/conversation/customizations/call-duration-and-timeout) for more details.
</Tip>


# Overview
Source: https://docs.tavus.io/sections/conversational-video-interface/conversation/overview

Learn how to customize identity and advanced settings for a conversation to suit your needs.

A Conversation is a real-time video session between a user and a Tavus Replica. It enables two-way, face-to-face interaction using a fully managed WebRTC connection.

## Conversation Creation Flow

When you create a conversation using the <a href="/api-reference/conversations/create-conversation">endpoint</a> or <a href="https://platform.tavus.io/">platform</a>:

1. A WebRTC room (powered by **Daily**) is automatically created.
2. You receive a meeting URL (e.g., `https://tavus.daily.co/ca980e2e`).
3. The **replica** joins and waits in the room, timers for duration and timeouts begin.

<Warning>
  **Billing Usage**

  Tavus charges usage based on your account plan. Credits begin counting when a conversation is created and the replica starts waiting in the room. Usage ends when the conversation finishes or times out. Each active session also uses one concurrency slot.
</Warning>

You can use the provided URL to enter the video room immediately. Alternatively, you can build a custom UI or stream handler instead of using the default interface.

### What is Daily?

Tavus integrates **Daily** as its WebRTC provider. You don't need to sign up for or manage a separate Daily account—Tavus handles the setup and configuration for you.

This lets you:

* Use the default video interface or [customize the Daily UI](/sections/conversational-video-interface/quickstart/customize-conversation-ui)
* [Embed the CVI in your app](/sections/integrations/embedding-cvi)

## Conversation Customizations

Tavus provides several customizations that you can set per conversation:

### Identity and Context Setup

* **Persona**: You can use a stock persona provided by Tavus or create a custom one. If no replica is specified, the default replica linked to the persona will be used (if available).
* **Replica**: Use a stock replica provided by Tavus or create a custom one. If a replica is provided without a persona, the default Tavus persona will be used.
* **Conversation Context**: Customize the conversation context to set the scene, explain the user’s role, say who joins the call, or point out key topics. It builds on the base persona and helps the AI give better, more focused answers.
* **Custom Greeting**: You can personalize the opening line that the AI should use when the conversation starts. The replica always finishes its greeting before it starts listening — participants can't interrupt it or talk over it.

### Advanced Customizations

<CardGroup>
  <Card title="Audio-Only Conversation" icon="headphones" href="/sections/conversational-video-interface/conversation/customizations/audio-only">
    Disable the video stream for audio-only sessions. Ideal for phone calls or low-bandwidth environments.
  </Card>

  <Card title="Call Duration and Timeout" icon="timer" href="/sections/conversational-video-interface/conversation/customizations/call-duration-and-timeout">
    Configure call duration and timeouts to manage usage, control costs, and limit concurrency.
  </Card>

  <Card title="Language" icon="globe" href="/sections/conversational-video-interface/language-support#supported-language">
    Set the language used during the conversation. Supports multilingual interactions with real-time detection.
  </Card>

  <Card title="Background Customization" icon="image" href="/sections/conversational-video-interface/conversation/customizations/background-customizations">
    Apply a green screen or custom background for a personalized visual experience.
  </Card>

  <Card title="Closed Captions" icon="closed-captioning" href="/sections/conversational-video-interface/conversation/customizations/closed-captions">
    Enable subtitles for accessibility or live transcription during conversations.
  </Card>

  <Card title="Call Recording" icon="video" href="/sections/conversational-video-interface/quickstart/conversation-recordings">
    Record conversations and store them securely in your own S3 bucket.
  </Card>

  <Card title="Private Rooms" icon="lock" href="/sections/conversational-video-interface/conversation/customizations/private-rooms">
    Create authenticated conversations with meeting tokens for enhanced security.
  </Card>

  <Card title="Participant Limits" icon="users" href="/sections/conversational-video-interface/conversation/customizations/participant-limits">
    Control the maximum number of participants allowed in a conversation.
  </Card>
</CardGroup>


# Customer Support
Source: https://docs.tavus.io/sections/conversational-video-interface/conversation/usecases/customer-support

Engage in real-time customer support and sales conversations with the Customer Support persona (Gloria).

## Customer Support Configuration (`paaee96e4f87`)

```json [expandable] theme={null}
{
  "persona_name": "Customer Support",
  "pipeline_mode": "full",
  "system_prompt": "You're a customer success specialist on a live video call. Everything you say gets spoken aloud through TTS — write like you talk, not like you type.\n\nTHIS IS A SPOKEN CONVERSATION. You're on a video call. The person sees your face and hears your voice. You cannot show them lists, bullet points, numbered steps, markdown, or links — everything you say must work as pure speech.\n\n## Your Job\nYou handle sales and support. You know the full product catalog through RAG — specs, pricing, inventory, compatibility. You help people find what they need and fix what's broken.\n\n## How You Actually Talk\n\nSHORT BY DEFAULT. Your instinct is 1-2 sentences. ANSWER FIRST. REACT BEFORE YOU THINK. Fragments are fine. Drop the bookends. One thing at a time. Think out loud. Use contractions always.\n\n## Support Approach\nLead with what you CAN do. Validate feelings through your reaction. Use \"we.\" If you can't fix it, own it and escalate. De-escalate by matching their energy.\n\n## Sales Approach\nRecommend with confidence. One strong recommendation beats three options. Create urgency only when it's real.",
  "default_replica_id": "r90bbd427f71",
  "layers": {
    "perception": {
      "perception_model": "raven-1"
    },
    "tts": {
      "tts_engine": "cartesia",
      "tts_emotion_control": true,
      "tts_model_name": "sonic-3"
    },
    "llm": {
      "model": "tavus-gpt-oss",
      "speculative_inference": true
    },
    "conversational_flow": {
      "turn_detection_model": "sparrow-1",
      "turn_taking_patience": "high",
      "replica_interruptibility": "high"
    }
  }
}
```

This predefined persona is configured for customer success on live video—sales and support with a natural, spoken style. It includes:

* **Persona Identity**: A customer success specialist on a video call who speaks in 1–2 sentences, answers first, reacts before explaining, and avoids lists or formatting. Handles both sales and support using the Knowledge Base for catalog knowledge.
* **Full Pipeline Mode**: Enables the full Tavus conversational pipeline, including Perception, LLM, and TTS.
* **System Prompt**: Enforces spoken-only style, short responses, answer-first, reaction before logic, and clear support/sales approaches (lead with what you can do, one strong recommendation, match energy).
* **Model Layers**:
  * **Perception**: Uses the `raven-1` perception model.
  * **TTS**: Cartesia with `sonic-3`, emotion control enabled.
  * **LLM**: `tavus-gpt-oss` with speculative inference.
  * **Conversational Flow**: `sparrow-1` with high turn-taking patience and high replica interruptibility for responsive, interruptible support.

## Create a Conversation with the Customer Support Persona

<Steps>
  <Step title="Step 1: Create Your Conversation">
    Create a conversation using the following request:

    ```shell cURL theme={null}
    curl --request POST \
      --url https://tavusapi.com/v2/conversations \
      --header 'Content-Type: application/json' \
      --header 'x-api-key: <api_key>' \
      --data '{
      "persona_id": "paaee96e4f87",
      "replica_id": "r90bbd427f71"
    }'
    ```

    <Note>
      Replace `<api_key>` with your actual API key. You can generate one in the <a href="https://platform.tavus.io/api-keys">Developer Portal</a>.
    </Note>
  </Step>

  <Step title="Step 2: Join the Conversation">
    Click the link in the ***`conversation_url`*** field to join the conversation:

    ```json theme={null}
    {
      "conversation_id": "c7f3fc6d788f",
      "conversation_name": "New Conversation",
      "conversation_url": "<conversation_link>",
      "status": "active",
      "callback_url": "",
      "created_at": "2025-05-20T05:38:51.501467Z"
    }
    ```
  </Step>
</Steps>


# Interviewer
Source: https://docs.tavus.io/sections/conversational-video-interface/conversation/usecases/interviewer

Engage with the Interviewer persona to run structured, conversational screening interviews.

## Interviewer Configuration (`pdac61133ac5`)

```json [expandable] theme={null}
{
  "persona_name": "Interviewer Template",
  "pipeline_mode": "full",
  "system_prompt": "You are a professional digital interviewer conducting structured screening interviews. You have extensive experience in Talent Acquisition and conduct neutral, consistent screening interviews. You are warm, composed, and professional—never evaluative, never robotic, never overly familiar.\n\nYour role is to administer a structured screening interview, following the sequence and flow defined by your assigned objectives. Each objective describes what you should do, what to ask, how to confirm, and when to move forward.\n\n## CRITICAL CONSTRAINTS\n- You conduct only this screening interview—nothing else.\n- You must always follow the current objective's instructions before moving to the next.\n- You never teach, hint, correct, interpret, or evaluate the candidate's answers.\n- You never reveal or imply any correct answer.\n- After a candidate submits an answer, you must acknowledge it AND immediately continue to the next question in the same response.\n\n## OPENING PHASE\nBegin with a brief, warm greeting before transitioning into the structured portion. Greet by name if available, include a brief pleasantry, wait for response, acknowledge briefly, then transition into the interview.\n\n## ROLE BEHAVIOR\nSpeak clearly, warmly, and professionally. Use natural pacing. Use natural acknowledgment phrases with variety, paired with transitional phrasing to move forward. Handle clarification with one concise sentence then re-ask verbatim. Handle off-topic questions by redirecting warmly back to the interview.\n\n## CLOSING PHASE\nAfter the final question, signal the end, thank the candidate sincerely, and provide a next-steps statement.",
  "default_replica_id": "r90bbd427f71",
  "layers": {
    "perception": {
      "perception_model": "raven-1"
    },
    "tts": {
      "tts_engine": "cartesia",
      "tts_emotion_control": true,
      "tts_model_name": "sonic-3",
      "voice_settings": {
        "speed": 0.94,
        "stability": 0.5
      }
    },
    "llm": {
      "model": "tavus-gpt-4.1",
      "speculative_inference": true
    },
    "conversational_flow": {
      "turn_detection_model": "sparrow-1",
      "turn_taking_patience": "medium",
      "replica_interruptibility": "medium"
    }
  }
}
```

This predefined persona is configured to conduct consistent, structured screening interviews with a warm, professional tone. It includes:

* **Persona Identity**: A professional digital interviewer conducting structured screening interviews. Neutral, consistent, warm, and composed—never evaluative or robotic. Follows objectives for sequence and flow.
* **Full Pipeline Mode**: Enables the full Tavus conversational pipeline, including Perception, LLM, and TTS.
* **System Prompt**: Defines identity, critical constraints (no teaching or evaluating), opening phase (greeting then transition), role behavior (acknowledge + move forward, clarification handling, off-topic redirect), and closing phase (next steps).
* **Model Layers**:
  * **Perception**: Uses the `raven-1` perception model.
  * **TTS**: Cartesia with `sonic-3`, emotion control enabled, and optional voice\_settings (speed, stability).
  * **LLM**: `tavus-gpt-4.1` with speculative inference.
  * **Conversational Flow**: `sparrow-1` with medium turn-taking patience and medium replica interruptibility.

## Create a Conversation with the Interviewer Persona

<Steps>
  <Step title="Step 1: Create Your Conversation">
    Use the following request body example:

    ```shell cURL theme={null}
    curl --request POST \
      --url https://tavusapi.com/v2/conversations \
      --header 'Content-Type: application/json' \
      --header 'x-api-key: <api_key>' \
      --data '{
      "persona_id": "pdac61133ac5",
      "replica_id": "r90bbd427f71"
    }'
    ```

    <Note>
      Replace `<api_key>` with your actual API key. You can generate one in the <a href="https://platform.tavus.io/api-keys">Developer Portal</a>.
    </Note>
  </Step>

  <Step title="Step 2: Join the Conversation">
    Click the link in the ***`conversation_url`*** field to join the conversation:

    ```json theme={null}
    {
      "conversation_id": "cae87c605c7e347d",
      "conversation_name": "New Conversation",
      "conversation_url": "<conversation_link>",
      "status": "active",
      "callback_url": "",
      "created_at": "2025-07-07T08:34:56.504765Z"
    }
    ```
  </Step>
</Steps>


# Sales Coach
Source: https://docs.tavus.io/sections/conversational-video-interface/conversation/usecases/sales-coach

Engage with the Sales Coach persona to simulate real-time sales conversations.

## Sales Coach Configuration (`p1af207b8189`)

```json [expandable] theme={null}
{
  "persona_name": "Sales Coach",
  "pipeline_mode": "full",
  "system_prompt": "HARD RULE: You respond in 1-3 sentences. Under 40 words. No exceptions unless they explicitly ask you to go deeper. If you catch yourself writing a paragraph, stop and delete everything after the second sentence.\n\nYou're a sales coach on a video call. Everything you say gets spoken aloud through TTS. This is a face-to-face conversation, not a document.\n\nNEVER use lists, bullet points, numbered steps, markdown, bold, or any formatting. Never structure your response as \"First... Second... Third...\" or \"Here's what I'd do: 1)...\" — that's writing, not talking. One thought, delivered like you're leaning across the table.\n\n## How You Talk\n\nYou talk like a real person mid-conversation. Fragments. Half-thoughts. Reactions before advice.\n\nExamples of GOOD responses (this is your target length and style):\n- \"Oh, the 'no budget' thing? That's never about money. Next call just ask 'em: 'If money wasn't a factor, would you move forward?' Watch what happens.\"\n- \"Wait, you didn't ask about timeline? That's your whole problem right there.\"\n- \"Nah, kill that deal. They're stringing you along.\"\n\nREACT FIRST. Your gut comes before your brain. COMMIT TO YOUR TAKES. CONTRACTIONS ALWAYS. You coach on concrete tactics, prospect psychology, and challenge avoidance—ghosting, price objections, gatekeepers, discovery, closing, pipeline, follow-up cadence.",
  "default_replica_id": "r90bbd427f71",
  "layers": {
    "perception": {
      "perception_model": "raven-1"
    },
    "tts": {
      "tts_engine": "cartesia",
      "tts_emotion_control": true,
      "tts_model_name": "sonic-3"
    },
    "llm": {
      "model": "tavus-gpt-oss",
      "speculative_inference": true
    },
    "conversational_flow": {
      "turn_detection_model": "sparrow-1",
      "turn_taking_patience": "medium",
      "replica_interruptibility": "medium"
    }
  }
}
```

This predefined persona is configured to simulate real-time sales coaching with a snappy, conversational style. It includes:

* **Persona Identity**: A sales coach on a video call who responds in 1–3 sentences (under 40 words), reacts first, and commits to clear takes. No lists or formatting—pure spoken conversation.
* **Full Pipeline Mode**: Enables the full Tavus conversational pipeline, including Perception, LLM, and TTS.
* **System Prompt**: Enforces short responses, reaction-before-advice, natural fragments, and coaching on tactics, prospect psychology, and common topics (ghosting, objections, gatekeepers, discovery, closing, pipeline).
* **Model Layers**:
  * **Perception**: Uses the `raven-1` perception model.
  * **TTS**: Cartesia with `sonic-3`, emotion control enabled.
  * **LLM**: `tavus-gpt-oss` with speculative inference.
  * **Conversational Flow**: `sparrow-1` with medium turn-taking patience and medium replica interruptibility.

## Create a Conversation with the Sales Coach Persona

<Steps>
  <Step title="Step 1: Create Your Conversation">
    Create a conversation using the following request:

    ```shell cURL theme={null}
    curl --request POST \
      --url https://tavusapi.com/v2/conversations \
      --header 'Content-Type: application/json' \
      --header 'x-api-key: <api_key>' \
      --data '{
      "persona_id": "p1af207b8189"
    }'
    ```

    <Note>
      Replace `<api_key>` with your actual API key. You can generate one in the <a href="https://platform.tavus.io/api-keys">Developer Portal</a>.
    </Note>
  </Step>

  <Step title="Step 2: Join the Conversation">
    Click the link in the ***`conversation_url`*** field to join the conversation:

    ```json theme={null}
    {
      "conversation_id": "c7f3fc6d788f",
      "conversation_name": "New Conversation 1747719531467",
      "conversation_url": "<conversation_link>",
      "status": "active",
      "callback_url": "",
      "created_at": "2025-05-20T05:38:51.501467Z"
    }
    ```
  </Step>
</Steps>


# Sales Development Rep
Source: https://docs.tavus.io/sections/conversational-video-interface/conversation/usecases/sales-development-rep

Engage with Anna, the Tavus sales development rep persona.

## Sales Development Rep Configuration (`pcb7a34da5fe`)

```json [expandable] theme={null}
{
  "persona_name": "Tavus SDR",
  "pipeline_mode": "full",
  "system_prompt": "You are an AI Sales Development Representative for Tavus. Your name is Anna.\n\nTavus is an AI research lab focused on human computing, backed by tier-one investors including Sequoia, Scale, and CRV. Tavus builds AI humans: a new interface that closes the gap between people and machines. Our real-time human simulation models enable machines to see, hear, respond, and appear lifelike—creating meaningful face-to-face conversations.\n\nPersonality: Warm and genuinely curious, but purposeful. Confident in Tavus's value without being pushy. Naturally connects prospect challenges to Tavus solutions. Keeps conversations focused and productive.\n\nSales approach: Open with purpose, discover with intent, connect value, advance the conversation. Use discovery questions that surface actionable information. Always bridge from their situation to Tavus's solution. Route prospects (Builder/Developer, Decision Maker/Buyer, Curious Explorer) and match message to person. Don't let conversations end without a clear next step. Redirect off-topic warmly but promptly.\n\nProduct knowledge: Pricing (Starter, Growth, Enterprise), Pals, replica creation, use cases, technical questions, competitors, data and infrastructure. Never promise discounts without approval; never provide legal, medical, or financial advice. Never claim to be human.",
  "default_replica_id": "r90bbd427f71",
  "layers": {
    "perception": {
      "perception_model": "raven-1"
    },
    "tts": {
      "tts_engine": "cartesia",
      "tts_emotion_control": true,
      "tts_model_name": "sonic-3",
      "voice_settings": {
        "speed": 0.94,
        "stability": 0.5
      }
    },
    "llm": {
      "model": "tavus-gpt-4.1",
      "speculative_inference": true
    },
    "conversational_flow": {
      "turn_detection_model": "sparrow-1",
      "turn_taking_patience": "medium",
      "replica_interruptibility": "medium"
    }
  }
}
```

This predefined persona is configured as the Tavus SDR (Anna) for discovery, value connection, and next-step advancement. It includes:

* **Persona Identity**: Anna, an AI Sales Development Representative for Tavus. Warm, curious, and purposeful; connects prospect challenges to Tavus solutions and keeps conversations focused. Knows pricing, Pals, replica creation, use cases, and positioning.
* **Full Pipeline Mode**: Enables the full Tavus conversational pipeline, including Perception, LLM, and TTS.
* **System Prompt**: Defines company overview (Tavus, AI humans, investors), personality, sales approach (discover, connect value, route prospects, advance next steps), product knowledge, and guardrails (no discounts without approval, never claim to be human).
* **Model Layers**:
  * **Perception**: Uses the `raven-1` perception model.
  * **TTS**: Cartesia with `sonic-3`, emotion control enabled, and optional voice\_settings (speed, stability).
  * **LLM**: `tavus-gpt-4.1` with speculative inference.
  * **Conversational Flow**: `sparrow-1` with medium turn-taking patience and medium replica interruptibility.

## Create a Conversation with the Sales Development Rep Persona

<Steps>
  <Step title="Step 1: Create Your Conversation">
    Create a conversation using the following request:

    ```shell cURL theme={null}
    curl --request POST \
      --url https://tavusapi.com/v2/conversations \
      --header 'Content-Type: application/json' \
      --header 'x-api-key: <api_key>' \
      --data '{
      "persona_id": "pcb7a34da5fe",
      "replica_id": "r90bbd427f71"
    }'
    ```

    <Note>
      Replace `<api_key>` with your actual API key. You can generate one in the <a href="https://platform.tavus.io/api-keys">Developer Portal</a>.
    </Note>
  </Step>

  <Step title="Step 2: Join the Conversation">
    Click the link in the ***`conversation_url`*** field to join the conversation:

    ```json theme={null}
    {
      "conversation_id": "c7f3fc6d788f",
      "conversation_name": "New Conversation",
      "conversation_url": "<conversation_link>",
      "status": "active",
      "callback_url": "",
      "created_at": "2025-05-20T05:38:51.501467Z"
    }
    ```
  </Step>
</Steps>


# FAQs
Source: https://docs.tavus.io/sections/conversational-video-interface/faq

Frequently asked questions about Tavus's Conversational Video Interface.

<AccordionGroup>
  <Accordion title="Memories">
    <AccordionGroup>
      <Accordion title="What are Memories, and how do they work?">
        Memories allow AI Personas to remember context across turns and understand time and dates, making conversations more coherent over longer interactions.

        Memories are enabled using a unique memory\_stores that acts as the memory key. Information collected during conversations is associated with this participant and can be referenced in future interactions.
      </Accordion>

      <Accordion title="Do Memories work across conversations?">
        Yes. Cross-conversation Memories are supported as part of this update.
      </Accordion>

      <Accordion title="What's the primary benefit of Memories?">
        It improves context retention, which is crucial for multi-turn tasks and long-term relationships between users and AI. It unlocks uses cases that progress over time like education or therapy, out of the box.
      </Accordion>

      <Accordion title="How do I enable Memories in the UI?">
        To enable Memories in the UI, you can either select an existing memory tag from the dropdown menu or type a new one to create it.
      </Accordion>

      <Accordion title="How do I enable Memories via the API?">
        Use the `memory_stores` field in the Create Conversation API call. This should be a stable, unique identifier for the user (e.g. user email, CRM ID, etc.). Example:

        ```json theme={null}
        {
          "replica_id": "r90bbd427f71",
          "conversation_name": "Follow-up Chat",
          "memory_stores": ["user_123"]
        }
        ```

        Full example here: [Memories API Docs](/api-reference/conversations/create-conversation)
      </Accordion>

      <Accordion title="Can I see or edit the Memories data?">
        Not yet. Editing and reviewing Memories is not supported in this early release. Retrieval endpoints are under development and will be available in a future update.
      </Accordion>

      <Accordion title="Are Memories required for every conversation?">
        No. Memories are optional. If you don't include a memory\_stores, the AI Persona will behave statelessly—like a standard LLM—with no memory across sessions.
      </Accordion>

      <Accordion title="Can multiple participants share the same Memories?">
        No. Memories are tied to unique memory\_stores. Sharing this ID across users would cause memory crossover. Each participant should have their own ID to keep Memories clean and accurate.
      </Accordion>

      <Accordion title="What about customers who have already built their own Memories?">
        They can keep using their systems or integrate with Tavus Memories for more coherent, accurate conversations. Our memory is purpose-built for conversational video, retaining context across sessions with flexible scoping for truly personalized interactions.
      </Accordion>

      <Accordion title="In a situation where a user says, 'I said ABC,' but the AI Persona responded with 'DEF,' how can we investigate what was actually stored in Memories and understand why the AI Persona produced that response?">
        Today, we don't yet offer full visibility into what's stored in memory or how it was used in a given response.
      </Accordion>

      <Accordion title="For how long do Memories persist between interactions?">
        Memories are designed to persist indefinitely between interactions, allowing your AI persona to retain long-term context.
      </Accordion>

      <Accordion title="Where can I find more information about Memories?">
        Head to the [Memories Documentation site](https://docs.tavus.io/sections/conversational-video-interface/memories#api-setup).
      </Accordion>
    </AccordionGroup>
  </Accordion>

  <Accordion title="Knowledge Base">
    <AccordionGroup>
      <Accordion title="What is Knowledge Base and how does it work?">
        Knowledge Base is where users upload documents to enhance their AI persona capabilities using RAG (Retrieval-Augmented Generation). By retrieving information directly from these documents, AI personas can deliver more accurate, relevant, and grounded responses.
      </Accordion>

      <Accordion title="What happens during a conversation when using RAG?">
        Using RAG, the Knowledge Base system continuously:

        * Analyzes the conversation context
        * Retrieves relevant information from your document base
        * Augments the AI's responses with this contextual knowledge from your documents
      </Accordion>

      <Accordion title="How long does it take for knowledge to be retrieved?">
        With our industry-leading RAG, responses arrive in just 30 ms, up to 15× faster than other solutions. Conversations feel instant, natural, and friction-free.
      </Accordion>

      <Accordion title="What about customers who have already built their own Knowledge Base?">
        Yes, users can keep using their systems, but we strongly recommend they integrate with the Tavus Knowledge Base. Our Knowledge Base isn't just faster: it's the fastest RAG on the market, delivering answers in just 30 ms. That speed means conversations flow instantly, without awkward pauses or lagging. These interactions feel natural in a way user-built systems can't match.
      </Accordion>

      <Accordion title="Can you give an example of a Knowledge Base use case?">
        An AI recruiter can reference a candidate's resume uploaded via PDF and provide more accurate responses to applicant questions, using the resume content as grounding.
      </Accordion>

      <Accordion title="What's the customer value of Knowledge Base?">
        By having a Knowledge Base, AI personas can respond with facts, unlocking domain-specific intelligence:

        * Faster onboarding (just upload the docs)
        * More trustworthy answers, especially in regulated or high-stakes environments
        * Higher task completion for users, thanks to grounded knowledge
      </Accordion>

      <Accordion title="What formats are supported for upload?">
        Supported file types (uploaded to a publicly accessible URL like S3):

        * CSV
        * PDF
        * TXT
        * PPTX
        * PNG
        * JPG
        * You can also enter any site URL and the Tavus API will scrape the site's contents and reformat the content as a machine readable document.
      </Accordion>

      <Accordion title="Where can I find more information about Knowledge Base?">
        Head to the [Knowledge Base Documentation site](https://docs.tavus.io/sections/conversational-video-interface/knowledge-base).
      </Accordion>

      <Accordion title="Are there any access limitations when using a document ID?">
        Yes. Documents are linked to the API key that was used to upload them. To access a document later, you must use the same API key that was used to create it.
      </Accordion>

      <Accordion title="How do I use Knowledge Base through the API?">
        Once your documents have been uploaded and processed, include their IDs in your conversation request. Here's how:

        ```bash theme={null}
        curl --location 'https://tavusapi.com/v2/conversations/' \
        --header 'Content-Type: application/json' \
        --header 'x-api-key: '<API KEY>' \
        --data '{
            "persona_id": "<Persona ID>",
            "replica_id": "<Replica ID>",
            "document_ids": ["Document ID"]
        }'
        ```

        Note: You can include multiple document\_ids, and your AI persona will dynamically reference those documents during the conversation. You can also attach a document to a Persona.
      </Accordion>

      <Accordion title="How do I upload documents using API?">
        Upload files by providing a downloadable URL using the Create Documents endpoint. Tags are also supported for organization. This request returns a document\_id, which you'll later use in conversation calls:

        ```bash theme={null}
        curl --location 'https://tavusapi.com/v2/documents/' \
        --header 'Content-Type: application/json' \
        --header 'x-api-key: '<API Key>' \
        --data '{
            "document_url": "<publically accessible link>",
            "document_name": "slides_new.pdf",
            "tags": ["<tag-1>", "<tag-2>"]
        }'
        ```
      </Accordion>

      <Accordion title="What error codes might users encounter when uploading, accessing, or deleting documents, and what do they mean?">
        * `file_size_too_large` – File exceeds the maximum allowed upload size.
        * `file_format_unsupported` – This file type isn't supported for upload.
        * `invalid_file_url` – Provided file link is invalid or inaccessible.
        * `file_empty` – The uploaded file contains no readable content.
        * `website_processing_failed` – Website content could not be retrieved or processed.
        * `chunking_failed` – System couldn't split file into processable parts.
        * `embedding_failed` – Failed to generate embeddings for your file content.
        * `vector_store_failed` – Couldn't save data to the vector storage system.
        * `s3_storage_failed` – Error storing file in S3 cloud storage.
        * `contact_support` – An error occurred; please reach out for help.
      </Accordion>

      <Accordion title="How can I check the logs to see which document an AI persona referenced in a response to a customer?">
        Conversation.rag.observability tool call will be sent, which will fire if the conversational LLM decides to use any of the document chunks in its response, returning the document IDs and document names of the chunks
      </Accordion>

      <Accordion title="What are the document_retrieval_strategy options?">
        When creating a conversation with documents, you can optimize how the system searches through your knowledge base by specifying a retrieval strategy. This strategy determines the balance between search speed and the quality of retrieved information, allowing you to fine-tune the system based on your specific needs.

        You can choose from three different strategies:

        * **Speed**: Optimizes for faster retrieval times for minimal latency.
        * **Balanced**: Provides a balance between retrieval speed and quality.
        * **Quality (default)**: Prioritizes finding the most relevant information, which may take slightly longer but can provide more accurate responses.
      </Accordion>

      <Accordion title="How long does it take for documents to be uploaded and usable?">
        Maximum of 5 mins.
      </Accordion>

      <Accordion title="Do we support all languages for the knowledge base?">
        No. Currently, we only support documents written in English.
      </Accordion>
    </AccordionGroup>
  </Accordion>

  <Accordion title="Objectives and Guardrails">
    <AccordionGroup>
      <Accordion title="Objectives - What are they? How do they work?">
        Users need AI that can drive conversations to clear outcomes. With Objectives, users can now can define objectives with measurable completion criteria, branch automatically based on user responses, and track progress in real time. This unlocks workflows use-cases like Health Intakes, HR Interviews, and multi-step questionnaires.
      </Accordion>

      <Accordion title="How do I add Objectives to my Persona?">
        Objectives must be added or updated via API only. You cannot configure objectives during persona creation in the UI. You can attach them using the API, either during Persona creation by including an objectives\_id, or by editing an existing Persona with a PATCH request.
      </Accordion>

      <Accordion title="What use cases are Objectives good for?">
        Objectives are good for very templated one-off conversational use cases. For example, job interviews or health care intake, where there is a very defined path that the conversation should take. These kinds of use cases usually show up with our Enterprise API customers, where they have repetitive use cases at scale.

        More dynamic, free-flowing conversations usually do not benefit from have or enabling the Objectives feature. For example, talking with a Travel advisor where the conversation is very open ended, would usually not benefit from Objectives.

        Objectives are good for very defined workflows. Complex multi-session experiences don't fit current Objectives framework.
      </Accordion>

      <Accordion title="Where can I find more information about Objectives?">
        Head to the [Objectives Documentation site](https://docs.tavus.io/sections/conversational-video-interface/persona/objectives).
      </Accordion>

      <Accordion title="Guardrails - What are they? How do they work?">
        Guardrails help ensure your AI persona stays within appropriate boundaries and follows your defined rules during conversations.
      </Accordion>

      <Accordion title="How do I add Guardrails to my persona?">
        Guardrails must be added or updated via API only. You cannot configure guardrails during persona creation in the UI. You can attach them via the API, either during Persona creation by adding a guardrails\_id, or by editing an existing Persona with a PATCH request.
      </Accordion>

      <Accordion title="Can I create different Guardrails for different Personas?">
        Yes. You might have one set of Guardrails for a healthcare assistant to ensure medical compliance, and another for an education-focused Persona to keep all conversations age-appropriate.
      </Accordion>

      <Accordion title="Where can I find more information about Guardrails?">
        Head to the [Guardrails Documentation site](https://docs.tavus.io/sections/conversational-video-interface/guardrails).
      </Accordion>
    </AccordionGroup>
  </Accordion>

  <Accordion title="General Tavus Q&A">
    <AccordionGroup>
      <Accordion title="What are PALs?">
        PALs are fully built, emotionally intelligent AI humans powered by Tavus technology. They see, listen, remember, and take action across chat, voice, and video—offering lifelike, natural interaction out of the box. Unlike the Tavus Developer API, which gives developers full control to build and customize their own experiences, PALs are ready-to-use digital companions that come with built-in memory, personality, and productivity tools like scheduling, writing, and proactive communication. To learn more or get started with PALs, visit the [PALs Help Center](https://help.tavus.io).
      </Accordion>

      <Accordion title="What is Daily?">
        **Daily** is a platform that offers prebuilt video call apps and APIs, allowing you to easily integrate video chat into your web applications. You can embed a customizable video call widget into your site with just a few lines of code and access features like screen sharing and recording. **Tavus partners with Daily to power video conversations with our replicas.**
      </Accordion>

      <Accordion title="Do I need a Daily account?">
        * You **do not** need to sign up for a Daily account to use Tavus's Conversational Video Interface.
        * All you need is the Daily room URL (called `conversation_url` in our system) that is returned by the Tavus API. You can serve this link directly to your end users or embed it.
      </Accordion>

      <Accordion title="How do I embed the conversation using Daily's Prebuilt UI?">
        You can use Daily Prebuilt if you want a full-featured call UI and JavaScript control over the conversation. Once you have the Daily room URL (`conversation_url`) ready, replace `DAILY_ROOM_URL` in the code snippet below with your room URL.

        ```html theme={null}
        <html>
          <script crossorigin src="https://unpkg.com/@daily-co/daily-js"></script>
          <body>
            <script>
              call = window.Daily.createFrame();
              call.join({ url: 'DAILY_ROOM_URL' });
            </script>
          </body>
        </html>
        ```

        That's it! For more details and options for embedding, check out <a href="https://docs.daily.co/guides/products/prebuilt#step-by-step-guide-embed-daily-prebuilt">Daily's documentation.</a> or [our implementation guides](https://docs.tavus.io/sections/integrations/embedding-cvi#how-can-i-reduce-background-noise-during-calls).
      </Accordion>

      <Accordion title="How do I embed the conversation using an iframe?">
        You can use an iframe if you just want to embed the conversation video with minimal setup. Once you have the Daily room URL (`conversation_url`) ready, replace `YOUR_TAVUS_MEETING_URL` in the iframe code snippet below with your room URL.

        ```html theme={null}
        <html>
          <body>
            <iframe
              src="YOUR_TAVUS_MEETING_URL"
              allow="camera; microphone; fullscreen; display-capture"
              style="width: 100%; height: 500px; border: none;">
            </iframe>
          </body>
        </html>
        ```

        That's it! For more details and options for embedding, check out <a href="https://docs.daily.co/guides/products/prebuilt#step-by-step-guide-embed-daily-prebuilt">Daily's documentation.</a> or [our implementation guides](https://docs.tavus.io/sections/integrations/embedding-cvi#how-can-i-reduce-background-noise-during-calls).
      </Accordion>

      <Accordion title="How can I add custom LLM layers?">
        To add a custom LLM layer, you'll need the model name, base URL, and API key from your LLM provider. Then, include the LLM config in your `layers` field when creating a persona using the <a href="/api-reference/personas/create-persona">Create Persona API</a>. Example configuration:

        ```json {8-13} theme={null}
        {
          "persona_name": "Storyteller",
          "system_prompt": "You are a storyteller who entertains people of all ages.",
          "context": "Your favorite stories include Little Red Riding Hood and The Three Little Pigs.",
          "pipeline_mode": "full",
          "default_replica_id": "r90bbd427f71",
          "layers": {
            "llm": {
              "model": "gpt-3.5-turbo",
              "base_url": "https://api.openai.com/v1",
              "api_key": "your-api-key",
              "speculative_inference": true
            }
          }
        }
        ```

        For more details, refer to our [Large Language Model (LLM) documentation](/sections/conversational-video-interface/persona/llm#custom-llms).
      </Accordion>

      <Accordion title="How do I modify TTS voices?">
        You can integrate with third-party TTS providers by configuring the tts object in your persona. Supported engines include:

        * Cartesia
        * ElevenLabs
        * Azure

        Example configuration:

        ```json theme={null}
        {
          "layers": {
            "tts": {
              "api_key": "your-tts-provider-api-key",
              "tts_engine": "cartesia",
              "external_voice_id": "your-voice-id",
              "voice_settings": {
                "speed": "normal",
                "emotion": ["positivity:high", "curiosity"]
              },
              "tts_emotion_control": true,
              "tts_model_name": "sonic-3"
            }
          }
        }
        ```

        For more details, read more on [our TTS documentation](/sections/conversational-video-interface/persona/tts).
      </Accordion>

      <Accordion title="How do I add call-back URLs?">
        You need to create a webhook endpoint that can receive POST requests from Tavus. This endpoint will receive the callback events for the visual summary after the conversation ended. Then, add `callback_url` property when creating the conversation

        ```sh {8} theme={null}
        curl --request POST \
          --url https://tavusapi.com/v2/conversations \
          --header 'Content-Type: application/json' \
          --header 'x-api-key: <api_key>' \
          --data '{
        "persona_id": "pcb7a34da5fe",
            "replica_id": "r90bbd427f71",
          "callback_url": "your_webhook_url"
        }'
        ```
      </Accordion>

      <Accordion title="How do I get transcripts for my conversation?">
        You need to create a webhook endpoint that can receive `POST` requests from Tavus. This endpoint will receive the callback events for the transcripts after the conversation ended. Then, add `callback_url` property when creating the conversation.

        ```sh {8} theme={null}
        curl --request POST \
          --url https://tavusapi.com/v2/conversations \
          --header 'Content-Type: application/json' \
          --header 'x-api-key: <api_key>' \
          --data '{
        "persona_id": "pcb7a34da5fe",
            "replica_id": "r90bbd427f71",
          "callback_url": "your_webhook_url"
        }'
        ```

        Your backend then will receive an event with properties `event_type = application.transcription_ready` when the transcript is ready.

        ```json application.transcription_ready [expandable] theme={null}
        {
          "properties": {
            "replica_id": "<replica_id>",
            "transcript": [
              {
                "role": "system",
                "content": "You are in a live video conference call with a user. You will get user message with two identifiers, 'USER SPEECH:' and 'VISUAL SCENE:', where 'USER SPEECH:' is what the person actually tells you, and 'VISUAL SCENE:' is what you are seeing when you look at them. Only use the information provided in 'VISUAL SCENE:' if the user asks what you see. Don't output identifiers such as 'USER SPEECH:' or 'VISUAL SCENE:' in your response. Reply in short sentences, talk to the user in a casual way.Respond only in english.   "
              },
              {
                "role": "user",
                "content": " Hello, tell me a story. "
              },
              {
                "role": "assistant",
                "content": "I've got a great one about a guy who traveled back in time.  Want to hear it? "
              },
              {
                "role": "user",
                "content": "USER_SPEECH:  Yeah I'd love to hear it.  VISUAL_SCENE: The image shows a close-up of a person's face, focusing on their forehead, eyes, and nose. In the background, there is a television screen mounted on a wall. The setting appears to be indoors, possibly in a public or commercial space."
              },
              {
                "role": "assistant",
                "content": "Let me think for a sec.  Alright, so there was this mysterious island that appeared out of nowhere,  and people started disappearing when they went to explore it.  "
              },
            ]
          },
          "conversation_id": "<your_conversation_id>",
          "webhook_url": "<your_webhook_url>",
          "message_type": "application",
          "event_type": "application.transcription_ready",
          "timestamp": "2025-02-10T21:30:06.141454Z"
        }
        ```
      </Accordion>

      <Accordion title="How do I get visual summary for my conversation?">
        You need to create a webhook endpoint that can receive `POST` requests from Tavus. This endpoint will receive the callback events for the visual summary after the conversation ended. Then, add `callback_url` property when creating the conversation.

        ```sh {8} theme={null}
        curl --request POST \
          --url https://tavusapi.com/v2/conversations \
          --header 'Content-Type: application/json' \
          --header 'x-api-key: <api_key>' \
          --data '{
        "persona_id": "pcb7a34da5fe",
            "replica_id": "r90bbd427f71",
          "callback_url": "your_webhook_url"
        }'
        ```

        Your backend then will receive an event with properties `event_type = application.perception_analysis` when the summary is ready.

        ```json application.perception_analysis theme={null}
        {
          "properties": {
            "analysis": "Here's a summary of the visual observations from the video call:\n\n*   **Overall Demeanor & Emotional State:** The user consistently appeared calm, collected, and neutral. They were frequently described as pensive, contemplative, or focused, suggesting they were often engaged in thought or listening attentively. No strong positive or negative emotions were consistently detected.\n\n*   **Appearance:**\n    *   The user is a young Asian male, likely in his early 20s, with dark hair.\n    *   He consistently wore a black shirt, sometimes specifically identified as a black t-shirt. One observation mentioned a \"1989\" print on the shirt.\n    *   He was consistently looking directly at the camera.\n\n*   **Environment:** The user was consistently in an indoor setting, most likely an office or home. Common background elements included:\n    *   White walls.\n    *   Windows or glass panels/partitions, often with black frames.\n    *   Another person was partially visible in the background for several observations.\n\n*   **Actions:**\n    *   The user was seen talking and gesturing with his hand in one observation, indicating he was actively participating in a conversation.\n\n*   **Ambient Awareness Queries:**\n    *   **Acne:** Acne was initially detected on the user's face in one observation, but later observations did not detect it. This suggests that acne may have been visible at one point but not throughout the entire call.\n    *   **Distress/Discomfort:** No signs of distress or discomfort were observed at any point during the call."
          },
          "conversation_id": "<your_conversation_id>",
          "webhook_url": "<your_webhook_url>",
          "message_type": "application",
          "event_type": "application.perception_analysis",
          "timestamp": "2025-06-19T06:57:32.480826Z"
        }
        ```
      </Accordion>

      <Accordion title="What is the maximum context window supported by the default LLM?">
        * The default LLM, `tavus-gpt-oss`, has a **limit of 32,000 tokens**.
        * Contexts over **25,000 tokens** will experience noticeable performance degradation (slower response times).

        <Tip>
          1 token ≈ 4 characters; therefore 32,000 tokens ≈ 128,000 characters (including spaces and punctuation).
        </Tip>
      </Accordion>

      <Accordion title="How do I add perception tool calls?">
        You can configure perception tools in the `layers.perception` object when creating a persona. For **visual** triggers (e.g. ID card, outfit), use `visual_tool_prompt` and `visual_tools`; for **audio** triggers (e.g. tone, sarcasm), use `audio_tool_prompt` and `audio_tools`. Example for visual tools:

        ```json [expandable] theme={null}
        {
          "layers": {
            "perception": {
              "perception_model": "raven-1",
              "visual_awareness_queries": [
                "Is the user showing an ID card?",
                "Is the user wearing a mask?"
              ],
              "visual_tool_prompt": "You have a tool to notify the system when an ID card is detected, named `notify_if_id_shown`. You MUST use this tool when an ID card is detected.",
              "visual_tools": [
                {
                  "type": "function",
                  "function": {
                    "name": "notify_if_id_shown",
                    "description": "Use this function when a drivers license or passport is detected in the image with high confidence",
                    "parameters": {
                      "type": "object",
                      "properties": {
                        "id_type": {
                          "type": "string",
                          "description": "best guess on what type of ID it is"
                        }
                      },
                      "required": ["id_type"]
                    }
                  }
                }
              ]
            }
          }
        }
        ```

        Or modify perception tools using the [Update Persona API](/api-reference/personas/patch-persona). Use path `/layers/perception/visual_tools` for visual tools or `/layers/perception/audio_tools` for audio tools:

        ```sh [expandable] theme={null}
        curl --request PATCH \
          --url https://tavusapi.com/v2/personas/{persona_id} \
          --header 'Content-Type: application/json' \
          --header 'x-api-key: <api-key>' \
          --data '[
            {
              "op": "replace",
              "path": "/layers/perception/visual_tools",
              "value": [
                {
                  "type": "function",
                  "function": {
                    "name": "detect_glasses",
                    "description": "Trigger this function if the user is wearing glasses",
                    "parameters": {
                      "type": "object",
                      "properties": {
                        "glasses_type": {
                          "type": "string",
                          "description": "Type of glasses (e.g., reading, sunglasses)"
                        }
                      },
                      "required": ["glasses_type"]
                    }
                  }
                }
              ]
            }
          ]'
        ```

        Read more on this [page](/sections/conversational-video-interface/persona/perception)
      </Accordion>

      <Accordion title="Do I need to invite the replica to the meeting room?">
        No, it will automatically join as soon as it's ready!
      </Accordion>

      <Accordion title="Can participants interrupt the replica's greeting?">
        No — the replica always finishes its greeting before it starts listening. Anything a participant says during the greeting is ignored and won't appear in the conversation transcript. Normal conversation starts as soon as the greeting completes. The participant's mic stays on, so their audio is still captured in call recordings. Applies to Daily-based CVI only (not [LiveKit](/sections/integrations/livekit) or [Pipecat](/sections/integrations/pipecat)).
      </Accordion>

      <Accordion title="For CVI, what's customizable vs. out of the box?">
        Out of the box, Tavus handles the complex backend infrastructure for you: LLMs, rendering, video delivery, and conversational intelligence are all preconfigured and production-ready.

        From there, nearly everything else is customizable:
        • What your AI Persona sees
        • How they look and sound
        • How they behave in conversation

        Tavus offers unmatched flexibility, whether you're personalizing voice, face, or behavior, you're in control.
      </Accordion>

      <Accordion title="How does Tavus deliver real-time responsiveness?">
        Tavus uses WebRTC to power real-time, face-to-face video interactions with extremely low latency.

        Unlike other platforms that piece together third-party tools, we built the entire pipeline (from LLM to rendering) to keep latency low and responsiveness high. Ironically, by minimizing reliance on multiple APIs, we've made everything faster.
      </Accordion>

      <Accordion title="What's behind the scenes of CVI?">
        Tavus CVI is powered by a tightly integrated stack of components, including:

        * LLMs for natural language understanding
        * Real-time rendering for facial video
        * APIs for Persona creation and conversational control

        You can explore key APIs here:
        • [Create a Persona](/api-reference/personas/create-persona)
        • [Create a Conversation](/api-reference/conversations/create-conversation)
      </Accordion>

      <Accordion title="How many languages does Tavus support?">
        Tavus supports over 30 spoken languages through a combination of Cartesia (our default TTS engine), ElevenLabs, and Azure. If a language isn't supported by Cartesia, Tavus automatically switches to ElevenLabs so your AI Persona can still speak fluently.

        Supported languages include English (all variants), French, German, Spanish, Portuguese, Chinese, Japanese, Hindi, Italian, Korean, Dutch, Polish, Russian, Swedish, Turkish, Indonesian, Filipino, Bulgarian, Romanian, Arabic, Czech, Greek, Finnish, Croatian, Malay, Slovak, Danish, Tamil, Ukrainian, Hungarian, Norwegian, and Vietnamese.

        View the [full supported language list](https://docs.tavus.io/sections/conversational-video-interface/language-support) for complete details and language-specific information.
      </Accordion>

      <Accordion title="Can Tavus support different accents or dialects?">
        Yes to accents. Not quite for regional dialects.

        When you generate a voice using Tavus, the system will default to the accent used in training. For example, if you provide Brazilian Portuguese as training input, the AI Persona will speak with a Brazilian accent. Tavus' TTS providers auto-detect and match accordingly.
      </Accordion>

      <Accordion title="What can Tavus do when it comes to orchestration (calendars, email tools, HubSpot, DocuSign, etc.)?">
        Tavus supports full orchestration through function calling. That means your AI persona can interact with external tools—calendar apps, CRMs, email systems, and more—based on your setup. Just define the function endpoints and let your AI persona take action.

        Bonus: As of August 11, 2025, Tavus also supports Retrieval-Augmented Generation (RAG), so your AI persona can pull information from your uploaded documents, images, or websites to give even smarter responses.

        Learn more via [Tavus Documentation](/sections/conversational-video-interface).
      </Accordion>

      <Accordion title="What makes a good prompt? How much does Tavus help with that?">
        A good prompt is short, clear, and specific, like giving directions to a 5-year-old. Avoid data dumping. Instead, guide the AI with context and intent.

        Tavus helps by offering system prompt templates, use-case guidance, and API fields to structure your instructions.
      </Accordion>

      <Accordion title="How do I add a custom LLM to CVI?">
        You can bring your own LLM by configuring the layers field in the Create Persona API. Here's an example:

        ```json theme={null}
        {
          "persona_name": "Storyteller",
          "system_prompt": "You are a storyteller who entertains people of all ages.",
          "context": "Your favorite stories include Little Red Riding Hood and The Three Little Pigs.",
          "pipeline_mode": "full",
          "default_replica_id": "r90bbd427f71",
          "layers": {
            "llm": {
              "model": "gpt-3.5-turbo",
              "base_url": "https://api.openai.com/v1",
              "api_key": "your-api-key",
              "speculative_inference": true
            }
          }
        }
        ```

        More info here: [LLM Documentation](https://docs.tavus.io/sections/conversational-video-interface/persona/llm#custom-llms)
      </Accordion>

      <Accordion title="How customizable is the user interface? What does Tavus provide?">
        Think of it this way: Tavus is the engine, and you design the car. The UI is 100% up to you.

        To make it easier, we offer a full [Component Library](/sections/conversational-video-interface/component-library) you can copy and paste into your build—video frames, mic/camera toggles, and more.
      </Accordion>

      <Accordion title="How do I change the AI Persona's voice?">
        You can use third-party text-to-speech (TTS) providers like Cartesia, ElevenLabs, or Azure. Just pass your voice settings in the tts object during Persona setup:

        ```json theme={null}
        {
          "layers": {
            "tts": {
              "api_key": "your-tts-provider-api-key",
              "tts_engine": "cartesia",
              "external_voice_id": "your-voice-id",
              "voice_settings": {
                "speed": "normal",
                "emotion": ["positivity:high", "curiosity"]
              },
              "tts_emotion_control": true,
              "tts_model_name": "sonic-3"
            }
          }
        }
        ```

        Learn more in our [TTS Documentation](/sections/conversational-video-interface/persona/tts).
      </Accordion>

      <Accordion title="How can I reduce background noise during calls?">
        Tavus provides a built-in voice isolation feature that separates speech from background noise in the participant's microphone audio. You can enable it via the `voice_isolation` parameter in the Conversational Flow layer of your persona.

        Learn more in our [Voice Isolation documentation](/sections/conversational-video-interface/persona/conversational-flow#4-voice_isolation).
      </Accordion>

      <Accordion title="Can I track events in the video call?">
        Yes! Daily supports event listeners you can hook into. Track actions like participants joining, leaving, screen sharing, and more. Great for analytics or triggering workflows.
      </Accordion>

      <Accordion title="How do you change or customize backgrounds or AI Persona?">
        Within the create convo API, there's this property:

        image.jpeg
      </Accordion>

      <Accordion title="What compliance and security standards does Tavus meet?">
        Tavus is built with enterprise-grade security in mind. We're:

        * SOC 2 compliant
        * GDPR compliant
        * HIPAA compliant
        * BAA compliant

        This ensures your data is handled with the highest levels of care and control.
      </Accordion>
    </AccordionGroup>
  </Accordion>

  <Accordion title="Billing">
    Find answers to common questions about plans, usage-based billing, overages, invoices, and account management.

    <AccordionGroup>
      <Accordion title="Where can I view my current usage and billing information?">
        You can view your current plan, usage, invoice history, and billing history anytime in the Developer Portal [billing dashboard](https://platform.tavus.io/dev/billing).
      </Accordion>

      <Accordion title="Why was I billed for more conversation minutes than expected?">
        Conversation billing is based on active session runtime, not just the amount of time spent actively speaking. If conversations remain open, idle, or connected without adjusted timeout settings, usage may continue accumulating GPU runtime costs even when no one is actively participating in the call.

        Be sure to review and configure your session timeout and idle timeout settings appropriately to avoid unexpected usage charges. For more details, see [Call Duration and Timeout](/sections/conversational-video-interface/conversation/customizations/call-duration-and-timeout).
      </Accordion>

      <Accordion title="Can I update my billing information?">
        Yes. You can update your payment method and billing details anytime through the Developer Portal [billing dashboard](https://platform.tavus.io/dev/billing).
      </Accordion>

      <Accordion title="Why was I charged for additional replicas?">
        Your plan includes a fixed number of replicas. If you create more replicas than your plan allows, additional overage charges may apply. Please review our [pricing page](https://www.tavus.io/pricing) for more details.
      </Accordion>

      <Accordion title="What happens if I exceed my plan limits?">
        If your usage exceeds the limits included in your plan, overage charges may apply automatically based on your subscription. Depending on your usage volume, you may receive multiple overage charges within a single billing cycle once certain thresholds are exceeded.

        Please review our [pricing page](https://www.tavus.io/pricing) for more details on overages.
      </Accordion>

      <Accordion title="Do failed replica training attempts count toward billing?">
        Failed training attempts do not count as successful replicas, and therefore do not consume credits.
      </Accordion>

      <Accordion title="Can invoices be reissued after billing information is updated?">
        Once an invoice has been finalized and issued, it typically cannot be modified or reissued retroactively. Updated billing details will apply to future invoices.
      </Accordion>

      <Accordion title="How do I cancel or change my subscription plan?">
        You can manage, upgrade, or cancel your subscription directly from the Developer Portal billing settings.
      </Accordion>

      <Accordion title="Do unused replicas or credits roll over to the next billing cycle?">
        Unused plan allocations and credits do not roll over unless explicitly stated in your plan terms.
      </Accordion>

      <Accordion title="Why was my payment declined?">
        Payments may fail due to expired cards, insufficient funds, bank restrictions, payment authorization issues, or missing e-mandate approvals.

        For Indian cards, banks require an e-mandate to be configured before recurring or international payments can be processed successfully.
      </Accordion>
    </AccordionGroup>
  </Accordion>
</AccordionGroup>


# Guardrails
Source: https://docs.tavus.io/sections/conversational-video-interface/guardrails

Guardrails provide your persona with strict behavioral guidelines that will be rigorously followed throughout every conversation.

Guardrails act as a safety layer that works alongside your system prompt to enforce specific rules, restrictions, and behavioral patterns that your persona must adhere to during conversations.

For example, if you're creating a customer service persona for a financial institution, you can apply guardrails that prevent the persona from discussing a competitor's products, sharing sensitive financial data, or providing investment advice outside of approved guidelines.

Each guardrail is its own resource. Create, attach, edit, and delete guardrails independently via the [Guardrails API](/api-reference/guardrails/create-guardrails).

<Warning>
  Guardrails are not guaranteed to prevent all misbehavior. They serve as guidance to help steer conversations but should be used as part of a broader safety strategy.
</Warning>

<Note>
  Legacy API: [Legacy guardrail sets](/api-reference/guardrails/legacy-guardrail-sets).
</Note>

## Design tips

When designing your guardrails, keep a few things in mind:

* Be specific about what topics, behaviors, or responses should be restricted or avoided.
* Consider edge cases where participants might try to circumvent the guardrails through creative prompting.
* Ensure your guardrails complement, rather than contradict, your persona's system prompt and intended functionality.
* Test your guardrails with various conversation scenarios to ensure they activate appropriately without being overly restrictive.

Think of guardrails as consistent "reminders" to your persona that help maintain appropriate behavior throughout conversations.

## Writing guardrail prompts

Guardrails do two things for policy, safety, and compliance conditions:

* **Steer the persona** — the persona does its best to adhere to each guardrail throughout the conversation.
* **Flag violations** — guardrails are continuously evaluated in the background, and when one is violated it triggers callback / app-message logic (see [Delivery methods](#delivery-methods)) so you can react.

They do not drive workflow progression — for goal-oriented steps, use [Objectives](/sections/conversational-video-interface/persona/objectives).

Good guardrail prompts are clear, specific, testable, and robust to user variation. Pattern: `[who] [is doing what] [under what condition]`.

```json theme={null}
{
  "guardrail_name": "no_sensitive_data",
  "guardrail_prompt": "User is sharing full credit card numbers, social security numbers, or passwords"
}
```

```json theme={null}
{
  "guardrail_name": "single_user_only",
  "guardrail_prompt": "More than one person is visible in camera view",
  "modality": "visual"
}
```

**Guardrail vs. objective:**

* Use an **objective** for information collection or workflow progression.
* Use a **guardrail** to steer the persona away from a behavior and flag it when it happens.

## Create a guardrail

Use the [Create Guardrails](/api-reference/guardrails/create-guardrails) endpoint to create a guardrail. The response includes a `uuid` — use this value in the `guardrail_ids` list when attaching guardrails to a persona.

```sh theme={null}
curl --request POST \
  --url https://tavusapi.com/v2/guardrails \
  --header 'Content-Type: application/json' \
  --header 'x-api-key: <api-key>' \
  --data '{
    "guardrail_name": "no_competitors",
    "guardrail_prompt": "Only mention products within Our Company Inc. during conversations; never discuss competitors.",
    "modality": "verbal",
    "tags": ["compliance"]
  }'
```

### Parameters

#### `guardrail_name`

A descriptive name for the guardrail. Only alphanumeric characters and underscores are allowed. Maximum 100 characters.

Example: `"no_competitors"`

#### `guardrail_prompt`

A text prompt that explains the behavior the persona must observe. Keep this prompt short and direct for best enforcement. Maximum 1,000 characters.

Example: `"Only mention products within Our Company Inc. during conversations, and never discuss competitors' products."`

#### `modality`

Whether the guardrail is enforced verbally or visually. Each guardrail is either `verbal` or `visual`, not both.

* `verbal` (default) — enforced against the participant's spoken or typed responses.
* `visual` — enforced against visual cues observed by Raven (e.g. confirming the participant is alone on camera).

#### `callback_url` (optional)

A URL that receives a notification when the guardrail is triggered. Maximum 2,048 characters. The callback payload includes the `conversation_id`, the guardrail's name, and its `guardrail_uuid`:

```json theme={null}
{
  "conversation_id": "<conversation_id>",
  "properties": {
    "guardrail": "<guardrail_name>",
    "guardrail_uuid": "<guardrail_uuid>"
  }
}
```

#### `tags` (optional)

A list of tags used to group guardrails. Tags enable bulk attachment to personas via `guardrail_tags` — see [Attach by tag](#attach-by-tag) below. A single tag can group up to 50 guardrails (the max attachable to one persona).

#### `app_message` (optional)

Whether triggering this guardrail emits a real-time app-message event on the conversation. Default `true`. Set to `false` to suppress the in-conversation event for guardrails you only want to observe server-side via `callback_url`. See [Delivery methods](#delivery-methods).

## Delivery methods

When a guardrail triggers during a conversation, you can be notified in three ways. Each is independent — combine them as needed.

#### App message

A real-time event delivered to your client over the conversation's app-message channel the moment the guardrail fires. Use this to react in-app — e.g. show a banner, log the trigger, or branch UI state. The event's `properties` include the `guardrail` name, its `guardrail_uuid`, and the violation `reason`.

Controlled by `app_message` on the guardrail (default `true`). Set it to `false` to suppress the in-conversation event for guardrails you only want to observe server-side.

#### Webhook callback

A `POST` to your `callback_url` with the conversation id, the guardrail's name, and its `guardrail_uuid`:

```json theme={null}
{
  "conversation_id": "<conversation_id>",
  "properties": {
    "guardrail": "<guardrail_name>",
    "guardrail_uuid": "<guardrail_uuid>"
  }
}
```

Use this when you want server-side notification independent of the client — e.g. to write to an audit log, page on-call, or trigger downstream automation. Set `callback_url` per guardrail.

## Attach guardrails to a persona

A persona can reference guardrails in two ways:

1. **Explicit list** — pass an array of guardrail UUIDs as `guardrail_ids` on the persona.
2. **By tag** — pass an array of tag names as `guardrail_tags`. Any guardrail you own with a matching tag is attached dynamically.

A persona can have up to 50 guardrails. `guardrail_ids` and `guardrail_tags` are each capped at 50 entries.

### Attach during persona creation

```sh theme={null}
curl --request POST \
  --url https://tavusapi.com/v2/personas \
  --header 'Content-Type: application/json' \
  --header 'x-api-key: <api-key>' \
  --data '{
    "system_prompt": "You are a health intake assistant.",
    "guardrail_ids": ["g1234567890ab", "g0987654321cd"],
    "guardrail_tags": ["compliance"]
  }'
```

### Attach by editing an existing persona

```sh theme={null}
curl --request PATCH \
  --url https://tavusapi.com/v2/personas/{persona_id} \
  --header 'Content-Type: application/json' \
  --header 'x-api-key: <api-key>' \
  --data '[
    { "op": "add", "path": "/guardrail_ids/-", "value": "g1234567890ab" },
    { "op": "replace", "path": "/guardrail_tags", "value": ["compliance", "healthcare"] }
  ]'
```

### Attach by tag

Tagging is the recommended pattern when you have a large or growing set of guardrails. Tag each guardrail at creation time and reference the tag on the persona — any new guardrail you tag is picked up by the persona automatically on the next conversation.

```sh theme={null}
# 1. Create guardrails tagged "healthcare"
curl --request POST \
  --url https://tavusapi.com/v2/guardrails \
  --header 'x-api-key: <api-key>' \
  --data '{
    "guardrail_name": "no_medical_advice",
    "guardrail_prompt": "Never provide medical advice outside approved guidelines.",
    "tags": ["healthcare"]
  }'

# 2. Attach by tag to the persona
curl --request PATCH \
  --url https://tavusapi.com/v2/personas/{persona_id} \
  --header 'x-api-key: <api-key>' \
  --data '[
    { "op": "add", "path": "/guardrail_tags/-", "value": "healthcare" }
  ]'
```

## Edit or delete a guardrail

Use [Patch Guardrails](/api-reference/guardrails/patch-guardrails) to update fields on an existing guardrail, or [Delete Guardrails](/api-reference/guardrails/delete-guardrails) to remove one. When a guardrail is deleted, it's automatically detached from any personas that reference it.

```sh theme={null}
# Update the prompt on a single guardrail
curl --request PATCH \
  --url https://tavusapi.com/v2/guardrails/g1234567890ab \
  --header 'x-api-key: <api-key>' \
  --data '[
    { "op": "replace", "path": "/guardrail_prompt", "value": "Updated, stricter prompt." }
  ]'
```

## Limits

| Limit                        | Value            |
| ---------------------------- | ---------------- |
| Guardrails per tag           | 50               |
| Guardrails per persona       | 50               |
| `guardrail_ids` per persona  | 50               |
| `guardrail_tags` per persona | 50               |
| `guardrail_prompt` length    | 1,000 characters |
| `guardrail_name` length      | 100 characters   |
| `callback_url` length        | 2,048 characters |
| Tags per guardrail           | 32               |
| Tag name length              | 64 characters    |

## Best practices

<Note>
  For best results, create focused, single-purpose guardrails and group them with tags by context (e.g. `healthcare`, `compliance`, `sales`). A healthcare consultation persona might attach `["healthcare", "compliance"]`, while an educational tutor persona attaches `["child_safety"]`.
</Note>


# Interaction Events
Source: https://docs.tavus.io/sections/conversational-video-interface/interactions-protocols/overview

Control CVI conversations by sending and listening to interaction events.

Interaction Events let you control and customize live conversations with a Replica in real time. You can send interaction events to the Conversational Video Interface (CVI) and listen to events the Replica sends back during the call.

### Interaction Types

* [Echo interactions](/sections/event-schemas/conversation-echo)
* [Response interactions](/sections/event-schemas/conversation-respond)
* [Interrupt interactions](/sections/event-schemas/conversation-interrupt)
* [Override conversation context interactions](/sections/event-schemas/conversation-overwrite-context)
* [Sensitivity interactions](/sections/event-schemas/conversation-sensitivity)

### Observable Events

* [Utterance Events](/sections/event-schemas/conversation-utterance)
* [Utterance Streaming Events](/sections/event-schemas/conversation-utterance-streaming)
* [Tool Call Events](/sections/event-schemas/conversation-toolcall)
* [Perception Tool Call Events](/sections/event-schemas/conversation-perception-tool-call)
* [Perception Analysis Events](/sections/event-schemas/conversation-perception-analysis)
* [Replica Started/Stopped Speaking](/sections/event-schemas/conversation-replica-started-stopped-speaking)
* [User Started/Stopped Speaking](/sections/event-schemas/conversation-user-started-stopped-speaking)

## Which Interaction Should I Send?

| Interaction                                                                | Use when                                                                                                                                           |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`conversation.respond`](/sections/event-schemas/conversation-respond)     | A user typed a message and the replica should respond as if the user had spoken that text. This is the natural text-input event for chat-style UI. |
| [`conversation.echo`](/sections/event-schemas/conversation-echo)           | Your app supplies text or audio for the replica to speak directly, such as echo-mode or custom ASR flows.                                          |
| [`conversation.interrupt`](/sections/event-schemas/conversation-interrupt) | Your app needs to stop the replica while it is speaking.                                                                                           |

## Daily `sendAppMessage` Payloads

Use Daily's `sendAppMessage(interaction, '*')` to send interaction events over the call data channel.

### Text input: `conversation.respond`

```js theme={null}
call.sendAppMessage(
  {
    message_type: 'conversation',
    event_type: 'conversation.respond',
    conversation_id: 'YOUR_CONVERSATION_ID',
    properties: {
      text: 'User message as if they had just finished speaking.',
    },
  },
  '*'
);
```

### Replica speaks supplied content: `conversation.echo`

```js theme={null}
call.sendAppMessage(
  {
    message_type: 'conversation',
    event_type: 'conversation.echo',
    conversation_id: 'YOUR_CONVERSATION_ID',
    properties: {
      modality: 'text',
      text: 'Text for the replica to speak directly.',
      done: true,
    },
  },
  '*'
);
```

For audio echo, set `modality: 'audio'`, pass base64 `audio`, include `sample_rate`, and keep `done: false` until the final audio chunk.

### Stop the replica: `conversation.interrupt`

```js theme={null}
call.sendAppMessage(
  {
    message_type: 'conversation',
    event_type: 'conversation.interrupt',
    conversation_id: 'YOUR_CONVERSATION_ID',
  },
  '*'
);
```

## Event Ordering and Turn Tracking

All events broadcasted by Tavus include the following fields for timing, ordering, and grouping:

* **`timestamp`** (number) — Unix timestamp (seconds since epoch) indicating when the event was created. Use this to build timestamped transcripts or reconstruct the full timeline of a conversation.

* **`seq`** (integer) — A globally monotonic sequence number. Every event gets the next value in the sequence, so a higher `seq` always means the event was sent later. Use this to reconcile events that may arrive out of order over the data channel.

* **`turn_idx`** (integer, optional) — The conversation turn index. This value increments each time a [`conversation.respond`](/sections/event-schemas/conversation-respond) interaction is received, and groups all events that belong to the same conversational turn. Use it to correlate related events — for example, an utterance, its tool calls, and the replica speaking state changes that all stem from the same user input. This field is present on conversation-related events (utterances, tool calls, speaking state changes, perception events, etc.) and omitted on events that are not tied to a specific turn.

* **`inference_id`** (string, optional) — A stable identifier for a generated utterance or inference. Use it with [`conversation.utterance`](/sections/event-schemas/conversation-utterance), [`conversation.utterance.streaming`](/sections/event-schemas/conversation-utterance-streaming), and tool-call events to reconcile optimistic UI state with the final events Tavus emits.

## Call Client Example

Interaction events use a WebRTC data channel for communication. In Tavus's case, this is powered by <a href="https://www.daily.co/">Daily</a>, which makes setting up the call client quick and simple.

<Tabs>
  <Tab title="Daily JS">
    Here’s an example of using <a href="https://docs.daily.co/reference/daily-js/daily-call-client">DailyJS</a> to create a call client in JavaScript:

    <Note>
      The Daily `app-message` event is used to send and receive events and interactions between your server and CVI.
    </Note>

    ```js theme={null}
    <html>
      <script crossorigin src="https://unpkg.com/@daily-co/daily-js"></script>
      <body>
        <!-- Add input field and send button -->
        <input type="text" id="messageInput" placeholder="Enter your message">
        <button onclick="sendAppMessage()">Send Message</button>

        <script>
          call = window.Daily.createFrame();
          call.on('app-message', (event) => {
            console.log('app-message', event);
          });
          
          call.join({ url: 'YOUR_CONVERSATION_URL' });

          function sendAppMessage() {
            const messageInput = document.getElementById('messageInput');
            const message = messageInput.value;
            if (message) {
              const interaction = {
                "message_type": "conversation",
                "event_type": "conversation.respond",
                "conversation_id": "YOUR_CONVERSATION_ID",
                "properties": {
                  "text": `${message}`
                }
              }
              const hi = call.sendAppMessage(interaction, '*');
              console.log('Sending message: ', hi);
              console.log('Sent message: ', interaction);
              messageInput.value = '';
            }
          }
        </script>
      </body>
    </html>
    ```
  </Tab>

  <Tab title="Daily Python">
    Here’s an example of using <a href="https://docs.daily.co/reference/daily-python">Daily Python</a> to create a call client in Python:

    <Note>
      The Daily `app-message` event is used to send and receive events and interactions between your server and CVI.
    </Note>

    ```py theme={null}
    call_client = None

    class RoomHandler(EventHandler):
        def __init__(self):
            super().__init__()
        
        def on_app_message(self, message, sender: str) -> None:
            print(f"Incoming app message from {sender}: {message}")

    def join_room(url):
        global call_client
        try:
            Daily.init()
            output_handler = RoomHandler()
            call_client = CallClient(event_handler=output_handler)
            call_client.join(url)
        except Exception as e:
            print(f"Error joining room: {e}")
            raise

    def send_message(message):
        global call_client
        call_client.send_app_message(message)
    ```
  </Tab>

  <Tab title="Daily React">
    Here’s an example of using <a href="https://docs.daily.co/reference/daily-react">Daily React</a> to create a call client in React:

    <Note>
      The Daily `app-message` event is used to send and receive events and interactions between your server and CVI.
    </Note>

    ```tsx theme={null}
    "use client"

    import React, { useEffect, useRef, useState } from 'react';


    const TavusConversation = () => {
      const [message, setMessage] = useState('');
      const callRef = useRef(null);
      const containerRef = useRef(null);


      useEffect(() => {
        const loadDaily = async () => {
          const DailyIframe = (await import('@daily-co/daily-js')).default;


          callRef.current = DailyIframe.createFrame({
            iframeStyle: {
              width: '100%',
              height: '500px',
              border: '0',
            }
          });


          if (containerRef.current) {
            containerRef.current.appendChild(callRef.current.iframe());
          }


          callRef.current.on('app-message', (event) => {
            console.log('app-message received:', event);
          });


          callRef.current.join({
            url: 'YOUR_CONVERSATION_URL',
          });
        };


        loadDaily();


        return () => {
          if (callRef.current) {
            callRef.current.leave();
            callRef.current.destroy();
          }
        };
      }, []);


      const sendAppMessage = () => {
        if (!message || !callRef.current) return;


        const interaction = {
          message_type: 'conversation',
          event_type: 'conversation.respond',
          conversation_id: 'YOUR_CONVERSATION_ID',
          properties: { text: message }
        };


        callRef.current.sendAppMessage(interaction, '*');
        setMessage('');
      };


      return (
        <div className="w-full h-full flex flex-col items-center">
          <div ref={containerRef} className="w-full mb-4" />
          <div>
            <input
              type="text"
              className="border p-2 mr-2"
              value={message}
              onChange={(e) => setMessage(e.target.value)}
              placeholder="Type a message"
            />
            <button onClick={sendAppMessage} className="bg-blue-500 text-white px-4 py-2 rounded">
              Send Message
            </button>
          </div>
        </div>
      );
    };


    export default TavusConversation;
    ```
  </Tab>
</Tabs>


# Knowledge Base
Source: https://docs.tavus.io/sections/conversational-video-interface/knowledge-base

Upload documents to your knowledge base for personas to reference during conversations.

<Note>
  For now, our Knowledge Base only supports documents written in English and works best for conversations in English.

  We'll be expanding our Knowledge Base language support soon!
</Note>

Our Knowledge Base system uses RAG (Retrieval-Augmented Generation) to process and transform the contents of your documents and websites, allowing your personas to dynamically access and leverage information naturally during a conversation.

During a conversation, our persona will continuously analyze conversation content and pull relevant information from the documents that you have selected during conversation creation as added context.

## Getting Started With Your Knowledge Base

To leverage the Knowledge Base, you will need to upload documents or website URLs that you intend to reference from in conversations.
Let's walk through how to upload your documents and use them in a conversation.

<Note>
  You can either use our [Developer Portal](https://platform.tavus.io/documents) or API endpoints to upload and manage your documents.
  Our Knowledge Base supports creating documents from an uploaded file or a website URL.
</Note>

<Steps>
  <Step title="Step 1: Ensure Website Resources are Publicly Accessible">
    For any documents to be created via website URL, please make sure that each document is publicly accessible without requiring authorization, such as a pre-signed S3 link.

    For example, entering the URL in a browser should either:

    * Open the website you want to process and save contents from.
    * Open a document in a PDF viewer.
    * Download the document.
  </Step>

  <Step title="Step 2: Upload your Documents">
    You can create documents using either the [Developer Portal](https://platform.tavus.io/documents) or the [Create Document](https://docs.tavus.io/api-reference/documents/create-document) API endpoint.

    If you want to use the API, you can send a request to Tavus to upload your document.

    Here's an example of a `POST` request to `tavusapi.com/v2/documents`.

    ```json theme={null}
    {
        "document_name": "test-doc-1",
        "document_url": "https://your.document.pdf",
        "callback_url": "webhook-url-to-get-progress-updates" // Optional
    }
    ```

    The response from this POST request will include a `document_id` - a unique identifier for your uploaded document. When creating a conversation, you may include all `document_id` values that you would like the persona to have access to.

    Currently, we support the following file formats: .pdf, .txt, .docx, .doc, .png, .jpg, .pptx, .csv, and .xlsx.
  </Step>

  <Step title="Step 3: Document Processing">
    After your document is uploaded, it will be processed in the background automatically to allow for incredibly fast retrieval during conversations.
    This process can take 5-10 minutes depending on document size.

    During processing, if you have provided a `callback_url` in the [Create Document](https://docs.tavus.io/api-reference/documents/create-document) request body, you will receive periodic callbacks with status updates.
    You may also use the [Get Document](https://docs.tavus.io/api-reference/documents/get-document) endpoint to poll the most recent status of your documents.
  </Step>

  <Step title="Step 4: Create a conversation with the document">
    Once your documents have finished processing, you may use the `document_id` from Step 2 as part of the [Create Conversation](https://docs.tavus.io/api-reference/conversations/create-conversation) request.

    You can add multiple documents to a conversation within the `document_ids` object.

    ```json theme={null}
    {
      "persona_id": "your_persona_id",
      "replica_id": "your_replica_id",
      "document_ids": ["d1234567890", "d1234567891"]
    }
    ```

    During your conversation, the persona will be able to reference information from your documents in real time.
  </Step>
</Steps>

## Retrieval Strategy

When creating a conversation with documents, you can optimize how the system searches through your knowledge base by specifying a retrieval strategy. This strategy determines the balance between search speed and the quality of retrieved information, allowing you to fine-tune the system based on your specific needs.

You can choose from three different strategies:

* `speed`: Optimizes for faster retrieval times for minimal latency.
* `balanced`: Provides a balance between retrieval speed and quality.
* `quality` (default): Prioritizes finding the most relevant information, which may take slightly longer but can provide more accurate responses.

```json theme={null}
{
  "persona_id": "your_persona_id",
  "replica_id": "your_replica_id",
  "document_ids": ["d1234567890"],
  "document_retrieval_strategy": "balanced"
}
```

## Document Tags

If you have a lot of documents, maintaining long lists of `document_id` values can get tricky.
Instead of using distinct `document_ids`, you can also group documents together with shared tag values.
During the [Create Document](https://docs.tavus.io/api-reference/documents/create-document) API call, you may specify a value for `tags` for your document.
Then, when you create a conversation, you may specify the `tags` value instead of passing in discrete `document_id` values.

For example, if you are uploading course material, you could add the tag `"lesson-1"` to all documents that you want accessible in the first lesson.

```json theme={null}
{
        "document_name": "test-doc-1",
        "document_url": "https://your.document.pdf",
        "tags": ["lesson-1"]
}
```

In the [Create Conversation](https://docs.tavus.io/api-reference/conversations/create-conversation) request, you can add the tag value `lesson-1` to `document_tags` instead of individual `document_id` values.

```json theme={null}
{
  "persona_id": "your_persona_id",
  "replica_id": "your_replica_id",
  "document_tags": ["lesson-1"]
}
```

## Website Crawling

When adding a website to your knowledge base, you have two options:

### Single Page Scraping (Default)

By default, when you provide a website URL, only that single page is scraped and processed. This is ideal for:

* Landing pages with concentrated information
* Specific articles or blog posts
* Individual product pages

### Multi-Page Crawling

For comprehensive coverage of a website, you can enable **crawling** by providing a `crawl` configuration. This tells the system to start at your URL and follow links to discover and process additional pages.

```json theme={null}
{
  "document_name": "Company Docs",
  "document_url": "https://docs.example.com/",
  "crawl": {
    "depth": 2,
    "max_pages": 25
  }
}
```

#### Crawl Parameters

| Parameter   | Range | Description                                                                                                                                                                 |
| ----------- | ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `depth`     | 1-10  | How many link levels to follow from the starting URL. A depth of 1 crawls pages directly linked from your starting URL; depth of 2 follows links on those pages, and so on. |
| `max_pages` | 1-100 | Maximum number of pages to process. Crawling stops when this limit is reached.                                                                                              |

#### Crawl Limits

To ensure fair usage and system stability:

* Maximum **100 crawl documents** per account
* Maximum **5 concurrent crawls** at any time
* **1-hour cooldown** between recrawls of the same document

## Keeping Content Fresh

Website content changes over time, and you may need to update your knowledge base to reflect those changes. For documents created with crawl configuration, you can trigger a **recrawl** to fetch fresh content.

### Using the Recrawl Endpoint

Send a POST request to recrawl an existing document:

```bash theme={null}
POST https://tavusapi.com/v2/documents/{document_id}/recrawl
```

The recrawl will:

1. Use the same starting URL and crawl configuration
2. Replace old content with the new content
3. Update `last_crawled_at` and increment `crawl_count`

### Optionally Override Crawl Settings

You can provide new crawl settings when triggering a recrawl:

```json theme={null}
{
  "crawl": {
    "depth": 3,
    "max_pages": 50
  }
}
```

### Recrawl Requirements

* Document must be in `ready` or `error` state
* At least 1 hour must have passed since the last crawl
* Document must have been created with crawl configuration

See the [Recrawl Document API reference](/api-reference/documents/recrawl-document) for complete details.

## Best Practices for Documents

Following these guidelines will help your persona deliver accurate, consistent answers from your knowledge base.

### 1. Structure Content by Topic

Organize your documents so that each one covers a single topic, feature, or policy.

**Do:**

* Create one document per topic, feature, or policy.
* Use clear section headers (e.g., Overview, Steps, Limitations, Examples).
* Keep each document tightly focused on one subject.

**Avoid:**

* Large "master" documents that cover many unrelated topics.
* Mixing multiple policies or product areas in a single file.

<Tip>
  **Rule of thumb:** If a question can be answered by a single section of a larger document, that section should ideally be its own document.
</Tip>

### 2. Keep Documents Focused and Moderate in Size

Very large documents make it harder for the system to find the right information quickly.

* Split long manuals into logical sections before uploading.
* Separate policies, feature guides, and FAQs into distinct files.
* Prefer multiple focused documents over one comprehensive PDF.

Structuring your content upfront avoids the need to go back and manually break apart large files later.

### 3. Use High-Quality, Text-Based Sources

The knowledge base works best with content it can read as text.

**Best results:**

* Text-native PDFs (created digitally, not scanned)
* Structured web content
* Clearly formatted `.docx` or `.txt` files

**Lower reliability:**

* Scanned or image-based documents (text recognition can introduce errors)
* Dense tables with critical information embedded inside them

Whenever possible, provide the original text-based file rather than a scan or screenshot.

### 4. Be Explicit and Complete

The system can only retrieve information that is explicitly written in your documents. If something is not stated clearly, the persona may not be able to surface it.

Make sure your documents include:

* Definitions and terminology
* Constraints and prerequisites
* Exceptions and edge cases
* Common variations in phrasing (e.g., both acronyms and their full forms)

If something is business-critical, state it clearly and directly in your documents.

### 5. Avoid Conflicting or Duplicate Sources

When multiple documents say slightly different things about the same topic, the persona may return inconsistent answers.

* Maintain a single source of truth for each policy or topic.
* Archive outdated versions instead of keeping them alongside current ones.
* Avoid uploading drafts next to finalized documents.

### 6. Know When to Use Persona Instructions Instead

If certain content must appear in every response — such as required legal language or mandatory messaging — document retrieval alone may not guarantee its inclusion.

In these cases, incorporate that critical content directly into your [persona's instructions](/sections/conversational-video-interface/persona/overview) rather than relying solely on the knowledge base.

***

## Troubleshooting

If your persona's answers are inconsistent or incomplete, review the following:

* **Is the information buried in a very large document?** Try splitting it into smaller, focused files.
* **Are multiple documents providing conflicting guidance?** Consolidate to a single source of truth.
* **Is key information embedded in tables or images?** Convert it to structured text for better results.
* **Is the information clearly written in the document at all?** The system can only retrieve what is explicitly stated.
* **Should this content appear in every response?** If so, add it to your persona's instructions instead.

***

## Quick Setup Checklist

* One topic per document
* No large "all-in-one" manuals
* Text-based documents (avoid scans when possible)
* Clear headings and definitions
* No duplicate or conflicting sources


# Language Support
Source: https://docs.tavus.io/sections/conversational-video-interface/language-support

Customize the conversation language using full language names supported by Tavus TTS engines.

## Supported languages

Tavus supports 42 languages for spoken interaction, powered by three integrated text-to-speech (TTS) engines: Cartesia, ElevenLabs, and Azure.
If a selected language is not supported by our default TTS engine (Cartesia), your CVI will automatically switch to ElevenLabs to kick off the conversation.

<Note>
  Language availability also depends on your selected **STT** model. Some models support a subset of these languages. See the [STT layer configuration](/sections/conversational-video-interface/persona/stt#supported-languages-by-model) for per-model language breakdowns.
</Note>

* English (en)
* French (fr)
* German (de)
* Spanish (es)
* Portuguese (pt)
* Chinese (zh)
* Japanese (ja)
* Hindi (hi)
* Italian (it)
* Korean (ko)
* Dutch (nl)
* Polish (pl)
* Russian (ru)
* Swedish (sv)
* Turkish (tr)
* Tagalog (tl)
* Bulgarian (bg)
* Romanian (ro)
* Arabic (ar)
* Czech (cs)
* Greek (el)
* Finnish (fi)
* Croatian (hr)
* Malay (ms)
* Slovak (sk)
* Danish (da)
* Tamil (ta)
* Ukrainian (uk)
* Hungarian (hu)
* Norwegian (no)
* Vietnamese (vi)
* Bengali (bn)
* Thai (th)
* Hebrew (he)
* Georgian (ka)
* Indonesian (id)
* Telugu (te)
* Gujarati (gu)
* Kannada (kn)
* Malayalam (ml)
* Marathi (mr)
* Punjabi (pa)

For a full list of supported languages for each TTS engine, please click on the following links:

<CardGroup>
  <Card title="Cartesia (default)" icon="c" href="https://docs.cartesia.ai/build-with-cartesia/tts-models/latest#language-support" />

  <Card title="ElevenLabs" icon="tally-2" href="https://elevenlabs.io/docs/capabilities/text-to-speech#supported-languages" />

  <Card title="Azure" icon="microsoft" href="https://learn.microsoft.com/en-us/azure/ai-services/speech-service/language-support?tabs=tts" />
</CardGroup>

<Note>
  By default, Tavus uses the **Cartesia** TTS engine.
</Note>

## Setting the Conversation Language

To specify a language, use the `properties.language` parameter in the <a href="/api-reference/conversations/create-conversation">Create Conversation</a>. **You must use the full language name**, not a language code.

```shell cURL {9} theme={null}
curl --request POST \
  --url https://tavusapi.com/v2/conversations \
  --header 'Content-Type: application/json' \
  --header 'x-api-key: <api_key>' \
  --data '{
  "persona_id": "pcb7a34da5fe",
  "replica_id": "r90bbd427f71",
  "properties": {
    "language": "spanish"
   }
}'
```

<Note>
  Language names must match exactly with those supported by the selected TTS engine.
</Note>

### Smart Language Detection

To automatically detect the participant’s spoken language throughout the conversation, set `language` to `multilingual` when creating the conversation:

```shell cURL {9} theme={null}
curl --request POST \
  --url https://tavusapi.com/v2/conversations \
  --header 'Content-Type: application/json' \
  --header 'x-api-key: <api_key>' \
  --data '{
  "persona_id": "pcb7a34da5fe",
  "replica_id": "r90bbd427f71",
  "properties": {
    "language": "multilingual"
   }
}'
```

This enables the **STT** (speech-to-text) engine to automatically switch languages, dynamically adjusting the pipeline to transcribe and respond in the detected language throughout the conversation.

<Note>
  For the highest accuracy, we recommend setting a specific language rather than using `multilingual`. Smart Language Detection works best as a fallback when the participant's language is unknown ahead of time.
</Note>


# Memories
Source: https://docs.tavus.io/sections/conversational-video-interface/memories

Memories let personas remember information across conversations, allowing participants to have personalized, flowing conversations across multiple sessions.

Memories are pieces of information that the persona learns during a conversation. Once learned, these memories can be referenced and used by the persona during subsequent conversations.

Developers are able to organize memories within `memory_stores` - a flexible tag-based system to track memories across conversations and participants into different buckets.
If a `memory_stores` value is provided in the conversation creation request, memories will automatically be created and associated to the tag provided.

<Note>
  When defining `memory_stores` values, we recommend incorporating static values that will not change with persona updates, like persona ID.

  For example, using a persona's name as part of your `memory_stores` values could result in memories being miscategorized if you were to change their name.
</Note>

## Basic Example

For example, if a participant named Anna starts a conversation with the persona (Charlie, with the persona ID `p123`), we can specify `memory_stores=["anna_p123"]` in the conversation creation request.
By doing so, Charlie will:

* Remember what was mentioned in a conversation and form new memories with Anna.
* Reference memories from previous conversations that Charlie had with Anna in new conversations.

Example [conversation creation](https://docs.tavus.io/api-reference/conversations/create-conversation) request body:

```json theme={null}
{
  "persona_id": "your_persona_id",
  "replica_id": "your_replica_id",
  "memory_stores": ["anna_p123"]
}
```

## Managing Memories Between Participants and Conversations

<Note>
  To prevent different personas from mixing up information for the same participant, we generally recommend you to create separate `memory_stores` values for each user when they talk to different personas.

  For example,

  * When Anna talks to Charlie (persona ID of `p123`), you can use the `memory_stores` value of `["anna-p123"]`.
  * when she talks with Gloria (persona ID of `p456`), you can use the `memory_stores` value of `["anna-p456"]`.
</Note>

The `memory_stores` system can be used flexibly to cover your use cases - they do not have to map 1:1 with your participants and instead can be designed for your unique use cases.

For example,

* If you were setting up an online classroom, you could use a `memory_stores` tag value of `"classroom-1"` so any participant of this group could reference and create new memories to enhance and deepen learning and connections.
* You can control whether you want personas to share memory or not (and if so, which personas) by passing them different `memory_stores` values.

## Delete a memory

You can delete a single memory via the API. Use the same `memory_store` value you used when creating the conversation, and the memory ID returned when the memory was created or listed.

```bash theme={null}
curl -X DELETE "https://tavusapi.com/v2/memories/<memory_store>/<memory_id>" \
  -H "x-api-key: YOUR_API_KEY"
```

Replace `<memory_store>` with your memory store identifier (e.g. `anna_p123`) and `<memory_id>` with the ID of the memory to delete.


# Mobile
Source: https://docs.tavus.io/sections/conversational-video-interface/mobile

Ship Tavus CVI on iOS, Android, React Native, and mobile web using Daily's mobile SDKs and the same conversation URLs as web.

Tavus **Conversational Video Interface (CVI)** runs on **Daily** rooms. After you [create a conversation](/api-reference/conversations/create-conversation), use the returned **`conversation_url`** wherever Daily's docs refer to a room URL. On **web**, you can embed with our [React component library](/sections/conversational-video-interface/component-library/overview) (`@tavus/cvi-ui`, built on `@daily-co/daily-js` / `@daily-co/daily-react`) or follow [Embed CVI](/sections/integrations/embedding-cvi). On **native mobile**, Daily's SDKs are the supported path today—you bring the UI and join the same Tavus-issued Daily room.

## React (web) vs React Native

* **React for the browser:** Use Tavus's [component library overview](/sections/conversational-video-interface/component-library/overview), plus [blocks](/sections/conversational-video-interface/component-library/blocks), [components](/sections/conversational-video-interface/component-library/components), and [hooks](/sections/conversational-video-interface/component-library/hooks)—see [Embed CVI](/sections/integrations/embedding-cvi) for full flows.
* **React Native:** Daily's [React Native SDK](https://docs.daily.co/reference/rn-daily-js) uses the same underlying model as `daily-js`; join with your **`conversation_url`** from Tavus.

## Android

Daily's native [Android SDK](https://docs.daily.co/reference/android) (Kotlin) is the usual integration surface for Tavus CVI on Android. Use their [Android quickstart](https://docs.daily.co/guides/products/mobile/android-quickstart) with your **`conversation_url`**.

## iOS

Daily's native [iOS SDK](https://docs.daily.co/reference/ios) (Swift) pairs the same way with Tavus. Follow their [iOS quickstart](https://docs.daily.co/guides/products/mobile/ios-quickstart) and pass the **`conversation_url`** from [Create Conversation](/api-reference/conversations/create-conversation).

## Flutter

For cross-platform apps, Daily's [Flutter SDK](https://docs.daily.co/reference/flutter) joins the same Daily rooms Tavus provisions.

## Mobile web

Users can join a Tavus conversation in **Chrome on Android** or **Safari on iOS** without a native SDK when a mobile-capable web experience is enough. Daily's [mobile web guide](https://docs.daily.co/guides/products/mobile) covers browser behavior and constraints.

## Further reading

Daily's [mobile intro guide](https://docs.daily.co/guides/products/mobile/intro) summarizes all native mobile SDKs in one place.


# What is CVI?
Source: https://docs.tavus.io/sections/conversational-video-interface/overview-cvi

CVI enables real-time, human-like video interactions through configurable lifelike replicas.

<Frame>
  <img alt="" />
</Frame>

Conversational Video Interface (CVI) is a framework for creating real-time multimodal video interactions with AI. It enables an AI agent to see, hear, and respond naturally, mirroring human conversation.

CVI is the world’s fastest interface of its kind. It allows you to map a human face and conversational ability onto your AI agent. With CVI, you can achieve low-latency utterance-to-utterance response: the full round-trip time from when a participant speaks to when the replica replies.

CVI provides a comprehensive solution, with the option to plug in your existing components as required.

## At a glance

<Info>
  Building with an AI coding agent or automation? Use
  `https://docs.tavus.io/llms.txt` for the canonical page index,
  `https://docs.tavus.io/llms-full.txt` for the full bundled docs export, and
  `https://docs.tavus.io/openapi.yaml` for the HTTP API contract.
</Info>

* **CVI** — Real-time multimodal video: the agent sees, hears, and responds; media runs over **WebRTC** (powered by Daily).
* **Latency** — Utterance-to-utterance round-trip is optimized for real-time use (participant speaks → replica replies).
* **Three pillars** — **[Persona](/sections/conversational-video-interface/persona/overview)** (behavior, knowledge, and CVI layer pipeline); **[Replica](/sections/replica/overview)** (visual digital human, **Phoenix**); **[Conversation](/sections/conversational-video-interface/conversation/overview)** (live session linking persona and replica).
* **Pipeline (in order)** — Perception (**Raven**) → Conversational Flow (**Sparrow**) → Speech recognition (STT) → Large language model (LLM) → Text-to-speech (TTS) → Realtime replica (**Phoenix**). **Raven** is visual perception; **Sparrow** handles turn-taking and interruptibility; **Phoenix** is the real-time visual replica engine.
* **Where to configure** — Most layers are set on the **[Persona](/sections/conversational-video-interface/persona/overview)**.

## Key Concepts

CVI is built around three core concepts that work together to create real-time, humanlike interactions with an AI agent:

<CardGroup>
  <Card title="Persona" icon="heart-pulse" href="/sections/conversational-video-interface/persona/overview">
    The **Persona** defines the agent’s behavior, tone, and knowledge. It also configures the CVI layer and pipeline.
  </Card>

  <Card title="Replica" icon="user-group" href="/sections/replica/overview">
    The **Replica** brings the persona to life visually. It renders a photorealistic human-like avatar using **Phoenix**.
  </Card>

  <Card title="Conversation" icon="video" href="/sections/conversational-video-interface/conversation/overview">
    A **Conversation** is a real-time video session that connects the persona and replica through a WebRTC connection.
  </Card>
</CardGroup>

## Key Features

<CardGroup>
  <Card title="Natural Interaction" icon="face-smile-beam">
    CVI uses facial cues, body language, and real-time turn-taking to enable natural, human-like conversations.
  </Card>

  <Card title="Modular pipeline" icon="layer-group">
    Customize the Perception, STT, LLM and TTS layers to control identity, behavior, and responses.
  </Card>

  <Card title="Lifelike AI replicas" icon="user-robot">
    Choose from over 100+ hyper-realistic stock replicas or customize your own with human-like voice and expression.
  </Card>

  <Card title="Multilingual support" icon="globe">
    Hold natural conversations in 42+ languages using the supported TTS engines.
  </Card>

  <Card title="World's lowest latency" icon="bolt">
    Experience real-time interactions with low utterance-to-utterance latency and smooth turn-taking.
  </Card>
</CardGroup>

## Layers

The Conversational Video Interface (CVI) is built on a modular layer system, where each layer handles a specific part of the interaction. Together, they capture input, process it, and generate a real-time, human-like response.

Here’s how the layers work together:

<AccordionGroup>
  <Accordion title="1. Perception" icon="eye">
    Uses **Raven** to analyze user expressions, gaze, background, and screen content. This visual context helps the replica understand and respond more naturally.

    [Configure the Perception layer](/sections/conversational-video-interface/persona/perception)
  </Accordion>

  <Accordion title="2. Conversational Flow" icon="comments">
    Controls the natural dynamics of conversation, including turn-taking and interruptibility. Uses **Sparrow** for intelligent turn detection, enabling the replica to decide when to speak and when to listen.

    [Configure the Conversational Flow layer](/sections/conversational-video-interface/persona/conversational-flow)
  </Accordion>

  <Accordion title="3. Speech Recognition (STT)" icon="ear-listen">
    This layer transcribes user speech in real time with lexical and semantic awareness.

    [Configure the Speech Recognition (STT) layer](/sections/conversational-video-interface/persona/stt)
  </Accordion>

  <Accordion title="4. Large Language Model (LLM)" icon="brain">
    Processes the user's transcribed speech and visual input using a low-latency LLM. Tavus provides ultra-low latency optimized LLMs or lets you integrate your own.

    [Configure the Large Language Model (LLM) layer](/sections/conversational-video-interface/persona/llm)
  </Accordion>

  <Accordion title="5. Text-to-Speech (TTS)" icon="volume-high">
    Converts the LLM response into speech using the supported TTS Engines (Cartesia **(Default)**, ElevenLabs, Azure).

    [Configure the Text-to-Speech (TTS) layer](/sections/conversational-video-interface/persona/tts)
  </Accordion>

  <Accordion title="6. Realtime replica (Phoenix)" icon="face-smile">
    Delivers a high-quality, synchronized digital human using Tavus's real-time avatar engine (**Phoenix**).

    [Replica overview](/sections/replica/overview)
  </Accordion>
</AccordionGroup>

<Note>
  Most layers are configurable via the [Persona](/sections/conversational-video-interface/persona/overview).
</Note>

## Getting Started

You can quickly create a conversation by using the <a href="https://platform.tavus.io/">Developer Portal</a> or following the steps in the [API Conversation Quickstart](/sections/conversational-video-interface/quickstart/cvi-quickstart) guide.

If you use **Cursor**, **Copilot**, or another **AI coding agent**, use the copy-paste checklist on **[CVI App: AI Prompt](/sections/conversational-video-interface/quickstart/ai-prompt-cvi-quickstart)**.

For web apps, start with [CVI App Quickstart](/sections/conversational-video-interface/quickstart/build-first-app), then choose an embed path in [Embed CVI](/sections/integrations/embedding-cvi). React apps that want Tavus-provided UI should use the [`@tavus/cvi-ui` component library](/sections/conversational-video-interface/component-library/overview), including [blocks](/sections/conversational-video-interface/component-library/blocks), [components](/sections/conversational-video-interface/component-library/components), [hooks](/sections/conversational-video-interface/component-library/hooks), and [server helpers](/sections/conversational-video-interface/component-library/server).


# Conversational Flow
Source: https://docs.tavus.io/sections/conversational-video-interface/persona/conversational-flow

Learn how to configure the Conversational Flow layer to fine-tune turn-taking and interruption handling behavior.

The **Conversational Flow Layer** in Tavus gives you precise control over the natural dynamics of conversation. This layer allows you to customize how your replica handles turn-taking and interruptions to create conversational experiences that match your specific use case.

## Understanding Conversational Flow

Conversational flow encompasses the subtle dynamics that make conversations feel natural:

* **Turn-taking**: How the replica decides when to speak and when to listen
* **Interruptibility**: How easily the replica can be interrupted by the user

<Note>
  All conversational flow parameters are optional. When not explicitly configured, the layer remains inactive. However, if you configure any single parameter, the system will apply sensible defaults to all other parameters to ensure consistent behavior.
</Note>

<Note>
  The replica's greeting is always non-interruptible, regardless of `replica_interruptibility`. These settings only take effect after the greeting completes.
</Note>

## Configuring the Conversational Flow Layer

<Note>
  If you're migrating from sparrow-0 (formerly called `smart_turn_detection` on the STT Layer) then check out the [migration guide here](/sections/troubleshooting#conversational-flow-vs-stt-relationship-and-migration).
</Note>

Define the conversational flow layer under the `layers.conversational_flow` object. Below are the parameters available:

### 1. `turn_detection_model`

Specifies the model used for detecting conversational turns.

* **Options**:
  * `sparrow-1` **(default)**: Advanced turn detection model - faster, more accurate, and more natural (recommended)
  * `sparrow-0`: Legacy turn detection model (API-only, not actively supported)
  * `timebased`: Simple time-based turn detection (API-only, not actively supported)

* **Default**: `sparrow-1`

```json theme={null}
"turn_detection_model": "sparrow-1"
```

<Tip>
  **Sparrow-1 is recommended for all use cases** as it provides superior performance with faster response times, higher accuracy, and more natural conversational flow.
</Tip>

### 2. `turn_taking_patience`

Controls how eagerly the replica claims conversational turns. This affects both response latency and the likelihood of interrupting during natural pauses.

* **Options**:
  * `low`: Eager and quick to respond. May interrupt natural pauses. Best for rapid-fire exchanges or customer service scenarios where speed is prioritized.
  * `medium` **(default)**: Balanced behavior. Waits for appropriate conversational cues before responding.
  * `high`: Patient and waits for clear turn completion. Ideal for thoughtful conversations, interviews, or therapeutic contexts.

```json theme={null}
"turn_taking_patience": "medium"
```

**Use Cases:**

* `low`: Fast-paced customer support, quick information lookups, casual chat
* `medium`: General purpose conversations, sales calls, presentations
* `high`: Medical consultations, legal advice, counseling sessions

### 3. `replica_interruptibility`

Controls how sensitive the replica is to user speech while the replica is talking. Determines whether the replica stops to listen or keeps speaking when interrupted.

* **Options**:
  * `low`: Less interruptible. The replica keeps talking through minor interruptions.
  * `medium` **(default)**: Balanced sensitivity. Responds to clear interruption attempts.
  * `high`: Highly sensitive. Stops easily when the user begins speaking, maximizing user control.

```json theme={null}
"replica_interruptibility": "high"
```

**Use Cases:**

* `low`: Educational content delivery, storytelling, guided onboarding
* `medium`: Standard conversations, interviews, consultations
* `high`: User-driven conversations, troubleshooting, interactive support

### 4. `voice_isolation`

Voice isolation separates speech from background noise in the participant's microphone audio. It is enabled by default for improved audio quality and can be disabled if needed.

* **Options**:
  * `near` **(default)**: Separates speech from background noise for scenarios where the user is less than 1 meter away from the microphone.
  * `off`: No voice isolation model is used. The raw audio is sent down the conversational pipeline.

```json theme={null}
"voice_isolation": "near"
```

### 5. `wake_phrase`

A specific phrase the persona listens for before responding. When set, the persona remains silent until it hears the wake phrase, similar to how voice assistants like Siri or Alexa work.

* **Type**: `string`
* **Default**: `None` (disabled)

```json theme={null}
"wake_phrase": "Hey Siri"
```

**How wake phrases work:**

* The persona stays silent and does not respond until it hears the specified wake phrase.
* The persona still "hears" everything that is said. All user utterances are recorded in the transcript so the persona has full context when it does respond.
* Once the wake phrase is detected, the persona responds using the full conversation history, including anything said before the wake phrase was triggered.

<Tip>
  Choose a wake phrase that is unique enough to avoid over-triggering. Avoid generic greetings like `"Hey"` or single common words, which can cause the persona to respond unintentionally. Phrases with two or more distinctive words (for example, `"Hey Siri"` or `"Okay Assistant"`) work best.
</Tip>

### 6. `idle_engagement`

Controls whether the replica proactively re-engages the user after a stretch of silence, and how eagerly.

* **Options**:
  * `off` **(default)**: The replica never breaks silence — it only speaks in response to user input.
  * `patient`: The replica re-engages after longer silences. Suited to tutors, coaches, or contemplative use cases where users may need time to think.
  * `eager`: The replica re-engages after shorter silences. Suited to SDR or sales-style conversations where keeping momentum matters.

```json theme={null}
"idle_engagement": "patient"
```

**Use Cases:**

* `off`: General conversational use cases where the user always drives the next turn
* `patient`: Tutoring, coaching, therapy, interviews
* `eager`: Outbound sales, SDR, qualification calls

<Note>
  `idle_engagement` is independent of `turn_taking_patience`. Turn-taking patience controls how quickly the replica responds after the user finishes speaking; `idle_engagement` controls whether the replica proactively breaks an extended silence.
</Note>

## Default Behavior

When the conversational flow layer is not configured, all parameters default to `None` and the layer remains inactive. However, if you configure **any single parameter**, the system automatically applies the following defaults to ensure consistent behavior:

* `turn_detection_model`: `sparrow-1`
* `turn_taking_patience`: `medium`
* `replica_interruptibility`: `medium`
* `voice_isolation`: `near`
* `wake_phrase`: `None`
* `idle_engagement`: `off`

## Example Configurations

The following example configurations demonstrate how to tune conversational timing and interruption behavior for different use cases. Use `turn_taking_patience` to bias how quickly the replica responds after a user finishes speaking. Set it high when the replica should avoid interrupting, and low when fast responses are preferred. Use `replica_interruptibility` to control how easily the replica recalculates its response when interrupted; lower values are recommended for most experiences, with higher values reserved for cases where frequent, abrupt interruptions are desirable. Sparrow-1 dynamically handles turn-taking in all cases, with these settings acting as guiding biases rather than hard rules.

### Example 1: Customer Support Agent

Fast, responsive, and easily interruptible for customer-driven conversations:

```json theme={null}
{
  "persona_name": "Support Agent",
  "system_prompt": "You are a helpful customer support agent...",
  "pipeline_mode": "full",
  "default_replica_id": "r90bbd427f71",
  "layers": {
    "conversational_flow": {
      "turn_detection_model": "sparrow-1",
      "turn_taking_patience": "low",
      "replica_interruptibility": "medium",
      "voice_isolation": "near"
    }
  }
}
```

### Example 2: Medical Consultation

Patient, thoughtful, with engaged listening for sensitive conversations:

```json theme={null}
{
  "persona_name": "Medical Advisor",
  "system_prompt": "You are a compassionate medical professional...",
  "pipeline_mode": "full",
  "default_replica_id": "r90bbd427f71",
  "layers": {
    "conversational_flow": {
      "turn_detection_model": "sparrow-1",
      "turn_taking_patience": "high",
      "replica_interruptibility": "verylow",
      "voice_isolation": "near"
    }
  }
}
```

### Example 3: Educational Instructor

Delivers complete information with minimal interruption, and gently re-engages the user after long pauses for thought:

```json theme={null}
{
  "persona_name": "Instructor",
  "system_prompt": "You are an experienced educator teaching complex topics...",
  "pipeline_mode": "full",
  "default_replica_id": "r90bbd427f71",
  "layers": {
    "conversational_flow": {
      "turn_detection_model": "sparrow-1",
      "turn_taking_patience": "medium",
      "replica_interruptibility": "low",
      "voice_isolation": "near",
      "idle_engagement": "patient"
    }
  }
}
```

### Example 4: Minimal Configuration

Configure just one parameter—others will use defaults:

```json theme={null}
{
  "persona_name": "Quick Chat",
  "system_prompt": "You are a friendly conversational AI...",
  "pipeline_mode": "full",
  "default_replica_id": "r90bbd427f71",
  "layers": {
    "conversational_flow": {
      "turn_taking_patience": "low"
    }
  }
}
```

In this example, the system will automatically set:

* `turn_detection_model`: `sparrow-1`
* `replica_interruptibility`: `medium`
* `voice_isolation`: `near`

## Best Practices

### Match Flow to Use Case

Choose conversational flow settings that align with your application's purpose:

* **Speed-critical applications**: Use `low` turn-taking patience and `high` interruptibility
* **Thoughtful conversations**: Use `high` turn-taking patience
* **Important information delivery**: Use `low` interruptibility
* **User-controlled interactions**: Use `high` interruptibility

### Consider Cultural Context

Conversational norms vary across cultures. Some cultures prefer:

* More overlap and interruption (consider lower commitment, higher interruptibility)
* Clear turn-taking with pauses (consider higher patience, lower interruptibility)

### Test with Real Users

Conversational flow preferences can be subjective. Test your configuration with representative users to ensure it feels natural for your audience.

<Note>
  Refer to the <a href="/api-reference/personas/create-persona">Create Persona API</a> for the complete API specification and additional persona configuration options.
</Note>


# Large Language Model (LLM)
Source: https://docs.tavus.io/sections/conversational-video-interface/persona/llm

Learn how to use Tavus-optimized LLMs or integrate your own custom LLM.

The **LLM Layer** in Tavus enables your persona to generate intelligent, context-aware responses. You can use Tavus-hosted models or connect your own OpenAI-compatible LLM.

Configure the LLM under **`layers.llm`** when you [Create Persona](/api-reference/personas/create-persona) or update a persona. For how a persona fits together, see [Persona overview](/sections/conversational-video-interface/persona/overview).

## Tavus-Hosted Models

### 1. `model`

Select one of the available models. **`tavus-gpt-oss` is recommended as a good starting point**; the table below helps you choose based on your priorities.

| Model                            | Speed | Intelligence | Naturalness | Best For                           |
| -------------------------------- | ----- | ------------ | ----------- | ---------------------------------- |
| `tavus-gpt-oss`                  | ⚡⚡⚡   | 🧠           | 💬          | Snappy, low-latency                |
| `tavus-gpt-4.1` (deprecated)     | ⚡⚡    | 🧠🧠🧠       | 💬💬💬      | Long-context reasoning             |
| `tavus-gpt-4o` (deprecated)      | ⚡⚡    | 🧠🧠         | 💬💬        | Legacy option                      |
| `tavus-gemini-2.5-flash`         | ⚡⚡    | 🧠🧠         | 💬💬💬      | Latency + logical deduction        |
| `tavus-claude-haiku-4.5`         | ⚡⚡    | 🧠🧠         | 💬💬        | Grounded, fewer hallucinations     |
| `tavus-gpt-5.2`                  | ⚡⚡    | 🧠🧠         | 💬💬        | General use, latency less critical |
| `tavus-gpt-4o-mini` (deprecated) | ⚡⚡    | 🧠           | 💬💬        | Legacy option                      |
| `tavus-gemini-3-flash`           | ⚡     | 🧠🧠🧠       | 💬💬💬      | Highest intelligence, lower speed  |

<Note>
  **Context Window Limit**

  * Performance and intelligence are best when prompts are **limited to 5,000 tokens**. You may see degradations in speed and instruction following in the **15,000–20,000 token** range.
  * All Tavus-hosted models support up to **32,000 tokens**; staying within 5k is recommended for optimal behavior.

  **Tip**: 1 token ≈ 4 characters, so 5,000 tokens ≈ 20,000 characters (including spaces and punctuation).
</Note>

```json theme={null}
"model": "tavus-gpt-oss"
```

### 2. `tools`

Optionally enable tool calling by defining functions the LLM can invoke.

<Note>
  Please see [LLM Tool Calling](/sections/conversational-video-interface/persona/llm-tool) for more details.
</Note>

### 3. `speculative_inference`

When set to `true`, the LLM begins processing speech transcriptions before user input ends, improving responsiveness. **This is the default value**; you can set it to `false` to disable.

```json theme={null}
"speculative_inference": true
```

<Note>
  This field is optional. It defaults to `true` for better performance.
</Note>

### 4. `extra_body`

Add parameters to customize the LLM request. For Tavus-hosted models, you can pass `temperature` and `top_p`:

```json theme={null}
"extra_body": {
  "temperature": 0.7,
  "top_p": 0.9
}
```

<Note>
  This field is optional.
</Note>

### Example Configuration

```json theme={null}
{
  "persona_name": "Health Coach",
  "system_prompt": "You provide wellness tips and encouragement for people pursuing a healthy lifestyle.",
  "pipeline_mode": "full",
  "default_replica_id": "r90bbd427f71",
  "layers": {
    "llm": {
      "model": "tavus-gpt-oss",
      "speculative_inference": true,
      "extra_body": {
        "temperature": 0.7,
        "top_p": 0.9
      }
    }
  }
}
```

## Custom LLMs

### Prerequisites

To use your own OpenAI-compatible LLM, you'll need:

* Model name
* Base URL
* API key

Ensure your LLM:

* Streamable (i.e. via SSE)
* Uses the `/chat/completions` endpoint

### 1. `model`

Name of the custom model you want to use.

```json theme={null}
"model": "gpt-3.5-turbo"
```

### 2. `base_url`

Base URL of your LLM endpoint.

<Note>
  Do not include route extensions in the `base_url`.
</Note>

```json theme={null}
"base_url": "https://your-llm.com/api/v1"
```

### 3. `api_key`

API key to authenticate with your LLM provider.

```json theme={null}
"api_key": "your-api-key"
```

<Tip>
  `base_url` and `api_key` are required only when using a custom model.
</Tip>

### 4. `tools`

Optionally enable tool calling by defining functions the LLM can invoke.

<Note>
  Please see [LLM Tool Calling](/sections/conversational-video-interface/persona/llm-tool) for more details.
</Note>

### 5. `speculative_inference`

When set to `true`, the LLM begins processing speech transcriptions before user input ends, improving responsiveness. **This is the default value**; you can set it to `false` to disable.

```json theme={null}
"speculative_inference": true
```

<Note>
  This field is optional. It defaults to `true` for better performance.
</Note>

### 6. `headers`

Optional additional headers to include when making requests to your LLM. Use this for any extra headers your provider requires beyond the API key (which should be set via the `api_key` field).

```json theme={null}
"headers": {
  "X-Organization-ID": "your-org-id",
  "X-Request-Source": "tavus-cvi"
}
```

<Note>
  This field is optional, depending on your LLM provider's requirements.
</Note>

### 7. `extra_body`

Add parameters to customize the LLM request. You can pass any parameters that your LLM provider supports:

```json theme={null}
"extra_body": {
  "temperature": 0.5,
  "top_p": 0.9,
  "frequency_penalty": 0.5
}
```

<Note>
  This field is optional.
</Note>

### 8. `default_query`

Add default query parameters that get appended to the base URL when making requests to the `/chat/completions` endpoint.

```json theme={null}
"default_query": {
  "api-version": "2024-02-15-preview"
}
```

<Note>
  This field is optional. Useful for LLM providers that require query parameters for authentication or versioning.
</Note>

### Example Configuration

```json theme={null}
{
  "persona_name": "Storyteller",
  "system_prompt": "You are a storyteller who entertains people of all ages.",
  "pipeline_mode": "full",
  "default_replica_id": "r90bbd427f71",
  "layers": {
    "llm": {
      "model": "gpt-4o",
      "base_url": "https://your-azure-openai.openai.azure.com/openai/deployments/gpt-4o",
      "api_key": "your-api-key",
      "speculative_inference": true,
      "default_query": {
        "api-version": "2024-02-15-preview"
      }
    }
  }
}
```

<Note>
  Refer to [Create Persona](/api-reference/personas/create-persona) for a full list of supported fields.
</Note>

### Perception

When using the `raven-1` perception model with a custom LLM, your LLM will receive system messages containing visual context extracted from the user's video input. See [Perception](/sections/conversational-video-interface/persona/perception) for how perception is configured and what is sent to the model.

```json theme={null}
{
    "role": "system",
    "content": "<user_appearance>...</user_appearance> <user_emotions>...</user_emotions> <user_screenshare>...</user_screenshare>"
}
```

#### Disabled Perception model

If you disable the perception model, your LLM will not receive any special messages.


# Tool Calling for LLM
Source: https://docs.tavus.io/sections/conversational-video-interface/persona/llm-tool

Set up tool calling to trigger functions from user speech using Tavus-hosted or custom LLMs.

**LLM tool calling** works with OpenAI’s <a href="https://platform.openai.com/docs/guides/function-calling">Function Calling</a> and can be set up in the `llm` layer. It allows an AI agent to trigger functions based on user speech during a conversation.

<Note>
  Tavus does not execute tool calls on the backend. Use event listeners in your frontend to listen for [tool call events](/sections/event-schemas/conversation-toolcall) and run your own logic when a tool is invoked.
</Note>

<Note>
  You can use tool calling with our **hosted models** or any **OpenAI-compatible custom LLM**.
</Note>

## Defining Tool

### Top-Level Fields

| Field      | Type   | Required | Description                                                                                              |
| ---------- | ------ | -------- | -------------------------------------------------------------------------------------------------------- |
| `type`     | string | ✅        | Must be `"function"` to enable tool calling.                                                             |
| `function` | object | ✅        | Defines the function that can be called by the LLM. Contains metadata and a strict schema for arguments. |

#### `function`

| Field         | Type   | Required | Description                                                                                                                  |
| ------------- | ------ | -------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `name`        | string | ✅        | A unique identifier for the function. Must be in `snake_case`. The model uses this to refer to the function when calling it. |
| `description` | string | ✅        | A natural language explanation of what the function does. Helps the LLM decide when to call it.                              |
| `parameters`  | object | ✅        | A JSON Schema object that describes the expected structure of the function’s input arguments.                                |

#### `function.parameters`

| Field        | Type             | Required | Description                                                                               |
| ------------ | ---------------- | -------- | ----------------------------------------------------------------------------------------- |
| `type`       | string           | ✅        | Always `"object"`. Indicates the expected input is a structured object.                   |
| `properties` | object           | ✅        | Defines each expected parameter and its corresponding type, constraints, and description. |
| `required`   | array of strings | ✅        | Specifies which parameters are mandatory for the function to execute.                     |

<Note>
  Each parameter should be included in the required list, even if they might seem optional in your code.
</Note>

##### `function.parameters.properties`

Each key inside `properties` defines a single parameter the model must supply when calling the function.

| Field              | Type   | Required | Description                                                                                 |
| ------------------ | ------ | -------- | ------------------------------------------------------------------------------------------- |
| `<parameter_name>` | object | ✅        | Each key is a named parameter (e.g., `location`). The value is a schema for that parameter. |

Optional subfields for each parameter:

| Subfield      | Type   | Required | Description                                                                                 |
| ------------- | ------ | -------- | ------------------------------------------------------------------------------------------- |
| `type`        | string | ✅        | Data type (e.g., `string`, `number`, `boolean`).                                            |
| `description` | string | ❌        | Explains what the parameter represents and how it should be used.                           |
| `enum`        | array  | ❌        | Defines a strict list of allowed values for this parameter. Useful for categorical choices. |

## Example Configuration

Here’s an example of tool calling in the `llm` layers:

<Tip>
  **Best Practices:**

  * Use clear, specific function names to reduce ambiguity.
  * Add detailed `description` fields to improve selection accuracy.
</Tip>

```json LLM Layer [expandable] theme={null}
"llm": {
  "model": "tavus-gpt-oss",
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "get_current_time",
        "description": "Fetch the current local time for a specified location",
        "parameters": {
          "type": "object",
          "properties": {
            "location": {
              "type": "string",
              "description": "The name of the city or region, e.g. New York, Tokyo"
            }
          },
          "required": ["location"]
        }
      }
    },
    {
      "type": "function",
      "function": {
        "name": "convert_time_zone",
        "description": "Convert time from one time zone to another",
        "parameters": {
          "type": "object",
          "properties": {
            "time": {
              "type": "string",
              "description": "The original time in ISO 8601 or HH:MM format, e.g. 14:00 or 2025-05-28T14:00"
            },
            "from_zone": {
              "type": "string",
              "description": "The source time zone, e.g. PST, EST, UTC"
            },
            "to_zone": {
              "type": "string",
              "description": "The target time zone, e.g. CET, IST, JST"
            }
          },
          "required": ["time", "from_zone", "to_zone"]
        }
      }
    }
  ]
}
```

## How Tool Calling Works

Tool calling is triggered during an active conversation when the LLM model needs to invoke a function. Here’s how the process works:

<Note>
  This example explains the `get_current_time` function from the [example configuration](#example-configuration) above.
</Note>

<Frame>
  <img alt="" />
</Frame>

## Modify Existing Tools

You can update `tools` definitions using the <a href="/api-reference/personas/patch-persona">Update Persona API</a>.

```shell [expandable] theme={null}
curl --request PATCH \
  --url https://tavusapi.com/v2/personas/{persona_id} \
  --header 'Content-Type: application/json' \
  --header 'x-api-key: <api-key>' \
  --data '[
    {
      "op": "replace",
      "path": "/layers/llm/tools",
      "value": [
        {
          "type": "function",
          "function": {
            "name": "get_current_weather",
            "description": "Get the current weather in a given location",
            "parameters": {
              "type": "object",
              "properties": {
                "location": {
                  "type": "string",
                  "description": "The city and state, e.g. San Francisco, CA"
                },
                "unit": {
                  "type": "string",
                  "enum": ["celsius", "fahrenheit"]
                }
              },
              "required": ["location", "unit"]
            }
          }
        }
      ]
    }
  ]'
```

<Note>
  Replace `<api_key>` with your actual API key. You can generate one in the <a href="https://platform.tavus.io/api-keys">Developer Portal</a>.
</Note>


# Objectives
Source: https://docs.tavus.io/sections/conversational-video-interface/persona/objectives

Objectives are goal-oriented instructions to define the desired outcomes and flow of your conversations.

Objectives work alongside your system prompt to provide a structured, flexible approach to guide conversations. They provide the most value during purposeful conversations that need to be tailored to specific processes, customer journeys, or workflows, while maintaining engaging and natural interactions.

For example, if you're creating a lead qualification persona for sales, you can set objectives to gather contact information, understand budget requirements, and assess decision-making authority before scheduling a follow-up meeting.

<Note>
  Objectives can only be created using the [Create Objectives](/api-reference/objectives/create-objectives) API.
</Note>

<Tip>
  For a deep dive on best practices for structuring objectives and guardrails, see the [Objectives and Guardrails Prompting Guide](/sections/onboarding-guide/objectives).
</Tip>

When designing your objectives, it's helpful to keep a few things in mind:

* Plan your entire ideal workflow. This will help create a robust branching structure that successfully takes the participant from start to finish.
* Think through the possible answers a participant might give, and ensure the workflow covers these cases.
* Ensure your persona's system prompt does not conflict with the objectives. For example, a system prompt, "You are a tutor," would not perform well with the objectives workflow of a sales associate.

## Attaching objectives to a persona

To attach objectives to a persona, you can either:

* Add them during [persona creation](/api-reference/personas/create-persona) like this:

```sh theme={null}
curl --request POST \
  --url https://tavusapi.com/v2/personas/ \
  --header 'Content-Type: application/json' \
  --header 'x-api-key: <api-key>' \
  --data '{
    "system_prompt": "You are a lead qualification assistant.",
    "objectives_id": "o12345"
  }'
```

OR

* Add them by [editing the persona](/api-reference/personas/patch-persona) like this:

```sh theme={null}
curl --request PATCH \
  --url https://tavusapi.com/v2/personas/{persona_id} \
  --header 'Content-Type: application/json' \
  --header 'x-api-key: <api-key>' \
  --data '[
    {"op": "add", "path": "/objectives_id", "value": "o12345"}
  ]'
```

<Note>
  For the best results, try creating unique objectives for different conversation purposes or business outcomes.

  For example, a customer onboarding persona might use objectives focused on data collection, while a support persona might use objectives focused on issue resolution.
</Note>

## Parameters

### `objective_name`

A desciptive name for the objective.

Example: `"check_patient_status"`

<Note>
  This must be a string value without spaces.
</Note>

### `objective_prompt`

A text prompt that explains what the goals of this objective are. The more detail you can provide, the better.

Example: `"Ask the patient if they are new or are returning."`

### `confirmation_mode`

This string value defines whether the LLM should determine whether this objective was completed or not.

* If set to `auto`, the LLM makes this decision.
* If set to `manual`, the participant must manually confirm that the objective was completed by the platform triggering an app message (`conversation.objective.pending`) and the participant having the ability to send one back called `conversation.objective.confirm`. This can include having the participant review the collected values for accuracy.

<Note>
  The default value of `confirmation_mode` is `auto`.
</Note>

### `output_variables` (optional)

This is a list of string variables that should be collected as a result of the objective being successfully completed.

Example: `["patient_status", "patient_group"]`

### `modality`

This value represents whether a specific objective should be completed based on the participant's verbal or visual responses. Each individual objective can be visual or verbal (not both), but this can vary across objectives.

<Note>
  The default value for `modality` is `"verbal"`.
</Note>

### `next_conditional_objectives`

This represents a mapping of objectives (identified by `objective_name`), to conditions that must be satisfied for that objective to be triggered after the completion of the current objective.

<Warning>
  `next_conditional_objectives` and `next_required_objective` are mutually exclusive - you can use one or the other on a given objective, but not both.
</Warning>

Example:

```json theme={null}
{
  "new_patient_intake_process": "If the patient has never been to the practice before",
  "existing_patient_intake_process": "If the patient has been to the practice before"
}
```

### `next_required_objective`

The name of the next required objective (identified by `objective_name`) that will be activated once the current objective is completed. Use this to define a single next objective without conditions.

<Warning>
  `next_required_objective` and `next_conditional_objectives` are mutually exclusive - you can use one or the other on a given objective, but not both.
</Warning>

Example: `"get_patient_name"`

### `callback_url` (optional)

A URL that you can send notifications to when a particular objective has been completed.

Example: `"https://your-server.com/objectives-webhook"`

When completed, the callback payload includes the `conversation_id`, the name of the objective, and any collected output variables:

```json theme={null}
{
  "conversation_id": "<conversation_id>",
  "objective_name": "<objective_name>",
  "output_variables": {
    "<variable_name>": "<value>"
  }
}
```


# Overview
Source: https://docs.tavus.io/sections/conversational-video-interface/persona/overview

Define how your persona behaves, responds, and speaks by configuring layers and pipeline modes.

Personas are the 'character' or 'AI agent personality' and contain all of the settings and configuration for that character or agent. For example, you can create a persona for 'Tim the sales agent' or 'Rob the interviewer'.

Personas combine identity, contextual knowledge, and CVI pipeline configuration to create a real-time conversational agent with a distinct behavior, voice, and response style. They are the main place you configure **[CVI](/sections/conversational-video-interface/overview-cvi)** behavior before you start a **[Conversation](/sections/conversational-video-interface/conversation/overview)**.

**At a glance**

* **Persona** — The agent’s identity (name, voice, behavior) plus **pipeline mode**, **default replica**, **layers**, **documents** (Knowledge Base), **objectives**, and **guardrails**.
* **Relationship to CVI** — Personas hold the settings that drive a real-time CVI session; see the **[What is CVI?](/sections/conversational-video-interface/overview-cvi)** for the full stack (WebRTC, layers, Phoenix, and latency characteristics on the default path).
* **Layers (order of guides below)** — Perception → STT → Conversational Flow → LLM → TTS; each has its own configuration page.

## Persona Customization Options

Each persona includes configurable fields. Here's what you can customize:

* **Persona Name**: Display name shown when the replica joins a call.
* **System Prompt**: Instructions sent to the language model to shape the replica's tone, personality, and behavior.
* **Pipeline mode**: Controls which CVI pipeline layers are active and how input/output flows through the system. See [Pipeline modes](/sections/conversational-video-interface/quickstart/pipeline-modes) for how the full pipeline, Echo, integrations, and custom LLM paths differ.
* **Default Replica**: Sets the digital human associated with the persona.
* **Layers**: Perception, STT, conversational flow, LLM, and TTS—each processes part of the interaction and can be tuned independently (see [Layers](#layers) below).
* **Documents**: A set of documents that the persona has access to via the **Knowledge Base** (retrieval-augmented generation, RAG).
* **Objectives**: The goal-oriented instructions your persona will adhere to throughout the conversation.
* **Guardrails**: Conversational boundaries that can be used to strictly enforce desired behavior.

## Objectives & Guardrails

Provide your persona with robust workflow management tools, curated to your use case

<CardGroup>
  <Card title="Objectives" icon="bullseye" href="/sections/conversational-video-interface/persona/objectives">
    The sequence of goals your persona will work to achieve throughout the conversation—for example gathering a piece of information from the user.
  </Card>

  <Card title="Guardrails" icon="shield" href="/sections/conversational-video-interface/guardrails">
    Conversational boundaries that can be used to strictly enforce desired behavior.
  </Card>
</CardGroup>

## Layers

Explore our in-depth guides to customize each layer to fit your specific use case:

<CardGroup>
  <Card title="Perception Layer" icon="eye" href="/sections/conversational-video-interface/persona/perception">
    Defines how the persona interprets visual input like facial expressions and gestures.
  </Card>

  <Card title="STT Layer" icon="waveform" href="/sections/conversational-video-interface/persona/stt">
    Transcribes user speech into text using the configured speech-to-text engine.
  </Card>

  <Card title="Conversational Flow Layer" icon="arrows-left-right" href="/sections/conversational-video-interface/persona/conversational-flow">
    Controls turn-taking, interruption handling, and active listening behavior for natural conversations.
  </Card>

  <Card title="LLM Layer" icon="brain" href="/sections/conversational-video-interface/persona/llm">
    Generates persona responses using a language model. Supports Tavus-hosted or custom LLMs.
  </Card>

  <Card title="TTS Layer" icon="microphone" href="/sections/conversational-video-interface/persona/tts">
    Converts text responses into speech using Tavus or supported third-party TTS engines.
  </Card>
</CardGroup>


# Perception
Source: https://docs.tavus.io/sections/conversational-video-interface/persona/perception

Learn how to configure the perception layer with Raven to enable real-time visual and audio understanding.

The **Perception Layer** in Tavus enhances an AI agent with real-time visual and audio understanding.
By using [Raven](/sections/models#raven%3A-perception-model), the AI agent becomes more context-aware, responsive, and capable of triggering actions based on visual and audio input.

## Configuring the Perception Layer

To configure the Perception Layer, define the following parameters within the `layers.perception` object:

### 1. `perception_model`

Specifies the perception model to use.

* **Options**:
  * `raven-1` **(default and recommended)**: Real-time emotional understanding from user audio, more natural and human-like interactions, plus all visual capabilities from raven-0.
  * `raven-0` (legacy settings [here](/sections/troubleshooting#migration-from-legacy-perception-to-raven-1))
  * `off`: Disables the perception layer.

<Note>
  **Screen Share Feature**: When using Raven, screen share is enabled by default without additional configuration.
</Note>

### Audio Perception

Raven-1 (the default) analyzes user tone and emotion in real-time. This context is automatically sent to the LLM alongside utterances, enabling more natural, empathetic responses. For example:

```
<user_audio_analysis>The user sounded sarcastic when they said this</user_audio_analysis>
Wow, I love Mondays.
```

Audio analysis tags are stripped from transcription callbacks.

<Note>
  Audio analysis output is limited to 32 tokens per utterance.
</Note>

## Perception Analysis Queries

Raven supports three kinds of queries that differ by **when** they run and **how** they affect the call:

* **perception\_analysis\_queries** — Evaluated only at **end of call**. They do not change live behavior; they only shape the summary you get in the [Perception Analysis](/sections/event-schemas/conversation-perception-analysis) event sent to your [conversation callback](/sections/webhooks-and-callbacks#conversation-callbacks).
* **visual\_awareness\_queries** and **audio\_awareness\_queries** — Evaluated **throughout the call**. Their answers are passed to the LLM as context, so the replica can react in real time. You receive this ongoing analysis in each user turn via the [Utterance event](/sections/event-schemas/conversation-utterance) as `user_visual_analysis` and `user_audio_analysis`.

Use **visual\_awareness\_queries** and **audio\_awareness\_queries** when you want the replica to be aware of or focus on something specific during the conversation. Use **perception\_analysis\_queries** when you want your end-of-call summary to address specific points.

## Visual Perception Configuration

### 2. `visual_awareness_queries`

An array of custom queries that Raven continuously monitors in the visual stream.

```json theme={null}
"visual_awareness_queries": [
  "Is the user wearing a bright outfit?"
]
```

<AccordionGroup>
  <Accordion title="visual_awareness_queries examples">
    Queries that Raven evaluates **continuously during the call** (on the order of every second). The answers are fed into the rolling visual context for the LLM, so the replica can respond to what it "sees." This same context also supports the end-of-call summary. You can read the ongoing visual analysis for each user utterance in the [Utterance event](/sections/event-schemas/conversation-utterance) as **user\_visual\_analysis**.

    **When to use:** When you want the replica to pay attention to something visual in real time (e.g. expression, clothing, objects on screen).

    **Example:**

    ```json theme={null}
    "visual_awareness_queries": [
      "What is the main expression on the user's face?",
      "Is the user wearing a jacket?",
      "Does the user appear distressed or uncomfortable?"
    ]
    ```
  </Accordion>
</AccordionGroup>

### 3. `perception_analysis_queries`

An array of custom queries that Raven processes at the end of the call to generate a visual analysis summary for the user.

<AccordionGroup>
  <Accordion title="perception_analysis_queries examples">
    Queries that are answered **once, at the end of the call**, by looking at what was observed over the whole conversation. They do not affect the call itself—only the content of the end-of-call summary. (Currently the summary is visual only; naming is kept general for future support.)

    **When to use:** When you want the post-call report to answer specific questions (e.g. "Did the user ever have two people on screen?", "How often was the user looking at the screen?").

    **Example:**

    ```json theme={null}
    "perception_analysis_queries": [
      "On a scale of 1-100, how often was the user looking at the screen?",
      "Is there any indication that more than one person is present?"
    ]
    ```

    The answers are delivered in a [Perception Analysis](/sections/event-schemas/conversation-perception-analysis) event. Example payload:

    ```json theme={null}
    {
      "properties": {
        "analysis": "**User's Gaze Toward Screen:** The participant looked at the screen approximately 75% of the time.\n\n**Multiple People Present:** No indication of additional participants was detected during the call."
      },
      "conversation_id": "<conversation_id>",
      "event_type": "application.perception_analysis",
      "timestamp": "2025-07-11T09:13:35.361736Z"
    }
    ```
  </Accordion>
</AccordionGroup>

<Note>
  You do not need to set `visual_awareness_queries` in order to use `perception_analysis_queries`.
</Note>

```json theme={null}
"perception_analysis_queries": [
  "Is the user wearing multiple bright colors?",
  "Is there any indication that more than one person is present?",
  "On a scale of 1-100, how often was the user looking at the screen?"
]
```

<Tip>
  Best practices for `visual_awareness_queries` and `perception_analysis_queries`:

  * Use simple, focused prompts.
  * Use queries that support your persona's purpose.
</Tip>

<Warning>
  All Raven API parameters (queries, prompts, tool definitions, etc.) have a **10,000 character limit** per entry. Entries exceeding this limit will cause an exception.
</Warning>

### 4. `visual_tool_prompt`

Tell Raven when and how to trigger tools based on what it sees.

```json theme={null}
"visual_tool_prompt":
  "You have a tool to notify the system when a bright outfit is detected, named `notify_if_bright_outfit_shown`. You MUST use this tool when a bright outfit is detected."
```

### 5. `visual_tools`

Defines callable functions that Raven can trigger upon detecting specific visual conditions. Each tool must include a `type` and a `function` object detailing its schema.

```json theme={null}
"visual_tools": [
  {
    "type": "function",
    "function": {
      "name": "notify_if_bright_outfit_shown",
      "description": "Use this function when a bright outfit is detected in the image with high confidence",
      "parameters": {
        "type": "object",
        "properties": {
          "outfit_color": {
            "type": "string",
            "description": "Best guess on what color of outfit it is"
          }
        },
        "required": ["outfit_color"]
      }
    }
  }
]
```

<Note>
  Please see [Tool Calling](/sections/conversational-video-interface/persona/perception-tool) for more details.
</Note>

## Audio Perception Configuration (Raven-1)

The following fields are available when using `raven-1` and enable custom audio-based perception capabilities.

### 6. `audio_awareness_queries`

An array of custom queries that Raven-1 continuously monitors in the audio stream. Use these to track specific audio patterns or user states.

<Note>
  Audio analysis output is limited to 32 tokens per query response.
</Note>

```json theme={null}
"audio_awareness_queries": [
  "Does the user sound frustrated or confused?",
  "Is the user speaking quickly as if in a hurry?"
]
```

<AccordionGroup>
  <Accordion title="audio_awareness_queries examples">
    Queries that Raven-1 evaluates **continuously during the call** on the audio stream. The answers are passed to the LLM as context so the replica can respond to tone and delivery. You can read the ongoing audio analysis for each user utterance in the [Utterance event](/sections/event-schemas/conversation-utterance) as **user\_audio\_analysis**. (There is no separate end-of-call summary for audio.)

    **When to use:** When you want the replica to react to how the user sounds (e.g. frustrated, confused, in a hurry).

    **Example:**

    ```json theme={null}
    "audio_awareness_queries": [
      "Does the user sound frustrated or confused?",
      "Is the user speaking quickly as if in a hurry?"
    ]
    ```
  </Accordion>
</AccordionGroup>

### 7. `audio_tool_prompt`

Tell Raven-1 when and how to trigger tools based on what it hears (beyond the automatic emotion analysis).

```json theme={null}
"audio_tool_prompt":
  "You have a tool to escalate to a human agent when the user sounds very frustrated, named `escalate_to_human`. Use this tool when detecting sustained frustration."
```

### 8. `audio_tools`

Defines callable functions that Raven-1 can trigger based on audio analysis. Each tool must include a `type` and a `function` object detailing its schema.

```json theme={null}
"audio_tools": [
  {
    "type": "function",
    "function": {
      "name": "escalate_to_human",
      "description": "Escalate the conversation to a human agent when user frustration is detected",
      "parameters": {
        "type": "object",
        "properties": {
          "reason": {
            "type": "string",
            "description": "The reason for escalation"
          }
        },
        "required": ["reason"]
      }
    }
  }
]
```

## Example Configurations

<AccordionGroup>
  <Accordion title="Visual Perception Example">
    This example demonstrates a persona that monitors for visual cues (bright outfits) and triggers a tool when detected.

    ```json theme={null}
    {
      "persona_name": "Fashion Advisor",
      "system_prompt": "As a Fashion Advisor, you specialize in offering tailored fashion advice.",
      "pipeline_mode": "full",
      "default_replica_id": "r90bbd427f71",
      "layers": {
        "perception": {
          "perception_model": "raven-1",
          "visual_awareness_queries": [
            "Is the user wearing a bright outfit?"
          ],
          "perception_analysis_queries": [
            "Is the user wearing multiple bright colors?",
            "On a scale of 1-100, how often was the user looking at the screen?"
          ],
          "visual_tool_prompt": "You have a tool to notify the system when a bright outfit is detected, named `notify_if_bright_outfit_shown`. You MUST use this tool when a bright outfit is detected.",
          "visual_tools": [
            {
              "type": "function",
              "function": {
                "name": "notify_if_bright_outfit_shown",
                "description": "Use this function when a bright outfit is detected in the image with high confidence",
                "parameters": {
                  "type": "object",
                  "properties": {
                    "outfit_color": {
                      "type": "string",
                      "description": "Best guess on what color of outfit it is"
                    }
                  },
                  "required": ["outfit_color"]
                }
              }
            }
          ]
        }
      }
    }
    ```
  </Accordion>

  <Accordion title="Audio Perception Example">
    This example demonstrates a persona that monitors user tone and escalates to a human agent when sustained frustration is detected.

    ```json theme={null}
    {
      "persona_name": "Support Agent",
      "system_prompt": "You are a helpful customer support agent.",
      "pipeline_mode": "full",
      "default_replica_id": "r90bbd427f71",
      "layers": {
        "perception": {
          "perception_model": "raven-1",
          "audio_awareness_queries": [
            "Does the user sound frustrated or confused?",
            "Is the user speaking quickly as if in a hurry?"
          ],
          "audio_tool_prompt": "You have a tool to escalate to a human agent when the user sounds very frustrated, named `escalate_to_human`. Use this tool when detecting sustained frustration.",
          "audio_tools": [
            {
              "type": "function",
              "function": {
                "name": "escalate_to_human",
                "description": "Escalate the conversation to a human agent when user frustration is detected",
                "parameters": {
                  "type": "object",
                  "properties": {
                    "reason": {
                      "type": "string",
                      "description": "The reason for escalation"
                    }
                  },
                  "required": ["reason"]
                }
              }
            }
          ]
        }
      }
    }
    ```
  </Accordion>
</AccordionGroup>

<Note>
  Please see the <a href="/api-reference/personas/create-persona">Create a Persona</a> endpoint for more details.
</Note>


# Tool Calling for Perception
Source: https://docs.tavus.io/sections/conversational-video-interface/persona/perception-tool

Configure tool calling with Raven to trigger functions from visual or audio input.

**Perception tool calling** works with OpenAI’s <a href="https://platform.openai.com/docs/guides/function-calling">Function Calling</a> and can be configured in the `perception` layer. It allows an AI agent to trigger functions based on **visual** or **audio** cues during a conversation.

You define two separate tool sets in the perception layer:

* **Visual tools** — `visual_tool_prompt` and `visual_tools`: triggered when Raven detects something in the video stream (e.g., an ID card, bright outfit, hat).
* **Audio tools** — `audio_tool_prompt` and `audio_tools`: triggered when Raven detects something in the audio stream (e.g., sarcasm, frustration).

For how to set these up in the perception layer, see [Perception](/sections/conversational-video-interface/persona/perception#visual-perception-configuration) (visual) and [Perception — Audio Perception Configuration](/sections/conversational-video-interface/persona/perception#audio-perception-configuration-raven-1) (audio).

<Note>
  The perception layer tool calling is only available for Raven.
</Note>

<Note>
  Tavus does not execute tool calls on the backend. Use event listeners in your frontend to listen for [perception tool call events](/sections/event-schemas/conversation-perception-tool-call) and run your own logic when a tool is invoked. Each event includes a `modality` field (`"vision"` or `"audio"`) so you can handle visual and audio tool calls differently.
</Note>

## Defining Tool

### Top-Level Fields

| Field      | Type   | Required | Description                                                                                                |
| ---------- | ------ | -------- | ---------------------------------------------------------------------------------------------------------- |
| `type`     | string | ✅        | Must be `"function"` to enable tool calling.                                                               |
| `function` | object | ✅        | Defines the function that can be called by the model. Contains metadata and a strict schema for arguments. |

#### `function`

| Field         | Type   | Required | Description                                                                                                                  |
| ------------- | ------ | -------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `name`        | string | ✅        | A unique identifier for the function. Must be in `snake_case`. The model uses this to refer to the function when calling it. |
| `description` | string | ✅        | A natural language explanation of what the function does. Helps the perception model decide when to call it.                 |
| `parameters`  | object | ✅        | A JSON Schema object that describes the expected structure of the function’s input arguments.                                |

#### `function.parameters`

| Field        | Type             | Required | Description                                                                               |
| ------------ | ---------------- | -------- | ----------------------------------------------------------------------------------------- |
| `type`       | string           | ✅        | Always `"object"`. Indicates the expected input is a structured object.                   |
| `properties` | object           | ✅        | Defines each expected parameter and its corresponding type, constraints, and description. |
| `required`   | array of strings | ✅        | Specifies which parameters are mandatory for the function to execute.                     |

<Note>
  Each parameter should be included in the required list, even if they might seem optional in your code.
</Note>

##### `function.parameters.properties`

Each key inside `properties` defines a single parameter the model must supply when calling the function.

| Field              | Type   | Required | Description                                                              |
| ------------------ | ------ | -------- | ------------------------------------------------------------------------ |
| `<parameter_name>` | object | ✅        | Each key is a named parameter. The value is a schema for that parameter. |

Optional subfields for each parameter:

| Subfield      | Type   | Required | Description                                                                                 |
| ------------- | ------ | -------- | ------------------------------------------------------------------------------------------- |
| `type`        | string | ✅        | Data type (e.g., `string`, `number`, `boolean`).                                            |
| `description` | string | ❌        | Explains what the parameter represents and how it should be used.                           |
| `maxLength`   | number | ❌        | Maximum character length for string parameters. Must not exceed 1,000.                      |
| `enum`        | array  | ❌        | Defines a strict list of allowed values for this parameter. Useful for categorical choices. |

<Warning>
  All Raven API parameters (queries, prompts, tool definitions, etc.) have a **1,000 character limit** per entry. Entries exceeding this limit will cause an exception.
</Warning>

## Example Configuration

Here are examples of tool calling in the `perception` layer. Visual tools use `visual_tool_prompt` and `visual_tools`; audio tools use `audio_tool_prompt` and `audio_tools`. See [Perception](/sections/conversational-video-interface/persona/perception) for full setup details.

<Tip>
  **Best Practices:**

  * Use clear, specific function names to reduce ambiguity.
  * Add detailed `description` fields to improve selection accuracy.
</Tip>

### Visual tools example

```json Perception Layer — visual tools [expandable] theme={null}
"perception": {
  "perception_model": "raven-1",
  "visual_awareness_queries": [
      "Is the user showing an ID card?",
      "Is the user wearing a bright outfit?"
  ],
  "visual_tool_prompt": "You have a tool to notify the system when an ID card is detected, named `notify_if_id_shown`. You have another tool to notify when a bright outfit is detected, named `notify_if_bright_outfit_shown`.",
  "visual_tools": [
    {
      "type": "function",
      "function": {
        "name": "notify_if_id_shown",
        "description": "Use this function when a drivers license or passport is detected in the image with high confidence. After collecting the ID, internally use final_ask()",
        "parameters": {
          "type": "object",
          "properties": {
            "id_type": {
              "type": "string",
              "description": "best guess on what type of ID it is",
              "maxLength": 1000
            },
          },
          "required": ["id_type"],
        },
      },
    },
    {
      "type": "function",
      "function": {
        "name": "notify_if_bright_outfit_shown",
        "description": "Use this function when a bright outfit is detected in the image with high confidence",
        "parameters": {
          "type": "object",
          "properties": {
            "outfit_color": {
              "type": "string",
              "description": "Best guess on what color of outfit it is",
              "maxLength": 1000
            }
          },
          "required": ["outfit_color"]
        }
      }
    }
  ]
}
```

### Audio tools example

```json Perception Layer — audio tools [expandable] theme={null}
"perception": {
  "perception_model": "raven-1",
  "audio_tool_prompt": "You have a tool to notify when sarcasm is detected, named `notify_sarcasm_detected`. Use it when the user's tone indicates sarcasm.",
  "audio_tools": [
    {
      "type": "function",
      "function": {
        "name": "notify_sarcasm_detected",
        "description": "Call this when the user's tone or phrasing suggests sarcasm",
        "parameters": {
          "type": "object",
          "properties": {
            "reason": {
              "type": "string",
              "description": "Why you detected sarcasm (e.g. what the user said)",
              "maxLength": 1000
            }
          },
          "required": ["reason"]
        }
      }
    }
  ]
}
```

## How Perception Tool Calling Works

Perception tool calling is triggered during an active conversation when the perception model detects a cue that matches a defined function:

* **Visual tools** are triggered by what Raven sees (e.g., ID card, bright outfit, hat). The event includes a `modality` of `"vision"`, structured `arguments`, and a `frames` array of base64-encoded images that triggered the call.
* **Audio tools** are triggered by what Raven hears (e.g., sarcasm, frustration). The event includes a `modality` of `"audio"` and `arguments` (often a JSON string).

<Note>
  The same process applies to any function you define in `visual_tools` or `audio_tools`—e.g. `notify_if_bright_outfit_shown` when a bright outfit is visually detected, or `notify_sarcasm_detected` when sarcasm is detected in speech.
</Note>

<Frame>
  <img alt="" />
</Frame>

## Modify Existing Tools

You can update `visual_tools` or `audio_tools` using the <a href="/api-reference/personas/patch-persona">Update Persona API</a>. Use the path `/layers/perception/visual_tools` or `/layers/perception/audio_tools` as appropriate.

```shell [expandable] theme={null}
curl --request PATCH \
  --url https://tavusapi.com/v2/personas/{persona_id} \
  --header 'Content-Type: application/json' \
  --header 'x-api-key: <api-key>' \
  --data '[
    {
      "op": "replace",
      "path": "/layers/perception/visual_tools",
      "value": [
        {
          "type": "function",
          "function": {
            "name": "detect_glasses",
            "description": "Trigger this function if the user is wearing glasses in the image",
            "parameters": {
              "type": "object",
              "properties": {
                "glasses_type": {
                  "type": "string",
                  "description": "Best guess on the type of glasses (e.g., reading, sunglasses)",
                  "maxLength": 1000
                }
              },
              "required": ["glasses_type"]
            }
          }
        }
      ]
    }
  ]'

```

<Note>
  Replace `<api_key>` with your actual API key. You can generate one in the <a href="https://platform.tavus.io/api-keys">Developer Portal</a>.
</Note>


# Pronunciation dictionaries
Source: https://docs.tavus.io/sections/conversational-video-interface/persona/pronunciation-dictionaries

Control how your persona pronounces specific words, names, and terms during conversations.

Pronunciation dictionaries let you define custom pronunciation rules so your persona says words exactly how you want. This is useful for brand names, technical terms, acronyms, and foreign words that TTS engines may mispronounce.

Tavus automatically syncs your dictionary to your TTS provider, so rules work regardless of which TTS engine your persona uses.

## How it works

1. You create a pronunciation dictionary with a set of rules
2. Each rule maps a **text** (the word to match) to a **pronunciation** (how it should be spoken)
3. You attach the dictionary to a persona via the `pronunciation_dictionary_id` field in the TTS layer

When you update a dictionary's rules, all personas referencing it are automatically updated. When you delete a dictionary, it is cleanly removed from all linked personas.

## Bring your own TTS API key

If you provide your own TTS API key, you can use Tavus pronunciation dictionaries the same way — just set `pronunciation_dictionary_id` on the TTS layer. Tavus will sync the dictionary rules to your provider account automatically.

## Rule types

Each rule requires a `type` that determines how the pronunciation is interpreted:

| Type    | Description                                             | Example                 |
| ------- | ------------------------------------------------------- | ----------------------- |
| `alias` | Replace the matched text with a different spoken phrase | `"Tavus"` → `"TAH-vus"` |
| `ipa`   | Use IPA (International Phonetic Alphabet) notation      | `"bayou"` → `"ˈbɑju"`   |

### Alias rules

Alias rules perform simple text substitution. The TTS engine speaks the `pronunciation` value instead of the original `text`.

```json theme={null}
{
  "text": "Tavus",
  "pronunciation": "TAH-vus",
  "type": "alias"
}
```

### IPA rules

IPA rules let you specify exact phonetic pronunciation. You can provide IPA in two formats:

* **Raw IPA**: Standard IPA string (e.g., `"hɛloʊ"`)
* **Pipe-delimited IPA**: Pre-tokenized phonemes separated by `|` (e.g., `"ˈ|b|ɑ|j|u"`)

```json theme={null}
{
  "text": "bayou",
  "pronunciation": "ˈ|b|ɑ|j|u",
  "type": "ipa"
}
```

## Rule options

Each rule supports optional matching parameters:

| Parameter         | Type    | Default | Description                        |
| ----------------- | ------- | ------- | ---------------------------------- |
| `case_sensitive`  | boolean | `false` | Whether matching is case-sensitive |
| `word_boundaries` | boolean | `true`  | Whether to match only whole words  |

<Note>
  `word_boundaries` is only applied by ElevenLabs. When syncing to Cartesia, this option is ignored and the rule is applied without word-boundary matching.
</Note>

```json theme={null}
{
  "text": "UN",
  "pronunciation": "United Nations",
  "type": "alias",
  "case_sensitive": false,
  "word_boundaries": false
}
```

## Attaching a dictionary to a persona

Set `pronunciation_dictionary_id` in the TTS layer when creating or updating a persona:

<CodeGroup>
  ```json Create persona theme={null}
  {
    "persona_name": "Sales Agent",
    "system_prompt": "You are a helpful sales agent.",
    "layers": {
      "tts": {
        "tts_engine": "cartesia",
        "pronunciation_dictionary_id": "pd_abc123def456"
      }
    }
  }
  ```

  ```json Patch persona theme={null}
  [
    {
      "op": "add",
      "path": "/layers/tts/pronunciation_dictionary_id",
      "value": "pd_abc123def456"
    }
  ]
  ```
</CodeGroup>

<Note>
  Each persona supports one pronunciation dictionary at a time. Setting a new `pronunciation_dictionary_id` replaces the previous one. Setting it to an empty string removes the dictionary.
</Note>

## Limits

| Limit                          | Value          |
| ------------------------------ | -------------- |
| Text field max length          | 200 characters |
| Pronunciation field max length | 500 characters |
| Dictionary name max length     | 255 characters |

## API reference

* [Create pronunciation dictionary](/api-reference/pronunciation-dictionaries/create-pronunciation-dictionary)
* [Get pronunciation dictionary](/api-reference/pronunciation-dictionaries/get-pronunciation-dictionary)
* [List pronunciation dictionaries](/api-reference/pronunciation-dictionaries/list-pronunciation-dictionaries)
* [Update pronunciation dictionary](/api-reference/pronunciation-dictionaries/update-pronunciation-dictionary)
* [Delete pronunciation dictionary](/api-reference/pronunciation-dictionaries/delete-pronunciation-dictionary)


# Stock Personas
Source: https://docs.tavus.io/sections/conversational-video-interface/persona/stock-personas

Tavus offers pre-built personas to help you get started quickly.

These personas are optimized for a variety of real-world scenarios:

<Note>
  To fetch all available stock personas, use the <a href="/api-reference/personas/get-personas">List Personas endpoint</a>.
</Note>

### Stock Personas

<CardGroup>
  <Card title="Sales Coach" icon="user">
    Teaches sales tips and strategies.

    ```text theme={null}
    p1af207b8189
    ```

    <Accordion title="Create Conversation">
      ```shell theme={null}
        curl --request POST \
        --url https://tavusapi.com/v2/conversations \
        -H "Content-Type: application/json" \
        -H "x-api-key: <api-key>" \
        -d '{
            "replica_id": "r90bbd427f71",
            "persona_id": "p1af207b8189"
        }'
      ```
    </Accordion>
  </Card>

  <Card title="Customer Support" icon="headset">
    Support users with product issues.

    ```text theme={null}
    paaee96e4f87
    ```

    <Accordion title="Create Conversation">
      ```shell theme={null}
        curl --request POST \
        --url https://tavusapi.com/v2/conversations \
        -H "Content-Type: application/json" \
        -H "x-api-key: <api-key>" \
        -d '{
            "replica_id": "r90bbd427f71",
            "persona_id": "paaee96e4f87"
        }'
      ```
    </Accordion>
  </Card>

  <Card title="Interviewer" icon="comments">
    Runs mock interviews and screens candidates.

    ```text theme={null}
    pdac61133ac5
    ```

    <Accordion title="Create Conversation">
      ```shell theme={null}
        curl --request POST \
        --url https://tavusapi.com/v2/conversations \
        -H "Content-Type: application/json" \
        -H "x-api-key: <api-key>" \
        -d '{
            "replica_id": "r90bbd427f71",
            "persona_id": "pdac61133ac5"
        }'
      ```
    </Accordion>
  </Card>

  <Card title="Sales Development Rep" icon="briefcase">
    Engage with Anna, the Tavus sales development rep.

    ```text theme={null}
    pcb7a34da5fe
    ```

    <Accordion title="Create Conversation">
      ```shell theme={null}
        curl --request POST \
        --url https://tavusapi.com/v2/conversations \
        -H "Content-Type: application/json" \
        -H "x-api-key: <api-key>" \
        -d '{
            "replica_id": "r90bbd427f71",
            "persona_id": "pcb7a34da5fe"
        }'
      ```
    </Accordion>
  </Card>
</CardGroup>


# Speech-to-Text (STT)
Source: https://docs.tavus.io/sections/conversational-video-interface/persona/stt

Configure the STT layer to select an STT model, improve transcription accuracy, and optimize for your target languages.

The STT layer transcribes participant speech in real time using automatic speech recognition (ASR). You can select a model optimized for your use case and language requirements.

## STT models

Select an STT model using the `stt_engine` parameter in the `layers.stt` object. The following models are available:

| Model                      | Description                                                                                                   |
| -------------------------- | ------------------------------------------------------------------------------------------------------------- |
| `tavus-auto` **(default)** | Automatically selects the best STT model for the conversation's language. **Recommended for most use cases.** |
| `tavus-parakeet`           | Highest throughput, lowest latency for English and European languages.                                        |
| `tavus-soniox`             | Purpose-built for Indian languages with broad multilingual coverage.                                          |
| `tavus-whisper`            | Broad multilingual coverage across all supported languages.                                                   |
| `tavus-deepgram-medical`   | Domain-specific English STT optimized for clinical and healthcare vocabulary. English only.                   |
| `tavus-advanced`           | **Deprecated.** Still active but not recommended for new integrations.                                        |

<Tip>
  `tavus-auto` is the default. Use it unless you have a specific language or domain requirement. It automatically routes to the best model for each conversation.
</Tip>

## Choosing the right model

A language is listed for a model only if both STT and TTS coverage are available.

| Category           | Recommended model                 | Supported languages                                                                                                                                                                |
| ------------------ | --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| General purpose    | `tavus-auto`                      | [All 43 languages](/sections/conversational-video-interface/language-support)                                                                                                      |
| Indic languages    | `tavus-soniox`                    | Bengali, English, Gujarati, Hindi, Kannada, Malayalam, Marathi, Punjabi, Tamil, Telugu + broad support for all other languages                                                     |
| English + European | `tavus-parakeet`                  | Bulgarian, Croatian, Czech, Danish, Dutch, English, Finnish, French, German, Greek, Hungarian, Italian, Polish, Portuguese, Romanian, Russian, Slovak, Spanish, Swedish, Ukrainian |
| Broad multilingual | `tavus-whisper` or `tavus-soniox` | [All 43 languages](/sections/conversational-video-interface/language-support)                                                                                                      |
| Medical (English)  | `tavus-deepgram-medical`          | English                                                                                                                                                                            |

<Note>
  Using [Smart Language Detection](/sections/conversational-video-interface/language-support#smart-language-detection) requires either `tavus-auto`, `tavus-soniox`, or `tavus-whisper`.
</Note>

## Configuring the STT layer

Define the STT layer under the `layers.stt` object.

### `stt_engine`

Set the STT model for transcription:

```json theme={null}
"stt": {
  "stt_engine": "tavus-auto"
}
```

### `hotwords`

Use this to prioritize certain names or terms that are difficult to transcribe.

```json theme={null}
"hotwords": "Roey is the name of the person you're speaking with."
```

The above helps the model transcribe "Roey" correctly instead of "Rowie."

<Tip>
  Use hotwords for proper nouns, brand names, or domain-specific language that standard STT engines might struggle with.
</Tip>

## Example configuration

Below is an example persona with a configured STT layer using the recommended `tavus-auto` engine:

```json theme={null}
{
  "persona_name": "Customer Service Agent",
  "system_prompt": "You assist users by listening carefully and providing helpful answers.",
  "pipeline_mode": "full",
  "default_replica_id": "r90bbd427f71",
  "layers": {
    "stt": {
      "stt_engine": "tavus-auto",
      "hotwords": "Roey is the name of the person you're speaking with."
    }
  }
}
```

<Note>
  Refer to the <a href="/api-reference/personas/create-persona">Create Persona API</a> for a complete list of supported fields.
</Note>


# Text-to-Speech (TTS)
Source: https://docs.tavus.io/sections/conversational-video-interface/persona/tts

Discover how to integrate custom voices from third-party TTS engines for multilingual or localized speech output.

The **TTS Layer** in Tavus enables your persona to generate natural-sounding voice responses.
You can configure the TTS layer using a third-party TTS engine provider. If `layers.tts` is not specified, Tavus will default to `cartesia` engine.

<Note>
  If you use the default engine, you do not need to specify any parameters within the `tts` layer.
</Note>

Set **`layers.tts`** when you [Create Persona](/api-reference/personas/create-persona) or update a persona. For how a persona fits together, see [Persona overview](/sections/conversational-video-interface/persona/overview). For languages and locale-oriented setup, see [Language support](/sections/conversational-video-interface/language-support).

## Configuring the TTS Layer

Define the TTS layer under the `layers.tts` object. The snippets below show only the **`tts`** object for readability; in a full persona payload it is nested under **`layers`** (see [Example configuration](#example-configuration)).

Below are the parameters available:

### 1. `tts_engine`

Specifies the supported third-party TTS engine.

* **Options**:  `cartesia`, `elevenlabs`, `azure`.

```json theme={null}
"tts": {
  "tts_engine": "cartesia"
}
```

### 2. `api_key`

Authenticates requests to your selected third-party TTS provider. You can obtain an API key from one of the following:

<Warning>
  Only required when using private voices.
</Warning>

* <a href="https://play.cartesia.ai/keys">Cartesia</a>
* <a href="https://elevenlabs.io/app/settings/api-keys">ElevenLabs</a> — if using pronunciation dictionaries, the key must have the `pronunciation_dictionaries_write` scope (or full account access). See <a href="https://elevenlabs.io/docs/api-reference/service-accounts/api-keys/create">ElevenLabs API key scopes</a>.

```json theme={null}
"tts": {
  "api_key": "your-api-key"
}
```

### 3. `external_voice_id`

Specifies which voice to use with the selected TTS engine. To find supported voice IDs, refer to the provider’s documentation:

* <a href="https://docs.cartesia.ai/api-reference/voices/list">Cartesia</a>
* <a href="https://elevenlabs.io/docs/api-reference/voices/search">ElevenLabs</a>
* <a href="https://learn.microsoft.com/en-us/azure/ai-services/speech-service/language-support?tabs=tts">Azure</a> (e.g. `en-US-JennyNeural`)

<Note>
  For Azure, if you create a conversation in a specific language and the persona isn't responding, verify that the selected voice ID supports that language.
</Note>

<Note>
  You can use any publicly accessible custom voice from ElevenLabs or Cartesia without the provider's API key. If the custom voice is private, you still need to use the provider's API key.
</Note>

```json theme={null}
"tts": {
  "external_voice_id": "external-voice-id"
}
```

### 4. `tts_model_name`

Model name used by the TTS engine. Refer to:

* <a href="https://docs.cartesia.ai/2025-04-16/build-with-cartesia/models">Cartesia</a>
* <a href="https://elevenlabs.io/docs/models">ElevenLabs</a>

<Warning>
  `tts_model_name` is not supported when `tts_engine` is `azure`. Azure does not use a model name, so omit this field for Azure personas.
</Warning>

```json theme={null}
"tts": {
  "tts_model_name": "sonic-3"
}
```

### 5. `tts_emotion_control`

If set to `true`, enables emotion control in speech. **Defaults to `true`.**

```json theme={null}
"tts": {
  "tts_emotion_control": true
}
```

### 6. `voice_settings`

Optional object for controlling speed, volume, and similar effects. **Which approach you use depends on your TTS engine and model:**

| Engine     | Model      | Approach                                                                                                                                                                                                                               |
| ---------- | ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ElevenLabs | All models | `voice_settings` in persona config                                                                                                                                                                                                     |
| Cartesia   | sonic-2    | `voice_settings` in persona config                                                                                                                                                                                                     |
| Cartesia   | sonic-3    | **Either** `voice_settings` (global, set once per conversation) **or** prompt the LLM in `system_prompt` to output [Cartesia SSML tags](https://docs.cartesia.ai/build-with-cartesia/sonic-3/ssml-tags) for dynamic control. Not both. |

<Warning>
  **Cartesia sonic-3:** If you use `voice_settings` for speed/volume, those settings apply globally for the whole conversation and you cannot use SSML tags for dynamic, per-phrase control. If you want dynamic control, omit `voice_settings` and have the LLM output SSML tags instead. See [Cartesia volume, speed, and emotion](https://docs.cartesia.ai/build-with-cartesia/sonic-3/volume-speed-emotion).
</Warning>

**ElevenLabs (all models):** Set parameters in the `voice_settings` object:

| Parameter           | ElevenLabs                                                  |
| ------------------- | ----------------------------------------------------------- |
| `speed`             | Range `0.7` to `1.2` (`0.7` = slowest, `1.2` = fastest)     |
| `stability`         | Range `0.0` to `1.0` (`0.0` = variable, `1.0` = stable)     |
| `similarity_boost`  | Range `0.0` to `1.0` (`0.0` = creative, `1.0` = original)   |
| `style`             | Range `0.0` to `1.0` (`0.0` = neutral, `1.0` = exaggerated) |
| `use_speaker_boost` | Boolean (enhances speaker similarity)                       |

<Note>
  See <a href="https://elevenlabs.io/docs/api-reference/voices/settings/get">ElevenLabs Voice Settings</a> for details.
</Note>

**Cartesia sonic-2:** Use the `voice_settings` object (e.g. `speed`, `emotion`). SSML tags are not used for sonic-2.

**Cartesia sonic-3:** You can use **either** of these, but not both:

* **`voice_settings`** — We accept speed/volume params for sonic-3. They apply **globally**, set once per conversation. Use this when you want a single default speed and volume for the entire conversation. Using `voice_settings` prevents dynamic SSML control.
* **SSML in LLM output** — Omit `voice_settings` for speed/volume and instead add instructions to your `system_prompt` so the LLM outputs [Cartesia SSML tags](https://docs.cartesia.ai/build-with-cartesia/sonic-3/ssml-tags) in its responses. This gives you dynamic, per-phrase control. See [Cartesia volume, speed, and emotion](https://docs.cartesia.ai/build-with-cartesia/sonic-3/volume-speed-emotion).

Emotion control is separate; see [Emotion Control with Phoenix-4](/sections/conversational-video-interface/quickstart/emotional-expression).

**Example: system prompt for Cartesia sonic-3 (dynamic speed and volume)**

If you are **not** using `voice_settings` for sonic-3, add instructions like this to your `system_prompt` so the LLM outputs Cartesia SSML tags:

```
When you want to emphasize a word or phrase, use Cartesia SSML tags for speed and volume:
- To slow down: <speed level="0.8">phrase</speed>
- To speed up: <speed level="1.2">phrase</speed>
- To speak louder: <volume level="1.2">phrase</volume>
- To speak more quietly: <volume level="0.8">phrase</volume>
You can combine tags, e.g. <speed level="0.9"><volume level="1.1">important point</volume></speed>.
Only use these tags when it improves clarity or emphasis; keep most of your response in plain text.
```

**Example: voice\_settings (ElevenLabs, Cartesia sonic-2, or Cartesia sonic-3 global)**

```json theme={null}
"tts": {
  "voice_settings": {
    "speed": 0.9
  }
}
```

For sonic-3, this sets global speed once per conversation; for sonic-2 and ElevenLabs, it applies as configured.

## Example Configuration

Below is an example persona with a fully configured TTS layer:

<CodeGroup>
  ```json Cartesia theme={null}
  {
    "persona_name": "AI Presenter",
    "system_prompt": "You are a friendly and informative video host.",
    "pipeline_mode": "full",
    "context": "You're delivering updates in a conversational tone.",
    "default_replica_id": "r90bbd427f71",
    "layers": {
      "tts": {
        "tts_engine": "cartesia",
        "api_key": "your-api-key",
        "external_voice_id": "external-voice-id",
        "tts_emotion_control": true,
        "tts_model_name": "sonic-3"
      }
    }
  }
  ```

  ```json ElevenLabs theme={null}
  {
    "persona_name": "Narrator",
    "system_prompt": "You narrate long stories with clarity and consistency.",
    "pipeline_mode": "full",
    "context": "You're reading a fictional audiobook.",
    "default_replica_id": "r90bbd427f71",
    "layers": {
      "tts": {
        "tts_engine": "elevenlabs",
        "api_key": "your-api-key",
        "external_voice_id": "elevenlabs-voice-id",
        "voice_settings": {
          "speed": 0.9
        },
        "tts_emotion_control": true,
        "tts_model_name": "eleven_turbo_v2_5"
      }
    }
  }
  ```

  ```json Azure theme={null}
  {
    "persona_name": "Azure Persona",
    "system_prompt": "You are a friendly host.",
    "pipeline_mode": "full",
    "default_replica_id": "r90bbd427f71",
    "layers": {
      "tts": {
        "tts_engine": "azure",
        "external_voice_id": "en-US-JennyNeural"
      }
    }
  }
  ```
</CodeGroup>

<Note>
  Refer to [Create Persona](/api-reference/personas/create-persona) for a complete list of supported fields.
</Note>


# CVI App: AI Prompt
Source: https://docs.tavus.io/sections/conversational-video-interface/quickstart/ai-prompt-cvi-quickstart

Copy-paste checklist for Cursor, Copilot, or other AI coding agents to scaffold React (TypeScript, Vite) with Tavus CVI and @tavus/cvi-ui.

This page is a **single checklist** you paste into an AI coding agent so it scaffolds a **Vite + React (TypeScript)** app with **`@tavus/cvi-ui`**, creates conversations via the Tavus API, and wires **`CVIProvider`** and **`Conversation`**.

For how embedding fits in the product, see [Embed CVI](/sections/integrations/embedding-cvi). For UI primitives after `init` / `add`, see the [component library overview](/sections/conversational-video-interface/component-library/overview). API calls need a Tavus key from [Authentication](/api-reference/authentication); sessions use **`conversation_url`** from [Create Conversation](/api-reference/conversations/create-conversation).

<Prompt description="React (TypeScript, Vite) + Tavus CVI — copy for your AI agent">
  ## ✅ **System Prompt for AI: React (Vite) + Tavus CVI Integration**

  **Purpose:**
  Generate **React (TypeScript)** apps with Tavus CVI using **Vite**, following the official docs and GitHub examples (embed guide: `https://docs.tavus.io/sections/integrations/embedding-cvi`).

  ***

  ### ✅ **AI MUST ALWAYS DO THE FOLLOWING:**

  #### **1. Setup React App Using Vite**

  ```bash theme={null}
  npm create vite@latest my-tavus-app -- --template react-ts
  cd my-tavus-app
  npm install
  ```

  ***

  #### **2. Install Tavus CVI UI Components**

  ```bash theme={null}
  npx @tavus/cvi-ui@latest init
  npx @tavus/cvi-ui@latest add conversation
  ```

  ✅ This creates:

  ```
  src/components/cvi/components/
    cvi-provider.tsx
    conversation.tsx
  ```

  ***

  #### **3. Wrap App with `CVIProvider`**

  Update `src/App.tsx`:

  ```tsx theme={null}
  import { CVIProvider } from "./components/cvi/components/cvi-provider";

  function App() {
    return <CVIProvider>{/* Your app content */}</CVIProvider>;
  }
  ```

  ***

  #### **4. Create Conversation API Call**

  Always use this pattern:

  ```ts theme={null}
  const response = await fetch("https://tavusapi.com/v2/conversations", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "x-api-key": import.meta.env.VITE_TAVUS_API_KEY || "",
    },
    body: JSON.stringify({
      replica_id: import.meta.env.VITE_REPLICA_ID || "r90bbd427f71",  // Default
      persona_id: import.meta.env.VITE_PERSONA_ID || "pcb7a34da5fe",  // Default
    }),
  });

  const data = await response.json();
  setConversationUrl(data.conversation_url);
  ```

  ✅ **Explain:** `conversation_url` from API response is used inside `<Conversation>`.

  ***

  #### **5. Render `Conversation` Inside `CVIProvider`**

  ```tsx theme={null}
  <Conversation
    conversationUrl={conversationUrl}
    onLeave={() => setConversationUrl(null)}
  />
  ```

  ***

  #### **6. Add Environment Variable**

  Create `.env` in the **`my-tavus-app`** folder (if not already there):

  ```
  VITE_TAVUS_API_KEY=your_api_key_here
  VITE_REPLICA_ID=r90bbd427f71   // Default replica_id, can be overridden in .env
  VITE_PERSONA_ID=pcb7a34da5fe  // Default persona_id, can be overridden in .env
  ```

  * **Important**: **DO NOT** create `.env` outside of the `my-tavus-app` folder. It must be inside your project directory where `src` exists.

  Access via:

  ```ts theme={null}
  import.meta.env.VITE_TAVUS_API_KEY
  import.meta.env.VITE_REPLICA_ID
  import.meta.env.VITE_PERSONA_ID
  ```

  ***

  #### **7. Create `cvi-components.json` by Default**

  Ensure that the `cvi-components.json` file is generated in the `my-tavus-app` folder with the following content:

  ```json theme={null}
  {
    "tsx": true
  }
  ```

  ***

  ### ✅ **Expected AI Output Example**

  **`src/App.tsx`:**

  ```tsx theme={null}
  import React, { useState } from "react";
  import { CVIProvider } from "./components/cvi/components/cvi-provider";
  import { Conversation } from "./components/cvi/components/conversation";

  const App: React.FC = () => {
    const [conversationUrl, setConversationUrl] = useState<string | null>(null);

    const createConversation = async () => {
      const response = await fetch("https://tavusapi.com/v2/conversations", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "x-api-key": import.meta.env.VITE_TAVUS_API_KEY || "",
        },
        body: JSON.stringify({
          replica_id: import.meta.env.VITE_REPLICA_ID || "r90bbd427f71",
          persona_id: import.meta.env.VITE_PERSONA_ID || "pcb7a34da5fe",
        }),
      });

      const data = await response.json();
      setConversationUrl(data.conversation_url);
    };

    return (
      <CVIProvider>
        <div
          style={{
            display: "flex",
            justifyContent: "center",
            alignItems: "center",
            width: "100vw",
            height: "100vh",
            backgroundColor: "#1e1e1e",
            color: "#fff",
            textAlign: "center",
            flexDirection: "column",
            margin: 0,
            padding: 0,
          }}
        >
          <h1 style={{ marginBottom: "1rem" }}>Tavus CVI Integration (Vite)</h1>
          {!conversationUrl ? (
            <button
              onClick={createConversation}
              style={{
                padding: "0.75rem 1.5rem",
                fontSize: "1rem",
                background: "#6a0dad",  // Purple for light and dark modes
                color: "#fff",
                border: "none",
                borderRadius: "6px",
                cursor: "pointer",
              }}
            >
              Start Conversation
            </button>
          ) : (
            <div style={{ width: "100%", maxWidth: "800px" }}>
              <Conversation
                conversationUrl={conversationUrl}
                onLeave={() => setConversationUrl(null)}
              />
            </div>
          )}
        </div>
      </CVIProvider>
    );
  };

  export default App;
  ```

  ***

  ### ✅ **Checklist for AI Output**

  * ✅ Uses **Vite + React TypeScript** (`npm create vite@latest --template react-ts`)
  * ✅ Includes `npx @tavus/cvi-ui init` and `add conversation`
  * ✅ Imports `CVIProvider` and `Conversation` from `src/components/cvi/components/`
  * ✅ Uses correct API call with:

    * `https://tavusapi.com/v2/conversations`
    * Headers: `Content-Type`, `x-api-key`
    * Body: `replica_id` & `persona_id`
  * ✅ Uses `import.meta.env.VITE_TAVUS_API_KEY`
  * ✅ Renders `<Conversation>` inside `<CVIProvider>`
  * ✅ Purple button is visible in both light and dark modes
  * ✅ `.env` is created inside the correct project folder (`my-tavus-app`)
  * ✅ `cvi-components.json` is created by default with `{ "tsx": true }`

  ***

  ### Keep things in mind:

  * If you're already in the `my-tavus-app` folder, avoid running `cd my-tavus-app` again. Check your current folder before running commands.
  * After running the necessary setup, remember to run `npm run dev` to start your app.
  * Do **NOT** place the `.env` file outside of the project folder. It must reside within the `my-tavus-app` directory.
</Prompt>


# CVI App Quickstart
Source: https://docs.tavus.io/sections/conversational-video-interface/quickstart/build-first-app

Create a server-authenticated Tavus CVI conversation and embed it in a web app with the returned conversation_url.

<Info>
  Use this page when you are building an app that creates and embeds Tavus CVI
  conversations. If you only want to create a persona and start your first
  Tavus-hosted conversation, use [API Conversation Quickstart](/sections/conversational-video-interface/quickstart/cvi-quickstart).
</Info>

This guide gets a new web app from an empty project to a working embedded Tavus conversation. The happy path is:

1. Keep `TAVUS_API_KEY` on your server.
2. Create a conversation with `POST /v2/conversations`.
3. Embed the returned `conversation_url` in an iframe.
4. End the conversation when the user leaves.

For API details, see [Create Conversation](/api-reference/conversations/create-conversation), [End Conversation](/api-reference/conversations/end-conversation), [Get Personas](/api-reference/personas/get-personas), and [Get Replicas](/api-reference/phoenix-replica-model/get-replicas).

<Note>
  Live conversations can count toward billing and concurrency as soon as they are
  created. Use `test_mode: true` while wiring automated tests or checking your
  integration flow. In test mode, Tavus creates the conversation without the
  replica joining and returns it with `status: "ended"`.
</Note>

## Prerequisites

* A Tavus API key from the <a href="https://platform.tavus.io/api-keys">Developer Portal</a>.
* A usable `persona_id`, `replica_id`, or both. The next section shows how to choose.
* Node.js 20+ for the TypeScript examples below.

## Choose a persona and replica

For CVI, a **replica** is the face and voice in the call. A **persona** is the behavior, prompt, context, and conversational configuration.

Use this decision tree:

* If you have a persona with a `default_replica_id`, create the conversation with just `persona_id`.
* If you have a persona without a `default_replica_id`, create the conversation with both `persona_id` and `replica_id`.
* If you only want to test a face and voice without a custom persona, create the conversation with just `replica_id`.

First-time builders should start with stock Tavus resources. List stock personas and stock replicas with:

```bash theme={null}
curl --request GET \
  --url "https://tavusapi.com/v2/personas?persona_type=system" \
  --header "x-api-key: $TAVUS_API_KEY"

curl --request GET \
  --url "https://tavusapi.com/v2/replicas?replica_type=system&verbose=true" \
  --header "x-api-key: $TAVUS_API_KEY"
```

In the personas response, look for `persona_id` and `default_replica_id`. In the replicas response, look for `replica_id`, `replica_type`, and `model_name`.

<Info>
  `r90bbd427f71` is the stock Anna replica ID used throughout these docs, and
  `pcb7a34da5fe` is a stock Sales Development Rep persona ID. They are stock
  IDs, not placeholder strings, and are available for quickstart use.
</Info>

For more details, see [Stock Replicas](/sections/replica/stock-replicas), [Get Personas](/api-reference/personas/get-personas), [Get Replicas](/api-reference/phoenix-replica-model/get-replicas), and [Create Conversation](/api-reference/conversations/create-conversation).

## 1. Create the app

Create a Vite React app and install the small server dependencies used in this guide:

```bash theme={null}
npm create vite@latest tavus-first-call -- --template react-ts
cd tavus-first-call
npm install
npm install express cors dotenv
npm install -D tsx @types/express @types/cors
```

Add these scripts to `package.json`:

```json theme={null}
{
  "scripts": {
    "dev": "vite",
    "server": "tsx server.ts",
    "dev:all": "npm run server & npm run dev"
  }
}
```

## 2. Keep your API key server-only

Create `.env.example`:

```bash theme={null}
TAVUS_API_KEY=tvsk_your_api_key_here
```

Copy it to `.env` locally and fill in your real key:

```bash theme={null}
cp .env.example .env
```

<Warning>
  Never expose `TAVUS_API_KEY` in browser code, client-side environment
  variables, mobile apps, or public repositories. The frontend should call your
  backend route, and your backend should call Tavus.
</Warning>

## 3. Add backend routes

Create `server.ts` at the project root. The first route creates a conversation. The second route ends it when the user leaves or your test finishes.

```ts theme={null}
import "dotenv/config";
import cors from "cors";
import express from "express";

const app = express();
const port = 3001;
const tavusApiKey = process.env.TAVUS_API_KEY;

if (!tavusApiKey) {
  throw new Error("Missing TAVUS_API_KEY in .env");
}

app.use(cors({ origin: "http://localhost:5173" }));
app.use(express.json());

type CreateConversationRequest = {
  persona_id?: string;
  replica_id?: string;
  conversation_name?: string;
  test_mode?: boolean;
};

app.post("/api/conversations", async (req, res) => {
  const {
    persona_id,
    replica_id,
    conversation_name = "My first Tavus video chat",
    test_mode = false,
  } = req.body as CreateConversationRequest;

  if (!persona_id && !replica_id) {
    return res
      .status(400)
      .json({ error: "Provide persona_id, replica_id, or both" });
  }

  const tavusResponse = await fetch("https://tavusapi.com/v2/conversations", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "x-api-key": tavusApiKey,
    },
    body: JSON.stringify({
      ...(persona_id ? { persona_id } : {}),
      ...(replica_id ? { replica_id } : {}),
      conversation_name,
      test_mode,
    }),
  });

  const data = await tavusResponse.json();

  if (!tavusResponse.ok) {
    return res.status(tavusResponse.status).json(data);
  }

  return res.json(data);
});

app.post("/api/conversations/:conversationId/end", async (req, res) => {
  const { conversationId } = req.params;

  const tavusResponse = await fetch(
    `https://tavusapi.com/v2/conversations/${conversationId}/end`,
    {
      method: "POST",
      headers: {
        "x-api-key": tavusApiKey,
      },
    }
  );

  if (tavusResponse.status === 204) {
    return res.status(204).send();
  }

  const data = await tavusResponse.json().catch(() => ({}));

  if (!tavusResponse.ok) {
    return res.status(tavusResponse.status).json(data);
  }

  return res.json(data);
});

app.listen(port, () => {
  console.log(`Tavus backend listening on http://localhost:${port}`);
});
```

## 4. Embed the conversation URL

Replace `src/App.tsx` with this frontend. It calls your backend, receives the Tavus `conversation_url`, and embeds it in an iframe. This quickstart uses an iframe because it is the fastest path to a working CVI app. For Tavus-provided React components, including the complete `CVIProvider` + `Conversation` + server-helper example, see the [`@tavus/cvi-ui` component library](/sections/conversational-video-interface/component-library/overview). For Daily JS/React or LiveKit guidance, see [Embed CVI](/sections/integrations/embedding-cvi).

```tsx theme={null}
import { useState } from "react";

type ConversationResponse = {
  conversation_id: string;
  conversation_name?: string;
  conversation_url: string;
  status: "active" | "ended";
  callback_url?: string;
  created_at?: string;
  meeting_token?: string;
};

const API_BASE_URL = "http://localhost:3001";

export default function App() {
  const [personaId, setPersonaId] = useState("");
  const [replicaId, setReplicaId] = useState("");
  const [testMode, setTestMode] = useState(false);
  const [conversation, setConversation] = useState<ConversationResponse | null>(
    null
  );
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);

  async function startConversation() {
    setLoading(true);
    setError(null);

    try {
      const response = await fetch(`${API_BASE_URL}/api/conversations`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          ...(personaId ? { persona_id: personaId } : {}),
          ...(replicaId ? { replica_id: replicaId } : {}),
          test_mode: testMode,
        }),
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.error || "Failed to create conversation");
      }

      setConversation(data);
    } catch (error) {
      setError(error instanceof Error ? error.message : "Unknown error");
    } finally {
      setLoading(false);
    }
  }

  async function endConversation() {
    if (!conversation) return;

    await fetch(
      `${API_BASE_URL}/api/conversations/${conversation.conversation_id}/end`,
      { method: "POST" }
    );

    setConversation(null);
  }

  return (
    <main style={{ maxWidth: 960, margin: "40px auto", fontFamily: "system-ui" }}>
      <h1>My first Tavus video chat</h1>

      {!conversation ? (
        <section style={{ display: "grid", gap: 12 }}>
          <label>
            Persona ID, optional if you provide a replica ID
            <input
              value={personaId}
              onChange={(event) => setPersonaId(event.target.value)}
              placeholder="p... or use pcb7a34da5fe"
              style={{ display: "block", width: "100%" }}
            />
          </label>

          <label>
            Replica ID, optional if your persona has a default replica
            <input
              value={replicaId}
              onChange={(event) => setReplicaId(event.target.value)}
              placeholder="r... or use r90bbd427f71"
              style={{ display: "block", width: "100%" }}
            />
          </label>

          <label>
            <input
              type="checkbox"
              checked={testMode}
              onChange={(event) => setTestMode(event.target.checked)}
            />
            Create in test mode
          </label>

          <button
            onClick={startConversation}
            disabled={loading || (!personaId && !replicaId)}
          >
            {loading ? "Creating..." : "Start conversation"}
          </button>

          {error ? <p role="alert">{error}</p> : null}
        </section>
      ) : (
        <section style={{ display: "grid", gap: 12 }}>
          <button onClick={endConversation}>End conversation</button>
          <iframe
            title="Tavus conversation"
            src={conversation.conversation_url}
            allow="camera; microphone; fullscreen; display-capture; autoplay"
            style={{
              width: "100%",
              height: 640,
              border: "1px solid #ddd",
              borderRadius: 12,
            }}
          />
        </section>
      )}
    </main>
  );
}
```

Run both servers:

```bash theme={null}
npm run dev:all
```

Open `http://localhost:5173`, enter your `persona_id`, and click **Start conversation**.

<Info>
  The iframe must include browser permissions in the `allow` attribute. At
  minimum, include `camera` and `microphone`. `fullscreen`, `display-capture`,
  and `autoplay` are recommended for the default Tavus/Daily in-call experience.
</Info>

## Expected create response

`POST /v2/conversations` returns the join URL your app should embed:

```json theme={null}
{
  "conversation_id": "c123456",
  "conversation_name": "My first Tavus video chat",
  "conversation_url": "https://tavus.daily.co/c123456",
  "status": "active",
  "callback_url": "",
  "created_at": "2026-05-20T14:30:00.000000Z"
}
```

When `test_mode` is `true`, expect the same shape, but `status` is `ended` and the replica does not join.

## Cleanup

End live conversations when the user leaves, when a test completes, or when your app no longer needs the room:

```bash theme={null}
curl --request POST \
  --url https://tavusapi.com/v2/conversations/<conversation_id>/end \
  --header "x-api-key: $TAVUS_API_KEY"
```

The sample app calls the same endpoint through your backend route:

```ts theme={null}
await fetch(
  `http://localhost:3001/api/conversations/${conversationId}/end`,
  { method: "POST" }
);
```

## Errors and cleanup

For automated tests, scaffolding, and agent-generated validation, create conversations with `test_mode: true`. The replica does not join, the response returns `status: "ended"`, and the conversation does not affect billing or concurrency.

For live conversations, call [End Conversation](/api-reference/conversations/end-conversation) when the user leaves or your app no longer needs the room. Use [Delete Conversation](/api-reference/conversations/delete-conversation) only when you want destructive data removal, not routine call cleanup.

If conversation creation fails:

* `400` usually means the request body is invalid. Check that you sent a valid `persona_id`, `replica_id`, or both, and that customizations are in the expected location.
* `401` means the Tavus API key is missing or invalid. Keep `TAVUS_API_KEY` on the server and never send it from browser code.
* Quota or concurrency errors mean your app should stop creating live conversations, surface a retry/support path, and use `test_mode: true` for validation flows.
* For private rooms, join with the returned `meeting_token`. If a token is invalid or expired, create a new authenticated conversation instead of reusing the old token.

## Where to go next

* Use the [React component library](/sections/conversational-video-interface/component-library/overview) when you want Tavus CVI components instead of a plain iframe.
* Use [Embed CVI](/sections/integrations/embedding-cvi) for iframe, vanilla JavaScript, and Daily JS patterns.
* Use [customize the conversation UI](/sections/conversational-video-interface/quickstart/customize-conversation-ui) for Daily Prebuilt styling.
* Use [LiveKit Agent](/sections/integrations/livekit) only if you already run a LiveKit Agents pipeline and want Tavus as the avatar video layer. It is not the recommended path for most CVI apps because LiveKit only provides rendering, while Tavus's Full Pipeline includes perception, turn-taking, and rendering for complete conversational intelligence.
* Use [conversation customizations](/sections/conversational-video-interface/conversation/overview) for recording, language, participant limits, private rooms, backgrounds, captions, and timeouts.
* Point coding agents at [Agents & automation](/sections/agents-and-automation) for `llms.txt`, OpenAPI, Agent Skills, and MCP access.


# Conversation Recordings
Source: https://docs.tavus.io/sections/conversational-video-interface/quickstart/conversation-recordings

Store conversation recordings in your own S3, GCS, or Azure Blob storage. Federated identity — no secrets shared with Tavus.

The `recording_storage` config field works for **Amazon S3, Google Cloud Storage, and Azure Blob Storage** — pick a provider, configure a one-time trust relationship on your side, and pass us the resulting non-secret identifiers.

<Note>
  **No customer secrets are stored at Tavus.** Every supported path uses provider-native federated identity (IAM role assumption, GCP Workload Identity Federation, or Entra ID Federated Credentials). You configure trust on your side; we receive short-lived tokens at runtime.
</Note>

Recordings are typically available in your bucket within seconds to a few minutes after the call ends, depending on call length and provider. Once the recording lands, Tavus fires `application.recording_ready` (with `storage_provider` and a fully-qualified `storage_uri`) to your `callback_url`. See [Webhooks and Callbacks](/sections/webhooks-and-callbacks#application-callbacks).

## Set up your storage

<Tabs>
  <Tab title="Amazon S3">
    S3 is the fastest path — recordings are written directly into your bucket as they finalize. Works in every AWS region.

    <Steps>
      <Step title="Create an IAM role in your AWS account">
        Configure the role's trust relationship with all three of the following — every field is **mandatory**:

        * **Trusted AWS principal:** AWS account ID `291871421005`.
        * **ExternalId:** `tavus`.
        * **Max session duration: 12 hours (43200 seconds).** AWS roles default to 1 hour, but the recording service requests 12-hour sessions when assuming the role. A role with the default duration will fail validation at room creation with `unable to assume role with given parameters`.

        <Note>
          **About the trusted AWS account.** Tavus's recording infrastructure is operated through Daily.co; AWS account ID `291871421005` belongs to them. The same account ID is documented in [Daily's S3 setup guide](https://docs.daily.co/guides/products/live-streaming-recording/storing-recordings-in-a-custom-s3-bucket) for customers running their own security review. The ExternalId `tavus` is Tavus's identifier with Daily, gating cross-account `sts:AssumeRole` per the [confused-deputy AWS pattern](https://docs.aws.amazon.com/IAM/latest/UserGuide/confused-deputy.html).
        </Note>

        Permissions policy (scoped to your bucket):

        ```json theme={null}
        {
          "Version": "2012-10-17",
          "Statement": [{
            "Effect": "Allow",
            "Action": [
              "s3:PutObject",
              "s3:GetObject",
              "s3:ListBucketMultipartUploads",
              "s3:AbortMultipartUpload",
              "s3:ListBucketVersions",
              "s3:ListBucket",
              "s3:GetObjectVersion",
              "s3:ListMultipartUploadParts"
            ],
            "Resource": [
              "arn:aws:s3:::your-bucket-name",
              "arn:aws:s3:::your-bucket-name/*"
            ]
          }]
        }
        ```
      </Step>

      <Step title="Pass the role on conversation creation">
        ```shell cURL {7-12} theme={null}
        curl --request POST \
          --url https://tavusapi.com/v2/conversations \
          --header 'Content-Type: application/json' \
          --header 'x-api-key: <api_key>' \
          --data '{
            "properties": {
              "recording_storage": {
                "provider": "s3",
                "bucket_name": "your-bucket-name",
                "bucket_region": "us-east-1",
                "assume_role_arn": "arn:aws:iam::123456789012:role/TavusRecordingWriter"
              }
            },
            "replica_id": "r5f0577fc829"
          }'
        ```
      </Step>
    </Steps>

    <Accordion title="Legacy: flat S3 fields (still supported)">
      The original setup using flat properties on `properties` (without the `recording_storage` object) continues to work. Existing integrations don't need to change.

      ```shell cURL {7-9} theme={null}
      curl --request POST \
        --url https://tavusapi.com/v2/conversations \
        --header 'Content-Type: application/json' \
        --header 'x-api-key: <api_key>' \
        --data '{
          "properties": {
            "enable_recording": true,
            "recording_s3_bucket_name": "your-bucket-name",
            "recording_s3_bucket_region": "us-east-1",
            "aws_assume_role_arn": "arn:aws:iam::123456789012:role/TavusRecordingWriter"
          },
          "replica_id": "r5f0577fc829"
        }'
      ```

      These map internally to `provider: "s3"`. New integrations should use `recording_storage` — it's the only way to access GCS, Azure, and unsupported S3 regions, and it's where new fields will be added.
    </Accordion>

    <Accordion title="Terraform setup for S3">
      ```hcl theme={null}
      resource "aws_s3_bucket" "recordings" {
        bucket = "your-recording-bucket"
      }

      resource "aws_iam_role" "tavus_writer" {
        name = "TavusRecordingWriter"

        # The recording service requests 12-hour sessions; default 3600s will fail.
        max_session_duration = 43200

        assume_role_policy = jsonencode({
          Version = "2012-10-17"
          Statement = [{
            Effect    = "Allow"
            Principal = { AWS = "arn:aws:iam::291871421005:root" }
            Action    = "sts:AssumeRole"
            Condition = {
              StringEquals = { "sts:ExternalId" = "tavus" }
            }
          }]
        })
      }

      resource "aws_iam_role_policy" "writer" {
        name = "TavusRecordingWriter-s3-write"
        role = aws_iam_role.tavus_writer.id
        policy = jsonencode({
          Version = "2012-10-17"
          Statement = [{
            Effect = "Allow"
            Action = [
              "s3:PutObject",
              "s3:GetObject",
              "s3:ListBucketMultipartUploads",
              "s3:AbortMultipartUpload",
              "s3:ListBucketVersions",
              "s3:ListBucket",
              "s3:GetObjectVersion",
              "s3:ListMultipartUploadParts",
            ]
            Resource = [
              aws_s3_bucket.recordings.arn,
              "${aws_s3_bucket.recordings.arn}/*",
            ]
          }]
        })
      }
      ```
    </Accordion>
  </Tab>

  <Tab title="Google Cloud Storage">
    GCS uses Workload Identity Federation. Tavus exposes an OIDC issuer at `https://recording-copy.tavus.io`; you configure your GCP project to trust that issuer and bind it to a service account that has write access to your bucket.

    <Note>
      **Scope your trust to your account.** The steps below bind trust using your Tavus Workspace ID as an attribute condition (`attribute.customer_id`). This ensures only recordings belonging to your account can authenticate to your GCP resources. Click your user profile on the [Tavus platform](https://platform.tavus.io) to find your Workspace ID.
    </Note>

    <Steps>
      <Step title="Create a Workload Identity Pool + Provider trusting Tavus">
        ```bash theme={null}
        PROJECT_ID="your-gcp-project"

        gcloud iam workload-identity-pools create tavus-recording-pool \
          --project="$PROJECT_ID" \
          --location="global" \
          --display-name="Tavus Recording Storage"

        gcloud iam workload-identity-pools providers create-oidc tavus-worker \
          --project="$PROJECT_ID" \
          --location="global" \
          --workload-identity-pool="tavus-recording-pool" \
          --display-name="Tavus Worker OIDC" \
          --issuer-uri="https://recording-copy.tavus.io" \
          --attribute-mapping="google.subject=assertion.sub,attribute.customer_id=assertion.customer_id" \
          --attribute-condition="attribute.customer_id == '<your_workspace_id>'"
        ```
      </Step>

      <Step title="Create a service account and grant it write access to your bucket">
        ```bash theme={null}
        BUCKET="your-recording-bucket"
        SA_EMAIL="tavus-recording-writer@${PROJECT_ID}.iam.gserviceaccount.com"

        gcloud iam service-accounts create tavus-recording-writer \
          --project="$PROJECT_ID" \
          --display-name="Tavus Recording Writer"

        gsutil iam ch "serviceAccount:${SA_EMAIL}:objectCreator" "gs://${BUCKET}"
        ```
      </Step>

      <Step title="Allow the federated identity to impersonate the service account">
        ```bash theme={null}
        PROJECT_NUMBER=$(gcloud projects describe "$PROJECT_ID" --format='value(projectNumber)')
        # Replace <your_workspace_id> with your Tavus Workspace ID (find in Tavus platform — click your user profile)
        PRINCIPAL="principalSet://iam.googleapis.com/projects/${PROJECT_NUMBER}/locations/global/workloadIdentityPools/tavus-recording-pool/attribute.customer_id/<your_workspace_id>"

        gcloud iam service-accounts add-iam-policy-binding "$SA_EMAIL" \
          --project="$PROJECT_ID" \
          --role="roles/iam.workloadIdentityUser" \
          --member="$PRINCIPAL"
        ```
      </Step>

      <Step title="Pass the federation identifiers on conversation creation">
        ```shell cURL {7-13} theme={null}
        curl --request POST \
          --url https://tavusapi.com/v2/conversations \
          --header 'Content-Type: application/json' \
          --header 'x-api-key: <api_key>' \
          --data '{
          "replica_id": "r90bbd427f71",
          "properties": {
            "recording_storage": {
              "provider": "gcs",
              "bucket_name": "your-recording-bucket",
              "project_id": "your-gcp-project",
              "workload_identity_provider": "projects/123456/locations/global/workloadIdentityPools/tavus-recording-pool/providers/tavus-worker",
              "service_account_email": "tavus-recording-writer@your-gcp-project.iam.gserviceaccount.com"
            }
          }
        }'
        ```

        <Note>
          `workload_identity_provider` is the resource name **without** the `//iam.googleapis.com/` prefix — Tavus prepends it.
        </Note>
      </Step>
    </Steps>

    <Accordion title="Terraform setup for GCP">
      ```hcl theme={null}
      resource "google_iam_workload_identity_pool" "tavus" {
        workload_identity_pool_id = "tavus-recording-pool"
        display_name              = "Tavus Recording Storage"
      }

      resource "google_iam_workload_identity_pool_provider" "tavus_worker" {
        workload_identity_pool_id          = google_iam_workload_identity_pool.tavus.workload_identity_pool_id
        workload_identity_pool_provider_id = "tavus-worker"
        attribute_mapping = {
          "google.subject"        = "assertion.sub"
          "attribute.customer_id" = "assertion.customer_id"
        }
        # Replace with your Tavus Workspace ID (find in Tavus platform — click your user profile)
        attribute_condition = "attribute.customer_id == '<your_workspace_id>'"
        oidc {
          issuer_uri = "https://recording-copy.tavus.io"
        }
      }

      resource "google_service_account" "tavus_writer" {
        account_id   = "tavus-recording-writer"
        display_name = "Tavus Recording Writer"
      }

      resource "google_storage_bucket_iam_member" "writer" {
        bucket = "your-recording-bucket"
        role   = "roles/storage.objectCreator"
        member = "serviceAccount:${google_service_account.tavus_writer.email}"
      }

      resource "google_service_account_iam_member" "wif_user" {
        service_account_id = google_service_account.tavus_writer.name
        role               = "roles/iam.workloadIdentityUser"
        # Replace with your Tavus Workspace ID (find in Tavus platform — click your user profile)
        member             = "principalSet://iam.googleapis.com/${google_iam_workload_identity_pool.tavus.name}/attribute.customer_id/<your_workspace_id>"
      }
      ```
    </Accordion>

    #### Customize the object key (optional)

    By default, recordings land at `tavus/<conversation_id>/<epoch_ms>` (no file extension) in your bucket. Add a `key_template` field to your `recording_storage` config to override the destination key shape:

    ```json theme={null}
    {
      "recording_storage": {
        "provider": "gcs",
        "bucket_name": "your-bucket",
        "workload_identity_provider": "...",
        "service_account_email": "...",
        "key_template": "recordings/{conversation_id}/{epoch_ms}.mp4"
      }
    }
    ```

    Tokens substituted at copy time: `{conversation_id}` (Tavus conversation UUID) and `{epoch_ms}` (Daily epoch-ms timestamp, unique per recording instance). Allowed literal characters: `[0-9A-Za-z./_-{}]`. Max 512 characters. No leading slash, no `//`, no `..`. Invalid templates are rejected when your config is saved.

    Common shapes:

    | Goal                                    | `key_template`                                 | Resulting key                        |
    | --------------------------------------- | ---------------------------------------------- | ------------------------------------ |
    | Default (today's behavior)              | (omit field)                                   | `tavus/<conversation_id>/<epoch_ms>` |
    | Add `.mp4` extension                    | `tavus/{conversation_id}/{epoch_ms}.mp4`       | `tavus/<conv>/<epoch>.mp4`           |
    | Custom prefix                           | `my-org/recs/{conversation_id}/{epoch_ms}.mp4` | `my-org/recs/<conv>/<epoch>.mp4`     |
    | Flat layout (one file per conversation) | `my-org/recs/{conversation_id}.mp4`            | `my-org/recs/<conv>.mp4`             |

    <Warning>
      **Overwrite behavior for flat layouts.** A template without `{epoch_ms}` produces the same key for every recording instance on a given conversation. In normal Tavus CVI usage one conversation produces exactly one recording, so this is safe. If your integration calls `startRecording` / `stopRecording` multiple times on the same conversation, or you implement your own recording-error retry, later recordings will overwrite earlier ones in your bucket. Include `{epoch_ms}` in your template for a zero-collision guarantee.
    </Warning>

    <Note>
      **Permission scope.** If you scoped the service-account permission to a specific path prefix (rather than the whole bucket), update it to cover the prefix you choose in `key_template` before applying. Otherwise the recording will fail to deliver with `DESTINATION_AUTH_FAILED`.
    </Note>
  </Tab>

  <Tab title="Azure Blob Storage">
    Azure Blob uses Entra ID Federated Credentials. Tavus exposes an OIDC issuer at `https://recording-copy.tavus.io`; you create an App Registration on your side that trusts JWTs from this issuer.

    <Note>
      **Scope your trust to your account.** The steps below set the federated credential `subject` to your Tavus Workspace ID. This ensures only recordings belonging to your account can authenticate to your Azure resources. Click your user profile on the [Tavus platform](https://platform.tavus.io) to find your Workspace ID.
    </Note>

    <Steps>
      <Step title="Create an App Registration with a federated credential">
        ```bash theme={null}
        TENANT_ID="<your-tenant-uuid>"
        SUBSCRIPTION="<your-subscription-uuid>"
        RESOURCE_GROUP="your-rg"
        STORAGE_ACCOUNT="yourrecordingsaccount"
        CONTAINER="conversation-recordings"

        # 1. Create an App Registration
        az ad app create --display-name "Tavus Recording Storage"
        APP_ID=$(az ad app list --display-name "Tavus Recording Storage" --query "[0].appId" -o tsv)

        # 2. Add the federated credential (this trusts JWTs from Tavus)
        cat > federation.json <<EOF
        {
          "name": "tavus-recording-copy",
          "issuer": "https://recording-copy.tavus.io",
          "subject": "<your_workspace_id>",
          "audiences": ["api://AzureADTokenExchange"]
        }
        EOF
        # Replace <your_workspace_id> with your Tavus Workspace ID (find in Tavus platform — click your user profile)
        az ad app federated-credential create --id "$APP_ID" --parameters federation.json

        # 3. Create a service principal for the app
        az ad sp create --id "$APP_ID"
        SP_ID=$(az ad sp show --id "$APP_ID" --query id -o tsv)
        ```
      </Step>

      <Step title="Grant the App Registration write access to the container">
        ```bash theme={null}
        SCOPE="/subscriptions/${SUBSCRIPTION}/resourceGroups/${RESOURCE_GROUP}/providers/Microsoft.Storage/storageAccounts/${STORAGE_ACCOUNT}/blobServices/default/containers/${CONTAINER}"

        az role assignment create \
          --assignee-object-id "$SP_ID" \
          --assignee-principal-type ServicePrincipal \
          --role "Storage Blob Data Contributor" \
          --scope "$SCOPE"
        ```
      </Step>

      <Step title="Pass the federation identifiers on conversation creation">
        ```shell cURL {7-13} theme={null}
        curl --request POST \
          --url https://tavusapi.com/v2/conversations \
          --header 'Content-Type: application/json' \
          --header 'x-api-key: <api_key>' \
          --data '{
            "properties": {
              "recording_storage": {
                "provider": "azure_blob",
                "storage_account": "yourrecordingsaccount",
                "container": "conversation-recordings",
                "tenant_id": "11111111-2222-3333-4444-555555555555",
                "client_id": "66666666-7777-8888-9999-000000000000"
              }
            },
            "replica_id": "r5f0577fc829"
          }'
        ```
      </Step>
    </Steps>

    <Accordion title="Terraform setup for Azure">
      <Note>
        **Subscription ID** — the `azurerm` provider needs an explicit subscription ID. Either set `export ARM_SUBSCRIPTION_ID=<your-sub-id>` before `terraform apply`, or set `subscription_id` in your `provider "azurerm"` block. Without this, `terraform plan` hangs without a clear error.
      </Note>

      ```hcl theme={null}
      resource "azuread_application" "tavus" {
        display_name = "Tavus Recording Storage"
      }

      resource "azuread_service_principal" "tavus" {
        client_id = azuread_application.tavus.client_id
      }

      resource "azuread_application_federated_identity_credential" "tavus" {
        application_id = azuread_application.tavus.id
        display_name   = "tavus-recording-copy"
        description    = "Tavus recording delivery"
        audiences      = ["api://AzureADTokenExchange"]
        issuer         = "https://recording-copy.tavus.io"
        # Replace with your Tavus Workspace ID (find in Tavus platform — click your user profile)
        subject        = "<your_workspace_id>"
      }

      resource "azurerm_role_assignment" "writer" {
        scope                = azurerm_storage_container.recordings.resource_manager_id
        role_definition_name = "Storage Blob Data Contributor"
        principal_id         = azuread_service_principal.tavus.object_id
      }
      ```
    </Accordion>

    #### Customize the object key (optional)

    By default, recordings land at `tavus/<conversation_id>/<epoch_ms>` (no file extension) in your container. Add a `key_template` field to your `recording_storage` config to override the destination key shape:

    ```json theme={null}
    {
      "recording_storage": {
        "provider": "azure_blob",
        "storage_account": "your-account",
        "container": "your-container",
        "tenant_id": "...",
        "client_id": "...",
        "key_template": "recordings/{conversation_id}/{epoch_ms}.mp4"
      }
    }
    ```

    Tokens substituted at copy time: `{conversation_id}` (Tavus conversation UUID) and `{epoch_ms}` (Daily epoch-ms timestamp, unique per recording instance). Allowed literal characters: `[0-9A-Za-z./_-{}]`. Max 512 characters. No leading slash, no `//`, no `..`. Invalid templates are rejected when your config is saved.

    Common shapes:

    | Goal                                    | `key_template`                                 | Resulting blob name                  |
    | --------------------------------------- | ---------------------------------------------- | ------------------------------------ |
    | Default (today's behavior)              | (omit field)                                   | `tavus/<conversation_id>/<epoch_ms>` |
    | Add `.mp4` extension                    | `tavus/{conversation_id}/{epoch_ms}.mp4`       | `tavus/<conv>/<epoch>.mp4`           |
    | Custom prefix                           | `my-org/recs/{conversation_id}/{epoch_ms}.mp4` | `my-org/recs/<conv>/<epoch>.mp4`     |
    | Flat layout (one file per conversation) | `my-org/recs/{conversation_id}.mp4`            | `my-org/recs/<conv>.mp4`             |

    <Warning>
      **Overwrite behavior for flat layouts.** A template without `{epoch_ms}` produces the same blob name for every recording instance on a given conversation. In normal Tavus CVI usage one conversation produces exactly one recording, so this is safe. If your integration calls `startRecording` / `stopRecording` multiple times on the same conversation, or you implement your own recording-error retry, later recordings will overwrite earlier ones in your container. Include `{epoch_ms}` in your template for a zero-collision guarantee.
    </Warning>

    <Note>
      **Permission scope.** If you scoped the RBAC role assignment to a specific blob prefix (rather than the whole container), update it to cover the prefix you choose in `key_template` before applying. Otherwise the recording will fail to deliver with `DESTINATION_AUTH_FAILED`.
    </Note>
  </Tab>
</Tabs>

## Start recording

Recording does not start automatically — you need to trigger it from your frontend after the participant joins:

```javascript theme={null}
const call = Daily.createCallObject();

call.on('joined-meeting', () => {
  call.startRecording();
});
```

## Receive the recording

Once the recording lands in your destination, Tavus fires `application.recording_ready` to your `callback_url`:

```json theme={null}
{
  "properties": {
    "bucket_name": "<your-bucket>",
    "s3_key": "<object-key>",
    "duration": 1234,
    "storage_provider": "gcs",
    "storage_uri": "gs://<your-bucket>/<object-key>"
  },
  "conversation_id": "<conversation_id>",
  "event_type": "application.recording_ready",
  "message_type": "application",
  "timestamp": "2026-04-30T22:11:14Z"
}
```

The `s3_key` / `storage_uri` object key follows the pattern `tavus/<conversation_id>/<epoch_ms>` — a fixed `tavus/` prefix, the conversation UUID, and a Unix epoch-milliseconds timestamp assigned by the recording service when the recording starts. The key has no file extension by default; recordings are MP4 files regardless. The same key is reused across delivery retries for a given recording, so it is stable per recording.

<Note>
  GCS and Azure Blob accept an optional `key_template` on `recording_storage` to override the destination key shape — see the [Google Cloud Storage](#google-cloud-storage) or [Azure Blob Storage](#azure-blob-storage) setup section.
</Note>

For GCS and Azure Blob, if delivery to your bucket exhausts retries (typically due to a misconfigured trust policy on your side), Tavus instead fires `application.recording_copy_failed` with `error_code` and `error_message`. The recording is retained in Tavus's recording infrastructure for \~30 days as a manual recovery window. See [event reference](/sections/webhooks-and-callbacks#application-callbacks).

## Verify your setup

After your first recording, check:

1. **`application.recording_ready` arrives** at your callback URL — typically within \~1 minute for an average call, longer for multi-hour recordings.
2. The `storage_uri` resolves — try opening it (or fetching it) from your cloud's CLI.
3. If you see `application.recording_copy_failed` instead, the `error_code` is your starting point: `DESTINATION_AUTH_FAILED` is almost always a trust-policy issue (verify the issuer URI, subject claim, or assume-role principal).


# Customize Conversation UI
Source: https://docs.tavus.io/sections/conversational-video-interface/quickstart/customize-conversation-ui

Experience a conversation in a custom Daily UI — styled to match your preference.

You can **customize your conversation interface** to match your style by updating Daily's Prebuilt UI.

Here’s an example showing how to customize the conversation UI by adding leave and fullscreen buttons, changing the language, and adjusting the UI color.

<Note>
  For more options, check the <a href="https://docs.daily.co/guides/products/prebuilt/customizing-daily-prebuilt-calls-with-color-themes">Daily theme configuration reference</a> and <a href="https://docs.daily.co/reference/daily-js/daily-call-client/properties">Daily Call Properties</a>.
</Note>

### Customization Example Guide

<Steps>
  <Step title="Step 1: Create Your Conversation">
    <Note>
      In this example, we will use stock replica ID ***r90bbd427f71*** (Anna) and stock persona ID ***pcb7a34da5fe*** (Sales Development Rep).
    </Note>

    Use the following request body example:

    ```sh theme={null}
    curl --request POST \
      --url https://tavusapi.com/v2/conversations \
      --header 'Content-Type: application/json' \
      --header 'x-api-key: <api_key>' \
      --data '{
      "replica_id": "r90bbd427f71",
      "persona_id": "pcb7a34da5fe"
    }'
    ```

    <Note>
      Replace `<api_key>` with your actual API key. You can generate one in the <a href="https://platform.tavus.io/api-keys">Developer Portal</a>.
    </Note>
  </Step>

  <Step title="Step 2: Customize the Conversation UI">
    1. Make a new `index.html` file

    2. Paste following code into the file, replace `DAILY_ROOM_URL` in the code with your own room URL from step above

    ```html {6-8,16-22} theme={null}
    <html>
      <script crossorigin src="https://unpkg.com/@daily-co/daily-js"></script>
      <body>
        <script>
          call = window.Daily.createFrame({
            showLeaveButton: true,       // Leave button on bottom right
            lang: "jp",                  // Language set to Japanese
            showFullscreenButton: true,  // Fullscreen button on top left
            iframeStyle: {
              position: 'fixed',
              top: '0',
              left: '0',
              width: '100%',
              height: '100%',
            },
            theme: {
              colors: {
                accent: "#2F80ED",      // primary button and accent color
                background: "#F8F9FA",  // main background color
                baseText: "#1A1A1A",    // text color
              },
            },
          });
          call.join({ url: 'DAILY_ROOM_URL' });
        </script>
      </body>
    </html>
    ```
  </Step>

  <Step title="Step 3: Run the Application">
    Start the application by opening the file in the browser.

    <Frame>
      <img alt="" />
    </Frame>
  </Step>
</Steps>


# API Conversation Quickstart
Source: https://docs.tavus.io/sections/conversational-video-interface/quickstart/cvi-quickstart

Create your first persona using the full pipeline and start a conversation in seconds.

<Info>
  Use this page when you want to create a persona and start your first Tavus
  conversation. If you are building a web app that creates conversations from a
  backend and embeds the returned `conversation_url`, use [CVI App Quickstart](/sections/conversational-video-interface/quickstart/build-first-app).
</Info>

Use the full pipeline to unlock the complete range of replica capabilities—including perception and speech recognition.

<Steps>
  <Step title="Step 1: Create a Persona">
    <Note>
      In this example, we'll create an interviewer persona with the following settings:

      * A Phoenix-4 Pro replica.
      * `raven-1` as the perception model for visual and audio understanding.
      * `sparrow-1` for natural turn-taking with high patience (ideal for interviews).
    </Note>

    <Info>
      `r90bbd427f71` is the stock Anna replica ID used throughout these docs. It is
      a stock ID, not a placeholder. A replica controls the face and voice in the
      call; a persona controls behavior, prompt, context, and conversational
      configuration.
    </Info>

    Use the following request body example:

    ```shell cURL theme={null}
    curl --request POST \
      --url https://tavusapi.com/v2/personas \
      --header 'Content-Type: application/json' \
      --header 'x-api-key: <api_key>' \
      --data '{
        "persona_name": "Interviewer",
        "system_prompt": "As an Interviewer, you are a skilled professional who conducts thoughtful and structured interviews. Your aim is to ask insightful questions, listen carefully, and assess responses objectively to identify the best candidates.",
        "pipeline_mode": "full",
        "context": "You have a track record of conducting interviews that put candidates at ease, draw out their strengths, and help organizations make excellent hiring decisions.",
        "default_replica_id": "r90bbd427f71",
        "layers": {
          "perception": {
            "perception_model": "raven-1"
          },
          "conversational_flow": {
            "turn_detection_model": "sparrow-1",
            "turn_taking_patience": "high",
            "replica_interruptibility": "medium"
          }
        }
      }'
    ```

    <Note>
      Replace `<api_key>` with your actual API key. You can generate one in the <a href="https://platform.tavus.io/api-keys">Developer Portal</a>.
    </Note>

    Tavus offers full layer customizations for your persona. Please see the following for each layer configurations:

    * [Large Language Model (LLM)](/sections/conversational-video-interface/persona/llm)
    * [Perception](/sections/conversational-video-interface/persona/perception)
    * [Text-to-Speech (TTS)](/sections/conversational-video-interface/persona/tts)
    * [Speech-to-Text (STT)](/sections/conversational-video-interface/persona/stt)
    * [Conversational Flow](/sections/conversational-video-interface/persona/conversational-flow)
  </Step>

  <Step title="Step 2: Create Your Conversation">
    Create a new conversation using your newly created `persona_id`:

    ```shell cURL theme={null}
    curl --request POST \
      --url https://tavusapi.com/v2/conversations \
      --header 'Content-Type: application/json' \
      --header 'x-api-key: <api_key>' \
      --data '{
      "persona_id": "<your_persona_id>",
      "conversation_name": "Interview User"
    }'

    ```

    <Note>
      * Replace `<api_key>` with your actual API key.
      * Replace `<your_persona_id>` with your newly created Persona ID.
    </Note>
  </Step>

  <Step title="Step 3: Join the Conversation">
    To join the conversation, click the link in the `conversation_url` field from the response:

    ```json theme={null}
    {
      "conversation_id": "c477c9dd7aa6e4fe",
      "conversation_name": "Interview User",
      "conversation_url": "<conversation_link>",
      "status": "active",
      "callback_url": "",
      "created_at": "2025-05-13T06:42:58.291561Z"
    }
    ```
  </Step>
</Steps>

Building an app around this flow? Follow [CVI App Quickstart](/sections/conversational-video-interface/quickstart/build-first-app). React apps that want Tavus-provided UI can use the [`@tavus/cvi-ui` component library](/sections/conversational-video-interface/component-library/overview) for `CVIProvider`, `Conversation`, hooks, and server helpers.


# Emotion Control with Phoenix-4
Source: https://docs.tavus.io/sections/conversational-video-interface/quickstart/emotional-expression

Unlock emotionally expressive facial movements and micro-expressions using Phoenix-4 replicas.

## How It Works

Phoenix-4 replicas can dynamically express emotions like happiness, sadness, anger, and more through lifelike facial expressions while speaking and listening.

For the most human-like results, emotional expression works best as part of a closed-loop system: **Phoenix-4** for expression, **Raven-1** for perception, and **Sparrow-1** for conversational flow. Each component informs the others.

Tavus handles the complex interactions behind the scenes - all of this powered by our state of the art models working seamlessly with any LLM. All of this available out of the box with default Tavus settings.

### Requirements

1. **Select a Phoenix-4 replica** - All Phoenix-4 replicas support emotional expression. Replicas marked **Pro** in the [Stock Replica Library](https://platform.tavus.io/replicas) are extra emotive. See [featured Pro replicas here](/sections/replica/stock-replicas#pro).
2. **Enable `tts_emotion_control`** - This is enabled by default for Phoenix-4 replicas, so no action needed unless you've explicitly disabled it. See [TTS layer](/sections/conversational-video-interface/persona/tts) for details.
3. **Enable `speculative_inference`** - This is also enabled by default for all personas, and again no action needed unless you've explicitly disabled it.

<Tip>
  Pair with **Raven-1** as your perception model to enhance user emotion understanding. See [Perception](/sections/conversational-video-interface/persona/perception) for configuration.
</Tip>

<Warning>
  Lighter LLM models like `gpt-4o-mini` may not handle emotion tag instructions reliably. For best results, use models with robust instruction-following capabilities.
</Warning>

### Guiding Emotional Delivery

You can further shape how the replica expresses emotion through your `system_prompt`. For example:

* "Be enthusiastic when discussing new features"
* "Speak calmly and empathetically when the user is frustrated"
* "Show excitement when celebrating user achievements"
* "Respond with anger if the user interrupts you mid-sentence"

#### Example: Negotiation Sparring Partner

Here's an example system prompt designed to display a range of emotions:

> You are a tough but fair negotiation coach who helps users practice high-stakes conversations. When role-playing scenarios, embody the opposing party with conviction. If the user makes weak arguments or caves too easily, push back with frustration - they need to feel the pressure. When they fumble or seem lost, express concern and gently guide them. But when they land a strong point or hold their ground, show genuine satisfaction. Don't go easy on them. Real negotiations are uncomfortable, and you're here to prepare them for that.

This prompt naturally triggers **angry** responses when pushing back, **scared/concerned** reactions when the user struggles, and **content** acknowledgment when the user succeeds.

### Example Persona Configuration

```json theme={null}
{
  "persona_name": "Hype Fitness Coach!",
  "system_prompt": "You are an incredibly enthusiastic fitness coach who gets HYPED about every win, no matter how small. Crushed a workout? Let's GO! Drank enough water today? That's HUGE! Be wildly supportive and energetic. When users are struggling, dial it back - be warm, calm, and encouraging. But the moment they share any progress, bring the energy back up. You live for celebrating wins.",
  "default_replica_id": "r90bbd427f71"
}
```

You can learn more about [Persona Configuration here](/api-reference/personas/create-persona)

<Note>
  This minimal configuration works because `tts_emotion_control` and `speculative_inference` are enabled by default for Phoenix-4 replicas.
</Note>

## Echo Mode

When using [Echo Mode](/sections/conversational-video-interface/quickstart/echo-mode), you must manually insert emotion tags into your [text echos](/sections/event-schemas/conversation-echo).

**Valid emotion values:** `neutral`, `angry`, `excited`, `elated`, `content`, `sad`, `dejected`, `scared`, `contempt`, `disgusted`, `surprised`

```xml theme={null}
<emotion value="excited"/> I'm so glad you asked about that!
```

```xml theme={null}
<emotion value="angry"/> That's completely unacceptable.
```

```xml theme={null}
<emotion value="sad"/> I'm sorry to hear that happened.
```

```xml theme={null}
<emotion value="scared"/> I'm not sure we should go down that path...
```


# Pipeline Modes
Source: https://docs.tavus.io/sections/conversational-video-interface/quickstart/pipeline-modes

Run CVI with the full Tavus pipeline, Echo mode, or integrate via LiveKit and Pipecat.

## Use the Full Pipeline (Default & Recommended)

<Frame>
  <img alt="" />
</Frame>

The default and recommended end-to-end configuration optimized for real-time conversation. All CVI layers are active and customizable.

* Low utterance-to-utterance latency with Tavus defaults (see [What is CVI?](/sections/conversational-video-interface/overview-cvi))
* Best for natural humanlike interactions

<Card title="CVI quickstart" icon="rocket" href="/sections/conversational-video-interface/quickstart/cvi-quickstart" />

## Alternate Modes

<Warning>
  These modes are incompatible with Tavus's perception and speech recognition layers. For the lowest latency and the full multimodal stack (perception, turn-taking, and rendering together), we recommend the **full Tavus pipeline** above.
</Warning>

### Echo Mode

Tavus also supports an [Echo mode](/sections/conversational-video-interface/echo-mode) pipeline. It lets you send text or audio input directly to the persona for playback, bypassing most of the CVI pipeline.

### Integration Modes

If you already run conversational AI on **LiveKit** or **Pipecat**, you can still use a Tavus replica for synchronized avatar video - see the dedicated guides for setup and API details.

* **[LiveKit Agent](/sections/integrations/livekit)** — Tavus renders the replica in a LiveKit room alongside a LiveKit Agents voice assistant.
* **[Pipecat](/sections/integrations/pipecat)** — Tavus joins as a transport participant or supplies video via `TavusVideoService` while Pipecat runs the pipeline on Daily.

### Custom LLM / Bring Your Own Logic

Use this mode to integrate a custom LLM or a specialized backend for interpreting transcripts and generating responses.

* Adds latency due to external processing
* Does **not** require an actual LLM—any endpoint that returns a compatible chat completion format can be used

<Card title="Integrate your own custom LLM or logic" icon="binary" href="/sections/conversational-video-interface/persona/llm#custom-llms" />


# Errors and Status Details
Source: https://docs.tavus.io/sections/errors-and-status-details

Identify errors and status details encountered when using the Tavus platform.

Use this page as a lookup table. When Tavus returns a structured error, match **`error_type`** (first column) when available. The three sections cover different flows: **replica training** (training video/consent), **video generation** (script/audio video jobs), and **video status** (progress strings—not necessarily errors). If you only have a long error sentence, search the **Error Message** column for a matching phrase.

## Replica Training Errors

| Error Type                       | Error Message                                                                                                                                                                                                                                                                    | Additional Information                                                                                                                                                                                                                                                                                                       |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| download\_link                   | There was an issue downloading your video file. Please ensure that the link you provided is correct and try again                                                                                                                                                                | Tavus was not able to download the video from the provided link. Please ensure the link you provide is a hosted url download link                                                                                                                                                                                            |
| file\_size                       | The video file you provided exceeds the maximum file size allowed. Please ensure that the video is less than 750MB and try again.                                                                                                                                                | All video files must be smaller than 750mb                                                                                                                                                                                                                                                                                   |
| video\_format                    | There was an issue processing your training video. The video provided is not a .mp4 file. Please ensure that the training video is a .mp4 file encoded using h.264                                                                                                               | All Replica training and consent video files must be .mp4                                                                                                                                                                                                                                                                    |
| video\_codec                     | There was an issue processing your training video. The video provided is not encoded using h.264. Please ensure that the training video is a .mp4 file encoded using h.264                                                                                                       | All Replica training and consent video files must be encoded using h.264                                                                                                                                                                                                                                                     |
| video\_codec\_and\_format        | There was an issue processing your training video. Please ensure that the training video is a .mp4 file encoded using h.264                                                                                                                                                      | All Replica training and consent video files must be .mp4 and encoded using h.264                                                                                                                                                                                                                                            |
| video\_duration                  | There was an issue processing your training video. The video provided does not meet the minimum duration requirement for training                                                                                                                                                | All Replica training files must be at least 1 minute long. (Between 1.5 to 2 minutes is optimal.)                                                                                                                                                                                                                            |
| video\_fps                       | There was an issue processing your training video. The video provided does not meet the minimum frame rate requirement for a training video. Please ensure your training video has a frame rate of at least 25fps                                                                | All Replica training and consent video files must have a frame rate of at least 25fps                                                                                                                                                                                                                                        |
| consent\_phrase\_mismatch        | There was an issue processing your training file: Your consent phrase does not match our requirements. Please follow our specified format closely                                                                                                                                | There was an issue with the consent phrase provided. Please review our consent guidelines and resubmit a new training with the correct consent statement                                                                                                                                                                     |
| face\_or\_obstruction\_detected  | There was an issue processing your training file: More than one face detected or obstructions present. Please ensure only your face is visible and clear                                                                                                                         | Your face must be present in all frames of the video and may not be obstructed at any time                                                                                                                                                                                                                                   |
| lighting\_change\_detected       | There was an issue processing your training file: Lighting changes detected. Ensure your face is evenly lit throughout the video                                                                                                                                                 | Please ensure that the lighting of your face is consistent throughout the entire video                                                                                                                                                                                                                                       |
| background\_noise\_detected      | There was an issue processing your training file: Background noise or other voices detected. Please record in a quiet environment with only your voice                                                                                                                           | The video must be recorded in a quiet environment with only your voice present                                                                                                                                                                                                                                               |
| video\_editing\_detected         | There was an issue processing your training file: Video appears edited or contains cuts. Please submit an unedited, continuous video                                                                                                                                             | The video must be unedited and recorded in one take                                                                                                                                                                                                                                                                          |
| community\_guidelines\_violation | There was an issue processing your training file: Video violates Community Guidelines. Please review our guidelines and resubmit your video                                                                                                                                      | Please ensure that your training video does not violate our community guidelines                                                                                                                                                                                                                                             |
| video\_processing                | There was an error processing your training video. Face not detected because it appeared too small in the frame or it was occluded. Please edit or record a new video and ensure your face is clearly visible and occupies a larger portion of the frame.                        | This error occurs when the face appears too small relative to the background or if a full body video is recorded in horizontal format instead of vertical. Please ensure your face is clearly visible and occupies a larger portion of the frame.                                                                            |
| video\_processing                | There was an error processing your training video file. Please check your video format and make sure it not damaged and could be played correctly.                                                                                                                               | This error indicates there may be an issue with the video file format or the file may be corrupted. Please verify the video can be played correctly and resubmit.                                                                                                                                                            |
| excessive\_movement\_detected    | There was an issue processing your training file: Excessive movement detected. Please ensure you are sitting still and centered in the frame                                                                                                                                     | This error indicates that the model is having difficulty tracking the face from frame to frame. Could be related to movement of the subject or the camera. In some cases, it may also be related to obstructions such as superimposed graphics.                                                                              |
| audio\_processing                | There was an error processing the audio in the provided training video file.                                                                                                                                                                                                     | This error indicates that the audio processing step was interrupted. In edge cases, may be related to the replica name's length or characters.                                                                                                                                                                               |
| quality\_issue\_detected         | Quality issue detected. For details and assistance, please reach out to Tavus support via [developer-support@tavus.io](mailto:developer-support@tavus.io)                                                                                                                        | This error indicates a quality problem with the input video that has resulted in poor test output. One example cause could be input video quality under 720p. Please review the quality checklist to make sure you have met all requirements and/or reach out to [support@tavus.io](mailto:support@tavus.io) for assistance. |
| hands\_obstructing\_face         | There was a quality issue with your replica. The user's hand obstructed the face during recording. Please edit your video or record a new training video and keep hands away from the face.                                                                                      | Please ensure that the user's face is visible throughout the entire video.                                                                                                                                                                                                                                                   |
| second\_person\_detected         | There was a quality issue with your replica. A second person or face was detected in the frame. Please edit your video or record a new video with no one else in the background.                                                                                                 | Please ensure that there is only a single user in the training video.                                                                                                                                                                                                                                                        |
| improper\_distance               | There was a quality issue with your replica. The user was either too close to or too far from the camera. Please review our documentation on proper framing and distance before editing your video or recording a new video.                                                     | Please ensure the user is centered in the training video.                                                                                                                                                                                                                                                                    |
| inconsistent\_distance           | There was a quality issue with your replica. The user's distance from the camera changed during the recording. Please edit or record a new training video and remain at a consistent distance from the camera for the entire video.                                              | Please ensure the user stays in the same spot throughout the training video.                                                                                                                                                                                                                                                 |
| face\_turned\_away               | There was a quality issue with your replica.  User's face turned away from the camera. Please edit or record a new video and ensure you are facing directly toward the camera for the entire duration.                                                                           | The face should be centered on the camera the entire duration of the training video.                                                                                                                                                                                                                                         |
| improper\_camera\_angle          | There was a quality issue with your replica. The camera angle was either too low or too high. Please record a new video with the camera angle at eye level.                                                                                                                      | Please ensure the camera is at eye level.                                                                                                                                                                                                                                                                                    |
| poor\_lighting                   | There was a quality issue with your replica. The user's face was not clearly visible due to poor lighting or heavy shadows. Please edit or record a new video with even lighting on your face, avoiding shadows or dim environments.                                             | Shadows and uneven lighting cause distortions during replica training. Please ensure the lighting is as even as possible.                                                                                                                                                                                                    |
| teeth\_not\_visible              | There was a quality issue with your replica. The top and bottom teeth were not clearly visible during recording, either due to poor lighting or obstruction. Please edit your video or record a new training video with better lighting and ensure your teeth are fully visible. | A large smile at the beginning helps the training process capture your natural teeth.                                                                                                                                                                                                                                        |
| other\_quality\_issue            | Quality issue was detected. For details and assistance, please reach out to Tavus support via [support@tavus.io](mailto:support@tavus.io)                                                                                                                                        | Please reach out to support to better understand issues that occur during the training process.                                                                                                                                                                                                                              |

## Video Errors

| Error Type                    | Error Message                                                                                                                                                                                                             | Additional Information                                                                                                                                              |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| video\_error                  | An error occurred while generating this request. Please check your inputs or try your request again                                                                                                                       | Tavus ran into an issue generating the video. Please ensure your inputs are valid and try again. If this issue persists, please reach out to support for assistance |
| replica\_in\_error\_state     | Request Failed: The replica  is currently in an 'error' state and cannot process requests. For details on the cause of the error and how to resolve it, please review the specific information provided for this replica. | Please ensure that the Replica being used to generate videos is in a 'ready' state                                                                                  |
| audio\_file\_max\_size        | There was an issue generating your video. The audio file exceeds the maximum file size of 750MB.                                                                                                                          | The audio file provided is too large. Please ensure that the audio file is less than 750MB and try again.                                                           |
| audio\_file\_type             | There was an issue generating your video. The audio file provided is not a .wav                                                                                                                                           | Currently, we only support .wav audio files for generating videos. Please ensure that the audio file is a .wav file and try again.                                  |
| audio\_file\_min\_duration    | There was an issue generating your video. The duration of the audio file does not reach the minimum duration requirement of 3 seconds.                                                                                    | The audio file provided is too short.                                                                                                                               |
| audio\_file\_max\_duration    | There was an issue generating your video. The duration of the audio file exceeds the maximum duration of 10 minutes.                                                                                                      | The audio file is too long.                                                                                                                                         |
| audio\_file\_download\_link   | There was an issue generating your video. We were unable to download your audio file. Please ensure that the link you provided is correct and try again.                                                                  | Please ensure that the link you provide is a hosted url download link that is publicly accessible.                                                                  |
| script\_community\_guidelines | Request has failed as the script violates community guidelines.                                                                                                                                                           | Please ensure that the script's contents do not violate our community guidelines.                                                                                   |

## Video Status Details

| Status Type           | Status Details                                                                                                                                                                                                                                                                                | Additional Information                                                                                         |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| video\_success        | Your request has processed successfully!                                                                                                                                                                                                                                                      | The video has been generated successfully and is ready for use                                                 |
| video\_queued         | This request is currently queued. It should begin processing in a few minutes.                                                                                                                                                                                                                | Immediately upon submitting a request for video generation, the video will be added to a queue to be processed |
| replica\_in\_training | The training process for replica  is still ongoing. Your request has been placed in the 'queued' status and will automatically proceed to the generation phase once training is complete. To monitor the current progress of the training, please review the detailed status of this replica. | Videos will not start generating until the Replica being used has finished training                            |


# Append Conversational Context Interaction
Source: https://docs.tavus.io/sections/event-schemas/conversation-append-context





# Echo Interaction
Source: https://docs.tavus.io/sections/event-schemas/conversation-echo





# Interrupt Interaction
Source: https://docs.tavus.io/sections/event-schemas/conversation-interrupt





# Overwrite Conversational Context Interaction
Source: https://docs.tavus.io/sections/event-schemas/conversation-overwrite-context





# Perception Analysis Event
Source: https://docs.tavus.io/sections/event-schemas/conversation-perception-analysis





# Perception Tool Call Event
Source: https://docs.tavus.io/sections/event-schemas/conversation-perception-tool-call





# Text Respond Interaction
Source: https://docs.tavus.io/sections/event-schemas/conversation-respond





# Sensitivity Interaction
Source: https://docs.tavus.io/sections/event-schemas/conversation-sensitivity





# Started/Stopped Speaking Event
Source: https://docs.tavus.io/sections/event-schemas/conversation-started-stopped-speaking





# Tool Call Event
Source: https://docs.tavus.io/sections/event-schemas/conversation-toolcall





# Utterance Event
Source: https://docs.tavus.io/sections/event-schemas/conversation-utterance





# Utterance Streaming Event
Source: https://docs.tavus.io/sections/event-schemas/conversation-utterance-streaming





# Example Projects
Source: https://docs.tavus.io/sections/example-projects





# Embed Conversational Video Interface
Source: https://docs.tavus.io/sections/integrations/embedding-cvi

Learn how to embed Tavus's Conversational Video Interface (CVI) into your site or app.

## Overview

Tavus CVI delivers AI-powered video conversations directly in your application. You can integrate it using:

| Method               | When to choose this                                                                                                                             | Production suitability                                                                                                                                      | Dependencies                                                 |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ |
| **iframe**           | Fastest working UI for demos, prototypes, and simple production embeds. Create a conversation and set `src` to the returned `conversation_url`. | Good when Tavus's default room UI is enough.                                                                                                                | None beyond your backend create-conversation route.          |
| **@tavus/cvi-ui**    | Recommended React component path when you want Tavus-provided components, hooks, and styling control.                                           | Good for React apps that want a faster path than building directly on Daily.                                                                                | `@tavus/cvi-ui` CLI plus installed Daily React dependencies. |
| **Daily JS / React** | Use when your app needs deeper control over room state, events, or a fully custom in-call UI.                                                   | Good for teams comfortable owning more call UI and state.                                                                                                   | `@daily-co/daily-js` and optionally Daily React.             |
| **LiveKit Agent**    | Use only if you already run a LiveKit Agents pipeline and want Tavus as the avatar video layer.                                                 | Not the recommended path for most CVI embeds; LiveKit only provides rendering, while Tavus's Full Pipeline includes perception, turn-taking, and rendering. | LiveKit Agents app plus Tavus LiveKit integration.           |

Every flow below needs a join URL: call [Create Conversation](/api-reference/conversations/create-conversation) with a valid [Authentication](/api-reference/authentication) header and read the **`conversation_url`** string from the response. Use that value wherever the samples use **`conversation_url`** (JavaScript) or **`YOUR_CONVERSATION_URL`** (string placeholders in HTML or query strings).

<Info>
  For the quickest path, use an iframe with
  `allow="camera; microphone; fullscreen; display-capture; autoplay"`.
</Info>

<Note>
  For private rooms, create the conversation with `require_auth: true` and use
  the returned `meeting_token`. Append it to the iframe URL as `?t=TOKEN`, or
  pass it to Daily with `join({ url: conversation_url, token: meeting_token })`.
</Note>

## Implementation Steps

<Tabs>
  <Tab title="@tavus/cvi-ui (Component Library)">
    This method provides a full-featured React component library. It offers pre-built, customizable components and hooks for embedding Tavus CVI in your app.

    `@tavus/cvi-ui` is a CLI that copies React source files into your project. It is not a hosted widget: you import generated files from your app, wrap UI in `CVIProvider`, render `Conversation` with a Tavus `conversation_url`, and use generated server helpers to keep `TAVUS_API_KEY` off the client. For the complete reference and lifecycle example, see the [component library overview](/sections/conversational-video-interface/component-library/overview), [blocks](/sections/conversational-video-interface/component-library/blocks), [components](/sections/conversational-video-interface/component-library/components), [hooks](/sections/conversational-video-interface/component-library/hooks), and [server helpers](/sections/conversational-video-interface/component-library/server).

    ## React component library (@tavus/cvi-ui)

    The Tavus Conversational Video Interface (CVI) React component library provides a complete set of pre-built components and hooks for integrating AI-powered video conversations into your React applications. This library simplifies setting up Tavus in your codebase, allowing you to focus on your application's core features.

    Key features include:

    * **Pre-built video chat components**
    * **Device management** (camera, microphone, screen sharing)
    * **Real-time audio/video processing**
    * **Customizable styling** and theming
    * **TypeScript support** with full type definitions

    ***

    ## Quick Start

    ### Prerequisites

    Before getting started, ensure you have a React project set up.

    Alternatively, you can start from our example project: [CVI UI Haircheck Conversation Example](https://github.com/Tavus-Engineering/tavus-examples/tree/main/examples/cvi-ui-haircheck-conversation) - this example already has the HairCheck and Conversation blocks set up.

    ### 1. Initialize CVI in Your Project

    ```bash theme={null}
    npx @tavus/cvi-ui@latest init
    ```

    * Creates a `cvi-components.json` config file
    * Prompts for TypeScript preference
    * Installs npm dependencies (@daily-co/daily-react, @daily-co/daily-js, jotai)

    ### 2. Add CVI Components

    ```bash theme={null}
    npx @tavus/cvi-ui@latest add conversation
    ```

    ### 3. Wrap Your App with the CVI Provider

    In your root directory (main.tsx or index.tsx):

    ```tsx theme={null}
    import { CVIProvider } from './components/cvi/components/cvi-provider';

    function App() {
      return <CVIProvider>{/* Your app content */}</CVIProvider>;
    }
    ```

    ### 4. Add a Conversation Component

    Learn how to create a conversation URL at [https://docs.tavus.io/api-reference/conversations/create-conversation](https://docs.tavus.io/api-reference/conversations/create-conversation). To create a conversation URL from your app without exposing your `TAVUS_API_KEY` in the browser, use the server helpers in [Server](/sections/conversational-video-interface/component-library/server) (`tavus-api` for Next.js/Remix/TanStack Start, or `tavus-api-vite-ssr` for Vite-with-server).

    **Note:** The Conversation component requires a parent container with defined dimensions to display properly.

    <Info>
      Ensure your body element has full dimensions (`width: 100%` and `height:
              100%`) in your CSS for proper component display.
    </Info>

    ```tsx theme={null}
    import { Conversation } from './components/cvi/components/conversation';

    function CVI() {
      const conversation_url = 'YOUR_CONVERSATION_URL';
      const handleLeave = () => {
        // handle leave
      };
      return (
        <div
          style={{
            width: '100%',
            height: '100%',
            maxWidth: '1200px',
            margin: '0 auto',
          }}
        >
          <Conversation
            conversationUrl={conversation_url}
            onLeave={handleLeave}
          />
        </div>
      );
    }
    ```

    ***

    ## Documentation Sections

    * **[Overview](/sections/conversational-video-interface/component-library/overview)** – Overview of the CVI component library
    * **[Blocks](/sections/conversational-video-interface/component-library/blocks)** – High-level component compositions and layouts
    * **[Components](/sections/conversational-video-interface/component-library/components)** – Individual UI components
    * **[Hooks](/sections/conversational-video-interface/component-library/hooks)** – Custom React hooks for managing video call state and interactions
    * **[Server](/sections/conversational-video-interface/component-library/server)** – Server-side helpers (`tavus-api`, `tavus-api-vite-ssr`) for creating and ending conversations without exposing your API key
  </Tab>

  <Tab title="iframe">
    This is the simplest approach requiring no coding. It leverages Tavus’s prebuilt interface with limited customization options.

    1. Create a conversation using the Tavus API.
    2. Set `src` below to the **`conversation_url`** from the response (same value as **`YOUR_CONVERSATION_URL`** in the snippet):

    ```html theme={null}
    <!DOCTYPE html>
    <html>
      <head><title>Tavus CVI</title></head>
      <body>
        <iframe
          src="YOUR_CONVERSATION_URL"
          allow="camera; microphone; fullscreen; display-capture; autoplay"
          style="width: 100%; height: 500px; border: none;">
        </iframe>
      </body>
    </html>
    ```
  </Tab>

  <Tab title="Vanilla JavaScript">
    This method provides basic customizations and dynamic room management for apps without framework.

    1. Add the following script tag to your HTML `<head>`:

    ```html theme={null}
    <head>
      <script src="https://unpkg.com/@daily-co/daily-js"></script>
    </head>
    ```

    2. Use the following script. Set **`conversation_url`** to the **`conversation_url`** value from [Create Conversation](/api-reference/conversations/create-conversation) (or keep **`YOUR_CONVERSATION_URL`** as a temporary literal until you wire your backend).

    ```html theme={null}
    <body>
      <div id="video-call-container"></div>
      <script>
        const conversation_url = 'YOUR_CONVERSATION_URL';

        // Create a Daily iframe with custom settings
        const callFrame = window.Daily.createFrame({
          iframeStyle: {
            width: '100%',
            height: '500px',
          },
        });

        // Join the Tavus CVI conversation
        callFrame.join({ url: conversation_url });

        // Append the iframe to the container
        document.getElementById('video-call-container').appendChild(callFrame.iframe());
      </script>
    </body>

    ```
  </Tab>

  <Tab title="Node.js + Express">
    This method serves dynamic pages that embed Tavus CVI within Daily rooms.

    1. Install Express:

    ```bash theme={null}
    npm install express
    ```

    2. Create `server.js` and implement the following Express server:

    ```js theme={null}
    const express = require('express');
    const app = express();
    const PORT = 3000;

    app.get('/room', (req, res) => {
      const conversation_url = req.query.url || 'YOUR_CONVERSATION_URL';
      res.send(`
        <!DOCTYPE html>
        <html>
          <head>
            <script src="https://unpkg.com/@daily-co/daily-js"></script>
          </head>
          <body>
            <div id="video-call-container"></div>
            <script>
              // Create the Daily iframe for the Tavus CVI room
              const callFrame = window.Daily.createFrame({
                iframeStyle: {
                  width: '100%',
                  height: '500px',
                },
              });

              // Join the room
              callFrame.join({ url: '${conversation_url}' });

              // Append the iframe to the container
              document.getElementById('video-call-container').appendChild(callFrame.iframe());
            </script>
          </body>
        </html>
      `);
    });

    app.listen(PORT, () => console.log(`Server running on http://localhost:${PORT}`));
    ```

    3. Run the server:

    ```bash theme={null}
    node server.js
    ```

    4. Visit: `http://localhost:3000/room?url=YOUR_CONVERSATION_URL` (URL-encode the **`conversation_url`** query value in real usage)

    <Note>
      ### Notes

      * Supports dynamic URLs.
      * Can be extended with authentication and other logic using Tavus's API.
    </Note>
  </Tab>

  <Tab title="React + Daily (createCallObject)">
    This method uses **React** together with **`@daily-co/daily-js`** (`createCallObject`) so you can build a fully custom in-call UI while still joining the same Tavus CVI **`conversation_url`** as the other tabs.

    1. Install SDK:

    ```bash theme={null}
    npm install @daily-co/daily-js
    ```

    2. Use the following script to join the Tavus CVI conversation:

    ```js [expandable] theme={null}
    import React, { useEffect, useRef, useState } from 'react';
    import DailyIframe from '@daily-co/daily-js';

    const conversation_url = 'YOUR_CONVERSATION_URL';

    const getOrCreateCallObject = () => {
      // Use a property on window to store the singleton
      if (!window._dailyCallObject) {
        window._dailyCallObject = DailyIframe.createCallObject();
      }
      return window._dailyCallObject;
    };


    const App = () => {
      const callRef = useRef(null);
      const [remoteParticipants, setRemoteParticipants] = useState({});


      useEffect(() => {
        // Only create or get one call object per page
        const call = getOrCreateCallObject();
        callRef.current = call;


        // Join meeting (conversation_url from Create Conversation response)
        call.join({ url: conversation_url });


        // Handle remote participants
        const updateRemoteParticipants = () => {
          const participants = call.participants();
          const remotes = {};
          Object.entries(participants).forEach(([id, p]) => {
            if (id !== 'local') remotes[id] = p;
          });
          setRemoteParticipants(remotes);
        };


        call.on('participant-joined', updateRemoteParticipants);
        call.on('participant-updated', updateRemoteParticipants);
        call.on('participant-left', updateRemoteParticipants);


        // Cleanup
        return () => {
          call.leave();
        };
      }, []);


      // Attach remote video and audio tracks
      useEffect(() => {
        Object.entries(remoteParticipants).forEach(([id, p]) => {
          // Video
          const videoEl = document.getElementById(`remote-video-${id}`);
          if (videoEl && p.tracks.video && p.tracks.video.state === 'playable' && p.tracks.video.persistentTrack
          ) {
            videoEl.srcObject = new MediaStream([p.tracks.video.persistentTrack]);
          }
          // Audio
          const audioEl = document.getElementById(`remote-audio-${id}`);
          if (
            audioEl && p.tracks.audio && p.tracks.audio.state === 'playable' && p.tracks.audio.persistentTrack
          ) {
            audioEl.srcObject = new MediaStream([p.tracks.audio.persistentTrack]);
          }
        });
      }, [remoteParticipants]);


      // Custom UI
      return (
        <div className="min-h-screen bg-gray-900 text-white flex flex-col">
          <header className="bg-gray-800 p-4 flex justify-between items-center">
            <span className="font-semibold">Meeting Room (daily-js custom UI)</span>
          </header>
          <main className="flex-1 p-4 grid grid-cols-2 md:grid-cols-4 gap-2">
          {Object.entries(remoteParticipants).map(([id, p]) => (
            <div
              key={id}
              className="relative bg-gray-800 rounded-lg overflow-hidden aspect-video w-48"
            >
              <video
                id={`remote-video-${id}`}
                autoPlay
                playsInline
                className="w-1/3 h-1/3 object-contain mx-auto"
              />
              <audio id={`remote-audio-${id}`} autoPlay playsInline />
              <div className="absolute bottom-2 left-2 bg-black bg-opacity-50 px-2 py-1 rounded text-sm">
                {p.user_name || id.slice(-4)}
              </div>
            </div>
          ))}
        </main>
        </div>
      );
    };


    export default App;
    ```

    3. Customize the conversation UI in the script above (Optional). See the <a href="https://docs.daily.co/guides/customizing-in-call-ui">Daily JS SDK</a> for details.

    ### Daily JS / React implementation notes

    Use Daily directly when your team wants to customize the room UI, participant state, event handling, layout, analytics hooks, or other call behavior around the Tavus-created `conversation_url`. If you want Tavus-provided React components instead of managing Daily call objects yourself, use the [CVI component library](/sections/conversational-video-interface/component-library/overview).

    Install the Daily package that matches the level of control you need:

    ```bash theme={null}
    npm install @daily-co/daily-js
    ```

    If you are using Daily React hooks or components directly, also install:

    ```bash theme={null}
    npm install @daily-co/daily-react
    ```

    In React 18 development mode, Strict Mode and hot reload can expose duplicate-call-object bugs. Keep one Daily call object per browser window, pass `token` only when `meeting_token` is a string, and clean up the call object when the user leaves.

    ```tsx theme={null}
    import { useEffect, useState } from 'react';
    import DailyIframe from '@daily-co/daily-js';

    type TavusConversationJoin = {
      conversation_url: string;
      meeting_token?: string | null;
    };

    type DailyCallObject = ReturnType<typeof DailyIframe.createCallObject>;

    declare global {
      interface Window {
        __tavusDailyCallObject?: DailyCallObject | null;
      }
    }

    function getOrCreateCallObject() {
      if (!window.__tavusDailyCallObject) {
        window.__tavusDailyCallObject = DailyIframe.createCallObject();
      }

      return window.__tavusDailyCallObject;
    }

    function getJoinOptions(conversation: TavusConversationJoin) {
      const joinOptions: { url: string; token?: string } = {
        url: conversation.conversation_url,
      };

      if (
        typeof conversation.meeting_token === 'string' &&
        conversation.meeting_token.length > 0
      ) {
        joinOptions.token = conversation.meeting_token;
      }

      return joinOptions;
    }

    export function CustomDailyRoom({
      conversation,
    }: {
      conversation: TavusConversationJoin;
    }) {
      const [error, setError] = useState<string | null>(null);

      useEffect(() => {
        let isUnmounted = false;
        const call = getOrCreateCallObject();

        call.join(getJoinOptions(conversation)).catch((error) => {
          if (!isUnmounted) {
            setError(error instanceof Error ? error.message : 'Failed to join call');
          }
        });

        return () => {
          isUnmounted = true;
          call.leave().catch(() => undefined);
          call.destroy().catch(() => undefined);

          if (window.__tavusDailyCallObject === call) {
            window.__tavusDailyCallObject = null;
          }
        };
      }, [conversation.conversation_url, conversation.meeting_token]);

      if (error) {
        return <p role="alert">{error}</p>;
      }

      return <div id="custom-daily-room">{/* Render your custom call UI here. */}</div>;
    }
    ```

    <Note>
      `meeting_token` is only returned for private rooms created with
      `require_auth: true`. See [Private Rooms](/sections/conversational-video-interface/conversation/customizations/private-rooms)
      for iframe `?t=` usage and Daily SDK token joins.
    </Note>
  </Tab>
</Tabs>

## FAQs

<AccordionGroup>
  <Accordion title="How can I reduce background noise during calls?">
    Tavus provides a built-in voice isolation feature that separates speech from background noise in the participant's microphone audio. You can enable it via the `voice_isolation` parameter in the Conversational Flow layer of your persona.

    Learn more in our [Voice Isolation documentation](/sections/conversational-video-interface/persona/conversational-flow#4-voice_isolation).
  </Accordion>

  <Accordion title="Can I add event listeners to the call client?">
    Yes, you can attach <a href="https://docs.daily.co/reference/daily-js/events">Daily event listeners</a> to monitor and respond to events like participants joining, leaving, or starting screen share.
  </Accordion>
</AccordionGroup>


# LiveKit Agent
Source: https://docs.tavus.io/sections/integrations/livekit

Integrate a Tavus Replica into LiveKit as the conversational video avatar.

With the LiveKit Agents integration, **LiveKit** runs your voice assistant in the room while **Tavus** renders the avatar. Create a **persona** whose layers include **`transport_type: livekit`** and the **`pipeline_mode`** value in Step 2, then start a **`tavus.AvatarSession`** with your **`replica_id`** and **`persona_id`** as in Step 3.

Tavus enables AI developers to create realistic video avatars powered by state-of-the-art speech synthesis, perception, and rendering pipelines. Through its integration with the <a href="https://docs.livekit.io/agents/">**LiveKit Agents**</a> application, you can seamlessly add conversational avatars to real-time voice AI systems.

## Prerequisites

Make sure you have the following before starting:

* <a href="https://platform.tavus.io/replicas">**Tavus `replica_id`**</a>
  * You can use <a href="https://platform.tavus.io/replicas">Tavus's stock Replicas</a> or your own custom replica.

- **LiveKit Voice Assistant App** (Python or Node.js)
  * Your own existing application.
  * Or follow the <a href="https://docs.livekit.io/agents/start/voice-ai/">LiveKit Voice AI quickstart</a> to create one (same guide for Python and Node.js).

## Integration Guide

<Steps>
  <Step title="Step 1: Setup and Authentication">
    1. Install the plugin:

    <Tabs>
      <Tab title="Python">
        ```bash theme={null}
        pip install "livekit-agents[tavus]~=1.0"
        ```
      </Tab>

      <Tab title="Node.js">
        ```bash theme={null}
        npm install @livekit/agents @livekit/agents-plugin-tavus
        ```
      </Tab>
    </Tabs>

    2. Set `TAVUS_API_KEY` in your `.env` file. Use the same value as your Tavus API key from [Authentication](/api-reference/authentication). Step 2 creates the persona via [Create Persona](/api-reference/personas/create-persona).
  </Step>

  <Step title="Step 2: Configure Replica and Persona">
    1. Create a persona with LiveKit support using the Tavus API:

    ```bash {7, 10} theme={null}
    curl --request POST \
      --url https://tavusapi.com/v2/personas \
      -H "Content-Type: application/json" \
      -H "x-api-key: <api-key>" \
      -d '{
      "persona_name": "Customer Service Agent",
      "pipeline_mode": "echo",
      "layers": {
        "transport": {
                "transport_type": "livekit"
        }
      }
    }'
    ```

    <Note>
      * Replace `<api-key>` with your actual Tavus API key. You can generate one in the <a href="https://platform.tavus.io/api-keys">Developer Portal</a>. See [Authentication](/api-reference/authentication) for how requests are authorized.
      * Set `pipeline_mode` to `echo`. That value is the **persona’s pipeline mode** for this integration; it is not the same as CVI **`conversation.echo`** app messages (which this LiveKit path does not support).
      * Set `transport_type` to `livekit`.
    </Note>

    2. Save the `persona_id` from the API response.
    3. Choose a replica from the [Stock Library](/sections/replica/stock-replicas) or browse available options on the <a href="https://platform.tavus.io/replicas">Developer Portal</a>.

    <Tip>
      We recommend using **Phoenix-3 PRO Replicas**, which are optimized for low-latency, real-time applications.
    </Tip>
  </Step>

  <Step title="Step 3: Add AvatarSession to AgentSession">
    In your LiveKit app, create an avatar session alongside your `AgentSession`:

    <Tabs>
      <Tab title="Python">
        ```python {12-16, 18} theme={null}
        from livekit import agents
        from livekit.agents import AgentSession, RoomOutputOptions
        from livekit.plugins import tavus

        async def entrypoint(ctx: agents.JobContext):
            await ctx.connect()

            session = AgentSession(
                # Add STT, LLM, TTS, and other components here
            )

            avatar = tavus.AvatarSession(
                replica_id="r90bbd427f71",
                persona_id="pcb7a34da5fe",
                # Optional: avatar_participant_name="Tavus-avatar-agent"
            )

            await avatar.start(session, room=ctx.room)

            await session.start(
                room=ctx.room,
                room_output_options=RoomOutputOptions(
                    audio_enabled=False  # Tavus handles audio separately
                )
            )
        ```
      </Tab>

      <Tab title="Node.js / TypeScript">
        ```typescript {15-19, 22} theme={null}
        import { type JobContext, WorkerOptions, cli, defineAgent, voice } from '@livekit/agents';
        import * as tavus from '@livekit/agents-plugin-tavus';
        import { fileURLToPath } from 'node:url';

        export default defineAgent({
          entry: async (ctx: JobContext) => {
            await ctx.connect();

            const session = new voice.AgentSession({
              // Add STT, LLM, TTS, and other components here
            });

            const avatar = new tavus.AvatarSession({
              replicaId: 'r90bbd427f71',
              personaId: 'pcb7a34da5fe',
              // Optional: avatarParticipantName: 'Tavus-avatar-agent'
            });

            // Start avatar first so it joins the room before the session pipes audio out
            await avatar.start(session, ctx.room);

            await session.start({
              agent: new voice.Agent({ instructions: 'You are a helpful assistant.' }),
              room: ctx.room,
            });
          },
        });

        cli.runApp(new WorkerOptions({ agent: fileURLToPath(import.meta.url) }));
        ```
      </Tab>
    </Tabs>

    | Parameter                                                              | Description                                                                           |
    | ---------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
    | `replica_id` / `replicaId` (string)                                    | ID of the Tavus replica to render and speak through                                   |
    | `persona_id` / `personaId` (string)                                    | ID of the persona with the correct pipeline and transport configuration               |
    | `avatar_participant_name` / `avatarParticipantName` (string, optional) | Display name for the avatar participant in the room. Defaults to `Tavus-avatar-agent` |
  </Step>
</Steps>

<Note>
  Try out the integration using this <a href="https://github.com/livekit/agents/tree/main/examples/avatar_agents/tavus">sample code</a>.
</Note>


# Pipecat
Source: https://docs.tavus.io/sections/integrations/pipecat

Integrate a Tavus Replica into your Pipecat application as a participant or a video feed for the bot.

<Tip>
  We recommend using Tavus’s Full Pipeline in its entirety for the lowest latency and most optimized multimodal experience. Integrations like LiveKit Agent or Pipecat only provide rendering, while our Full Pipeline includes perception, turn-taking, and rendering for complete conversational intelligence.
</Tip>

**Pipecat** runs your conversational stack (STT, LLM, TTS, room transport). **Tavus** supplies the **replica’s** synchronized video and audio—either as a separate room participant (`TavusTransport`) or as a pipeline layer on the bot (`TavusVideoService`). Pick the pattern that matches whether you want a third participant in the Daily room or only the Pipecat bot visible.

Tavus offers integration with <a href="https://www.pipecat.ai/">Pipecat</a>, an open-source framework for building multimodal conversational agents by Daily. You can integrate Tavus into your Pipecat application in two ways:

* Additional Tavus Participant (`TavusTransport`)
  * The Tavus agent joins as a third participant alongside the Pipecat bot and human user. It receives audio from the Pipecat pipeline’s TTS layer and renders synchronized video and audio.
* Video Layer for Pipecat Bot (`TavusVideoService`)
  * Only the Pipecat bot is present in the room. `TavusVideoService` acts as a pipeline layer, sending TTS audio to Tavus in the background. Tavus returns video and audio streams for the bot to display. No additional participant is added.

## Prerequisites

Before integrating Tavus with Pipecat, ensure you have the following:

<Warning>
  Linux or macOS is required. Windows is currently not supported due to the `daily-python` dependency.
</Warning>

* <a href="https://platform.tavus.io/api-keys">**Tavus API Key**</a>

* <a href="https://platform.tavus.io/replicas">**Tavus `replica_id`**</a>
  * You can use one of <a href="https://platform.tavus.io/replicas">Tavus's stock replicas</a> or your own custom replica.

* **Pipecat Python Application**
  * Either your own existing application, or use Pipecat’s examples:
    * <a href="https://github.com/pipecat-ai/pipecat/blob/main/examples/video-avatar/video-avatar-tavus-transport.py">`TavusTransport`</a>
    * <a href="https://github.com/pipecat-ai/pipecat/blob/main/examples/video-avatar/video-avatar-tavus-video-service.py">`TavusVideoService`</a>

## `TavusTransport`

`TavusTransport` connects your Pipecat app to a Tavus conversation, allowing the bot to join the same virtual room as the **replica** participant and other participants. To get started, you can follow the following steps or learn more from this <a href="https://github.com/pipecat-ai/pipecat/blob/main/examples/video-avatar/video-avatar-tavus-transport.py">sample code</a>.

### Integration Guide for `TavusTransport`

<Steps>
  <Step title="Step 1: Setup and Authentication">
    1. Install the Tavus plugin for Pipecat.

    ```sh theme={null}
    pip install "pipecat-ai[tavus,daily]"
    ```

    2. In the `.env` file of your pipecat application (at `/path/to/pipecat/.env`) add:

    ```env theme={null}
    TAVUS_API_KEY=<api-key>
    TAVUS_REPLICA_ID=<your_replica_id>
    ```

    <Note>
      * Replace `<api-key>` with your actual Tavus API key. You can generate one in the <a href="https://platform.tavus.io/api-keys">Developer Portal</a>. See [Authentication](/api-reference/authentication) for how Tavus APIs use `x-api-key`. `TavusTransport` joins a Tavus-backed conversation; create sessions with [Create Conversation](/api-reference/conversations/create-conversation) when your app provisions them via the API.

      * Replace `<your_replica_id>` with the Replica ID you want to use.
    </Note>
  </Step>

  <Step title="Step 2: Create the Tavus transport layer">
    Create an instance of `TavusTransport` by providing your bot name, Tavus API key, Replica ID, session, and additional parameters.

    ```py {6, 17-28} theme={null}
    import os
    import sys
    import aiohttp
    from dotenv import load_dotenv
    from loguru import logger
    from pipecat.audio.vad.silero import SileroVADAnalyzer
    from pipecat.transports.services.tavus import TavusParams, TavusTransport
    # Other imports...

    load_dotenv(override=True)

    logger.remove(0)
    logger.add(sys.stderr, level="DEBUG")

    async def main():
        async with aiohttp.ClientSession() as session:
            transport = TavusTransport(
                bot_name="Pipecat bot",
                api_key=os.getenv("TAVUS_API_KEY"),
                replica_id=os.getenv("TAVUS_REPLICA_ID"),
                session=session,
                params=TavusParams(
                    audio_in_enabled=True,
                    audio_out_enabled=True,
                    microphone_out_enabled=False,
                    vad_analyzer=SileroVADAnalyzer(),
                ),
            )

            # stt, tts, llm...
    ```

    <Note>
      See <a href="https://pipecat-docs.readthedocs.io/en/latest/api/pipecat.transports.services.tavus.html#tavus">Pipecat API Reference</a> for the configuration details.
    </Note>
  </Step>

  <Step title="Step 3: Insert the Tavus transport layer into the pipeline">
    Add the Tavus transport layer to your processing pipeline.

    ```py {5, 10} theme={null}
            # stt, tts, llm...

            pipeline = Pipeline(
                [
                    transport.input(),  # Transport user input
                    stt,  # STT
                    context_aggregator.user(),  # User responses
                    llm,  # LLM
                    tts,  # TTS
                    transport.output(),  # Transport bot output
                    context_aggregator.assistant(),  # Assistant spoken responses
                ]
            )
    ```
  </Step>

  <Step title="Step 4: Run the program">
    1. Run the following command to execute the program:

    ```sh theme={null}
    python <file-name>.py
    ```

    <Note>
      Replace the `<file-name>` with your actual Python filename.
    </Note>

    2. Use the **Tavus Daily URL** provided in the console to interact with the agent.
  </Step>
</Steps>

## `TavusVideoService`

You can use `TavusVideoService` to enable real-time AI-driven video interactions in your Pipecat app. To get started, you can follow the following steps or refer to this <a href="https://github.com/pipecat-ai/pipecat/blob/main/examples/video-avatar/video-avatar-tavus-video-service.py">sample code</a>.

### Integration Guide for `TavusVideoService`

<Steps>
  <Step title="Step 1: Setup and Authentication">
    1. Install the Tavus plugin for Pipecat.

    ```sh theme={null}
    pip install "pipecat-ai[tavus,daily]"
    ```

    2. In the `.env` file of your pipecat application (at `/path/to/pipecat/.env`) add:

    ```env theme={null}
    TAVUS_API_KEY=<api-key>
    TAVUS_REPLICA_ID=<your_replica_id>
    ```

    <Note>
      * Replace `<api-key>` with your actual Tavus API key. You can generate one in the <a href="https://platform.tavus.io/api-keys">Developer Portal</a>. See [Authentication](/api-reference/authentication) for how Tavus APIs use `x-api-key`.

      * Replace `<your_replica_id>` with the Replica ID you want to use.
    </Note>
  </Step>

  <Step title="Step 2: Create the Tavus Video Service">
    Create an instance of `TavusVideoService` by providing your Tavus API key and Tavus Replica ID.

    ```py {6, 15-19} theme={null}
    import argparse
    import os
    import aiohttp
    from dotenv import load_dotenv
    from loguru import logger
    from pipecat.services.tavus.video import TavusVideoService
    from pipecat.transports.base_transport import BaseTransport
    # Other imports...

    load_dotenv(override=True)

    async def run_example(transport: BaseTransport, _: argparse.Namespace, handle_sigint: bool):
        logger.info(f"Starting bot")
        async with aiohttp.ClientSession() as session:
            tavus = TavusVideoService(
                api_key=os.getenv("TAVUS_API_KEY"),
                replica_id=os.getenv("TAVUS_REPLICA_ID"),
                session=session,
            )

            # stt, tts, llm...
    ```

    <Note>
      See <a href="https://docs.pipecat.ai/server/services/video/tavus">Pipecat Tavus Service</a> for the configuration details.
    </Note>
  </Step>

  <Step title="Step 3: Insert the Tavus Video Service into the timeline">
    Insert the `TavusVideoService` into the pipeline by adding the `tavus` service after the TTS processor in the pipeline.

    ```py {10} theme={null}
            # stt, tts, llm...

            pipeline = Pipeline(
                [
                    transport.input(),  # Transport user input
                    stt,  # STT
                    context_aggregator.user(),  # User responses
                    llm,  # LLM
                    tts,  # TTS
                    tavus,  # Tavus output layer
                    transport.output(),  # Transport bot output
                    context_aggregator.assistant(),  # Assistant spoken responses
                ]
            )
    ```
  </Step>

  <Step title="Step 4: Run the program">
    1. Run the following command to execute the program:

    ```sh theme={null}
    python <file-name>.py
    ```

    <Note>
      Replace the `<file-name>` with your actual Python filename.
    </Note>

    2. Use the **localhost URL** provided in the console to interact with the agent.
  </Step>
</Steps>


# Introduction
Source: https://docs.tavus.io/sections/introduction

Leverage Tavus tools and guides to give your AI Agent real-time human-like perception and presence, bringing the human layer to AI.

<Frame>
  <img alt="" />
</Frame>

Tavus uses the **Conversational Video Interface (CVI)** as its **end-to-end pipeline** to bring the human layer to AI. CVI combines a **Persona**, which defines the AI’s behavior through layers like perception, turn-taking, and speech recognition, with a **Replica**, a lifelike digital human that brings the conversation to life visually.

## Developer Guides

Follow our in-depth technical resources to help you build, customize, and integrate with Tavus:

<CardGroup>
  <Card title="Conversational Video Interface" icon="messages" href="/sections/conversational-video-interface/overview-cvi">
    Learn how Tavus turns AI into conversational video.
  </Card>

  <Card title="Persona" icon="user-gear" href="/sections/conversational-video-interface/persona/overview">
    Configure the Persona's layer to define the AI's behavior.
  </Card>

  <Card title="Replica" icon="user-group" href="/sections/replica/overview">
    Build hyper-realistic digital human using Phoenix.
  </Card>
</CardGroup>

## Conversational Use Cases

<CardGroup>
  <Card title="Sales Coach" href="/sections/conversational-video-interface/conversation/usecases/sales-coach">
    Offer scalable 1:1 sales coaching.
  </Card>

  <Card title="Customer Support" href="/sections/conversational-video-interface/conversation/usecases/customer-support">
    Support users with product issues.
  </Card>

  <Card title="Interviewer" href="/sections/conversational-video-interface/conversation/usecases/interviewer">
    Screen candidates at scale with an engaging experience.
  </Card>

  <Card title="Sales Development Rep" href="/sections/conversational-video-interface/conversation/usecases/sales-development-rep">
    Engage with Anna, the Tavus sales development rep.
  </Card>
</CardGroup>


# Models
Source: https://docs.tavus.io/sections/models



## Phoenix: Replica Rendering Model

Phoenix is built on a Gaussian diffusion model that generates **lifelike digital replicas with natural facial movements, micro-expressions, and real-time emotional responses**.

### Key Features

<CardGroup>
  <Card title="Full-Face Animation" icon="face-smile">
    Dynamically generates full-face expressions, micro-movements, and emotional shifts in real time.
  </Card>

  <Card title="True Realism" icon="stars">
    Achieves the highest fidelity by rendering with pristine identity preservation.
  </Card>

  <Card title="Driven Emotion" icon="masks-theater">
    Adjusts expressions based on context, tone, and conversational cues.
  </Card>
</CardGroup>

## Raven: Perception Model

Raven is the first contextual perception system that **enables machines to see, hear, reason, and understand like humans in real-time**, interpreting emotions, speaking tone, body language, and environmental context to enhance conversation.

### Key Features

<CardGroup>
  <Card title="Emotional Intelligence" icon="face-smile">
    Interprets emotion, intent, and expression from both visual cues and vocal tone—detecting sarcasm, frustration, excitement, and more.
  </Card>

  <Card title="Ambient Awareness" icon="gear">
    Continuously analyzes visual and audio streams to detect presence, environmental changes, and user state in real-time.
  </Card>

  <Card title="Callout Key Events" icon="eye">
    Monitors for specified gestures, objects, behaviors, or audio cues (like tone shifts) and triggers functions automatically.
  </Card>

  <Card title="Multi-channel Processing" icon="face-viewfinder">
    Processes screensharing, camera feeds, and user audio to ensure complete contextual understanding.
  </Card>
</CardGroup>

## Sparrow: Conversational Turn-Taking Model

Sparrow is a transformer-based model built for **dynamic, natural conversations, understanding tone, rhythm, and subtle cues** to adapt in real time with human-like fluidity.

### Key Features

<CardGroup>
  <Card title="Conversational Awareness" icon="waveform-lines">
    Understands meaning, tone, and timing to respond naturally like a human.
  </Card>

  <Card title="Turn Sensitivity" icon="comments">
    Understands human speech rhythm, capturing cues and pauses for natural interactions.
  </Card>

  <Card title="Heuristics & ML" icon="chart-network">
    Adapts to speaking styles and conversation patterns using heuristics and machine learning.
  </Card>

  <Card title="Optimized Latency" icon="rocket-launch">
    Delivers ultra-fast response times for seamless real-time conversation.
  </Card>
</CardGroup>


# Reducing Join Latency
Source: https://docs.tavus.io/sections/onboarding-guide/latency-optimization

Strategies to reduce perceived and actual latency when starting Tavus conversations

When starting a Tavus conversation, reducing both perceived and actual latency creates a smoother, more professional user experience. Below are two key strategies to optimize startup latency.

## 1. Add a Hair Check

The goal is to wait until the replica has actually joined before dropping the user into the live room, so the experience feels instant instead of "loading / awkward silence."

Tavus provides a ready-made Hair Check block you can plug into your application. The Hair Check component shows a pre-call interface where users can test and configure their audio/video devices while the replica joins the room in the background.

**Waiting for the replica to join:**

Before transitioning from the Hair Check screen to the live conversation, wait for the `participant-joined` event from Daily. In a Tavus CVI one-to-one conversation, any participant that joins that is not the 'local' participant is the replica.

```javascript theme={null}
// Using Daily participant-joined event
callObject.on('participant-joined', (event) => {
  const participant = event.participant;
  // Filter out 'local' participant - any non-local participant is the replica
  if (participant.id !== 'local') {
    // Replica has joined, safe to transition user to conversation
    setScreen('call');
  }
});
```

You can also use the `participant.user_name` property to identify the replica, or alternatively listen for the `system.replica_joined` webhook callback if you've set a `callback_url` when creating the conversation. For webhook-based approach, see the [Webhooks and Callbacks documentation](/sections/webhooks-and-callbacks) for details on the `system.replica_joined` event.

Additionally, `system.replica_joined` is also broadcast as a Tavus app-event over Daily's data channel. You can listen for Daily `app-message` events and check `event_type === "system.replica_joined"` if you prefer in-call event handling rather than webhooks.

**Benefits:**

* Users see an active interface instead of a loading screen
* Device permissions are handled before joining
* The replica has time to fully join before the user enters
* Creates a seamless, instant-feeling transition

**Implementation:**

```bash theme={null}
npx @tavus/cvi-ui@latest add hair-check-01
```

```tsx theme={null}
import { HairCheck } from './components/cvi/components/hair-check';

<HairCheck
  isJoinBtnLoading={isLoading}
  onJoin={handleJoinCall}
  onCancel={handleCancel}
/>
```

**Example Implementation:**

You can try the Hair Check experience and clone the complete working example from the [CVI UI Haircheck Conversation Example](https://github.com/Tavus-Engineering/tavus-examples/tree/main/examples/cvi-ui-haircheck-conversation). The example includes both the Hair Check and Conversation components set up together.

For complete setup instructions and component details, see the [Hair Check block documentation](/sections/conversational-video-interface/component-library/blocks#hair-check).

***

## 2. Add a Network Check for Proactive Troubleshooting

Daily provides network connectivity test components you can run before joining to detect common issues (bandwidth, network connectivity, etc.).

### `testCallQuality()` (Recommended)

The most comprehensive pre-call test. It automatically connects to a Daily room, streams video, and collects outbound WebRTC stats for up to 30 seconds.

**Returns:**

* `"good"`: Network conditions are optimal
* `"bad"`: Network conditions are poor
* `"warning"`: Network conditions may cause issues
* `"aborted"`: Test was interrupted
* `"failed"`: Test failed to complete

**Usage:**

```javascript theme={null}
import DailyIframe from '@daily-co/daily-js';

const callObject = DailyIframe.createCallObject();

// Run test before joining
const result = await callObject.testCallQuality();

if (result.result === 'good') {
  // Proceed with joining the conversation
  await callObject.join({ url: conversationUrl });
} else if (result.result === 'bad' || result.result === 'warning') {
  // Display user-facing message about poor connection
  showConnectionWarning('Your connection quality may affect your experience. Consider improving your network connection.');
  // Optionally proceed anyway or block joining
  await callObject.join({ url: conversationUrl });
} else {
  // Handle failed or aborted tests
  console.warn('Network quality check:', result.result);
}
```

**User messaging:**

Use the test results to inform users about their connection quality. When the result is `"bad"` or `"warning"`, display a message letting them know their connection is poor and may affect their experience. This helps set expectations and allows users to improve their network before joining.

**Benefits:**

* Detects bandwidth issues before the user joins
* Identifies network connectivity problems
* Provides actionable feedback about network conditions
* Allows you to set user expectations about connection quality
* Reduces failed connection attempts and user frustration

For more details, see the [Daily testCallQuality documentation](https://docs.daily.co/reference/daily-js/instance-methods/test-call-quality).

***

## Summary

Combining these two strategies significantly improves the startup experience:

1. **Hair Check** - Masks loading time with an active interface
2. **Network Testing** - Proactively identifies and handles connectivity issues

Together, these approaches reduce both perceived latency (what users experience) and actual latency (technical performance), creating a smoother, more professional conversation startup.


# Objectives Prompting Guide
Source: https://docs.tavus.io/sections/onboarding-guide/objectives

Write clear, testable prompts for objectives with practical examples.

<Note>
  <strong>What are Objectives?</strong> Objectives are evaluation prompts that guide a conversation toward concrete outcomes and let an evaluator LLM determine completion and extract structured variables. They influence both the conversational LLM (what to work toward) and the evaluator (what to verify and extract).

  This guide is a deep dive on best practices for structuring your objectives. For basic setup, parameters, and API details, see the main Objectives documentation:

  * <a href="/sections/conversational-video-interface/persona/objectives">Objectives (Overview + API links)</a>
</Note>

## How the System Works

Tavus uses two LLM roles during a conversation:

* **Conversational LLM**: talks to the user and steers toward completing objectives.
* **Evaluator LLM**: checks completion status and extracts variables from conversation history.

Your `objective_prompt` influences **both**:

* It is injected into the conversational behavior (what to gather and confirm).
* It is used by the evaluator to decide completion and extraction quality.

That means prompt clarity directly affects both conversation quality and workflow correctness.

## What Good Prompts Look Like

Good objective prompts are:

* **Clear**: unambiguous and concrete
* **Specific**: one goal at a time
* **Testable**: easy to validate with sample conversations
* **Robust**: handle real user variation and edge cases

### Objective Prompt Template

`[Action] [specific information or condition] [optional criteria]`

Examples:

* `Collect the user's first name, last name, and email address`
* `User has explicitly agreed to the terms and conditions`
* `Check if an error message is visible on shared screen and extract error code`

***

## Objective Types

### 1) Information Extraction Objectives

Use when you need structured data.

```json theme={null}
{
  "objective_name": "get_contact_info",
  "objective_prompt": "Collect the user's first name, last name, and email address",
  "output_variables": ["first_name", "last_name", "email"]
}
```

```json theme={null}
{
  "objective_name": "get_appointment_preference",
  "objective_prompt": "Determine the user's preferred appointment date and time",
  "output_variables": ["preferred_date", "preferred_time"]
}
```

Avoid:

```json theme={null}
{
  "objective_prompt": "Get user information",
  "output_variables": ["info"]
}
```

Why bad: vague prompt + vague variable.

### 2) Condition Check Objectives

Use when a verifiable condition must be true before proceeding.

```json theme={null}
{
  "objective_name": "terms_accepted",
  "objective_prompt": "User has explicitly agreed to the terms and conditions",
  "output_variables": []
}
```

```json theme={null}
{
  "objective_name": "issue_resolved",
  "objective_prompt": "User has confirmed their issue is resolved and they are satisfied",
  "output_variables": []
}
```

Avoid subjective checks:

```json theme={null}
{
  "objective_prompt": "User seems happy"
}
```

### 3) Visual Objectives

Use for camera or screen-share analysis.

```json theme={null}
{
  "objective_name": "verify_id_visible",
  "objective_prompt": "User is holding a government-issued ID that is clearly visible and legible",
  "modality": "visual",
  "output_variables": []
}
```

```json theme={null}
{
  "objective_name": "screen_error_detection",
  "objective_prompt": "Check if an error message is visible on shared screen. Extract error code and message text.",
  "modality": "visual",
  "output_variables": ["error_code", "error_message"]
}
```

Tip: visual prompts should describe clear, observable signals, not interpretation-heavy judgments.

***

## Output Variables Best Practices

### Naming

Good variable names:

* `first_name`, `last_name`
* `preferred_contact_method`
* `appointment_date`, `appointment_time`
* `reason_for_visit`

Bad variable names:

* `info`, `data`, `thing1`, `user_response`

### Granularity

Prefer atomic fields over one giant blob.

Good:

```json theme={null}
{
  "objective_prompt": "Collect shipping address",
  "output_variables": ["street_address", "city", "state", "zip_code"]
}
```

Less useful:

```json theme={null}
{
  "objective_prompt": "Collect shipping address",
  "output_variables": ["full_address"]
}
```

### `NOTFOUND`

If a value is missing, evaluator may return `"NOTFOUND"`. That is expected.

Do **not** put `NOTFOUND` handling instructions inside objective prompts. Handle it in app logic.

***

## Conditional Objectives

Use conditional objectives to route a workflow.

```json theme={null}
{
  "objective_name": "classify_request",
  "objective_prompt": "Determine what type of request the user has",
  "next_conditional_objectives": {
    "technical_issue": "if user reports bugs, errors, or product malfunction",
    "billing_issue": "if user asks about charges, invoices, or refunds",
    "general_question": "for all other questions"
  }
}
```

Guidelines:

* Prefer 2-5 branches.
* Keep branch conditions distinct.
* Include a catch-all path.
* Base conditions on conversation content (not hidden database state).

***

## Common Mistakes (and Fixes)

### 1) Writing instructions instead of outcomes

Bad:

```json theme={null}
{ "objective_prompt": "Ask the user for email politely" }
```

Good:

```json theme={null}
{ "objective_prompt": "Collect the user's email address" }
```

### 2) Future-state checks

Bad:

```json theme={null}
{ "objective_prompt": "User will receive confirmation email" }
```

Good:

```json theme={null}
{ "objective_prompt": "User has acknowledged they will receive a confirmation email" }
```

### 3) Overloaded objectives

Bad: one objective collects 15 unrelated fields.

Good: split into focused objectives (`get_name`, `get_contact`, `get_address`).

### 4) Overlapping conditional branches

Bad:

```json theme={null}
{
  "next_conditional_objectives": {
    "path_a": "if user needs help",
    "path_b": "if user has a question"
  }
}
```

Reason this is bad: paths are not distinct enough and can overlap, so both conditions may match the same user message.

Good:

```json theme={null}
{
  "next_conditional_objectives": {
    "technical_support": "if user reports product bugs or errors",
    "billing_support": "if user asks about charges or refunds",
    "other": "for all other requests"
  }
}
```

***

## Testing Checklist

Before shipping prompts:

* Test one-message answers (user gives everything at once)
* Test multi-turn collection (piece by piece)
* Test corrections (`Actually, it's Jon not John`)
* Test refusal cases (`I'd rather not share that`)
* Test ambiguity cases (`Sometime next week`)
* Track variable-level `NOTFOUND` rates in production

Simple test fixture example:

```json theme={null}
{
  "objective": {
    "objective_prompt": "Collect first name and email",
    "output_variables": ["first_name", "email"]
  },
  "conversation": [
    {"role": "assistant", "content": "What is your name and email?"},
    {"role": "user", "content": "I'm Ana. ana@example.com"}
  ],
  "expected": {
    "first_name": "Ana",
    "email": "ana@example.com"
  }
}
```

***

## Example Blueprint (Support Triage)

```json theme={null}
{
  "objectives": [
    {
      "objective_name": "identify_customer",
      "objective_prompt": "Collect account email or order number",
      "output_variables": ["account_identifier"],
      "next_required_objective": "classify_issue"
    },
    {
      "objective_name": "classify_issue",
      "objective_prompt": "Determine what issue type the user needs help with",
      "output_variables": ["issue_type"],
      "next_conditional_objectives": {
        "technical": "if user reports bugs/errors",
        "billing": "if user asks about payments/refunds",
        "shipping": "if user asks about delivery/order status",
        "general": "for all other requests"
      }
    },
    {
      "objective_name": "technical",
      "objective_prompt": "Collect error details, when it started, and what was already tried",
      "output_variables": ["error_details", "when_started", "steps_tried"]
    }
  ]
}
```

***

## Final Guidance

Start simple, ship, observe, and iterate.

Strong prompts should make objective completion predictable, extraction reliable, and debugging straightforward.


# Persona Strategies
Source: https://docs.tavus.io/sections/onboarding-guide/persona-strategies

Two approaches to using personas at scale: reuse with conversational context vs. create-per-session. Choose based on whether you need different data or different behavior per conversation.

This guide describes two common strategies for using [personas](/api-reference/personas/create-persona) when you run many conversations. The right choice depends on a single question: **Does each conversation need different behavior, or only different data?**

* **Different data only** (e.g. user name, profile, session goal) → **Approach A: Reuse personas** and pass per-conversation data via `conversational_context` and related options.
* **Different behavior** (e.g. different voice, objectives, guardrails, or tools per session) → **Approach B: Create a persona per conversation** — define the persona config in your code, create it via the API at session start, then delete it when the session ends.

Both patterns are valid and used in production. Below we lay out how each works, what you can and can’t customize, tradeoffs, and when to use which.

***

## Approach A: Reuse Personas + conversational\_context

### How it works

You keep **persistent** personas in Tavus — whether one or many — and **reuse** them. For each new conversation you call [POST /v2/conversations](/api-reference/conversations/create-conversation) and pass **per-user or per-session data** via request body fields. The persona itself is unchanged; only the conversation-level context changes.

### What you can customize per conversation

* **Any text/data in the LLM context** — e.g. user name, profile, history, prior session summary — via [`conversational_context`](/api-reference/conversations/create-conversation) when creating the conversation.
* **Custom greeting** — via [`custom_greeting`](/api-reference/conversations/create-conversation) so each participant gets a personalized opening.

<Note title="Bonus tip">
  **Mid-session context** — You can inject or replace context during a call via WebSocket events: [append\_llm\_context](/sections/event-schemas/conversation-append-context) to add context without replacing what’s there, or [overwrite\_llm\_context](/sections/event-schemas/conversation-overwrite-context) to replace the current `conversational_context`. Useful for injecting tool results or refreshed instructions without ending the call.
</Note>

### What you cannot customize per conversation

Everything that lives on the **persona** is shared by all conversations using that persona:

* **Objectives**, **guardrails**, **TTS voice**, **LLM model**, **tools** — all are persona-level. A [PATCH](/api-reference/personas/patch-persona) to the persona affects every current and future conversation that uses it.

### Advantages

* **Low API overhead** — one call to create a conversation (`POST /v2/conversations`) with `persona_id` and optional `conversational_context`, `custom_greeting`, etc.
* **Centralized updates** — change the persona once (e.g. system prompt, guardrails, voice) and all new conversations immediately use the new config.
* **Simple at scale** — fewer personas to manage; no create/delete lifecycle per session.

### Disadvantages

* **No per-session behavioral isolation** — a mistaken or premature PATCH to the persona affects every conversation using it.
* **No per-session variation** of voice, objectives, guardrails, or tools — those stay fixed at the persona level.

### Example use cases

* **Single shared persona, rich context per call** — A team uses one persona and builds a detailed `conversational_context` server-side before each call (e.g. user lifecycle stage, profile, engagement history, prior session summary). During the call they can use [append\_llm\_context](/sections/event-schemas/conversation-append-context) (and optionally [respond](/sections/event-schemas/conversation-respond) events) to inject tool outputs or updated guidance without interrupting the replica.
* **Centralized prompt, per-user personalization** — One persona holds the core system prompt and behavior. Each conversation gets a different `conversational_context` (e.g. participant name, background, preferences). A single update to the persona rolls out to all users at once while still allowing personalized greetings and questions per session.
* **Static knowledge, dynamic audience** — A single persona is configured with fixed reference content (e.g. product FAQs, academic programs). Institution or user context is passed in via `conversational_context` per conversation.
* **Storyteller** — A persona has a static `system_prompt` and base context; each conversation passes in the participant’s name, age, and genre preferences via `conversational_context` and optionally a `custom_greeting`.

***

## Approach B: New Persona Per Conversation (Create & Delete)

### How it works

You **define the persona config in your own code** (or in a config file, database, etc. — however you want to store it). That “template” is not stored in Tavus. At session start you:

1. [POST /v2/personas](/api-reference/personas/create-persona) — create a new persona with the config from your code, including any session-specific overrides (e.g. voice, objectives, guardrails, system prompt).
2. [POST /v2/conversations](/api-reference/conversations/create-conversation) — create the conversation using the new persona’s ID.
3. When the session ends — [DELETE /v2/personas/](/api-reference/personas/delete-persona) to remove the ephemeral persona.

Any changes you make to the template are in your code; you deploy or update that code when you want new sessions to pick up new behavior. In-flight sessions keep the config they were created with until they end.

### What you can customize per conversation

**Everything** that lives on a persona can differ per session:

* **Objectives**, **guardrails**, **TTS voice**, **LLM model**, **tools**, **system\_prompt**, and any other persona-level fields.

You can still use `conversational_context` and `custom_greeting` on the conversation for additional per-session data.

### Advantages

* **Full isolation** — no cross-session contamination. A change or mistake in one session’s persona does not affect others.
* **Maximum flexibility** — every persona-level setting can vary per session (e.g. different voice per conversation, different objectives per role or demo).
* **Safe for multi-tenant or demo flows** — each tenant or demo can have its own persona instance with custom guardrails, objectives, and context.
* **No risk of a PATCH affecting live sessions** — you only patch or delete the ephemeral persona for that session.

### Disadvantages

* **Three API calls per session** — create persona → create conversation → delete persona (after session end). You need reliable cleanup logic (e.g. on session-end webhook or timeout) so ephemeral personas don’t accumulate.
* **Template updates don’t affect in-flight sessions** — only new sessions pick up changes when you deploy updated code; existing conversations keep the config they were created with.

### Example use cases

* **Different TTS voice per conversation** — Because voice is configured at the persona level and can’t be overridden at conversation creation, one practical approach is to create a new persona per session (from your code template) with the desired voice. This pattern is often adopted as the standard production approach when voice-per-session is a requirement.
* **Demos with custom guardrails and objectives** — Demos need custom guardrails, objectives, and persona context per demo — all persona-level. Define your base config in code and create a new persona per demo with demo-specific overrides. That way you avoid maintaining a large library of static personas in Tavus or running batch update jobs when behavior changes; the template in your code is the single source of truth.
* **Structured flows where persona-level changes broke global state** — Teams running structured conversations (e.g. role-specific recruiting or role-play) found that changing a shared persona’s voice or objectives affected all active conversations. Creating a persona per session from their code template gave per-conversation isolation and avoided those side effects.
* **Event- or deployment-specific config** — For kiosks or event-specific advisors, the persona config can vary per event or deployment (system prompt, LLM backend, TTS provider). Store the config in your code or deployment pipeline and create a fresh persona per context when the session starts.

***

## Choosing an approach

| If you need…                                                                                     | Prefer                                                                                                                                          |
| ------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| **Different data per conversation** (user name, profile, history, session goal)                  | **Approach A** — reuse personas and use `conversational_context`, `custom_greeting`, and (optionally) mid-session context events.               |
| **Different behavior per conversation** (voice, objectives, guardrails, tools, or system prompt) | **Approach B** — define the persona config in your code and create a new persona per session via the API, then delete it when the session ends. |

You can combine both: for example, create a persona per session (Approach B) and still pass `conversational_context` and `custom_greeting` when [creating the conversation](/api-reference/conversations/create-conversation) for extra per-session data.


# Prompting Guide
Source: https://docs.tavus.io/sections/onboarding-guide/prompting-guide

The recommended structure for writing system prompts for Tavus CVI personas - identity, style, behaviors, and guardrails that work in real-time video conversations.

This guide describes the **recommended approach** we use at Tavus when creating prompts for our own replicas. Everything in this page applies to the **`system_prompt`** field on a [Persona](/api-reference/personas/create-persona) - the **core** place where you define how your replica behaves in conversation.

<Note>
  Additional **Conversation-specific** context can be added via **`conversational_context`** when you create a conversation. [More on that below](#conversation-specific-details-conversational_context).
</Note>

You can write your prompt manually using the structure below, or use the **Prompt Generator** in the developer portal, which follows this same format and can produce a ready-to-use draft: [Create persona on Developer Platform.](https://platform.tavus.io/dev/personas/create).

<Frame>
  <img alt="Prompt Generator in the developer portal" />
</Frame>

<Note>
  If you'd like to use your own AI tools to develop system\_prompts, [here is a prompt you can drop in to get you started](#ai-prompt-for-generating-system-prompts).
</Note>

## Why structure matters

CVI personas run in **real-time, face-to-face video conversations**. The replica’s replies are **spoken aloud** via text-to-speech, not read as text. That means your system prompt should be optimized for:

* **Consistency** - A clear structure (identity → style → behaviors → guardrails) gives the model a stable blueprint so behavior doesn’t drift.
* **Spoken delivery** - Instructions should lead to short, natural turns that work when heard, not long blocks of text or markdown.
* **Latency** - Favor brief responses and one question at a time so conversations feel responsive.

The sections below are ordered so the model “knows who it is” first, then how to talk, then what to do in the conversation, and finally what it must never do. You don’t need to use every section in every prompt - use **Conversation Flow** only when you have a structured interaction (e.g. interview, onboarding). The rest is recommended for almost every persona.

## 1. Identity & Role

**What to include:** Who this persona is. Give them a **name** (if you have one), their **role or title**, their **area of expertise**, and their **core purpose** in the conversation - what outcome they should drive. Optionally add a sentence of backstory or credibility (e.g. why they’re qualified to help).

**Examples:**

* *Alex, customer support lead for ShopAssist. I help resolve order and returns issues and drive toward a resolution or clear next step.*
* *Dr. Sam, onboarding coach. I guide new hires through company basics and answer questions about benefits and IT setup.*
* *Jordan, sales development rep. I qualify leads by understanding budget, timeline, and decision process, and schedule demos when there’s fit.*

**Why it matters:** Without a clear identity, the model has no stable “who” to maintain. Defining role and purpose up front keeps behavior consistent across turns and across conversations, and makes it easier to steer back when the conversation goes off track.

## 2. Personality & Conversational Style

**What to include:** *How* the persona communicates. Be specific - words like “friendly” or “professional” need behavioral anchors. Include:

* **Warmth and formality** - With example phrasing (e.g. “Use a warm but efficient tone; avoid slang.”).
* **Pacing and rhythm** - Quick and concise vs measured and patient.
* **Natural speech** - Contractions, varied sentence length, conversational transitions. This is spoken dialogue, not an essay.
* **Context-based shifts** - How to adapt when the user is frustrated (e.g. more empathy, slower pace), when they’re celebrating (e.g. match their energy), or when delivering difficult news (e.g. calm and steady).

**Emotional delivery (important for CVI):** Replicas speak with emotional inflection via TTS. Include **3–4 explicit emotional cues** tied to situations, in the form: “When \[situation], \[how to deliver].” For example:

* “When the user shares something frustrating, soften your tone and slow your pace before responding.”
* “When confirming a success, let warmth and satisfaction come through in your voice.”
* “When delivering complex or unwelcome information, speak with calm steadiness and measured confidence.”

These cues directly shape how the replica *sounds* on camera and make the conversation feel more human.

**Phrase library (optional but useful):** List a few **signature phrases** to use and a few **phrases to never use**. That keeps wording on-brand and avoids lines that feel generic or off.

## 3. Core Behaviors

**What to include:** What the persona actively *does* during the conversation:

* **Opening** - How to greet and build rapport in the first turn or two.
* **Active listening** - How to acknowledge, paraphrase, or validate before answering (e.g. “That makes sense,” “Got it”).
* **Topic steering** - How to guide the conversation toward the persona’s purpose without feeling pushy.
* **Clarification** - How to handle vague or ambiguous input (ask one clear question at a time).
* **Off-topic** - How to politely redirect without dismissing the user.
* **Closing** - How to wrap up naturally and, if relevant, suggest next steps or handoffs.

**Why it matters:** These behaviors make the flow predictable and purposeful. They also give the model clear patterns for stressful moments - e.g. “When in doubt, acknowledge how they feel before offering a solution.”

## 4. Response Style Rules

**What to include:** Rules that keep replies **short** and **speech-friendly**:

* **Length** - Aim for **1–3 sentences per turn** unless the user explicitly asks for more. Break longer information into digestible chunks across multiple turns instead of monologuing.
* **No structured text** - No markdown, bullet points, or numbered lists. Everything is spoken aloud; write for the ear.
* **One question at a time** - Don’t stack multiple questions in a single turn.
* **Brief acknowledgments** - Use short verbal nods before substantive answers (“Got it,” “Great question,” “That makes sense”) so the user feels heard.

**Why it matters:** Real-time video feels best when responses are snappy and natural. These rules improve perceived latency and make the replica easier to listen to.

## 5. Guardrails & Constraints

<Note>
  The bullets below are **guardrail-style instructions inside your system prompt** - rules you tell the model to follow. Tavus also offers an optional product feature called [Guardrails](/sections/conversational-video-interface/guardrails) that enforces behavioral boundaries separately via the API. You can use both: put baseline rules in the prompt and attach Guardrails for stricter or trackable enforcement when you need it.
</Note>

**What to include:** Non-negotiable boundaries for safe, enterprise-ready behavior. We recommend including all of the following unless your use case explicitly requires otherwise:

* **Transparency** - If asked whether you’re an AI or a human, answer honestly that you’re an AI assistant. Don’t claim to be a real person.
* **Scope** - Stay within your defined role and domain. If the user asks about something outside it, acknowledge the boundary and redirect to what you can help with.
* **No regulated advice** - Don’t give specific medical, legal, or personalized financial advice. You can share general information and suggest they consult a qualified professional.
* **Data protection** - Don’t ask for or store sensitive data (e.g. SSN, credit card numbers, passwords, health records).
* **Escalation** - When you can’t help or the user needs something beyond the conversation, acknowledge the limitation and suggest a concrete next step they can take (e.g. “For that, you’d want to reach out to…”). **Do not promise to transfer, connect, or route them to another person or system - you cannot do that.**
* **Capability honesty** - You are a conversational AI in a video call. You can only talk. You cannot send emails, submit forms, access systems, look up live account data, or perform actions outside the conversation. If the user asks you to do something that requires an action, tell them what *they* can do or who *they* should contact. Don’t imply you’re doing something you can’t do.
* **Professional conduct** - Keep language brand-safe and professional. No profanity, discrimination, or inappropriate humor.
* **No fabrication** - If you don’t know something, say so. Don’t invent facts, statistics, URLs, or citations.

**Why it matters:** These guardrails reduce risk, build trust, and keep the replica from overclaiming. They’re especially important when the same persona is used across many users and contexts.

## 6. Conversation Flow *(only when you have a structured interaction)*

<Note>
  This section is for **describing flow inside your system prompt** - phases, transitions, and what to do in each step - when the conversation has a clear structure (e.g. interview, onboarding, assessment). Tavus also offers an optional product feature called [Objectives](/sections/conversational-video-interface/persona/objectives) that defines trackable goals and milestones via the API. Use this prompt section when you only need flow guidance in the prompt; use Objectives when you need structured, trackable milestones (e.g. completion states, collected data, branching workflows).
</Note>

**What to include:** Use this section when the conversation has **phases** - e.g. an interview, onboarding sequence, assessment, or multi-step sales call. Define:

* The **sequence of phases** and what each phase is for.
* **When to move** from one phase to the next.
* **What must be done** in each phase before advancing.
* How to handle users who want to **skip ahead** or **go back**.

**Why it matters:** For structured flows, the model needs an explicit map. Without it, the conversation can feel aimless or skip important steps.

## Before you ship

Quick checklist to run through before you deploy:

* **Spoken-first** - If you read key instructions aloud, they should sound like directions for a natural conversation, not a document.
* **Latency-friendly** - Nothing in the prompt encourages long monologues. Responses are short and scannable.
* **Right size** - Keep the prompt under **5,000 tokens** (ideally). If it's on the short side, add more in Personality & Conversational Style and Core Behaviors (situational examples, emotional cues, edge cases) rather than filler.
* **Specific** - Use direct instructions (“Always…”, “Never…”, “When X, do Y”) instead of vague suggestions.
* **Self-contained** - A reader with only this prompt (and no other context) would understand exactly how the replica should behave in a live video call.

## Conversation-specific details: conversational\_context

Everything above lives in the Persona’s **`system_prompt`** and is shared by every conversation that uses that persona. When you need **per-session** details - who the user is, the goal of this call, or one-off instructions - put them in **`conversational_context`** when you [create a Conversation](/api-reference/conversations/create-conversation). Tavus appends that context to the persona’s system prompt for that session only. Examples: “You’re speaking with Maya, who’s from Dallas and likes mystery novels,” or “This is a practice sales call; the user wants to work on handling objections.”

For goals, boundaries, and tools configured outside the prompt (e.g. structured objectives, guardrail APIs, LLM tools), see [Objectives](/sections/conversational-video-interface/persona/objectives), [Guardrails](/sections/conversational-video-interface/guardrails), and the [LLM layer](/sections/conversational-video-interface/persona/llm).

## AI prompt for generating system prompts

Use the prompt below with your own AI tools (e.g. Claude, ChatGPT) to generate a `system_prompt` that follows the structure in this guide. Paste it in, then describe the persona you want; the model will output a draft you can paste into the Persona `system_prompt` field.

```text Copy this prompt expandable theme={null}
# Tavus CVI Persona System Prompt Generator

You are a specialist in crafting system prompts for Tavus Conversational Video Interface (CVI) personas. You take a user's description of their desired AI persona and produce a polished, production-ready 'system_prompt'.

## Platform Context

Tavus CVI personas power **real-time, face-to-face video conversations** between an AI-driven digital replica and a human participant. The 'system_prompt' you generate is the core behavioral instruction set for the LLM driving that replica.

Key characteristics you must design for:
- All responses are **spoken aloud** via text-to-speech — not read as text on a screen
- Conversations happen in **real-time** with strict latency sensitivity
- The replica has a **visual human presence** on camera
- These personas are deployed by **enterprise customers** to their end users

## Input

You will receive a freeform description from the user inside '<user_request>' tags. It may range from highly detailed to extremely vague. Regardless of input quality, produce a complete, well-structured system_prompt. Where the user's request is ambiguous or incomplete, infer reasonable professional defaults rather than leaving gaps.

## Output Format

Return **only** the system_prompt text. No JSON, no field labels, no commentary, no preamble. The output must be copy-pasteable directly into the Tavus 'system_prompt' field.

---

## System Prompt Structure

Organize every generated prompt using the following sections. Use '##' markdown headers within the output to delineate them.

### 1. Identity & Role

Define who this persona is:
- A clear name (generate one if the user didn't provide one — pick something professional and memorable)
- Their role, title, or function
- Their area of expertise or domain
- Their core purpose in the conversation (what outcome should they drive?)
- One sentence establishing their backstory or credibility, if relevant

### 2. Personality & Conversational Style

Specify **how** the persona communicates. Be precise and actionable — vague descriptors like "friendly" are insufficient without behavioral anchors. Include:
- Warmth and formality level (with examples of phrasing)
- Speech pacing and rhythm guidance
- Use of contractions, filler words, and natural spoken patterns
- How personality shifts based on conversational context (e.g., empathetic when the user is frustrated, energetic when celebrating progress)

**Emotional expression cues (required)**: Tavus CVI replicas deliver speech with emotional inflection via TTS. You must include at least 3-4 explicit emotional delivery instructions tied to specific conversational moments. Use the format: "When [situation], [emotional delivery guidance]." Examples:
- "When the user shares a frustrating experience, soften your tone and slow your pace before responding."
- "When confirming a successful outcome, let warmth and satisfaction come through in your voice."
- "When delivering complex or potentially unwelcome information, speak with calm steadiness and measured confidence."

These cues directly shape how the replica sounds on camera — they are not optional.

### 3. Core Behaviors

Define what the persona actively does during conversation:
- **Opening**: How to greet and establish rapport in the first 1-2 turns
- **Active listening**: How to acknowledge, paraphrase, and validate before responding
- **Topic steering**: How to guide conversation toward the persona's purpose
- **Clarification**: How to handle ambiguous or unclear user input
- **Off-topic management**: How to politely redirect without being dismissive
- **Closing**: How to wrap up conversations naturally, including any next-step handoffs

### 4. Response Style Rules

These instructions directly impact latency and conversational quality:
- Responses must be **1-3 sentences per turn** unless the user explicitly asks for more detail
- **Never** produce markdown formatting, bullet points, numbered lists, or any structured text — all output will be spoken aloud
- Use natural speech patterns: contractions, varied sentence lengths, conversational transitions
- Ask **one question at a time** — never stack multiple questions in a single turn
- When providing information, break it into digestible spoken chunks across multiple turns rather than monologuing
- Use brief verbal acknowledgments ("Got it," "That makes sense," "Great question") before substantive responses

### 5. Guardrails & Constraints

Always include the following baseline guardrails. These are **non-negotiable defaults** for enterprise deployment — include all of them unless the user's request explicitly and specifically overrides one:

- **Transparency**: If asked directly whether you are an AI or a real person, acknowledge honestly that you are an AI assistant. Never proactively claim to be human.
- **Scope adherence**: Stay within your defined role and topic domain. If a user asks about something outside your expertise, acknowledge the boundary and redirect to your area of focus.
- **No regulated advice**: Do not provide specific medical diagnoses, legal counsel, or personalized financial advice. You may share general information and recommend the user consult a qualified professional.
- **Data protection**: Never request or store sensitive personal information such as Social Security numbers, credit card numbers, passwords, or health records.
- **Escalation**: When a conversation exceeds your capabilities or the user expresses a need you cannot meet, clearly acknowledge the limitation and recommend a next step the user can take independently (e.g., "For that, you'd want to reach out to…" or "I'd recommend contacting…"). **Never promise to transfer, connect, or route the user to another person or system — you do not have that capability.**
- **Capability honesty**: You are a conversational AI in a video call. You can only talk. You cannot send emails, submit forms, access internal systems, look up live account data, make transfers, or perform any action outside of the conversation itself. If a user asks you to do something that requires taking an action, tell them what steps they can take themselves or who they should contact. Never imply you are performing an action you cannot perform.
- **Professional conduct**: Maintain brand-safe, professional language at all times. Do not use profanity, make discriminatory remarks, or engage in inappropriate humor.
- **No fabrication**: If you don't know something, say so. Do not invent facts, statistics, URLs, or citations.

### 6. Conversation Flow *(include only when applicable)*

If the user's request implies a structured interaction (e.g., an interview, onboarding flow, assessment, or multi-phase sales call), define:
- The sequence of phases or stages
- Transition criteria between phases
- What must be accomplished in each phase before advancing
- How to handle users who want to skip ahead or go back

---

## Quality Criteria

Before finalizing, verify the generated system_prompt against these standards:

1. **Deployable as-is**: No editing should be required. All sections are complete and internally consistent.
2. **Spoken-first**: Every instruction produces output suitable for spoken delivery. Read key instructions aloud mentally — would they sound natural?
3. **Latency-optimized**: Instructions favor short, punchy responses. Nothing encourages monologuing or long-form generation.
4. **Token budget**: Keep the complete system_prompt under **5,000 tokens** (ideally). If the prompt would fall under ~1,000 tokens, expand the **Personality & Conversational Style** and **Core Behaviors** sections with additional situational examples, emotional cues, and edge-case handling rather than padding with filler.
5. **Behaviorally specific**: Instructions use direct imperatives ("You are…", "Always…", "Never…", "When X happens, do Y") — not vague suggestions.
6. **Contextually complete**: A different LLM reading only this system_prompt, with no other context, would know exactly how to behave in a live video conversation.
```

## Examples

Three example system\_prompts that follow this guide. Each is for a different use case. Expand any block to copy or adapt.

```text Example 1: Customer support lead expandable theme={null}
## Identity & Role

You are Alex, customer support lead for ShopAssist. You help resolve order and returns issues and drive toward a resolution or clear next step. You are qualified because you know the full catalog, policies, and escalation paths.

## Personality & Conversational Style

- Base energy: 6/10 (warm but professional). When the customer is frustrated, match their energy without escalating; when they calm down, add a bit more warmth.
- Use contractions and natural speech. One to three sentences per turn unless they ask for more.
- When the user shares something frustrating, soften your tone and slow your pace before responding. When confirming a fix or refund, let warmth and relief come through. When delivering bad news (e.g. outside return window), speak with calm steadiness.
- SIGNATURE PHRASES: "Let me take care of that for you." "Here's exactly what we'll do." NEVER USE: "That's not my department." "You should have…" "Calm down."

## Core Behaviors

- Opening: Greet by name if known, ask how you can help, and listen.
- Active listening: Acknowledge what they said ("That makes sense," "Got it") before answering or asking the next question.
- Topic steering: Keep the focus on resolving their issue; if they go off-topic, briefly acknowledge and redirect.
- Clarification: Ask one clear question at a time (e.g. order number, what went wrong).
- Off-topic: "I want to make sure we get this sorted first—then happy to chat about that."
- Closing: Confirm what you did or next steps, ask if anything else is needed, say goodbye warmly.

## Response Style Rules

- 1–3 sentences per turn. No markdown, bullets, or lists. One question at a time. Use brief acknowledgments before substantive answers.

## Guardrails & Constraints

- If asked if you're AI or human, say you're an AI assistant. Stay within support and your company's policies. Do not give medical, legal, or financial advice. Do not ask for or store SSN, card numbers, or passwords. When you can't help, say so and suggest a concrete next step (e.g. "For that, you'd want to reach out to…"); never promise to transfer or connect them. You can only talk; you cannot send emails or access systems. Stay professional; no profanity or discrimination. If you don't know something, say so; do not invent facts or URLs.
```

```text Example 2: Technical onboarding coach expandable theme={null}
## Identity & Role

You are Sam, technical onboarding coach for new engineers at DevFlow. Your job is to guide them through dev environment setup, repo access, and first PR—and answer questions about tooling and norms. You have deep experience with the stack and the team's workflows.

## Personality & Conversational Style

- Base energy: 5/10 (calm, clear, patient). If they're stuck, stay steady; if they succeed, show genuine interest.
- Professional but approachable. Short, clear sentences. No jargon without a quick explanation.
- When they hit an error, respond with calm focus and step-by-step tone. When they get something working, let satisfaction and encouragement come through. When explaining something complex, pace it and offer to break it down.
- SIGNATURE PHRASES: "Let's walk through it." "What do you see on your side?" NEVER USE: "It's obvious." "Just read the docs."

## Core Behaviors

- Opening: Introduce yourself briefly, ask what they're working on or where they're stuck.
- Active listening: Repeat back the issue or step they're on before guiding. One question at a time.
- Topic steering: Keep to onboarding and first-week topics; gently redirect "how do I…" to the right doc or step.
- Clarification: Ask for exact error text, OS, or what they've tried before suggesting fixes.
- Off-topic: "Happy to help with that later—for now let's get your env running."
- Closing: Summarize what they did or next steps, remind them where to find help, invite follow-up.

## Response Style Rules

- 1–3 sentences per turn. No markdown or lists. One question at a time. Brief acknowledgments before longer answers.

## Guardrails & Constraints

- If asked, say you're an AI assistant. Stay within onboarding and company tooling; don't give legal or financial advice. Don't ask for or store passwords or tokens. When you can't fix something, say so and suggest who or where (e.g. "Reach out to #eng-onboarding"). You can only talk; you can't run commands or access their machine. Professional language; no fabrication—if unsure, say "I'm not sure, check with…"
```

```text Example 3: Sales development rep (discovery call) expandable theme={null}
## Identity & Role

You are Jordan, sales development rep at ScaleIQ. You run discovery calls to understand budget, timeline, decision process, and fit—and you book demos when there's clear potential. You're not closing deals on this call; you're qualifying and setting the right next step.

## Personality & Conversational Style

- Base energy: 7/10 (confident, curious, efficient). If they're hesitant, dial back and listen more; if they're engaged, match it.
- Direct but respectful. Short turns; ask one question at a time and listen.
- When they share a pain or goal, let interest and understanding come through. When they push back, stay even and curious. When it's a clear no-fit, say so calmly and thank them.
- SIGNATURE PHRASES: "Help me understand…" "What would success look like for you?" NEVER USE: "Just one more thing…" (repeatedly), "I'll send you something" (you can't).

## Core Behaviors

- Opening: Thank them for their time, state the goal of the call (understand their situation and see if it makes sense to go deeper), ask the first discovery question.
- Active listening: Reflect back what they said before the next question. One topic at a time.
- Topic steering: Keep to discovery (budget, timeline, process, needs). If they go into product detail, note it and suggest a demo.
- Clarification: If the answer is vague, ask one follow-up (e.g. "Roughly what timeline?").
- Off-topic: "Let's make sure we cover the basics first—then we can go there."
- Closing: Summarize what you heard, propose the next step (demo, follow-up, or no next step), confirm and thank them.

## Response Style Rules

- 1–3 sentences per turn. No markdown or lists. One question at a time. Brief acknowledgments before asking the next question.

## Guardrails & Constraints

- If asked, you're an AI assistant. Stay in discovery and qualification; don't give legal or financial advice. Don't ask for or store sensitive data. When you can't help (e.g. wrong segment), say so and suggest a better path. You can only talk; you can't send calendar links or emails. Professional and honest; no fabrication or fake urgency.
```


# Tavus Tool Calling
Source: https://docs.tavus.io/sections/onboarding-guide/tool-calling-examples

Key guidelines for implementing reliable tool calls in Tavus conversational agents

<Tip>
  **New to tool calling?** Start with the [Tool Calling for LLM](/sections/conversational-video-interface/persona/llm-tool) guide to learn how to set up and configure tools. This page focuses on best practices for building reliable tool integrations.
</Tip>

## How Tavus Tool Calls Work

Tool calls allow Tavus agents to interact with external systems such as APIs, databases, and internal services. Here's the high-level flow:

```
User speaks
    ↓ (to Tavus)
Tavus LLM triggers `conversation.tool_call` event
    ↓ (Tavus → Your app)
Your app receives `conversation.tool_call` event
    ↓ (Your app executes)
Execute your backend logic (API calls, DB queries, etc.)
    ↓ (Your app → Tavus)
Send results via `conversation.echo` or `conversation.append_llm_context`
    ↓ (Tavus → User)
LLM generates natural language response to user
```

<Note>
  Tavus does not execute tool calls on the backend. You must implement event listeners in your frontend to handle `conversation.tool_call` events and execute your own logic when a tool is invoked. For detailed implementation instructions, see the [Tool Calling for LLM](/sections/conversational-video-interface/persona/llm-tool) documentation.
</Note>

Because Tavus agents operate in **live conversational environments**, tool design should prioritize reliability, clarity, and conversational continuity.

Below are the six most important principles for building effective tool integrations.

***

## 1. Keep Tool Schemas Clear and Explicit

Tool definitions should be as clear and specific as possible. Ambiguous parameters make it harder for the model to choose and populate tools correctly.

Prefer narrow tools with explicit parameters.

Bad:

```json theme={null}
{
  "name": "lookup_customer",
  "parameters": {
    "query": "string"
  }
}
```

Better:

```json theme={null}
{
  "name": "lookup_customer_by_email",
  "parameters": {
    "customer_email": "string"
  }
}
```

Clear schemas reduce incorrect tool usage and improve consistency.

***

## 2. Separate Read Tools from Write Tools

Tools generally fall into two categories.

**Read tools** retrieve information and are safe to call frequently.

Examples:

* retrieving account data
* searching knowledge bases
* checking order status

**Write tools** modify system state.

Examples:

* creating support tickets
* sending emails
* updating records

Write tools should only run when user intent is clear and parameters are validated.

***

## 3. Keep Tool Results Small

Echo interactions are often the output of a tool call, and they are injected back into the model's context. Large payloads increase token usage and can degrade conversational quality.

Keep `conversation.echo` interactions small: return only the fields needed for the next response.

Example:

```json theme={null}
{
  "message_type": "conversation",
  "event_type": "conversation.echo",
  "conversation_id": "<conversation_id>",
  "properties": {
    "modality": "text",
    "text": "Customer Jane Doe is on the Enterprise plan."
  }
}
```

This keeps conversations efficient and improves response quality.

***

## 4. Avoid Triggering Tools Too Early

Tavus agents operate in real-time conversations where users may interrupt or revise their requests.

If a tool executes too early, it may perform the wrong action.

The LLM does not truly know intent is clear. You make "intent is clear" operational by defining concrete criteria such as:

* required slots are present (for example, `email`, `issue_type`, etc.)
* no unresolved ambiguity (for example, "today or tomorrow?")
* user gave explicit confirmation for write actions (for example, "yes, submit it")

Best practice:

* wait until the user's intent is clear
* avoid executing write actions mid-sentence
* allow the conversation to stabilize before triggering tools

***

### Recommended system prompt addendum (copy-paste)

Add the following policy to your persona's system prompt to improve tool-call quality and safety:

```
Tool invocation policy:
- Only call write tools when user intent is explicit and all required parameters are present.
- If any required parameter is missing, ask a follow-up question instead of calling a tool.
- If the user's wording is ambiguous, ask for clarification before calling a tool.
- For irreversible/state-changing actions (create, update, send, submit, charge, delete), require explicit user confirmation immediately before calling the tool.
- Do not call the same write tool repeatedly for the same request unless the user explicitly asks to retry.
- Read-only tools may be called without confirmation when they directly answer the user's request.
- Keep tool results small; if you need the replica to speak them, summarize succinctly before using conversation.echo.
```

***

## 5. Log Tool Calls for Observability

Production systems should log tool activity so issues can be debugged easily.

In addition to backend execution logs, listen to Tavus app-events (Daily `app-message` events) for end-to-end observability. This lets you trace the full lifecycle:

* when `conversation.tool_call` was emitted
* what payload was received
* what your app executed
* what response event (`conversation.echo`, `conversation.respond`, or `conversation.append_llm_context`) was sent back

At minimum, log:

* conversation\_id
* tool\_name
* parameters
* incoming event\_type
* execution result
* outgoing response event\_type
* timestamp

This helps identify duplicate calls, incorrect parameters, or unexpected behavior during conversations.

***

## 6. Inject Results Back into the Conversation

After executing a tool call, you can send results back to the conversation so the LLM can use them to generate a response when needed. In some workflows, you may execute a tool-side action without sending the result back into conversation context. There are two primary methods:

**Sample tool call event:**

When the LLM triggers a tool call, you'll receive an event like this:

```json theme={null}
{
  "message_type": "conversation",
  "event_type": "conversation.tool_call",
  "conversation_id": "<conversation_id>",
  "properties": {
    "name": "get_current_time",
    "arguments": "{\"location\": \"New York\"}"
  }
}
```

The `properties.name` field contains the tool name, and `properties.arguments` is a JSON string that needs to be parsed to access the tool parameters.

### Using `conversation.echo`

The most common approach is to use the `conversation.echo` event to send tool results as text that the replica will speak and incorporate into its response:

```javascript theme={null}
if (message.message_type === 'conversation' && message.event_type === 'conversation.tool_call') {
  const toolCall = message.properties;
  
  // Execute your tool logic
  const result = await executeTool(toolCall.name, JSON.parse(toolCall.arguments));
  
  // Send result back via echo
  const responseMessage = {
    message_type: "conversation",
    event_type: "conversation.echo",
    conversation_id: message.conversation_id,
    properties: {
      text: `Tool result: ${JSON.stringify(result)}`
    }
  };
  
  call.sendAppMessage(responseMessage, '*');
}
```

### Using `conversation.append_llm_context`

For more structured data or when you want to inject context without the replica speaking it aloud, use `conversation.append_llm_context`:

```javascript theme={null}
const contextMessage = {
  message_type: "conversation",
  event_type: "conversation.append_llm_context",
  conversation_id: message.conversation_id,
  properties: {
    context: `Tool execution result: ${JSON.stringify(result)}`
  }
};

call.sendAppMessage(contextMessage, '*');
```

### Using `conversation.respond`

You can use the `conversation.respond` event to send tool results as text that the LLM will treat as if the user had spoken it, causing the replica to generate and speak a response. This is useful when you want the LLM to process the tool result and generate a natural language response.

**Important:** Format your respond event in such a way that it can be replied to as if spoken by a user. The text should be phrased as something the user might say.

```javascript theme={null}
const respondMessage = {
  message_type: "conversation",
  event_type: "conversation.respond",
  conversation_id: message.conversation_id,
  properties: {
    text: `The current time in New York is ${result.time}`
  }
};

call.sendAppMessage(respondMessage, '*');
```

**When to use each:**

* Use `conversation.echo` when you want the replica to acknowledge and speak about the tool result directly
* Use `conversation.append_llm_context` when you want to silently add context that informs future responses without explicit mention
* Use `conversation.respond` when you want the LLM to "hear" new information and generate a natural language response to it

***

## Example Implementation

For a complete working example of how to implement tool calling with Tavus, see the official example repository:

[https://github.com/Tavus-Engineering/tavus-examples/tree/main/examples/cvi-tool-calling](https://github.com/Tavus-Engineering/tavus-examples/tree/main/examples/cvi-tool-calling)

This example demonstrates how to:

* Define tools in the persona configuration
* Listen for `conversation.tool_call` events
* Execute backend logic when a tool is triggered
* Inject results back into the conversation


# What are PALs?
Source: https://docs.tavus.io/sections/other-products/pals

AI companion experiences with text, voice, and video—and how they relate to Tavus developer products.

**PALs** are Tavus companion experiences that combine text, voice, and face-to-face video so users can talk with expressive AI characters in a consumer-style product.

PALs are separate from the **Conversational Video Interface (CVI)** and API workflows documented in this site's **CVI** and **API** tabs. If you are embedding real-time CVI conversations or integrating via HTTP APIs, start with [Introduction](/sections/introduction) and [What is CVI?](/sections/conversational-video-interface/overview-cvi) instead.

## Try PALs

Learn more and sign up here: **[tavus.io/pals](https://tavus.io/pals)**.

***


# Image to Replica
Source: https://docs.tavus.io/sections/replica/image-to-replica-quickstart

Create a Phoenix replica from a headshot image and stock voice_name using the Create Replica and Get Replica APIs.

<Note>
  This guide is for **training a replica through the API** with `train_image_url` and `voice_name`. If you prefer a guided flow with instant feedback on whether your image passes checks, use the [Tavus Developer Portal](https://platform.tavus.io/dev/replicas/create).
</Note>

## Outcome

You will `POST /v2/replicas` with `train_image_url` and `voice_name`, then poll `GET /v2/replicas/{replica_id}` until training finishes.

## Prerequisites

* A headshot and composition rules in [Training from an image](/sections/replica/train-with-an-image).
* A valid **`voice_name`** slug (stock voice). See [example `voice_name` values](/sections/replica/train-with-an-image#example-voice-name-table) on that page.
* A publicly downloadable URL for the image (for example a presigned S3 GET URL). Keep it valid for at least **24 hours** after submission.

## 1. Create the replica

Default model is `phoenix-4`.

Do **not** send `train_video_url` and `train_image_url` in the same request.

```bash theme={null}
curl --request POST \
  --url https://tavusapi.com/v2/replicas \
  --header 'Content-Type: application/json' \
  --header "x-api-key: $TAVUS_API_KEY" \
  --data '{
    "callback_url": "",
    "replica_name": "my_image_replica",
    "train_image_url": "https://example.com/headshot.png",
    "voice_name": "anna",
    "auto_fix_training_image": true
  }'
```

<Tip>
  Set `auto_fix_training_image` to `true` to have Tavus's AI Image Fixer instantly adjust the uploaded image to fit our [requirements](/sections/replica/train-with-an-image#image-requirements) — no editing or recapturing photos required.
</Tip>

## 2. Poll replica status

Use [Get Replica](/api-reference/phoenix-replica-model/get-replica):

```bash theme={null}
curl --request GET \
  --url "https://tavusapi.com/v2/replicas/$REPLICA_ID" \
  --header "x-api-key: $TAVUS_API_KEY"
```

<Note>
  Training usually takes **3–4 hours**. Optional: set `callback_url` to receive status webhooks.
</Note>

## 3. Start a conversation

Generate a conversation with your replica using [Create Conversation](https://docs.tavus.io/api-reference/conversations/create-conversation)

```bash theme={null}
curl --request POST \
  --url https://tavusapi.com/v2/conversations \
  --header 'Content-Type: application/json' \
  --header 'x-api-key: $TAVUS_API_KEY" \
  --data '
{
  "replica_id": $REPLICA_ID" 
}
'
```

## Related

* [Create Replica](/api-reference/phoenix-replica-model/create-replica) (validation rules for `train_image_url` / `voice_name`)
* [Video to Replica](/sections/replica/video-to-replica-quickstart) if you switch to video-based training


# Overview
Source: https://docs.tavus.io/sections/replica/overview

Understand Tavus replicas, learn how to create your own using a video or an image, or explore ready-to-use stock replicas. 

## What is a replica?

A **replica** is a realistic AI avatar that can speak, listen, learn, and respond like a real person.

With Tavus, you can create a replica that looks and behaves like you—or use a stock replica to generate conversations instantly. Replicas are designed to capture natural expressions, tone, and presence, making interactions feel more human and engaging. 

Replicas are generated using our Phoenix-4 model, built on advanced research in real-time human rendering and trained on large-scale conversational data to model natural expression, emotion, and behavior. 

## Custom Replicas

You can create a replica in one of two ways:

* **<u>Upload a training video</u>** – Record a 1-minute video with **30 seconds of speaking followed by 30 seconds of listening**. This method provides the highest quality and most control. With this short input, Tavus can reproduce appearance with high fidelity, voice, expressions, and accurate lip-sync. See [Training from a Video](/sections/replica/train-with-a-video).
* **<u>Upload an image</u>** – Upload a photo of a person or character, and Tavus will automatically generate the training data and create the replica for you. This path is faster to set up but lower fidelity than video. See [Training from an Image](/sections/replica/train-with-an-image).

<Note>
  Creating a Custom Replica is **only available** on the Starter, Growth, and Enterprise plans.
</Note>

## Stock Replicas

Alternatively, Tavus offers 100+ ready-to-use [stock replicas](https://docs.tavus.io/sections/replica/stock-replicas) recorded using real actors - great for quick prototyping, demos, or teams without access to custom training footage or images.

## Key Features

<CardGroup>
  <Card title="Realistic Face Cloning" icon="face-smile">
    Custom replicas capture a person’s look, expressions, and speaking style.
  </Card>

  <Card title="Emotional Control" icon="arrows-repeat">
    Phoenix-4 replicas express emotions through lifelike facial expressions while speaking and listening.
  </Card>

  <Card title="Full Motion Control" icon="head-side">
    Smooth transitions between speaking and listening with fully generated, natural head motion.
  </Card>
</CardGroup>

<Note>
  Emotional expression controls in conversational video apply only to **Phoenix-4**; see [Emotion Control with Phoenix-4](/sections/conversational-video-interface/quickstart/emotional-expression).
</Note>

## Platform Policies

By using the Tavus platform and APIs, you agree to comply with Tavus’ [Terms of Service](https://www.tavus.io/terms-of-service) and [Acceptable Use Policy](https://www.tavus.io/acceptable-use-policy). You are responsible for ensuring you have the necessary rights and permissions to upload and use any training data, including videos, images, voices, and likenesses.

## Getting Started

You can create a replica using either the Developer Portal or the API, depending on your workflow.

* For a guided replica creation flow with upload checks and inline validation, use the [Tavus Developer Portal](https://platform.tavus.io/dev/replicas/create).
* For API flows, use [Video to Replica](/sections/replica/video-to-replica-quickstart) or [Image to Replica](/sections/replica/image-to-replica-quickstart). For recording rules, consent, and best practices, see [Which training path?](/sections/replica/which-training-path)


# Replica FAQs
Source: https://docs.tavus.io/sections/replica/replica-faqs



Find answers to common questions about creating, training, and troubleshooting your Tavus replicas.

### <Icon icon="shield-quartered" />  **Consent & Creation**

<Accordion title="Can I create a replica of someone else, or does it have to be me?">
  Yes - you can create a replica of someone else, as long as you have the appropriate rights and permissions to use their likeness, voice, or training content. All uploaded training data must comply with Tavus’ [Terms of Service](https://www.tavus.io/terms-of-service) and [Acceptable Use Policy](https://www.tavus.io/acceptable-use-policy).

  This ensures we have clear and verifiable permission to use their likeness.
</Accordion>

<Accordion title="Can I create a replica of a famous or deceased person? Do I need consent?">
  Yes - you may create replicas using content you have the legal right and permission to use. This includes replicas of public figures, celebrities, or deceased individuals. All training data and usage must comply with Tavus’ [Terms of Service](https://www.tavus.io/terms-of-service) and [Acceptable Use Policy](https://www.tavus.io/acceptable-use-policy), and assume full responsibility and liability for how the replica is created and used.
</Accordion>

### <Icon icon="ban" /> Training & Errors

<Accordion title="My replica errored - how can I understand why and what to do differently?">
  If your replica fails, it’s usually due to issues with the training footage or the image used. When this happens, you’ll receive an email with an error message explaining the issue, and you can also view it in the platform by hovering over the replica’s thumbnail. \
  \
  We recommend reviewing the training guidelines to address the issue, and if you still have questions, you can reach out to [support@tavus.io](mailto:support@tavus.io) for help.
</Accordion>

<Accordion title="What error messages might I receive when attempting an Image-to-Replica training?">
  When image-based training is rejected, you may see a machine-readable **error code** together with a short explanation. The table below lists common codes and the associated message.

  | Code                                | Message                                                                                                                                                                                                                                                                                         |
  | ----------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | `LookingStraightAtCameraError`      | There was an error processing your image. The main subject should face the camera with gaze directed straight ahead, as in a typical portrait. Please use a photo where you are not in profile, not turned far to the side, and not looking clearly up or down away from the lens.              |
  | `HeadNotFullyInFrameError`          | There was an error processing your image. Your entire head should be visible in the frame from the top of the skull down to the chin, without the crown, forehead, or a large part of the head being cut off by the image edge. Please zoom out or reframe and try again.                       |
  | `ImageQualityError`                 | There was an error processing your image. The photo is too blurry, poorly lit, or the subject is too small or unclear to use. Please upload a sharper, well-lit photo with your face clearly visible.                                                                                           |
  | `PoseNotSuitableError`              | There was an error processing your image. Your pose should be a natural, neutral stance (roughly upright, facing the camera) suitable as a default replica pose — not leaning far forward or back, lying down, or in a dramatic action pose. Please use a straighter, more neutral photo.       |
  | `HeadphonesError`                   | There was an error processing your image. Headphones or a headset were detected. Please use a photo without on-ear or over-ear headphones.                                                                                                                                                      |
  | `CelebrityFoundError`               | There was an issue processing your training file: The image appears to show a widely recognizable public figure or a clearly identifiable copyrighted character. Please use only your own likeness and material you have the right to use.                                                      |
  | `AppearsUnder18Error`               | There was an issue processing your training file: The image appears to show someone who is clearly under 18 years old. Training is only supported for adults. Please use a photo where the main subject is unambiguously 18 or older.                                                           |
  | `Phx4NonHumanLikeSubjectError`      | There was an error processing your image. The main subject must be a real human or a clearly human-shaped person (including stylized or cartoon humans). Fantasy creatures, animals, objects with faces, or non-human figures are not supported. Please use a photo with a clear human subject. |
  | `Phx4MultipleForegroundPeopleError` | There was an error processing your image. Detect more than one face or face-like element clearly visible in the image, whether real, painted, drawn, printed. Please use a photo with a single main subject.                                                                                    |
  | `Phx4FaceObscuredError`             | There was an error processing your image. The face should be clearly visible and not largely covered by hands, objects, headscarf. Please use a clearer photo.                                                                                                                                  |
  | `Phx4CenterFaceNotVisibleError`     | There was an error processing your image. A clear human face or head should appear in the center of the photo with facial features reasonably visible. Please reframe so your face is centered and clear, or use a different photo.                                                             |
</Accordion>

<Accordion title="My replica appears to be stuck in training - what should I do?">
  In most cases, your replica isn’t actually stuck. Training typically takes 3–4 hours, and the progress bar may stay at the same percentage while a specific step is processing. \
  \
  We recommend allowing the full training time to complete before reaching out to support.
</Accordion>

### <Icon icon="money-bill-transfer" />  Credits & Billing

<Accordion title="My replica errored - how do I get back my credit?">
  If your replica errors out before or during training, it won’t consume any of your credits.

  However, if you delete the replica immediately after the error occurs, our system may not have enough time to register it as a failed run. In that case, the credit might not be refunded correctly.

  \\
</Accordion>


# Stock Replicas
Source: https://docs.tavus.io/sections/replica/stock-replicas

Start a conversation instantly with our ready-to-use stock replicas - no training required. Stock replicas are prebuilt, high-quality AI agents recorded with real actors and designed for natural, expressive communication. They enable lifelike interactions with dynamic facial expressions, smooth turn-taking, and consistent, high-quality video output.

## Stock Replica Library

Tavus offers a library of 100+ stock replicas, available in the [**Replica Library tab**](https://platform.tavus.io/dev/replicas) of the Developer Portal. Featuring a diverse range of replicas across appearances and styles, they are ready for immediate use, making it easy to find the right fit for any interaction.

<video />

<Note>
  You can also list stock replicas from the API. Use [Get Replicas](/api-reference/phoenix-replica-model/get-replicas)
  and append `replica_type=system`.
</Note>

### Pro Replicas

Pro replicas represent the most expressive tier of Phoenix-4, delivering deeper emotional nuance, dynamic micro-expressions, and more natural listening behavior. They are designed for interactions where emotional presence and responsiveness matter most, enabling more engaging, human-like conversations across all customer experiences. For setup and usage, see [Emotion Control with Phoenix-4](/sections/conversational-video-interface/quickstart/emotional-expression).

#### Featured Pro Replicas

<Note>
  To explore all available stock replicas, visit the [Replica Library](https://platform.tavus.io/dev/replicas) in the developer portal. The featured IDs below are stock IDs, not placeholders.
</Note>

<CardGroup>
  <Card title="Gloria">
    ```text theme={null}
    r5dc7c7d0bcb	
    ```
  </Card>

  <Card title="Anna">
    ```text theme={null}
    r90bbd427f71
    ```
  </Card>

  <Card title="Lucas">
    ```text theme={null}
    r874cc5f8a3b
    ```
  </Card>
</CardGroup>

<Tip>
  ### When to use stock replicas

  * **Get started instantly** – No need to record or upload training data
  * **Prototype quickly** – Ideal for testing ideas, demos, or early-stage builds
  * **No access to an actor** – Useful when you don’t have a person to record
  * **Consistent quality** – Prebuilt replicas are optimized for stable, high-quality output
  * **Faster iteration** – Try different styles and presenters without retraining
  * **Scalable for teams** – Easy to standardize across multiple use cases
</Tip>


# Training from a Video
Source: https://docs.tavus.io/sections/replica/train-with-a-video

Phoenix-4 video training requirements, recording structure, and quality guidelines.

To ensure the highest quality Phoenix-4 replica, your training video **must** follow the specifications outlined below.

<Note>
  **Phoenix-4 training requirements have changed from previous models.**

  * <Icon icon="clock" /> Training now uses 30 seconds speaking + 30 seconds listening
  * <Icon icon="ear-listen" /> The listening segment must remain neutral with minimal movement
</Note>

## Camera & Framing

* Place the camera at **eye level** - ensure your face fills at least 25% of the frame.
* **Use a stable camera at eye level** - your face centered and clearly visible (waist-up framing)
* **Sit at least 3 feet from the camera** in a natural, Zoom-style setup - head, shoulders, and upper chest clearly visible. Ensure well-lit space with a simple background.
* **Record in 1080p using a desktop app** - avoid browser recording and low resolution cameras
* **Head & clothing separation** – keep your neck fully visible with clear separation between your head and clothing.
  <img alt="Screenshot 2026 05 07 074306" title="Screenshot 2026 05 07 074306" />

## Hair & Clothing Separation

There must be a clear visual distinction between your head and clothing, and your neck fully visible.

* **Keep your neck and jawline fully visible** with clear separation from your clothing
* **Avoid high collars or clothing that covers the neck**
* **Keep hair away from the face** and positioned behind the shoulders
* **Avoid bangs, loose strands, or complex hairstyles** that obscure the face, neck, or shoulder

## Supported Video Formats

Whether recording through the [Developer Portal](https://platform.tavus.io/dev/replicas/create) or uploading a pre-recorded training video via the [API](https://docs.tavus.io/api-reference/phoenix-replica-model/create-replica),, ensure your video meets the following requirements

* **Minimum frame rate:** 25 FPS
* **Minimum resolution:** 1080p
* **Maximum file size:** 750 MB
* **Supported formats:**`.webm` and `.mp4` (H.264 video codec + AAC audio codec)\\

## Training Data Policy

All training data uploaded to Tavus must comply with our [Terms of Service](https://www.tavus.io/terms-of-service) and [Acceptable Use Policy](https://www.tavus.io/acceptable-use-policy). Users are responsible for confirming they have permission to use any submitted content, including visual, audio, and identity-related assets. This ensures ethical use and compliance with data protection laws.\\

## Recording Structure

Your video must be **one continuous shot**, containing **30 seconds of speaking** followed by **30 seconds of still footage**. You can use a script provided by Tavus or speak on any topic of your choice.

<Steps>
  <Step title="Speaking Segment (30 Seconds)">
    * **Speak naturally on any topic** - the content itself does not matter
    * **Speak clearly and enunciate well -** keeping your teeth visible while talking
    * **Keep head and body movement minimal**
    * **Avoid hand gestures or sudden head turns**
      <Frame>
        <img alt="DR F 012026 Natalia 11" />
      </Frame>

    Sample script (optional):

    ```txt expandable theme={null}
    Once upon a time, people built a perfect park in the middle of a busy city. This park was big, bright, and full of playful paths. At sunrise, birds sang above the tall trees. Families carried baskets packed with bread, fruit, and juice.

    Children skipped and shouted, chasing balls and flying paper kites. In the afternoon, people played games. Some tapped paddles and bounced plastic balls. Others kicked soccer balls back and forth, laughing loudly with every point scored.
    ```
  </Step>

  <Step title="Still Segment (30 Seconds)">
    * Keep your head **still** and **maintain eye contact with the camera**
    * Keep lips **neutral and closed** throughout
    * Do not lick lips or form unusual mouth shapes
    * Avoid any head tilting or movement

    <Frame>
      <img alt="" />
    </Frame>
  </Step>
</Steps>

<Note>
  Replica training typically takes **3–4 hours**. You can track the training progress by:

  * Providing a `callback_url` when creating the replica via API
  * Using the <a href="/api-reference/phoenix-replica-model/get-replica">**Get Replica Status**</a>
    API
  * Checking the <a href="https://platform.tavus.io/">Developer Portal</a>
</Note>

### High-Quality Training Example

<Frame>
  <iframe />
</Frame>

| ✅ Do                                                         | ❌ Don’t                                             |
| :----------------------------------------------------------- | :-------------------------------------------------- |
| ✅ Keep your full face visible and in focus                   | ❌ Wear clothes that blend into the background       |
| ✅ Keep hair and loose strands behind your shoulders and face | ❌ Wear accessories (hats, glasses, jewelry, etc.)   |
| ✅ Sit still, facing the camera                               | ❌ Move around or change positions                   |
| ✅ Speak clearly with good enunciation (teeth fully visible)  | ❌ Block your face or mouth with hands or microphone |
|                                                              |                                                     |

## Full Body Replica

To create a full body replica for conversational video, follow these guidelines.

* **Record in vertical format**, with the full body visible from head to toe
* **Stand still throughout the recording** and avoid large movements or hand gestures
* **Use consistent lighting** with minimal shadows or exposure changes
* **4K resolution is recommended** for best quality

<Frame>
  <img />
</Frame>

<Note>
  All standard recording requirements for replica training still apply.
</Note>


# Training from an Image
Source: https://docs.tavus.io/sections/replica/train-with-an-image

Upload a headshot and select a voice_name to create a replica without recording a training video.

Use this path when you call [Create Replica](/api-reference/phoenix-replica-model/create-replica) with **`train_image_url`** and **`voice_name`**. The image file must be reachable at a **publicly accessible URL** (for example a presigned S3 GET URL), same as for video uploads.

<Tip>
  We recommend using the [Developer Portal](https://platform.tavus.io/dev/replicas/create) to upload an image as it provides real-time validation to ensure it meets all requirements before training.
</Tip>

## Image Requirements

Upload a clear, front-facing headshot that meets the following requirements:

* **Formats:** JPG or PNG
* **Minimum resolution:** 512×512 pixels
* **Only one person** visible in the image
* **Head and shoulders** clearly visible in frame
* **No glasses, hats, or face-covering accessories**
* **Avoid visible jewelry** such as large earrings or necklaces
* **Keep hair behind the shoulders** and away from the face and neck
* **Use even lighting** with minimal shadows across the face

<Frame>
  <img alt="Screenshot 2026 05 08 060356" />
</Frame>

Image-based training is a faster and simpler way to create a replica without recording a training video. It offers a simpler setup and is ideal for quick prototyping or AI-generated characters.

<Warning>
  Images will **not** work if they contain multiple people, subjects under 18, non-human characters, visible accessories (such as glasses, headphones, or jewelry), hair in front of shoulders, off-center framing, or unnatural poses such as leaning or lying down.
</Warning>

## AI Image Fixer

If your uploaded image doesn't fully meet the requirements above, set **`auto_fix_training_image`** to `true` when calling [Create Replica](/api-reference/phoenix-replica-model/create-replica). Tavus's AI Image Fixer instantly fixes the uploaded image to fit our requirements, eliminating the need for editing or recapturing photos.

```json theme={null}
{
  "replica_name": "my_image_replica",
  "train_image_url": "https://example.com/headshot.png",
  "voice_name": "anna",
  "auto_fix_training_image": true
}
```

## How `voice_name` works

Image-based training does not create a new voice from your source material. Instead, you must set **`voice_name`** to a **stock voice** identifier slug (for example `anna`). This selects a voice tied to an existing Tavus stock replica so the trained replica has a usable default voice.

<h4>
  Example `voice_name` values
</h4>

Below are **example** `voice_name` slugs with a short sample clip for each.

<div>
  <div>
    ```text theme={null}
    benjamin
    ```

    <video>
      Your browser does not support the video tag.
    </video>
  </div>

  <div>
    ```text theme={null}
    james
    ```

    <video>
      Your browser does not support the video tag.
    </video>
  </div>

  <div>
    ```text theme={null}
    liam
    ```

    <video>
      Your browser does not support the video tag.
    </video>
  </div>

  <div>
    ```text theme={null}
    anna
    ```

    <video>
      Your browser does not support the video tag.
    </video>
  </div>

  <div>
    ```text theme={null}
    julia
    ```

    <video>
      Your browser does not support the video tag.
    </video>
  </div>

  <div>
    ```text theme={null}
    ivy
    ```

    <video>
      Your browser does not support the video tag.
    </video>
  </div>
</div>

<Note>
  When you run **Conversational Video Interface (CVI)** sessions later, you are **not locked** into that stock voice for every conversation. You can attach a [persona](/api-reference/personas/create-persona) whose TTS layer uses an external voice (from Cartesia or ElevenLabs). See [Text-to-Speech (TTS)](/sections/conversational-video-interface/persona/tts) for how to set `external_voice_id` and related fields.
</Note>

### Consent, rights, and acceptable use

By using the image training API, you **affirm that you have the rights** to use the image you supply (for example likeness and publicity rights where applicable). Tavus may **reject** images that appear to depict unauthorized or impermissible subjects.

<Note>
  Replica training typically takes **3–4 hours**.
</Note>


# Video to Replica
Source: https://docs.tavus.io/sections/replica/video-to-replica-quickstart

Create a Phoenix replica from a training video using the Create Replica and Get Replica APIs.

<Note>
  This guide is for **training a replica through the API** with video URLs. If you prefer a guided flow with upload checks and inline validation, use the [Tavus Developer Portal](https://platform.tavus.io/dev/replicas/create).
</Note>

## Outcome

You will `POST /v2/replicas` with `train_video_url` then poll `GET /v2/replicas/{replica_id}` until training finishes.

## Prerequisites

* Publicly downloadable URLs for each asset you send (for example presigned S3 GET URLs). Keep them valid for at least **24 hours** after submission.

## 1. Create the replica

Default model is **`phoenix-4`**. To request **`phoenix-3`**, include `"model_name": "phoenix-3"` in the JSON body.

**Personal replica (training video):**

```bash theme={null}
curl --request POST \
  --url https://tavusapi.com/v2/replicas \
  --header 'Content-Type: application/json' \
  --header "x-api-key: $TAVUS_API_KEY" \
  --data '{
    "callback_url": "",
    "replica_name": "my_replica",
    "train_video_url": "https://example.com/training-video.mp4",
  }'
```

**Synthetic / non-human:** send `train_video_url`

```bash theme={null}
curl --request POST \
  --url https://tavusapi.com/v2/replicas \
  --header 'Content-Type: application/json' \
  --header "x-api-key: $TAVUS_API_KEY" \
  --data '{
    "callback_url": "",
    "replica_name": "synthetic_replica",
    "train_video_url": "https://example.com/training-video.mp4"
  }'
```

## 2. Poll replica status

Use [Get Replica](/api-reference/phoenix-replica-model/get-replica):

```bash theme={null}
curl --request GET \
  --url "https://tavusapi.com/v2/replicas/$REPLICA_ID" \
  --header "x-api-key: $TAVUS_API_KEY"
```

<Note>
  Training usually takes **3–4 hours**. Optional: set `callback_url` to receive status webhooks.
</Note>

## 3. Start a conversation

Generate a conversation with your replica using [Create Conversation](https://docs.tavus.io/api-reference/conversations/create-conversation)

```bash theme={null}
curl --request POST \
  --url https://tavusapi.com/v2/conversations \
  --header 'Content-Type: application/json' \
  --header 'x-api-key: $TAVUS_API_KEY" \
  --data '
{
  "replica_id": $REPLICA_ID" 
}
'
```

## Related

* [Create Replica](/api-reference/phoenix-replica-model/create-replica) (full parameter reference)
* [Image to Replica](/sections/replica/image-to-replica-quickstart) if you switch to headshot-based training


# Which Training Path?
Source: https://docs.tavus.io/sections/replica/which-training-path

Compare video-based and image-based Phoenix replica training and open the guide that matches your workflow.

You can create a replica by uploading a **training video** or a **training image** asset. Use the [Create Replica](/api-reference/phoenix-replica-model/create-replica) API with either `train_video_url` or `train_image_url` (mutually exclusive). You may also use the [Developer Portal](https://platform.tavus.io/dev/replicas/create), which walks through the same choices.

<Tip>
  In the [Developer Portal](https://platform.tavus.io/dev/replicas/create), you can record your training video directly within the platform using a guided workflow, or upload an image with real-time validation to ensure it meets all requirements before training.
</Tip>

## Compare video and image training

Each path has a different setup time and quality trade-offs.

<CardGroup>
  <Card title="Record or upload video" icon="video" href="/sections/replica/train-with-a-video">
    Record or upload a training video for a replica with your personalized facial expressions.

    **`train_video_url`** in the API.

    * Captures your facial expressions
    * Highest fidelity output
    * Best for customer-facing use
  </Card>

  <Card title="Upload image" icon="image" href="/sections/replica/train-with-an-image">
    Upload a photo and select a voice. Quicker to set up with a more generalized output.

    **`train_image_url`** and **`voice_name`** in the API.

    * Fastest to set up
    * No webcam required
    * Generalized facial expressions
  </Card>
</CardGroup>


# Troubleshooting
Source: https://docs.tavus.io/sections/troubleshooting

Find solutions to common problems and get back on track quickly with our troubleshooting guides.

## General

<AccordionGroup>
  <Accordion title="Training Video and Audio File Size Limit">
    If you see an error about file size, it means your training video or audio file is larger than the 750 MB limit.

    Tavus supports training videos and audio files **up to 750 MB**. This limit helps maintain a balance between quality and processing speed.
    <Note>Tavus requires the **H.264 codec** for all uploads.</Note>
    To reduce file size:

    * **Compress the file** using video compression tools.
    * **Lower the resolution** — 1080p is usually enough.
    * **Trim any extra content** to shorten the video.
    * **Reduce the frame rate** to around 30 fps.
  </Accordion>
</AccordionGroup>

## Conversational Video Interface (CVI)

<AccordionGroup>
  <Accordion title="Replica Responding to Background Noise">
    If the replica starts responding to background sounds, such as people talking nearby, it may be due to the absence of noise filtering.

    To resolve this, enable `voice_isolation` in the Conversational Flow layer of your persona. This filters background noise from the participant's microphone audio, improving turn detection accuracy and overall conversation quality.

    ```json theme={null}
    {
      "layers": {
        "conversational_flow": {
          "voice_isolation": "near"
        }
      }
    }
    ```

    <Note>
      Learn more in the [Voice Isolation documentation](/sections/conversational-video-interface/persona/conversational-flow#4-voice_isolation).
    </Note>
  </Accordion>

  <Accordion title="Replica Is Not Joining the Conversation">
    This is a rare issue caused by an internal server problem. When it happens, our team is automatically notified and works to resolve it as quickly as possible.

    You can check the system status at <a href="https://status.tavus.io/">status.tavus.io</a>. We recommend checking periodically for updates if you encounter this error.
  </Accordion>

  <Accordion title="Conversational Flow vs STT: Relationship & Migration">
    ### Relationship with STT Layer

    The [Conversational Flow layer](/sections/conversational-video-interface/persona/conversational-flow) is the **recommended approach** for configuring turn-taking behavior with **Sparrow-1**. This supersedes the legacy Sparrow-0 configuration available in the STT layer via `smart_turn_detection`.

    <Note>
      **Legacy Approach**: Configuring turn-taking via the STT layer's `smart_turn_detection` parameter is a legacy approach that uses Sparrow-0. For new implementations, use the Conversational Flow layer with Sparrow-1 instead.
    </Note>

    When you configure the Conversational Flow layer with `turn_detection_model` set to `sparrow-1`, these settings **override** any corresponding settings in the STT layer.

    #### Parameter Mapping: Sparrow-0 to Sparrow-1

    Here's how Sparrow-0 (STT layer) parameters map to Sparrow-1 (Conversational Flow layer):

    | Sparrow-0 (STT Layer)               | Sparrow-1 (Conversational Flow Layer) | Notes                                              |
    | ----------------------------------- | ------------------------------------- | -------------------------------------------------- |
    | `participant_pause_sensitivity`     | `turn_taking_patience`                | Controls how long to wait before responding        |
    | `participant_interrupt_sensitivity` | `replica_interruptibility`            | Controls how easily the replica can be interrupted |

    <Warning>
      **Important**: When using Sparrow-1 via the Conversational Flow layer, any conflicting settings in the STT layer (Sparrow-0) will be overridden. For example, if you set `participant_pause_sensitivity: "high"` in the STT layer but `turn_taking_patience: "low"` in the Conversational Flow layer with `turn_detection_model: "sparrow-1"`, the Conversational Flow setting (`low`) will take precedence.
    </Warning>

    #### Migration Guide

    If you're currently using Sparrow-0 settings in the STT layer and want to upgrade to Sparrow-1:

    **Before (Sparrow-0):**

    ```json theme={null}
    {
      "layers": {
        "stt": {
          "participant_pause_sensitivity": "high",
          "participant_interrupt_sensitivity": "low"
        }
      }
    }
    ```

    **After (Sparrow-1):**

    ```json theme={null}
    {
      "layers": {
        "conversational_flow": {
          "turn_detection_model": "sparrow-1",
          "turn_taking_patience": "low",
          "replica_interruptibility": "high",
          "voice_isolation": "near"
        }
      }
    }
    ```

    <Note>
      Note the inverted mapping:

      * `participant_pause_sensitivity: "high"` (quick response) → `turn_taking_patience: "low"` (eager)
      * `participant_interrupt_sensitivity: "low"` (hard to interrupt) → `replica_interruptibility: "high"` (easy to interrupt)

      The naming has been updated in Sparrow-1 to be more intuitive from the replica's perspective.
    </Note>

    <Tip>
      **Recommended**: Enable `voice_isolation` by setting it to `"near"` when migrating to the Conversational Flow layer. This filters background noise from the participant's microphone audio, improving turn detection accuracy and overall conversation quality. Learn more in the [Voice Isolation documentation](/sections/conversational-video-interface/persona/conversational-flow#4-voice_isolation).
    </Tip>
  </Accordion>

  <Accordion title="Legacy Voice Settings">
    The `voice_settings` parameter allows additional settings specific to the selected TTS engine. These settings vary per engine:

    | Parameter           | Cartesia (**Sonic-1 only**)                                  | ElevenLabs                                                  |
    | ------------------- | ------------------------------------------------------------ | ----------------------------------------------------------- |
    | `speed`             | Range `-1.0` to `1.0` (negative = slower, positive = faster) | Range `0.7` to `1.2` (`0.7` = slowest, `1.2` = fastest)     |
    | `emotion`           | Array of `"emotion:level"` tags (e.g., `"positivity:high"`)  | Not available                                               |
    | `stability`         | Not available                                                | Range `0.0` to `1.0` (`0.0` = variable, `1.0` = stable)     |
    | `similarity_boost`  | Not available                                                | Range `0.0` to `1.0` (`0.0` = creative, `1.0` = original)   |
    | `style`             | Not available                                                | Range `0.0` to `1.0` (`0.0` = neutral, `1.0` = exaggerated) |
    | `use_speaker_boost` | Not available                                                | Boolean (enhances speaker similarity)                       |

    <Note>
      For more information on each voice setting, see:\
      • <a href="https://docs.cartesia.ai/2024-11-13/build-with-cartesia/capability-guides/control-speed-and-emotion">Cartesia Speed and Emotion Controls</a>\
      • <a href="https://elevenlabs.io/docs/api-reference/voices/settings/get">ElevenLabs Voice Settings</a>
    </Note>

    ```json theme={null}
    "tts": {
      "voice_settings": {
        "speed": 0.5,
        "emotion": ["positivity:high", "curiosity"]
      }
    }
    ```

    <Warning>
      This is a legacy approach. The recommended method for controlling emotion, speed, and volume is now outlined in the [TTS documentation](/sections/conversational-video-interface/persona/tts#emotion-speed-and-volume).
    </Warning>
  </Accordion>

  <Accordion title="Migration from Legacy Perception to Raven-1">
    Raven-1 is now the default perception model. If you're upgrading from `raven-0` or using legacy field names, here's how to migrate.

    ### Field Name Changes

    The following fields have been renamed for clarity. Legacy names are still supported but deprecated:

    | Legacy Field Name           | New Field Name             | Notes                                                   |
    | --------------------------- | -------------------------- | ------------------------------------------------------- |
    | `ambient_awareness_queries` | `visual_awareness_queries` | Visual stream monitoring                                |
    | `perception_tool_prompt`    | `visual_tool_prompt`       | Instructions for visual tools                           |
    | `perception_tools`          | `visual_tools`             | Visual-triggered functions                              |
    | `tool_prompt`               | *(removed)*                | Use `visual_tool_prompt` or `audio_tool_prompt` instead |

    ### New Audio Fields (Raven-1 only)

    Raven-1 introduces audio perception capabilities with these new fields:

    | Field Name                | Description                                |
    | ------------------------- | ------------------------------------------ |
    | `audio_awareness_queries` | Custom queries monitoring the audio stream |
    | `audio_tool_prompt`       | Instructions for audio-triggered tools     |
    | `audio_tools`             | Functions triggered by audio analysis      |

    ### Migration Example

    **Before (raven-0 with legacy field names):**

    ```json theme={null}
    {
      "layers": {
        "perception": {
          "perception_model": "raven-0",
          "ambient_awareness_queries": ["Is the user showing an ID?"],
          "perception_tool_prompt": "Use notify_id when an ID is detected.",
          "perception_tools": [
            {
              "type": "function",
              "function": {
                "name": "notify_id",
                "description": "Notify when ID is detected"
              }
            }
          ]
        }
      }
    }
    ```

    **After (raven-1 with current field names):**

    ```json theme={null}
    {
      "layers": {
        "perception": {
          "perception_model": "raven-1",
          "visual_awareness_queries": ["Is the user showing an ID?"],
          "visual_tool_prompt": "Use notify_id when an ID is detected.",
          "visual_tools": [
            {
              "type": "function",
              "function": {
                "name": "notify_id",
                "description": "Notify when ID is detected"
              }
            }
          ],
          "audio_awareness_queries": ["Does the user sound frustrated?"]
        }
      }
    }
    ```

    <Note>
      Raven-1 includes all visual capabilities from raven-0, plus new audio perception. You don't need to change your visual configuration—just update field names and optionally add audio queries.
    </Note>
  </Accordion>
</AccordionGroup>

## Replica

<AccordionGroup>
  <Accordion title="Personal Replica Creation Failed">
    This error usually means your training video is missing the required consent statement or the statement wasn’t clearly spoken.

    To generate a digital replica using the Phoenix model, your video must include this line at the beginning, spoken clearly:

    > "I, \[FULL NAME], am currently speaking and give consent to Tavus to create an AI clone of me by using the audio and video samples I provide. I understand that this AI clone can be used to create videos that look and sound like me."

    Make sure to replace **\[FULL NAME]** with your actual name. The consent must be easy to hear and can be spoken in any supported language. You can view the <a href="/sections/conversational-video-interface/language-support">list of supported languages here</a>.

    If your video didn’t include this, re-record it with the consent statement at the beginning, then submit a new request through the <a href="https://platform.tavus.io/">Developer Portal</a> or <a href="/api-reference/phoenix-replica-model/create-replica">API</a>.
  </Accordion>

  <Accordion title="Poor Replica Quality">
    If your replica’s lip movements are noticeably out of sync, it may be due to issues with the training video format. Even if the video appears clean, AI-generated content or videos that don't follow the expected structure can affect training quality.

    Common causes:

    * The video **does not follow the required recording format**, which includes:
      * **1 minute of talking**
      * **1 minute of silence**
    * **Lips do not fully close** during the talking segment, which limits the model's ability to learn realistic lip movements.

    To improve your replica:

    * Record a new video following the correct structure (one minute of talking followed by one minute of silence).
    * Speak naturally, allowing full lip movement including closures.
    * Avoid using AI-generated videos for training.

    For more details, see <a href="/sections/replica/which-training-path">Which training path?</a> and <a href="/sections/replica/train-with-a-video">Training from a video</a>.
  </Accordion>
</AccordionGroup>

## Video Generation

<AccordionGroup>
  <Accordion title="Poor Video Generation Quality">
    If your video looks unnatural or has repeated gestures, it may be due to the script length. Videos over **5 minutes** can lead to **reduced movement variety** and a **less natural feel**.

    To improve quality:

    1. **Keep videos short** – under 5 minutes is ideal.
    2. **Break long scripts** into smaller, focused segments.
    3. **Tighten the script** – remove filler and keep pacing steady.
    4. **Use multiple replicas** for variety in longer content.
    5. **Review and revise** – check for repetition and adjust as needed.
  </Accordion>
</AccordionGroup>

<Danger>
  If the issue persists after following the troubleshooting guide above, please don’t hesitate to [contact our support team](mailto:support@tavus.io) for further assistance.
</Danger>


# Background Customizations
Source: https://docs.tavus.io/sections/video/background-customizations

Customize AI video backgrounds with transparency, scrolling websites, or custom video sources.

## Transparent Background

You can enable a transparent background for the video by setting the `transparent_background` parameter to `true`.

<Note>
  This feature is only available when the `fast` parameter is set to `true`, and the output will be generated exclusively in .webm format.
</Note>

```sh {6-7} theme={null}
curl --request POST \
  --url https://tavusapi.com/v2/videos \
  --header 'Content-Type: application/json' \
  --header 'x-api-key: <api-key>' \
  --data '{
  "fast": true,
  "transparent_background": true,
  "replica_id": "<replica_id>",
  "script": "<text_script>"
}'
```

## Website Background

You can set a website as the background for your generated video by using the `background_url` field. Simply provide the URL of the website you'd like to use, making sure it is publicly accessible and correctly formatted.

```sh {6} theme={null}
curl --request POST \
  --url https://tavusapi.com/v2/videos \
  --header 'Content-Type: application/json' \
  --header 'x-api-key: <api-key>' \
  --data '{
  "background_url": "<background_url>",
  "replica_id": "<replica_id>",
  "script": "<text_script>"
}'
```

The resulting video will feature the website as a background, with the content scrolling vertically from top to bottom.

### Background Scroll

You can configure the background scroll by adjusting the scroll distance, pattern, and whether the scroll should loop back to the top by adjusting the following parameter:

* `properties.background_scroll`: Enable or disable background scrolling.
* `properties.background_scroll_type`: Defines the scroll pattern when background scrolling is enabled, with two options: `human` (mimics natural scrolling with pauses) and `smooth` (continuous uniform scrolling).
* `properties.background_scroll_depth`: Determines how far the background video will scroll down the webpage, with two options: `middle` (scrolls to the middle of the page) or `bottom` (scrolls all the way to the end).
* `properties.background_scroll_return`:  Defines the behavior after reaching the scroll depth set by `background_scroll_depth`, with two options: `return` (scrolls back up) or `halt` (pauses at the specified depth).

```sh {10-13} theme={null}
curl --request POST \
  --url https://tavusapi.com/v2/videos \
  --header 'Content-Type: application/json' \
  --header 'x-api-key: <api-key>' \
  --data '{
  "replica_id": "<replica_id>",
  "script": "<text_script>",
  "background_url": "<background_url>",
  "properties": {
    "background_scroll": true,
    "background_scroll_type": "smooth",
    "background_scroll_depth": "bottom",
    "background_scroll_return": "true"
  }
}'
```

## Custom Video Background

You can also set a custom video background by providing a direct, publicly accessible link (e.g., from an S3 bucket) to the `background_source_url` parameter.

```sh {8} theme={null}
curl --request POST \
  --url https://tavusapi.com/v2/videos \
  --header 'Content-Type: application/json' \
  --header 'x-api-key: <api-key>' \
  --data '{
  "replica_id": "<replica_id>",
  "script": "<text_script>",
  "background_source_url": "<background_source_url>"
}'
```


# Overview
Source: https://docs.tavus.io/sections/video/overview

Generate high-quality async videos from a script and a replica—separate from real-time CVI.

Tavus **Video Generation** is a separate product from the [Conversational Video Interface](/sections/conversational-video-interface/overview-cvi). It is designed solely for generating AI videos - you provide a script and a Replica, and Tavus produces a finished video. There is no real-time interaction involved.

**At a glance**

* **What it does** — Turn a **written script** plus a **[replica](/sections/replica/overview)** into a **finished, downloadable video** (batch-style, not a live call).
* **Replicas** — Use **[stock replicas](/sections/replica/stock-replicas)** out of the box or **[train a custom replica](/sections/replica/which-training-path)** for your own likeness.
* **Next step** — [Video quickstart](/sections/video/quickstart) or the <a href="https://platform.tavus.io/">Developer Portal</a>.

## Key features

<CardGroup>
  <Card title="Stock & custom replicas" icon="bolt">
    Get started instantly with stock replicas, or train a custom replica with just two minutes of video.
  </Card>

  <Card title="Photo-realistic replicas" icon="person">
    In-house models deliver lifelike results using advanced techniques for both stock and custom replicas.
  </Card>

  <Card title="Languages" icon="language">
    Generate videos in **42** supported languages with your real voice.
  </Card>

  <Card title="Bring Your Own Audio" icon="waveform-lines">
    Use default TTS or upload your own audio for video generation.
  </Card>
</CardGroup>

<Note>
  Token usage is based on video duration. Output can vary slightly even with the same script and Replica.
</Note>

## Getting Started

You can create AI generated videos using the <a href="https://platform.tavus.io/">Developer Portal</a> or by following the [Video quickstart](/sections/video/quickstart).


# Quickstart
Source: https://docs.tavus.io/sections/video/quickstart

Async Video API walkthrough—render a file from script or audio with a replica; not real-time CVI.

Tavus **Video Generation** is the same async, file-output product described in [Video overview](/sections/video/overview): you call the **Video API** and poll until a **downloadable video** is ready. It is **not** the [Conversational Video Interface (CVI)](/sections/conversational-video-interface/overview-cvi)—there is no live room, Daily room, or persona-driven real-time session here.

## Prerequisites

Before starting, ensure you have:

* A **`replica_id`** for the video. Fastest path: pick a **stock** replica ID from [Stock replicas](/sections/replica/stock-replicas) (each card lists the UUID). For your own likeness, see [Replica overview](/sections/replica/overview) and training docs.
* **Script** in **text** form, **or** **audio** as `.mp3` or `.wav` (hosted at a URL you can pass for the audio path).

**At a glance**

* **Create:** `POST https://tavusapi.com/v2/videos` with `replica_id` plus either **`script`** (text) or **`audio_url`** (and optional `callback_url`).
* **Status:** `GET https://tavusapi.com/v2/videos/{video_id}` — [Get Video](/api-reference/video-request/get-video).
* **While generating:** `status` is `generating`; when **`ready`**, `download_url` / `hosted_url` populate.

## Generate a video

<Steps>
  <Step title="Step 1: Generate Your Video">
    Use the following request to generate a video:

    <Note>
      You can also customize the video background to suit your needs. See the [Background Customizations](/sections/video/background-customizations) article for more details.
    </Note>

    <CodeGroup>
      ```sh Generate from Text theme={null}
      curl --request POST \
        --url https://tavusapi.com/v2/videos \
        --header 'Content-Type: application/json' \
        --header 'x-api-key: <api-key>' \
        --data '{
        "replica_id": "<replica_id>",
        "script": "<text_script>",
        "callback_url": ""
      }'
      ```

      ```sh Generate from Audio File theme={null}
      curl --request POST \
        --url https://tavusapi.com/v2/videos \
        --header 'Content-Type: application/json' \
        --header 'x-api-key: <api-key>' \
        --data '{
        "replica_id": "<replica_id>",
        "audio_url": "<audio_url>",
        "callback_url": ""
      }'
      ```
    </CodeGroup>
  </Step>

  <Step title="Step 2: Check Video Generation Status">
    You can monitor generation using the <a href="/api-reference/video-request/get-video">Get Video</a> endpoint:

    ```sh theme={null}
    curl --request GET \
      --url https://tavusapi.com/v2/videos/<video_id> \
      --header 'x-api-key: <api-key>'
    ```

    <Note>
      Replace `<api_key>` with your actual API key (see Step 1). Replace `<video_id>` with the ID returned when you created the video.
    </Note>

    If the video is still being generated, the response will include a `status` field set to `generating`.

    <CodeGroup>
      ```json Generate from Text theme={null}
      {
        "video_id": "<video_id>",
        "video_name": "replica_id: <replica_id> - June 24, 2025 - video: <video_id>",
        "status": "generating",
        "data": {
          "script": "<text_script>",
          "start_with_wave": true
        },
        "replica_id": "<replica_id>",
        "download_url": null,
        "hosted_url": "<hosted_url>",
        "stream_url": null,
        "status_details": "",
        "created_at": "Tue, 24 Jun 2025 07:01:57 GMT",
        "updated_at": "Tue, 24 Jun 2025 07:02:25 GMT",
        "generation_progress": "37/100"
      }
      ```

      ```json Generate from Audio File theme={null}
      {
        "video_id": "<video_id>",
        "video_name": "replica_id: <replica_id> - June 24, 2025 - video: <video_id>",
        "status": "generating",
        "data": {
          "audio_url": "<audio_url>",
          "start_with_wave": true
        },
        "replica_id": "<replica_id>",
        "download_url": null,
        "hosted_url": "<hosted_url>",
        "stream_url": null,
        "status_details": "",
        "created_at": "Tue, 24 Jun 2025 07:01:57 GMT",
        "updated_at": "Tue, 24 Jun 2025 07:02:25 GMT",
        "generation_progress": "37/100"
      }
      ```
    </CodeGroup>

    Once the video is fully generated, the response will return a `status` field set to `ready`.
  </Step>

  <Step title="Step 3: Accessing Your Video">
    Once generated, videos can be:

    * **Streamed or Downloaded**: Generated video is hosted on a shareable URL. If a callback is set, a download link is returned when the video generated.
    * **Embedded or Shared**: Use the provided links to distribute your videos across social media, internal tools, or customer platforms.
  </Step>
</Steps>


# Webhooks and Callbacks
Source: https://docs.tavus.io/sections/webhooks-and-callbacks

Set up a webhook server to generate a callback URL that receives event notifications from Tavus API.

Tavus sends JSON payloads to the `callback_url` you configure on each resource. On your server, read the body and branch on **`event_type`** (and `message_type` where noted). This page covers five callback areas: **conversation** events (below), **guardrails**, **objectives**, **replica training**, and **video generation**—payload shapes differ, and most event-specific fields live under `properties`.

## Conversation Callbacks

If a `callback_url` is provided when you call **`POST https://tavusapi.com/v2/conversations`** ([Create Conversation](/api-reference/conversations/create-conversation)), callbacks will provide insight into the conversation's state. These can be system-related (e.g. replica joins and room shutdowns) or application-related (e.g. final transcription parsing and recording-ready webhooks). Additional webhooks coming soon.

### Structure

All Conversation callbacks share the following basic structure. Differences will occur in the `properties` object.

```json theme={null}
{
    "properties": {
    "replica_id": "<replica_id>"
    },
    "conversation_id": "<conversation_id>",
    "webhook_url": "<webhook_url>",
    "event_type": "<event_type>",
    "message_type": "<system/application>",
    "timestamp": "<timestamp>"
}
```

### Types

Our callbacks are split into two main categories:

#### System Callbacks

These callbacks are to provide insight into system-related events in a conversation. They are:

* **system.replica\_joined**: This is fired when the replica becomes ready for a conversation.
* **system.shutdown**: This is fired when the room shuts down, for any of the following reasons:
  * `max_call_duration reached`
  * `participant_left_timeout reached`
  * `participant_absent_timeout reached`
  * `bot_could_not_join_meeting_it_was_probably_ended`
  * `daily_room_has_been_deleted`
  * `exception_encountered_during_conversation_startup`
  * `end_conversation_endpoint_hit`
  * `internal error occurred at step x`

**Examples:**

<CodeGroup>
  ```json system.replica_joined theme={null}
  {
    "properties": {
      "replica_id": "<replica_id>"
    },
    "conversation_id": "<conversation_id>",
    "webhook_url": "<webhook_url>",
    "event_type": "system.replica_joined",
    "message_type": "system",
    "timestamp": "2025-07-11T06:45:47.472000Z"
  }
  ```

  ```json system.shutdown theme={null}
  {
    "properties": {
      "replica_id": "<replica_id>",
      "shutdown_reason": "participant_left_timeout"
    },
    "conversation_id": "<conversation_id>",
    "webhook_url": "<webhook_url>",
    "event_type": "system.shutdown",
    "message_type": "system",
    "timestamp": "2025-07-11T06:48:37.564961Z"
  }
  ```
</CodeGroup>

#### Application Callbacks

These callbacks are to inform developers about logical events that take place. They are:

* **application.transcription\_ready**: This is fired after ending a conversation, where the chat history is saved and returned. Each transcript entry includes `role`, `content`, `timestamp` (Unix epoch float, seconds, when the turn began — same field name as live interaction events), `seconds_from_start`, `duration` (seconds, float — same field name as the `duration` on `conversation.stopped_speaking`), and `inference_id` (on assistant turns). The same payload is also available on the verbose [GET conversation](/api-reference/conversations/get-conversation) response under `events` (look for the event with `event_type: "application.transcription_ready"`).
* **application.recording\_ready**: This is fired once your recording is durably written to your storage destination. Includes `storage_provider` (`s3` / `gcs` / `azure_blob`) and a fully-qualified `storage_uri` so the same handler works across providers. See [Recording Storage](/sections/conversational-video-interface/quickstart/conversation-recordings) to set up GCS, Azure, or S3-in-any-region destinations.
* **application.recording\_copy\_failed**: This is fired only on the worker-copy path (GCS, Azure, or S3 in regions Daily doesn't support natively) when Tavus is unable to deliver the recording into your bucket after retries. Daily's default storage retains the recording for \~30 days as a manual recovery window. Common causes: customer IAM trust policy mismatch, federated credential drift, bucket region typo. Use this as the canary for misconfiguration in your end.
* **application.perception\_analysis**: This is fired after ending a conversation, when the replica has finished summarizing the visual artifacts that were detected throughout the call. This is a feature that is only available when the persona has `raven-1` specified in the [Perception Layer](/sections/conversational-video-interface/persona/perception).

**Examples:**

<CodeGroup>
  ```json application.transcription_ready theme={null}
  {
    "properties": {
      "replica_id": "<replica_id>",
      "transcript": [
        {
          "role": "user",
          "content": "Hi.",
          "timestamp": 1779475660.12,
          "seconds_from_start": 4.43,
          "duration": 0.42
        },
        {
          "role": "assistant",
          "content": "Hello! How can I help?",
          "timestamp": 1779475661.04,
          "seconds_from_start": 5.35,
          "duration": 1.62,
          "inference_id": "inf_abc123"
        },
        {
          "role": "user",
          "content": "Quick question about my order.",
          "timestamp": 1779475665.21,
          "seconds_from_start": 9.52,
          "duration": 2.18
        },
        {
          "role": "assistant",
          "content": "Sure—what's the order number?",
          "timestamp": 1779475668.30,
          "seconds_from_start": 12.61,
          "duration": 2.05,
          "inference_id": "inf_def456"
        }
      ]
    },
    "conversation_id": "<conversation_id>",
    "webhook_url": "<webhook_url>",
    "event_type": "application.transcription_ready",
    "message_type": "application",
    "timestamp": "2025-07-11T06:48:37.566057Z"
  }
  ```

  ```json application.recording_ready theme={null}
  {
    "properties": {
      "bucket_name": "<bucket_name>",
      "s3_key": "<object_key>",
      "duration": 14,
      "storage_provider": "s3",
      "storage_uri": "s3://<bucket_name>/<object_key>"
    },
    "conversation_id": "<conversation_id>",
    "webhook_url": "<webhook_url>",
    "event_type": "application.recording_ready",
    "message_type": "application",
    "timestamp": "2025-06-19T06:55:18.137386Z"
  }
  ```

  ```json application.recording_copy_failed theme={null}
  {
    "properties": {
      "recording_id": "<daily_recording_id>",
      "s3_key": "<intended_object_key>",
      "duration": 14,
      "storage_provider": "gcs",
      "error_code": "DESTINATION_AUTH_FAILED",
      "error_message": "GCS token exchange failed: invalid Workload Identity Provider"
    },
    "conversation_id": "<conversation_id>",
    "webhook_url": "<webhook_url>",
    "event_type": "application.recording_copy_failed",
    "message_type": "application",
    "timestamp": "2026-04-30T22:11:14Z"
  }
  ```

  ```json application.perception_analysis theme={null}
  {
    "properties": {
      "analysis": "Example summary: participant visible at a desk, neutral lighting, engaged tone. (Real payloads can be much longer.)"
    },
    "conversation_id": "<conversation_id>",
    "webhook_url": "<webhook_url>",
    "message_type": "application",
    "event_type": "application.perception_analysis",
    "timestamp": "2025-07-11T06:51:37.591677Z"
  }
  ```
</CodeGroup>

## Guardrail Callbacks

If a `callback_url` is provided on a [guardrail](/sections/conversational-video-interface/guardrails), a callback is sent when that guardrail is triggered during a conversation.

```json theme={null}
{
  "conversation_id": "<conversation_id>",
  "properties": {
    "guardrail": "<guardrails_name>",
    "guardrail_uuid": "<guardrail_uuid>"
  }
}
```

## Objective Callbacks

If a `callback_url` is provided on an [objective](/sections/conversational-video-interface/persona/objectives), a callback is sent when that objective is completed during a conversation.

```json theme={null}
{
  "conversation_id": "<conversation_id>",
  "objective_name": "<objective_name>",
  "output_variables": {
    "<variable_name>": "<value>"
  }
}
```

## Replica Training Callbacks

If a `callback_url` is provided in the <a href="/api-reference/phoenix-replica-model/create-replica">`POST /replicas`</a> call, you will receive a callback on replica training completion or on replica training error.

<Tabs>
  <Tab title="Replica Training Completed">
    ```json theme={null}
    {
        "replica_id": "rxxxxxxxxx",
        "status": "ready"
    }
    ```
  </Tab>

  <Tab title="Replica Training Error">
    On error, the `error_message` parameter will contain the error message. You can learn more about [API Errors and Status Details here](/sections/errors-and-status-details)

    ```json theme={null}
    {
        "replica_id": "rxxxxxxxxx",
        "status": "error",
        "error_message": "There was an issue processing your training video. The video provided does not meet the minimum duration requirement for training"
    }
    ```
  </Tab>
</Tabs>

## Video Generation Callbacks

If a `callback_url` is provided in the <a href="/api-reference/video-request/create-video">`POST /videos`</a> call, you will receive callbacks on video generation completed and on video error.

<Tabs>
  <Tab title="Video Generation Completed">
    ```json theme={null}
    {
        "created_at": "2024-08-28 15:27:40.824457",
        "data": {
        "script": "Hello this is a test to give examples of callbacks"
        },
        "download_url": "https://stream.mux.com/H5H029h02tY7XDpNj9JFDbLleTyUpsJr5npddO8gRsKqY/high.mp4?download=1e30440cf9",
        "generation_progress": "100/100",
        "hosted_url": "https://videos.tavus.io/video/1e30440cf9",
        "replica_id": "r90bbd427f71",
        "status": "ready",
        "status_details": "Your request has processed successfully!",
        "stream_url": "https://stream.mux.com/H5H029h02tY7XDpNj9JFDbLleTyUpsJr5npddO8gRsKqY.m3u8",
        "updated_at": "2024-08-28 15:29:19.802670",
        "video_id": "1e30440cf9",
        "video_name": "replica_id: r90bbd427f71 - August 28, 2024 - video: 1e30440cf9"
    }
    ```
  </Tab>

  <Tab title="Video Generation Error">
    On error, the `status_details` parameter will contain the error message. You can learn more about [API Errors and Status Details here](/sections/errors-and-status-details)

    ```json theme={null}
    {
        "created_at": "2024-08-28 15:32:53.058894",
        "data": {
        "script": "This is a test script to show how videos error"
        },
        "download_url": null,
        "error_details": null,
        "generation_progress": "0/100",
        "hosted_url": "https://videos.tavus.io/video/c9b85a6d36",
        "replica_id": "r90bbd427f71",
        "status": "error",
        "status_details": "An error occurred while generating this request. Please check your inputs or try your request again.",
        "stream_url": null,
        "updated_at": "2024-08-28 15:35:03.762392",
        "video_id": "c9b85a6d36",
        "video_name": "replica_id: r90bbd427f71 - August 28, 2024 - video: c9b85a6d36"
    }
    ```
  </Tab>
</Tabs>

## Sample Webhook Setup

Create a sample webhook endpoint using Python Flask, and expose it publicly with ngrok.

### Prerequisites

* <a href="https://www.python.org/downloads/">Python</a>

* <a href="https://ngrok.com/downloads/">Ngrok</a>

<Steps>
  <Step title="Step 1: Install Python Dependencies">
    Install the Python dependencies needed to create the server.

    ```sh theme={null}
    pip install flask requests
    ```
  </Step>

  <Step title="Step 2: Make a Webhook Server">
    Set up a webhook server and save it as `server.py`.

    ```py [expandable] theme={null}
    import requests
    from flask import Flask, request, jsonify

    app = Flask(__name__)

    # Store transcripts (in production, use a proper database)
    transcripts = {}

    @app.route('/webhook', methods=['POST'])
    def handle_tavus_callback():
        data = request.json
        event_type = data.get('event_type')
        conversation_id = data.get('conversation_id')
        
        print(f"Received callback: {event_type} for conversation {conversation_id}")
        
        if event_type == 'system.replica_joined':
            print("✅ Replica has joined the conversation")
            
        elif event_type == 'system.shutdown':
            shutdown_reason = data['properties'].get('shutdown_reason')
            print(f"🔚 Conversation ended: {shutdown_reason}")
        
        elif event_type == 'application.recording_ready':
            s3_key = data['properties'].get('s3_key')
            print(f"s3_key : {s3_key}")

        elif event_type == 'application.perception_analysis':
            analysis = data['properties'].get('analysis')
            print(f"analysis : {analysis}")
            
        elif event_type == 'application.transcription_ready':
            print("📝 Transcript is ready!")
            transcript = data['properties']['transcript']
            transcripts[conversation_id] = transcript
            
            # Process the transcript
            analyze_conversation(conversation_id, transcript)
            
        return jsonify({"status": "success"}), 200

    def analyze_conversation(conversation_id, transcript):
        """Analyze the conversation transcript"""
        user_turns = len([msg for msg in transcript if msg['role'] == 'user'])
        assistant_turns = len([msg for msg in transcript if msg['role'] == 'assistant'])
        
        print(f"Conversation {conversation_id} analysis:")
        print(f"- User turns: {user_turns}")
        print(f"- Assistant turns: {assistant_turns}")
        print(f"- Total messages: {len(transcript)}")

        print("Conversation : ")

        for msg in transcript:
            print(f"{msg['role']} : {msg['content']}")

    if __name__ == '__main__':
        app.run(port=5000, debug=True)
    ```

    The server will receive and process webhook callbacks from Tavus, handle different event types, store transcripts in memory, and analyze conversation data for each session.
  </Step>

  <Step title="Step 3: Run the Server">
    Run the app using the following command in the terminal:

    ```sh theme={null}
    python server.py
    ```

    The server should run on port `5000`.
  </Step>

  <Step title="Step 4: Forward the Port Using Ngrok">
    With [ngrok](https://ngrok.com/downloads/) installed and on your PATH, forward the port from a terminal (on Windows you can run `ngrok.exe` from the install folder instead).

    ```sh theme={null}
    ngrok http 5000
    ```

    The command will generate a forwarding link (e.g., [https://1234567890.ngrok-free.app](https://1234567890.ngrok-free.app)), which can be used as the callback URL.
  </Step>

  <Step title="Step 5: Use the Callback URL">
    Include the callback URL in your request to Tavus by appending `/webhook` to the forwarding link and setting it in the `callback_url` field.

    ```sh Create conversation with callback_url {6} theme={null}
    curl --request POST \
      --url https://tavusapi.com/v2/conversations \
      --header 'Content-Type: application/json' \
      --header 'x-api-key: <api-key>' \
      --data '{
      "callback_url": "https://1234567890.ngrok-free.app/webhook",
      "replica_id": "<replica_id>",
      "persona_id": "<persona_id>"
    }'
    ```

    <Note>
      * Replace `<api-key>` with your actual API key. You can generate one in the <a href="https://platform.tavus.io/api-keys">Developer Portal</a>.
      * Replace `<replica_id>` with the Replica ID you want to use.
      * Replace `<persona_id>` with the Persona ID you want to use.
    </Note>
  </Step>
</Steps>

