#!/usr/bin/env python3
"""Check transport integrity of the sealed Observatory checkpoint 14 package."""

import argparse
import hashlib
import json
from pathlib import Path
import re
import stat
import subprocess
import sys
import zipfile


DIGEST = "9f1dcab0d244f667e90cdf712eea15c6f07b8141c1adaee7569f26774c57a198"
SIZE = 21_554_391
MEMBER_COUNT = 2_888
PIN_COUNT = 24
PREFIX = "riemann-observatory/"
ARCHIVE = "archive/riemann-observatory"
ZIP_PATH = "artifacts/riemann-observatory-checkpoint14.zip"
SIDECAR = ZIP_PATH + ".sha256"
RECEIPT = "verification/checkpoint14_sealed_validation.json"


def require(condition, message):
    if not condition:
        raise ValueError(message)


def read_regular(root, name):
    path = root
    parts = name.split("/")
    for part in parts[:-1]:
        path /= part
        require(stat.S_ISDIR(path.lstat().st_mode), f"Expected directory: {path}")
    path /= parts[-1]
    require(stat.S_ISREG(path.lstat().st_mode), f"Expected regular file: {path}")
    return path.read_bytes()


def expected_members(sealed):
    names = set()
    for member in sealed.infolist():
        name = member.filename.removeprefix(PREFIX)
        require(
            member.orig_filename == member.filename
            and member.filename.startswith(PREFIX)
            and "\\" not in name
            and all(part not in {"", ".", ".."} for part in name.split("/")),
            f"Unsafe ZIP path: {member.orig_filename!r}",
        )
        kind = stat.S_IFMT(member.external_attr >> 16)
        require(not member.is_dir() and kind in (0, stat.S_IFREG), f"Unexpected ZIP type: {name}")
        require(name not in names, f"Duplicate ZIP path: {name}")
        names.add(name)
    require(len(names) == MEMBER_COUNT, "Unexpected ZIP member count")
    return names


def verify_extracted(root, sealed, members):
    # Include the ancestor directories as well so empty extras and directory symlinks fail.
    directories = {ARCHIVE}
    for name in members:
        parts = (ARCHIVE + "/" + name).split("/")
        directories.update("/".join(parts[:i]) for i in range(1, len(parts)))
    expected_files = {ARCHIVE + "/" + name for name in members}
    actual_files = set()
    pending = ["archive"]
    while pending:
        relative = pending.pop()
        directory = root / relative
        require(stat.S_ISDIR(directory.lstat().st_mode), f"Expected directory: {relative}")
        for path in directory.iterdir():
            name = path.relative_to(root).as_posix()
            kind = path.lstat().st_mode
            if stat.S_ISDIR(kind):
                require(name in directories, f"Unexpected archive directory: {name}")
                pending.append(name)
            else:
                require(stat.S_ISREG(kind) and name in expected_files, f"Unexpected archive path: {name}")
                member_name = PREFIX + name.removeprefix(ARCHIVE + "/")
                require(path.read_bytes() == sealed.read(member_name), f"Archive bytes differ: {name}")
                actual_files.add(name)
    require(actual_files == expected_files, f"Missing archive files: {sorted(expected_files - actual_files)[:5]}")


def verify_sealed(root, members):
    receipt = json.loads(read_regular(root, RECEIPT))
    require(
        receipt["checkpoint"] == "checkpoint14"
        and receipt["archive_sha256"] == DIGEST
        and receipt["archive_bytes"] == SIZE,
        "Sealed receipt identifies a different artifact",
    )
    pins = receipt["code_pins"]
    require(
        len(pins) == PIN_COUNT and len({pin["result"] for pin in pins}) == PIN_COUNT,
        "Expected 24 distinct result code pins",
    )
    archive = root / ARCHIVE
    args = [
        sys.executable, "-B", "-E", str(archive / "scripts/validate_sealed_checkpoint.py"),
        str(root / ZIP_PATH), "--checkpoint", "14", "--bytes", str(SIZE), "--sha256", DIGEST,
        "--pdf", str(archive / "final_synthesis/synthesis.pdf"),
        "--html", str(archive / "final_synthesis/synthesis.html"),
    ]
    for pin in pins:
        result, source = pin["result"], pin["source"]
        require(result in members and source in members, f"Unarchived result or source: {result}")
        digest = pin["sha256"]
        require(
            hashlib.sha256((archive / source).read_bytes()).hexdigest() == digest,
            f"Sealed receipt source hash mismatch: {source}",
        )
        args.extend(["--code-pin", f"{result}={source}"])
    outcome = subprocess.run(args, capture_output=True, check=False)
    require(outcome.returncode == 0, f"Sealed validator failed: {outcome.stderr.decode(errors='replace').strip()}")
    require(json.loads(outcome.stdout)["validation"] == "PASS", "Sealed validator did not report PASS")


