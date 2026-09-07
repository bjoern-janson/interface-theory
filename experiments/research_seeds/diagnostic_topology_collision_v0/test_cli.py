import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent
RUNNER = ROOT / "run_v0.py"


class CliTests(unittest.TestCase):
    def test_validate_contract_reports_unexecuted_state(self):
        proc = subprocess.run(
            [sys.executable, str(RUNNER), "--validate-contract"],
            check=True, capture_output=True, text=True, cwd=ROOT,
        )
        payload = json.loads(proc.stdout)
        self.assertEqual(payload["protocol_state"], "FROZEN_PRE_EXECUTION_ASSAY")
        self.assertEqual(payload["execution_state"], "UNEXECUTED")
        self.assertEqual(payload["scientific_result"], "NONE")

    def test_validate_rejects_write(self):
        proc = subprocess.run(
            [sys.executable, str(RUNNER), "--validate-contract", "--write", "x.json"],
            capture_output=True, text=True, cwd=ROOT,
        )
        self.assertNotEqual(proc.returncode, 0)
        self.assertIn("--write is valid only with --execute", proc.stderr)

    def test_execute_requires_write(self):
        proc = subprocess.run(
            [sys.executable, str(RUNNER), "--execute"],
            capture_output=True, text=True, cwd=ROOT,
        )
        self.assertNotEqual(proc.returncode, 0)
        self.assertIn("--execute requires --write", proc.stderr)


if __name__ == "__main__":
    unittest.main()
