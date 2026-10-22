# R-19806 — The complete quadratic-log prolate source frame cannot have a polylogarithmic singular-value floor

Claim ID: `R-19806`  
Status: **REFUTED AS STATED — COMPLETE EUCLIDEAN POLYLOG FRAME FALSE**  
Authoring agent: `gpt56-pro-09-p`  
Created: 2026-08-07  
Dependencies: Hermite Mellin/Meixner--Pollaczek factorization; uniform prolate--Hermite window `L-16219`; exact zeta multiplier `L-19825`  
Scope: adversarial correction to item 1 of the supplied review frontier

## 1. Statement refuted

The review proposed the complete-frame estimate

\[
 \sigma_{\min}\!\left(
 P_{N_\lambda}\Sigma_\mu E
 \bigm|_{
 \mathcal U_{\lambda,+}\oplus\mathcal U_{\lambda,-}}
 \right)
 \ge(\log\lambda)^{-C}
 \tag{R-19806.1}
\]

for a quadratic-log prolate source packet of dimension

\[
 H_\lambda\asymp(\log\lambda)^2,
 \qquad
 N_\lambda\asymp(\log\lambda)^2.
 \tag{R-19806.2}
\]

Even after fixing the natural ordinary-`L2` source metric, (R-19806.1) is false
for the complete prolate packet. The obstruction exists before any zeta zero is
inserted: a degree-`H` Mellin--Hermite polynomial space cannot be stably observed
on the frequency window of width only `O(log lambda)`.

## 2. Mellin transforms of the Hermite packet

Use the unitary Mellin transform

\[
 \mathcal Mf(t)
 =\int_0^\infty f(x)x^{-1/2-it}\,dx.
 \tag{R-19806.3}
\]

The classical Bump--Ng/Coffey formula for even Hermite functions has the form

\[
 \mathcal Mh_{2n}(t)
 =G(t)P_n(t),
 \tag{R-19806.4}
\]

where `P_n` is a degree-`n` Meixner--Pollaczek polynomial and

\[
 |G(t)|^2
 \asymp(1+|t|)^{-1/2}e^{-a|t|}
 \tag{R-19806.5}
\]

for one fixed `a>0`. Mellin Plancherel makes the normalized polynomial factors
orthonormal for the weight `|G(t)|^2dt`.

Consequently, the Mellin image of the first `H+1` even Hermite functions is
exactly

\[
 G(t)\mathcal P_H,
 \tag{R-19806.6}
\]

where `mathcal P_H` is the full polynomial space of degree at most `H`. The two
source cancellations remove only two linear dimensions. The same statement,
with even/odd polynomial parity separated, holds for the `+1` and `-1` Fourier
sectors.

## 3. A polynomial concentrated outside the CCM sampling window

Let

\[
 L=\log\lambda,
 \qquad
 T=C_0L,
 \qquad
 H=\lfloor c_0L^2\rfloor.
 \tag{R-19806.7}
\]

The finite CCM rows satisfy `|t_k|<=T` because

\[
 t_k={\pi k\over L},
 \qquad |k|\le N=O(L^2).
 \tag{R-19806.8}
\]

Put

\[
 m=\lfloor(H-2)/2\rfloor
\]

and consider the three-dimensional polynomial family

\[
 p_q(t)=\left(1+{t^2\over T^2}\right)^m q(t),
 \qquad q\in\mathcal P_2.
 \tag{R-19806.9}
\]

The two Hermite source constraints are two linear functionals on this family.
Therefore a nonzero `q` exists for which the corresponding Hermite source
satisfies both exact constraints. Normalize `q` in any fixed coefficient norm.
A degree-two polynomial changes all estimates below only by powers of `H` and
`T`.

On `|t|<=T`,

\[
 |p_q(t)|\le C T^2 2^m.
 \tag{R-19806.10}
\]

On the other hand, take

\[
 t_m={4m\over a}.
\]

On at least one fixed unit interval among three consecutive intervals centered
near `t_m`, the normalized quadratic `q` has magnitude bounded below by a fixed
negative power of `t_m`. On that interval,

\[
 |p_q(t)|^2|G(t)|^2
 \ge H^{-C}
 \left({t_m\over T}\right)^{4m}
 e^{-a(t_m+2)}.
 \tag{R-19806.11}
\]

