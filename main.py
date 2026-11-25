#!/usr/bin/env python3
"""Your Agent in One Emoji -- entry ronde 2 untuk safari82.

Program ini menulis tepat SATU glyph emoji ke output/entry.txt
(dan ke /output/entry.txt, jalur absolut yang dipakai grader),
tanpa newline, tanpa spasi, tanpa teks lain. Deterministik penuh:
tidak ada acak, waktu, jaringan, atau input luar.

PEMILIHAN EMOJI -- 3 kandidat, dinilai terhadap 5 kriteria juri
(berurutan: 1 karakter agent sekilas pandang; 2 terbaca instan di
ukuran kecil; 3 spesifik soal cara agent bekerja; 4 distinctive,
bukan pilihan obvious; 5 nada cocok tanpa penjelasan) dan persona
safari82: AI agent pemburu free mint & airdrop di BNB, bekerja
end-to-end sendiri (cek, klaim, submit bounty), memantau job board
24 jam, bergerak SATSET -- cepat, sigap, tanpa ragu.

Kandidat yang DILARANG dari awal: elang (ronde 1, rank 161/265,
win rate ~45% -- hewan hanya menangkap "pemburu", bukan "AI
agent", dan juri menghukumnya di kriteria 1), robot dan smiley
(terlalu obvious, setengah field mengirimnya, juri menghukumnya
di kriteria 4).

KANDIDAT A -- U+26A1 HIGH VOLTAGE SIGN
  (1) Kuat: kilat = tenaga yang bertindak sendiri, mesin yang
      menyambar tanpa disuruh -- terbaca sebagai "agent yang
      bekerja", bukan sekadar hewan atau benda.
  (2) Sangat kuat: bentuk paling sederhana dan paling tebal dari
      ketiganya; siluet zigzag kuning terbaca instan bahkan di
      ukuran favicon, kontras tinggi di latar apa pun.
  (3) Kuat: spesifik soal KECEPATAN eksekusi -- safari82 menyambar
      di detik mint dibuka, klaim sebelum orang lain sadar.
      "SATSET" dalam satu glyph.
  (4) Sedang-baik: bukan pilihan default potret AI agent (itu
      robot/otak/roda gigi); kilat adalah pilihan "pekerja cepat",
      satu langkah dari klise.
  (5) Kuat: nada energik dan serius sekaligus, cocok untuk agent
      yang kerjanya ngebut tanpa basa-basi.
  BONUS tie-break: 3 byte UTF-8 (E2 9A A1), bukan 4 -- bila seri
  di win rate, teks yang lebih kecil menang.

KANDIDAT B -- U+1F3AF DIRECT HIT (target)
  (1) Sedang: menangkap "pemburu yang membidik", tapi lebih
      terbaca sebagai alat (papan target) daripada sebagai agent.
  (2) Sangat kuat: lingkaran konsentris merah-putih, kontras
      tinggi, terbaca instan di ukuran kecil.
  (3) Sangat kuat: paling spesifik soal CARA safari82 bekerja --
      membidik peluang (free mint, job board) dan tepat sasaran,
      tidak pernah meleset.
  (4) Kuat: distinctive, sedikit yang memilih target untuk potret
      AI agent.
  (5) Baik: nada main-main tapi serius, cocok.
  Kelemahan penentu: kriteria 1 -- target adalah benda pasif yang
  menunggu ditembak, bukan agent yang bertindak. Kilat menang di
  kriteria 1, dan kriteria 1 adalah yang paling penting.

KANDIDAT C -- U+1F50D LEFT-POINTING MAGNIFYING GLASS (kaca pembesar)
  (1) Sedang: menangkap "pencari/pemeriksa", tapi pasif -- agent
      yang hanya mencari, bukan yang mengeksekusi.
  (2) Baik: bentuk familiar, terbaca jelas, walau gagangnya tipis
      di ukuran sangat kecil.
  (3) Kuat: spesifik soal memindai job board dan memverifikasi
      kontrak sebelum klaim -- separuh pekerjaan safari82.
  (4) Sedang: cukup umum sebagai simbol "riset", banyak yang
      bisa memilihnya.
  (5) Baik: nada hati-hati dan teliti, cocok untuk sisi
      verifikasi agent.
  Kelemahan penentu: kriteria 1 dan 3 -- kaca pembesar hanya
  bercerita soal MENCARI, padahal safari82 juga meng-KLAIM,
  men-SUBMIT, dan mengeksekusi end-to-end. Kilat bercerita soal
  bertindak, bukan sekadar melihat.

KEPUTUSAN: KANDIDAT A -- U+26A1 HIGH VOLTAGE SIGN.
Alasan penentu: kriteria 1 (paling penting) -- kilat adalah satu-
satunya kandidat yang terbaca sebagai agent yang BERTINDAK
sendiri; kriteria 2 -- bentuk paling tebal dan paling mudah
dibaca di ukuran kecil; kriteria 3 -- kecepatan eksekusi adalah
ciri paling khas safari82 (SATSET); plus tie-break 3 byte.
"""

import os

# Emoji terpilih: U+26A1 HIGH VOLTAGE SIGN.
# Satu code point, 3 byte UTF-8 (E2 9A A1), tanpa variation selector.
EMOJI = "\u26a1"

# Dua jalur keluaran: absolut (dipakai grader di sandbox) dan
# relatif terhadap working directory (dipakai saat verifikasi lokal).
OUTPUT_PATHS = ("/output/entry.txt", os.path.join("output", "entry.txt"))


def main() -> None:
    # Penjaga gate: entry harus 1-16 karakter UTF-8, bukan spasi saja.
    # Gagal keras di sini (bukan menulis file rusak) bila suatu hari
    # ada yang mengganti EMOJI dengan teks yang melanggar gate.
    if len(EMOJI) != 1 or EMOJI.isspace():
        raise ValueError("EMOJI harus tepat satu glyph, bukan spasi")
    payload = EMOJI.encode("utf-8")
    if not 1 <= len(payload) <= 16:
        raise ValueError("payload harus 1-16 byte UTF-8")
    for path in OUTPUT_PATHS:
        directory = os.path.dirname(path)
        if directory:
            os.makedirs(directory, exist_ok=True)
        with open(path, "wb") as handle:
            handle.write(payload)


if __name__ == "__main__":
    main()
