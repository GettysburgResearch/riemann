#!/usr/bin/env python3
"""Import closure, declaration index and lexical trust scan for the OAI 7/8 Lean import.

Status: EXPLORATORY tooling (reading only). No Lean process is started.

Usage:
  python3 -I lean_closure_map.py <lean_root> <out_json> [--git-ref REF --git-prefix PREFIX --repo DIR]
          [--decls DECLS_TSV]   (default: <out_json stem>_decls.tsv; about 3 MB)

<lean_root> is the upstream `lean/` directory (the one containing `OAI/` and `lakefile.lean`).
The root module is OAI.NumberTheory.DirichletL.Nonvanishing.

What it does:
  1. Reads every `import` line of every OAI/**/*.lean file and computes the transitive closure
     of the root module over OAI modules. External imports (Mathlib, PrimeNumberTheoremAnd,
     RellichKondrachov, Lean) are recorded but not followed.
  2. Counts closure modules and lines per sub-directory of OAI/NumberTheory/DirichletL.
  3. Optional: recomputes the git blob id of every closure file and compares it with
     `git ls-tree -r REF PREFIX` (checks that the scanned tree is byte-identical to the ref).
  4. Lexical scan of the closure, after stripping comments and string literals, for
     trust-relevant tokens (axiom, sorry, native_decide, implemented_by, extern, unsafe, csimp,
     debug.skipKernelTC, ofReduceBool, trustCompiler, decide-with-kernel flags, custom
     syntax/macro/elab, set_option maxRecDepth/maxHeartbeats, ...).
  5. Approximate declaration index (keyword + name + namespace stack), for lookup only.

The input files are treated as untrusted data: they are read as text and never executed.
"""
import hashlib
import json
import os
import re
import subprocess
import sys
from collections import Counter, defaultdict

ROOT_MODULE = "OAI.NumberTheory.DirichletL.Nonvanishing"

IMPORT_RE = re.compile(r"^\s*(?:public\s+)?(?:meta\s+)?import\s+(?:all\s+)?([A-Za-z0-9_.'«»]+)")


def module_to_path(root, mod):
    return os.path.join(root, *mod.split(".")) + ".lean"


def path_to_module(root, path):
    rel = os.path.relpath(path, root)
    return rel[:-5].replace(os.sep, ".")


def strip_comments_and_strings(src):
    """Remove Lean comments (nested /- -/ and --) and string literal contents.

    Doc comments (/-- ... -/, /-! ... -/) are comments too. Newlines are kept so that
    line numbers survive. Char literals are left alone (they cannot contain keywords that
    matter here)."""
    out = []
    i, n = 0, len(src)
    depth = 0
    in_str = False
    while i < n:
        c = src[i]
        if depth > 0:
            if src.startswith("/-", i):
                depth += 1
                i += 2
                continue
            if src.startswith("-/", i):
                depth -= 1
                i += 2
                continue
            out.append("\n" if c == "\n" else " ")
            i += 1
            continue
        if in_str:
            if c == "\\" and i + 1 < n:
                out.append("  " if src[i + 1] != "\n" else " \n")
                i += 2
                continue
            if c == '"':
                in_str = False
                out.append('"')
                i += 1
                continue
            out.append("\n" if c == "\n" else " ")
            i += 1
            continue
        if src.startswith("/-", i):
            depth = 1
            i += 2
            out.append("  ")
            continue
        if src.startswith("--", i):
            j = src.find("\n", i)
            if j < 0:
                j = n
            out.append(" " * (j - i))
            i = j
            continue
        if c == '"':
            in_str = True
            out.append('"')
            i += 1
            continue
        out.append(c)
        i += 1
    return "".join(out)


