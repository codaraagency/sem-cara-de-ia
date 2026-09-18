#!/usr/bin/env python3
"""Valida e empacota o plugin Sem Cara de IA em um .zip para distribuição."""

import argparse
import json
import sys
import tempfile
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANIFEST_PATH = ROOT / ".codex-plugin" / "plugin.json"
DIST_DIR = ROOT / "dist"

REQUIRED_TOP_LEVEL_FIELDS = ["name", "version", "description", "author", "license"]
REQUIRED_INTERFACE_FIELDS = ["display_name", "short_description", "category", "capabilities"]
MAX_PROMPTS = 3
MAX_PROMPT_LENGTH = 128


def load_manifest() -> dict:
    if not MANIFEST_PATH.exists():
        sys.exit(f"Manifesto não encontrado: {MANIFEST_PATH}")
    return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))


def validate_source(manifest: dict) -> None:
    missing = [field for field in REQUIRED_TOP_LEVEL_FIELDS if field not in manifest]
    if missing:
        sys.exit(f"Campos obrigatórios ausentes no manifesto: {', '.join(missing)}")

    interface = manifest.get("interface", {})
    missing_interface = [field for field in REQUIRED_INTERFACE_FIELDS if field not in interface]
    if missing_interface:
        sys.exit(f"Campos obrigatórios ausentes em 'interface': {', '.join(missing_interface)}")

    prompts = interface.get("prompts", [])
    if len(prompts) > MAX_PROMPTS:
        sys.exit(f"'interface.prompts' tem {len(prompts)} entradas; o máximo é {MAX_PROMPTS}")
    for entry in prompts:
        text = entry.get("prompt", "")
        if len(text) > MAX_PROMPT_LENGTH:
            sys.exit(f"Prompt excede {MAX_PROMPT_LENGTH} caracteres: {text!r}")

    files = manifest.get("files", {})
    for label, rel_path in files.items():
        if not (ROOT / rel_path).exists():
            sys.exit(f"Arquivo referenciado em files.{label} não existe: {rel_path}")

    logo = manifest.get("branding", {}).get("logo")
    if logo and not (ROOT / logo).exists():
        sys.exit(f"Logo referenciado em branding.logo não existe: {logo}")

    print("Manifesto válido.")


def package_files(manifest: dict) -> set[str]:
    """Inclui os recursos da skill, não apenas seu ponto de entrada."""
    paths = set(manifest["files"].values())
    paths.update({".codex-plugin/plugin.json", "agents/openai.yaml"})
    skill_dir = (ROOT / manifest["files"]["skill"]).parent
    for path in skill_dir.rglob("*"):
        if path.is_file() and "__pycache__" not in path.parts and path.suffix != ".pyc":
            paths.add(path.relative_to(ROOT).as_posix())
    logo = manifest.get("branding", {}).get("logo")
    if logo:
        paths.add(logo)
    return paths


def build_plugin(manifest: dict, output_dir: Path | None = None) -> Path:
    version = manifest["version"]
    name = manifest["name"]
    output_dir = DIST_DIR if output_dir is None else output_dir
    output_dir.mkdir(parents=True, exist_ok=True)
    zip_path = output_dir / f"{name}-plugin-{version}.zip"
    # Valide antes de substituir a build da mesma versão. Outros artefatos ficam intactos.
    with tempfile.TemporaryDirectory(prefix="sem-cara-de-ia-", dir=output_dir) as temp:
        candidate = Path(temp) / zip_path.name
        with zipfile.ZipFile(candidate, "w", zipfile.ZIP_DEFLATED) as zf:
            for rel_path in sorted(package_files(manifest)):
                zf.write(ROOT / rel_path, rel_path)
        validate_build(candidate, manifest)
        candidate.replace(zip_path)
    print(f"Plugin empacotado em {zip_path}")
    return zip_path


def validate_build(zip_path: Path, manifest: dict) -> None:
    expected = package_files(manifest)

    with zipfile.ZipFile(zip_path) as zf:
        bad_entry = zf.testzip()
        if bad_entry is not None:
            sys.exit(f"Arquivo corrompido dentro do zip: {bad_entry}")
        names = set(zf.namelist())

    missing = expected - names
    if missing:
        sys.exit(f"Arquivos ausentes no zip gerado: {', '.join(sorted(missing))}")

    print("Build validada com sucesso.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="Valida e constrói em diretório temporário, sem alterar dist/.",
    )
    args = parser.parse_args()

    manifest = load_manifest()
    validate_source(manifest)
    if args.check:
        with tempfile.TemporaryDirectory(prefix="sem-cara-de-ia-check-") as temp:
            build_plugin(manifest, Path(temp))
        print("Modo --check: validação concluída sem alterar dist/.")
    else:
        build_plugin(manifest)


if __name__ == "__main__":
    main()
