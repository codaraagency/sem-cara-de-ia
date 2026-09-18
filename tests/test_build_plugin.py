"""Verifica a distribuição real; não mede comportamento editorial de LLMs."""

import importlib.util
import tempfile
import unittest
import zipfile
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("build_plugin", ROOT / "scripts/build_plugin.py")
build = importlib.util.module_from_spec(spec)
spec.loader.exec_module(build)


class BuildPluginTests(unittest.TestCase):
    def setUp(self):
        self.manifest = build.load_manifest()

    def test_bundle_contains_supporting_resources_and_exact_content(self):
        with tempfile.TemporaryDirectory() as temp:
            archive = build.build_plugin(self.manifest, Path(temp))
            with zipfile.ZipFile(archive) as zf:
                for rel in (
                    "skills/sem-cara-de-ia/SKILL.md",
                    "skills/sem-cara-de-ia/references/padroes.md",
                    "skills/sem-cara-de-ia/references/exemplos.md",
                    "skills/sem-cara-de-ia/eval.md",
                    "skills/sem-cara-de-ia/agents/openai.yaml",
                    "agents/openai.yaml",
                ):
                    self.assertEqual(zf.read(rel), (ROOT / rel).read_bytes())
                self.assertFalse(any(n.startswith(".git/") for n in zf.namelist()))

    def test_build_and_check_preserve_existing_artifacts(self):
        with tempfile.TemporaryDirectory() as temp:
            dist = Path(temp) / "dist"
            dist.mkdir()
            sentinel = dist / "another-release.zip"
            sentinel.write_bytes(b"existing artifact")
            with patch.object(build, "DIST_DIR", dist):
                build.build_plugin(self.manifest)
                before = {p.name: p.read_bytes() for p in dist.iterdir()}
                with patch("sys.argv", ["build_plugin.py", "--check"]):
                    build.main()
                after = {p.name: p.read_bytes() for p in dist.iterdir()}
            self.assertEqual(before, after)
            self.assertEqual(sentinel.read_bytes(), b"existing artifact")

    def test_validation_rejects_archive_missing_reference(self):
        with tempfile.TemporaryDirectory() as temp:
            archive = Path(temp) / "incomplete.zip"
            omitted = "skills/sem-cara-de-ia/references/padroes.md"
            with zipfile.ZipFile(archive, "w") as zf:
                for rel in build.package_files(self.manifest) - {omitted}:
                    zf.write(ROOT / rel, rel)
            with self.assertRaises(SystemExit) as failure:
                build.validate_build(archive, self.manifest)
            self.assertIn(omitted, str(failure.exception))


if __name__ == "__main__":
    unittest.main()
