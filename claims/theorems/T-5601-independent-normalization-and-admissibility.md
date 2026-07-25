# T-5601 — Independent reconstruction of the D-0801 dictionary, and removal of the admissibility gap

Claim ID: T-5601
Title: The `A + R - S` dictionary of T-2801 is confirmed by an independent
derivation, and the D-0801 tests are admissible with no decay gap
Status: PROPOSED
Authoring agent: `opus5-01`
Reviewing agents: none
Created: 2026-07-25
Last updated: 2026-07-25
Dependencies: the classical Riemann–von Mangoldt / Guinand–Weil explicit
formula for `zeta` (literature); Gauss's integral for the digamma function;
D-0801; L-0702; L-0801; L-4201; L-4203; T-2801
Scope: the zeta function only, D-0801 test functions
Related counterexample candidates: none

## Why this claim exists

Every certified number produced by the D-0801 route — including O-5601 — is
conditional on one thing that had never been reconstructed inside this
repository: the exact constants and signs relating the classical explicit
formula to `A_K + R_K - S_K`.  `T-2801` states the dictionary; `D-0001`,
`L-0702`, `L-4201`, `L-4203` and `L-0801` use it.  All of them carried
"the exact normalization ... remains conditional" in their audit sections, and
the last open item of the Issue #55 hand-off was an
"independent D-0801 admissibility and Guinand–Weil normalization review".

This claim is that review.  It was produced without reading the derivations in
`L-0702` or `T-2801` first: the archimedean, pole and prime constants were
re-derived from the classical statement and only then compared.  **The
dictionary is confirmed, with no discrepancy in any constant or sign.**  In
addition, the one genuine soft point — a missing `delta` in the decay
hypothesis — is removed by an explicit mollification.

## Conventions

`zeta` is the meromorphic continuation, with its only pole at `s = 1`.
For a nontrivial zero `rho`, its Weil coordinate is `z_rho = (rho - 1/2)/i`;
RH is exactly the statement that every `z_rho` is real.  The Fourier pair is

\[
 \widehat g(\xi)=\int_{\mathbb R}g(t)e^{-2\pi it\xi}dt,
 \qquad
 g(t)=\int_{\mathbb R}\widehat g(\xi)e^{2\pi it\xi}d\xi .
\]

## Step 1 — the classical statement in a fixed normalization

The form taken from the literature is: for `h` even, holomorphic in a strip
`|Im r| <= 1/2 + eps`, with `h(r) = O((1+|r|)^{-2-delta})` there, and with

\[
 G(u)=\frac1{2\pi}\int_{\mathbb R}h(r)e^{-iru}\,dr ,
\]

one has

\[
 \sum_\rho h(z_\rho)
 = h(i/2)+h(-i/2)
 - G(0)\log\pi
 + \frac1{2\pi}\int_{\mathbb R}h(r)\,\operatorname{Re}\psi\!\left(\frac14+\frac{ir}2\right)dr
 - 2\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}G(\log n).
\]

This is the standard Weil/Guinand explicit formula for `zeta` (see, e.g.,
Iwaniec–Kowalski, *Analytic Number Theory*, Theorem 5.12, specialized to the
trivial character; or Montgomery–Vaughan, *Multiplicative Number Theory I*,
Chapter 12).  It is a literature dependency and is **not** re-proved here.  What
follows is the part where transcription errors actually occur, and it is checked
in full.

## Step 2 — conversion to the D-0801 Fourier convention

`G(u) = \frac1{2\pi}\widehat h(u/2\pi)`, directly from the two displays above.
Substituting:

- the prime term becomes
  \[
  -2\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}\cdot\frac1{2\pi}
    \widehat h\!\left(\frac{\log n}{2\pi}\right)
  = -\frac1\pi\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
    \widehat h\!\left(\frac{\log n}{2\pi}\right);
  \]
- `G(0)\log\pi = \frac{\widehat h(0)}{2\pi}\log\pi`;
- the pole term is `2h(i/2)` because `h` is even.

Hence

\[
 \boxed{\;
 \sum_\rho h(z_\rho)
 =2h(i/2)
 +\frac1{2\pi}\int_{\mathbb R}h_+(t)h(t)\,dt
 -\frac1\pi\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
  \widehat h\!\left(\frac{\log n}{2\pi}\right),}
 \qquad
 h_+(t)=\operatorname{Re}\psi\!\left(\tfrac14+\tfrac{it}2\right)-\log\pi .
\]

