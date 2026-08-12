# L-91333 — Balanced and reserve parity channels have an exact nonduplicating least-prime source partition

Claim ID: `L-91333`  
Status: **PROVED EXACT MEASURE-TYPED SOURCE TREE; PHYSICAL RESET ASSEMBLY OPEN**  
Created: 2026-08-12  
Depends on exact paths:

- `claims/lemmas/L-91109-factor54-window-has-a-positive-parity-shadow-automaton.md`;
- `claims/lemmas/L-91315-balanced-rough-ray-is-uniquely-mass-and-score-neutral.md`;
- `claims/lemmas/L-91330-balanced-two-channel-reset-has-an-exact-nonduplicating-row-partition.md`;
- `claims/refutations/R-91305-heterogeneous-corridor-channels-do-not-share-a-common-hall-transport.md`.

RH status: **unproved**

## 1. Paired parity source at parameter `a`

For real `a>=1`, real `x>=1`, and squarefree `n<=x`, put

\[
 w_a(x,n)=\frac{a\sqrt x}{n}-\frac1{\sqrt n}>0.
\]

For the ordered primes `p_j`, define positive even and odd source measures
restricted by least prime:

\[
 E_j^{(a)}(x)
 =\sum_{\substack{n\le x,\ n\text{ squarefree}\\
 P^-(n)\ge p_j,\ \omega(n)\text{ even}}}
 w_a(x,n)\,\delta_n,
\]

\[
 O_j^{(a)}(x)
 =\sum_{\substack{n\le x,\ n\text{ squarefree}\\
 P^-(n)\ge p_j,\ \omega(n)\text{ odd}}}
 w_a(x,n)\,\delta_n.
\]

The paired source state is

\[
 \boxed{\mathbf P_j^{(a)}(x)=(E_j^{(a)}(x),O_j^{(a)}(x)).}
\]

The parameter label `a` belongs to the pair. It is not attached independently
to the even and odd coordinates.

## 2. Exact least-prime recursion

Let

\[
 \phi_a(x)=a\sqrt x-1
\]

and let `S` swap the two parity coordinates. Every nontrivial squarefree integer
has a unique least prime, and

\[
 p^{-1/2}w_a(x/p,n)=w_a(x,pn).
\]

Therefore

\[
 \boxed{
 \mathbf P_j^{(a)}(x)
 =\binom{\phi_a(x)}0
 +\sum_{\substack{k\ge j\\p_k\le x}}
 p_k^{-1/2}S\,\mathbf P_{k+1}^{(a)}(x/p_k).
 }
\tag{L-91333.1}

Every summand is a positive measure and every source atom occurs exactly once.
This is a measure identity, not merely equality of total masses.

Most importantly, the child state in every summand carries the **same parameter
`a`** as the parent. Parameter drift appears only if delayed child states are
collapsed into one fixed-scale two-state matrix before reset.

## 3. Finite-block expansion

For any finite initial prime block `p_j,...,p_{m-1}`, iteration of
(L-91333.1) gives

\[
 \boxed{
 \mathbf P_j^{(a)}(x)
 =\sum_{d\mid P_{j,m}}
 d^{-1/2}S^{\omega(d)}
 \mathbf P_m^{(a)}(x/d),
 }
\tag{L-91333.2}

where

\[
 P_{j,m}=\prod_{j\le k<m}p_k
\]

and terms with `d>x` vanish. The Boolean states are positive and disjoint by
their unique small-prime subset.

For the initial block through `61`, `m` is the index of `67`. Every nontrivial
child then has argument at most `x/67<c_0x`.

## 4. Exact SHARP source partition into two fixed paired channels

Put

\[
 \kappa_*=-\frac{2(1+\zeta(1/2))}{2+\zeta(1/2)},
 \qquad
 a_*=-\frac2{\zeta(1/2)}.
\]

The atomwise identity of `L-91330` is

\[
 w_\Psi
 =(1+\kappa_*)w_{a_*}
 +(2-\kappa_*)w_1.
\]

Attach separate channel labels `bal` and `res` before applying the least-prime
recursion. Equations (L-91333.1)--(L-91333.2) act independently on those labels
and preserve their parameters. Hence the complete SHARP source has the exact
positive tree partition

\[
 \boxed{
 \mathbf P_j^{\Psi}
 =(1+\kappa_*)\mathbf P_j^{(a_*)}
 \oplus
 (2-\kappa_*)\mathbf P_j^{(1)}.
 }
\tag{L-91333.3}

No arithmetic atom, parity mass, small-prime state, or rough least-prime branch
is duplicated. The signed observation is exactly

\[
 \Psi=H_*+(2-\kappa_*)R.
\]

## 5. Why the heterogeneous Hall counterexample does not apply

`R-91305` proves that arbitrary branchwise parameters in `[4/3,3/2]` cannot be
mixed after forgetting their pair labels. The partition (L-91333.3) never does
that. It retains two fixed paired parameters:

\[
 a=a_*,\qquad a=1.
\]

Each channel uses its own no-upward Hall transport and exact component-row lift.
The source labels remain disjoint through every least-prime delay.

Thus the **source-typing** objection in PR #405 is repaired at the arithmetic
measure-tree level without the false completed matrices `N_p`.

## 6. Linear total-variation ledger

Let `|P|` denote the total positive mass of a paired source. Taking total mass in
(L-91333.1) gives the exact coefficient-one ledger

\[
 \boxed{
 |\mathbf P_j^{(a)}(x)|
 =\phi_a(x)
 +\sum_{\substack{k\ge j\\p_k\le x}}
 p_k^{-1/2}|\mathbf P_{k+1}^{(a)}(x/p_k)|.
 }
\tag{L-91333.4
 }

The summands are source-disjoint. This is the measure-level counterpart of the
linear four-state telescope in `L-91327`.

It does not imply that the signed Hall residual or the physical target capacity
has the same additive decomposition. Those require the reset projection.

## 7. Exact remaining commuting theorem

The only missing arrow after (L-91333.3) is no longer an unspecified native
source partition. It is the commutation of the local Hall/row producer with the
positive delayed tree:

\[
 \boxed{
 \mathcal P_a\left[
  \binom{\phi_a}0+
  \sum_p p^{-1/2}S\mathbf P_{p+}^{(a)}(\cdot/p)
 \right]
 =
 \mathcal O_a+
  \sum_p\mathcal A_p\mathcal P_a[\mathbf P_{p+}^{(a)}],
 }
\tag{L-91333.5}

with:

```text
all terms positive endpoint-row packets;
one-use ordinary and radix-four capacity;
all fractional terminal losses paid once;
nonnegative residual paired state at the contracted endpoint;
coefficient-one score transfer plus O(1) reset debt.
```

The left side is a nonlinear Hall projection; (L-91333.5) does not follow from
source linearity. It is the genuine all-generation theorem.

## 8. Proof boundary

```text
paired channel source measure                         EXACT
least-prime positive recursion                         EXACT
finite Boolean expansion                               EXACT
parameter labels preserved through all delays          EXACT
atomwise balanced/reserve SHARP source split            EXACT
nonduplicating complete source tree                     EXACT
linear positive source-mass ledger                      EXACT
Hall/row producer commutes with delayed source tree     OPEN / RH-BEARING
physical capacity and score recurrence                  OPEN
Riemann Hypothesis                                      UNPROVEN
```
