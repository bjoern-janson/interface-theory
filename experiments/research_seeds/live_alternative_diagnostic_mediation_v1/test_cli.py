import contextlib, io, json, tempfile, unittest
from pathlib import Path
from unittest.mock import patch
import run_v1


class CliTests(unittest.TestCase):
    def test_validate_contract_cannot_execute_assay(self):
        stdout = io.StringIO()
        with patch.object(run_v1,"run_assay",side_effect=AssertionError("assay executed")):
            with contextlib.redirect_stdout(stdout):
                code = run_v1.main(["--validate-contract"])
        payload = json.loads(stdout.getvalue())
        self.assertEqual(code, 0)
        self.assertEqual(payload["execution_state"], "UNEXECUTED")
        self.assertEqual(payload["scientific_result"], "NONE")

    def test_execute_without_write_stops_before_assay(self):
        with patch.object(run_v1,"run_assay",side_effect=AssertionError("assay executed")):
            with self.assertRaises(SystemExit):
                run_v1.main(["--execute"])

    def test_write_without_execute_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory)/"result.json"
            with self.assertRaises(SystemExit):
                run_v1.main(["--validate-contract","--write",str(target)])
            self.assertFalse(target.exists())


if __name__ == "__main__":
    unittest.main()