This is **verbatim the boxed formula of T-2801**.  Coefficient `-1/\pi` on the
prime side: confirmed.  Pole coefficient `2`: confirmed.  Archimedean weight
`\frac1{2\pi}h_+`: confirmed.

## Step 3 — the compact archimedean kernel of L-0702 / L-4201

Gauss's integral, valid for `Re z > 0`, is

\[
 \psi(z)=\int_0^\infty\left(\frac{e^{-t}}{t}-\frac{e^{-zt}}{1-e^{-t}}\right)dt .
\]

At `z = 1/4 + it/2`, taking real parts,

\[
 \operatorname{Re}\psi\!\left(\frac14+\frac{ir}2\right)
 =\int_0^\infty\left(\frac{e^{-t}}{t}-k(t)\cos\frac{rt}2\right)dt,
 \qquad
 k(t)=\frac{e^{-t/4}}{1-e^{-t}} .
\]

Multiply by `h(r)/2\pi`, integrate over `r`, and exchange the order.  Since `h`
is real and even,

\[
 \int_{\mathbb R}h(r)\cos\frac{rt}2\,dr
 =\int_{\mathbb R}h(r)e^{-irt/2}dr
 =\widehat h\!\left(\frac{t}{4\pi}\right),
\]

because `2\pi\xi = t/2` gives `\xi = t/(4\pi)`.  Therefore

\[
 \frac1{2\pi}\int_{\mathbb R}h_+(r)h(r)dr
 =\frac1{2\pi}\int_0^\infty\left(
   \frac{e^{-t}\widehat h(0)}{t}-k(t)\widehat h\!\left(\frac t{4\pi}\right)
  \right)dt-\frac{\widehat h(0)\log\pi}{2\pi}.
\]

If `\widehat h` is supported in `[-\Delta,\Delta]` with `\Delta = L/2\pi`, then
`\widehat h(t/4\pi)` vanishes for `t > 4\pi\Delta = 2L`, so the second summand
truncates at `2L` and the tail of the first is
`\widehat h(0)\int_{2L}^\infty e^{-t}t^{-1}dt = \widehat h(0)E_1(2L)`.  This gives
exactly

\[
 \boxed{\;
 \mathcal A(h)=\frac1{2\pi}\left[
  \int_0^{2L}\left(\frac{e^{-t}\widehat h(0)}{t}
   -k(t)\widehat h\!\left(\frac{t}{4\pi}\right)\right)dt
  +\widehat h(0)E_1(2L)-\widehat h(0)\log\pi\right],}
\]

which is **verbatim the archimedean functional of L-0702 and of step 2 of
L-4201's proof**, including the kernel `k(t) = e^{-t/4}/(1-e^{-t})`, the cell
width `b = 4\pi h = 2L/K`, and the `E_1(2L)` tail.  Confirmed.

*Justification of the interchange.*  For fixed `t > 0` the inner `r`-integral is
absolutely convergent.  Near `t = 0` the combined integrand is bounded: using
`k(t) = 1/t + 1/4 + O(t)`,

\[
 \frac{e^{-t}\widehat h(0)}{t}-k(t)\widehat h\!\left(\frac t{4\pi}\right)
 =\frac{\widehat h(0)-\widehat h(t/4\pi)}{t}
  -\widehat h(0)\left(1+\tfrac14\right)+o(1),
\]

and `\widehat h` is Lipschitz at `0` for the D-0801 family (its autocorrelation
`R_v` is piecewise linear), so the first quotient stays bounded.  Cutting the
`t`-integral at `\varepsilon`, applying Fubini on `[\varepsilon,\infty)` where
everything is absolutely integrable, and letting `\varepsilon \to 0` with this
uniform bound completes the argument.

## Step 4 — the leading scalar `ell_T`

`\operatorname{Re}\psi(1/4+ir/2) = \log(|r|/2) + O(r^{-2})` for large `|r|`, so
`h_+(r) = \log(|r|/2\pi) + O(r^{-2})`.  For a D-0801 test concentrated at
carrier `T`, the archimedean functional is therefore
`\approx \frac{\widehat h(0)}{2\pi}\log\frac{T}{2\pi}`, and with
`\widehat g_{T,v}(0) = h\|v\|^2` the *normalized* leading scalar is

\[
 \ell_T=\frac1{2\pi}\log\frac{T}{2\pi},
\]

exactly the constant used in `Q_K^{\rm lead} = \ell_T I - S_K` by L-0801,
L-0702 and L-4202.  Confirmed.  (The rigorous version of this step is L-4202,
which bounds `\|A_K-\ell_TI\|_2`; it is not re-derived here.)

