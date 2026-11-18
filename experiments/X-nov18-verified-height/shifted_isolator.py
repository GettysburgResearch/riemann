"""Replayable FLINT 3.6.0 Platt/Turing batches using an offset grid center.

The underscored release function constructs a grid with these explicit inputs
and invokes the same _isolate_zeros as the ordinary local function. Its native
return is the number of certified consecutive open sign brackets. The center
formula and integer tuning constants determine efficiency only.
"""
import ctypes

from isolate import ANCHOR, NativeIsolator, bind


class ShiftedIsolator(NativeIsolator):
    def __init__(self):
        super().__init__()
        pointer, integer = ctypes.c_void_p, ctypes.c_long
        self.arb_alloc = bind(self.library, "_arb_vec_init", pointer, [integer])
        self.arb_clear = bind(self.library, "_arb_vec_clear", None, [pointer, integer])
        self.arb_set = bind(self.library, "arb_set_si", None, [pointer, integer])
        self.arb_shift = bind(self.library, "arb_mul_2exp_si", None, [pointer, pointer, integer])
        self.explicit_isolate = bind(
            self.library, "_acb_dirichlet_platt_isolate_local_hardy_z_zeros", integer,
            [pointer, pointer, integer, pointer, integer, integer, pointer, pointer,
             integer, integer, integer, pointer, integer, integer],
        )
        self.last_parameters = None

    def batch(self, first, requested, precision):
        # Near the historical anchor, the mean spacing is 0.23364675677...
        # The source uses a backward Turing pad before the target index.
        # Avoid consuming most of that pad with a positive offset when the
        # entire requested batch is short.
        offset = min(540, max(0, (requested - 1) * 233647 // 2_000_000))
        center = 3_000_175_332_800 + (first - ANCHOR) * 233647 // 1_000_000 + offset
        parameters = {
            "T": center, "A": 8, "B": 4096, "h_mantissa": 170, "h_exponent": 0,
            "J": 925000, "K": 16, "sigma_grid": 1965, "Ns_max": 200,
            "H_mantissa": 93, "H_exponent": -6, "sigma_interp": 25,
        }
        return self.batch_from_parameters(first, requested, precision, parameters)

    def batch_from_parameters(self, first, requested, precision, parameters):
        if not (0 < first < 2**61 and 0 < requested <= 100000 and 32 <= precision <= 1024):
            raise ValueError("Invalid shifted batch range or precision")
        if not (0 < parameters["T"] < 2**61 and 0 < parameters["J"] < 2**61):
            raise ValueError("Grid center and Dirichlet cutoff must fit immediate fmpz values")
        if (parameters["A"] != 8 or parameters["B"] != 4096
                or parameters["sigma_grid"] != 1965 or parameters["Ns_max"] != 200
                or parameters["sigma_interp"] != 25 or parameters["H_mantissa"] != 93
                or parameters["H_exponent"] != -6):
            raise ValueError("Unknown shifted grid parameter family")
        family = tuple(parameters[key] for key in ("h_mantissa", "h_exponent", "J", "K"))
        if family not in ((925, -3, 953187, 42), (170, 0, 925000, 16)):
            raise ValueError("Unknown Gaussian window or Taylor and Dirichlet cutoffs")
        self.last_parameters = dict(parameters)
        n = ctypes.c_long(first)
        center = ctypes.c_long(parameters["T"])
        cutoff = ctypes.c_long(parameters["J"])
        h, H = self.arb_alloc(1), self.arb_alloc(1)
        vector = self.allocate(2 * requested)
        try:
            for point, name in [(h, "h"), (H, "H")]:
                self.arb_set(point, parameters[f"{name}_mantissa"])
                self.arb_shift(point, point, parameters[f"{name}_exponent"])
            found = self.explicit_isolate(
                vector, ctypes.byref(n), requested, ctypes.byref(center),
                parameters["A"], parameters["B"], h, ctypes.byref(cutoff),
                parameters["K"], parameters["sigma_grid"], parameters["Ns_max"],
                H, parameters["sigma_interp"], precision,
            )
            return self.unpack(vector, requested, found)
        finally:
            self.release(vector, 2 * requested)
            self.arb_clear(h, 1)
            self.arb_clear(H, 1)
