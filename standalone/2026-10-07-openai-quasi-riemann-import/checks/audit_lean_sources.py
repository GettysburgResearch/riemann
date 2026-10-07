#!/usr/bin/env python3
"""Inventory the internal Lean imports and scan implementation source for markers.

The default input is this packet's ``upstream/lean`` directory. This is a
stdlib-only lexical source audit, NOT Lean elaboration, a kernel check, a proof
of theorem equivalence, or an audit of external dependency implementations.

Examples:
  python checks/audit_lean_sources.py --output formal-dependency-audit.json
  python checks/audit_lean_sources.py --lean-root /checkout/openai-math/lean
"""
from __future__ import annotations

import argparse
from collections import Counter
import json
from pathlib import Path
import re
import sys


DEFAULT_ROOTS = (
    "OAI.NumberTheory.DirichletL.Nonvanishing",
    "OAI.NumberTheory.DirichletL.Hecke.Nonvanishing",
    "OAI.NumberTheory.SiegelZeros.Main",
)
MARKERS = (
    "sorry", "admit", "axiom", "unsafe", "native_decide", "sorryAx",
    "ofReduceBool", "implemented_by", "extern",
)
MARKER_PATTERN = re.compile(
    r"(?<![\w'])" + "(?:" + "|".join(map(re.escape, MARKERS)) + r")(?![\w'])"
)
IMPORT_PATTERN = re.compile(
    r"(?m)^[ \t]*(?:(?:public|private|meta)[ \t]+)*import[ \t]+([^\n]*)"
)
CHAR_PATTERN = re.compile(
    r"'(?:\\(?:[nrt0'\"\\]|x[0-9a-fA-F]{2}|u\{[0-9a-fA-F]+\})|[^\\'\r\n])'"
)
RAW_STRING_PATTERN = re.compile(r'r(#+)?"')


def mask_comments_and_literals(source: str) -> str:
    """Replace comments and quoted literals by spaces, preserving line numbers.

    Recognizes nested /- -/ comments, -- comments, ordinary escaped strings,
    raw strings r#\"...\"# with any number of # characters, and character
    literals. This is a lexical filter, not a complete Lean parser. In
    particular it does not elaborate macros or interpolations in strings.
    """
    out = list(source)
    n = len(source)
    i = 0

    def blank(start: int, end: int) -> None:
        for k in range(start, end):
            if source[k] not in "\r\n":
                out[k] = " "

    while i < n:
        if source.startswith("--", i):
            end = source.find("\n", i + 2)
            end = n if end < 0 else end
            blank(i, end)
            i = end
        elif source.startswith("/-", i):
            start = i
            depth = 1
            i += 2
            while i < n and depth:
                if source.startswith("/-", i):
                    depth += 1
                    i += 2
                elif source.startswith("-/", i):
                    depth -= 1
                    i += 2
                else:
                    i += 1
            if depth:
                raise ValueError("Unterminated block comment")
            blank(start, i)
        elif source[i] == "r" and (i == 0 or not (source[i - 1].isalnum()
                                                   or source[i - 1] in "_′'")):
            raw = RAW_STRING_PATTERN.match(source, i)
            if raw is None:
                i += 1
                continue
            start = i
            closing = '"' + (raw.group(1) or "")
            end = source.find(closing, raw.end())
            if end < 0:
                raise ValueError("Unterminated raw string")
            i = end + len(closing)
            blank(start, i)
        elif source[i] == '"':
            start = i
            i += 1
            closed = False
            while i < n:
                if source[i] == "\\":
                    i += 2
                elif source[i] == '"':
                    i += 1
                    closed = True
                    break
                else:
                    i += 1
            if not closed:
                raise ValueError("Unterminated string")
            blank(start, i)
        elif source[i] == "'":
            char = CHAR_PATTERN.match(source, i)
            if char is None:
                i += 1
            else:
                blank(i, char.end())
                i = char.end()
        else:
            i += 1
    return "".join(out)


def module_path(root: Path, module: str) -> Path:
    components = module.split(".")
    if not components or any(not part.replace("'", "_").isidentifier()
                             for part in components):
        raise ValueError(f"Unsupported module name: {module!r}")
    path = root.joinpath(*components).with_suffix(".lean")
    if not path.resolve().is_relative_to(root):
        raise ValueError(f"Module path escapes Lean source root: {module}")
    return path


