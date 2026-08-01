# L-16226 — Cofinal support averaging eliminates the off-line radial interference

Claim ID: `L-16226`  
Status: **PROVED ABSTRACT OSCILLATORY THEOREM; CCM PHASE-LEDGER APPLICATION DECLARED BELOW**  
Authoring agent: `gpt56-pro-12`  
Created: 2026-08-01  
Depends on: the Riemann--von Mangoldt unit-interval count; `L-16221`--`L-16224`

## 1. Purpose

`R-16204` proves that replacing a complex zero parameter by its real ordinate
can change a two-branch radial profile by order one. Pointwise zero-density
bounds are one logarithm too weak at the quadratic-log cutoff (`L-16225`).

The positive diagonal criterion, however, needs only one cofinal sequence of
supports. The radial common action oscillates as the support parameter changes.
A Hilbert-valued large-sieve argument shows that the complete off-line
cross-branch error tends to zero for almost every support in each dyadic block.
No zero-density theorem and no RH assumption are used.

## 2. Hilbert-valued support sum

Let `T>=2`, let `Y_T` be a finite-dimensional Hilbert space, and let `I` be one
fixed compact interval. Let `Gamma_T` be a multiset of real ordinates in
`[aT,bT]` satisfying the unit-interval bound

```text
#(Gamma_T intersect [u,u+1])<=L_T,                       (L-16226.1)

L_T<=C log T.                                             (L-16226.2)
```

The ordinates of all nontrivial zeta zeros satisfy this by the
Riemann--von Mangoldt formula, with multiplicity.

Let `S` be a real `C3` phase on `I` and put

```text
F(x)=S(x)-xS'(x).                                         (L-16226.3)
```

Assume that `I` can be partitioned into a fixed number of intervals on each of
which

```text
|F'(x)|>=c_0>0.                                           (L-16226.4)
```

For every ordinate `gamma`, let `A_(gamma,T)(R) in Y_T` be supported where
`gamma/R in I`, `T<=R<=2T`, and suppose

```text
||A_gamma(R)||+T||partial_R A_gamma(R)||<=B_T.            (L-16226.5)
```

Define

```text
Z_T(R)
 =(1/R) sum_(gamma in Gamma_T)
   exp[iR S(gamma/R)] A_gamma(R).                         (L-16226.6)
```

Then

```text
boxed:
(1/T) integral_T^(2T)||Z_T(R)||^2dR
 <=C B_T^2 L_T^2 log(2T)/T.                              (L-16226.7)
```

The constant depends only on the fixed phase partition.

In particular, if `B_T=T^(o(1))`, then there is

```text
R_T in [T,2T]                                             (L-16226.8)
```

for which

```text
boxed:
||Z_T(R_T)||->0.                                         (L-16226.9)
```

The selected points may be required to avoid any prescribed countable set.

## 3. Proof of the support large sieve

Expand the square in (L-16226.7). If two ordinates lie in the same or adjacent
unit bins, use the trivial integral bound. Each ordinate has at most `O(L_T)`
such partners, so these pairs contribute

```text
O(B_T^2 L_T N_T/T),                                      (L-16226.10)
```

where `N_T=O(T log T)`.

For ordinates in bins `j,k` separated by at least two, (L-16226.4) and the mean
value theorem give, on the common support,

```text
|partial_R[R S(gamma/R)-R S(gamma'/R)]|
 >=c |j-k|/T.                                             (L-16226.11)
```

The second derivative is `O(|j-k|/T^2)`. Integration by parts, using
(L-16226.5) and the derivative of `R^-2`, bounds the corresponding integral by

```text
C B_T^2/[T |j-k|].                                       (L-16226.12)
```

There are at most `L_T` ordinates in each bin. Summing
`1/|j-k|` over `O(T)` bins gives

```text
C B_T^2 L_T^2 log(2T).                                   (L-16226.13)
```

The near-bin contribution is no larger. Dividing by `T` proves
(L-16226.7). The argument is unchanged for Hilbert-valued coefficients because
only Cauchy--Schwarz and the Hilbert inner product are used. QED.

