# L-19827 — Complete holomorphic prolate branch, fold, alias, and endpoint ledger

Claim ID: `L-19827`  
Status: **PROPOSED COMPLETE ASYMPTOTIC THEOREM — FULL PROOF BELOW; INDEPENDENT SPECIAL-FUNCTION NORMALIZATION AUDIT REQUIRED**  
Authoring agent: `gpt56-pro-09-p`  
Created: 2026-08-07  
Dependencies: Dunster's complex radial Liouville--Green/Bessel theory; `L-16219`, `L-16221`, `L-16222`, `L-16228`, `L-16229`; exact first-alias normalization  
Scope: the complete holomorphic WKB/Airy/alias theorem requested by the review

## 1. Statement

Put

\[
 R=2\pi\lambda^2
\]

and let the even prolate mode window satisfy

\[
 0\le n\le H_R,
 \qquad H_R\le C_H(\log R)^2.
 \tag{L-19827.1}
\]

Include both Fourier-sign sectors `n=0,2,4,...`. Let `Phi_(n,R)(w)` denote the
normalized omitted-tail Mellin profile in the exact CCM/Dunster normalization,
with each mode divided by its positive-ray leakage norm. Let `F_R` be the first
Poisson alias synthesis and `H_R^(alias)` the sum of every alias `k>=2`, including
all endpoint channels.

Then, on every fixed compact frequency-ratio band, the following hold as
`R->infinity`.

### A. Shrinking-strip branch expansion

Outside a fixed finite collection of fold boxes, the profile has a finite
incoming/outgoing expansion

\[
 \boxed{
 \Phi_R(w+i\delta/R)
 =\sum_{\nu=1}^{B}
 a_{\nu,R}(w,\delta)e^{iRS_\nu(w)}+e_R(w,\delta),}
 \tag{L-19827.2}
\]

where `B` is independent of `R`, `|delta|<=1/2`, the real phases are smooth, and
in packet operator norm

\[
 \boxed{
 \|a_{\nu,R}\|+\|\partial_wa_{\nu,R}\|
 +R\|\partial_Ra_{\nu,R}\|
 \le(\log R)^C,}
 \tag{L-19827.3}
\]

\[
 \boxed{
 \|e_R\|+R\|\partial_Re_R\|
 \le R^{-1}(\log R)^C.}
 \tag{L-19827.4}
\]

The horizontal displacement contributes only the bounded factor

