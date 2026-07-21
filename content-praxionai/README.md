# The AI-Agent Builder — Workspace

Automation agency. Misi: bikin task repetitif ilang selamanya.

## Quick start
1. Buka folder ini di VS Code.
2. Pastiin Claude Code aktif — dia auto-baca `CLAUDE.md`.
3. Jalanin agent: lihat `/agents/`.

## Stack (4-layer workflow harian)
| Layer | Tool | Peran |
|-------|------|-------|
| Kerja | VS Code | tempat kerja — buka repo ini |
| Eksekusi | Claude Code | jalanin agent, generate, debug |
| Knowledge base | Obsidian | baca/nulis `/wiki`, graph view antar note |
| Histori | GitHub | commit = jejak kerja, compound tiap sesi |

> Ini beda sama tool stack production (n8n, Railway, Postgres, dst) di `CLAUDE.md` §4 — itu buat automation klien, ini buat workflow harian gw sendiri.

## Struktur
- `/sources`   raw input (link, ide, transkrip)
- `/wiki`       Obsidian Vault — knowledge base permanen (log harian, troubleshooting, hooks)
- `/agents`     definisi + prompt tiap agent
- `/content`    output (`/drafts`, `/published`)
- `/scripts`    n8n export, python, bash

Prinsip: **Compound, Not Reset.**
