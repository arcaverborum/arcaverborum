# pereira1964irantxe — Irántxe (Manoki), Pereira 1964

**Source.** Pereira, Adalberto Holanda, S.J. 1964. "Vocabulário da língua dos índios Irántxe." *Revista de Antropologia* (São Paulo) 12(1–2): 105–115. doi:10.11606/2179-0892.ra.1964.110740. Pp. 105–106 are an ethnographic introduction and bibliography; the **Irántxe–Portuguese vocabulary** is printed in two column pairs, alphabetically, on **pp. 107–115** (PDF pp. 3–11). The author was a Jesuit missionary at Utiariti (Missão Anchieta, Diamantino, Mato Grosso).

**Scan.** https://www.revistas.usp.br/ra/article/download/110740/109166 , sha256 `972cdd341340421c81359710094cef36dad5f7474e9a9677bb7bad48203c014a`. Page images of pp. 107–115 (grey, 110 dpi) are in `pages/`.

**Preparation.** Transcribed by an AI agent from page images on 2026-11-04 and verified by a second, independent reading (see `VERIFY.md`). The PDF text layer was used only to read the introduction, never for forms.

## Conventions

* Forms are exactly as printed (NFC): acute, circumflex, tilde, macron (ā ē ō ū), breve (ĭ ŭ), diaeresis (ä ë ï ö ü), capitals as printed (`MÜNKÜ`, `Ionádi`). The author prints a glyph like a **question mark** inside words (`á?á`, `mi?á`). It is evidently a glottal-stop letter but the paper never explains it. It is transcribed as ASCII `?`, as printed.
* `Value` = the printed form column of the entry, including alternatives and parenthesised material. `Form` = one alternative. Comma-separated alternatives in the form column become separate rows (24 rows).
* Parenthesised material after a form (`iakümbá (ci)`, `numã (ci)`, `piambá (ci)`, `iamaiminí (iohú)`, …; 11 rows) is unexplained by the author. It is kept in `Value`, omitted from `Form`, and noted in `Comment`.
* **Senses.** Many entries carry several comma-separated Portuguese glosses (`ver, paca`; `água, lágrima, matar`). Each comma-separated sense is its own parameter; the entry yields one row per sense, with the full printed gloss in `Comment` (113 rows). Parenthesised qualifiers stay with their sense (`pacu (peixe)`). `Name` = the sense as printed + ` | ` + English.
* Footnote 1 (p. 109, on *ietá* 'flauta sagrada') is given in `Comment`: "Chamada de “jararaca” pelos seringueiros." Footnote 2 (p. 111) belongs to an excluded ethnonym (see below).
* `Segments` is empty: the orthography is Portuguese-based and pre-phonological (x, nh, tx, c, ?). Loans are not marked; the source marks none.
* Concepticon mappings are conservative (364 of 624 parameters). Generic/specific mismatches, local species, possessed or derived forms (`meu pai`, `pé de pequi`) and kin terms are left unmapped.

## Counts and exclusions

590 printed entries (pp. 107–115: 24, 65, 75, 80, 68, 77, 67, 63, 73) → **652 rows, 589 distinct forms, 624 parameters (364 mapped)**.
Excluded senses (9; 8 entries contribute nothing):
* ethnonyms (6): *Ionádi* 'Nambiquara', *Kudáli, Man?miá* 'Pareci', *Maimiakí, Poimiá* 'Beiço de Pau' (footnote 2 "poi — mato, mi?á — homem" thus not used), *Meianlú* 'Kaiabí', *Salumã* 'Erikbátsia (índios Canoeiros de Mato Grosso)', and the sense 'IRÁNTXE' of *MÜNKÜ* (its sense 'gente' is kept);
* toponym (1): *sakapê* 'rio Juruena';
* grammatical morpheme (1): *kiní* 'terminação do imperativo';
* sentence (1): *iammtakiní* 'dá para mim'.

## Licence

The *Revista de Antropologia* (USP) publishes its back issues under the journal-wide **CC BY 3.0** notice. Following the maintainer's rule for USP journal files, the licence is `https://creativecommons.org/licenses/by/3.0/`. Caveat: applying the notice retroactively to a 1964 article is legally uncertain, the author's death year is not established, and the article is not pre-1931 public domain. The maintainer should confirm.

## Identity and caveats

Glottolog Irántxe-Münkü (iran1263) has two dialects: Manoki (iran1264), the Irántxe of the rio Cravari, and Münkü/Myky (munk1243), a group contacted only in 1971. Pereira's speakers were the Cravari Irántxe gathered at Utiariti from 1948 on, so this list is assigned to **Manoki (iran1264)**. The author gives "Münkü" ('gente') as their self-name, but that does not make this the Myky variety. Two later sources on the same language are not used here: Meader 1967 (Museu Nacional, unlicensed) and Moura 1957/1960 (in copyright).
