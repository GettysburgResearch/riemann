# Independent review of the joint divisor mean

**Reviewer:** signed_conductor_attack, acting independently of the author
joint_divisor_attack. This is an agent mathematical review, not external
peer review or formal verification.

**Date:** 2026-10-10.

**Reviewed object:** [JOINT_DIVISOR_MEAN.md](JOINT_DIVISOR_MEAN.md).
The final content identity is recorded in the freeze section below.

**Verdict:** Sections 1–6 prove the stated joint block estimate and
large-divisor tail improvement, conditional on the exact imported analytic
inputs. Section 7 is correct at the finite coefficient-algebra scope
specified there. This review does not approve a global A2 adapter,
an improved full moment, or a proof of RH.

## 1. Sources and review boundary

I read the complete proposed proof and independently reconstructed its
local algebra, row expansion, joint polynomial, dyadic estimates and
tail comparison. I compared its imported formulas with the mathematical
source of PR #922 at commit
8f2acaacddc10bd8fb053a66070a1d06d25aa922:

- SECOND_REFLECTION_BOOTSTRAP.md, equations (1.1)–(3.5);
- SPECTRAL_ROW_MEAN.md, equations (1.1)–(3.3).

The theta mean remains an imported hypothesis at the stated source
normalization. Its provenance is the October 5 paper2.tex in OpenAI/math
at adc7f1241b42e322a6451854ab7e4b4c146bf78a, Proposition R and
the equation labeled eq:T. The squarefree sextic large sieve remains
the imported Blomer–Goldmakher–Louvel Theorem 1.3. This review checks
the deduction from these statements; it does not reproduce their proofs
or certify their full upstream dependency chains.

For the finite A2 comparison I independently opened the primary papers:

