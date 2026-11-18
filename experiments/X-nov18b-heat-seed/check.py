#!/usr/bin/env python3
"""Certify forward height bounds using Raymond's 67 physical source rows."""
import argparse
import hashlib
import json
from math import comb
from pathlib import Path
from zipfile import ZipFile

from flint import fmpq as Rat


INPUTS = {
    "M8_LATE_PLAN.json": "ec346b7c1136eda38021eb6323033b3b48ed21e6f7458eeeac7cc9579db2497a",
    "MAIN_CLOCK_SOURCE.json": "b59905d7b994d3424ba14f9347be75a2429ae4d4b0de2c2404971ffda1d4d536",
}
HEIGHT_DEN = 10**28
RATE_DEN = 10**20


def check(condition, description):
    if not condition:
        raise ValueError(description)


def floor(value):
    return int(value.p // value.q)


def ceil(value):
    return -floor(-value)


def inputs():
    records = []
    with ZipFile(Path(__file__).with_name("raymond-inputs.zip")) as archive:
        for name, digest in INPUTS.items():
            data = archive.read(name)
            check(hashlib.sha256(data).hexdigest() == digest, name)
            records.append(json.loads(data))
    return records[0]["rows"], records[1]["records"]


def prepare(plan, source, counter):
    check(plan["row"] == source["row"] == counter and plan["mode"] == source["mode"], "row identity")
    start, end = map(Rat, plan["time"])
    lo, cap = map(Rat, plan["q_interval"])
    check((start, end) == (Rat(source["t_lo"]), Rat(source["t_hi"])), "thermal cell")
    check((lo, cap) == tuple(map(Rat, source["q_interval"])) and lo == 0 < cap, "full height interval")
    main, debit, first, last = (Rat(source[k]) for k in ("main_lo", "native_debit", "first_hi", "last_hi"))
    check(start < end and first >= last > 0, "increasing source chord")
    intercept = main - debit - first
    slope = (first - last) / (end - start)

    overlay = plan.get("joint_jet_overlay")
    plain_scale = Rat(overlay["alpha"]) if overlay else Rat(1)
    nodes = []
    for node in plan["nodes"]:
        h, v, w = (Rat(node[k]) for k in ("height", "shift", "weight"))
        check(h > 0 and h*h > cap, "ordinary pair pole")
        total = h*h + v*v
        nodes.append((plain_scale*2*w*h, total, 4*v*v))

    jets = []
    for entry in overlay["centres"] if overlay else ():
        p = Rat(entry["p"])
        check(p > 0 and p*p > cap, "jet pole")
        # The mth derivative divided by m! is (-1)^m times the
        # sum of the two (m+1)th reciprocal powers at p +/- sqrt(q).
        polynomials = []
        for m, coefficient in enumerate(map(Rat, entry["b"])):
            n = m + 1
            multiplier = 4 * coefficient * (-1)**m * p**(m-1)
            polynomials.append([multiplier * comb(n, j) * p**(n-j) for j in range(0, n+1, 2)])
        jets.append((p*p, polynomials))
    return start, end, cap, intercept, slope, nodes, jets


def own(q, nodes, jets):
    result = Rat(0)
    for weight, total, four_v_squared in nodes:
        difference = total - q
        result += weight * difference / (difference*difference + four_v_squared*q)
    for pole_squared, polynomials in jets:
        denominator = pole_squared - q
        denominator_power = Rat(1)
        for coefficients in polynomials:
            numerator = Rat(0)
            for coefficient in reversed(coefficients):
                numerator = numerator*q + coefficient
            denominator_power *= denominator
            result += numerator / denominator_power
    return result


def check_constants():
    plan, source = inputs()
    check(len(plan) == len(source) == 67, "row count")
    rates = []
    for index, (p, s) in enumerate(zip(plan, source)):
        _, _, cap, intercept, _, nodes, jets = prepare(p, s, index)
        rates.append((2*(intercept-own(cap,nodes,jets)), index))
    value, index = min(rates)
    check(index == 0 and Rat(12380974,10**6) < value < Rat(12380975,10**6),
          "uniform minimum on the licensed rectangles")
    _, _, _, intercept, _, nodes, jets = prepare(plan[0], source[0], 0)
    value_at_zero = 2*(intercept-own(Rat(0),nodes,jets))
    check(Rat(12651018,10**6) < value_at_zero < Rat(12651019,10**6), "first-row zero-height rate")
    print("12.380974 < minimum licensed rate < 12.380975")
    print("12.651018 < initial zero-height rate < 12.651019")


def run(theta, ticks):
    check(Rat(1,2) <= theta <= Rat(7,8), "seed range")
    check(ticks > 0 and ticks % 800 == 0, "thermal cells on grid")
    mass = ceil(HEIGHT_DEN * ((2*theta-1)**2 + Rat(1,10**13)))
    common = RATE_DEN * ticks
    previous = Rat(0)
    plan, source = inputs()
    check(len(plan) == len(source) == 67, "row count")
    for index, (p, s) in enumerate(zip(plan,source)):
        start, end, cap, intercept, slope, nodes, jets = prepare(p, s, index)
        check(start == previous and (ticks*start).q == (ticks*end).q == 1, "row join")
        previous = end
        for i in range(int(start*ticks), int(end*ticks)):
            q = Rat(mass, HEIGHT_DEN)
            check(0 < q <= cap, f"cap at tick {i}")
            physical = intercept + slope*(Rat(i,ticks)-start)
            k = floor(2*RATE_DEN*(physical-own(q,nodes,jets))) - 1
            check(0 < k < common, f"rate at tick {i}")
            velocity = 2*HEIGHT_DEN*RATE_DEN + k*mass
            if mass*common <= velocity:
                endpoint = Rat(i,ticks) + q/2
                check(Rat(i,ticks) < Rat(19,125) and endpoint < Rat(41,250), "analytic horizons")
                decimal_ceiling = ceil(endpoint * 10**12)
                print(f"theta={theta} steps={i} step_denominator={ticks}")
                print(f"endpoint={endpoint}")
                print(f"upward_decimal={decimal_ceiling // 10**12}.{decimal_ceiling % 10**12:012d}")
                return
            # Integrate q'=-2-(k/RATE_DEN)q. The cubic Taylor lower
            # bound for (1-exp(-x))/x gives an outward rational reset.
            decrease = velocity * (24*common**3 - 12*common**2*k + 4*common*k*k - k**3)
            next_mass = mass - decrease//(24*common**4)
            check(0 < next_mass < mass, f"positive outward endpoint at tick {i}")
            mass = next_mass
    raise ValueError("the barrier has not reached a terminal cell")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("theta", type=Rat, nargs="?", help="rational zero-free abscissa")
    parser.add_argument("--ticks", type=int, default=8192000,
                        help="reciprocal time step, divisible by 800")
    parser.add_argument("--constants", action="store_true", help="verify the analytic transfer constants")
    args = parser.parse_args()
    if args.constants:
        check_constants()
    if args.theta is not None:
        run(args.theta, args.ticks)
    elif not args.constants:
        parser.error("supply a seed or use --constants")
