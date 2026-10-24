# Pricing the resonant angular case in the sextic μγ₂ moment

24 October 2026. Proposed source-dependent companion theorem, submitted
for independent review. The nonresonant theorem remains unchanged.
This note proves the remaining fixed angular case with an explicit
additional term. It uses no zero-free hypothesis and asserts no global
zero-free improvement.

## 1. Parent theorem and statement

Use the data, exact additive normalization, all original zero
extensions, and definitions of `SEXTIC_ROW_PHASE_CANCELLATION.md`,
SHA256
`e9e93c049e735905bef2a9a02e56453c74fd0952ce8ca7bb4d9e224e1e991304`.
Its source inputs are the pinned squarefree sextic sieve, ordinary
Hecke functional equation, fixed-angular gamma quotient, and natural
reflection. This companion does not assume any of its conclusions at
the excluded angular type.

In particular θ(n)=α(n)^ℓν(n), with fixed finite ray data ν and fixed
integer ℓ; fixed finite linear combinations at the same angular type
are permitted. For all A,B≥1, define the parent moment

\[
 J_{6,\theta}(A,B)=\frac1B\sum_{a\equiv1\ (3)}W(a/\sqrt A)
 \left|\sum_n\mu(n)\theta(n)\gamma_2(n)
                         V(Nn/B)\chi_n(a)\right|^2.
 \tag{1}
\]

**Theorem.** For every fixed ℓ and every ε>0,

\[
 \boxed{J_{6,\theta}(A,B)\ll(AB)^\epsilon
 \left\{A+B+\mathbf1_{\ell=-1}A^{5/6}B^{1/3}\right\}.}
 \tag{2}
\]

The constants and test uniformity are as in the parent theorem.
The bound need not be sharp in every length range. The additional term
is an upper bound for the explicitly identified principal-character
frequency set, not an unproved spectral subtraction.

For ℓ≠−1, (2) is the parent theorem. Suppose henceforth ℓ=−1, so
the post-Poisson ordinary angular type is zero.

## 2. Remove principal inducing rows before reflection

The parent's exact first Poisson, common-divisor extraction, and
coprimality inversion apply without an angular restriction. Their
notation is

\[
 F=Nf,\quad M=Nm,\quad L=Nl,\quad m\mid f,\quad(f,l)=1,
 \qquad v=f^2m^5,
\]

\[
 K_0=B^2/A,\qquad K_{fm}=K_0 M/F^2,\qquad Y=B/(FL).
 \tag{3}
\]

The external absolute weight is A/(9BML), the row mask is (k,l)=1,
and the ordinary squarefree column has coefficient
μ²(n)α(n)G(n)θ(n), with puncture (n,fl)=1 and character
overline(χ_n(vk)). The exact finite pair phase ρ(n₁,n₂) is unchanged.

Expand G and ρ in their fixed finite ray character bases. For each
resulting ordinary column the natural character is

\[
 \psi_k^0(n)=\zeta(n)\overline{\chi_n(vk)}1_{(n,f)=1},
 \tag{4}
\]

where ζ is now a fixed finite-order character, with conductor supported
inside the fixed S. Partition the k rows according to whether the
primitive character inducing (4) is principal. This partition is made
before applying a functional equation. Its definition is independent
of the extra puncture l and of the squarefree-sieve divisor d.

On the nonprincipal subset the ordinary Hecke L-function is entire,
including when its finite character is real. Only its functional
equation is used; an exceptional real zero is irrelevant. The complete
natural presentation still satisfies

\[
 Q_k N R_{0,k}\ll KF
\]

on a frequency dyad Nk≈K. The parent's proof of its ordinary estimate
therefore applies on this row subset: original and reflected common
polynomials, logarithmic scale suprema, extra-puncture erasure, and
the μ² identity retain the same inducing character. The subset may be
enlarged only after the exact nonprincipal reflection. This gives

\[
 \sum_{\substack{Nk\asymp K\\\psi_k^*\ne1}}
 \left|\sum_{(n,fl)=1}\frac{\mu^2(n)\zeta(n)}{\sqrt{Nn}}
       \overline{\chi_n(vk)}U(Nn/Y)\right|^2
 \ll (KFLY)^\epsilon K\sqrt F.
 \tag{5}
\]

Thus all nonprincipal rows have exactly the parent's total B cost
after the f,m,l sum. No pole has been ignored to obtain (5).

## 3. The exact good-prime support of a principal frequency

Since ζ is ramified only at S, a principal inducing character in (4)
must be unramified at every good prime. At such a prime the local
sextic Kummer exponent in vk must consequently be zero modulo six.

At a prime dividing f but not m, the exponent of v is two, so the
exponent in k is four modulo six. At a prime dividing m, the exponent
of v is seven, so the exponent in k is five modulo six. At every good
prime outside f, the exponent in k is zero modulo six. Therefore the
good part of every principal frequency has the exact shape

