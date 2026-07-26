#!/usr/bin/env python3
"""ctypes binding for Arb's Platt-method batch zero isolation.

Agent: fable5-01   Issue: #55

`O-5610` measured `acb.zeta_zeros` (the generic zero finder exposed by
python-flint) at `15.7` s per zero at index `4.3e13` and concluded the library
route loses to sign-sampling by `56x`.  But FLINT ships a second, unexposed
backend: `acb_dirichlet_platt_local_hardy_z_zeros`, Platt's method, which
evaluates `Z` on a whole block by FFT multi-evaluation instead of one ordinate
at a time.  That is the algorithm behind the record verifications, and it is
exported from the bundled `libflint` -- just not wrapped by python-flint.

This module reaches it with ctypes.

    slong acb_dirichlet_platt_local_hardy_z_zeros(
        arb_ptr res, const fmpz_t n, slong len, slong prec)

isolates `len` consecutive zeros of Hardy's `Z`, starting at the zero of index
`n` (1-based), each returned as an `arb` ball.  The return value is how many it
actually isolated (0 on failure).  An isolated ball of a `Z`-zero is a
certified critical-line zero, so a successful run of `len` zeros starting at
index `N(a)+1` whose balls all lie inside `(a,b)` gives `N_0 >= len` directly
-- the same predicate `certify_gram.py` feeds, from a different engine.

Memory layout (verified at import time by a round-trip test rather than
assumed): on x86-64, `arb_struct` is `arf_struct` (4 words) + `mag_struct`
(2 words) = 48 bytes.
"""
from __future__ import annotations

import ctypes
import ctypes.util
import glob
import os

_LIB = None
ARB_STRUCT_SIZE = 48


def lib():
    global _LIB
    if _LIB is None:
        cands = glob.glob("/usr/local/lib/python3*/dist-packages/python_flint.libs/libflint*.so*")
        if not cands:
            raise RuntimeError("bundled libflint not found")
        _LIB = ctypes.CDLL(cands[0])
        _setup(_LIB)
        _verify_layout(_LIB)
    return _LIB


def _setup(L):
    L._arb_vec_init.restype = ctypes.c_void_p
    L._arb_vec_init.argtypes = [ctypes.c_long]
    L._arb_vec_clear.restype = None
    L._arb_vec_clear.argtypes = [ctypes.c_void_p, ctypes.c_long]
    L.arb_get_str.restype = ctypes.c_char_p
    L.arb_get_str.argtypes = [ctypes.c_void_p, ctypes.c_long, ctypes.c_ulong]
    L.arb_set_si.restype = None
    L.arb_set_si.argtypes = [ctypes.c_void_p, ctypes.c_long]
    L.acb_dirichlet_platt_local_hardy_z_zeros.restype = ctypes.c_long
    L.acb_dirichlet_platt_local_hardy_z_zeros.argtypes = [
        ctypes.c_void_p, ctypes.POINTER(ctypes.c_long), ctypes.c_long, ctypes.c_long]
    L.acb_dirichlet_platt_hardy_z_zeros.restype = ctypes.c_long
    L.acb_dirichlet_platt_hardy_z_zeros.argtypes = [
        ctypes.c_void_p, ctypes.POINTER(ctypes.c_long), ctypes.c_long, ctypes.c_long]
    L.acb_dirichlet_hardy_z_zeros.restype = None
    L.acb_dirichlet_hardy_z_zeros.argtypes = [
        ctypes.c_void_p, ctypes.POINTER(ctypes.c_long), ctypes.c_long, ctypes.c_long]


def _verify_layout(L):
    """Round-trip integers through an arb vector at the assumed stride.

    If ARB_STRUCT_SIZE were wrong, writes at index i would land astride the
    true entries and the read-back would be garbage.  Fail loudly rather than
    ever interpret misaligned memory as a certified ordinate.
    """
    n = 8
    v = L._arb_vec_init(n)
    try:
        for i in range(n):
            L.arb_set_si(v + i * ARB_STRUCT_SIZE, 1000 + i)
        for i in range(n):
            s = L.arb_get_str(v + i * ARB_STRUCT_SIZE, 10, 0).decode()
            # an exact small integer prints with no radius; a stride error
            # would read astride two entries and produce garbage or a ball
            if "+/-" in s or float(s) != 1000 + i:
                raise RuntimeError(
                    "arb_struct stride %d failed round-trip at %d: got %r"
                    % (ARB_STRUCT_SIZE, i, s))
    finally:
        L._arb_vec_clear(v, n)


def platt_zeros(n_start: int, count: int, prec: int = 64, local: bool = True,
                digits: int = 30):
    """Isolate `count` consecutive Z-zeros starting at 1-based index `n_start`.

    Returns (isolated, list-of-ball-strings).  `n_start` must fit in a small
    fmpz (one signed word, < 2^62), which holds to far beyond any height
    reachable here; guarded anyway.
    """
    if not (0 < n_start < 2 ** 61):
        raise ValueError("index out of small-fmpz range")
    L = lib()
    fz = ctypes.c_long(n_start)          # small fmpz is a single word
    v = L._arb_vec_init(count)
    try:
        fn = (L.acb_dirichlet_platt_local_hardy_z_zeros if local
              else L.acb_dirichlet_platt_hardy_z_zeros)
        got = fn(v, ctypes.byref(fz), count, prec)
        out = [L.arb_get_str(v + i * ARB_STRUCT_SIZE, digits, 0).decode()
               for i in range(got)]
        return got, out
    finally:
        L._arb_vec_clear(v, count)


if __name__ == "__main__":
    import argparse
    import time

    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, required=True, help="1-based start index")
    ap.add_argument("--count", type=int, default=50)
    ap.add_argument("--prec", type=int, default=64)
    ap.add_argument("--global-variant", action="store_true")
    args = ap.parse_args()

    t0 = time.time()
    got, balls = platt_zeros(args.n, args.count, args.prec,
                             local=not args.global_variant)
    dt = time.time() - t0
    print("requested %d from index %d at prec %d -> isolated %d  [%.1f s, %s]"
          % (args.count, args.n, args.prec, got, dt,
             ("%.3f s/zero" % (dt / got)) if got else "n/a"))
    for s in balls[:5]:
        print("   ", s)
    if got > 5:
        print("    ...")
        print("   ", balls[-1])