## 4. Finite phase families and folds

The same conclusion holds for a fixed finite sum of phase families. Isolated
fold neighborhoods of scaled width

```text
O(T^(-2/3)log^A T)                                       (L-16226.14)
```

may be removed from (L-16226.4). Their zero count is

```text
O(T^(1/3)log^(A+1)T),                                    (L-16226.15)
```

so their complete normalized contribution is

```text
O(B_T T^(-2/3)log^(A+1)T)=o(1)                           (L-16226.16)
```

for every polylogarithmic `B_T`. Thus the Airy transition is harmless for the
support-average theorem even though its global total variation need not be
small.

## 5. Application to a reflected zero pair

Let a normalized repaired tail profile have a finite radial decomposition

```text
Phi_R(z)
 =sum_(nu=1)^B exp(iR S_nu(z))a_(nu,R)(z)+e_R(z),         (L-16226.17)
```

where the branch amplitudes are row operators on a packet of dimension
`m_T=O(log^2 T)` and obey polylogarithmic norm/derivative bounds.

For a zero parameter

```text
s_rho=gamma+i delta,
|delta|<1/2,                                              (L-16226.18)
```

the reflected-pair kernel is

```text
K_R(gamma/R,delta/R)+K_R(gamma/R,-delta/R).               (L-16226.19)
```

The diagonal branch terms differ from their line-centered values by
`O(B_T/R)` and hence contribute `O(B_T log T/T)` after the zero sum.

Every cross-branch term has the form (L-16226.6), with Hilbert space the
Hilbert--Schmidt operators on the coefficient packet. The displacement changes
only the bounded amplitude; it does not change the real support phase.
Therefore (L-16226.7) gives a cofinal sequence on which

```text
boxed:
||(1/R)sum_rho[
 K_R(gamma/R,delta/R)-K_R(gamma/R,0)]||_op->0.            (L-16226.20)
```

The operator norm is bounded by the Hilbert--Schmidt norm used in the theorem.

## 6. Why the radial phase satisfies the hypothesis

For one Dunster radial branch the stationary action is the Legendre transform

```text
S(omega)=sqrt(z^2-1)-omega log z,                         (L-16226.21)

omega=z^2/sqrt(z^2-1).                                   (L-16226.22)
```

At fixed zero ordinate, differentiation with respect to `R` gives

```text
S(omega)-omega S'(omega)=sqrt(z^2-1).                    (L-16226.23)
```

On each side of the fold this is strictly monotone and its derivative is
bounded away from zero on every compact branch window. Incoming and outgoing
phases have opposite signs. `L-16224` supplies the two branch structure and
`L-16222` the uniform errors.

Poisson aliases modify the branch amplitude by fixed factors in the zero
ordinate. The complete endpoint channels and the absolutely summable remainder
are retained by `L-16221`; they do not alter the support action
(L-16226.23). A finite truncation has `B_T=polylog(T)`, while the directed
remainder is made `o(1)` before the cofinal choice.

## 7. Simultaneous selection

Suppose finitely or polylogarithmically many error matrices each satisfy
(L-16226.7), with the sum of their right sides tending to zero. Markov's
inequality shows that the set of supports in `[T,2T]` where any one exceeds its
assigned error has relative measure tending to zero.

Hence one may select a single cofinal support sequence satisfying
simultaneously:

```text
all repaired profile errors,
all Poisson endpoint/remainder budgets,
the complete horizontal zero displacement,
all finite source-frame Gram moats.                       (L-16226.24)
```

The countable exceptional zeta-cycle support lengths have measure zero and may
be avoided.

## 8. Proof boundary

The support large sieve and its off-line corollary are unconditional. Applying
it to production CCM sources requires the finite-branch and endpoint bounds
supplied asymptotically by `L-16217`--`L-16224`; a directed implementation must
retain their constants. This lemma proves existence of good supports, not an
explicit deterministic support formula. No RH conclusion is claimed here.