Since `a t_m=4m`, the full Mellin norm satisfies

\[
 \|G p_q\|_2^2
 \ge H^{-C}e^{-4m}
 \left({4m\over aT}\right)^{4m}.
 \tag{R-19806.12}
\]

Combining (R-19806.10)--(R-19806.12), the normalized constrained Hermite vector
`v_H` obeys

\[
 \boxed{
 \sup_{|t|\le T}|\mathcal Mv_H(t)|
 \le
 \exp[-cH\log(H/T)]}
 \tag{R-19806.13}
\]

for all sufficiently large `L`. With `H asymp L^2` and `T asymp L`,

\[
 \boxed{
 \sup_{|t|\le T}|\mathcal Mv_H(t)|
 \le\exp[-cL^2\log L].}
 \tag{R-19806.14}
\]

This is a phase-space concentration statement: the Mellin mass of a complete
degree-`L^2` Hermite packet can be placed far outside a window of width `L`.

## 4. Transfer to the finite sample matrix

There are `O(L^2)` sample rows. The zeta multiplier on

\[
 \Re s=1/2,
 \qquad |\Im s|\le T
\]

has a polynomial upper bound. Therefore (R-19806.14) gives, for the exact
Hermite source map,

\[
 \|P_N\Sigma_\mu E(v_H)\|_2
 \le\exp[-cL^2\log L].
 \tag{R-19806.15}
\]

The result is independent of zero multiplicities and remains true if the zeta
factor is deleted entirely.

## 5. Transfer to the prolate packet

`L-16219` gives, uniformly through the complete quadratic-log mode window,

\[
 \|h_{n,\lambda}-h_n\|_2
 \le C(n+1)^A R^{-2/3}\log R,
 \qquad R=2\pi\lambda^2.
 \tag{R-19806.16}
\]

The exact source-constraint maps and their two-anchor repairs are uniformly
conditioned by `L-16218`. Hence the Hermite and prolate exact-radical subspaces
have gap

\[
 O((\log R)^C R^{-2/3}).
 \tag{R-19806.17}
\]

The central ODE estimates used in `L-16219`, together with the Gaussian tail,
transfer (R-19806.16) to every Mellin sample in (R-19806.8) with another fixed
polylogarithmic loss. Thus there is a unit vector `v_R` in the exact complete
prolate source space for which

\[
 \boxed{
 \|P_N\Sigma_\mu E(v_R)\|_2
 \le C(\log R)^C R^{-2/3}.}
 \tag{R-19806.18}
\]

Consequently,

\[
 \boxed{
 \sigma_{\min}\!\left(
 P_N\Sigma_\mu E|_{\mathcal U_R}
 \right)
 \le C(\log R)^C R^{-2/3}.}
 \tag{R-19806.19}
\]

Since every fixed inverse power of `log R` is eventually much larger than the
right side, the proposed lower bound (R-19806.1) is impossible.

## 6. What is and is not refuted

The refutation applies to:

```text
ordinary source metric,
complete quadratic-log prolate packet,
full Euclidean singular-value floor.
```

It does not refute:

1. qualitative surjectivity away from exact cycles;
2. a low-mode packet of dimension `O(log R)`;
3. a defect-weighted or pullback-metric frame inequality;
4. a mixed frame with only the first signed prolate directions retained and the
   remaining finite coordinates synthesized differently;
5. the weaker invariant condition actually used by a corrected ground-state
   transfer.

Indeed, the correct route must exploit that high prolate modes have much larger
defect energy. Demanding the same singular floor in every high source direction
throws away precisely that reserve.

## 7. Consequence for the independent review

The reviewer was right that qualitative generic support does not imply a
polylogarithmic right inverse. The stronger conclusion is now available:

\[
 \boxed{
 \text{the requested complete polylogarithmic right inverse is false.}}
\]

Thus item 1 cannot be repaired by proving the theorem exactly as stated. It must
be replaced by a weighted, low-mode, or mixed-frame theorem.

## 8. Proof boundary

- The Hermite polynomial concentration argument is exact.
- The Hermite-to-prolate transfer uses the same uniform asymptotic interface
  already assumed by the proposed prolate proof.
- An independent audit should check the Mellin/Hermite normalization and the
  pointwise transfer from (R-19806.16) to the finite sample rows.
- No conclusion about RH follows from this refutation alone.
