"""Additional unmocked acceptance attacks on the frozen selected-point packet."""

import copy
import json
from fractions import Fraction as Q

import xi_joint_polynomial_point_transport as source


def reject(call):
    try:
        call()
    except (ValueError, TypeError, OverflowError):
        return
    raise RuntimeError("hostile input was accepted")


def reseal(value):
    value.pop("payload_sha256", None)
    value["payload_sha256"] = source.oa.digest(source.canonical(value))
    return value


def main():
    report = source.decode(source.FIXTURE.read_bytes())
    controls = 0
    for pair in ([False, 1], [1, False], [0, -1], [3, 6], [1], [1, 2, 3]):
        reject(lambda pair=pair: source.oa.unpair(pair))
        controls += 1
    for raw in (b'{"x":1,"x":1}', b"[1.0]", b"[NaN]", b"[Infinity]"):
        reject(lambda raw=raw: source.decode(raw))
        controls += 1
    with source.ha.precision(512):
        for index in (False, -1, 64, Q(2)):
            reject(lambda index=index: source.arc_angle(index))
            controls += 1
        for radius in (Q(-1, 10), Q(7, 8), Q(9, 8)):
            reject(lambda radius=radius: source.joint_tail(Q(1), radius, source.arb(1)))
            controls += 1
    attacks = []
    wrong_node = copy.deepcopy(report)
    wrong_node["record"]["node_index"] = 18
    reject(lambda: source.check_report(reseal(wrong_node)))
    attacks.append("fully resealed relabelled physical point")
    no_tail = copy.deepcopy(report)
    record = no_tail["record"]
    record["tail_upper"] = [0, 1]
    for arc in record["arcs"]:
        arc["tail_upper"] = [0, 1]
        arc["error_upper"] = copy.deepcopy(arc["polynomial_upper"])
        ratio = Q(*arc["error_upper"]) / Q(*arc["margin_lower"])
        arc["error_over_margin"] = [ratio.numerator, ratio.denominator]
    reject(lambda: source.check_report(reseal(no_tail)))
    attacks.append("fully resealed deleted tail with self-consistent error ratios")
    print(
        json.dumps(
            {
                "strict_guards": controls,
                "fresh_unmocked_rejected": attacks,
                "status": "PASS",
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
