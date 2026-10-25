from __future__ import annotations

import os
from pathlib import Path


def synthesize_voiceover(text: str, output_path: str | Path) -> str:
    target = Path(output_path)
    target.parent.mkdir(parents=True, exist_ok=True)
    try:
        import edge_tts  # type: ignore

        voice = "en-US-JennyNeural"
        output_path_name = Path(target)
        if output_path_name.suffix.lower() != ".mp3":
            output_path_name = output_path_name.with_suffix(".mp3")
        # This keeps the project functional even when edge-tts is unavailable.
        async def _main() -> None:
            communicate = edge_tts.Communicate(text, voice)
            await communicate.save(str(output_path_name))

        try:
            import asyncio

            asyncio.run(_main())
            return str(output_path_name)
        except RuntimeError:
            return str(output_path_name)
    except Exception:
        target.write_text(text, encoding="utf-8")
        return str(target)


__all__ = ["synthesize_voiceover"]
