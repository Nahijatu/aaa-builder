# Dev Session — 2026-07-11 — Auto-logging system + CLAUDE.md self-audit

## Apa yang dibangun

1. **Auto-logging system (§7.1 WATCH HISTORY, §7.2 BUILDING SESSIONS)** ditambahin ke `CLAUDE.md`,
   diadaptasi dari "PROMPT ADVANCED — Auto-logging" yang Andre kasih literal di
   `sources/andreas-course/Course 7 Build your 2nd Brain.md:235-249`.
   - Folder baru: `sources/watch/`, `sources/sessions/`.
   - File baru: `wiki/log.md` (timeline auto-capture, append-only, beda dari `log-YYYY-MM-DD.md`
     yang freeform).
   - Trigger eksplisit: `"log video [link]"`, `"log sesi hari ini"`. Trigger proaktif: nanya user
     di akhir sesi krusial.
2. **Self-audit CLAUDE.md vs 6 transcript course** (Course 3-8) — baca ulang menyeluruh termasuk
   raw transcript & "Prompt Guide" tiap file (ternyata tiap course punya prompt template resmi di
   bagian akhir).

## Keputusan teknis

- Konfirmasi: struktur 3-layer (`sources/` → `wiki/` → `CLAUDE.md`) di §5.1 dan auto-logging §7.1/7.2
  ternyata adaptasi **langsung dari prompt resmi Andre** (Course 7), bukan interpretasi bebas —
  jadi udah align 1:1 by design.
- 6 gap ditemuin & langsung diterapin ke CLAUDE.md §2, §3, §4:
  1. **Mulai Simpel, Jangan Over-Engineer** — bullet baru di §2, dari quote Andre di prompt loop
     engineering ("mulai dari versi PALING SIMPEL dulu, jangan over-engineer",
     `Course 8 Loop Engineering.md:181`).
  2. **Tangga Otomasi progresif** — bullet baru di §2: Smart Tools → Connect → Agent → Orchestrator
     baru specialized track, gak boleh loncat (`Course 7 Build your 2nd Brain.md:205`).
  3. **Agent vs Tools presisi istilah** — §2 "Agent-First" direvisi, gak asal sebut semua solusi
     "agent" (`Course 5 Build your first AI Agent.md`, definisi Tools vs Agent di 00:02:22-00:11:17).
  4. **Asumsikan user non-coder by default** — bullet baru di §3, dari pola "Gw ga bisa coding.
     Jelasin se-simple mungkin." yang muncul di 4 dari 6 prompt template course.
  5. **Jangan Bocorin Secret** — bullet baru di §2, dari warning Andre soal API key
     (`Course 3 Build your 1st Smart Tools.md:17:32`, "pantang banget enggak boleh disebarin").
  6. **Klarifikasi n8n vs Orchestrator** — catatan baru di §4: n8n gak pernah disebut di course
     (0 kali di 6 transcript); "Orchestrator" ala Andre itu AI agent Cloud Code + Railway/Vercel,
     bukan n8n. n8n dipertahankan buat kebutuhan client di luar konteks course.

## Masalah + solusi

- Awalnya salah nomorin referensi section pas nambah §5.1 (nulis "lihat §8" padahal auto-logging
  tetep §7 karena §5.1 cuma subsection, gak geser nomor section lain) — ke-fix sebelum commit.
- Wikilink ke `CLAUDE.md` dari halaman wiki (`second-brain.md`, `log.md`) gak valid karena
  CLAUDE.md di luar vault Obsidian (`/wiki` root) — diganti ke markdown link biasa `[]()`,
  konsisten sama aturan §5.1 (wikilink cuma buat link di dalam vault).