def audit(lean_root: Path, roots: tuple[str, ...]) -> dict:
    lean_root = lean_root.resolve()
    if not lean_root.is_dir():
        raise ValueError(f"Lean source directory is missing: {lean_root}")
    if any(not name.startswith("OAI.") for name in roots):
        raise ValueError("Root modules must use the internal OAI.* namespace")

    pending = list(roots)
    graph: dict[str, list[str]] = {}
    missing: set[str] = set()
    files: list[dict] = []
    marker_matches: list[dict] = []
    while pending:
        module = pending.pop()
        if module in graph or module in missing:
            continue
        path = module_path(lean_root, module)
        if not path.is_file():
            missing.add(module)
            continue
        raw = path.read_bytes()
        source = raw.decode("utf-8")
        try:
            masked = mask_comments_and_literals(source)
        except ValueError as exc:
            raise ValueError(f"{path.relative_to(lean_root)}: {exc}") from exc
        dependencies: list[str] = []
        for statement in IMPORT_PATTERN.finditer(masked):
            for dependency in statement.group(1).split():
                # Check syntax rather than silently dropping an unrecognized import.
                module_path(lean_root, dependency)
                dependencies.append(dependency)
                if dependency.startswith("OAI."):
                    pending.append(dependency)
        graph[module] = dependencies
        relative = path.relative_to(lean_root).as_posix()
        files.append({"module": module, "path": relative, "bytes": len(raw),
                      "lines": len(source.splitlines())})
        raw_lines = source.splitlines()
        for line_number, line in enumerate(masked.splitlines(), start=1):
            for match in MARKER_PATTERN.finditer(line):
                marker_matches.append({"path": relative, "line": line_number,
                                       "token": match.group(),
                                       "source_line": raw_lines[line_number - 1]})

    external = sorted({dep for deps in graph.values() for dep in deps
                       if not dep.startswith("OAI.")})
    per_root = {}
    for root in roots:
        visited: set[str] = set()
        todo = [root]
        while todo:
            item = todo.pop()
            if item in visited:
                continue
            visited.add(item)
            todo.extend(dep for dep in graph.get(item, ()) if dep.startswith("OAI."))
        per_root[root] = {"present_internal_modules": len(visited.intersection(graph)),
                          "missing_internal_modules": sorted(visited.intersection(missing))}

    return {
        "schema": "openai-quasi-rh-lean-source-audit-v1",
        "check": "internal import completeness and lexical implementation-source scan",
        "source_scan_pass": not missing and not marker_matches,
        "kernel_build_run": False,
        "statement_equivalence_checked": False,
        "external_dependency_sources_checked": False,
        "root_modules": list(roots),
        "checked_internal_modules": len(files),
        "checked_internal_lines": sum(row["lines"] for row in files),
        "checked_internal_bytes": sum(row["bytes"] for row in files),
        "missing_internal": sorted(missing),
        "external_imports": external,
        "external_import_namespace_counts": dict(sorted(Counter(
            name.split(".")[0] for name in external).items())),
        "per_root": per_root,
        "scanned_markers": list(MARKERS),
        "source_marker_matches": sorted(marker_matches, key=lambda row: (
            row["path"], row["line"], row["token"])),
        "limitations": [
            "Marker matches are review candidates, not conclusions about theorem axioms.",
            "Comments and quoted literals are masked; interpolation and macros are not elaborated.",
            "Challenge specification stubs are not implementation roots and are intentionally excluded.",
            "No claim of Lean parsing, elaboration, kernel acceptance, or theorem equivalence is made.",
        ],
        "checked_files": sorted(files, key=lambda row: row["path"]),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lean-root", type=Path,
                        default=Path(__file__).resolve().parents[1] / "upstream" / "lean")
    parser.add_argument("--root-module", action="append", dest="roots",
                        help="Internal root module; may be repeated. Defaults to the three solutions.")
    parser.add_argument("--output", type=Path, help="Write the full JSON report to this file.")
    args = parser.parse_args()
    try:
        report = audit(args.lean_root, tuple(args.roots or DEFAULT_ROOTS))
    except (OSError, UnicodeError, ValueError) as exc:
        print(json.dumps({"source_scan_pass": False, "error": str(exc),
                          "kernel_build_run": False}), file=sys.stderr)
        return 2
    payload = json.dumps(report, indent=2, ensure_ascii=False) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(payload, encoding="utf-8")
        print(json.dumps({"source_scan_pass": report["source_scan_pass"],
                          "checked_internal_modules": report["checked_internal_modules"],
                          "checked_internal_bytes": report["checked_internal_bytes"],
                          "missing_internal": len(report["missing_internal"]),
                          "marker_matches": len(report["source_marker_matches"]),
                          "kernel_build_run": False}))
    else:
        sys.stdout.write(payload)
    return 0 if report["source_scan_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
