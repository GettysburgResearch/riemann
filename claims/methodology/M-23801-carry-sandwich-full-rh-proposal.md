# M-23801 — Carry Sandwich full RH proposal

Methodology ID: `M-23801`  
Title: Replace balanced Möbius Type II by a two-sided nonnegative carry certificate whose finite entropy sandwich gives the critical prime ramp  
Status: **FULL PROPOSAL — CARRY SANDWICH THEOREM PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-07  
Issue: #238  
Imported context: PRs #202, #216, #229, #234, #235, #236 at their current reviewed heads  
Scope: independent elementary-facing proposal; RH is not claimed proved

## 1. Why this proposal is different

The dominant arithmetic routes now meet at a signed balanced Möbius packet. A
generic norm estimate loses the signs, while terminal Euler summation removes
only packets with a free macroscopic lattice variable.

The carry matrix compresses the same cancellation into a finite cone. Exact
Carry Saturation asks for one triangular inverse to be nonnegative. The present
proposal is weaker:

\[
\boxed{
\text{find any nonnegative packing below the target and any nonnegative cover
above it, both entropy-sharp}.}
\]

The two certificates may be different. Isolated negative entries of the exact
inverse are permitted.

## 2. Finite objects

For every endpoint `X`, construct:

1. the exact rational carry matrix `B_X=(beta_(nq))`;
2. the target `w_X(q)=q^(-1/2)log(X/q)`;
3. the binomial-row entropy values
   \[
   G_n={1\over n+1}\sum_{j=0}^{n}\log\binom nj;
   \]
4. the canonical greedy packing `d_X^gr` of `L-23802`;
5. the exact triangular inverse `c_X` and canonical cover `c_X^+`.

The proposed theorem is the two-sided estimate

\[
\boxed{
\sum_n d_X^{\rm gr}(n)G_n
\ge4\sqrt X-X^{o(1)},
\qquad
\sum_n c_X^+(n)G_n
\le4\sqrt X+X^{o(1)}.}
\tag{M-23801.1}
\]

A more flexible proof may replace either canonical vector by another explicitly
source-bound nonnegative certificate.

`T-23801` proves that (M-23801.1) implies RH.

## 3. Exact quotient-layer coordinates

The key algebra is the Möbius adjoint identity

\[
\sum_{k\le n/m}\mu(k)\beta_{n,mk}
={2m-n-1\over n+1}.
\tag{M-23801.2}
\]

For the exact inverse, put

\[
u_m=\sum_{k\le X/m}\mu(k)w_X(mk).
\]

Then

\[
 c_j
 ={(j+1)[j u_j-(j-2)u_{j+1}]
   +2\sum_{m=j+2}^{X}u_m
  \over j(j-1)}.
\tag{M-23801.3}
\]

On the quotient cell

\[
{X\over r+1}<m\le{X\over r},
\]

only `mu(1),...,mu(r)` occur. The full proof must group the complete `r`-cell
before taking a positive or negative part.

This is the carry analogue of the signed common-cell rule in BTP.

## 4. Proposed obstacle theorem

Let `rho_X^(n)` be the descending greedy residual of `L-23802`, and put

\[
\Delta_{X,n}(q)
=\rho_X^{(n)}(q)\beta_{nn}
 -\rho_X^{(n)}(n)\beta_{nq}.
\tag{M-23801.4}
\]

Exact Carry Saturation is the strong invariant

\[
\Delta_{X,n}(q)\ge0
\qquad(2\le q\le n\le X).
\tag{M-23801.5}
\]

The proposal requires only the following weaker, aggregated theorem.

> **Carry Obstacle Theorem `CO(X)`.** After grouping complete quotient cells,
> the total entropy loss caused by off-diagonal greedy saturations and the
> weighted negative mass of the exact inverse satisfy
> \[
> \boxed{
> \sum_{n=2}^{X}n(c_X(n))_-
> +\sum_{n=2}^{X}n\,[c_X(n)-d_X^{\rm gr}(n)]_+
> =X^{o(1)}.}
> \tag{M-23801.6}
> \]
> In addition the signed continuum carry mass has the sharp elementary
> archimedean normalization, with a subpolynomial endpoint ledger.

