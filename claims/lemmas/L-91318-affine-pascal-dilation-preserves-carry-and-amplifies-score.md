# L-91318 — Affine Pascal dilation preserves every matched carry exactly and amplifies entropy score

Claim ID: `L-91318`  
Status: **PROVED EXACT FINITE CARRY / COMBINATORIAL SCORE THEOREM — POSITIVE ROUGH-FIBER PROJECTION OPEN**  
Created: 2026-08-12  
Depends on: the averaged and atomized carry definitions; the exact average-binomial entropy row `G_n`  
RH status: **unproved**

## 1. Continuous-column Pascal kernel

For an integer parent `n>=0` and a real column `q>0`, put

\[
 M=n+1,
 \qquad
 a=\left\lceil\frac Mq\right\rceil-1
\]

and define

\[
 \boxed{
 \overline\beta_n(q)
 =\frac{a((a+1)q-M)}M.
 }
\tag{L-91318.1}
\]

If `q>=M`, then `a=0` and the value is zero. Since

\[
 a<\frac Mq\le a+1,
\]

the kernel is nonnegative.

For integer `q`, one has

\[
 a=\left\lfloor\frac nq\right\rfloor,
\]

and

\[
 (a+1)q-M
 =q-1-(n\bmod q).
\]

Therefore

\[
 \boxed{
 \overline\beta_n(q)=\beta_{nq}
 \qquad(q\in\mathbb Z_{\ge2}).
 }
\tag{L-91318.2}
\]

Thus (L-91318.1) is the canonical piecewise-linear extension of the averaged
Pascal carry row to real columns.

## 2. Exact affine covariance

For an integer `m>=1`, define the affine parent lift

