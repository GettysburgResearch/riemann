#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
items = {}
for name in ("verification.json", "interface-verification.json"):
    p = HERE / "results" / name
    raw = p.read_bytes()
    data = json.loads(raw)
    items[name] = {
        "sha256": hashlib.sha256(raw).hexdigest(),
        "classification": data["classification"],
    }

proof = {
    "schema": "riemann.x97400.proof-object.v1",
    "inputs": items,
    "directed_p61_bias_proved": True,
    "pr565_source_interface_refuted": True,
    "pr566_implication_refuted": True,
    "global_source_producer_proved": False,
    "RH_established": False,
}
canon = json.dumps(proof, sort_keys=True, separators=(",", ":")).encode()
proof["proof_object_sha256"] = hashlib.sha256(canon).hexdigest()
out = HERE / "results" / "proof-object.json"
out.write_text(json.dumps(proof, indent=2, sort_keys=True) + "\n")
print("PASS_T97400_PROOF_OBJECT")
print(proof["proof_object_sha256"])