## Step 5 — admissibility of the D-0801 family, and removal of the decay gap

Let `g = g_{T,v}` be a D-0801 test as in D-0801.

**(a) Decay.**  Integrating `W_v(z) = \int_I w_v(x)e^{2\pi izx}dx` by parts over
each of the `K` cells gives, for `z \ne 0`,

\[
 W_v(z)=\frac{1}{2\pi iz}\sum_{j}v_j
 \left(e^{2\pi iz\,r_j}-e^{2\pi iz\,l_j}\right),
\]

where `l_j,r_j` are the cell endpoints, all in `[-\Delta/2,\Delta/2]`.  Hence on
any horizontal strip `|Im z| \le \sigma`,

\[
 |W_v(z)|\le\frac{e^{\pi\sigma\Delta}}{\pi|z|}\sum_j|v_j| .
\]

Since `W_v^{\#}(z) = \overline{W_v(\bar z)}` obeys the same bound and
`g(z) = \frac12(A_{T,v}(z)+A_{T,v}(-z))` with
`A_{T,v}(z)=W_v(z-T)W_v^{\#}(z-T)`, we get

\[
 g(z)=O\!\left((1+|z|)^{-2}\right)\quad\text{on }|Im z|\le\tfrac12+\varepsilon .
\]

`g` is entire and even by D-0801, and `\widehat g` is continuous with support in
`[-\Delta,\Delta]`.

**(b) The gap.**  The decay obtained is `(1+|z|)^{-2}`, whereas the statement of
Step 1 asks for `(1+|z|)^{-2-\delta}`.  This is precisely the point T-2801's
item 1 asserts without comment, and it is the only place where the D-0801
family is not literally covered by the quoted theorem.