\[
 k_{\rm good}=(f/m)^4m^5q^6=f^4m q^6,
 \qquad q\text{ good},\qquad N(f^4m)=F^4M.
 \tag{6}
\]

The displayed exponents describe a necessary condition; the fixed ray
and S-local conditions can further restrict this set. The natural
zeros at primes dividing vk or f remain, even though the inducing
phase is principal. No condition (q,f)=1 is imposed.

Write a general nonzero lattice frequency as u k_S k_good, with u a
unit and k_S supported on S. Taking all such units and S-parts only
enlarges the principal set. The ideal count and the convergence of
the finite-prime geometric series give

\[
 \#\{k\text{ principal as in (4)}:Nk\le K\}
 \ll_S\left(\frac K{F^4M}\right)^{1/6}.
 \tag{7}
\]

When the right side corresponds to a subunit q range, that range is
empty. Bounded annular changes in (7) only change the fixed constant.

It is useful to retain the physical Fourier tail rather than first
replace it by a row count. For any fixed R>1/6, enlarged if necessary
to absorb smooth seminorm and small-power losses, (6) implies

\[
 \sum_{k\text{ principal}}
        (1+Nk/K_{fm})^{-R}
 \ll_R\left(\frac{K_{fm}}{F^4M}\right)^{1/6}
      =\frac{K_0^{1/6}}F.
 \tag{8}
\]

Indeed for x>0,
Σ_q(1+(Nq)^6/x)^(−R)≪x^(1/6), by ideal counting when x≥1 and
absolute summation when x<1. Summing the S-supported part costs
Σ_(k_S)(Nk_S)^(−1/6)<∞. This proves (8) at every positive nominal
width K_(fm), including subunit widths. It does not insert a spurious
constant frequency contribution.

## 4. Pay the principal columns and sum the full ledger

For a principally induced row, the natural character in (4) is a
coprimality indicator on its original domain. Regardless of that mask,
the centrally normalized annular squarefree column is bounded by

\[
 \left|\sum_{(n,fl)=1}\frac{\mu^2(n)\zeta(n)}{\sqrt{Nn}}
       \overline{\chi_n(vk)}U(Nn/Y)\right|\ll\sqrt Y.
 \tag{9}
\]

The same estimate holds for the finite common profile derivatives and
their Mellin majorants. Empty subunit column ranges contribute zero;
a nonempty bounded scale costs only a fixed profile constant. The row
mask (k,l)=1 only reduces the positive bound.

If two columns in a finite bilinear ray expansion have different
principal subsets, use 2|ab|≤|a|²+|b|² before their estimates. Every
resulting square is covered by (5) or (8)--(9). No positivity of the
original finite pair phase is assumed.

Combining the exact outside weight with (8)--(9), the entire principal
contribution is at most

\[
\begin{split}
 &(AB)^\epsilon\frac AB
    \sum_f\sum_{m\mid f}\sum_l
      \frac1{ML}\,\frac B{FL}\,\frac{K_0^{1/6}}F\\
 &\qquad=(AB)^\epsilon A K_0^{1/6}
      \sum_f\frac1{F^2}\sum_{m\mid f}\frac1M
                       \sum_l\frac1{L^2}\\
 &\qquad\ll(AB)^\epsilon A^{5/6}B^{1/3}.
\end{split}                                                     \tag{10}
\]

All three ideal/divisor sums converge after an arbitrarily small
divisor loss. The discarded coprimality restrictions only decrease
this positive upper bound. The genuine pair diagonal remains
Oε(A(AB)^ε); the artificial unit pair and its subtraction remain
Oε(B^ε), exactly as in the parent. Equations (5) and (10), together
with these two terms, prove (2).

## 5. A concrete resonant coefficient and the remaining consumer

On squarefree good n the Gauss identity gives

\[
 \mu(n)\gamma_2(n)\alpha(n)^{-1}\overline{G(n)}
                         =\overline{\gamma_1(n)}.
 \tag{11}
\]

The finite-ray function overline(G) can be expanded in the permitted
fixed finite character basis. Thus (2) explicitly includes the
coefficient overline(γ₁) with positive sextic orientation, and its
whole conjugate. At A=B the added term is B^(7/6), so the resonant
case does not have the nonresonant A+B conclusion.

This prices the single-numerator functional-equation angle excluded
from the parent theorem. It does not remove the extra term in a
numerator consumer. It also does not change the PR1019 coefficient
comparison: its raw μ column produces αG overline(γ₂), with no free
μ factor, after the first transform. The missing coefficient remains
missing in (11). The exact signed inverse complement, the d₆
coefficient extension, and the complete sixth-moment consumer remain
separate open requirements.