Equation (M-23801.6) is strictly weaker than (M-23801.5). It permits finitely or
thinly many negative coefficients and off-diagonal saturation events.

## 5. Intended proof of the obstacle theorem

### 5.1 Complete quotient-cell recombination

Use (M-23801.2) before absolute values. The `r`-th cell is a finite signed
combination involving only `mu(k), k<=r`. Its two boundary rows are carried to
the neighboring cells rather than estimated separately.

### 5.2 Layer potential

For one complete cell define

\[
\mathscr V_r
=\sum_{m\in I_r}
 \left[
  (m+1)m u_m-(m+1)(m-2)u_{m+1}
 \right]
 +2\sum_{m\in I_r}
  \sum_{h\ge m+2}u_h.
\tag{M-23801.7}
\]

The internal tail terms telescope after adjacent quotient cells are joined.
Only:

- the outer `r`-boundary;
- the next-cell entrance;
- a finite floor discrepancy;

remain. The proof target is a nonnegative block barrier plus a boundary ledger
of subpolynomial total weight.

### 5.3 Greedy/cover coupling

The same cell potential is evaluated twice:

- on the greedy packing residual;
- on the positive part of the exact inverse.

A negative excursion in one ledger creates slack in the other. The proposal
pairs them before summing in `n`; it never estimates the two errors separately
by total variation.

### 5.4 Sharp archimedean mass

The continuum carry kernel has the exact leading integral producing the
`4 sqrt(X)` mass. Euler--Maclaurin is applied only after complete quotient-cell
recombination. Endpoint and floor errors are required to be `X^(o(1))`.

This phase supplies (M-23801.1) from (M-23801.6).

## 6. Mandatory proof firewalls

A review must reject any proof that:

1. takes absolute values of the Möbius sum in `u_m` before grouping a quotient
   cell;
2. infers the global theorem from positivity on finitely many outer layers;
3. silently replaces the exact inverse by its positive part without paying the
   cover slack;
4. proves only `o(sqrt(X))` error rather than `X^(o(1))`;
5. uses prime-number-theorem or zero-free-region input strong enough to imply the
   final prime-ramp estimate;
6. omits the first fixed-ratio Mertens mutation from PR #229/#234.

The first-cell firewall is automatic at the conclusion: the carry sandwich gives
RH, hence the square-root fixed-ratio Mertens increment. A source-level proof
should also exhibit where that coherent Möbius mode is spent inside the quotient
cell ledger.

## 7. Exact proof-producing schema

One finite certificate contains:

```text
X
complete beta matrix hash
target log/sqrt intervals
greedy saturation column at every n
nonnegative residual intervals
exact triangular inverse intervals
positive/negative inverse split
packing and covering feasibility
G_n entropy intervals
packing objective interval
covering objective interval
4 sqrt(X) comparison
quotient-cell labels
CO(X) loss ledger
```

The consumer must fail closed if a residual crosses zero, a target interval is
ambiguous, or a quotient row is omitted.

## 8. Full proposed chain

```text
finite carry matrix and Legendre identity
-> nonnegative packing/covering programs
-> exact Mobius quotient-layer decoder
-> Carry Obstacle Theorem CO(X)
-> entropy-sharp two-sided carry sandwich
-> prime ramp = 4 sqrt(X) + X^(o(1))
-> Laplace holomorphy in Re z>0
-> no zeta zero with Re rho>1/2
-> RH.
```

## 9. Proof boundary

Exact and ready for review:

- `L-23801` finite carry/Legendre algebra;
- `L-23802` LP duality, greedy packing, and canonical cover;
- `L-23803` Möbius adjoint decoder;
- `T-23801` carry-sandwich-to-RH composition.

Proposed load-bearing theorem:

\[
\boxed{CO(X)\text{ and the resulting sharp carry sandwich}.}
\]

RH is not claimed proved until that quotient-layer obstacle theorem survives
review.