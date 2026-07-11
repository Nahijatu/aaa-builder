#!/usr/bin/env python3
"""
transcribe.py — Transcribe video/audio (course Andreas) jadi note markdown Obsidian.

Pake OpenAI Whisper model 'medium' (atau lebih besar) biar transcript
Bahasa Indonesia detail & rapi — model kecil (tiny/base/small) DILARANG
karena suka salah tangkap kata.

Requirement:
    pip install openai-whisper
    ffmpeg harus ke-install & ada di PATH

Usage:
    python scripts/transcribe.py <file_atau_folder_video> [--model medium] [--lang id]

Output:
    wiki/andreas-course/<judul-video>.md
"""

import argparse
import re
import sys
from pathlib import Path

import whisper

VIDEO_EXTENSIONS = {".mp4", ".mkv", ".mov", ".avi", ".webm", ".m4a", ".mp3", ".wav"}
ALLOWED_MODELS = ["medium", "medium.en", "large", "large-v2", "large-v3", "large-v3-turbo"]

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_OUTPUT_DIR = REPO_ROOT / "wiki" / "andreas-course"


def sanitize_filename(name: str) -> str:
    name = re.sub(r'[\\/:*?"<>|]', "", name).strip()
    return name or "untitled"


def format_timestamp(seconds: float) -> str:
    m, s = divmod(int(seconds), 60)
    h, m = divmod(m, 60)
    return f"{h:02d}:{m:02d}:{s:02d}"


def build_markdown(title: str, source_file: str, model_name: str, language: str, segments) -> str:
    lines = [
        f"# {title}",
        "",
        "#transcript #andreas-course",
        "",
        f"> Source: `{source_file}`",
        f"> Whisper model: {model_name} | Language: {language}",
        "",
        "## Transcript",
        "",
    ]
    for seg in segments:
        ts = format_timestamp(seg["start"])
        text = seg["text"].strip()
        lines.append(f"**[{ts}]** {text}")
        lines.append("")
    return "\n".join(lines)


def transcribe_file(model, path: Path, output_dir: Path, model_name: str, language: str):
    print(f"[transcribe] {path.name} ...")
    result = model.transcribe(str(path), language=language, verbose=False)

    title = sanitize_filename(path.stem)
    md = build_markdown(title, path.name, model_name, language, result["segments"])

    output_dir.mkdir(parents=True, exist_ok=True)
    out_path = output_dir / f"{title}.md"
    out_path.write_text(md, encoding="utf-8")
    print(f"[saved] {out_path}")


def main():
    parser = argparse.ArgumentParser(description="Transcribe video/audio ke markdown notes (Obsidian).")
    parser.add_argument("input", help="File video/audio, atau folder isi banyak file")
    parser.add_argument(
        "--model", default="medium", choices=ALLOWED_MODELS,
        help="Whisper model (default: medium — minimal buat akurasi Bahasa Indonesia)",
    )
    parser.add_argument("--lang", default="id", help="Kode bahasa (default: id)")
    parser.add_argument(
        "--output", default=str(DEFAULT_OUTPUT_DIR),
        help=f"Folder output markdown (default: {DEFAULT_OUTPUT_DIR})",
    )
    args = parser.parse_args()

    input_path = Path(args.input)
    output_dir = Path(args.output)

    if not input_path.exists():
        print(f"Error: input tidak ditemukan: {input_path}", file=sys.stderr)
        sys.exit(1)

    if input_path.is_dir():
        files = sorted(f for f in input_path.iterdir() if f.suffix.lower() in VIDEO_EXTENSIONS)
        if not files:
            print(f"Error: gak ada file video/audio di {input_path}", file=sys.stderr)
            sys.exit(1)
    else:
        files = [input_path]

    print(f"[model] loading whisper '{args.model}' ...")
    model = whisper.load_model(args.model)

    for f in files:
        transcribe_file(model, f, output_dir, args.model, args.lang)

    print(f"\nSelesai. {len(files)} file di-transcribe ke {output_dir}/")


if __name__ == "__main__":
    main()
