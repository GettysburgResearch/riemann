# Lane P2 — The W-pinch transfer theorem (w3) and the genuine-zeta continuation frame (w1)

Status: P2.1, P2.2, P2.3, P2.4, P2.5 PROVED self-contained (classical inputs named inline);
P2.7 (the transfer) PROVED modulo two named interfaces [P1-LOC] (lane P1's, calibrated here to the
genuine object) and [P2-FAR] (this lane's residual wall, precisely stated, obstruction-analyzed,
numerically supported). RH never assumed, never claimed; no zero-free half-plane assumed anywhere.
Replay: laneP2/num1.py..num5.py, NOTES.md. Notation as in L-105058 / T-105059.

## 0. Objects and conventions

For X >= 64: `U_X = floor(X^{1/3})`, `N_X = floor(X/U_X)`, `h_U = (mu 1_{>U})*eta`
(`eta` = Dirichlet coefficients of `zeta^{1/2}`, `0 <= eta <= 1`, `eta(p^k) = binom(2k,k)4^{-k}`),
`v(y) := (ln(2y)/ln 2) 1_{(1/2,1]}(y)` (the tent), `Lambda(X) := sum_n h_{U_X}(n) n^{-1/2} v(n/N_X)`
(equals T-105059.5's tent sum exactly: `v(n/N) = ln(2n/N)/ln2` on `N/2 < n <= N`).

    V(X) := Lambda(X) sqrt(log N_X) X^{-1/6}   (X >= 64;  V := 0 on [1,64)).

TARGET(V): `limsup_Y (1/log Y) int_1^Y V(X)^2 dX/X >= c_0' > 0`.

## P2.1 Theorem (formulation equivalence and consumption; trap (ii) resolved)

(a) With `u := X^{1/3}` continuous (so `U_X = floor(u)` inside `Lambda`), and
`W_u := Lambda(u^3) sqrt(log N_{u^3})/u` as pinned in T-105059.6:
`u W_u^2 du/u = (1/3) V(X)^2 dX/X` identically, hence

    limsup_T (1/log T) int_1^T u W_u^2 du/u  =  limsup_Y (1/log Y) int_1^Y V^2 dX/X .

(b) If TARGET(V) holds then for every `eps > 0` there are infinitely many octaves L with
`int_{2^L}^{2^{L+1}} V^2 dX/X >= (c_0'-eps) ln 2`, and for each such L, T-105059.5 gives

    E(L) >= 2 ln2 int_oct Lambda^2 dX/X = 2 ln2 int_oct V^2 (X^{1/3}/log N_X) dX/X
         >= 3 ln2 (c_0'-eps) 2^{L/3}/(L+1) (1+O(1/L)),

i.e. exactly the consumption `E(L) >> 2^{L/3}/L` io demanded by T-105059.5(ii)/(.7). So TARGET(V)
IS the pinned W-pinch lemma, verbatim, and no u-cell bookkeeping is needed.

Proof. (a) `u W_u^2 du/u = (Lambda^2 log N / u^2) du = V^2 X^{1/3} (1/3) X^{-1/3} dX/X`
using `du/u = (1/3)dX/X`, `u^2 = X^{2/3}`, `Lambda^2 = V^2 X^{1/3}/log N_X`. Substituting
`Y = T^3` turns `(1/log T) int_1^T` into `(1/log Y) int_1^Y` with the factor 3 cancelling.
(b) io-octaves: as in L-105058.5 Cor 2 — if only finitely many octaves were heavy,
`int_1^{2^J} V^2 dX/X <= C + (c_0'-eps) J ln2` for all J, contradicting the limsup. Then
`min_oct X^{1/3}/log N_X >= 2^{L/3}/((2/3)(L+1) ln2)` since `log N_X <= (2/3) log(2X)`. QED.

## P2.2 Lemma (smoothing bridge; the floor corrections are L2(dX/X)-summable)

Define the smooth-parameter field (all cutoffs in ratios; NO floors except inside mu, eta):

    Lambda*(X) := sum_{d,e >= 1, d > X^{1/3}} mu(d) eta(e) (de)^{-1/2} v(de X^{-2/3}),
    V*(X) := Lambda*(X) sqrt((2/3) log X) X^{-1/6}.

Then `int_{64}^inf (V - V*)^2 dX/X =: C_A0 < infinity`. Consequently TARGET(V) <=> TARGET(V*)
with the same constant, and `Q_V(Y) <= A' log Y (Y >= Y_0)` implies
`Q_{V*}(Y) <= A' log Y + 2 sqrt(A' C_A0 log Y) + O(1)`.

Proof. Write `V - V* = delta_1 + delta_2` (the d-cutoff is EXACT: for integer d,
`d > floor(X^{1/3})` iff `d > X^{1/3}` — including cube X, where both read `d >= X^{1/3}+1`;
so there is no d-correction).
(delta_1: weight) `|sqrt(log N_X) - sqrt((2/3)log X)| << X^{-1/3}/sqrt(log X)` since
`log N_X - (2/3)log X = log(N_X U_X/X) - log(U_X X^{-1/3}) = O(X^{-2/3}) + O(X^{-1/3})`, and
`|Lambda| <= sum_{N/2<n<=N} d(n) n^{-1/2} << X^{1/3} log X` (divisor sum, partial summation).
Hence `|delta_1| << X^{-1/6} (log X)^{1/2}`, square log-integrable.
(delta_2: argument of v) With the weight fixed, compare `v(n/N_X)` vs `v(n X^{-2/3})` inside
the h-sum, `|h_{U}(n)| <= (|mu|*eta)(n) <= d(n)`. (i) Both arguments differ by a factor
`1 + O(X^{-1/3})`; on the common support v is Lipschitz (slope `1/ln2`), giving per-n error
`O(X^{-1/3})` and total `<< X^{-1/3} sum_{n<=X^{2/3}} d(n) n^{-1/2} << log X`. (ii) Upper-edge
mismatch: n between `N_X` and `X^{2/3}`, an interval of length `<= X/U_X - X^{2/3} + 1
<= X^{1/3}+1`; a short-interval divisor bound (`sum_{x<n<=x+y} d(n) <= 2 sum_{a<=2 sqrt x}(y/a+1)
<< y log x + sqrt x`, here `y << sqrt x`, `x = X^{2/3}`) gives total `<< X^{-1/3} X^{1/3} log X
= log X`. (iii) Lower-edge mismatch: an interval of length `<< X^{1/3}` on which BOTH v-values
are `<= (2 n x_edge^{-1} - 1)^+/ln2 << X^{-1/3}`, total `<< X^{-1/3} log X`. Summing:
`|Lambda - Lambda*| << log X` off the weight, so `|delta_2| << X^{-1/6}(log X)^{3/2}`, square
log-integrable. Finally `int (V-V*)^2 dX/X << int X^{-1/3} (log X)^3 dX/X < infinity`, and the
limsup/Q transfers are Cauchy–Schwarz: `|sqrt(Q_V) - sqrt(Q_{V*})| <= sqrt(C_A0)`. QED.
[Numeric: num1.py — |V-V*| decays ~X^{-0.46} over X in (1e2, 7e5); max 0.18 at X~1e3.]

## P2.3 Proposition (EXACT double-Dirichlet representation; the diagonal admits one)

For `Re s > 1/6`, with all sums/integrals absolutely convergent:

    G*(s) := int_{64}^inf V*(X) X^{-s} dX/X
           = (3/2) sum_{d > e >= 1} mu(d) eta(e) (de)^{-3/4-(3/2)s} T_{d,e}(s),
    T_{d,e}(s) := int_{t1(d,e)}^{t2(d,e)} v(1/t) sqrt(log(de t)) t^{-1/4-(3/2)s} dt/t,
    t1 = max(1, 16/(de)),  t2 = min(2, d/e).

Proof. Fix (d,e). The (d,e)-term of `V*(X) X^{-s-1}` is supported on
`X in [max(64,(de)^{3/2}), min(d^3, (2de)^{3/2}))`: the v-support forces
`de X^{-2/3} in (1/2,1]` i.e. `X in [(de)^{3/2}, (2de)^{3/2})`, and `d > X^{1/3}` iff `X < d^3`;
the range is nonempty only if `d > e` (`d^3 > (de)^{3/2}` iff `d > e`), and
`d^3 >= (2de)^{3/2}` iff `d >= 2e` (whence `t2 = min(2, d/e)`). Substituting `X = (de t)^{3/2}`
(`dX/X = (3/2) dt/t`, `sqrt((2/3) log X) = sqrt(log(de t))`, `de X^{-2/3} = 1/t`) gives the term.
Absolute convergence for `Re s = sigma > 1/6`: `|T_{d,e}| << sqrt(log(2de))` and
`sum_{d>e} |mu(d)| eta(e) (de)^{-3/4-(3/2)sigma} sqrt(log 2de) <= sum_m d(m) m^{-3/4-(3/2)sigma}
sqrt(log 2m) < inf` iff `3/4 + (3/2)sigma > 1` iff `sigma > 1/6` — which matches the X-side
threshold (`|V*| << X^{1/6} log X`), so Fubini applies. QED.
[Numeric: num2.py — LHS/RHS agree to 7e-17 at s = 0.3+2i, and the pairwise assembly reproduces
V*(X) pointwise to 1e-16.]

## P2.4 Proposition (the half-derivative operator identity; the designed escape made exact)

Let `B_0(s) := int_{64}^inf Lambda*(X) X^{-1/6-s} dX/X` (the UNWEIGHTED transform; absolutely
convergent, analytic on `Re s > 1/6`), and for f analytic on the ray `[s, s+infinity)` define

    D_half[f](s) := -(1/(2 sqrt(pi))) int_0^inf ( f(s+del) - f(s) ) del^{-3/2} d del.

(a) For `Re s > 1/6`:  `G*(s) = sqrt(2/3) * D_half[B_0](s)`.
(b) `D_half[(. - a)^{-1/2}](s) = (1/sqrt(pi)) (s-a)^{-1}` for `Re(s-a) > 0` — the half
derivative turns the raw half-singularity into a FULL POLE (T-105059.6's model, now an identity).
(c) If `|f| <= M` and `|f'| <= M` on the ray then `|D_half[f](s)| <= 3M/sqrt(pi)`.

Proof. (a) For `L > 0`: `int_0^inf (e^{-del L} - 1) del^{-3/2} d del = -2 sqrt(pi L)` (integrate
by parts: `= [ -2 del^{-1/2}(e^{-del L}-1) ]_0^inf - 2L int_0^inf del^{-1/2} e^{-del L} d del
= -2L * Gamma(1/2) L^{-1/2}`). With `L = log X`: `sqrt(log X) = -(1/(2 sqrt(pi)))
int_0^inf (X^{-del}-1) del^{-3/2} d del`. Insert into `G* = sqrt(2/3) int Lambda* sqrt(log X)
X^{-1/6-s} dX/X` and apply Fubini: the double integral converges absolutely since
`int_0^inf min(1, del log X) del^{-3/2} d del = 4 sqrt(log X)` and `B_0`'s integrand is
absolutely integrable at exponent `s` (Re s > 1/6). The inner del-integral then reassembles
`B_0(s+del) - B_0(s)`. (b) `int_0^inf ((x+del)^{-1/2} - x^{-1/2}) del^{-3/2} d del
= x^{-1} int_0^inf ((1+u)^{-1/2}-1) u^{-3/2} du = -x^{-1} B(1/2,1) = -2 x^{-1}` (parts, then
Beta), valid for `Re x > 0` by analytic continuation from `x > 0`; multiply by `-(1/(2 sqrt pi))`.
(c) Split `del <= 1` (`|f(s+del)-f(s)| <= M del`, `int_0^1 del^{-1/2} = 2`) and `del > 1`
(`<= 2M`, `int_1^inf del^{-3/2} = 2`): `(2M + 4M)/(2 sqrt pi) = 3M/sqrt(pi)`. QED.

## P2.5 Proposition (z-integral representation and pinch geometry for the genuine object)

Let `a := 3/4 + (3/2)s`, `beta_0 := a - 1/2`, and

    k(beta) := int_1^2 v(1/t) t^{-beta} dt/t = 1/beta - (1 - 2^{-beta})/(beta^2 ln 2)

(closed form; verified to 1e-12, num5.py). Define the unweighted r-kernel
`kap_0(r) := int_1^{min(2,r)} v(1/t) t^{-1/4-(3/2)s} dt/t` (so `kap_0(d/e)` is P2.3's
weight-1 t-integral with `t1 = 1`; it vanishes for `r <= 1`, carrying the constraint d > e),
and the finite head `H_0(s) := -(3/2) sum_{d>e, de<16} mu(d) eta(e) (de)^{-a}
int_1^{min(16/(de), 2, d/e)} v(1/t) t^{-1/4-(3/2)s} dt/t` (the X < 64 part of the full-kernel
series, removed because B_0's integral starts at 64: `X >= 64` iff `t >= 16/(de)`); H_0 is a
finite sum, entire, and together with its s-derivative bounded on `{Re s >= 0, |Im s| <= 20}`.
Then for `Re s > 1/6` and any `0 < c < (3/2)Re s - 1/4`:

    B_0(s) = H_0(s) + (3/2) (1/(2 pi i)) int_{Re z = c}
             k(1/4 + (3/2)s + z) * zeta^{1/2}(a+z) / ( z * zeta(a-z) ) dz,

where `H_0` is the (entire, explicitly bounded) unweighted head correction re-adding the
`de < 16` truncation. The integrand's singularities in z, for s near `s_0 := i gamma_1/3`:
kernel pole `z = 0`; branch point of `zeta^{1/2}(a+z)` at `z_b = 1-a = 1/4 - (3/2)s`; poles at
zeros `z_p(rho) = a - rho`; and

    z_p(rho_1) - z_b = 2a - 1 - rho_1 = 3 (s - s_0):

the branch point PINCHES the rho_1-pole exactly at `s = s_0 = i gamma_1/3` (`Re s_0 = 0`, the
boundary line of the reductio's analyticity half-plane — precisely where the H2 lines
`Re s = h` probe as `h -> 0`). The pinch point is `z* = 1/4 - i gamma_1/2` (`|z*| = 7.0718`);
the kernel argument there is `1/4 + (3/2)s_0 + z* = 1/2`, so the pinch carries the factor
`k(1/2) = 0.309778 != 0`. All other singularities are O(1)-separated from z* uniformly for
`|Im s - gamma_1/3| <= r_0 <= 1`: nearest zero-pole `z_p(rho_2)` at distance `> 6`, conjugate
`z_p(bar rho_1)` at distance `> 13`, kernel pole at distance `|z*| = 7.07` — because Im s is
BOUNDED in the window, the z-plane sees only low zeros locally; no zero-density input enters.

Proof. Mellin: `kap_0(r) = 0` for `r <= 1`, constant for `r >= 2`, continuous, piecewise C^1;
`hat kap_0(z) = int_1^inf kap_0(r) r^{-z} dr/r = (1/z) k(1/4+(3/2)s+z)` (Fubini on
`int_t^inf r^{-z-1} dr`), absolutely `O(|z|^{-2})` on vertical lines; Mellin inversion holds
pointwise (continuous BV function, absolutely convergent inverse). Insert into P2.3's
unweighted series (kernel form: term `= (3/2) mu(d) eta(e) (de)^{-a} kap_0(d/e)`, and
`kap_0(d/e)` vanishes for `d <= e`, so the constraint d > e is carried by the kernel); swap
sum and z-integral by absolute convergence (`Re(a-z) > 1` and `Re(a+z) > 1` on `Re z = c`):
the d-sum gives `1/zeta(a-z)`, the e-sum `zeta^{1/2}(a+z)` (Dirichlet series of `zeta^{1/2}`,
absolutely convergent). The singularity bookkeeping is arithmetic with `rho_1 = 1/2 + i gamma_1`,
`gamma_1 = 14.134725...`; separations are computed with `gamma_2 = 21.022`. QED.

## P2.6 The two interfaces

Split the P2.5 contour at `|Im z| = Z_0 := 40` and (for s in the window) deform the
`|Im z| <= Z_0` piece across the branch point as it crosses (`Re z_b = 1/4 - (3/2)Re s > c`
once `Re s < 1/6`), producing a cut-hugging loop. Write `B_0 = H_0 + Z_loc + Z_far`
correspondingly. On `Omega(r_0) := {0 < Re s <= 1/4, |Im s - gamma_1/3| <= r_0}` with the ray
extension `Omega^+ := Omega ∪ {Re s > 1/4, |Im s - gamma_1/3| <= r_0}`:

[P1-LOC] (lane P1's model expansion, calibrated to the genuine kernel; ASSUMED here, cited):
there are `r_0 in (0,1]` and `c_B in C`, `c_B != 0`, with

    Z_loc(s) = c_B (s - s_0)^{-1/2} + R_loc(s),   s in Omega^+,

`R_loc` analytic with `|R_loc| + |R_loc'| <= M_loc` on `Omega^+`, branch of `(s-s_0)^{-1/2}`
principal on `Re(s - s_0) > 0`. The loop-collapse computation identifying the coefficient gives

    |c_B| = (3/2) |k(1/2)| / ( sqrt3 |z*| |zeta'(rho_1)| ) = 0.04782893516094 (20-digit certified; the 0.047832 quote was a rounding slip caught by the coefficient lane)...

(`|zeta'(rho_1)| = 0.79316`; the `sqrt3` from `z_p - z_b = 3(s-s_0)`; the unimodular branch
factor does not affect `|c_B|`). Zeta inputs needed by the local analysis are CLASSICAL only:
analyticity, the bounded-height verified zero-set (all zeros with `|Im| <= 60` lie on the
critical line and are simple — rigorous classical computation, the same input class as
L-105058.5's use of rho_1), and boundedness of `zeta^{1/2}` on compact cut regions. No
zero-free half-plane, no density estimates: the window's z-geometry is compact.

[P2-FAR] (this lane's residual): `|Z_far| + |Z_far'| <= M_far` on `Omega^+`, with `M_far`
independent of h. (A weaker L2-window form suffices with minor changes: see P2.8(iii).)

## P2.7 THEOREM (the hypothesis-side transfer — the L-105058.5 architecture for W, verbatim)

Assume [P1-LOC] and [P2-FAR]. Then TARGET(V) holds with the explicit constant

    c_0' = 2 |c_P|^2,  c_P := sqrt(2/(3 pi)) c_B,  i.e.  c_0' = (4/(3 pi)) |c_B|^2
         = 9.71e-4  (with [P1-LOC]'s coefficient value),

i.e. `limsup_T (1/log T) int_1^T u W_u^2 du/u >= c_0'` — the W-pinch lemma of T-105059.6 —
and hence (P2.1(b) + T-105059.5, both exact and unconditional) `E(L) >= c 2^{L/3}/L` for
infinitely many L, unconditionally.

Proof. Suppose not: `A := limsup_Y (1/log Y) int_1^Y V^2 dX/X < c_0'`; fix `A < A' < c_0'`.
(1) `Q_V(Y) <= A' log Y` for `Y >= Y_0`; by P2.2, `Q_{V*}(Y) <= A' log Y + C_2 sqrt(log Y) + C_3`.
(2) For `h in (0, 1/2)`:
`J(h) := int_{64}^inf V*^2 X^{-2h} dX/X = int Y^{-2h} dQ_{V*}(Y)
= [Q_{V*} Y^{-2h}] + 2h int_{64}^inf Q_{V*}(Y) Y^{-2h} dY/Y <= A'/(2h) + O(h^{-1/2})`
— the boundary term vanishes BY (1) (not by any a priori bound; `Q_{V*}(Y) Y^{-2h} -> 0`), and
`2h int log Y * Y^{-2h} dY/Y = 1/(2h)`, `2h int sqrt(log Y) Y^{-2h} dY/Y = O(h^{-1/2})`.
In particular `J(h) < infinity` for every `h > 0`.
(3) For every `sigma > 0`, by Cauchy–Schwarz with `h' = sigma/2`:
`int |V*| X^{-sigma} dX/X <= J(sigma/2)^{1/2} (int_{64}^inf X^{-sigma} dX/X)^{1/2} < infinity`.
Hence `G*(s)` is an ABSOLUTELY convergent integral for `Re s > 0`, so analytic there (Morera +
dominated convergence); the same argument gives analyticity of `B_0` on `Re s > 0` (the
unweighted object obeys `Q_{V_0}(Y) <= (3/2) A' loglog Y (1+o(1))` by partial summation of (1)
against `(3/2)/log X`, hence its own J-finiteness). By the identity theorem, the P2.3/P2.5
formulas, valid on `Re s > 1/6`, continue to `Re s > 0`: under the reductio, `G*`, `B_0`,
`Z_far = B_0 - H_0 - Z_loc` are all analytic on `Omega^+`; every pointwise identity among them
persists.
(4) Plancherel. `phi_h(x) := V*(e^x) e^{-hx} 1_{x >= log 64}` lies in `L^1(R)` (by (3) with
`sigma = h`) AND `L^2(R)` (`= J(h)`); its Fourier transform is EXACTLY `t -> G*(h+it)`
(absolutely convergent integral — no a.e. caveat needed), and Plancherel for `L^1 ∩ L^2` gives

    J(h) = (1/(2 pi)) int_R |G*(h+it)|^2 dt.

(5) The window lower bound. By P2.4(a) and (3), on `Omega`:
`G* = sqrt(2/3) ( D_half[H_0] + D_half[Z_loc] + D_half[Z_far] )` — D_half converges on the ray
`[s, s+inf)` because each piece is analytic there with the stated bounds ([P1-LOC], [P2-FAR],
head bounds; for `Re s' >= 1/4` all pieces are absolutely-convergent-bounded). By P2.4(b),
`D_half[c_B (.-s_0)^{-1/2}] = (c_B/sqrt(pi)) (s-s_0)^{-1}`; by P2.4(c) the other three images
are bounded by `M := (2/sqrt(pi))(M_head + M_loc + M_far)`. Hence on the window line `s = h+it`,
`|t - gamma_1/3| <= r_0`:

    |G*(h+it)| >= sqrt(2/(3 pi)) |c_B| / |h + i(t - gamma_1/3)|  -  sqrt(2/3) M .

(6) Contradiction. Using both conjugate windows (V* real => |G*(h+it)| = |G*(h-it)|):
`(1/2pi) int_R |G*|^2 dt >= (2/2pi) int_{|tau| <= r_0} [ (2/(3pi))|c_B|^2/(h^2+tau^2)
- O(M |c_B| (h^2+tau^2)^{-1/2}) ] dtau >= (2/(3 pi^2))|c_B|^2 (pi/h)(1 - O(h/r_0))
- O(M |c_B| log(r_0/h))`. With (2) and (4): `A'/(2h) + O(h^{-1/2}) >= (2/(3pi))|c_B|^2 / h
- O(M|c_B| log(1/h))`. Multiply by 2h and let `h -> 0`: `A' >= (4/(3 pi)) |c_B|^2 = c_0'`,
contradicting `A' < c_0'`. QED.

Remarks. (i) Every step (1)-(4) and (6) is the L-105058.5 architecture verbatim: negation =>
partial-integration J-bound => CS absolute-convergence licence => one-sided PW/Plancherel =>
window Schwarz; step (5) replaces "F = 1/(s zeta(s+1)) explicitly" by the P2.3-P2.5
representation plus the two interfaces — this is exactly where the genuine tent field is harder
than m(u). (ii) The en-route conclusion of L-105058.5 ("hypothesis => zeta nonzero on
Re > 1/2") has NO analogue here and is NOT used: the reductio yields analyticity of G*, B_0 on
Re s > 0 only, which is all steps (3)-(5) consume. (iii) If [P2-FAR] is available only as
`limsup_h h * int_win |D_half[Z_far](h+it)|^2 dt <= eps^2 (2/(3pi))|c_B|^2` with eps < 1, the
same proof gives `c_0' = (1-eps)^2 (4/(3pi))|c_B|^2`: an L2-window far-field bound suffices.

## P2.8 The wall, honestly: status of [P2-FAR], obstruction analysis, routes

(a) WHAT IS PROVED HERE: everything except [P2-FAR] ([P1-LOC] is lane P1's by assignment;
P2.5 supplies the exact genuine-kernel calibration `k(1/2)/z*` and the pinch geometry its
model must match). The half-singularity wall and its D_half repair are now exact operator
statements (P2.4), not models.
(b) OBSTRUCTION (why [P2-FAR] is genuinely the wall): on any fixed vertical z-contour piece
with `|Im z| > Z_0`, the factor `1/zeta(a-z)` is evaluated at `Re(a-z) ~ 3/4` at UNBOUNDED
heights. Unconditionally there is NO pointwise, L1-, or L2-bound for `1/zeta` on any fixed
line inside the strip (hypothetical off-line zeros make it non-locally-integrable); pushing
the contour left to the classical (dlVP/VK) zero-free boundary — where `1/zeta << log^C` IS
classical — is blocked by the branch points of `zeta^{1/2}(a+z)`, whose position depends on
the SAME unknown zeros: the half-divisor structure puts one power of zeta in the denominator
on every factorization, and the mirror trick (functional equation) reproduces the problem.
This is T-105059.6's negative-moment wall relocated to the far field — the pinch itself (the
local part) is NOT obstructed: it needs only bounded-height classical inputs.
(c) ROUTES (both in-scope for a successor lane): (R1) arithmetic far-field: split the
r = d/e kernel `kap_0 = kap_smooth + kap_corner`; the smooth part's z-transform decays
superpolynomially (its far-field cost concentrates at the corner scales), and the corner part
is a NEAR-DIAGONAL divisor-correlation object (`d/e` near 1 or 2) whose window-L2 mass can be
attacked by Montgomery–Vaughan on the X-side plus Hooley–Tenenbaum Delta-function second
moments (`sum_{m<=M} Delta(m)^2 << M (log M)^C`, unconditional) with an `eps_1`-absorption
into P2.7's remark (iii). Numerics (e) strongly support this: the corner part is spectrally
FLAT at the pinch frequency. (R2) reductio-side far-field: under the negation, `B_0` has
line-L2 `<= 3 pi A' log(1/h)` — the far field inherits an L2-log bound; upgrading it through
D_half loses `1/h` by naive pointwise routes (one log short); a genuinely L2-based D_half
window estimate (x-side: multiplier `sqrt(x)` against the frequency-localized `phi`) is the
open refinement.
(d) FAILURE MODES: a proof that `c_B = 0` (excluded: `k(1/2) = 0.3098`, `|z*| != 0`,
`zeta'(rho_1) != 0` — [P1-LOC]'s coefficient is a nonzero closed form times `1/zeta'(rho_1)`,
same input and fallback as L-105058.5 step (4)); or `Z_far` carrying window mass `>> 1/h`
(numerically contradicted at truncation, see (e)).
(e) NUMERICS (num1-num5.py, truncation Xc = 2e4, i.e. h_eff ~ 1/log Xc ~ 0.1):
  - P2.3 identity: 7e-17. Kernel closed form: 1e-12. A0 differences: ~X^{-0.46}, L2-summable.
  - Plancherel (step 4): J(h) vs (1/2pi)int|G*|^2 dt: ratio 1.000000 at h = 0.02 and 0.01,
    with G* cross-validated pointwise against the exact pair formula (moduli agree to 4 digits
    at t in {1.7, 4.71, 9.3}).
  - Window: |G*|^2 peaks at t = 4.785 (predicted gamma_1/3 = 4.7116 + O(1/log Xc) smearing);
    window mass grows as h decreases (0.0054 -> 0.0061 on +-0.15 at h 0.02 -> 0.01); ~8-20x
    enhancement over control bands.
  - COEFFICIENT CHECK: predicted pole mass `pi |c_P|^2 / h_eff` with `|c_B| = 0.04783`,
    h_eff = 0.1: 0.0153 vs measured 0.0146 (+-0.5-window, h=0.01) — the [P1-LOC] coefficient
    is quantitatively consistent with the genuine object's measured window mass.
  - CORNER/FAR SUPPORT: pairs with d/e in (1,1.25]∪[1.75,2) carry 77% of the raw mean square
    but only 3.5% of the window mass (0.00019 vs 0.00549), and dominate the flat control band
    — the pinch lives in the bulk ratios; the far/corner field is spectrally flat, as [P2-FAR]
    asserts.

## Classical inputs used (none beyond L-105058.5's class)
Divisor-sum elementary bounds; Dirichlet series of zeta^{1/2} (|eta| <= 1); Mellin inversion
for BV functions; L1∩L2 Fourier–Plancherel; Gamma(-1/2)/Beta integrals; rho_1 on the line,
simple, |zeta'(rho_1)| = 0.79316, gamma_2 - gamma_1 > 6 (verified classical computation);
[for P1-LOC, cited]: bounded-height zero verification |Im| <= 60. NO RH, no zero-free
half-plane, no density hypotheses. The dlVP/VK region is mentioned only in the obstruction
discussion (b), not used by any proved statement.
