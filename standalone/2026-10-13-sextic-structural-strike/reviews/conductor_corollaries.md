# Scoped review of the conductor corollaries

**Reviewed file:** `pass3_bilinear_corollaries.md`, 8,872 bytes, SHA-256

`49d471154fbfb2b8589742a70343f9abfa8e407172648b73f33a14d5f3e3031d`.

**Main input reviewed separately:**
`CONJUGATE_PAIR_CONDUCTOR_SIEVE.md`, SHA-256
`220d767a03ed6c61b8e5a3ea34b48a0a2adae92607047fbfa0bb96e5be876ef2`.
See `pass3_bilinear_review_extraction.md` and its updated hash binding.

**Scope:** independent reconstruction of Sections 1--3. I did not
develop these corollaries. I read the final Section 4 for its stated
limitations but did not attempt to construct or rule out every possible
multiple-reflection method mentioned there. No linear-programming
output is treated as proof.

**Verdict:** Sections 1--3 pass this source-qualified check. No required
correction found. The conductor-size bound covers the stated conjugate
local types; the exponent \(11/8\) is an optimum of the displayed
inequalities, not an arithmetic lower bound on a moment.

## 1. The conductor-ordered sum

With bounded background conductor, every ratio in the main proof's
general-order equation (4.6) is bounded uniformly over \(A,B\geq1\).
For the last ratio, use \(N_0\geq M\) to obtain

\[
M^{7/(2n)-1}N_0^{-1/(2n)}\leq M^{3/n-1}\leq1
\qquad(n\geq3).
\]

The dyadic bound is therefore \((AB)^{1+\eta}\) times the fixed
vertical polynomial. The boxes meeting \(N(ab)\leq X\) have
\(AB\ll X\). Since
\(\sum_{2^{j+\ell}\ll X}2^{j+\ell}\ll X\log(2X)\), summing
them with a smaller preliminary loss proves (1.1).

The background's finitely many fixed conductor primes can be included
in the initial bad set. If one starts with an index set that includes
them, there are only finitely many choices of their presence in the
two squarefree coprime labels. Factoring out those choices and absorbing
their character powers in the fixed background gives the same result.
An unbounded moving set could not be handled this way; the statement
does not attempt that.

After this fixed local adjustment, the good conductor is precisely
\(ab\). Thus the theorem is ordered by conductor, and does not
mistake the larger ideal norm \(N(a b^{n-1})\) for conductor norm.

## 2. Which local types are covered

At a good prime, the standard residue character has order \(n\).
Its \(j\)-th power has exact order \(n\) if and only if
\((j,n)=1\). For \(n=3,4,6\), those exponents are exactly
\(1,n-1\). Partitioning the ramified primes into these two types
therefore gives the required squarefree coprime labels \(a,b\).
The fixed bad-prime data and any bounded unramified ambiguity give
only a finite family of twists.

This proves the asserted coverage in the standard family, including
the fully sextic local type over the Eisenstein field. It does not
cover a general sextic character made from local components of order
two or three, even if the global character has order six. The
manuscript explicitly preserves that distinction.

The consequence for disjoint singleton primes is accurate: their
good local exponents are \(\pm1\), so this family is covered. The
native accounting argument still loses its long-singleton factor
after absolute values. A sharp family mean alone is not claimed to
remove it.

## 3. Three estimates for the same five-label mean

For the squarefree coprime labels \(q_1,\ldots,q_5\), every
nonzero local exponent remains ramified. Thus the moving good
conductor of the frozen background is exactly the product of the
three other labels for either pair method. Counting those background
labels turns the pair mean's prefactor into \(P\), with the ratio
shown in (2.2) or (2.3). The coprimality restrictions can only
decrease these positive means.

The characters from the original sixth-order family raised to powers
two and three give, respectively, the cubic and quadratic families
after the fixed ray data are specified. This family reduction is also
stated in the primary source's Section 9. The quadratic sieve at row
length \(Q_3\) and AFE length \(P^{1/2}\) gives the ratio
\(1+P^{1/2}/Q_3=1+(R_2/Q_3)^{1/2}\), as in (2.4). Its squarefree
index reduction and primitive bad-prime convention are the same
ones already reviewed for the main proof.

I directly checked the primary source:
[de Faveri, arXiv:2610.04045v1, Section 9](https://arxiv.org/html/2610.04045v1).
It supplies the stated weighted-box objective, the exponent
\((3n-7)/(2(n-2))\), and the single-label estimate used for the
matching upper bound. At \(n=6\), that exponent is \(11/8\).
The corollary does not import a zero-density or asymptotic-moment
consequence that would require additional hypotheses elsewhere in
the primary paper.

## 4. The exact bound-envelope optimum

At \(Q_i=X\) for every label, \(P=X^5\) and both pair backgrounds
have scale \(X^3\). Direct substitution gives the ratios

\[
\begin{array}{c|c}
\text{branch}&\text{ratios}\\ \hline
\text{sextic pair}&1,\ X^{-1/6},\ X^{3/2},\ X^{1/4}\\
\text{cubic pair}&1,\ X^{3/2},\ X^{2/3}\\
\text{quadratic label}&1,\ X^{3/2}
\end{array}
\]

Every single-label branch also contains the AFE length ratio
\(P^{1/2}/Q_j=X^{3/2}\). Thus the displayed complete right-hand
sides all have exponent at least \(5+3/2=13/2\) in this box.
Taking their minimum or geometric means cannot reduce that exponent.
The desired weighted right-hand side has exponent \(1+4\alpha\),
forcing \(\alpha\geq11/8\) for this particular collection of
bounds. No assertion about the actual size of \(\mathcal M\) follows
from this calculation.

For the matching upper bound, put \(R=Q_2Q_3Q_4Q_5\) and let
\(T=\max_iQ_i\). Then \(T\geq Q_1\) and \(T\geq R^{1/4}\).
In particular \(T\geq Q_1^{1/2}R^{1/8}\), so

\[
P^{1/2}/T\leq R^{3/8},\qquad P/T\leq R.
\]

Substitution in the source's single-label bound yields

\[
\mathcal M\ll P^{1+\eta}(1+R^{3/8}+R^{1/3})
\ll Q_1^{1+\epsilon}R^{11/8+\epsilon}.
\]

This is a direct matching proof; no numerical optimization is needed.
The balanced example limits the displayed upper-bound methods and
does not exclude a stronger estimate exploiting more than two
conductor labels together.

## 5. Review boundary

The result is a valid deduction from the reviewed pair theorem and
the named external sieve inputs. This review does not certify the
external foundations afresh, establish external novelty, or claim a
native diagonal moment. It also does not turn the exponent-envelope
obstruction into a lower bound for the actual arithmetic mean. The
separate fully sextic and mixed-local-type scopes should remain
explicit in any summary.
