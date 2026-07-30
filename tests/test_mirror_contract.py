from __future__ import annotations

from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github" / "workflows" / "candidate.yml"
EXPECTED_REF = (
    "ghcr.io/rjckkkkk/qwen36-gb10@sha256:"
    "d4e9505469af37e7c65b83a8e9a6b3025173ab9836366443eacee2dbf0493ae7"
)
EXPECTED_IDENTITY = (
    "https://github.com/rjckkkkk/qwen36-gb10-mirror/"
    ".github/workflows/candidate.yml@refs/heads/main"
)


class MirrorWorkflowContractTest(unittest.TestCase):
    def workflow(self) -> str:
        return WORKFLOW.read_text(encoding="utf-8")

    def test_workflow_uses_fixed_immutable_image(self) -> None:
        text = self.workflow()
        self.assertIn(EXPECTED_REF, text)
        self.assertIn(EXPECTED_IDENTITY, text)
        self.assertNotIn(":latest", text)

    def test_workflow_never_builds_or_runs_inference(self) -> None:
        text = self.workflow().lower()
        forbidden = (
            "docker build",
            "build-push-action",
            "reproduce.sh",
            "huggingface-cli download",
            "modelscope download",
            "launch_server",
        )
        for value in forbidden:
            self.assertNotIn(value, text)

    def test_workflow_uses_least_privilege(self) -> None:
        text = self.workflow()
        self.assertIn("contents: read", text)
        self.assertIn("id-token: write", text)
        self.assertIn("packages: write", text)
        self.assertNotIn("contents: write", text)

    def test_all_actions_are_commit_pinned(self) -> None:
        text = self.workflow()
        actions = re.findall(r"uses:\s*([^\s]+)", text)
        self.assertGreaterEqual(len(actions), 3)
        for action in actions:
            self.assertRegex(action, r"^[^@]+@[0-9a-f]{40}$")


if __name__ == "__main__":
    unittest.main()
