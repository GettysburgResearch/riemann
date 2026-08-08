# Weighted shell-tail carry transport — consolidated review report

Date: 2026-08-08  
PR: #240  
Branch: `agent/gpt56-pro/238-carry-packing-minorant`  
Status: review-ready full proposal; `WSTS` open; RH unproved

## Executive conclusion

The carry programme has been reduced to one explicit finite scalar theorem without relying on the failed source-count, reflected-reserve, nonnegative-cover, or complete-Green-energy mechanisms.

The durable chain is:

```text
explicit parabolic seed with score 4 sqrt(X)-O(log^2 X)
-> self-contained fixed-ratio continuum shell majorization
-> finite shell profile plus absolutely summable floor error
-> logarithmically weighted prime upper-tail charge
-> exact zero-cost signed carry transport
-> exact in-support dyadic shell assembly
-> WSTS
-> sharp prime-ramp lower bound
-> square-screw / Landau
-> RH.
```

Every arrow before `WSTS` is represented by a proof-facing file and an explicit formula. `WSTS` is not proved and is the only new RH-bearing assertion.

## What was consolidated

### Historical two-contact route

Superseded. The same-sign Möbius cube showed that two endpoints of a scalar affine interval do not bound the number of arithmetic source coordinates.

### Green/balayage route

Retained as valid exact finite algebra, but removed from the preferred dependency chain. It compresses high-rank geometry to the logarithmic scalar without estimating that scalar.

### Endpoint-scale and affine-lift routes

Retained as independent positive-producer and positivity-lift interfaces. They are not needed for the weighted shell-tail composition and do not alter its proof status.

### Preferred shell route

Promoted as the canonical review target because it supplies:

1. a proved scalar continuum order for every fixed ratio;
2. an exact finite transport theorem matching the logarithmic prime objective;
3. a uniform finite-to-continuum error with summable floor loss;
4. literal shell telescoping;
5. one named prime-sampling remainder.

## Main exact theorem: continuum shell order

For the parabolic defect `E`, define

\[
H(\theta)=\int_\theta^1E(u)du,
\qquad
J(\theta)=H(\theta)/\sqrt\theta.
\]

`L-23823` now derives its reciprocal-cell formula directly and proves

\[
J'(\theta)\ge0.
\]

Since `J(1)=0`, this gives `H<=0` without importing another branch. For a shell ratio `c`,

\[
H_c(\theta)=H(\theta)-\sqrt c H(\theta/c)\le0.
\]

For `c=1/2`,

\[
H_{1/2}(\theta)
\le-(\log2/5)\sqrt\theta
\quad(0<\theta\le1/4).
\]

This is the negative continuum moat that must remain present in every finite estimate.

## Main exact theorem: weighted finite transport

For a signed residual on ordered primes, use weighted masses

\[
\mu_p=(\log p)r_p.
\]

If every upper tail of `mu` is nonpositive, positive residual can be moved to larger-prime slack by exact carry incidence blocks. The destination amount is adjusted so that the logarithmic objective change cancels exactly.

For an arbitrary residual the least one-boundary charge in this class is

\[
\mathcal B(r)
=\max_z\left(\sum_{p\ge z}(\log p)r_p\right)_+.
\]

Paying that charge at the largest prime in the endpoint makes all tails nonpositive; the remaining correction costs zero. This produces an exact signed feasible carry certificate losing at most `mathcal B(r)`.

## Main exact reduction: finite shell to Chebyshev sampling

For the parabolic residual,

\[
r_X(q)=X^{-1/2}E(q/X)
+O\!\left(q^{-3/2}[1+\log(X/q)]\right).
\]

Subtracting the half-scale endpoint gives the shell analogue. The floor error is summable against `log p`. Stieltjes summation yields

\[
\sum_{z\le p\le X}(\log p)s_X(p)
=
\sqrt XH_{1/2}(z/X)
+\mathcal E_X(z)
+O(\log^2X),
\]

where

\[
\mathcal E_X(z)
=X^{-1/2}\int_{[z,X]}E_{1/2}(t/X)d[\vartheta(t)-t].
\]

The first term is nonpositive. Thus the sole remaining theorem is not a generic prime-number-theorem error but the one-sided source-specific bound

\[
\sup_z(\mathcal E_X(z))_+=X^{o(1)}.
\]

## Full proposed theorem

Define

\[
\mathcal B_X
=\max_z\left(\sum_{z\le p\le X}(\log p)
[r_X(p)-\mathbf1_{p\le\lfloor X/2\rfloor}r_{\lfloor X/2\rfloor}(p)]\right)_+.
\]

`WSTS` states

\[
\mathcal B_X\le C_\varepsilon X^\varepsilon
\]

for every `epsilon>0`.

Under `WSTS`, exact dyadic assembly loses only `X^o(1)`, so the complete von Mangoldt ramp is at least

\[
4\sqrt X-X^{o(1)}.
\]

The frozen square-screw/Landau consumer then gives RH.

## Review verdict requested

The reviewer should classify separately:

```text
L-23823  continuum shell theorem
L-23824  finite weighted transport
L-23825  finite shell/Stieltjes reduction
L-23826  shell assembly
T-23811  conditional composition
WSTS      arithmetic theorem
```

The expected pre-review status is:

```text
first five items: proposed complete / independently checkable
WSTS:             open / RH-bearing
RH:               not proved
```

## Decisive rejection tests

Reject any claimed completion that:

- changes the logarithmic prime weight;
- separates positive defect from negative slack before transport;
- takes absolute values of the Chebyshev remainder before adding the moat;
- uses only a classical absolute PNT error;
- proves an average or finite-ladder statement;
- loses the first fixed-ratio Mertens shell;
- imports a superseded source-count, Green-energy, or reflected-reserve theorem.

## Final assessment

The architecture is finished enough for concentrated adversarial review. The mathematics is not yet an accepted proof of RH because `WSTS` remains unproved. The review question is now singular:

> Does the negative parabolic shell moat dominate the one-sided finite Chebyshev sampling fluctuation at subpolynomial scale for every endpoint and every upper tail?

A proof of that statement completes the chain. A counterexample or equivalence/circularity diagnosis rejects only the final hinge and leaves the continuum and transport theorems intact.
