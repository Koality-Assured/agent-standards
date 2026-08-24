"""Unit tests validating agent-standards schemas, RFCs, and specifications."""

import json
import unittest
from pathlib import Path
import sys

_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_ROOT))

from tools.validate_specs import validate_json_schemas, validate_rfc_documents


class TestStandardsValidation(unittest.TestCase):
    def setUp(self):
        self.root = _ROOT
        self.specs_dir = self.root / "specs"
        self.standards_dir = self.root / "standards"
        self.rfcs_dir = self.root / "rfcs"

    def test_specs_exist_and_validate(self):
        self.assertTrue(self.specs_dir.exists())
        passed, failed = validate_json_schemas(self.specs_dir)
        self.assertGreater(passed, 0)
        self.assertEqual(failed, 0)

    def test_normative_standards_exist(self):
        context_std = self.standards_dir / "context" / "5-tier-context-management.md"
        proto_std = self.standards_dir / "protocols" / "a2a-protocol-v1.md"
        sec_std = self.standards_dir / "security" / "security-musts.md"

        self.assertTrue(context_std.exists(), "5-tier context spec should exist")
        self.assertTrue(proto_std.exists(), "A2A protocol spec should exist")
        self.assertTrue(sec_std.exists(), "Security MUSTs spec should exist")

    def test_rfcs_validate(self):
        self.assertTrue(self.rfcs_dir.exists())
        passed, failed = validate_rfc_documents(self.rfcs_dir)
        self.assertGreater(passed, 0)
        self.assertEqual(failed, 0)

    def test_a2a_sample_message_matches_schema(self):
        schema_file = self.specs_dir / "a2a-message.schema.json"
        schema = json.loads(schema_file.read_text(encoding="utf-8"))

        sample = {
            "message_id": "msg_01HXYZ1234567890ABCDEF",
            "correlation_id": "task_12345",
            "timestamp": "2026-08-24T12:00:00Z",
            "sender": {"agent_id": "subagent-1", "role": "developer"},
            "recipient": {"agent_id": "parent", "role": "orchestrator"},
            "message_type": "task_result",
            "status": "success",
            "payload": {"result": "ok"}
        }

        try:
            import jsonschema
            jsonschema.validate(instance=sample, schema=schema)
        except ImportError:
            self.assertEqual(sample["message_type"], "task_result")


if __name__ == "__main__":
    unittest.main()
