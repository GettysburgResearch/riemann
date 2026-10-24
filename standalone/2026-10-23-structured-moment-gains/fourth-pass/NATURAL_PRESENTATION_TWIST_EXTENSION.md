# Moving natural presentations in the Möbius cubic moment

24 October 2026. Proposed source-dependent extension, kept separate from
the already reviewed odd-local-sextic theorem. This note permits canceled
local characters and redundant natural punctures. It does not assert a
new global zero-free boundary.

## 1. Data and statement

Work in the Eisenstein primary-ideal convention of the frozen third-pass
packet at `GettysburgResearch/riemann@f11e86684905c6417683a9f45ac75c223da6a162`.
The input exceptional proof is its `QUANTIFIED_MOBIUS_EXCEPTIONAL_MEAN.md`;
the full-moment assembly is its `FULL_MOBIUS_CUBIC_MOMENT.md`.

The additional exact reflection input is `old-eq:2.1c`--`old-eq:2.1d` in
`openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a`,
`preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex`.
The local source copy is `arithmetic_lane/ope26a_source.tex`, SHA256
`42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3`.
The fixed-angular version uses the source cubic paper's `sections/angular.tex`
with the exact remote source binding in the third-pass `SOURCES.json`.

Let $R$ be squarefree and prime to the fixed omitted set. Let
$\vartheta_R$ be a completely multiplicative natural finite presentation:
at a good prime of $R$ its unit character is a sextic character of any
exponent, including exponent zero, and it vanishes on nonunits there.
Thus $R$ includes both its good primitive conductor and **all** its good
redundant zeros. The ramified data at the fixed omitted primes range over
a fixed finite family. Set

\[
 \theta_R=\Theta_\ell\nu\vartheta_R,
\]

where the angular order $\ell$ and the initial ray data $\nu$ are fixed.
The entire presentation $R,\theta_R$ is common to a given row mean. It
may vary with the lengths. No row-dependent extra mask is allowed outside
this specified natural product.

For the two exceptional configurations and the notation of the frozen
quantitative appendix, assume

\[
 NR\le Y^{7/10},\qquad 1+|u|\le Y^{1/100},\qquad
 Nv,Ne\le Y^\delta,\qquad \delta=10^{-9}.
\]

The $p,q$ are coprime squarefree rows whose norm exponents lie in the
same $\delta$-neighborhoods of $(1,0)$ or $(1/3,1/3)$. Then

\[
 \sum_{p,q}\left|
   \sum_{(b,e)=1}\mu(b)\theta_R(b)W(Nb/Y)(Nb)^{iu}
                      \chi_b(vpq^2)
 \right|^2
 \ll Y^{7/3-10^{-6}}.                                    \tag{1}
\]

The constant is uniform in $R$ and its allowed finite presentation.
As for the frozen exceptional estimate, (1) uses no zero-free hypothesis.

## 2. Separate the principal inducing rows first

For a row $p,q$, write $\psi^0_{p,q}$ for the complete natural character
in the full smooth factor, including the $e$ puncture. Its primitive
inducing character is denoted $\psi^*_{p,q}$. The norm twist is kept in
the smooth profile, not in this notation.

If $\ell\ne0$, $\psi^*_{p,q}$ is not principal. If $\ell=0$ and it is
principal, every prime of $pq$ outside the fixed omitted set must divide
$Rv$: outside that union the corresponding local cubic character is
nontrivial. Since $p,q$ are squarefree and coprime, the number of such
pairs is at most

\[
 3^{\omega(R\operatorname{rad}v)}\ll_\epsilon Y^\epsilon.
\]

This upper bound is sufficient; no uniqueness assertion is needed.
Each original Möbius polynomial has absolute value $O(Y)$ up to the
fixed weight bound, uniformly in its norm height. The total contribution
of these rows to the left side of (1) is therefore
$O(Y^{2+\epsilon})$. Remove them before applying the Möbius identity or
any full-factor functional equation. In particular, no principal polar
term is omitted from a reflected full smooth factor.

## 3. Natural reflection preserves the common coefficient

Fix one of the remaining rows. Let $Q$ be its primitive conductor norm
and let $R_0$ be the radical of its redundant natural zeros, disjoint
from that primitive conductor. At every good prime, tameness gives
exactly one of these two possibilities. Thus

\[
 Q\,NR_0\ll N(Rvpqe),                                    \tag{2}
\]

with only a fixed factor at the omitted primes. In (2), taking radicals
on the right would only improve the inequality. Cancellation of a local
character transfers its prime from the conductor to $R_0$; it does not
make the prime disappear from the budget.

