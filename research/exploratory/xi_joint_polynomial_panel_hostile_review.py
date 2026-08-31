"""Additional unpatched full-reconstruction attacks on frozen JX."""

import copy
import importlib.util
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
SPEC = importlib.util.spec_from_file_location(
    "jx", HERE / "xi_joint_polynomial_panel_transport.py"
)
m = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(m)


def need(ok, why):
    if not ok:
        raise ValueError(why)


def reject(call, why):
    try:
        call()
    except (ValueError, TypeError, OverflowError):
        return
    raise ValueError("unexpected acceptance: " + why)


def main():
    checks = 0
    for raw in (
        b'{"x":1,"x":2}',
        b'{"x":1.0}',
        b'{"x":NaN}',
        b'{"x":Infinity}',
        "{}",
        b" " * (m.MAX_BYTES + 1),
    ):
        reject(lambda raw=raw: m.decode(raw), "strict JSON")
        checks += 1
    for value in ({1: 1}, {"x": 1 << 4097}, [0] * 8001, {"x": "a" * 4097}, {"x": 1.0}):
        reject(lambda value=value: m.canonical(value), "type/cap")
        checks += 1
    deep = None
    for _ in range(26):
        deep = [deep]
    reject(lambda: m.canonical(deep), "depth cap")
    checks += 1
    for index in (True, 1.0, "1", -1, 26):
        reject(lambda index=index: m.point(index, {"index": index}, {}), "strict point")
        checks += 1
    with m.ha.precision(512):
        for index in (True, -1, 64):
            reject(lambda index=index: m.jp.arc_angle(index), "strict arc")
            checks += 1
    original = m.decode(m.FIXTURE.read_bytes())
    for attack in ("remove_tail", "counterfeit_success"):
        bad = copy.deepcopy(original)
        if attack == "remove_tail":
            # Fully change the displayed error sums/outcomes and global summary;
            # no mock/cache bypass replaces the fresh primitive reconstruction.
            for row in bad["records"]:
                tail = m.oa.unpair(row["tail_upper"])
                margin = m.oa.unpair(row["margin_lower"])
                row["tail_upper"] = [0, 1]
                for arc in row["arcs"]:
                    error = m.oa.unpair(arc["error_upper"]) - tail
                    arc["error_upper"] = m.oa.pair(error)
                    arc["strict_pass"] = error < margin
                    arc["status"] = "PASS" if error < margin else "UNRESOLVED"
                row["transport_certified"] = all(a["strict_pass"] for a in row["arcs"])
                row["matched_transport_certified"] = (
                    row["transport_certified"] and row["parent_matched"]
                )
                row["status"] = (
                    "PASS" if row["matched_transport_certified"] else "UNRESOLVED"
                )
        else:
            # Reassign an existing positive record to the unresolved physical node22.
            row = copy.deepcopy(bad["records"][19])
            row["index"] = 22
            row["selection"] = "PRIMARY_UNTRIED"
            bad["records"][22] = row
        bad["summary"] = m.summary(bad["records"])
        bad.pop("payload_sha256")
        bad["payload_sha256"] = m.oa.digest(m.canonical(bad))
        try:
            m.check_report(bad)
        except ValueError as exc:
            need(
                str(exc) == "fresh full26 primitive reconstruction",
                "fresh rejection route",
            )
        else:
            raise ValueError("fully resealed attack accepted: " + attack)
        print("REJECTED fresh", attack, flush=True)
    print("PASS", checks, "strict guards and2 fully resealed unpatched full26 attacks")


if __name__ == "__main__":
    main()
