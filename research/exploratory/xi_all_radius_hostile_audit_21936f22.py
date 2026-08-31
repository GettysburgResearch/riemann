"""Extra QR acceptance attacks; this API harness imports the frozen producer."""

import copy
import json
import sys
import time
from fractions import Fraction as Q

import xi_all_radius_transport_obstruction as qr


def need(ok, message):
    if not ok:
        raise ValueError(message)


def rejected(action, label):
    try:
        action()
    except (ValueError, TypeError, UnicodeError):
        return
    raise ValueError("accepted hostile input: " + label)


def main():
    # These checks do not alter source, manifest, fixture or acceptance code.
    guards = [
        (lambda: qr.decode(b'{"x":1,"x":true}'), "duplicate bool key"),
        (lambda: qr.decode(b"-Infinity"), "negative infinity"),
        (lambda: qr.decode(b"1e0"), "float token"),
        (lambda: qr.typed({1: 2}), "nonstring key"),
        (lambda: qr.typed([Q(1, 2)]), "Fraction in JSON"),
        (lambda: qr.typed(1 << 4096), "large integer"),
        (lambda: qr.typed({"x" * 1025: 1}), "large key"),
        (lambda: qr.bounds([[1, -1], [2, 1]]), "negative denominator"),
        (lambda: qr.bounds([[1, 1], [False, 1]]), "boolean endpoint"),
        (lambda: qr.sqrt_interval((Q(0), Q(1)), 1025), "sqrt cap"),
        (lambda: qr.sqrt_interval((Q(0), Q(1)), False), "sqrt bool"),
        (lambda: qr.lf(b"a\x80"), "invalid UTF8"),
        (lambda: qr.lf(b"a\r"), "unpaired CR"),
    ]
    for action, name in guards:
        rejected(action, name)
    original = qr.decode(qr.FIXTURE.read_bytes())
    cases = []
    for label in ("false_unresolved_source_claim", "different_joint_criterion"):
        forged = copy.deepcopy(original)
        if label == "false_unresolved_source_claim":
            row = forged["records"][19]
            need(row["status"] == "UNRESOLVED", "held-out attack node")
            row["status"] = "ALL_RADII_CRITERION_IMPOSSIBLE"
            row["sharp_obstruction"] = True
            row["independent_fraction_comparison"]["sharp"] = True
            forged["summary"]["all_radii_impossible"] += 1
            forged["summary"]["unresolved"] -= 1
        else:
            forged["contract"]["joint_remainder_criterion_ruled_out"] = True
        forged.pop("payload_sha256")
        forged["payload_sha256"] = qr.sha(qr.canonical(forged))
        start = time.monotonic()
        rejected(lambda forged=forged: qr.check_report(forged), label)
        cases.append(
            {
                "attack": label,
                "rejected": True,
                "seconds": round(time.monotonic() - start, 3),
            }
        )
    print(
        json.dumps(
            {
                "optimized": bool(sys.flags.optimize),
                "extra_guards": len(guards),
                "fresh_unmocked_resealed_attacks": cases,
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
