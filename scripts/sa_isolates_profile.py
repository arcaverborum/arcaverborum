"""Compile reviewed South American author-key profiles.

No ordinary Latin-letter defaults are supplied: the brief requires a printed
authorial value for every grapheme. Koch-Grünberg explicitly adopts Schmidt's
Anthropos alphabet; his own and local statements take precedence. Other
round-one source decisions remain unchanged. Sources without an applicable key receive
guarded written-only overrides, preventing the generic IPA-tokenizer fallback.
No intake, extension, slice, source choice or supplement admission is changed.

Review: docs/SOUTH_AMERICA_ISOLATES_2026-11-04.md, Profiles section.
Run with the repository environment: python scripts/sa_isolates_profile.py
--write [--review-output PATH]. The default is a read-only coverage report.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import re
import sqlite3
import unicodedata
from collections import Counter
from pathlib import Path

import yaml

from arcaverborum.phonology import normalize_segments, segments_are_valid
from arcaverborum.supplements import evidence_hash

ROOT = Path(__file__).resolve().parents[1]

# Each rule is independently supported by the indicated printed comparison.
# In particular, no reduction or unprinted value is guessed. Koch-Grünberg's
# adopted alphabet supplies ordinary values; other source decisions stay fixed.
# Whole Unicode combining clusters are checked below
# when reporting gaps, so a known base never silently removes its accent.
JAHN = {"sh": ("ʃ", "Jahn 1927: p. 379, Ayomán key; English sh / German sch.")}
KOCH = {
    "e̱": ("ɛ", "Koch-Grünberg 1928 IV: p. 2, Zur Transskription; German ä / French è; unmarked short vowel."),
    "e̱:": ("ɛː", "Koch-Grünberg 1928 IV: p. 2, Zur Transskription; e̱ quality and explicit colon length."),
    "w": ("w", "Koch-Grünberg 1928 IV: p. 3, Zur Transskription; English w in water."),
    "y": ("j", "Koch-Grünberg 1928 IV: p. 3, Zur Transskription; English y in youth."),
    "r": ("r", "Koch-Grünberg 1928 IV: p. 3, Zur Transskription; r ist rollend."),
    "x": ("x", "Koch-Grünberg 1928 IV: p. 3, Zur Transskription; German ch in nach / Spanish j."),
    "x̭": ("ç", "Koch-Grünberg 1928 IV: p. 3, Zur Transskription; German ch in nicht."),
    "'": ("ʔ", "Koch-Grünberg 1928 IV: p. 3, Zur Transskription; laryngaler, stimmloser Explosivlaut."),
}


def koch_rules():
    """Finite reviewed alphabet, including explicitly composed diacritics.

    Values are conventional readings of the printed key, conditional on the
    extension's literal glyphs; they do not resolve its retained glyph doubts.
    No standalone mark can disappear or attach to an unsupported base.
    """
    rules = dict(KOCH)
    for g in "bkp":
        rules[g] = (
            g,
            "Schmidt 1907: pp. 872, 874, §§355, 359-361; voiced/voiceless stops; adopted by Koch-Grünberg IV p. 2.",
        )
    for g in "dg":
        rules[g] = (
            g,
            "Koch-Grünberg 1928 IV: p. 3; ordinary German value internally; word-final weakened cases excluded.",
        )
    for g in "stz":
        rules[g] = (
            g,
            (
                "Schmidt 1907: p. 856, §321, alveolar row; pp. 870-872 voicing and"
                " manner; adopted by Koch-Grünberg IV p. 2."
            ),
        )
    for g in "mn":
        rules[g] = (g, "Schmidt 1907: pp. 858-860, §§325-329; labial m, alveolar n; adopted by Koch-Grünberg IV p. 2.")
    rules.update(
        {
            "l": (
                "l",
                (
                    "Schmidt 1907: p. 862, §§334-336; plain alveolar l; not the "
                    "separate hooked R-L glyph in Koch-Grünberg IV p. 3."
                ),
            ),
            "h": (
                "h",
                "Schmidt 1907: p. 878, §372; open-glottis breath; consonant conspectus after p. 1098, Aspiratio.",
            ),
            "f": (
                "f",
                (
                    "Schmidt 1907: consonant conspectus after p. 1098; voiceless "
                    "labiodental fricative. Koch-Grünberg IV p. 3 fʰ remains "
                    "unresolved."
                ),
            ),
            "š": (
                "ʃ",
                "Schmidt 1907: pp. 876-878, §§370-371; voiceless palatal fricative; adopted by Koch-Grünberg IV p. 2.",
            ),
            "ž": (
                "ʒ",
                "Schmidt 1907: pp. 876-878, §§370-371; voiced counterpart of š; adopted by Koch-Grünberg IV p. 2.",
            ),
            "tš": (
                "tʃ",
                "Schmidt 1907: p. 848, §303; explicit voiceless affricate tš; adopted by Koch-Grünberg IV p. 2.",
            ),
            "dž": (
                "dʒ",
                (
                    "Schmidt 1907: p. 848, §303; explicit voiced affricate dž; adopted"
                    " by Koch-Grünberg IV p. 2; Kaliána p. 314 also hears dy, not "
                    "substituted."
                ),
            ),
            "ts": (
                "ts",
                (
                    "Schmidt 1907: p. 880, §§375-379; homorganic alveolar "
                    "stop-fricative affricate; adopted by Koch-Grünberg IV p. 2."
                ),
            ),
            "ḥ": ("ħ", "Schmidt 1907: consonant conspectus after p. 1098; underdotted h, voiceless Pharyngales."),
            "ỵ": (
                "ɣ",
                (
                    "Schmidt 1907: p. 876, §367 and consonant conspectus; underdotted "
                    "y, voiced posterior guttural fricative; distinct from KG p. 3 "
                    "plain y=j."
                ),
            ),
            "ḍ": ("ɖ", "Schmidt 1907: pp. 852, 856, §§314, 321; underdotted cerebral voiced stop."),
            "ṇ": ("ɳ", "Schmidt 1907: p. 860, §329; underdotted cerebral nasal."),
            "ṅ": (
                "ŋ",
                "Schmidt 1907: pp. 858-860, §§326-329; n plus dot above, retained alternative for the guttural nasal.",
            ),
            "-": (
                "+",
                (
                    "Koch-Grünberg 1928 IV: p. 3 analytical hyphen; p. 309 fn1 "
                    "identifies ki- as probable pronominal prefix. Preserve boundary."
                ),
            ),
        }
    )
    # Only the finite vowel clusters actually transcribed in this source.
    # ẹ overrides Schmidt's closed-e value: KG calls it reduced, not ordinary e.
    clusters = "a a̯ a̱ á á̱ ã ã́ ạ ạ́ e e̱ é é̱ ẽ ẽ́ ẽ̱ ẽ̱́ ē i i̯ í ĩ ĩ́ ĩ̯ ĭ o ó õ ṍ ö u u̯ u̱ ú ú̱ ũ ũ̯ ũ̱ ṹ ü ǘ ọ̃".split()
    qualities = {
        "a": (
            "ä",
            (
                "Schmidt 1907 p. 540 §145, open a with tongue at rest, contrasted "
                "with the front-raised underdotted a; central open conventional "
                "value"
            ),
        ),
        "ạ": (
            "a",
            (
                "Schmidt 1907 p. 540 §145 and p. 560 §183, underdotted "
                "front-raised open a, French madame / Spanish a; distinct from "
                "ordinary central a"
            ),
        ),
        "e": ("e", "Schmidt 1907 p. 540 §144, middle E, German See / French été"),
        "i": ("i", "Schmidt 1907 p. 540 §143, German wieder / French fini"),
        "u": ("u", "Schmidt 1907 p. 546 §151, French sous / English too"),
        "o": ("ɔ", "Koch-Grünberg 1928 IV p. 2, stated typical open o (gewöhnlich), not every surface token"),
        "e̱": ("ɛ", "Koch-Grünberg 1928 IV p. 2, German ä / French è"),
        "u̱": (
            "ʊ",
            (
                "Schmidt 1907 p. 546 §151, identical underlined u, German Mutter /"
                " English full; KG IV p. 2 between u and o is compatible"
            ),
        ),
        "a̱": (
            "ɑ",
            (
                "Schmidt 1907 p. 546 §153, identical underlined a, French lâche; "
                "KG IV p. 2 between a and o is compatible; no walk-specific extra "
                "rounding inferred"
            ),
        ),
        "ü": ("y", "Schmidt 1907 pp. 552-558 §§164-173, front tongue plus rounded lips, high labiodental vowel"),
        "ö": ("ø", "Schmidt 1907 pp. 552-558 §§164-173, middle labiodental rounded vowel"),
        "ọ": (
            "o",
            "Schmidt 1907 pp. 546, 560 §§152, 182-183, closed underdotted o; distinct from KG's typical plain open o",
        ),
    }
    for cluster in clusters:
        decomposed = unicodedata.normalize("NFD", cluster)
        marks = set(decomposed[1:])
        quality = unicodedata.normalize(
            "NFC", decomposed[0] + "".join(c for c in decomposed[1:] if c in "\u0331\u0323\u0308")
        )
        ipa, note = qualities[quality]
        if "\u0303" in marks:
            ipa += "\u0303"
            note += "; Schmidt 1907 p. 564 §§187-190, tilde nasality; KG IV p. 2 all vowels may be nasal"
        if "\u032f" in marks:
            ipa += "\u032f"
            note += "; Schmidt 1907 p. 584 §§242-243 and KG IV p. 3, nonsyllabic arc"
        if "\u0306" in marks:
            ipa += "\u0306"
            note += "; KG IV p. 2 overrides Schmidt 1907 p. 568 §201: breve is VERY short"
        if "\u0304" in marks:
            ipa += "ː"
            note += "; Schmidt 1907 p. 568 §202, macron length"
        if "\u0301" in marks:
            ipa = "ˈ" + ipa
            note += "; Schmidt 1907 p. 570 §210, dynamic accent; nucleus-attached stress, no inferred syllabification"
        rules[cluster] = (unicodedata.normalize("NFC", ipa), note + ".")
        if not marks & {"\u0306", "\u0304", "\u032f"}:
            rules[cluster + ":"] = (unicodedata.normalize("NFC", ipa + "ː"), note + "; KG IV p. 2, colon length.")
    for cluster in ["ẽ̱", "ũ̱"]:
        ipa, note = rules[cluster]
        rules[cluster + "´"] = (
            "ˈ" + ipa,
            note + " KG IV p. 308 fn2: spacing acute after this vowel is its accent; Schmidt 1907 p. 570 §210.",
        )
    # KG p. 3 calls a/o + accented i/u (or arc-marked i/u) diphthongs, but does
    # not say which member the acute leaves as the nucleus; Schmidt §242 (the
    # unaccented member is nonsyllabic) would contradict the arc reading. No
    # diphthong rule is admitted; such forms are guarded in scoped_koch().
    # Local Máku dot follows its vowel, unlike a nasal/quality underdot.
    rules["e·"] = (
        "ĕ",
        (
            "Koch-Grünberg 1928 IV: p. 318 fn1, raised dot makes preceding "
            "vowel very short; e quality Schmidt 1907 p. 540 §144."
        ),
    )
    return rules


KOCH_ROUND1 = dict(KOCH)
KOCH = koch_rules()
BOGGIANI = {
    "s": ("z", "Boggiani 1900: p. 208, Letras y signos convencionales; Italian s in rosa/casa, always."),
    "z": ("ts", "Boggiani 1900: p. 208, Letras y signos convencionales; Italian z in pezzo/tizzone."),
    "z'": ("dz", "Boggiani 1900: p. 208, Letras y signos convencionales; Italian z in mezzo/bazza/gazza."),
    "y": ("dʒ", "Boggiani 1900: p. 208, Letras y signos convencionales; Italian g before i/e."),
    "ü": ("y", "Boggiani 1900: p. 208, Letras y signos convencionales; French u / German ü."),
    "w": ("w", "Boggiani 1900: p. 208, Letras y signos convencionales; English w, between u and v."),
    "ch": ("tʃ", "Boggiani 1900: p. 208, Letras y signos convencionales; Spanish ch / Italian c before e/i."),
    "x": ("ʃ", "Boggiani 1900: p. 208, Letras y signos convencionales; English sh / Italian sc before i/e."),
}
# The extension explicitly renders small capitals as initial capital + lowercase.
# This is a typographic case equivalent, not another sound rule or lowercasing
# of the source Form. Do not introduce accent/length/reduction equivalents.
BOGGIANI.update({g[0].upper() + g[1:]: value for g, value in list(BOGGIANI.items())})

PRIMARY = {
    "jir-ayoman": ("jahn1927", "jahn1927_ayoman", JAHN),
    "jir-jirajara": ("jahn1927", "jahn1927_jirajara", {}),
    "jir-gayon": ("jahn1927", "jahn1927_gayon", {}),
    "tmc-timote": ("jahn1927", "jahn1927_timote", {}),
    "aru-awake": ("kochgrunberg1928", "kochgrunberg1928_Auake", KOCH),
    "pay-payagua": ("boggiani1900", "paya_boggiani", BOGGIANI),
    "mtn-matanawi": ("nimuendaju1925", "matanawi", {}),
    "xuk-xukuru": ("nimuendaju1949", "nimuendaju1949_sukuru", {}),
}
SUPPLEMENTS = {
    "mak-maku": {"kochgrunberg1928": KOCH},
    "sap-sape": {"kochgrunberg1928": KOCH},
    "ful-fulnio": {"nimuendaju1935": {}},
    "xuk-xukuru": {"nimuendaju1935": {}},
}
REASONS = {
    "jir-ayoman": (
        "Partial profile: only sh is unambiguous in Jahn 1927 p. 379. Undefined letters and marks remain unresolved. "
        "The source-language selector excludes all Oramas and Freitez Pineda forms; no Jahn rule is applied to them."
    ),
    "jir-jirajara": (
        "Profile held: Jahn 1927 pp. 339, 379, 388 do not establish that the Ayomán key applies to "
        "Párraga's Siquisique spelling. Guarded written-only evidence; no reading inferred."
    ),
    "jir-gayon": (
        "Profile held: Jahn 1927 pp. 339, 379, 392 do not explicitly extend the Ayomán key to Gayón. "
        "Guarded written-only evidence; shared authorship and glyphs do not certify a reading."
    ),
    "tmc-timote": (
        "Profile held: Jahn 1927 p. 326 explicitly retains Urrecheaga's original spelling; "
        "p. 379 is the Ayomán key. Guarded written-only evidence; no reading inferred."
    ),
    "aru-awake": (
        "Reviewed profile: Koch-Grünberg 1928 IV pp. 2-3 and local notes override his explicitly adopted "
        "Schmidt 1907 Anthropos alphabet (pp. 540-584, 848-880, consonant conspectus after p. 1098). "
        "Nasality, quantity, nucleus stress and boundaries are retained; plain o uses KG's stated typical open value. "
        "Parenthesized reductions, reduced/intermediate or uncertain glyph"
        " values and local exceptional readings remain unresolved."
    ),
    "pay-payagua": (
        "Partial profile from Boggiani 1900 p. 208, Letras y signos convencionales. "
        "Only explicit, unambiguous values are mapped; ordinary vowels, ambiguous qualities, "
        "stress combinations and reduced letters remain unresolved."
    ),
    "mtn-matanawi": (
        "Profile held: Nimuendajú 1925 pp. 166-171 specify hooked stress-bearing vowels but no complete segment key; "
        "the p. 148 table is attached to Torá and does not establish the Matanawí convention. "
        "Guarded written-only evidence."
    ),
    "xuk-xukuru": (
        "Profile held: Nimuendajú's forms printed by Loukotka 1949 pp. 79-80 and the 1935 typescript "
        "have no applicable authorial notation key. Guarded written-only evidence; "
        "no later or cross-source alphabet inferred."
    ),
}


def read_csv(path):
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def profile_text(rules):
    return "Grapheme\tIPA\tnotes\n" + "".join(f"{g}\t{ipa}\t{note}\n" for g, (ipa, note) in sorted(rules.items()))


def gaps(form, profile):
    """Report longest-match misses as NFC base+combining-mark clusters."""
    form = unicodedata.normalize("NFC", form)
    unknown = []
    i = 0
    keys = sorted((g for g in profile if not (g.startswith("^") and g.endswith("$"))), key=lambda g: (-len(g), g))
    while i < len(form):
        key = next(
            (
                g
                for g in keys
                if form.startswith(g, i) and (i + len(g) == len(form) or not unicodedata.combining(form[i + len(g)]))
            ),
            "",
        )
        if key:
            i += len(key)
        elif form[i].isspace():
            i += 1
        else:
            end = i + 1
            while end < len(form) and unicodedata.combining(form[end]):
                end += 1
            unknown.append(form[i:end])
            i = end
    return unknown


def review(rows, rules):
    profile = {g: ipa for g, (ipa, _) in rules.items()}
    results = []
    for row in rows:
        # Empty rules mean held evidence, never generic resegmentation.
        segments, status = normalize_segments("", row["Form"], profile) if profile else ("", "unclean")
        if segments and not segments_are_valid(segments):
            raise ValueError("Invalid resulting profile reading: " + row["ID"])
        results.append(
            {
                "id": row["ID"],
                "form": row["Form"],
                "segments": segments,
                "status": status,
                "unmapped": gaps(row["Form"], profile),
                **(
                    {"held_reason": rules[f"^{unicodedata.normalize('NFC', row['Form'])}$"][1]}
                    if f"^{unicodedata.normalize('NFC', row['Form'])}$" in rules
                    and not rules[f"^{unicodedata.normalize('NFC', row['Form'])}$"][0]
                    else {}
                ),
            }
        )
    return {
        "total": len(results),
        "profiled": sum(r["status"] == "profile" for r in results),
        "unmapped": sorted({g for r in results for g in r["unmapped"]}),
        "unmapped_counts": dict(sorted(Counter(g for r in results for g in r["unmapped"]).items())),
        "forms": results,
    }


def scoped_koch(rows):
    """Exact empty keys fail closed on local descriptions lacking a value."""
    rules = dict(KOCH)
    for row in rows:
        form, comment = row["Form"], row["Comment"]
        reason = ""
        if any(s in comment for s in ["verschwommen", "zögernd", "Gaumen gesprochen", "sehr kurz ausgesprochen"]):
            reason = "local note needs a form-specific phonetic value: " + comment
        if any(word.endswith(("d", "g")) for word in form.split()):
            reason = "p. 3 weakened word-final d/g has no unique value"
        if "--" in form:
            reason = "extended duration/ellipsis is not an ordinary analytical hyphen"
        # KG p. 3: a/o + accented i/u is a diphthong (even across a hyphen), but
        # the nucleus is not stated; a hiatus reading would contradict the key.
        nfd = unicodedata.normalize("NFD", form)
        if re.search(r"[ao][\u0300-\u036f]*:?-?[iu][\u0300-\u036f]*\u0301", nfd):
            reason = "p. 3 a/o + accented i/u diphthong; nucleus not stated by the key"
        if reason:
            page = row["ID"].split("-p")[1].split("-")[0]
            rules[f"^{unicodedata.normalize('NFC', form)}$"] = (
                "",
                f"Koch-Grünberg 1928 IV: p. {page}, {reason}. Unresolved whole-form guard; no mark deleted.",
            )
    return rules


def compile_profiles(root=ROOT, *, write=False):
    for _, _, rules in PRIMARY.values():
        for g, (ipa, note) in rules.items():
            if (
                unicodedata.normalize("NFC", g) != g
                or unicodedata.normalize("NFC", ipa) != ipa
                or (ipa and not segments_are_valid(ipa))
                or not note
            ):
                raise ValueError("Invalid or undocumented profile rule: " + g)
    report = {"primary": {}, "supplements": {}}
    # Direct read-only SQLite access: this script cannot rebuild intake.
    with sqlite3.connect((root / "intake/intake.sqlite").resolve().as_uri() + "?mode=ro", uri=True) as db:
        db.row_factory = sqlite3.Row
        for av_id, (dataset, language_id, rules) in PRIMARY.items():
            directory = root / "varieties" / av_id
            config_path = directory / "config.yaml"
            config = yaml.safe_load(config_path.read_text())
            if (config["sources"]["transcription"], config["sources"]["source_language_id"]) != (dataset, language_id):
                raise ValueError("Reviewed primary selector changed: " + av_id)
            rows = [
                dict(r)
                for r in db.execute(
                    "SELECT * FROM forms WHERE gc_lc=? AND Dataset=? AND Language_ID=? ORDER BY seq",
                    (config["glottocode"], dataset, language_id),
                )
            ]
            if not rows or any(r["Segments"] for r in rows):
                raise ValueError("Written source disappeared or acquired supplied segments: " + av_id)
            if dataset == "kochgrunberg1928":
                rules = scoped_koch(rows)
            report["primary"][av_id] = review(rows, rules)
            if not write:
                continue
            custom = directory / "custom"
            custom.mkdir(exist_ok=True)
            if rules:
                path = custom / "profile.tsv"
                expected = profile_text(rules)
                # Round 2 explicitly replaces only the previous KG profile.
                allowed = {expected}
                if dataset == "kochgrunberg1928":
                    allowed.add(profile_text(KOCH_ROUND1))
                if path.exists() and path.read_text() not in allowed:
                    raise ValueError("Existing reviewed profile differs: " + av_id)
                if (custom / "transcriptions.csv").exists():
                    raise ValueError("Do not overwrite existing transcription decisions: " + av_id)
                path.write_text(expected)
            else:
                # Per-record source hash: protect spelling and notation together.
                out = io.StringIO(newline="")
                writer = csv.DictWriter(
                    out,
                    fieldnames=["source_form_id", "expected_evidence_sha256", "transcription_policy", "notes"],
                    lineterminator="\n",
                )
                writer.writeheader()
                writer.writerows(
                    {
                        "source_form_id": r["ID"],
                        "expected_evidence_sha256": evidence_hash(r),
                        "transcription_policy": "orthographic_only",
                        "notes": REASONS[av_id],
                    }
                    for r in rows
                )
                path = custom / "transcriptions.csv"
                if path.exists() and path.read_text() != out.getvalue():
                    raise ValueError("Previously reviewed written evidence changed: " + av_id)
                if (custom / "profile.tsv").exists():
                    raise ValueError("Held source unexpectedly has a primary profile: " + av_id)
                path.write_text(out.getvalue())
            config["extensions"]["profile"] = bool(rules)
            config["extensions"]["transcriptions"] = not bool(rules)
            # Keep historical registration/provenance; replace the old reading claim.
            prefix = config["notes"].split(" Profile review 2026-11-05:")[0].split("Written-only:")[0].rstrip()
            if av_id == "jir-ayoman":
                prefix = prefix.replace("; Oramas 1916 forms as quoted by Jahn are written-only gap fills.", ".")
            config["notes"] = prefix + " Profile review 2026-11-05: " + REASONS[av_id]
            config_path.write_text(yaml.safe_dump(config, allow_unicode=True, sort_keys=False, width=95))
        for av_id, datasets in SUPPLEMENTS.items():
            ledger = read_csv(root / "varieties" / av_id / "custom/supplements.csv")
            report["supplements"][av_id] = {}
            for dataset, rules in datasets.items():
                rows = []
                for decision in ledger:
                    if decision["source"] != dataset:
                        continue
                    matches = db.execute(
                        "SELECT * FROM forms WHERE gc_lc=? AND Dataset=? AND ID=?",
                        (decision["source_glottocode"], dataset, decision["source_form_id"]),
                    ).fetchall()
                    if len(matches) != 1 or evidence_hash(dict(matches[0])) != decision["evidence_sha256"]:
                        raise ValueError("Supplement evidence changed: " + decision["source_form_id"])
                    if decision.get("transcription_policy") != "orthographic_only" and not (
                        dataset == "kochgrunberg1928"
                        and decision.get("profile_file") == "kochgrunberg1928.tsv"
                        and not decision.get("transcription_policy")
                    ):
                        raise ValueError("Supplement reading policy changed: " + decision["source_form_id"])
                    rows.append(dict(matches[0]))
                if dataset == "kochgrunberg1928":
                    rules = scoped_koch(rows)
                result = review(rows, rules)
                if result["profiled"] and dataset != "kochgrunberg1928":
                    raise ValueError("New complete supplemental reading requires an explicit admission review")
                if dataset == "kochgrunberg1928" and result["profiled"]:
                    by_id = {r["id"]: r for r in result["forms"]}
                    exact = {
                        f"^{r['form']}$": (
                            r["segments"],
                            "Koch-Grünberg 1928 IV pp. 2-3 and local notes; adopted Schmidt "
                            "1907 pp. 540-584, 848-880 and consonant conspectus after p. 1098. "
                            "Exact complete reading; grapheme-by-grapheme values/precedence in"
                            " scripts/sa_isolates_profile.py and the KG evidence review.",
                        )
                        for r in result["forms"]
                        if r["status"] == "profile"
                    }
                    expected = profile_text(exact)
                    digest = hashlib.sha256(expected.encode()).hexdigest()
                    path = root / "varieties" / av_id / "custom/supplement_profiles/kochgrunberg1928.tsv"
                    if path.exists():
                        old_digest = hashlib.sha256(path.read_bytes()).hexdigest()
                        if any(
                            d.get("profile_sha256") != old_digest for d in ledger if d.get("profile_file") == path.name
                        ):
                            raise ValueError("Previously reviewed supplemental profile changed: " + av_id)
                    for decision in ledger:
                        if decision["source"] != dataset:
                            continue
                        converted = by_id[decision["source_form_id"]]["status"] == "profile"
                        if converted:
                            decision.update(profile_file=path.name, profile_sha256=digest, transcription_policy="")
                            decision["rationale"] = decision["rationale"].replace(
                                "Written-only: no reading inferred.",
                                (
                                    "Reviewed source-scoped reading: Koch-Grünberg IV pp. 2-3/local "
                                    "notes, adopted Schmidt 1907 Anthropos key; source glyph "
                                    "uncertainties retained."
                                ),
                            )
                        elif decision.get("profile_file"):
                            raise ValueError("Previously converted reading fell outside reviewed scope")
                    if write:
                        path.parent.mkdir(exist_ok=True)
                        path.write_text(expected)
                        ledger_path = root / "varieties" / av_id / "custom/supplements.csv"
                        fields = list(ledger[0])
                        fields += [f for f in ["profile_file", "profile_sha256"] if f not in fields]
                        with ledger_path.open("w", newline="", encoding="utf-8") as handle:
                            writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
                            writer.writeheader()
                            writer.writerows(ledger)
                        config_path = root / "varieties" / av_id / "config.yaml"
                        config = yaml.safe_load(config_path.read_text())
                        prefix = config["notes"].split(" Profile review 2026-11-05:")[0]
                        config["notes"] = prefix + (
                            " Profile review 2026-11-05: Koch-Grünberg 1928 IV supplements use"
                            " guarded exact readings from pp. 2-3/local notes and the adopted "
                            "Schmidt 1907 Anthropos key; unresolved rows retain "
                            "orthographic_only. Other-source primaries keep their own "
                            "notation."
                        )
                        config_path.write_text(yaml.safe_dump(config, allow_unicode=True, sort_keys=False, width=95))
                report["supplements"][av_id][dataset] = result
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--review-output", type=Path)
    args = parser.parse_args()
    report = compile_profiles(write=args.write)
    if args.review_output:
        args.review_output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    for scope, items in report.items():
        for av_id, item in items.items():
            groups = {"primary": item} if scope == "primary" else item
            for source, result in groups.items():
                print(scope, av_id, source, f"{result['profiled']}/{result['total']}")


if __name__ == "__main__":
    main()