\[
 \boxed{
 \Phi_m(n)=m(n+1)-1.
 }
\tag{L-91318.3}

Then

\[
 \Phi_m(n)+1=m(n+1).
\]

The ratio controlling (L-91318.1) is unchanged:

\[
 \frac{\Phi_m(n)+1}{mq}
 =\frac{n+1}{q}.
\]

Hence the same integer `a` occurs on both sides, and

\[
 \boxed{
 \overline\beta_{\Phi_m(n)}(mq)
 =\overline\beta_n(q)
 \qquad(q>0).
 }
\tag{L-91318.4}

In particular, at every integer matched column,

\[
 \boxed{
 \beta_{m(n+1)-1,\,mq}=\beta_{nq}.
 }
\tag{L-91318.5}

The familiar obstruction from the denominator `n+1` disappears exactly under
the affine, rather than homogeneous, dilation.

## 3. Atomized carry covariance

For `0<=j<=n` and `0<=r<m`, put

\[
 N=\Phi_m(n),
 \qquad
 J=mj+r.
\]

Then for every integer `q>=2`,

\[
 \boxed{
 \chi_{N,J}(mq)=\chi_{n,j}(q).
 }
\tag{L-91318.6
 }

Indeed,

\[
 \left\lfloor\frac{mj+r}{mq}\right\rfloor
 =\left\lfloor\frac jq\right\rfloor,
\]

and

\[
 N-J=m(n-j)+(m-1-r),
 \qquad0\le m-1-r<m,
\]

so

\[
 \left\lfloor\frac{N-J}{mq}\right\rfloor
 =\left\lfloor\frac{n-j}{q}\right\rfloor.
\]

The same calculation for `N` gives the parent term. Thus the affine lift is an
exact functor already at the atomized split level.

Averaging uniformly over the unique representation

\[
 J=mj+r,
 \qquad
 0\le j\le n,
 \quad0\le r<m,
\]

recovers (L-91318.5).

## 4. Target and radix-four covariance

Extend the critical target to real columns by

\[
 \overline w_X(q)
 =q^{-1/2}\log(X/q)\mathbf1_{q\le X}.
\tag{L-91318.7}
\]

Then

\[
 \boxed{
 \overline w_X(mq)
 =m^{-1/2}\overline w_{X/m}(q).
 }
\tag{L-91318.8}
\]

The radix-four detail

\[
 \overline\Omega_X(q)
 =\overline w_X(q)-2\overline w_X(4q)
\]

has the same covariance:

\[
 \boxed{
 \overline\Omega_X(mq)
 =m^{-1/2}\overline\Omega_{X/m}(q).
 }
\tag{L-91318.9}

Let `d(n)>=0` be any finite child row vector and define the lifted vector

\[
 \boxed{
 D(\Phi_m(n))=m^{-1/2}d(n),
 }
\tag{L-91318.10}

with zero coefficients elsewhere. Then at every matched real column `mq`,

\[
 \boxed{
 \sum_ND(N)\overline\beta_N(mq)
 =m^{-1/2}\sum_nd(n)\overline\beta_n(q).
 }
\tag{L-91318.11}

Thus continuum-column carry feasibility, ordinary or radix-four, is preserved
exactly under the affine lift. Nonnegative row coefficients remain nonnegative.

For physical integer columns, (L-91318.11) is exact on the rough fiber
`Q=mq`. Contributions to columns outside that color are nonnegative leakage;
a positive rough-fiber projection or allocation is still required before
several lifted children can be superposed in one scalar column space.

## 5. Exact entropy amplification

Use the exact average-binomial entropy row

\[
 G_n=\frac1{n+1}\sum_{j=0}^{n}\log\binom nj.
\tag{L-91318.12}
\]

Put

\[
 N=m(n+1)-1.
\]

Partition a set of `N` elements into `m` labelled blocks of size `n` and one
extra block of size `m-1`. For each `0<=r<m`, fix one `r`-element subset of the
extra block.

An `m`-tuple of `j`-subsets, one from each labelled `n`-block, maps injectively
to an `(mj+r)`-subset of the `N`-set by taking their union and adjoining the
fixed extra `r`-set. Therefore

\[
 \boxed{
 \binom{m(n+1)-1}{mj+r}
 \ge\binom nj^m
 }
\tag{L-91318.13}
\]

for every `j,r`.

Every integer `0<=J<=N` has the unique form `J=mj+r`. Averaging the logarithm of
(L-91318.13) gives

\[
\begin{aligned}
 G_N
 &=\frac1{m(n+1)}
   \sum_{j=0}^{n}\sum_{r=0}^{m-1}
   \log\binom N{mj+r}\\
 &\ge\frac1{m(n+1)}
   \sum_{j=0}^{n}\sum_{r=0}^{m-1}
   m\log\binom nj.
\end{aligned}
\]

Hence

\[
 \boxed{
 G_{m(n+1)-1}\ge mG_n.
 }
\tag{L-91318.14}

Consequently the lifted row vector (L-91318.10) has score

\[
 \boxed{
 \sum_ND(N)G_N
 \ge\sqrt m\sum_nd(n)G_n.
 }
\tag{L-91318.15}

The rough-child dilation is therefore strongly score-favorable; it cannot be the
source of a coefficient greater than one in the score-loss recurrence.

## 6. Colored capacity interpretation

Introduce a colored column `(m,q)` whose physical location is `mq`. Equations
(L-91318.4), (L-91318.8), and (L-91318.11) show that

```text
child Pascal row at endpoint X/m
 -> affine parent row n -> m(n+1)-1
 -> colored parent column (m,q)
```

is an exact positive functor preserving capacity and improving score.

The remaining physical operation is the forgetful map from colored columns to
the single ordinary column `Q`. `L-91317` proves that least-prime labels route
all colors either to the already paid outer block or below the contracted scale,
without coefficient inflation. What remains is to recombine their nonnegative
leakage in the projective `(L,R)` port without spending one physical column more
than once.

## 7. Proof boundary

```text
real-column Pascal B-spline kernel               EXACT
affine covariance n -> m(n+1)-1                 EXACT
atomized split covariance                        EXACT
critical target and radix-four covariance        EXACT
nonnegative matched-fiber row lift               EXACT
entropy amplification G_Phi >= m G_n             EXACT
coefficient-one colored rough-child lift          EXACT
positive projection to uncolored physical columns OPEN
Riemann Hypothesis                               UNPROVED
```
