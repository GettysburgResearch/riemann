#!/usr/bin/env python3
"""Fail-closed Challenge/Solution theorem-type audit for the combined tree.

The source preflight is read-only.  The full audit invokes Lean exactly twice:
once with all Challenge modules and once with all Solution modules.  It never
writes into the repository; probe files live in an operating-system temporary
directory.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


class AuditError(RuntimeError):
    pass


@dataclass(frozen=True)
class Topic:
    file_stem: str
    challenge_decl: str
    solution_decl: str


TOPICS: tuple[Topic, ...] = (
    Topic("RH", "rh_statement_exact", "rh_statement_exact"),
    Topic(
        "MellinAPI",
        "Comparator.MellinAPI.fixedMellinConsumerChallenge",
        "Comparator.MellinAPI.fixedMellinConsumerSolution",
    ),
    Topic(
        "ArithmeticRows23",
        "Challenge.ArithmeticRows23.challenge",
        "Solution.ArithmeticRows23.solution",
    ),
    Topic(
        "FixedDetectorFiveThree",
        "Challenge.FixedDetectorFiveThree.challenge",
        "Solution.FixedDetectorFiveThree.solution",
    ),
    Topic(
        "OperatorPositiveSchurRescue",
        "OperatorPositiveSchurRescue_firewall",
        "OperatorPositiveSchurRescue_firewall",
    ),
    Topic("XiPickThreeNode", "XiPickThreeNode_identity", "XiPickThreeNode_identity"),
    Topic(
        "XiPickOrderThreeConditional",
        "XiPickOrderThreeConditional_psd",
        "XiPickOrderThreeConditional_psd",
    ),
)

TOKEN_PATTERNS = {
    "sorry": re.compile(r"(?<![\w'])sorry(?![\w'])"),
    "admit": re.compile(r"(?<![\w'])admit(?![\w'])"),
}
ANSI_ESCAPE = re.compile(r"\x1b\[[0-?]*[ -/]*[@-~]")


def fail(message: str) -> None:
    raise AuditError(message)


def strip_comments_and_strings(source: str) -> str:
    """Replace Lean comments and string contents with spaces.

    Lean block comments nest.  Keeping newlines makes diagnostics predictable;
    no source rewrite is used for theorem-type comparison.
    """

    out: list[str] = []
    i = 0
    block_depth = 0
    in_line = False
    in_string = False
    escaped = False

    while i < len(source):
        pair = source[i : i + 2]
        ch = source[i]

        if in_line:
            if ch == "\n":
                in_line = False
                out.append("\n")
            else:
                out.append(" ")
            i += 1
            continue

        if block_depth:
            if pair == "/-":
                block_depth += 1
                out.extend((" ", " "))
                i += 2
            elif pair == "-/":
                block_depth -= 1
                out.extend((" ", " "))
                i += 2
            else:
                out.append("\n" if ch == "\n" else " ")
                i += 1
            continue

        if in_string:
            out.append("\n" if ch == "\n" else " ")
            if escaped:
                escaped = False
            elif ch == "\\":
                escaped = True
            elif ch == '"':
                in_string = False
            i += 1
            continue

        if pair == "--":
            in_line = True
            out.extend((" ", " "))
            i += 2
        elif pair == "/-":
            block_depth = 1
            out.extend((" ", " "))
            i += 2
        elif ch == '"':
            in_string = True
            out.append(" ")
            i += 1
        else:
            out.append(ch)
            i += 1

    if block_depth:
        fail("unterminated Lean block comment during source preflight")
    if in_string:
        fail("unterminated Lean string during source preflight")
    return "".join(out)


def count_placeholder_tokens(source: str) -> tuple[int, int]:
    code = strip_comments_and_strings(source)
    return (
        len(TOKEN_PATTERNS["sorry"].findall(code)),
        len(TOKEN_PATTERNS["admit"].findall(code)),
    )


def module_root(formal: Path, side: str) -> Path:
    return formal / "comparator" / side / f"RiemannComparator{side}"


def topic_file(formal: Path, side: str, topic: Topic) -> Path:
    return module_root(formal, side) / f"{topic.file_stem}.lean"


def expected_inventory(formal: Path, side: str) -> set[Path]:
    side_root = formal / "comparator" / side
    return {topic_file(formal, side, topic).relative_to(side_root) for topic in TOPICS}


def actual_inventory(formal: Path, side: str) -> set[Path]:
    side_root = formal / "comparator" / side
    if not side_root.is_dir():
        fail(f"missing comparator directory: {side_root}")
    return {path.relative_to(side_root) for path in side_root.rglob("*.lean")}


def declaration_basename(name: str) -> str:
    return name.rsplit(".", 1)[-1]


def check_decl_is_present_once(code: str, declaration: str, path: Path) -> None:
    basename = declaration_basename(declaration)
    occurrences = re.findall(rf"\btheorem\s+{re.escape(basename)}\b", code)
    if len(occurrences) != 1:
        fail(
            f"{path}: expected exactly one source theorem named {basename}, "
            f"found {len(occurrences)}"
        )


def source_preflight(formal: Path) -> None:
    if not (formal / "lean-toolchain").is_file():
        fail(f"not a formal project (missing lean-toolchain): {formal}")
    if not (formal / "lakefile.toml").is_file():
        fail(f"not a formal project (missing lakefile.toml): {formal}")

    for side in ("Challenge", "Solution"):
        expected = expected_inventory(formal, side)
        actual = actual_inventory(formal, side)
        missing = sorted(str(path) for path in expected - actual)
        unexpected = sorted(str(path) for path in actual - expected)
        if missing or unexpected:
            fail(
                f"{side} topic inventory mismatch; missing={missing}; "
                f"unexpected={unexpected}"
            )

    for topic in TOPICS:
        for side, declaration in (
            ("Challenge", topic.challenge_decl),
            ("Solution", topic.solution_decl),
        ):
            path = topic_file(formal, side, topic)
            source = path.read_text(encoding="utf-8")
            code = strip_comments_and_strings(source)
            check_decl_is_present_once(code, declaration, path)
            sorry_count, admit_count = count_placeholder_tokens(source)
            if side == "Challenge":
                if sorry_count != 1 or admit_count != 0:
                    fail(
                        f"{path}: expected exactly one Challenge sorry and zero "
                        f"admit; found sorry={sorry_count} admit={admit_count}"
                    )
            elif sorry_count != 0 or admit_count != 0:
                fail(
                    f"{path}: Solution must contain zero sorry/admit; found "
                    f"sorry={sorry_count} admit={admit_count}"
                )


def sentinel(side: str, topic: Topic, boundary: str) -> str:
    return f"__RIEMANN_AUDIT_{side.upper()}_{topic.file_stem}_{boundary}__"


def make_probe(side: str) -> str:
    imports = [f"import RiemannComparator{side}.{topic.file_stem}" for topic in TOPICS]
    lines = [*imports, "", "set_option pp.fullNames true"]
    for topic in TOPICS:
        declaration = topic.challenge_decl if side == "Challenge" else topic.solution_decl
        lines.extend(
            (
                f'#eval IO.println "{sentinel(side, topic, "BEGIN")}"',
                f"#check {declaration}",
                f'#eval IO.println "{sentinel(side, topic, "END")}"',
            )
        )
    return "\n".join(lines) + "\n"


def extract_check_output(output: str, side: str, topic: Topic) -> str:
    begin = sentinel(side, topic, "BEGIN")
    end = sentinel(side, topic, "END")
    if output.count(begin) != 1 or output.count(end) != 1:
        fail(
            f"{side}/{topic.file_stem}: expected one BEGIN and END marker; "
            f"found BEGIN={output.count(begin)} END={output.count(end)}"
        )
    before, after_begin = output.split(begin, 1)
    del before
    payload, after_end = after_begin.split(end, 1)
    del after_end
    payload = payload.strip()
    if ANSI_ESCAPE.search(payload):
        fail(f"{side}/{topic.file_stem}: unexpected ANSI escape in Lean output")
    if not payload:
        fail(f"{side}/{topic.file_stem}: empty #check output")
    return payload


def normalize_printed_type(check_output: str, declaration: str) -> str:
    """Remove only the exact theorem-name prefix and Unicode whitespace."""

    if not check_output.startswith(declaration):
        fail(
            f"#check output did not start with the exact queried declaration "
            f"prefix {declaration!r}: {check_output[:160]!r}"
        )
    type_text = check_output[len(declaration) :]
    if not type_text or not type_text[0].isspace():
        fail(
            f"#check output declaration prefix was not followed by whitespace: "
            f"{check_output[:160]!r}"
        )
    normalized = "".join(ch for ch in type_text if not ch.isspace())
    if not normalized:
        fail(f"empty normalized type for {declaration}")
    return normalized


def run_lean_probe(
    formal: Path,
    side: str,
    lake: str,
    timeout_seconds: int,
) -> dict[str, str]:
    probe = make_probe(side)
    env = os.environ.copy()
    env.update({"NO_COLOR": "1", "CLICOLOR": "0", "PYTHONUTF8": "1"})
    with tempfile.TemporaryDirectory(prefix=f"riemann-{side.lower()}-type-audit-") as tmp:
        source = Path(tmp) / f"Audit{side}.lean"
        source.write_text(probe, encoding="utf-8", newline="\n")
        completed = subprocess.run(
            [lake, "env", "lean", str(source)],
            cwd=formal,
            env=env,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            encoding="utf-8",
            errors="strict",
            timeout=timeout_seconds,
            check=False,
        )
    if completed.returncode != 0:
        fail(
            f"{side} Lean probe failed with exit {completed.returncode}:\n"
            f"{completed.stdout}"
        )

    result: dict[str, str] = {}
    for topic in TOPICS:
        declaration = topic.challenge_decl if side == "Challenge" else topic.solution_decl
        raw = extract_check_output(completed.stdout, side, topic)
        result[topic.file_stem] = normalize_printed_type(raw, declaration)
    return result


def compare_types(
    challenge: dict[str, str], solution: dict[str, str]
) -> list[tuple[Topic, str]]:
    expected = {topic.file_stem for topic in TOPICS}
    for side, values in (("Challenge", challenge), ("Solution", solution)):
        if set(values) != expected:
            fail(
                f"{side} result inventory mismatch; "
                f"expected={sorted(expected)} actual={sorted(values)}"
            )
    matches: list[tuple[Topic, str]] = []
    for topic in TOPICS:
        ctype = challenge[topic.file_stem]
        stype = solution[topic.file_stem]
        if ctype != stype:
            fail(
                f"{topic.file_stem}: exact normalized theorem types differ\n"
                f"Challenge: {ctype}\nSolution:  {stype}"
            )
        matches.append((topic, ctype))
    return matches


def verify_manifest_hashes(
    path: Path, matches: Iterable[tuple[Topic, str]]
) -> None:
    if not path.is_file():
        fail(f"missing expected comparator-hash manifest: {path}")
    manifest = json.loads(path.read_text(encoding="utf-8"))
    expected = manifest.get("comparator_type_hashes")
    if not isinstance(expected, dict):
        fail("manifest lacks comparator_type_hashes object")
    actual = {
        topic.file_stem: hashlib.sha256(normalized.encode("utf-8")).hexdigest()
        for topic, normalized in matches
    }
    if expected != actual:
        fail(f"comparator hash mismatch; expected={expected} actual={actual}")
    print(f"PASS_FORMAL_V0_1_COMPARATOR_HASHES topics={len(actual)}")


def write_report(path: Path, matches: Iterable[tuple[Topic, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
        writer.writerow(
            (
                "topic",
                "challenge_declaration",
                "solution_declaration",
                "normalized_type_sha256",
                "normalized_type",
            )
        )
        for topic, normalized in matches:
            digest = hashlib.sha256(normalized.encode("utf-8")).hexdigest()
            writer.writerow(
                (
                    topic.file_stem,
                    topic.challenge_decl,
                    topic.solution_decl,
                    digest,
                    normalized,
                )
            )


def self_test() -> None:
    sample = """