- Chinta–Gunnells, [Constructing Weyl group multiple Dirichlet
  series, arXiv:0803.0691v2](https://arxiv.org/html/0803.0691v2),
  Proposition 2.1 and equations (4.3)–(4.4);
- Chinta–Gunnells, [the A2 paper,
  arXiv:math/0703040v1](https://arxiv.org/html/math/0703040v1),
  equations (1.4), (2.8)–(2.9).

I also checked the local definition of the normalized Gauss coefficient
in the inherited October 5 source: the index 2 coefficient uses the
cubic character obtained by squaring the sextic character. The
additive normalization must match when this is identified with the
papers' cubic Gauss sum.

PR #914 at 0cc0428fedbbfc340044c7451b3d392c1da9a103,
A2_COMPLETION.md, Sections 1–4, is credited by the reviewed note
as the earlier source of the A2 coefficient identification. I did not
replay that complete earlier packet or approve its global analytic
composition. The Section 7 conclusion reviewed here is reconstructed
directly at finite coefficient scope.

No finite computation is used as evidence for an infinite analytic
theorem. The checks below are independent mathematical reconstruction
of the displayed proof, together with source and content-identity reads.

## 2. Exact cube adjustment and row expansion

Write $a=\Re u$ and $b=\Re t$. At a permitted prime, let $z$ be
the completed inner cube variable and $A$ the mixed outer correction
variable, as in (1.4) of the reviewed note. Its equation (1.10) has
the correct direction:

$$
L_{S,kd}=L_{S,k}\prod_{p\mid d}(1-z_p)
\quad\Longrightarrow\quad
G_{k,d}=\frac{\mathcal T_{k,d}}{L_{S,k}}
             \prod_{p\mid d}(1-z_p)^{-1}.
$$

In particular the moving cube mask supplies a reciprocal, not a
numerator. Multiplying the old outer coefficient by its old correction
gives exactly

$$
\kappa a_{\xi_1}\chi_k q^{-u}
   \left(\kappa^{-1}q^{u-t}-c_kq^{1/2-3t}\right)
=a_{\xi_1}\chi_k q^{-t}(1-A).
$$

Consequently (1.8)–(1.9) preserve both the exterior cube ratio and
every moving local factor. The initial region $a>1$, $b>a$ is
adequate for the stated rearrangements. For the subsequent Euler
bounds, $a,b>1/2$ imply $3a-1/2,3b-1/2>1$, so absolute
Euler products dominate every moving omission uniformly in the row.

For the row expansion, put $z=z_0\varepsilon$ and
$A=A_0\varepsilon$, where $\varepsilon=\chi_k(p)^3$.
At permitted primes $\varepsilon^2=1$, and direct multiplication
checks

$$
\frac{1-A_0\varepsilon}{1-z_0\varepsilon}
=1+\frac{z_0(z_0-A_0)}{1-z_0^2}
 +\frac{z_0-A_0}{1-z_0^2}\varepsilon.
$$

The denominator is nonzero on the stated strip. The exponent

$$
r_*=\min(3a-\tfrac12,\,2b+a-\tfrac12)>1
$$

gives absolute summability of the correction indices with a positive
norm weight smaller than $r_*-1$. This justifies the later
Minkowski step uniformly in both imaginary parts. At a deleted
prime the original summand is zero; the proof explicitly avoids
using the false identity $0^2=1$.

The supplementary reciprocity change is permissible only as stated:
partition the rows into finitely many fixed ray classes and absorb
the resulting character into both coefficient families. This preserves
their ratio $\xi_2/\xi_1=\kappa$ and the associated cube factors.

## 3. The joint completed block estimate

I checked both alternatives in (3.1):

$$
\sum_{k\in\mathcal K_Q}|\mathfrak B_{F,X}(k)|^2
\ll (QFX)^\epsilon\|W\|_{C^J}^2
\min\left\{
Q+FX+(QFX)^{2/3},\,
FQ+\frac{Q^2F^2}{X}
\right\}.
$$

The first bound retains the divisor covariance. For a fixed cube
index $b_0$, write $L=X/(Nb_0)^3$. The original normalization
is exactly $1/Nb_0$ times the polynomial normalization
$(FL)^{-1/2}$. The coprime Gauss product is

$$
a_{\xi_1}(d)a_{\xi_2}(m)\chi_m(d)^4
=a_{\xi_1}(dm)\kappa(m).
$$

Thus the squarefree column is $\ell=dm$. The inner divisor
coefficient is independent of the row and is bounded by
$\tau(\ell)\|W\|_\infty$. Its normalized squared mass has
only an arbitrarily small power loss. This is the correct point
at which to apply the imported squarefree row sieve.

The cube-index summation is finite. Weighted Cauchy with the
exact weight $1/Nb_0$ leaves sums with norm powers $-1$,
$-4$ and $-3$ for the three sieve terms, respectively. The
first has only a logarithm and the others converge. Any additional
logarithm from weighted Cauchy is absorbed by the same power loss.

For the actual row-dependent correction, fixing
$r=r_0r_1$ and writing $d=rj$ leaves a single column
$\ell=jm$, an additional fixed column factor
$\chi_\ell(r)^4$, and the bounded external row factors

$$
\chi_k(r)\chi_k(r_1)^3\chi_k(b_0)^3.
$$

The effective scale is $F/Nr$ and the normalization supplies
$(Nr)^{-1/2}$. This yields (3.6). Only after this joint
polynomial estimate does the proof sum the correction indices,
using the absolute convergence established in Section 2.

All masks survive. In particular, there is no introduced
$(m,b_0)=1$ condition; the actual cube restriction
$(b_0,d)=1$ is retained; and after extracting $r$, the
conditions $(r,jmb_0)=1$ and $(j,m)=1$ remain in the
coefficient vector. Such row-independent coefficient restrictions
are allowed by the sieve. Literal row zeros are preserved by
their character factors. No step substitutes an arbitrary
row-dependent coefficient into that sieve.

The bounded-scale convention is sufficient: nonempty terms
have a positive fixed lower bound on the effective column scale;
when $Nr\le 2F$, the outer scale is at least $1/2$.
Enlarging a sieve cutoff by a fixed constant has no asymptotic cost.

For the second alternative, the imported fixed-divisor mean is
$Q+Q^2F/X$. Uniform boundedness of the exact correction
and Minkowski over $O(F)$ divisors, with the normalization
$F^{-1/2}$, give precisely $FQ+Q^2F^2/X$.
The source reference parameter used in the note keeps the
derivative order $J$ fixed. Restricting the permitted rows
to $\mathcal K_Q$ does not increase a nonnegative row mean.

The hypotheses concerning weights are necessary and correctly
stated: the exterior divisor coefficients may be arbitrary bounded
coefficients, but must be independent of the row.

## 4. Dyadic reconstruction and the four terms

The completed dyadic reconstruction is valid initially by the
source identity and continues normally for $a>1/2$ in each
finite row space using the theta bound. The exterior divisor block
is finite. Multiplying its coefficient by $(Nd/F)^{-t}$
does not create a derivative loss in $\Im t$ because the
coefficient is allowed to be arbitrary. Derivatives of
$W_u(y)=y^{-u}W_0(y)$ give the stated polynomial dependence
on $\Im u$.

I independently recomputed the nonnegative minimum decomposition
and all crossover powers. Before the common factor
$F^{1/2-b}$, the relevant dyadic sums are:

| Term under the square root | Crossover in $X$ | Dyadic bound after the factor $X^{1/2-a}$ |
|---|---|---|
| $Q$ | none | $Q^{1/2}$ |
| $\min(FX,FQ)$ | $Q$ | $F^{1/2}Q^{1-a}$ |
| $\min(FX,Q^2F^2/X)$ | $QF^{1/2}$ | $Q^{1-a}F^{1-a/2}$ |
| $\min((QFX)^{2/3},FQ)$ | $(QF)^{1/2}$ | $(QF)^{3/4-a/2}$ |
| $\min((QFX)^{2/3},Q^2F^2/X)$ | $(QF)^{4/5}$ | $(QF)^{1-4a/5}$ |

All crossovers are at least one. The lower geometric sums in
the last two rows require $a<5/6$, and their upper sums
are controlled by $a>1/2$. The linear lower sums require
$a<1$, which is already satisfied. Arbitrarily small initial
power losses can be chosen below every strict strip margin.
The second row is dominated by the third for $F\ge1$.
This gives exactly the four displayed terms in (4.3):

$$
\begin{aligned}
&Q^{1/2}F^{1/2-b}
+Q^{1-a}F^{3/2-b-a/2}\\
&\qquad
+Q^{3/4-a/2}F^{5/4-b-a/2}
+Q^{1-4a/5}F^{3/2-b-4a/5}.
\end{aligned}
$$

There is no endpoint claim at $a=1/2$ or $a=5/6$.
The proof establishes a dyadic estimate, not an unjustified
integral approximation or an exchange of two unproved infinite
expansions.

## 5. Large-divisor tail and the unchanged full-series boundary

Substitution of $b=(3-a)/2+\eta$ gives the four terms

$$
Q^{1/2}F^{a/2-1-\eta},\quad
Q^{1-a}F^{-\eta},\quad
Q^{3/4-a/2}F^{-1/4-\eta},\quad
Q^{1-4a/5}F^{-3a/10-\eta}.
$$

For $F\ge Q^{2/3}$, their ratios to
$Q^{1-a}F^{-\eta}$ are bounded, respectively, by

$$
Q^{4a/3-7/6},\qquad
1,\qquad
Q^{a/2-5/12},\qquad
Q^{a/5}F^{-3a/10}.
$$

Every ratio is at most one on the strict interval
$1/2<a<5/6$. The disjoint blocks
$2^jR\le Nd<2^{j+1}R$ are covered by the permitted
bounded coefficients. Choosing the internal loss smaller than
$\eta$ makes their norm sum convergent. The exterior Euler
ratio is uniformly bounded, as already proved. This establishes
the actual norm limit in (5.3), with all cube and coprimality
masks still present.

The stated overlap with the old normally convergent region
also checks: in the earlier variables
$\tau=\Re v=1+a-b=(3a-1)/2-\eta$, so
$3a-2\tau=1+2\eta>1$. Consequently this is the
tail of the same continued function.

At $a=3/4$, $b=9/8+\eta$, and $R\ge Q^{2/3}$,
the new tail estimate is $Q^{1/4+\epsilon}R^{-\eta+\epsilon}$.
The comparison with the earlier $Q^{1/2+\epsilon}$
tail norm is justified for this specified part of the divisor
series.

The claimed limitation is also correct. Among the four block
terms, the largest exponent of $F$ is
$3/2-b-a/2$. Its differences from the other three
exponents are $1-a/2$, $1/4$, and $3a/10$,
all positive in the stated range. Hence summing this particular
positive bound over all large $F$ still requires
$2b+a>3$. This says nothing about a singularity of the
actual signed function on the boundary. The smaller-divisor
contribution, including $d=1$, remains, and no improved
full-moment exponent follows.

## 6. A2 identification: coefficient scope only

Removing the multiplicative angular, ray and row factors
from the joint squarefree coefficient gives

$$
\gamma_2(d)\gamma_2(m)
  \left(\frac d m\right)_3^2.
$$

For mutually coprime pairs $(d,m)$ and $(d',m')$,
Gauss CRT and cubic reciprocity give the factor

$$
\left(\frac d{d'}\right)_3^2
\left(\frac m{m'}\right)_3^2
\left(\frac d{m'}\right)_3^{-1}
\left(\frac {d'}m\right)_3^{-1}.
$$

This is the cubic A2 twisted multiplicativity with root lengths
normalized as in the general Chinta–Gunnells paper.
The values at $(0,0)$, $(1,0)$ and $(0,1)$ therefore
determine the squarefree coprime coefficient family.

I checked the normalization of the displayed local numerator.
The identities $g(p,p^2)=qg_2(1,p)$,
$g_1(1,p)g_2(1,p)=q$, and
$\gamma_2(p)=q^{-1/2}g_1(1,p)$, with matching
additive convention, give

$$
1+\gamma_2(p)(X+Y)
+q^{1/2}(XY^2+X^2Y)
+q^{1/2}\gamma_2(p)X^2Y^2.
$$

For the A2 Cartan matrix
$C=\begin{pmatrix}2&-1\\-1&2\end{pmatrix}$,

$$
C(1,2)=(0,3),\qquad
C(2,1)=(3,0),\qquad
C(2,2)=(2,2).
$$

Thus the first two insertion vectors have zero cross pairing
modulo three, and the last contributes the common cubic twist
claimed in the note. These statements are finite local algebra.
The A2 paper's global function-field setup is not silently
transferred to the present number-field family.

In particular this review excludes verification of a global
second functional equation for the actual cube-adjusted series.
The archimedean angular data, quadratic part of the sextic
row, all local sections at the growing conductor, full correction
family and uniform estimates would still need their own adapter
and review. Section 7 expressly preserves this boundary, and
Sections 1–6 do not depend on such an adapter.

## 7. Issues reported and freeze

Two minor editorial issues were reported during review:

1. The separator between the divisor coefficient and
   $a_{\xi_1}(d)$ in (3.0) was a comma instead of
   multiplication. The author repaired it.
2. In the A2 paper, equation (2.8) displays the rational function
   with numerator $N$, and equation (2.9) displays the
   numerator itself. I requested that the local-polynomial
   citation expressly include (2.9). The author repaired it to
   cite (1.4), (2.8)–(2.9).

Neither changes the mathematics. No additional mathematical
defect was found in the scope above.

**Content freeze:** the approved source has SHA256
7b42abe2c3c62acfd934b663405821748eac54bb440f1d1071671961a9e97035
and 22,983 bytes. I read the final repaired citation and
independently recomputed this hash. Reverting exactly that citation
change reproduces the fully reviewed predecessor hash
2a41ac0141a9abb23fda7039fa4eafa25759023b8f62dfca492e6ff45e87b72d.
This confirms that the final repair introduced no other difference.
Approval is bound to this content identity and to the conditional
scope stated above; a later commit receipt may bind the same content
to a repository head.

**Smallest load-bearing assertions:** the exact representation
(1.8) and the joint block estimate (3.1), including their masks
and normalizations. Theorem 5.1 depends on both and on the
stated imported inputs. A failure of a future global A2 adapter
would not invalidate this source-conditional deduction.