Let $F^0(s)$ be the natural Dirichlet series and put

\[
 E(s)=\prod_{\mathfrak p\mid R_0}
           (1-\psi^*(\mathfrak p)(N\mathfrak p)^{-s}).
\]

Then $F^0(s)=L(s,\psi^*)E(s)$. The primitive functional equation gives
the exact natural functional equation

\[
 F^0(s)=\varepsilon Q^{1/2-s}\mathcal G_\ell(s)
       \frac{E(s)}{\overline E(1-s)}
       \overline F^{,0}(1-s),                             \tag{3}
\]

up to the fixed field scale; $\overline E$ and
$\overline F^{,0}$ mean conjugation of the arithmetic coefficients.
Here $|\varepsilon|=1$, and the fixed-angular gamma quotient
$\mathcal G_\ell$ has modulus one on $\Re s=1/2$. The dual series in
(3) has exactly the character $\overline{\psi^0}$, including all its
original zeros. Its coefficient twist $\overline{\theta_R}$ is common
to every row; the $v,e$ factors are also common.

On the symmetry line,

\[
 \left|\frac{E(s)}{\overline E(1-s)}\right|
 \le \prod_{\mathfrak p\mid R_0}
        \frac{1+(N\mathfrak p)^{-1/2}}
             {1-(N\mathfrak p)^{-1/2}}
 \ll_\epsilon Y^\epsilon.                                \tag{4}
\]

The constant is uniform in the radical. The elementary last estimate
follows by bounding each sufficiently large prime factor by an
arbitrarily small prescribed power of its norm, and absorbing the
finitely many remaining primes into the constant.

Equivalently, the exact centered reflection from `old-eq:2.1d` is

\[
 T_{\psi^0}(Z;W)
 =\varepsilon
  \sum_{\substack{d\mid R_0\\\operatorname{rad}(h)\mid R_0}}
  \frac{\mu(d)\psi^*(d)\overline{\psi^*(h)}}{\sqrt{Nd\,Nh}}
  T_{\overline{\psi^0}}
       \left(\frac{C\,Nd}{Z\,Nh};W^\sharp\right),           \tag{5}
\]

where $C$ is a fixed field constant times $Q$. The total absolute
coefficient mass in (5) is bounded by the product in (4). Row-dependent
eligibility of $d,h$ is part of this identity; it is not replaced by
an unmasked character. Formula (3) permits keeping their sum as one
bounded row multiplier instead of partitioning those eligibility sets.

### Dual cutoff, height, and common norm shifts

Apply Mellin inversion to a full factor of length $Z$ and norm height
$u$. On a far-left line the dual series is absolutely convergent.
Expansion of the Euler quotient gives the $d,h$ factors in (5).
Its largest scale is bounded by

\[
 \frac{Q\,NR_0}{Z}\le \frac{N(Rvpqe)}{Z}.
\]

The usual gamma estimate gives the same height enlargement as in the
source's full-smooth-sum lemma. Consequently the dual norm dyads may be
truncated uniformly at

\[
 J\ll Y^\epsilon\frac{N(Rvpqe)(1+|u|)^2}{Z}.               \tag{6}
\]

One can first use this common largest cutoff on the far-left line and
then move the retained finite dyads to $\Re s=1/2$. The far-left tail
has arbitrary power decay; (2), (4), and the $d,h$ expansion give
uniformity in the natural presentation. If the $h$ expansion itself
is truncated, Rankin's bound with any fixed exponent below $1/2$
gives an arbitrarily small tail after a sufficiently large polynomial
cutoff. There is no unbounded enumeration cost.

On the symmetry line each retained dyad has amplitude
$Y^\epsilon\sqrt{Z/J}$. Root numbers, conductor phases, and the Euler
quotient are rowwise scalar multipliers, bounded as in (4). Its norm
shifts are integrated against the common rapidly decreasing Mellin
majorant from the source full-sum proof. The gamma quotient is of
modulus one there, including for the fixed angular order. Translation
by $u$ does not increase that majorant's $L^1$ mass. Thus this argument
does not pay an unspecified polynomial in the allowed height in the
finite exponent budget.

The reflected polynomial is the common-coefficient family
$\overline{\theta_R}(n)\overline{\chi_n(vpq^2)}1_{(n,e)=1}$.
It is therefore a legitimate input to the same unrestricted-inner
cubic sieve as in the frozen quantitative proof. If the alternative
scale-supremum formulation of (5) is used, the source's logarithmic
scale boxes and Euler derivatives give the same arbitrarily small
power cost.

## 4. Complete the exceptional estimate