/- sorry /- admit -/ -/
theorem wanted : True := by
  -- admit
  let message := "sorry admit"
  sorry
"""
    if count_placeholder_tokens(sample) != (1, 0):
        fail("self-test: comment/string-aware placeholder count failed")

    declaration = "Namespace.example"
    raw = "Namespace.example :\n  ∀ (x : Nat),\n    x = x"
    expected = ":∀(x:Nat),x=x"
    if normalize_printed_type(raw, declaration) != expected:
        fail("self-test: exact prefix/whitespace normalization failed")
    if normalize_printed_type(raw.replace("x = x", "x = 0"), declaration) == expected:
        fail("self-test: mathematical type mutation was incorrectly normalized away")
    binder_decl = "OperatorPositiveSchurRescue_firewall"
    binder_raw = (
        "OperatorPositiveSchurRescue_firewall {b z c : ℝ} "
        "(hb : b < 0) (hc : 0 < c) : b - z ^ 2 / c < 0"
    )
    binder_expected = "{bzc:ℝ}(hb:b<0)(hc:0<c):b-z^2/c<0"
    if normalize_printed_type(binder_raw, binder_decl) != binder_expected:
        fail("self-test: explicit binder preservation failed")

    topic = TOPICS[0]
    fixture = (
        f"noise\n{sentinel('Challenge', topic, 'BEGIN')}\n"
        f"{topic.challenge_decl} : True\n"
        f"{sentinel('Challenge', topic, 'END')}\nnoise"
    )
    extracted = extract_check_output(fixture, "Challenge", topic)
    if normalize_printed_type(extracted, topic.challenge_decl) != ":True":
        fail("self-test: sentinel extraction failed")

    with tempfile.TemporaryDirectory(prefix="riemann-comparator-static-test-") as tmp:
        formal = Path(tmp) / "formal"
        (formal / "lean-toolchain").parent.mkdir(parents=True)
        (formal / "lean-toolchain").write_text("test\n", encoding="utf-8")
        (formal / "lakefile.toml").write_text("name = \"test\"\n", encoding="utf-8")
        for candidate in TOPICS:
            for side, declaration in (
                ("Challenge", candidate.challenge_decl),
                ("Solution", candidate.solution_decl),
            ):
                path = topic_file(formal, side, candidate)
                path.parent.mkdir(parents=True, exist_ok=True)
                proof = "sorry" if side == "Challenge" else "True.intro"
                path.write_text(
                    f"theorem {declaration_basename(declaration)} : True := {proof}\n",
                    encoding="utf-8",
                )
        source_preflight(formal)
        unexpected = module_root(formal, "Challenge") / "Unexpected.lean"
        unexpected.write_text("theorem extra : True := by sorry\n", encoding="utf-8")
        try:
            source_preflight(formal)
        except AuditError as error:
            if "inventory mismatch" not in str(error):
                raise
        else:
            fail("self-test: unexpected topic file did not fail closed")
        unexpected.unlink()
        missing = topic_file(formal, "Solution", TOPICS[-1])
        missing.unlink()
        try:
            source_preflight(formal)
        except AuditError as error:
            if "inventory mismatch" not in str(error):
                raise
        else:
            fail("self-test: missing topic file did not fail closed")

    print(
        "PASS_COMBINED_COMPARATOR_AUDIT_SELF_TEST "
        "normalization=1 sentinels=1 lexer=1 inventory_fail_closed=1"
    )


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--repo",
        type=Path,
        help="Riemann repository root containing formal/ (required except for --self-test)",
    )
    parser.add_argument(
        "--preflight",
        action="store_true",
        help="run only read-only file inventory and placeholder checks; do not invoke Lean",
    )
    parser.add_argument(
        "--self-test",
        action="store_true",
        help="run internal static fixtures only; do not inspect a repository or invoke Lean",
    )
    parser.add_argument("--lake", default="lake", help="Lake executable (default: lake)")
    parser.add_argument("--timeout", type=int, default=600, help="timeout per Lean process")
    parser.add_argument(
        "--output",
        type=Path,
        help="optional TSV output path (full audit only; never written inside repo by default)",
    )
    parser.add_argument(
        "--expected-manifest",
        type=Path,
        help="optional formal-v0.1 manifest whose comparator hashes must match",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    if args.self_test:
        if (
            args.repo is not None
            or args.preflight
            or args.output is not None
            or args.expected_manifest is not None
        ):
            fail(
                "--self-test cannot be combined with --repo, --preflight, "
                "--output, or --expected-manifest"
            )
        self_test()
        return 0
    if args.repo is None:
        fail("--repo is required unless --self-test is used")
    if args.timeout <= 0:
        fail("--timeout must be positive")

    repo = args.repo.resolve()
    formal = repo / "formal"
    source_preflight(formal)
    print(
        "PASS_COMBINED_COMPARATOR_SOURCE_PREFLIGHT "
        f"topics={len(TOPICS)} challenge_sorries={len(TOPICS)} "
        "solution_placeholders=0"
    )
    if args.preflight:
        if args.output is not None or args.expected_manifest is not None:
            fail("--output and --expected-manifest are unavailable with --preflight")
        return 0

    # These must remain distinct subprocess calls: several Challenge and Solution
    # declarations intentionally have identical global theorem names.
    challenge = run_lean_probe(formal, "Challenge", args.lake, args.timeout)
    solution = run_lean_probe(formal, "Solution", args.lake, args.timeout)
    matches = compare_types(challenge, solution)
    if args.expected_manifest is not None:
        verify_manifest_hashes(args.expected_manifest.resolve(), matches)
    if args.output is not None:
        output = args.output.resolve()
        if output == repo or output.is_relative_to(repo):
            fail("--output must be outside the audited repository")
        write_report(output, matches)
    print(
        "PASS_COMBINED_COMPARATOR_TYPE_FIDELITY "
        f"topics={len(matches)} lean_processes=2 normalization=prefix+whitespace-only"
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (AuditError, OSError, UnicodeError, subprocess.SubprocessError) as error:
        print(f"FAIL_COMBINED_COMPARATOR_TYPE_FIDELITY: {error}", file=sys.stderr)
        raise SystemExit(1)
