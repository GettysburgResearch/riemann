# T-23701 — Carry phase-frame full RH proposal

Claim ID: `T-23701`  
Title: Reconstruct the critical prime ramp from four unconditional positive carry bands  
Status: `FULL PROPOSAL — GAP/BLOCKED AT THE PHASE-RENEWAL THEOREM`  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-07  
Scope: proposed global proof architecture  
RH status: **not proved**

## 1. Executive statement

The proposal replaces exact Carry Saturation by a weaker, source-specific
positive minorant.

For each endpoint `2<=T<=X` and band `r=1,2,3,4`, `L-23703` supplies an explicit
nonnegative coefficient vector `a_(T,r)`. Define

\[
\Gamma_{T,r}(q)=\sum_n a_{T,r}(n)\beta_{nq},
\qquad
\mathcal H_{T,r}=\sum_n a_{T,r}(n)G_n.
\tag{T-23701.1}
\]

The load-bearing theorem is:

> **Carry Phase-Frame Theorem `CPF`.** For every `epsilon>0`, there is
> `C_epsilon` such that for every sufficiently large integer `X` there are
> nonnegative weights `lambda_(T,r)` satisfying
> \[
> \sum_{T=2}^{X}\sum_{r=1}^{4}
>  \lambda_{T,r}\Gamma_{T,r}(q)
> \le \frac1{\sqrt q}\log\frac Xq
> \quad(2\le q\le X),
> \tag{T-23701.2}
> \]
> and
> \[
> \sum_{T=2}^{X}\sum_{r=1}^{4}
>  \lambda_{T,r}\mathcal H_{T,r}
> \ge4\sqrt X-C_\epsilon X^\epsilon.
> \tag{T-23701.3}
> \]

Every object in `CPF` is finite and elementary: floors, logarithms, square
roots, factorials, Möbius values `mu(1),...,mu(4)`, and nonnegative real weights.
No zero, contour, large sieve, or unbounded operator occurs in its statement.

## 2. `CPF` implies the critical prime-ramp bound

Let

\[
P_X=\sum_{q=p^k\le X}
 \frac{\Lambda(q)}{\sqrt q}\log\frac Xq.
\tag{T-23701.4}
\]

Multiply (T-23701.2) by `Lambda(q)>=0` and sum over prime powers. By
`L-23702.5`,

\[
\sum_{q=p^k\le X}\Lambda(q)\Gamma_{T,r}(q)
 =\mathcal H_{T,r}.
\tag{T-23701.5}
\]

Therefore `CPF` gives

\[
\boxed{P_X\ge4\sqrt X-C_\epsilon X^\epsilon.}
\tag{T-23701.6}
\]

No prime estimate is used in this implication. The lower bound is supplied by
binomial entropy carried through an exact prime-power valuation identity.

## 3. Prime-ramp bound to RH

Set `X=N^2`. The exact square-screw formula in source-pinned `T-19801` is

\[
\mathscr S(N)=\Psi(2\log N)
 =4(N+N^{-1}-2)-P_{N^2}+O(\log N),
\tag{T-23701.7}
\]

where the `O(log N)` is an explicit digamma/Lerch expression, not an omitted
prime tail.

Equation (T-23701.6) yields the one-sided subpolynomial upper envelope

\[
\boxed{
\Psi(2\log N)\le N^{o(1)}.}
\tag{T-23701.8}
\]

The square mesh has spacing `asymp exp(-t/2)`, while the unconditional derivative
budget is `exp(t/2)` up to a polynomial. The interpolation lemma used by
`T-19801` therefore promotes (T-23701.8) to

\[
\Psi(t)\le C_\delta(1+t)^{B_\delta}e^{\delta t}
\qquad(t\ge0)
\tag{T-23701.9}
\]

for every `delta>0`.

Apply Landau's one-sign Laplace theorem to

\[
C_\delta(1+t)^{B_\delta}e^{\delta t}-\Psi(t)\ge0.
\]

Together with

