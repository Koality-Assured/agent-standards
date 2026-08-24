# Specification: Agent-to-Agent (A2A) Interaction Protocol v1.0

- **Status:** Normative Standard
- **Version:** 1.0.0
- **Author:** Koality-Assured Protocol Working Group

## 1. Abstract

This specification defines the Agent-to-Agent (A2A) messaging envelope, communication semantics, and lifecycle state machines governing interactions between orchestrator agents, specialized subagents, and peer agents.

## 2. Message Envelope Specification

All A2A messages **MUST** conform to the following JSON structure:

```json
{
  "$schema": "https://schema.koality-assured.org/agent/a2a-message.schema.json",
  "message_id": "msg_01HXYZ1234567890ABCDEF",
  "correlation_id": "task_9876543210FEDCBA",
  "timestamp": "2026-08-24T12:00:00Z",
  "sender": {
    "agent_id": "subagent-frontend-01",
    "role": "frontend-specialist"
  },
  "recipient": {
    "agent_id": "parent-orchestrator",
    "role": "orchestrator"
  },
  "message_type": "task_result",
  "status": "success",
  "payload": {
    "summary": "Completed component refactoring and unit tests.",
    "artifacts": ["src/components/Header.tsx", "tests/Header.test.tsx"],
    "metrics": {
      "duration_seconds": 14.2,
      "tokens_consumed": 3840
    }
  }
}
```

## 3. Lifecycle States

```
[Spawned] ──> [Dispatched] ──> [Executing] ──> [Completed]
                   │                │
                   └──> [Rejected]  └──> [Failed / Cancelled]
```

## 4. Message Types

| Message Type | Description |
| --- | --- |
| `task_dispatch` | Orchestrator delegates a scoped task to a subagent. |
| `task_acknowledge` | Subagent confirms receipt and readiness to execute. |
| `heartbeat` | Periodic liveness and progress update from executing agent. |
| `task_result` | Final payload with results, modified files, and telemetry metrics. |
| `task_cancel` | Preemptive cancellation instruction sent to active agent. |
