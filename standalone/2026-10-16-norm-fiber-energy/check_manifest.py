#!/usr/bin/env python3
"""Check local bytes only; no mathematical certification."""
from pathlib import Path
import hashlib
import json


def main() -> None:
    root=Path(__file__).resolve().parent
    manifest=json.loads((root/"MANIFEST.json").read_text())
    actual={str(f.relative_to(root)) for f in root.rglob("*")
            if f.is_file() and "__pycache__" not in f.parts and f.name!="MANIFEST.json"}
    if actual!=set(manifest["files"]):
        raise RuntimeError("unlisted or missing payload files")
    for name, expected in manifest["files"].items():
        data=(root/name).read_bytes()
        got={"bytes":len(data),"sha256":hashlib.sha256(data).hexdigest(),
             "git_blob":hashlib.sha1(f"blob {len(data)}\0".encode()+data).hexdigest()}
        if got!=expected:
            raise RuntimeError(f"byte mismatch: {name}")
    print(f"PASS: {len(actual)} payload files match; no proof certification implied")

if __name__=="__main__":
    main()