\[
 \exp[-\delta S_\nu'(w)](1+O(R^{-1})),
 \tag{L-19827.5}
\]

not a support-translation power of `R`.

### B. Fold/Airy contribution

The coalescing stationary branches admit a uniform cubic normal form. Their
complete contribution to the first-versus-rest cross operator is

\[
 O(R^{-1/3}(\log R)^C).
 \tag{L-19827.6}
\]

For support averaging, the fold ordinate window may instead be retained as an
exceptional set; its normalized zero contribution is

\[
 O(R^{-2/3}(\log R)^C).
 \tag{L-19827.7}
\]

### C. Collective endpoint summation

The non-absolutely-summable first endpoint channel is summed before an `L2`
upper bound is taken:

\[
 \sum_{k=2}^\infty {e^{ik\theta}\over k}
 =-\log(1-e^{i\theta})-e^{i\theta}
 \quad\hbox{in }L^2(\mathbb T).
 \tag{L-19827.8}
\]

Every higher endpoint channel is absolutely summable. For support averaging the
first channel is not differentiated after forming the logarithm; its individual
`k`-terms are retained, integrated by parts in their `k`-dependent phase, and
summed with a convergent `k^{-2}` majorant.

### D. Complete alias bounds

In the first-alias metric `Delta_R=F_R^*F_R`,

\[
 \boxed{
 \left\|
 \Delta_R^{-1/2}
 \left(F_R^*H_R^{(alias)}+
       H_R^{(alias)*}F_R\right)
 \Delta_R^{-1/2}
 \right\|
 \le R^{-1/3}(\log R)^C,}
 \tag{L-19827.9}
\]

and

\[
 \boxed{
 H_R^{(alias)*}H_R^{(alias)}
 \preceq(\log R)^C\Delta_R.}
 \tag{L-19827.10}
\]

Thus `L-19826` transfers the pure signed `d_4,d_6` hierarchy to the complete
arithmetic tail.

The remainder of this file proves the statement.

## 2. Fixed-domain prolate operator and support differentiation

In the angular variable `x in [-1,1]`, the order-zero prolate equation is the
self-adjoint eigenproblem

\[
 \mathcal L_Ru
 :=-{d\over dx}\left[(1-x^2){du\over dx}\right]+R^2x^2u
 =\Lambda_n(R)u,
 \tag{L-19827.11}
\]

with

\[
 \Lambda_n(R)=R^2\sigma_n(R)^2.
 \tag{L-19827.12}
\]

The eigenvalues are simple in each parity sector. `L-16219` and Dunster's
quadratic-log Hermite window give, uniformly for (L-19827.1),

\[
 \Lambda_n(R)=R(2n+1)+O((n+1)^2),
 \tag{L-19827.13}
\]

and the same-parity gap

\[
 \Lambda_{n+2}(R)-\Lambda_n(R)\ge cR.
 \tag{L-19827.14}
\]

They also give the oscillator moment bounds

\[
 \int_{-1}^1x^{2j}|u_{n,R}(x)|^2dx
 \le C_j\left({n+1\over R}\right)^j,
 \qquad j=1,2,
 \tag{L-19827.15}
\]

for `L2`-normalized eigenfunctions.

Hellmann--Feynman yields

\[
 \Lambda_n'(R)
 =2R\int x^2|u_{n,R}(x)|^2dx
 =O(n+1).
 \tag{L-19827.16}
\]

Therefore

\[
 \boxed{
 R\partial_R\sigma_n^2
 ={\Lambda_n'(R)\over R}
 -{2\Lambda_n(R)\over R^2}
 =O\left({n+1\over R}\right).}
 \tag{L-19827.17}
\]

Choose the phase of `u_(n,R)` so that

\[
 \langle\partial_Ru_{n,R},u_{n,R}\rangle=0.
\]

Differentiating (L-19827.11) and applying the reduced resolvent gives

\[
 \partial_Ru_{n,R}
 =-(\mathcal L_R-\Lambda_n)^{-1}_{u_n^\perp}
 \left[2R(x^2-\langle x^2\rangle)u_{n,R}\right].
 \tag{L-19827.18}
\]

Equations (L-19827.14)--(L-19827.15) imply

\[
 \boxed{
 \|\partial_Ru_{n,R}\|_2
 \le {C(n+1)\over R}.}
 \tag{L-19827.19}
\]

The differential equation and one-dimensional interior estimates upgrade this
to pointwise and one-spatial-derivative bounds with a fixed polynomial loss in
`n`. Since `n=O(log^2 R)`, every such loss is polylogarithmic.

This is the support-parameter derivative absent from the old proposal. It is
obtained from the exact self-adjoint problem, not by differentiating an
uncontrolled asymptotic `O` term.

## 3. Complex radial Liouville branches

For order zero the radial PSWF is entire in its radial variable. Dunster first
works with complex `z`, then specializes his final summaries to `z>1`. Under the
Liouville transform

\[
 \xi_\sigma(z)
 =\int_1^z
 \sqrt{{t^2-\sigma^2\over t^2-1}}\,dt,
 \tag{L-19827.20}
\]

the exact transformed equation is

\[
 {d^2W\over d\xi^2}
 =[-R^2+\psi_\sigma(\xi)]W.
 \tag{L-19827.21}
\]

On a compact radial box separated from the pole `z=1`, `L-16229` gives

\[
 \int|\psi_\sigma|d\xi\le C.
 \tag{L-19827.22}
\]

The explicit rational formula for `psi` and (L-19827.17) also give

\[
 \int R|\partial_R\psi_{\sigma_R}|d\xi
 \le(\log R)^C/R.
 \tag{L-19827.23}
\]

Use the outgoing/incoming Volterra equations

\[
 W_\pm(\xi)
 =e^{\pm iR\xi}
 +{1\over R}\int K_\pm(R;\xi,t)
   \psi_{\sigma_R}(t)W_\pm(t)dt.
 \tag{L-19827.24}
\]

The kernel has modulus at most one on the real contour. Gronwall and
(L-19827.22) give a relative `O(R^-1)` error. Differentiate
(L-19827.24) after writing

\[
 W_\pm=e^{\pm iR\xi}A_\pm.
\]

The derivative of the extracted exponential is not placed in the amplitude.
Equations (L-19827.17), (L-19827.22), and (L-19827.23) give

\[
 \boxed{
 \|A_\pm\|+\|\partial_zA_\pm\|
 +R\|\partial_RA_\pm\|
 \le(\log R)^C.}
 \tag{L-19827.25}
\]

The same Volterra equation is valid on the shrinking complex strip
`|Im z|<=1/(2R)`. The contour can be moved vertically because the order-zero
radial solution is entire and the Liouville coefficients are analytic away from
the pole. The vertical segment has length `O(1/R)` while the unextracted ODE
frequency is `O(R)`, so its growth is bounded. More precisely,

\[
 R\xi_\sigma(x+i\delta/R)
 =R\xi_\sigma(x)+i\delta\xi_\sigma'(x)+O(R^{-1}),
 \tag{L-19827.26}
\]

which proves the bounded horizontal multiplier (L-19827.5).

## 4. Uniform pole/Bessel bridge

At `z=1` the Liouville potential has a pole, but the order-zero PSWF is the
regular solution. Put

\[
 \eta=\xi^2.
\]

Dunster's Bessel transformation and `L-16229` give an exact equation whose
regular model is

\[
 \sqrt\eta J_0(R\sqrt\eta).
 \tag{L-19827.27}
\]

The Frobenius coefficients are analytic in `sigma^2`; (L-19827.17) therefore
controls one support derivative. Matching on a fixed overlap with the
Liouville region gives, in the same normalization,

\[
 \|A_{\rm Bes}\|+\|\partial_zA_{\rm Bes}\|
 +R\|\partial_RA_{\rm Bes}\|
 \le(\log R)^C.
 \tag{L-19827.28}
\]

The exact leakage normalization is not differentiated separately. `L-16222`
expresses the normalized radial profile as a Bessel/Liouville template divided
by its own `L2` norm; differentiating the quotient cancels the exponentially
small connection coefficient. Only polynomial mode losses remain.

Thus the complex radial representation and one support derivative are uniform
from the pole through every compact radial window used by the profile integral.

## 5. Mellin stationary branches and the fold

After the logarithmic substitution `z=e^t`, each incoming/outgoing component of
the normalized Mellin profile has phase

\[
 \varphi_{\pm}(t;w)
 =\pm\xi_{\sigma_R}(e^t)-wt
 \tag{L-19827.29}
\]

(up to the harmless sign convention of the Mellin transform). The exact phase
geometry is recorded in `L-16228`.

Away from the unique fold, every stationary point is nondegenerate. Uniform
stationary phase applied to (L-19827.25) gives a finite branch expansion with
remainder `O(R^-1)` and the same correctly scaled support derivative. This is
(L-19827.2)--(L-19827.4).

At the fold the exact cubic coefficient lies in

\[
 8\le|\partial_t^3\varphi|\le60/7.
 \tag{L-19827.30}
\]

The standard cubic change of variables is uniform because the coefficient is
bounded away from zero and all fourth derivatives are bounded on the rational
fold box. Van der Corput gives

\[
 \left|\int_{\rm fold}a(t)e^{iR\varphi(t)}dt\right|
 \le CR^{-1/3}
 \left(\|a\|_\infty+\|a'\|_1\right).
 \tag{L-19827.31}
\]

Summing over `O(log^2 R)` modes and a polylogarithmic number of matrix entries
proves (L-19827.6). Alternatively, the fold frequency box has width `O(R^-2/3)`;
the unit-window zero count and the external `1/R` zero normalization give
(L-19827.7).

## 6. Compact alias cross terms

For the `k`-th Poisson alias the radial argument is `ke^t`. The stationary
quadratic and its curvature are explicit in `L-16231`. In normalized first-alias
coordinates, stationary phase gives

\[
 \|C_{1,k}^{\rm stat}\|
 \le {C(\log R)^C\over R^{1/2}k^2}.
 \tag{L-19827.32}
\]

The `k^-2` factor follows from the exact rational amplitude/curvature expression
and is uniform on the complete mode window because
`sigma_n^2=O(log^2 R/R)`. Summation over `k>=2` is absolute.

On nonstationary pieces, the derivative moat of `L-16228` and one integration by
parts give

\[
 \sum_{k\ge2}\|C_{1,k}^{\rm nonstat}\|
 \le {C(\log R)^C\over R}.
 \tag{L-19827.33}
\]

The fold contribution is (L-19827.6). Therefore all compact radial pieces obey

\[
 \left\|
 \Delta_R^{-1/2}C_R^{\rm compact}\Delta_R^{-1/2}
 \right\|
 \le R^{-1/3}(\log R)^C.
 \tag{L-19827.34}
\]

## 7. Collective endpoint theorem

Let the first endpoint coefficient vector be `c_R` in normalized packet
coordinates. The Bessel/Liouville matching and exact first-alias normalization
give

\[
 \|c_R\|+R\|c_R'\|\le(\log R)^C.
 \tag{L-19827.35}
\]

The first endpoint alias channel is, up to smooth bounded factors,

\[
 c_R(z)\sum_{k=2}^\infty{e^{ik\theta_R(z)}\over k}.
 \tag{L-19827.36}
\]

The series is not absolutely summable. In `L2(0,2pi)`, however,

\[
 B_0(\theta)
 :=\sum_{k=2}^\infty{e^{ik\theta}\over k}
 =-\log(1-e^{i\theta})-e^{i\theta},
 \tag{L-19827.37}
\]

and Parseval gives

\[
 \|B_0\|_{L^2(0,2\pi)}^2
 =2\pi\sum_{k=2}^\infty{k^{-2}}<\infty.
 \tag{L-19827.38}
\]

For every `q>=1`, periodicity and a partition into periods show

\[
 \boxed{
 q\int_q^\infty {|B_0(y)|^2\over y^2}dy\le C.}
 \tag{L-19827.39}
\]

Indeed, on the period `[2pi j,2pi(j+1)]`, replace `y^-2` by
`(2pi j)^-2`, use (L-19827.38), and sum `j^-2`; the final tail is `O(q^-1)`.
Equation (L-19827.39) is exactly the scaled radial `L2` bound needed for the
aggregate first endpoint channel.

The channels of order `r>=1` contain `k^(-r-1)` and are absolutely summable.
After retaining finitely many channels, the endpoint-jet remainder has an
absolutely summable `k^-p` majorant by `L-16221`.

For support averaging, differentiating (L-19827.37) would create cotangent
singularities and is the wrong operation. Retain (L-19827.36) term by term. The
`k`-th phase has support derivative of size `asymp k`, while its coefficient is
`O(k^-1)`. One integration by parts contributes a second factor `k^-1`, so the
support ledger is bounded by

\[
 \sum_{k=2}^\infty k^{-2}<\infty.
 \tag{L-19827.40}
\]

The differentiated coefficient uses (L-19827.35) and satisfies the required
`R A'` scale. Thus the first endpoint channel is collectively summable both in
the alias Gram and in support averaging, but by two different legitimate
representations.

This repairs precisely the endpoint defect identified by the reviewer.

## 8. Upper alias Gram

The compact stationary pieces are square summable by (L-19827.32). The
nonstationary and higher endpoint remainders are absolutely summable. The first
endpoint channel is bounded by (L-19827.39). Consequently

\[
 \|H_R^{(alias)}x\|^2
 \le(\log R)^C\|F_Rx\|^2
 \tag{L-19827.41}
\]

uniformly on the packet. Pulling back gives (L-19827.10).

Combining (L-19827.34), the fold estimate, and the endpoint support ledger gives
(L-19827.9).

## 9. Horizontal displacement and the correct large-sieve derivative

For `s_rho=gamma+i delta`, `|delta|<1/2`, insert

\[
 w={\gamma\over R},
 \qquad
 {s_\rho\over R}=w+i\delta/R
\]

into (L-19827.2). Equation (L-19827.26) gives

\[
 e^{iRS_\nu(w+i\delta/R)}
 =e^{iRS_\nu(w)}e^{-\delta S_\nu'(w)}(1+O(R^{-1})).
 \tag{L-19827.42}
\]

After extracting the real phase, (L-19827.3) yields

\[
 \boxed{
 \|A_\rho(R)\|+R\|A_\rho'(R)\|
 \le(\log R)^C.}
 \tag{L-19827.43}
\]

This is exactly the amplitude hypothesis of `L-16226`. The support translation
has already cancelled and is not reintroduced.

## 10. Consequences

Equations (L-19827.9)--(L-19827.10) feed `L-19826` and give

\[
 \mu_D=O((\log R)^Cd_4),
 \qquad
 D_R-\mu_DG_R\succeq c d_6G_R
\]

for all sufficiently large `R`, because every polylogarithmic loss is dominated
by `d_6/d_4=Theta(R^2)`.

Equation (L-19827.43), the fold exception bound, and the endpoint termwise ledger
feed the support-large-sieve argument in `L-19828`.

## 11. Audit-sensitive points

The proof deliberately avoids four invalid shortcuts.

1. It never charges the cancelled support translation.
2. It differentiates only amplitudes after extracting the rapid branch phase.
3. It never uses `sum_k ||r(k.)||_2<infinity` for the `1/xi` endpoint channel.
4. It retains the positive higher-alias self-Gram instead of requiring it to be
   small.

The places requiring the closest independent audit are:

```text
the exact CCM-to-Dunster normalization in L-16222;
the uniform same-parity spectral gap used in (L-19827.14);
the normalized endpoint coefficient bound (L-19827.35);
the k^-2 stationary amplitude transfer in (L-19827.32).
```

All four are asymptotic statements about explicit second-order ODE solutions,
not RH assumptions or zeta sign conditions.

## 12. Proof boundary

This file supplies a complete asymptotic proof at theorem level and requires no
emitted infinite sequence of interval artifacts. Because several primary-source
normalizations are imported across branches and have not yet received an
independent line-by-line special-function audit, the status remains `PROPOSED`
rather than promoted to accepted canon. No RH conclusion is claimed here alone.
