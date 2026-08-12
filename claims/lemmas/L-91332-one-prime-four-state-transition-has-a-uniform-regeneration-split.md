# L-91332 — Every one-prime four-state transition has a uniform canonical regeneration split

Claim ID: `L-91332`  
Status: **PROVED EXACT STATE-SPACE REGENERATION; MEASURE-TYPED RESET ASSEMBLY OPEN**  
Created: 2026-08-12  
Depends on exact paths:

- `claims/lemmas/L-91317-active-rough-euler-cubes-are-positive-dilations.md`;
- `claims/lemmas/L-91318-affine-pascal-dilation-preserves-carry-and-amplifies-score.md`;
- `claims/lemmas/L-91327-rough-euler-semigroup-has-a-positive-four-state-linear-dilation.md`;
- `claims/lemmas/L-91329-fractional-terminal-endpoint-atoms-have-uniform-lower-response.md`;
- `claims/lemmas/L-91330-balanced-two-channel-reset-has-an-exact-nonduplicating-row-partition.md`;
- `claims/lemmas/L-91331-one-rough-prime-sharp-channel-has-uniform-no-upward-hall-and-row-lift.md`.

RH status: **unproved**

## 1. Positive four-state source

Use the diagonal arithmetic modes

\[
X=L-R,
\qquad
Y=L-2R,
\]

and their source-faithful parity decomposition

\[
X=X_+-X_-,
\qquad
Y=Y_+-Y_-,
\qquad
z=(X_+,X_-,Y_+,Y_-)^T\ge0.
\]

The SHARP observation is

\[
\boxed{
\Psi(z)=(4,-4,-3,3)z=4X-3Y.
}
\tag{L-91332.1}
\]

For one rough prime `p>=67`, put

\[
r=p^{-1/2},
\qquad
A=1-r^2,
\qquad
B=1-r.
\]

The exact positive four-state action is

\[
\boxed{
D_p=\operatorname{diag}(A,A,B,B).
}
\tag{L-91332.2}
\]

## 2. A uniform Doeblin split

Set

\[
\boxed{
c_p=\frac{B}{50}
}
\tag{L-91332.3}
\]

and

\[
\boxed{
R_p=D_p-c_pI_4
=\operatorname{diag}(A-c_p,A-c_p,B-c_p,B-c_p).
}
\tag{L-91332.4}
\]

Every entry of `R_p` is positive and

\[
\boxed{D_p=c_pI_4+R_p.}
\tag{L-91332.5}
\]

Thus every positive post-prime state splits coefficientwise, without source
duplication, into

```text
canonical residual state:  c_p z;
complementary state:       R_p z.
```

The residual is the same four-state source type as `z`, and

\[
0<c_p<\frac1{50}.
\tag{L-91332.6}
\]

## 3. The complementary observation lies in the uniform Hall corridor

The SHARP observation of the complementary state is

\[
\begin{aligned}
\Psi(R_pz)
&=4(A-c_p)X-3(B-c_p)Y\\
&=3(B-c_p)U_{b_p},
\end{aligned}
\tag{L-91332.7}
\]

where `U_b=bX-Y` and

\[
\boxed{
b_p
=\frac{4(A-c_p)}{3(B-c_p)}
=\frac43\left(1+\frac{50}{49\sqrt p}\right).
}
\tag{L-91332.8}
\]

Clearly `b_p>4/3`. The exact integer inequality

\[
400^2<49^2\cdot67
\]

implies

\[
\frac1{\sqrt p}\le\frac1{\sqrt{67}}<\frac{49}{400}
\qquad(p\ge67).
\]

Therefore

\[
\boxed{
\frac43<b_p<\frac32.
}
\tag{L-91332.9}
\]

At the exact state-algebra level, `R_pz` is therefore a compact-corridor SHARP
channel. `L-91331` supplies the corresponding no-upward Hall and exact-row
producer whenever the source presented at the reset boundary is the canonical
Möbius channel represented by `z`.

## 4. Commutation with linear physical functors

The split (L-91332.5) occurs before observation. Every subsequent map already
used by the route is linear:

- affine Pascal lifting;
- ordinary and fractional-column response;
- radix-four detail response;
- positive B-spline quantization;
- source-to-target Markov transport;
- finite score evaluation.

Each such map preserves the exact two-summand decomposition. The fractional
terminal packet of `L-91329` pays the real-column terminal loss after the sum is
formed, so it is not replicated branchwise.

## 5. Consequence under a typed least-prime subpartition

Suppose one reset generation presents pairwise source-disjoint positive branch
states `z_b`, with least primes `p_b>=67`, satisfying the coefficientwise
measure inequality

\[
\sum_b z_b\preceq z_{\rm in}.
\tag{L-91332.10}
\]

Apply (L-91332.5) to each branch. The canonical recursive state is

\[
z_{\rm next}=\sum_b c_{p_b}z_b.
\]

For the positive total-variation ledger

\[
\mathfrak m(z)=X_++X_-+Y_++Y_-,
\]

one gets

\[
\boxed{
\mathfrak m(z_{\rm next})
<\frac1{50}\sum_b\mathfrak m(z_b)
\le\frac1{50}\mathfrak m(z_{\rm in}).
}
\tag{L-91332.11}
\]

Hence a correctly typed recursive use of the split has geometric residual bound

\[
\boxed{
\mathfrak m(z^{(j)})\le50^{-j}\mathfrak m(z^{(0)}).
}
\tag{L-91332.12}
\]

The complementary `R_(p_b)z_b` pieces are in the uniform Hall corridor and are
assigned to the same generation's positive row producer.

## 6. Score implication, conditional on the typed source ledger

The Hall interval packets have nonnegative score. Martingale quantization is
score-favorable, and affine Pascal dilation amplifies the naturally normalized
child score. Therefore, after the one global safety scaling and fixed omissions,
a typed source partition as in (L-91332.10) would give the strengthened reset
recurrence

\[
\boxed{
\mathfrak L_X
\le\frac1{50}\mathfrak L_{K_X}+O(1),
\qquad
K_X\le c_0X+O(1).
}
\tag{L-91332.13}
\]

This is stronger than the coefficient-one recurrence consumed by `T-91101`.

## 7. Scope firewall

This theorem does not propagate the refuted positive two-state completion
`N_p`. It splits the exact arithmetic four-state action before observation.

The remaining load-bearing issue is not the matrix algebra. It is the exact
measure typing of (L-91332.10): every paired interior, activation frontier,
finite Boolean source, Schur packet and contracted child must appear once in one
positive least-prime partition. Scalar least-prime uniqueness alone is not that
statement.

```text
four-state Doeblin split D_p=c_p I+R_p          EXACT
canonical residual coefficient <1/50             EXACT
complementary parameter 4/3<b_p<3/2              EXACT
commutation with linear physical functors         EXACT
geometric residual under typed subpartition       EXACT CONDITIONAL
measure-valued least-prime subpartition            OPEN / REVIEW-CRITICAL
factor-54 recurrence                              CONDITIONAL
Riemann Hypothesis                                UNPROVED
```
