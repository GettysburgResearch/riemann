"""Recompute analytic FLINT error envelopes for each explicitly parameterized Platt call."""

import argparse
import ctypes
import json
import subprocess
from pathlib import Path

from isolate import NativeIsolator, bind

PTR = ctypes.c_void_p
LONG = ctypes.c_long
GRID = "acb_dirichlet_platt_"


class GridErrors:
    def __init__(self):
        self.native = NativeIsolator()
        lib = self.native.library
        self.allocate = bind(lib, "_arb_vec_init", PTR, [LONG])
        self.release = bind(lib, "_arb_vec_clear", None, [PTR, LONG])
        self.set_si = bind(lib, "arb_set_si", None, [PTR, LONG])
        self.shift = bind(lib, "arb_mul_2exp_si", None, [PTR, PTR, LONG])
        self.inflate = bind(lib, "arb_add_error_2exp_si", None, [PTR, LONG])
        self.dump = bind(lib, "arb_dump_str", PTR, [PTR])
        self.sqrt = bind(lib, "arb_sqrt", None, [PTR, PTR, LONG])
        self.sub_ui = bind(lib, "arb_sub_ui", None, [PTR, PTR, ctypes.c_ulong, LONG])
        self.mul = bind(lib, "arb_mul", None, [PTR, PTR, PTR, LONG])
        signatures = {
            "lemma_A5": [LONG, PTR, LONG], "lemma_A7": [LONG, PTR, PTR, LONG, LONG],
            "lemma_32": [PTR, PTR, PTR], "lemma_B1": [LONG, PTR, PTR, PTR],
            "lemma_B2": [LONG, PTR, PTR], "lemma_A9": [LONG, PTR, PTR, LONG],
            "lemma_A11": [PTR, PTR, LONG], "i_bound": [PTR, LONG, PTR, LONG],
            "bound_C3": [PTR, LONG, PTR, LONG],
        }
        self.bounds = {n: bind(lib, GRID+n, None, [PTR, *types, LONG])
                       for n, types in signatures.items()}

    def exponent(self, ball):
        string = self.dump(ball)
        try:
            parts = ctypes.string_at(string).split()
            mid, em, rad, er = map(lambda part: int(part, 16), parts)
            if (not mid and em) or (not rad and er):
                raise ArithmeticError("Nonfinite native analytic error enclosure")
            upper = [abs(value).bit_length() + exp for value, exp in ((mid, em), (rad, er)) if value]
            if not upper:
                raise ArithmeticError("A positive error term unexpectedly vanished")
            return max(upper) + int(len(upper) == 2)
        finally:
            self.native.free(string)

    def capture(self, p, prec):
        balls = [self.allocate(1) for _ in range(8)]
        T, tgrid, h, H, xi, zero, factor, out = balls
        try:
            self.set_si(T, p["T"])
            self.set_si(tgrid, p["T"])
            self.inflate(tgrid, 12)  # Contains the entire width-4096 grid and adjacent nodes.
            self.set_si(h, p["h_mantissa"])
            self.shift(h, h, p["h_exponent"])
            self.set_si(H, p["H_mantissa"])
            self.shift(H, H, p["H_exponent"])
            self.set_si(xi, 1)
            self.shift(xi, xi, -13)  # 1/(2B), B=4096.
            if p["B"] != 4096:
                raise ArithmeticError("Unexpected grid width")
            self.set_si(factor, p["J"])
            self.sqrt(factor, factor, prec)
            self.shift(factor, factor, 1)
            self.sub_ui(factor, factor, 1, prec)
            j = LONG(p["J"])
            A, B, K, sig = (p[key] for key in ("A", "B", "K", "sigma_grid"))

            def bound(name, *args):
                self.bounds[name](out, *args, prec)
                return self.exponent(out)

            result = {
                "A5_by_k": [bound("lemma_A5", B, h, k) for k in range(K)],
                "A7_by_k": [bound("lemma_A7", sig, T, h, k, A) for k in range(K)],
                "lemma32_all_x": bound("lemma_32", h, T, zero),
                "B1": bound("lemma_B1", sig, T, h, ctypes.byref(j)),
                "A9": bound("lemma_A9", sig, T, h, A),
                "A11": bound("lemma_A11", T, h, B),
                "interpolation_alias_full_grid": bound("i_bound", tgrid, A, H, p["sigma_interp"]),
            }
            self.bounds["lemma_B2"](out, K, h, xi, prec)
            self.mul(out, out, factor, prec)
            result["B2_scaled"] = self.exponent(out)
            trunc = [bound("bound_C3", tgrid, A, H, ns) for ns in range(1, p["Ns_max"]+1)]
            result["interpolation_C3_full_support"] = trunc[-1]
            result["interpolation_C3_any_allowed_support"] = max(trunc)
            return result
        finally:
            for ball in balls:
                self.release(ball, 1)