# Trust-relevant lexical patterns, applied to comment- and string-stripped text.
TRUST_PATTERNS = {
    "axiom (declaration)": r"(?m)^[ \t]*(?:@\[[^\]]*\]\s*)?(?:private\s+|protected\s+)?axiom\b",
    "axiom (any token)": r"\baxiom\b",
    "sorry": r"\bsorry\b",
    "admit": r"\badmit\b",
    "sorryAx": r"\bsorryAx\b",
    "native_decide": r"\bnative_decide\b",
    "decide +native / +kernel": r"\bdecide\s*\+\s*(?:native|kernel)\b",
    "kernel := true / native := true": r"\b(?:kernel|native)\s*:=\s*true\b",
    "Lean.ofReduceBool / reduceBool": r"\b(?:ofReduceBool|reduceBool|ofReduceNat|reduceNat)\b",
    "trustCompiler": r"\btrustCompiler\b",
    "implemented_by": r"\bimplemented_by\b",
    "extern": r"@\[\s*extern\b|\bextern\b",
    "unsafe": r"\bunsafe\b",
    "csimp": r"\bcsimp\b",
    "debug.skipKernelTC": r"\bdebug\.skipKernelTC\b|\bskipKernelTC\b",
    "opaque": r"(?m)^[ \t]*(?:@\[[^\]]*\]\s*)?(?:private\s+|protected\s+)?opaque\b",
    "partial def": r"\bpartial\s+def\b",
    "syntax (custom)": r"(?m)^[ \t]*(?:@\[[^\]]*\]\s*)?(?:local\s+|scoped\s+)?syntax\b",
    "macro (custom)": r"(?m)^[ \t]*(?:@\[[^\]]*\]\s*)?(?:local\s+|scoped\s+)?macro\b",
    "macro_rules": r"\bmacro_rules\b",
    "elab (custom)": r"(?m)^[ \t]*(?:@\[[^\]]*\]\s*)?(?:local\s+|scoped\s+)?elab\b",
    "elab_rules": r"\belab_rules\b",
    "notation (local/scoped/global)": r"(?m)^[ \t]*(?:local\s+|scoped\s+)?(?:notation|infix|infixl|infixr|prefix|postfix)\b",
    "initialize / builtin_initialize": r"(?m)^[ \t]*(?:builtin_)?initialize\b",
    "run_cmd / run_elab / run_meta": r"\brun_(?:cmd|elab|meta)\b",
    "#eval": r"#eval\b",
    "Lean.Elab / Lean.Meta use": r"\bLean\.(?:Elab|Meta)\b",
    "attribute [irreducible]/[implemented_by]": r"attribute\s*\[[^\]]*(?:irreducible|implemented_by)[^\]]*\]",
    "set_option maxHeartbeats": r"\bset_option\s+maxHeartbeats\b",
    "set_option synthInstance.maxHeartbeats": r"\bset_option\s+synthInstance\.maxHeartbeats\b",
    "set_option maxRecDepth": r"\bset_option\s+maxRecDepth\b",
    "set_option (other)": r"\bset_option\s+(?!maxHeartbeats\b|maxRecDepth\b|synthInstance\.maxHeartbeats\b)[A-Za-z_.]+",
    "decide (tactic or term)": r"\bdecide\b",
    "Decidable.decide / by rfl on Bool": r"\bDecidable\.decide\b",
}

DECL_RE = re.compile(
    r"(?m)^[ \t]*(?:@\[[^\]]*\][ \t\n]*)*(?:(?:private|protected|noncomputable|nonrec|partial|unsafe)[ \t]+)*"
    r"(theorem|lemma|def|abbrev|structure|class|instance|inductive|axiom|opaque)\b[ \t]*"
    r"([^\s:({\[⦃]*)"
)
NS_RE = re.compile(r"(?m)^[ \t]*(namespace|end|section|noncomputable section)\b[ \t]*([A-Za-z0-9_.'«»]*)")


def git_blob_sha1(data):
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()