\[
\int_0^\infty\Psi(t)e^{izt}dt
 =-z^{-2}\frac{\xi'}{\xi}(1/2-iz),
\tag{T-23701.10}
\]

this excludes every zero with `Re rho>1/2+delta`. Letting `delta` tend to zero
and using functional-equation symmetry gives RH.

This is the sign-reversed companion of the negative-part transfer proved in
`T-19801`; a reviewer should audit the one-sign orientation independently.

Hence

\[
\boxed{\mathrm{CPF}\Longrightarrow\mathrm{RH}.}
\tag{T-23701.11}
\]

## 4. Concrete route to `CPF`: four-band phase renewal

The proposal does not leave `CPF` as an unstructured linear program. It supplies
the following intended proof.

### Step A — pass to logarithmic phase

Use the explicit continuum kernels `k_1,...,k_4` from `L-23704`. They satisfy

\[
\sum_{r=1}^{4}k_r(v)=v
\quad(0\le v<\log5)
\tag{T-23701.12}
\]

and the critical mass identities

\[
\int_0^\infty e^{-v/2}k_r(v)dv=h_r.
\tag{T-23701.13}
\]

The quotient phase is `v mod log5`; the four bands activate at phases
`0,log2,log3,log4`.

### Step B — prove positive phase renewal

For every horizon `Z`, construct nonnegative measures
`lambda_(r,Z)` on `[0,Z]` such that

\[
\sum_{r=1}^{4}(k_r*\lambda_{r,Z})(v)\le v
\qquad(0\le v\le Z)
\tag{T-23701.14}
\]

and

\[
\int_0^Z
\left[v-\sum_r(k_r*\lambda_{r,Z})(v)\right]e^{-v/2}dv
\le C(1+Z)^A e^{-Z/2}.
\tag{T-23701.15}
\]

By `L-23704.17`, this is exactly the asymptotically sharp entropy statement.

The proposed proof is a four-component Volterra induction over successive
`log5` cells. On each cell:

1. retain the incoming nonnegative reserve as a function of phase;
2. use the newly activating quotient bands to saturate the first contact points;
3. recombine all four spills before imposing an inequality;
4. propagate the residual through a positive phase-transfer operator;
5. prove contraction only on the critical-mass-zero subspace.

The critical left vector is fixed by (T-23701.13); therefore contraction of the
orthogonal defect cannot lose the constant `4`.

### Step C — return to finite floors

Take

\[
Z_X=\log X-B\log\log(2X).
\tag{T-23701.16}
\]

Discretize the phase measures onto integer endpoints `T=floor(Xe^{-u})` and the
four exact atoms of `L-23703`. Prove a bounded-variation floor estimate after
complete band recombination. The total loss from the macroscopic range must be
`O((log X)^A)`; endpoints below `(log X)^B` are closed directly by finite
backward substitution.

This produces (T-23701.2)--(T-23701.3).

The phase discretization is not permitted to discard a fixed fraction of the
critical mass. Its proof must use the exact conserved vector (T-23701.13), not a
generic uniform approximation bound.

## 5. Sparse finite production form

For computation and eventual formalization, use a log-phase mesh

\[
T_j=\left\lfloor X\exp\left(-j\frac{\log5}{H}\right)\right\rfloor,
\qquad H=\lceil(\log(2X))^2\rceil,
\tag{T-23701.17}
\]

with duplicate endpoints removed. The finite linear program has only
`O(H log X)` endpoints and four bands per endpoint. The full theorem does not
depend on this sparse form; all integer endpoints are allowed in `CPF`.

Floating reconnaissance in `X-23701` found that the sparse phase-band cone
recovers more than `99.9%` of the exact finite prime-ramp objective at several
moderate cutoffs. This is evidence only that there is no obvious fixed geometric
loss. It is not evidence for the asymptotic lower bound (T-23701.3).

## 6. Mandatory firewalls

A valid proof of `CPF` must survive all of the following.

1. **Mertens firewall.** PR #229 shows that the first critical Farey cell is an
   RH-equivalent fixed-ratio Mertens increment. The phase proof may not erase
   Möbius coherence by an unsigned norm. It must obtain its strength from the
   positive carry/entropy factorization itself.
2. **Sharp constant.** A certificate with `(4-eta)sqrt(X)` for fixed `eta>0`
   proves nothing at the RH scale. The exact critical mass in `L-23704` must be
   retained.
3. **No hidden full Carry Saturation.** The proof may use only the four outer
   bands unless it separately proves positivity of an inner coefficient.
4. **Floor stability.** A continuum theorem without an `X^{o(1)}` finite-floor
   ledger is incomplete.
5. **One-sided Landau orientation.** The passage from an upper envelope for
   `Psi` to zero exclusion must be reconstructed, not cited by analogy alone.
6. **Prime-free production.** The weights `lambda_(T,r)` may depend on `X` and
   the carry atoms, but not on the locations or signs of prime errors.

## 7. Decisive review hinge

The proposal stands or falls on one theorem:

\[
\boxed{\text{positive four-band phase renewal with vanishing critical-mass defect}.}
\tag{T-23701.18}
\]

A reviewer can reject the route by producing any of the following:

- a nonnegative dual phase functional that forces a fixed critical-mass gap;
- one phase cell where every saturation requires a negative band weight;
- an `Omega(sqrt X)` floor-discretization loss;
- a fixed loss in the Perron/critical conserved direction;
- a failure of the one-sided Landau transfer.

Conversely, a proof of (T-23701.14)--(T-23701.15) plus the declared finite-floor
ledger completes the elementary route.

## 8. Exact status

```text
L-23701 Green factorization                 PROPOSED COMPLETE EXACT ALGEBRA
L-23702 cumulative entropy ledger           PROPOSED COMPLETE EXACT ALGEBRA
L-23703 outer four-band positivity          PROPOSED COMPLETE ELEMENTARY PROOF
L-23704 critical Mellin-mass reduction      PROPOSED COMPLETE CALCULUS
four-band positive phase renewal            OPEN / RH-BEARING
finite floor/BV transfer                    OPEN AS PART OF SAME HINGE
CPF => prime-ramp lower bound               COMPLETE CONDITIONAL
prime-ramp lower bound => RH                PROPOSED COMPLETE TRANSFER
Riemann Hypothesis                          NOT PROVED
```
