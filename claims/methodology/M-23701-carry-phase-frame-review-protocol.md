# M-23701 — Carry phase-frame adversarial review protocol

Claim ID: `M-23701`  
Status: `REVIEW PROTOCOL`  
Target: `T-23701`

## Review order

1. `L-23701`: derive the floor identity and Möbius Green kernel from scratch.
2. `L-23702`: verify the cumulative kernel and formal entropy increment.
3. `L-23703`: audit the strict `5m>T` boundary and the derivative gate.
4. `L-23704`: reconstruct the scaling kernels and critical Mellin mass.
5. `T-23701` Sections 2--3: check both inequality orientations.
6. Only then review the positive phase-renewal theorem.
7. Finish with the finite-floor/BV transfer and computational reconnaissance.

## A. Exact finite algebra

A reviewer should independently check

\[
(n+1)\beta_{nq}
 =(n+1)\lfloor n/q\rfloor-2\sum_{j\le n}\lfloor j/q\rfloor,
\]

\[
\sum_{k\le n/m}\mu(k)\beta_{n,mk}
 =\frac{2m-n-1}{n+1},
\]

\[
\Delta_{mq}=m\mathbf1_{q|m}-\lfloor m/q\rfloor,
\]

and

\[
F_m-F_{m-1}=\log(m^{m-1}/(m-1)!).
\]

The committed checker is a regression, not a replacement for these proofs.

## B. Outer theorem

Check every endpoint convention:

- the theorem is strict `5m>T`;
- the fourth band excludes `m=T/5` when divisible;
- `mu(4)=0` is retained rather than treated as a positive term;
- the profile is continuous at `L=log2,log3,log4`;
- the minimum derivative occurs at `L=log5` because `C<0`;
- the adjoint tail starts at `m+2`.

One counterexample in this range invalidates the atom dictionary.

## C. Continuum kernel

Reconstruct the scale limit separately on every quotient cell. In particular,
verify that the finite remainder at exact integer quotient boundaries is put in
the floor/BV ledger and is not silently lost.

Test the Mellin calculation

\[
\widehat{\mathcal D S}(s)=\zeta(s)(s-1)s^{-1}\widehat S(s+1)
\]

and the pole cancellation at `s=1`.

## D. Positive phase renewal

The reviewer should request an explicit phase-transfer operator, not only a
claim that a finite LP was feasible.

For each `log5` cell, record:

1. the incoming reserve profile;
2. all four newly placed band measures;
3. the complete outgoing spill;
4. the critical mass before and after;
5. the norm in which the zero-mass defect contracts;
6. endpoint atoms and phase discontinuities.

Reject any proof that bounds the four bands separately before recombination.

## E. Dual attack

The most efficient refutation attempt is the dual cone. Search for a
nonnegative phase functional `Y(v)` such that

\[
\int Y(v)(k_r*\lambda)(v)dv
\]

prices every band below its entropy mass while the target price is strictly less
than `4`. A fixed dual gap rejects the proposal immediately.

At finite `X`, the LP dual is

\[
\min_{y(q)\ge0}\sum_qy(q)w_X(q)
\]

subject to

\[
\sum_qy(q)\Gamma_{T,r}(q)\ge\mathcal H_{T,r}
\]

for every endpoint and band. Inspect the shape of near-optimal dual vectors and
whether they converge to a genuine phase obstruction.

## F. Finite-floor transfer

Require a signed error ledger before taking absolute values. The desired final
loss is `X^{o(1)}`, not `o(sqrt X)` and not a fitted relative error.

The small endpoint block may be checked exactly, but the threshold must be
polylogarithmic and every omitted endpoint must be covered.

## G. RH bridge

Audit the complete explicit square-screw formula, including digamma and Lerch
terms. Then repeat the Landau argument with

\[
C e^{\delta t}(1+t)^B-\Psi(t)\ge0.
\]

The sign-reversed use of the one-sign theorem is a load-bearing dependency.

## H. Computational classification

- `verify.py`: `EXACT_RATIONAL_AND_INTEGER`, finite algebra only.
- transcendental derivative gate: exact rational interval bounds built by the
  checker.
- `recon.py`: `FLOATING_RECONNAISSANCE`, SciPy/HiGHS; no directed guarantee.
- reported LP percentages compare with the exact **finite** prime-ramp objective,
  not with the asymptotic constant `4`.

## Acceptance criterion

Accept the full proposal only if the reviewer can write a complete theorem with
all phase measures, transition inequalities, critical-mass conservation, and
finite-floor errors. Until then the correct classification is `GAP/BLOCKED`,
with the exact Green and outer lemmas reviewed separately.