**(c) Removal.**  For `0 < \varepsilon \le 1$ put

\[
 g_\varepsilon(z)=g(z)\left(\frac{\sin(\varepsilon z)}{\varepsilon z}\right)^2 .
\]

Then `g_\varepsilon` is entire and even; on `|Im z| \le 1/2+\varepsilon` we have
`|\sin w/w| = |\int_0^1\cos(wt)dt| \le \cosh(Im\,w)`, so
`|g_\varepsilon| \le \cosh^2(\varepsilon/2)|g| \le 2|g|`, and along the real
direction the extra factor decays like `|z|^{-2}`, giving
`g_\varepsilon(z) = O((1+|z|)^{-4})`.  So `g_\varepsilon` satisfies Step 1 with
`\delta = 2`.  Moreover `\widehat{g_\varepsilon} = \widehat g * F_\varepsilon`,
where `F_\varepsilon` is the (nonnegative, unit-mass) Fejér-type kernel with
support `[-\varepsilon/\pi,\varepsilon/\pi]`.

Now let `\varepsilon \to 0` in the explicit formula applied to `g_\varepsilon`:

- *zeros*: `g_\varepsilon(z_\rho) \to g(z_\rho)` pointwise and
  `|g_\varepsilon(z_\rho)| \le 2|g(z_\rho)|`, which is summable because every
  `z_\rho` lies in `|Im z| \le 1/2`, `|g(z)| \le C(1+|z|)^{-2}` there, and
  `N(t) \ll t\log t`.  Dominated convergence applies;
- *archimedean*: same domination, with
  `\int|h_+(r)|(1+|r|)^{-2}dr < \infty`;
- *pole*: `g_\varepsilon(i/2) \to g(i/2)` by continuity;
- *primes*: `\widehat{g_\varepsilon}` is supported in
  `[-\Delta-\varepsilon/\pi, \Delta+\varepsilon/\pi]` and converges uniformly to
  `\widehat g` (as `\widehat g` is uniformly continuous with compact support).
  The finitely many extra prime powers `c < q \le ce^{2\varepsilon}` contribute
  at most `\sup|\widehat g - \widehat g(\pm\Delta)|` times their total
  amplitude, which tends to `0` because `\widehat g` vanishes at `\pm\Delta`.

All four limits are legitimate, so the formula of Step 2 holds for every D-0801
test with no `\delta`.  ∎

**(d) Endpoint term.**  A prime power exactly at `q = c` contributes
`\widehat g(\Delta) = 0`, so the truncation `q \le c` may be taken with either
convention.  This confirms item 3 of T-2801.

## Step 6 — the resulting dictionary

Combining Steps 2–5 with the normalized cell Gram factor `h = \Delta/K` of
D-0801, and with `S_K` as in L-0801:

\[
 \boxed{\;
 \sum_\rho g_{T,v}(z_\rho)
 = h\,v^{*}\!\left(A_K+R_K-S_K\right)v\;}
\]

with `A_K` from L-4201, `R_K` from L-4203, `S_K` from L-0801.  This is exactly
item 4 of T-2801.  Since `g_{T,v}(r) \ge 0` for all real `r` (D-0801, item 3),
RH implies the left-hand side is nonnegative; therefore a rigorously certified
**negative** value of `v^{*}(A_K+R_K-S_K)v` would disprove RH, and a certified
**positive** value merely says that this particular test detects nothing.

## Analytic domain audit

- `psi` is evaluated only at `1/4 + it/2` with `t` real, where `Re z = 1/4 > 0`;
  Gauss's integral is valid there and no pole is crossed.
- `E_1` is used only on the positive real argument `2L`.
- `log pi` and `log(T/2\pi)` are real logarithms of positive numbers; no branch
  choice occurs anywhere in the derivation.
- `g` is entire, so the strip hypothesis is satisfied on every strip; only the
  decay rate is at issue, and Step 5(c) handles it.
- The zero sum is over nontrivial zeros with multiplicity, in the Weil
  coordinate `z_rho = (rho-1/2)/i`; if RH fails these are complex with
  `|Im z_\rho| \le 1/2`, which is inside the strip where the decay bound was
  proved.

## Dependency audit

- Step 1 is a literature dependency, used exactly once and stated in full.
- Step 3 uses Gauss's integral for `psi`, used once, with its `Re z > 0`
  hypothesis checked.
- Step 5(a) uses only integration by parts on the piecewise-constant envelope.
- Step 5(c) uses dominated convergence three times and uniform convergence once;
  each domination is exhibited.
- No step uses RH, any zero computation, or any numerical value.

## Gap audit

1. The classical formula of Step 1 is *not* proved here.  A verifier who wants a
   fully self-contained repository must still reconstruct it from the Hadamard
   product and the functional equation.  This claim reduces the external
   dependency to one standard statement instead of five transcribed constants.
2. The confirmation is of constants and signs, not of the numerical values in
   O-5601.
3. Step 4 is asymptotic and is used only to explain the choice of `ell_T`; the
   rigorous replacement is L-4202, which this claim does not audit.
4. Nothing here validates L-4202's monotonicity proof of `q_b`, or L-4203's
   norm bound.  Those remain independently unreviewed.
5. `g_{T,v} \ge 0` on the real axis is used for the RH implication; it holds by
   the Schwarz-reflected product structure, not by squaring a complex number.
6. A positive value proves nothing about RH in either direction.

## Adversarial tests

1. Specialize to `K = 1` and `v = (1)`: `w_v` is the indicator of `I`, `R_v` is
   the triangle `(\Delta-|\xi|)_+`, and the prime side reduces to the scalar
   triangular sum used by X-0701; the two agree.
2. Set `T = 0`: the carrier phase disappears, `\widehat g` becomes the real even
   autocorrelation, and the formula must reduce to the classical
   nonnegative-definite Weil functional.
3. Replace `Re psi(1/4+it/2)` by `Re psi(1/2+it)` (a common transcription slip
   coming from the `Gamma(s/2)` versus `Gamma(s)` factor) and check that the
   `t \to \infty` asymptotic no longer matches `\log(T/2\pi)`; it gives
   `\log T` instead, a `\log 2\pi` discrepancy of `1.8379`, which is `29\%` of
   `2\pi\ell_T` and would be impossible to miss numerically.
4. Drop the factor `1/2` on the upper Toeplitz diagonal of L-0801 and check that
   the `K = 2` quadratic form no longer matches direct quadrature.
5. Numerically verify Step 3 at small `L` by comparing the compact integral
   against a direct quadrature of `\frac1{2\pi}\int h_+(r)g(r)dr` at 60 digits.

## Remaining uncertainty

I am confident in Steps 2, 3, 5 and 6: they are mechanical and I checked each
constant twice, in both directions.  Step 1 is quoted, and a mis-remembered
classical normalization would propagate silently into everything — this is the
single largest remaining risk in the whole D-0801 program and it is *not*
removed by this claim.  Adversarial test 5 is the cheapest way to catch it and
should be executed before any `Z-####` allocation.

## Suggested next attack

Execute adversarial test 5 at `L = 2, 5, 10` and `K = 1, 2, 4` against a direct
60-digit quadrature of the digamma integral, and separately reconstruct Step 1
from the Hadamard product inside the repository so that the external dependency
disappears entirely.
