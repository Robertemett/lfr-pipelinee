from __future__ import annotations

import os
from pathlib import Path
from typing import Any


def validate_ltx_key() -> str:
    key = os.getenv("LTX_API_KEY", "").strip()
    if not key:
        raise RuntimeError("LTX_API_KEY is not set. Add it to your environment or .env file.")
    return key


def build_model_name(model: str | None = None) -> str:
    return (model or "ltx-2-5-pro").strip() or "ltx-2-5-pro"


def create_manifest(day_number: int, model: str, output_dir: str | Path, prompts: list[str]) -> Path:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    manifest_path = output_path / "pipeline_manifest.txt"
    lines = [
        f"Day: {day_number}",
        f"Model: {model}",
        "Prompts:",
    ]
    for index, prompt in enumerate(prompts, start=1):
        lines.append(f"{index}. {prompt}")
    manifest_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return manifest_path


def build_ltx_payload(day_number: int, prompts: list[str], model: str, single_clip: bool) -> dict[str, Any]:
    return {
        "day": day_number,
        "model": model,
        "single_clip": bool(single_clip),
        "prompts": prompts,
    }

__all__ = ["validate_ltx_key", "build_model_name", "create_manifest", "build_ltx_payload"]
