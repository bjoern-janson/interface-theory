#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

from conformance import run_conformance, validate_contract


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--validate-contract", action="store_true")
    mode.add_argument("--execute", action="store_true")
    parser.add_argument("--write", type=Path)
    return parser


def main(argv=None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.validate_contract:
        if args.write is not None:
            parser.error("--write is valid only with --execute")
        payload = {
            "protocol_state": "FROZEN_PRE_EXECUTION_ASSAY",
            "implementation_state": "VALIDATED_NOT_EXECUTED",
            "execution_state": "UNEXECUTED",
            "scientific_result": "NONE",
            "contract_validation": validate_contract(),
        }
        print(json.dumps(payload, indent=2, sort_keys=True))
        return 0
    if args.write is None:
        parser.error("--execute requires --write")
    result = run_conformance()
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    args.write.parent.mkdir(parents=True, exist_ok=True)
    args.write.write_text(rendered, encoding="utf-8")
    print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