The exact identity $\mu=2m-m*m*1$ on the original annulus commutes
with $\theta_R$, including its zeros. The principal rows have already
been removed. Truncate the common Mellin shifts at $Y^{1/100}$;
the total full-factor height is at most $Y^{1/50}$ for large $Y$.
The new radical and height budget in (6) is

\[
 Y^{7/10}(Y^{1/50})^2=Y^{37/50}=Y^{.74}.                    \tag{7}
\]

The remaining $v,e$ and endpoint costs are the original $O(\delta)$
costs. The Euler quotient in (4), dyadic sums, and source sieve losses
can all be assigned arbitrarily small powers within the frozen
$10^{-4}$ total error budget. Hence the dominant-full-factor bounds
with cutoff $a_3\ge9/10$ are unchanged: their exponents are at most
$349/150+10^{-4}$ and $341/150+10^{-4}$ at the two endpoints.

For the other configurations all ordinary and cubic sieves put the
entire $\theta_R$ in their common coefficient vector. Complete
multiplicativity ensures that copied products still have a single
common $\theta_R(n)$ times divisor-bounded coefficients.
For the Gram step take the full ambient primary-ideal Hilbert space
and the row vectors $W(Nn/Z)^{1/2}\chi_p(n)$. Put the natural zeros
in the coefficient vector. Its squared norm is at most $Z^{1+\epsilon}$,
and the Gram kernel is precisely the source's unmasked kernel.
Thus no growing mask is introduced into that kernel and no masked
Gram monotonicity is asserted.

The finite repetition argument (at most 29 copies) and all its strict
numerical gaps now apply unchanged. Together with the negligible
principal-row contribution, this proves (1).

## 5. Full-moment and rectangular consequences

Under the explicit all-finite-character `ZF_beta` hypothesis of the
frozen full-moment theorem, the same assembly gives some
$\eta_{\rm nat}>0$, uniform in the natural presentation, such that

\[
 J_R(A,B)=\sum_aW(a/\sqrt A)
  \left|\sum_b\frac{\mu(b)\theta_R(b)G(b)}{\sqrt{Nb}}
                   \overline{\chi_b(a)}V(Nb/B)\right|^2
 \ll(AB)^\epsilon\{A+(AB)^{2/3-\eta_{\rm nat}}\}            \tag{8}
\]

for $A\ge B\ge2$ and $NR\le B^{2/3}$. Here the effective moving
quantity is the **whole presentation radical**, not just the
primitive conductor. No numerical value of the full-moment saving
$\eta_{\rm nat}$ is asserted.

The parameter handoff is the one explicitly checked in
`cubic_review_lane/pass4/MOVING_SEXTIC_TWIST_EXTENSION.md` (SHA256
`b43ee0452b171420aad77f5dc345c65b12ada1a269c8228ea9bebf95c804ee23`),
with $NR$ in place of $Nt$. In its exceptional blocks $Y=B/(FL)$ and
$Y\ge X^c$, with $c=1/4$ available, so

\[
 NR\le Y^{2/3+4\delta_{\rm out}/(3c)}<Y^{7/10},\qquad
 Nv\le Y^{4\delta_{\rm out}/c},\qquad
 Ne\ll Y^{\rho+(7\delta_{\rm out}+2\delta')/(3c)}.
\]

Choose $\rho\le\delta_{\rm exc}/10$,
$\delta_{\rm out}\le c\delta_{\rm exc}/100$, and
$\delta'\le\delta_{\rm out}/100$, also respecting the earlier
$\beta$-dependent choices. The small-conductor reciprocal bounds
include all finite twists and all natural deleted factors; their
arbitrarily small conductor and radical powers are absorbed in
$(AB)^\epsilon$. The generic large-conductor estimates already allow
these common divisor-bounded coefficients. Only (1) is the new
exceptional input needed for (8).

The exact cubic amplification identity also commutes with this natural
presentation and its zeros. Consequently, for $1\le A\le B$ and
$C\asymp(B/A)^{1/3}$, the sufficient restriction

\[
 NR\le(B/C)^{2/3}
\]

gives

\[
 J_R(A,B)\ll(AB)^\epsilon
       \{A^{1/3}B^{2/3}+A^{1/3}B^{1-2\eta_{\rm nat}}\}.
                                                               \tag{9}
\]

All additional moving punctures must be charged to $R$ or to the
explicitly small $e$ data. These statements do not cover a different
twist at every live row, arbitrary detected-class indicators, or an
unbounded angular order. A prime-amplified fourth-moment or global
zero-free consumer still requires its own complete signed assembly.
