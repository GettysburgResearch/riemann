# L-105462 — The equal-pair source is an F1 configuration square and ordinary multiplication adds only diagonal contractions

Claim ID: `L-105462`

Status: **PROVED EXACT CONFIGURATION-SPACE/WICK FACTORIZATION**

Use the prime-box Chow algebra of `L-105460`.  Let \(\Pi\) be the singleton
owner class,

\[
\Pi(\{p\})=x_p,
\qquad
\Pi(S)=0\quad(|S|\ne1),
\]

and let \(T_\theta\) multiply a degree-\(j\) core class by \(\theta^j\).
For the Boolean half-core \(\mathfrak f_U\), put

\[
\boxed{
\mathfrak G_{U,\theta}
 =
 \Pi\star T_\theta\mathfrak f_U.
}
\tag{L-105462.1}
\]

Every atom has the unique physical shape

\[
n=pa^2,\qquad (p,a)=1.
\tag{L-105462.2}
\]

The squarefree kernel of \(n\) is \(p\), so \((p,a)\mapsto pa^2\) is
injective.

## 1. The exact configuration square

By `L-105461.5`, the canonical equal-pair source is

\[
\boxed{
\mathfrak B_U^{\rm eq}
 =
 \int_0^1(1-\theta)
 \mathfrak G_{U,\theta}^2\,d\theta
}
\tag{L-105462.3}
\]

inside the Chow algebra.  The integral is finite algebraic notation for the
rational coefficient \(1/\binom{k}{2}\) on depth \(k\).

Because \(h_p^2=0\), (L-105462.3) is the square on the open two-point
configuration space of disjoint prime-label supports.  It is already Wick
normal ordered.

## 2. Physical Wick realization

Let

\[
F_{U,\theta}
 =
 \mathcal O_A[\mathfrak G_{U,\theta}]
\]

be the positive ratio-four half-field.  The physical image of
(L-105462.3) is

\[
\boxed{
\mathcal J_U^\diamond
 =
 \int_0^1(1-\theta)
 (F_{U,\theta}\diamond_MF_{U,\theta})\,d\theta.
}
\tag{L-105462.4}
\]

This is coefficient-exact.

## 3. Ordinary compactification and the diagonal ideal

The ordinary Mellin square is

\[
\mathcal J_U
 =
 \int_0^1(1-\theta)
 (F_{U,\theta}*_MF_{U,\theta})\,d\theta.
\]

Partition every ordered pair of half-source atoms according to whether their
literal prime-label supports are disjoint.  This gives

\[
\boxed{
\mathcal J_U
 =
 \mathcal J_U^\diamond+\mathcal C_U,
}
\tag{L-105462.5}
\]

where \(\mathcal C_U\) is supported on the diagonal incidence locus.

Every shared label has one of the following physical exponents:

```text
owner / owner     1+1 = 2;
owner / core      1+2 = 3;
core / core       2+2 = 4.
```

If several labels are shared, at least one such exponent is present.
Therefore every atom of \(\mathcal C_U\) belongs to the repeated-label or
higher-prime-power ledger.

The frozen `T-102990` source closures imply, for the fixed derivative/outer
observation,

\[
\int\left|
\mathcal D_{\rm out}\mathcal C_U
\right|\,dX/X
 =
 Y^{o(1)}.
\tag{L-105462.6}
\]

No diagonal term is declared zero before observation; it is moved with its
literal coefficient into the inherited closed ledger.

## F1 interpretation

Equation (L-105462.5) is the boundary decomposition

```text
ordinary two-copy product
  =
open F1 configuration square
  +
prime-divisor diagonal strata.
```

Thus the F1 source square is exact.  The remaining theorem concerns the
physical trace of the open configuration class, equivalently the ordinary
square modulo the explicitly closed diagonal strata.
