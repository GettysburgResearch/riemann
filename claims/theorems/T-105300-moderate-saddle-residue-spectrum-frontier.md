# T-105300 — Xi moderate saddle, quotient residue spectrum, and reduced descent frontier

Claim ID: `T-105300`  
Status: **MAJOR PROPOSED UNCONDITIONAL ADVANCE; LOW-ORDER DESCENT OPEN**  
Created: 2026-08-23  
Base: dedicated continuation of proposed `T-105200`  
Depends on: `L-105300--L-105302`; proposed parent `L-105200--L-105205`; PRs #716, #720, #723  
RH status: **unproved**

## 1. Exact finite residue spectrum

For every monic polynomial `p` with squarefree derivative, define

\[
U=[p(p'')^{-1}]\quad\text{on }K[z]/(p').
\]

`L-105300` proves that the eigenvalues of `U` are precisely

\[
\rho_c={p(c)\over p''(c)},
\qquad p'(c)=0.
\]

Therefore

\[
\operatorname{Tr}U^r=\sum_c\rho_c^r
\]

for every `r>=1`, and

\[
\det(\lambda I-U)
={\operatorname{Res}(p',\lambda p''-p)
 \over n^2\operatorname{Res}(p',p'')}.
\]

The first and second residue moments are now one debt-free finite spectrum.
PR #723's cross-residue term is an exactly equivalent contour coordinate, not
an intrinsic obstruction to computing the second moment.

For real-rooted `p`,

\[
\rho_c
=-\left(\sum_j(c-x_j)^{-2}\right)^{-1}<0,
\]

and residue coherence is exactly the spectral flatness of `U`.

## 2. Cubic-corrected Xi saddle

Let

\[
\gamma_m=S_m^{(3)}(w_m)s_m^3.
\]

`L-105301` proves

\[
\gamma_m=-\sqrt2\sqrt{w_m/m}(1+o(1))
\]

and the relative one-sided Fourier asymptotic

\[
\boxed{
A_m(z)
=
\exp\!\left(
 iw_mz-{s_m^2z^2\over2}
 +{\gamma_m(i s_mz)^3\over6}
\right)(1+o(1))
}
\tag{T-105300.1}

uniformly for every `m>=M` and

\[
|\Re z|\le C(M/\log M)^{2/3},
\qquad |\Im z|\le H.
\]

The cubic correction is order one at this height and cannot be omitted.

## 3. Dramatically improved high-derivative entry

The analytic phase

\[
\Theta_m(z)=w_mz-{\gamma_ms_m^3z^3\over6}
\]

has no nonreal sine/cosine preimages in a fixed vertical strip and is strictly
increasing on the real axis. `L-105302` uses cellwise Rouché to prove that all
zeros of every `Xi^(m)`, `m>=M`, are real and simple in the common two-thirds
box, with

\[
N_m(T_M)={2w_mT_M\over\pi}+O(1).
\]

At the real zeros of `Xi^(m+1)` in a buffered box,

\[
{\Xi^{(m)}(c)\over\Xi^{(m+2)}(c)}
=-w_m^{-2}(1+o(1)),
\]

so residue coherence is `1-o(1)` uniformly throughout the derivative tail.

Equivalently, a height-`T` rectangle is unconditionally cleared by every
order

\[
\boxed{
m\ge K T^{3/2}\log(2+T),}
\tag{T-105300.2}

subject to independent review of the contour-shift proof. This improves the
natural Gaussian entry order `T^2 log T` by a square-root power.

## 4. Reduced cumulative descent frontier

The exact parent budget gives

\[
O_{\Omega_T}(\Xi)
\le
2\sum_{j<r(T)}R_j(T)(1-\mathfrak C_j(T))
+
\sum_{j<r(T)}(B_j(T)+W_j(T)-1).
\tag{T-105300.3}

The present packet permits

\[
r(T)=O(T^{3/2}\log T)
\]

instead of `O(T^2 log T)`. Thus the unresolved moderate-to-fixed derivative
ledger is materially shorter, but it is not removed.

`CRDB105200` remains the conclusion-facing statement: the right side of
(T-105300.3) must be below two for every sufficiently large regular height.
Then the even nonnegative off-real zero count vanishes and RH follows.

## 5. Next-pass programme on this same PR

The dedicated branch will be continued along two linked targets:

1. **quartic/full saddle extension:** include further standardized saddle
   cumulants and push the entry exponent beyond `2/3`;
2. **spectral-flow descent:** relate the quotient operators of adjacent
   derivative orders and seek a summable variance/winding budget.

No new PR is needed for those passes.

## 6. Exact status

```text
critical-residue quotient spectrum          PROPOSED EXACT / REPLAYED
resultant characteristic polynomial         PROPOSED EXACT / REPLAYED
real-rooted electrostatic residue formula    PROPOSED EXACT
cubic standardized Xi coefficient            PROPOSED COMPLETE
relative two-thirds saddle law                PROPOSED COMPLETE / REVIEW REQUIRED
T^(3/2) log T derivative entry               PROPOSED COMPLETE / REVIEW REQUIRED
high-tail residue coherence                  PROPOSED COMPLETE / REVIEW REQUIRED
low-order cumulative defect/winding budget   OPEN / RH-BEARING
Riemann Hypothesis                           UNPROVEN
```
