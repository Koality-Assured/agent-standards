"""CLI to validate JSON schemas, RFC documents, and normative specifications.

tags: [validator, standards, rfc, specs]
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Tuple

try:
    import jsonschema
except ImportError:
    jsonschema = None  # type: ignore


def validate_json_schemas(specs_dir: Path) -> Tuple[int, int]:
    """Validate all *.schema.json files under specs/."""
    schema_files = list(specs_dir.glob("*.schema.json"))
    passed = 0
    failed = 0

    print(f"Validating {len(schema_files)} JSON Schema(s) in {specs_dir}...")
    for sf in schema_files:
        try:
            data = json.loads(sf.read_text(encoding="utf-8"))
            if jsonschema is not None:
                jsonschema.Draft202012Validator.check_schema(data)
            print(f"  [PASS] {sf.name}")
            passed += 1
        except Exception as exc:
            print(f"  [FAIL] {sf.name}: {exc}", file=sys.stderr)
            failed += 1

    return passed, failed


def validate_rfc_documents(rfcs_dir: Path) -> Tuple[int, int]:
    """Validate that RFC Markdown files follow structural conventions."""
    rfc_files = [f for f in rfcs_dir.glob("*.md") if f.name != "template.md"]
    passed = 0
    failed = 0

    print(f"Validating {len(rfc_files)} RFC document(s) in {rfcs_dir}...")
    for rf in rfc_files:
        content = rf.read_text(encoding="utf-8")
        errors = []
        if not content.startswith("# RFC"):
            errors.append("Must start with '# RFC' heading")
        if "**Status:**" not in content and "- **Status:**" not in content:
            errors.append("Missing Status metadata field")

        if not errors:
            print(f"  [PASS] {rf.name}")
            passed += 1
        else:
            print(f"  [FAIL] {rf.name}: {', '.join(errors)}", file=sys.stderr)
            failed += 1

    return passed, failed


def main(argv: List[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--all", action="store_true", help="Validate all schemas and RFCs")
    parser.add_argument("--base-dir", type=str, default=".", help="Base directory of repository")
    args = parser.parse_args(argv)

    base = Path(args.base_dir).resolve()
    specs_dir = base / "specs"
    rfcs_dir = base / "rfcs"

    total_passed = 0
    total_failed = 0

    if specs_dir.exists():
        p, f = validate_json_schemas(specs_dir)
        total_passed += p
        total_failed += f

    if rfcs_dir.exists():
        p, f = validate_rfc_documents(rfcs_dir)
        total_passed += p
        total_failed += f

    print(f"\nOverall Result: {total_passed} passed, {total_failed} failed.")
    return 0 if total_failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
