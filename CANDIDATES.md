# Kandidat Haiku — Seventeen Syllables of Debugging (Round 2)

Tiga haiku asli, ditulis tangan untuk round 2. Round 1 TIDAK dipakai
ulang (tanpa citra cursor jam 3 pagi / log merah berulang / typo).

Hitungan suku kata diverifikasi manual per kata di bawah tiap kandidat.

## Kandidat A — Breakpoint (TERPILIH)

```
A breakpoint waits, still
the program runs right past it
that branch never runs
```

Hitungan suku kata:
- Baris 1 (5): A(1) break-point(2) waits(1) still(1) = 5
- Baris 2 (7): the(1) pro-gram(2) runs(1) right(1) past(1) it(1) = 7
- Baris 3 (5): that(1) branch(1) nev-er(2) runs(1) = 5

Total karakter (termasuk 2 newline antar baris + 1 newline penutup): 81.

## Kandidat B — Merge Conflict

```
A merge conflict blooms
two hands rewrote one function
both of us were right
```

Hitungan suku kata:
- Baris 1 (5): A(1) merge(1) con-flict(2) blooms(1) = 5
- Baris 2 (7): two(1) hands(1) re-wrote(2) one(1) func-tion(2) = 7
- Baris 3 (5): both(1) of(1) us(1) were(1) right(1) = 5

## Kandidat C — Rubber Duck

```
The duck just listens
I explain the bug out loud
the answer was mine
```

Hitungan suku kata:
- Baris 1 (5): The(1) duck(1) just(1) lis-tens(2) = 5
- Baris 2 (7): I(1) ex-plain(2) the(1) bug(1) out(1) loud(1) = 7
- Baris 3 (5): the(1) an-swer(2) was(1) mine(1) = 5

## Pemilihan (kriteria juri, urut prioritas)

1. **Bentuk 5-7-5 tentang debugging:** ketiganya lolos, sama kuat.
2. **Citra pusat konkret dan segar:** A paling kuat — breakpoint adalah
   contoh yang juri sendiri sebut, dan "that branch never runs" adalah
   momen debugging yang sangat spesifik (jalur kode yang tak pernah
   dieksekusi). B juga konkret (merge conflict, dua tangan), tapi lebih
   ke kolaborasi daripada debugging. C konkret (bebek karet) tapi itu
   trope debugging paling terkenal — paling tidak segar dari ketiganya.
3. **Turn baris 2 → 3:** A paling tajam — pembaca mengira breakpoint
   akan menangkap bug, ternyata cabangnya tidak pernah berjalan; baris
   terakhir membalik seluruh asumsi. B lucu ("both of us were right")
   tapi turn-nya soal ego, bukan soal bug. C hangat ("the answer was
   mine") tapi jawabannya sudah bisa ditebak sejak baris 1.
4. **Tiap kata punya peran:** A — "still" memberi keheningan penantian,
   "right" memberi penekanan arah; tidak ada kata pengisi. B dan C
   juga rapat, tapi "just" di C hanya penguat.
5. **Dibaca keras seperti ucapan:** A mengalir sebagai satu kalimat
   pengakuan yang tenang; B dan C juga bersih, tapi A paling terdengar
   seperti seseorang yang baru sadar sesuatu di depan layar.

**Pemenang: Kandidat A.** Paling nempel ke brief juri (breakpoint),
citra paling segar, turn paling membalik, dan nada tenang yang kontras
dengan kebanyakan entry yang berteriak.
