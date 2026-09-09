"""World schema contract for the cross-world survival/mechanism matrix.

One schema, two views:
  - the #764 survival ladder L0..L9 (issue #764, 'Structural survival ladder');
  - the #763 mechanism axes (Euler product, duality/FE, trace formula,
    positivity/purity, tensor operations, family membership).

Every cell carries its own status, rigor label, witness, and citation.  A
FAILS cell must carry a witness (exact object or precise citation).  Nothing
in a world record is a claim about RH; every record embeds
rh_established=false.
"""

import json
import os

LADDER = ["L0_WELL_DEFINED", "L1_MULTIPLICATIVITY", "L2_EULER_PRODUCT",
          "L3_BOUNDED_DEGREE_RATIONAL", "L4_WEIGHT_DUALITY",
          "L5_CONDUCTOR_GAMMA_ROOT", "L6_CONTINUATION_FE",
          "L7_TWIST_TENSOR_COMPAT", "L8_REALIZATION",
          "L9_EXPLICIT_FORMULA_POSITIVITY"]

MECHANISMS = ["EULER_PRODUCT", "DUALITY_FE", "TRACE_FORMULA",
              "POSITIVITY_PURITY", "TENSOR_OPS", "FAMILY"]

CELL_STATUS = ["HOLDS", "FAILS", "OPEN", "CONJECTURAL", "NOT_APPLICABLE"]
CELL_RIGOR = ["PROVED_HERE", "IMPORTED_THEOREM", "EXACT_WITNESS",
              "REFUTED_BY_WITNESS", "NON_DIRECTED_NUMERIC",
              "SYNTHETIC_CONTROL", "OPEN"]
CL_STATUS = ["THEOREM", "CONJECTURE", "FALSE", "NOT_FORMULATED", "OPEN"]

REQUIRED = ["id", "title", "definition", "arithmetic_class", "ladder",
            "mechanisms", "critical_line", "sources", "rh_established"]


def cell(status, rigor, witness="", citation=""):
    assert status in CELL_STATUS, status
    assert rigor in CELL_RIGOR, rigor
    if status in ("FAILS",) and not (witness or citation):
        raise ValueError("FAILS cell requires a witness or citation")
    if rigor in ("EXACT_WITNESS", "REFUTED_BY_WITNESS") and not witness:
        raise ValueError(f"{rigor} requires a witness")
    return {"status": status, "rigor": rigor, "witness": witness,
            "citation": citation}


def validate_world(w: dict) -> list:
    """Return a list of problems (empty list = valid)."""
    probs = []
    for k in REQUIRED:
        if k not in w:
            probs.append(f"missing key {k}")
    if w.get("rh_established") is not False:
        probs.append("rh_established must be literal false")
    for name, keys in (("ladder", LADDER), ("mechanisms", MECHANISMS)):
        block = w.get(name, {})
        for k in keys:
            if k not in block:
                probs.append(f"{name} missing {k}")
                continue
            c = block[k]
            if c.get("status") not in CELL_STATUS:
                probs.append(f"{name}.{k} bad status {c.get('status')}")
            if c.get("rigor") not in CELL_RIGOR:
                probs.append(f"{name}.{k} bad rigor {c.get('rigor')}")
            if c.get("status") == "FAILS" and not (c.get("witness") or c.get("citation")):
                probs.append(f"{name}.{k} FAILS without witness/citation")
        for k in block:
            if k not in keys:
                probs.append(f"{name} has unknown key {k}")
    cl = w.get("critical_line", {})
    if cl.get("status") not in CL_STATUS:
        probs.append(f"critical_line bad status {cl.get('status')}")
    if cl.get("status") == "FALSE" and not (cl.get("witness") or cl.get("citation")):
        probs.append("critical_line FALSE without witness/citation")
    return probs


def save_world(w: dict, directory: str) -> str:
    probs = validate_world(w)
    if probs:
        raise ValueError("invalid world record: " + "; ".join(probs))
    path = os.path.join(directory, w["id"] + ".json")
    with open(path, "w") as f:
        json.dump(w, f, indent=1, sort_keys=True, default=str)
        f.write("\n")
    return path


def load_worlds(directory: str) -> dict:
    out = {}
    for fn in sorted(os.listdir(directory)):
        if fn.endswith(".json"):
            with open(os.path.join(directory, fn)) as f:
                w = json.load(f)
            out[w["id"]] = w
    return out