def main(argv):
    if len(argv) < 3:
        print(__doc__)
        return 2
    root, out_json = argv[1], argv[2]
    git_ref = git_prefix = repo = None
    if "--git-ref" in argv:
        git_ref = argv[argv.index("--git-ref") + 1]
        git_prefix = argv[argv.index("--git-prefix") + 1]
        repo = argv[argv.index("--repo") + 1]

    # 1. imports of every OAI module
    imports = {}
    lines = {}
    raw = {}
    for dp, _dn, fns in os.walk(os.path.join(root, "OAI")):
        for fn in fns:
            if not fn.endswith(".lean"):
                continue
            p = os.path.join(dp, fn)
            m = path_to_module(root, p)
            with open(p, "rb") as fh:
                data = fh.read()
            raw[m] = data
            txt = data.decode("utf-8")
            lines[m] = txt.count("\n") + (0 if txt.endswith("\n") else 1)
            imps = []
            for ln in strip_comments_and_strings(txt).splitlines():
                mm = IMPORT_RE.match(ln)
                if mm:
                    imps.append(mm.group(1))
            imports[m] = imps

    # 2. closure
    closure, external = set(), Counter()
    missing = set()
    stack = [ROOT_MODULE]
    while stack:
        m = stack.pop()
        if m in closure:
            continue
        if m not in imports:
            missing.add(m)
            continue
        closure.add(m)
        for i in imports[m]:
            if i.startswith("OAI."):
                stack.append(i)
            else:
                external[i] += 1
    closure_sorted = sorted(closure)
    ext_roots = Counter(i.split(".")[0] for i in external)
    ext_nonmathlib = sorted(i for i in external if not i.startswith(("Mathlib", "Lean", "Init", "Std")))

    # longest import chain (depth) inside the closure
    depth = {}

    def dep(m):
        if m in depth:
            return depth[m]
        depth[m] = 0  # cycle guard
        d = 1 + max([dep(i) for i in imports[m] if i in closure] or [0])
        depth[m] = d
        return d

    sys.setrecursionlimit(100000)
    max_depth = dep(ROOT_MODULE)

    # 3. per-directory stats
    def topdir(m):
        parts = m.split(".")
        # OAI.NumberTheory.DirichletL.<X>[...]
        if len(parts) >= 4 and parts[:3] == ["OAI", "NumberTheory", "DirichletL"]:
            return parts[3] if len(parts) > 4 else "(DirichletL root files)"
        return ".".join(parts[:3])

    dir_mods, dir_lines = Counter(), Counter()
    for m in closure:
        dir_mods[topdir(m)] += 1
        dir_lines[topdir(m)] += lines[m]
    not_in_closure = sorted(set(imports) - closure)
    nic_dirs = Counter(topdir(m) for m in not_in_closure)

    # 4. optional git byte-identity check
    git_check = None
    if git_ref:
        res = subprocess.run(["git", "-C", repo, "ls-tree", "-r", git_ref, git_prefix],
                             capture_output=True, text=True, check=True)
        blob = {}
        for ln in res.stdout.splitlines():
            meta, path = ln.split("\t", 1)
            blob[path] = meta.split()[2]
        mism, absent = [], []
        for m in closure_sorted:
            gp = git_prefix.rstrip("/") + "/" + m.replace(".", "/") + ".lean"
            if gp not in blob:
                absent.append(m)
            elif blob[gp] != git_blob_sha1(raw[m]):
                mism.append(m)
        git_check = {"ref": git_ref, "prefix": git_prefix, "closure_files_checked": len(closure_sorted),
                     "blob_mismatches": mism, "absent_in_git": absent}

    # 5. lexical trust scan + declaration index
    hits = defaultdict(list)
    decls = []
    for m in closure_sorted:
        txt = raw[m].decode("utf-8")
        s = strip_comments_and_strings(txt)
        for key, pat in TRUST_PATTERNS.items():
            for mm in re.finditer(pat, s):
                ln = s.count("\n", 0, mm.start()) + 1
                line_txt = txt.splitlines()[ln - 1].strip()
                hits[key].append({"module": m, "line": ln, "text": line_txt[:200]})
        # namespace-aware decl index (approximate)
        ns_stack = []
        events = []
        for mm in NS_RE.finditer(s):
            events.append((mm.start(), "ns", mm.group(1), mm.group(2)))
        for mm in DECL_RE.finditer(s):
            events.append((mm.start(), "decl", mm.group(1), mm.group(2)))
        events.sort()
        for pos, kind, kw, name in events:
            if kind == "ns":
                if kw == "namespace":
                    ns_stack.append(("ns", name))
                elif kw in ("section", "noncomputable section"):
                    ns_stack.append(("sec", name))
                elif kw == "end":
                    if ns_stack:
                        ns_stack.pop()
            else:
                prefix = ".".join(n for t, n in ns_stack if t == "ns" and n)
                full = (prefix + "." + name) if (prefix and name and not name.startswith("_root_.")) else name
                ln = s.count("\n", 0, pos) + 1
                decls.append({"kind": kw, "name": full, "module": m, "line": ln})

    trust_counts = {k: len(v) for k, v in hits.items()}
    for k in TRUST_PATTERNS:
        trust_counts.setdefault(k, 0)
    kinds = Counter(d["kind"] for d in decls)

    out = {
        "root_module": ROOT_MODULE,
        "lean_root": os.path.abspath(root),
        "oai_modules_total": len(imports),
        "oai_lines_total": sum(lines.values()),
        "closure_modules": len(closure),
        "closure_lines": sum(lines[m] for m in closure),
        "longest_import_chain_modules": max_depth,
        "missing_modules": sorted(missing),
        "external_import_roots": dict(ext_roots),
        "external_nonmathlib_imports": ext_nonmathlib,
        "closure_by_dir": {k: {"modules": dir_mods[k], "lines": dir_lines[k]} for k in sorted(dir_mods)},
        "not_in_closure_by_dir": dict(sorted(nic_dirs.items())),
        "git_check": git_check,
        "trust_counts": trust_counts,
        "trust_hits": {k: v for k, v in hits.items()
                       if k not in ("decide (tactic or term)", "set_option maxHeartbeats",
                                    "notation (local/scoped/global)",
                                    "set_option maxRecDepth", "set_option synthInstance.maxHeartbeats",
                                    "set_option (other)")},
        "set_option_other_values": dict(Counter(
            re.sub(r"\s+", " ", h["text"]).split("set_option", 1)[1].strip().split(" ")[0]
            for h in hits.get("set_option (other)", []))),
        "maxHeartbeats_values": dict(Counter(
            (re.search(r"maxHeartbeats\s+(\d+)", h["text"]) or [None, "?"])[1]
            for h in hits.get("set_option maxHeartbeats", []))),
        "maxRecDepth_values": dict(Counter(
            (re.search(r"maxRecDepth\s+(\d+)", h["text"]) or [None, "?"])[1]
            for h in hits.get("set_option maxRecDepth", []))),
        "decl_kind_counts": dict(kinds),
        "notation_texts": dict(Counter(re.sub(r"\s+", " ", h["text"]) for h in
                                       hits.get("notation (local/scoped/global)", [])).most_common(10)),
        "closure_module_list": [{"module": m, "lines": lines[m], "depth": depth.get(m)} for m in closure_sorted],
    }
    with open(out_json, "w") as fh:
        json.dump(out, fh, indent=1, sort_keys=False)
    decl_path = (argv[argv.index("--decls") + 1] if "--decls" in argv
                 else os.path.splitext(out_json)[0] + "_decls.tsv")
    with open(decl_path, "w") as fh:
        fh.write("kind\tname\tmodule\tline\n")
        for d in decls:
            fh.write(f"{d['kind']}\t{d['name']}\t{d['module']}\t{d['line']}\n")

    print(f"OAI modules on disk: {len(imports)} ({sum(lines.values())} lines)")
    print(f"closure of {ROOT_MODULE}: {len(closure)} modules, {out['closure_lines']} lines; "
          f"longest chain {max_depth}; missing {len(missing)}")
    print("external import roots:", dict(ext_roots))
    print("external non-Mathlib imports:", ext_nonmathlib)
    if git_check:
        print(f"git check vs {git_ref}: {git_check['closure_files_checked']} files, "
              f"{len(git_check['blob_mismatches'])} mismatches, {len(git_check['absent_in_git'])} absent")
    print("closure by directory (modules, lines):")
    for k in sorted(dir_mods, key=lambda k: -dir_lines[k]):
        print(f"  {k:40s} {dir_mods[k]:5d} {dir_lines[k]:8d}")
    print("not in closure, by directory:", dict(sorted(nic_dirs.items())))
    print("trust counts:")
    for k in TRUST_PATTERNS:
        print(f"  {k:45s} {trust_counts[k]}")
    print("maxHeartbeats values:", out["maxHeartbeats_values"])
    print("maxRecDepth values:", out["maxRecDepth_values"])
    print("other set_option:", out["set_option_other_values"])
    print("decl kinds:", dict(kinds))
    print("wrote", out_json, "and", decl_path)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
