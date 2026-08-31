"""Extra genuinely fresh JR acceptance attacks; imports source only as API."""

import copy
import json
import sys
import time

import xi_quadratic_joint_remainder_transport as jr


def rejected(action):
    try:
        action()
    except (ValueError, TypeError, UnicodeError):
        return
    raise ValueError("hostile input accepted")


def main():
    guards = [
        lambda: jr.decode(b'{"a":1,"a":false}'),
        lambda: jr.decode(b"-Infinity"),
        lambda: jr.decode(b"1e0"),
        lambda: jr.validate_tree({1: 0}),
        lambda: jr.validate_tree(1 << 12288),
        lambda: jr.unpair([True, 1]),
        lambda: jr.unpair([1, False]),
        lambda: jr.integer(True, 0, 2),
        lambda: jr.rational(1.0),
        lambda: jr.decode("{}"),
        lambda: jr.commit_object(jr.BINDINGS[0]["git_blob"]),
        lambda: jr.read_source(dict(jr.BINDINGS[0], path="a/../b")),
        lambda: jr.read_source(dict(jr.BINDINGS[0], path="/a")),
    ]
    for guard in guards:
        rejected(guard)
    original = jr.decode(jr.FIXTURE.read_bytes())
    results = []
    for attack in ("forged_contained_transport", "changed_source_M3_and_domain"):
        bad = copy.deepcopy(original)
        row = next(r for r in bad["records"] if r["full_parent_rectangle_contained"])
        if attack == "forged_contained_transport":
            row["transport_certified"] = True
            row["matched_parent_root"] = True
            row["status"] = "MATCHED_PARENT"
            bad["summary"]["joint_certified_cells"] = 1
            bad["summary"]["joint_matched_cells"] = 1
            bad["summary"]["joint_noncertified_cells"] = 389
        else:
            row["source_M3_upper"] = [0, 1]
            row["source_region_radius"] = [1000, 1]
            row["joint_error"] = [[0, 1], [0, 1]]
        bad.pop("payload_sha256")
        bad["payload_sha256"] = jr.digest(jr.canonical(bad))
        start = time.monotonic()
        rejected(lambda bad=bad: jr.check_report(bad))
        results.append(
            {
                "attack": attack,
                "rejected": True,
                "seconds": round(time.monotonic() - start, 3),
            }
        )
    print(
        json.dumps(
            {
                "optimized": bool(sys.flags.optimize),
                "strict_guards": len(guards),
                "fresh_unmocked_attacks": results,
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
