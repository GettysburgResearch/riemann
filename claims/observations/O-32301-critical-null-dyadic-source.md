# O-32301 — A critical-null dyadic source simultaneously compacts the bare carry boundary and preserves every off-line zeta pole

Status: **NEW EXACT SOURCE OBSERVATION / GLOBAL HERMITEAN PLACEMENT OPEN**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-09

## 1. Source

Define

\[
 B_\dagger(s)
 =\frac{(1-2^{-s})(1-2^{1/2-s})(1-2^{1-s})}{\zeta(s)}
\]

and let `b_dagger` be its coefficient sequence.

The finite numerator is

\[
 f_\dagger
 =(\varepsilon-\delta_2)
  *(\varepsilon-\sqrt2\,\delta_2)
  *(\varepsilon-2\delta_2)
\]

so

\[
 f_\dagger
 =\varepsilon-(3+\sqrt2)\delta_2
 +(2+3\sqrt2)\delta_4
 -2\sqrt2\delta_8.
\]

Since `1*mu=epsilon`,

\[
 \boxed{\mathbf1*b_\dagger=f_\dagger.}
\]

## 2. Compact bare carry potential

The prefix potential of `f_dagger` is

\[
D_\dagger(x)=
\begin{cases}
0,&0\le x<1,\\
1,&1\le x<2,\\
-2-\sqrt2,&2\le x<4,\\
2\sqrt2,&4\le x<8,\\
0,&x\ge8.
\end{cases}
\]

Hence the bare source charge of a split `n=j+k` is

\[
 Y_\dagger(n,j)=D_\dagger(n)-D_\dagger(j)-D_\dagger(k).
\]

Therefore

\[
 \boxed{n,j,k\ge8\Longrightarrow Y_\dagger(n,j)=0.}
\]

In particular every quarter-balanced row with `n>=32` has exactly zero unweighted source charge. This is stronger than the Q=4 finite adverse collar: the entire cofinal balanced bare-source channel vanishes.

## 3. Positive inverse and generalized primes

The inverse series is

\[
 A_\dagger(s)
 =\frac{\zeta(s)}
 {(1-2^{-s})(1-2^{1/2-s})(1-2^{1-s})}.
\]

Every coefficient is positive. At the prime two its local generating series is

\[
 \frac1{(1-x)^2(1-\sqrt2 x)(1-2x)},
 \qquad x=2^{-s},
\]

which has coefficientwise positive expansion; odd-prime local coefficients are the ordinary zeta coefficients.

The generalized-prime sequence is nonnegative. Explicitly,

\[
 \Lambda_\dagger(p^r)=\log p\quad(p\text{ odd}),
\]

and

\[
 \boxed{
 \Lambda_\dagger(2^r)
 =(\log2)\,[2+2^{r/2}+2^r]>0.
 }
\]

Thus the generalized Selberg machinery applies with a positive inverse and positive generalized primes.

## 4. Pole audit

The three finite factors have zero sets on the vertical lines

\[
 \Re s=0,\qquad\Re s=\frac12,\qquad\Re s=1,
\]

respectively. The `Re s=1` factor removes the ordinary zeta pole. No hypothetical nontrivial zero with

\[
 \frac12<\Re\rho<1
\]

is cancelled.

Therefore a subexponential physical block bound for the `B_dagger` current would still exclude every zero to the right of the critical line.

## 5. Critical-frequency filter

Writing `s=1/2+z` and `w=2^{-z}`, the finite numerator becomes

\[
 \boxed{
 (1-2^{-1/2}w)(1-w)(1-\sqrt2 w).
 }
\]

The middle factor is an exact critical Haar difference. The first factor is strictly stable in the right half-plane, while the third removes only the deterministic `s=1` pole.

Thus the source simultaneously has:

```text
compact unweighted carry boundary;
positive inverse;
positive generalized primes;
critical zero-mode cancellation;
main-pole cancellation;
all off-line zeta poles retained.
```

## 6. Complete dyadic-fiber cancellation of the hinge

At the prime two, the full source `b_dagger` has local polynomial

\[
 P_b(x)=(1-x)^2(1-\sqrt2 x)(1-2x),
\]

because the Mobius factor contributes one additional `(1-x)`.

For an odd squarefree core `m`, a complete two-adic fiber is

\[
 m,2m,4m,8m,16m.
\]

For the square-root hinge

\[
 h_T(n)=n^{-1/2}-T^{-1/2},
\]

the complete fiber contribution is proportional to

\[
 m^{-1/2}P_b(2^{-1/2})-T^{-1/2}P_b(1)=0.
\]

Hence every complete fiber with `16m<=T` cancels exactly, and

\[
 \boxed{
 \sum_{n\le T}b_\dagger(n)h_T(n)
 \text{ is supported only on odd cores }m>T/16.
 }
\]

This is a fixed top-sixteenth arithmetic shell, not a deep unrestricted Mobius tail. It remains RH-sensitive: a fixed-ratio shell can still carry Mertens cancellation, so this localization is not itself a proof.

## 7. Source-curvature simplification

Let `Lambda_dagger`, `C_dagger`, `q_dagger=b_dagger*Lambda_dagger`, and `t_dagger=b_dagger*C_dagger` be the generalized first, second, source-current, and source-second-current sequences. On a balanced row with `n>=32`,

\[
Y_\dagger=0.
\]

Consequently the usual source-augmented Jordan curvature reduces exactly to

\[
 \boxed{
 \mathcal A_\dagger
 =R_\dagger+Q_\dagger^2,
 }
\]

with no `Y*T` cross term. Likewise the product-source Jordan curvature is simply `Q_dagger^2` on these rows. Any positive generalized Kummer reserve `R_dagger` therefore absorbs the scalar product curvature with coefficient one and leaves the full reserve unused.

This is a scalar-row statement. It does **not** yet prove the complete independent-frequency Hermitian matrix placement; rowwise positivity cannot be substituted for that missing polarization theorem.

## 8. Frontier

This source is proposed as a new simplification of the reflected route, not as an RH proof.

The next exact target is:

```text
construct the complete independent-frequency source-convolved matrix
for B_dagger and prove that the scalar Y_dagger=0 cancellation
polarizes without an untracked boundary/cross term.
```

If that matrix placement succeeds, the source has no cofinal unweighted boundary state and no main-pole return to route.

RH remains unproved.