def run_git(root, *args):
    return subprocess.check_output(["git", "-C", str(root), *args])


def verify_git(root, reference, sealed, members, zip_bytes, sidecar):
    git_root = Path(run_git(root, "rev-parse", "--show-toplevel").decode().rstrip("\n")).resolve()
    relative_root = root.relative_to(git_root).as_posix()
    prefix = b"" if relative_root == "." else relative_root.encode("utf-8") + b"/"
    commit = run_git(root, "rev-parse", "--verify", "--end-of-options", reference + "^{commit}").decode().strip()
    require(re.fullmatch(r"[0-9a-f]{40}|[0-9a-f]{64}", commit), "Invalid resolved Git commit")
    # Root the pathspec and keep it literal even when a checkout directory contains glob characters.
    paths = [f":(top,literal){(prefix + name.encode()).decode()}" for name in ("archive", ZIP_PATH, SIDECAR)]
    records = run_git(git_root, "ls-tree", "-rz", "--full-tree", commit, "--", *paths)
    blobs = {}
    for record in records.split(b"\0"):
        if not record:
            continue
        metadata, name = record.split(b"\t", 1)
        mode, kind, oid = metadata.split()
        require(name.startswith(prefix), f"Git path outside package: {name!r}")
        require(mode in {b"100644", b"100755"} and kind == b"blob", f"Unexpected Git mode or type: {name!r}")
        blobs[name.removeprefix(prefix)] = oid
    expected = {(ARCHIVE + "/" + name).encode() for name in members}
    expected.update({ZIP_PATH.encode(), SIDECAR.encode()})
    require(set(blobs) == expected, "Git archive and artifact paths differ from the sealed package")
    with subprocess.Popen(
        ["git", "-C", str(git_root), "cat-file", "--batch"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
    ) as batch:
        for name, oid in blobs.items():
            batch.stdin.write(oid + b"\n")
            batch.stdin.flush()
            fields = batch.stdout.readline().split()
            require(len(fields) == 3 and fields[:2] == [oid, b"blob"], f"Cannot read Git blob: {name!r}")
            length = int(fields[2])
            if name == ZIP_PATH.encode():
                expected_bytes = zip_bytes
            elif name == SIDECAR.encode():
                expected_bytes = sidecar
            else:
                member = PREFIX + name.decode("utf-8").removeprefix(ARCHIVE + "/")
                expected_bytes = sealed.read(member)
            # Drain this record before raising so the batch process cannot block on a full pipe.
            contents = batch.stdout.read(length)
            separator = batch.stdout.read(1)
            require(contents == expected_bytes and separator == b"\n", f"Git blob bytes differ: {name!r}")
        batch.stdin.close()
        require(batch.wait() == 0, "git cat-file batch failed")
    return commit


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent, help="Package directory")
    parser.add_argument("--git-ref", metavar="REF", help="Also compare committed Git blobs at this ref")
    options = parser.parse_args()
    root = options.root.resolve()
    try:
        zip_bytes = read_regular(root, ZIP_PATH)
        require(len(zip_bytes) == SIZE, "Sealed ZIP byte count differs")
        require(hashlib.sha256(zip_bytes).hexdigest() == DIGEST, "Sealed ZIP SHA-256 differs")
        sidecar = read_regular(root, SIDECAR)
        require(sidecar == f"{DIGEST}  {Path(ZIP_PATH).name}\n".encode(), "Checksum sidecar differs")
        with zipfile.ZipFile(root / ZIP_PATH) as sealed:
            members = expected_members(sealed)
            verify_extracted(root, sealed, members)
            verify_sealed(root, members)
            commit = verify_git(root, options.git_ref, sealed, members, zip_bytes, sidecar) if options.git_ref else None
        report = {
            "validation": "PASS",
            "checkpoint": 14,
            "zip_sha256": DIGEST,
            "zip_bytes": SIZE,
            "archive_members": len(members),
            "code_pins": PIN_COUNT,
        }
        if commit:
            report["git_commit"] = commit
        print(json.dumps(report))
    except (OSError, ValueError, KeyError, TypeError, zipfile.BadZipFile, subprocess.CalledProcessError) as exc:
        parser.exit(1, f"Checkpoint verification failed: {exc}\n")


if __name__ == "__main__":
    main()
