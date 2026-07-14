# Index — Wiki

#index

Daftar isi semua halaman konsep di vault ini. Baca file ini dulu sebelum nambah/update halaman baru (lihat CLAUDE.md §5.1 — 3-Layer Knowledge System).

## Agent Aktif

Pipeline konten sekarang = **Researcher → Scriptwriter → Reviewer** (feedback loop, tolak skor <8). Content mode: educator-first — ngajarin, bukan jualan (lihat [[voice]]).

- [[../agents/01-researcher|01-researcher]] — sumber mentah (transkrip/berita/ide) → ringkasan poin inti + fakta terverifikasi
- [[../agents/02-scriptwriter|02-scriptwriter]] — poin inti → 3 opsi hook (pilih 1) → full draft carousel Design-Ready, wajib baca [[voice]]
- [[../agents/03-reviewer|03-reviewer]] — kritik tajam + skor 1-10 per 5 kriteria, TOLAK kalau <8 dengan revisi konkret

### Archived
- [[../agents/_archive/content-repurposer|content-repurposer]] *(ARCHIVED — dipindah ke `agents/_archive/`, digantiin pipeline 3-agent di atas)* — agent lama monolitik (research+writing+formatting jadi satu), gak ada feedback loop

## Andreas AI Builder Course

Status project sekarang: **Tools** (lihat [[andreas-course/smart-tools]]).
Belum naik ke [[andreas-course/ai-agents]] — nunggu memory loop persisten.
Roadmap penuh: [[andreas-course/smart-tools]] → [[andreas-course/ai-agents]]
→ [[andreas-course/orchestrator]] → [[andreas-course/loop-engineering]].

Konsep-konsep dari [[andreas-course/smart-tools|Andreas AI Builder Course]] (Course 3-8; Course 1-2 belum ada transcript-nya di `/sources`):

- [[andreas-course/smart-tools|Smart Tools]] — sistem otomasi dasar: trigger → data → proses → delivery, belum punya memori
- [[andreas-course/connecting-smart-tools|Connecting Smart Tools]] — menghubungkan beberapa Smart Tools jadi satu ekosistem
- [[andreas-course/ai-agents|AI Agents]] — upgrade Smart Tools jadi Agent dengan memory loop + feedback system
- [[andreas-course/orchestrator|Orchestrator]] — layer paling atas: mengatur & mendelegasikan ke banyak Agent/Tools
- [[andreas-course/second-brain|Second Brain]] — sistem knowledge management buat builder, basis dari 3-layer system project ini
- [[andreas-course/loop-engineering|Loop Engineering]] — pola generik (5 komponen loop) di balik semua Smart Tools & Agent

### Alur Belajar (Corepath)

[[andreas-course/smart-tools|Smart Tools]] → [[andreas-course/connecting-smart-tools|Connecting Smart Tools]] → [[andreas-course/ai-agents|AI Agents]] → [[andreas-course/orchestrator|Orchestrator]] → *(specialized tracks)* → [[andreas-course/second-brain|Second Brain]], [[andreas-course/loop-engineering|Loop Engineering]]
