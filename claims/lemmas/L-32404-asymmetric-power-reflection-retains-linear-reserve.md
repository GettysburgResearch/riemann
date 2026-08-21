# L-32404 — Asymmetric power reflection retains a linear Selberg reserve

Claim ID: `L-32404`  
Title: Subtracting normalized powered individual Selberg identities from the unpowered reflected product isolates the Hermitian cross term plus a surviving positive-coefficient linear forcing  
Status: **PROPOSED COMPLETE EXACT ALGEBRAIC LEMMA — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-08  
Dependencies: `L-32402`, `R-32401`; PR #241 reflected generalized Selberg identity  
Scope: exact coefficient polarization and carry-row reserve; the sign of the surviving linear term after physical independent-frequency localization remains open

## 1. Notation

Let `A_+` and `A_-` be the two reflected zeta factors

\[
 A_+(s)=\zeta(s+it),
 \qquad
 A_-(s)=\zeta(s-iu),
\]

with generalized von Mangoldt sequences `Lambda_+` and `Lambda_-`.

For any Dirichlet series `A`, write

\[
\boxed{
 \mathcal C[A]
 =\Lambda_A\log+\Lambda_A*\Lambda_A
}
\tag{L-32404.1}
\]

for the generalized Selberg forcing sequence `b*(a log^2)`.

The product satisfies

\[
 \Lambda_{A_+A_-}=\Lambda_++\Lambda_-.
\]

## 2. Asymmetric polarization

Fix an integer `M>=2`. The product identity is left at power one, while each individual reflected factor is powered to `M` and normalized by `M^2`.

One has

\[
\begin{aligned}
 \mathcal C[A_+A_-]
 ={}&(\Lambda_++\Lambda_-)\log\\
 &+(\Lambda_++\Lambda_-)*(\Lambda_++\Lambda_-),
\end{aligned}
\tag{L-32404.2}
\]

and

\[
 {1\over M^2}\mathcal C[A_+^M]
 ={1\over M}\Lambda_+\log+\Lambda_+*\Lambda_+,
\tag{L-32404.3}
\]

with the analogous identity for `A_-`.

Subtracting (L-32404.3) and its reflected copy from (L-32404.2) cancels the two analytic self-squares but **does not** cancel the complete linear forcing. Exactly,

\[
\boxed{
\begin{aligned}
 &\mathcal C[A_+A_-]
 -{1\over M^2}\mathcal C[A_+^M]
 -{1\over M^2}\mathcal C[A_-^M]\\
 &\qquad=
 2\Lambda_+*\Lambda_-
 +\left(1-{1\over M}\right)
  (\Lambda_++\Lambda_-)\log.
\end{aligned}}
\tag{L-32404.4}
\]

This is an exact coefficient identity for independent reflected frequencies `t,u`.

It differs essentially from the standard power reflection in `R-32401`: there the product is also powered to `M`, and the linear term cancels. Here the mismatch of powers leaves a controlled linear reserve.

## 3. Diagonal vertical form

On a real vertical line set `u=t`. If

\[
 H(s)=-{\zeta'\over\zeta}(s)
\]

and

\[
 L(s)=\sum_n{\Lambda(n)\log n\over n^s}=-H'(s),
\]

then the Dirichlet-series value of the right side of (L-32404.4) is

\[
\boxed{
 2|H(\sigma+it)|^2
 +2\left(1-{1\over M}\right)
   \operatorname{Re}L(\sigma+it).
}
\tag{L-32404.5}
\]

Thus the surviving term is linear and explicit. It is not asserted pointwise nonnegative in `t`.

## 4. Untwisted carry-row consequence

At `t=u=0`, use the ordinary row notation of `L-32402`:

\[
 F=\log\binom nj,
 \qquad
 A=\sum_d\Lambda(d)\log d\,\chi_{n,d}(j),
 \qquad
 B=\sum_d(\Lambda*\Lambda)(d)\chi_{n,d}(j).
\]

The normalized right side of (L-32404.4), divided by two, has row forcing

\[
\boxed{
 B+\left(1-{1\over M}\right)A.
}
\tag{L-32404.6]
\]

Since `L-29002` gives `F^2>=A+B`,

\[
\begin{aligned}
 F^2-\left[B+\left(1-{1\over M}\right)A\right]
 &=Q+{A\over M}.
\end{aligned}
\]

Therefore

\[
\boxed{
 F^2-\left[B+\left(1-{1\over M}\right)A\right]
 =Q+{A\over M}\ge0.
}
\tag{L-32404.7]

For every nontrivial split, `A>0`, so

\[
\boxed{
 F^2>B+\left(1-{1\over M}\right)A.
}
\tag{L-32404.8]

This includes the endpoint neighbors where the ordinary reserve `Q` vanishes. At an endpoint row the exact surviving reserve is simply `A/M>0`.

Thus the asymmetric reflected algebra keeps precisely the type of linear forcing that can see the root/two-contact channel of `L-32401`.

## 5. Why this is not yet a physical proof

The physical independent-frequency block does not evaluate only the untwisted row. In (L-32404.5),

\[
 \operatorname{Re}L(\sigma+it)
\]

has no pointwise sign. Therefore the following inference is **not** made:

```text
strict untwisted carry-row reserve
    =>
strict positive physical Hermitian block.
```

A valid completion must keep the linear term through the complete two-frequency localization and prove one of the following:

1. it becomes a nonnegative source-bound boundary form after exact recombination;
2. it is an exact derivative/commutator whose boundary is polylogarithmic;
3. it combines with the two-contact endpoint reserve of `L-32403` into a positive Schur complement.

Taking its absolute value would lose the new reserve and return to an overstrong source norm.

## 6. Proof boundary

Closed exactly:

- the asymmetric reflected identity (L-32404.4);
- cancellation of analytic self-squares;
- survival of the coefficient `(1-1/M)` linear forcing;
- the strict untwisted carry-row reserve `Q+A/M`.

Open:

- the source-bound sign or boundary representation of the linear term after physical localization;
- the resulting root-polarized Schur complement;
- RH.
