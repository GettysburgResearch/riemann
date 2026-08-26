# L-106132 — The Boolean balanced source is an exact half-source square with a least-prime Calderón row

Claim ID: `L-106132`  
Programme aliases: `LFAM1.BOOLEAN_HALF_SOURCE`, `LFAM2.LEAST_PRIME_CUTOFF_DIFFERENCE`, `STRESS.PRIME_FILTRATION_CALDERON_ROW`  
Status: **PROVED EXACT FINITE-EULER SOURCE FACTORIZATION**  
Created: 2026-08-25  
Depends on: `L-106080`; parent `L-102951--L-102954`; Boolean disjoint-support convolution  
Programme issues: #743, #736, #737  
RH status: **not assumed**

`R-106131` shows that a positive square of every least-prime conductor fibre
charges a conductor-dimensional atomic trace. The Boolean source itself does
not arrive as such a positive sum. It has an exact signed half-source
factorization which assembles the prime filtration before any physical square
is taken.

This lemma records that structure.

## 1. Exact Boolean square root of Möbius

On the finite squarefree Boolean algebra, let `star` denote disjoint-support
convolution. Define

\[
\boxed{
 h(S)=\left(-\frac12\right)^{|S|}.
}
\tag{L-106132.1}
\]

Primewise,

\[
(1-\tfrac12x_p)\star(1-\tfrac12x_p)=1-x_p
\]

because `x_p star x_p=0` in the squarefree algebra. Tensoring over the finite
prime set gives

\[
\boxed{
 h\star h=\mu_{\rm sf}.
}
\tag{L-106132.2}
\]

Let

\[
a_U=\varepsilon-\mu_U\star\mathbf1_{\rm sf}
\]

be the Boolean Vaughan defect and put

\[
\boxed{
 f_U=a_U\star h.
}
\tag{L-106132.3}
\]

The balanced Boolean coefficient is

\[
b_U=a_U\star a_U\star\mu_{\rm sf},
\]

so (L-106132.2) gives the exact square

\[
\boxed{
 b_U=f_U\star f_U.
}
\tag{L-106132.4}
\]

No analytic continuation or quotient by repeated primes is used: this is an
identity in the literal finite squarefree source algebra.

Because `a_U(S)=0` whenever `prod(S)<=U`, the same is true of `f_U`:

\[
\boxed{
 f_U(S)=0
 \qquad
 \bigl(\prod_{p\in S}p\le U\bigr).
}
\tag{L-106132.5}
\]

Thus both factors in (L-106132.4) are genuinely beyond the Vaughan cutoff.

## 2. Exact cutoff recurrence at the least prime

Fix a prime `ell` and restrict all remaining labels to primes larger than
`ell`. Write

\[
F_{U,>\ell}
=
\operatorname{Res}_{>\ell}f_U.
\]

For a squarefree tail `u` supported on primes larger than `ell`, the Boolean
defect satisfies

\[
\boxed{
 a_U(\ell u)
 =
 a_U(u)-a_{U/\ell}(u).
}
\tag{L-106132.6}
\]

Indeed, divisors of `ell u` split uniquely into divisors of `u` and `ell`
times divisors of `u`; the two cutoff conditions are `d<=U` and
`d<=U/ell`.

The local half-source coefficient of `ell` is `-1/2`. Convolving
(L-106132.6) with the tail half-source therefore gives

\[
\boxed{
 f_U(\ell u)
 =
 \frac12F_{U,>\ell}(u)
 -
 F_{U/\ell,>\ell}(u).
}
\tag{L-106132.7}
\]

This is an exact cutoff difference, not an estimate.

## 3. Least-prime row of the balanced source

Every nonempty squarefree support has one least prime. Since
`b_U=f_U star f_U`, the label `ell` occurs in exactly one of the two half-source
factors. Combining (L-106132.4) and (L-106132.7),

\[
\boxed{
\begin{aligned}
b_U(\ell u)
={}&
F_{U,>\ell}\star F_{U,>\ell}(u)\\
&-2F_{U,>\ell}\star F_{U/\ell,>\ell}(u).
\end{aligned}
}
\tag{L-106132.8}
\]

Equivalently,

\[
\boxed{
b_U(\ell u)
=
\bigl(F_{U,>\ell}-F_{U/\ell,>\ell}\bigr)^{\star2}(u)
-
F_{U/\ell,>\ell}^{\star2}(u).
}
\tag{L-106132.9}
\]

Thus the least-prime conductor row is a signed difference of two Boolean
squares.

Since `b_U(1)=0`, the complete balanced source is the disjoint linear sum

\[
\boxed{
b_U
=
\sum_\ell
x_\ell
\left[
F_{U,>\ell}^{\star2}
-2F_{U,>\ell}\star F_{U/\ell,>\ell}
\right],
}
\tag{L-106132.10}
\]

where each nonempty source support occurs exactly once, at its least prime.

## 4. Source multiplicity

All coefficients in (L-106132.1)--(L-106132.10) are finite divisor sums. On a
physical horizon their representation multiplicities are bounded by
`C^omega(n)=n^o(1)` for a fixed absolute `C`. The half-source transformation
therefore introduces no positive power cost in the existing finite carrier,
shell or marked-prime ledger.

This statement concerns labelled source multiplicity only. It does not
declare different least-prime rows orthogonal after physical observation.

## 5. Meaning for the family repair

The first bilateral family frontier treated each least-prime row as a positive
conductor fibre and then squared it. Equations (L-106132.8)--(L-106132.10)
show the source-faithful alternative:

```text
least-prime source row
  =
same-scale half-source square
  MINUS
cross-scale half-source product.
```

The negative cross-scale term is lost by a fibrewise positive moment. It is
precisely the kind of signed inter-conductor transport which can cancel the
atomic conductor dimension of `R-106131`.

Accordingly, the repaired conclusion programme must keep either:

```text
the Wick-centered additive/Kummer identity of L-106131;
or
the signed half-source cutoff difference of this lemma;
```

until after the complete conductor sum. It may not replace both by a positive
sum of conductor-fibre squares.

## Scope

The lemma proves the exact half-source factorization and prime-filtration
cutoff recurrence. It does not estimate the physical image of
(L-106132.10), prove either gate of `T-106140`, prove `BCI102990`, or prove RH.
