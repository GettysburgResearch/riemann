# Lane P3 — (w4) The pinch coefficient at rho_1: exact expression and nonvanishing

Setting: P2.5's exact representation (laneP2/THEOREM.md). `a = 3/4 + (3/2)s`,
`s_0 = i gamma_1/3`, pinch point `z* = 1/4 - i gamma_1/2`, kernel
`k(beta) = 1/beta - (1-2^{-beta})/(beta^2 ln 2)`, `rho_1 = 1/2 + i gamma_1`.
The local (cut-hugging) piece `Z_loc` of `B_0` is the object of [P1-LOC].

## Theorem W4 (pinch coefficient: exact form and nonvanishing)

With the P2.6 contour split defining `Z_loc`, the [P1-LOC] leading coefficient is

    c_B = omega * (sqrt3/2) * k(1/2) / ( z* * zeta'(rho_1) ),      |omega| = 1,

where `omega` is a unimodular orientation/branch factor fixed by the parent contour
(irrelevant for `c_0' = (4/(3pi))|c_B|^2`, which consumes `|c_B|^2` only). Hence

    |c_B| = (3/2) |k(1/2)| / ( sqrt3 |z*| |zeta'(rho_1)| )  =  0.04782893516094...  != 0.

**Derivation of the form** (P1 Theorem A instantiated on the genuine kernel; mirrored
geometry). Near the pinch the P2.5 integrand is

    (3/2) [k(1/4+(3/2)s+z)/z] * b(a+z) (z-z_b)^{-1/2} * (-1)/((z-z_p) zeta'(rho_1)) * (1+O(|z-z_p|)),

using `zeta^{1/2}(a+z) = (z-z_b)^{-1/2} b(a+z)`, `b(v) = ((v-1)zeta(v))^{1/2}` locally,
`b(1)=1` (branch point `z_b = 1-a`, cut LEFTWARD in z since the argument is `a+z`, the
mirror of P1's `w-z` model — P1's Theorem A applies verbatim under `z -> -z`), and
`1/zeta(a-z) = -1/((z-z_p) zeta'(rho_1))(1+O(|z-z_p|))` at the simple zero
(`z_p = a - rho_1`; SIMPLICITY INPUT, see below). Endpoint-pinch collapse (P1 Thm A
step (1)-(3)): with `delta := z_p - z_b = 3(s-s_0)` (exact, P2.5) and
`int_0^inf x^{-1/2}(x+delta)^{-1} dx = pi delta^{-1/2}` (principal branch, Re delta > 0
on the probe side Re s = h > 0),

    Z_loc(s) = (3/2) * (k(1/2)/z*) * (1/zeta'(rho_1)) * (3(s-s_0))^{-1/2} * omega * (1 + O(|s-s_0|^{1/2}))

— the frozen amplitude is evaluated at the pinch, where the kernel argument is
`1/4 + (3/2)s_0 + z* = 1/2` exactly and `b(1) = 1`; the factor `3^{-1/2}` comes from
`delta = 3(s-s_0)`. The error exponent `1/2` and the constants are P1's Theorem A with
its explicit `C_A` (amplitude derivative bounds hold: `k` entire in beta near 1/2, `1/z`
analytic near z* since `|z*| = 7.07 != 0`, `b` analytic on `D(1, 4r)`, `1/(Z-part)`
analytic since no other zero is within distance 6 — P2.5's separation bookkeeping).

**Evaluation** (mpmath, dps 50, reproduced at dps 80 with relative shift 1.2e-50;
laneP3/cpinch.py):

    gamma_1        = 14.13472514173469379...
    zeta'(rho_1)   = 0.78329651186703092865 + 0.12469982974817108941 i
    |zeta'(rho_1)| = 0.79316043335650611601
    k(1/2)         = 0.30977762283130429755   [closed form 2 - 4(1-1/sqrt2)/ln2; the two
                     expressions agree to 8e-51 — also = 2(1-(2/ln2)(1-1/sqrt2)), the
                     form P4 measured blind: 0.2489 +- 0.0033 vs k(1/2) sqrt2/sqrt(pi)
                     = 0.247167]
    |z*|           = 7.0717829228629971335  = sqrt(1/16 + gamma_1^2/4)
    |c_B|          = 0.04782893516093999598
    c_0'           = (4/(3pi)) |c_B|^2 = 0.00097089058146581794

**Nonvanishing with a rigorous radius.** `c_B != 0` iff each factor is nonzero:
(i) `k(1/2) != 0` — ELEMENTARY: with the rational sandwiches `1.4142135 < sqrt2 <
1.4142136` (squares straddle 2) and `0.6931471 < ln 2 < 0.6931472` (standard verified
enclosure), exact rational arithmetic gives `k(1/2) in (0.3097773, 0.3097779)`,
strictly positive. (ii) `z* != 0`: `Re z* = 1/4`. (iii) `1/zeta'(rho_1) != 0`:
trivial (`zeta'` is finite). For a certified LOWER bound only upper bounds are needed:
`|zeta'(rho_1)| <= 0.79317`, `|z*| <= 7.07179` give

    |c_B| >= 1.5 * 0.3097773 / (1.7320509 * 7.07179 * 0.79317) = 0.047828 > 0.

Error radius of the quoted digits: the only transcendental inputs are `gamma_1` and
`zeta'(rho_1)`; both are stable to 5e-50 across a precision doubling and
`|zeta'(rho_1)|` matches the classically published value 0.7931604...; the elementary
factors carry exact rational enclosures. Certified: `|c_B| in (0.0478289351, 0.0478289352)`,
`c_0' in (9.70890581e-4, 9.70890582e-4)`; and coarsely but with hand-checkable inputs,
`|c_B| in (0.0478, 0.0479)` — NONZERO.

**Simplicity input, honestly.** The residue extraction `1/zeta(a-z) ~ -1/((z-z_p)
zeta'(rho_1))` uses that `rho_1` is a SIMPLE zero on the critical line. This is
rigorously known by classical verified computation (all zeros with `|Im| <= 60` on the
line and simple — the same input class L-105058.5 step (4) and P2.6 consume; not RH).
If simplicity were ever to be dropped, the expansion changes type (a higher-order pole
pinches the cut — the singularity gets STRONGER, not weaker, but the coefficient formula
above no longer applies). CAUTION on the fallback (hostile-review finding F5): the
L-105058.5-style Schwarz constant `2 max_{|w-rho_1|=1/2} |zeta| = 0.98384` (240-point
circle scan, laneP3/cpinch.py) bounds `|F| = 1/(|s||zeta|)` POINTWISE in L-105058.5's
setting; here the zero factor sits inside a cut INTEGRAL, and a pointwise `|1/zeta|`
lower bound does not by itself lower-bound `|Z_loc|` (phase cancellation is possible).
The correct fallback shape in this setting is P1's (I2) multiplicity variant, not the
pointwise constant; the derived number `|c_B| >= 0.03856` is therefore ILLUSTRATIVE
ONLY. Nothing load-bearing: simplicity of rho_1 is verified, so the main-line formula
stands and no fallback is consumed anywhere.

**Falsifier.** An exact identity forcing `k(1/2) = 0` or a corrected kernel with a zero
at beta = 1/2 (would break the program; P4's blind measurement of the constant at 1.0
+- 0.013 of prediction makes this empirically excluded at the measured scales).

Consistency triangle (independent): P2's calibration 0.047832 (rounded); P4's blind
pinch-constant measurement 0.2489 +- 0.0033 vs 0.247167 and c0'-candidate 0.000971;
this lane's 20-digit evaluation. All agree.

Precision provenance (hostile-review finding F6): "20-digit" is interval-grade
(rational-sandwich) ONLY for the kernel value k(1/2), which has a closed form; the
zeta inputs `gamma_1`, `|zeta'(rho_1)|` are precision-doubled mpmath evaluations
cross-checked against published values, not certified enclosures. The CERTIFIED
statement of record is the lower bound `|c_B| >= 0.047828`, valid given
`|zeta'(rho_1)| <= 0.79317` and `|z*| <= 7.07179`.

Bridge identity (added post-review; the triangle closes ANALYTICALLY, not just
numerically): `sqrt(2/(3 pi)) |c_B| = C_chain/(|rho_1 - 1| |zeta'(rho_1)|)` reduces
to the exact identity `|rho_1 - 1| = 2|z*|`, i.e. `sqrt(1/4 + gamma^2) =
2 sqrt(1/16 + gamma^2/4)` — true for EVERY gamma. Hence `c_0' = C_chain^2 c_0`
exactly (0.061091 x 0.0158924 = 9.709e-4), and the kernel argument at the pinch
equals 1/2 for every zero (gamma-independent) — which is exactly why P4's blind
chain constant is gamma-independent and the two-zero test is structurally
consistent.
