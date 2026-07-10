# The AI-Agent Builder — Workspace

Automation agency. Misi: bikin task repetitif ilang selamanya.

## Quick start
1. Buka folder ini di VS Code.
2. Pastiin Claude Code aktif — dia auto-baca `CLAUDE.md`.
3. Jalanin agent: lihat `/agents/`.

## Struktur
- `/sources`   raw input (link, ide, transkrip)
- `/wiki`       knowledge base permanen
- `/agents`     definisi + prompt tiap agent
- `/content`    output (`/drafts`, `/published`)
- `/scripts`    n8n export, python, bash
- `/2nd-brain`  ilmu numpuk (`/wiki`, `/logs`)

Prinsip: **Compound, Not Reset.**