def default_parameters(probe, call):
    if not 10**7 <= call["first_index"] < 2*10**17:
        raise ValueError("Outside the tagged default planner branch with Ns_max=200")
    args = [str(probe.resolve()), str(call["first_index"]), str(call["precision"])]
    fields = subprocess.check_output(args, text=True).strip().split("\t")
    center, A, B, J, K, sigma, sigma_i, prec = map(int, fields[:8])
    if prec != call["precision"] or len(fields) != 10:
        raise ArithmeticError("Malformed native planner trace")
    values = {"T": center, "A": A, "B": B, "J": J, "K": K, "sigma_grid": sigma,
              "sigma_interp": sigma_i, "Ns_max": 200}
    for name, record in zip(("h", "H"), fields[8:]):
        mantissa, exponent, radius, radius_exp = (int(x, 16) for x in record.split())
        if not 0 < mantissa < 2**62 or radius or radius_exp:
            raise ArithmeticError("Default planner produced a nonexact compact window")
        values[name+"_mantissa"], values[name+"_exponent"] = mantissa, exponent
    return values


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    here = Path(__file__).parent
    parser.add_argument("--blocks", type=Path, default=here / "blocks")
    parser.add_argument("--first", type=int, default=50)
    parser.add_argument("--stop", type=int, required=True)
    parser.add_argument("--output", type=Path, default=here / "grid-errors")
    parser.add_argument("--verify", action="store_true")
    parser.add_argument("--native-probe", type=Path,
                        help="compiled capture_default_grid.c for default-grid calls")
    args = parser.parse_args()
    engine = GridErrors()
    args.output.mkdir(exist_ok=True, parents=True)
    for number in range(args.first, args.stop):
        manifest = json.loads((args.blocks / f"{number:04d}.json").read_text())
        calls, stock = [], []
        for call in manifest["calls"]:
            if "shifted_parameters" in call:
                calls.append({"raw_stream_sha256": call["stream_sha256"],
                              "error_exponents": engine.capture(call["shifted_parameters"], call["precision"])})
        result = {"block": number, "stream_sha256": manifest["stream_sha256"], "explicit_grid_calls": calls}
        if args.native_probe:
            for call in manifest["calls"]:
                if "shifted_parameters" not in call:
                    parameters = default_parameters(args.native_probe, call)
                    stock.append({"raw_stream_sha256": call["stream_sha256"],
                                  "captured_parameters": parameters,
                                  "error_exponents": engine.capture(parameters, call["precision"])})
        if stock:
            result["default_grid_calls"] = stock
        path = args.output / f"{number:04d}.json"
        if args.verify:
            if json.loads(path.read_text()) != result:
                raise ArithmeticError(f"Analytic error record differs in block {number}")
        else:
            tmp = path.with_suffix(".tmp")
            tmp.write_text(json.dumps(result, separators=(",", ":")) + "\n")
            tmp.replace(path)


if __name__ == "__main__":
    main()
