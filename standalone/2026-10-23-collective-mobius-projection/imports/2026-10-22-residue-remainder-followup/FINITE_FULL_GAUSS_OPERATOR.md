# A finite operator bound with all sextic Gauss moduli retained

22 October 2026. Status: proposed theorem with proof; independent review
pending. Scope: a finite Gauss matrix, including nonsquarefree moduli
and arbitrary label coefficients. This does not identify or estimate a
continued primitive remainder and does not imply a new zero-free bound.

The only analytic import is the sixth-power-free sextic large sieve of
de Faveri, Theorem 1.1, <https://arxiv.org/html/2610.04045v1>. The full
Gauss normalization is that of rStation paper 10, version 2, available
at <https://rstation.ai/api/v1/papers/riemann_hypothesis_10/versions/2/download>.
The downloaded paper-10 snapshot has SHA256
`525c899dd4dd5cb0ed15db43f63fb6e25cc140f98358e9d41ddfe897f5a23a7a`.

## Statement

Work in the Eisenstein integers, with good primary representatives and
the self-dual additive character used in paper 10. Norms below are ideal
norms. All multiplicative characters have their natural zero extension.
Rows are any subset of good ideals `Nn <= X`; labels are any set of
distinct sixth-power-free good ideals `NR <= K`. Let `L >= 1`, fix an
absolute constant `C >= 1`, and take arbitrary coefficients `a_c` with
`|a_c| <= 1`, supported on good ideals `Nc <= C L`. No squarefree
restriction is imposed on `c`. Set

\[
 T_L(n,R)=\sum_c
       \frac{a_c g_6(nR,c)}{\sqrt{L\,Nc}}.                 \tag{1}
\]

Then, for every `epsilon > 0`,

\[
 \boxed{\quad
 \|T_L\|_{\rm op}^2\ll_{\epsilon,C}(XLK)^\epsilon
 (X+L^2)\left(1+K L^{-5/6}
       +K^{1/3}L^{-1/6}+K^{5/6}L^{-2/3}\right).
 \quad}                                                   \tag{2}
\]

Fixed ray sectors, row and label subsets, and common modulus punctures
are allowed. They do not turn (2) into a bound for a matrix with an
arbitrary moving coprimality mask.

## Proof

Fix an arbitrary label vector `lambda_R`. Expand the additive Gauss
sum and, in a term with modulus `c` and label `R`, put

\[
             t=(c,R),\qquad c=mt,\qquad R=tR_0.
\]

Thus `(m,R_0)=1`. Each prime exponent in `t` is at most five.
If a prime of `c` disappears entirely from `m`, its exponent in `c`
lies between one and its exponent in `R`, hence between one and five.
The additive phase is then constant in that prime component, while its
sextic character is nonprincipal. Its unit sum vanishes. Consequently
every nonzero term satisfies

\[
                  \operatorname{rad}(c)=\operatorname{rad}(m).
                                                               \tag{3}
\]

Under (3), reduction of units from modulus `c=mt` to modulus `m` has
fibers of size `Nt`. The character `chi_c` factors through this
reduction. Changing the reduced unit variable by `y=R_0 x` gives

\[
 g_6(nR,mt)=Nt\,\overline{\chi_{mt}(R_0)}
           \sum_{y\bmod m}^{*}\chi_{mt}(y)e(ny/m).       \tag{4}
\]

This is a finite identity; no functional equation or analytic
continuation is involved.

Collect the coefficients of each reduced additive fraction `y/m`:

\[
 (T_L\lambda)(n)=\sum_m\sum_{y\bmod m}^{*}
                     A_{m,y}e(ny/m),
\]

\[
 A_{m,y}=\sum_{\substack{t:\,\operatorname{rad}(t)\mid
                                      \operatorname{rad}(m)}}
       \sqrt{\frac{Nt}{L\,Nm}}\,a_{mt}\chi_{mt}(y)
       \sum_{R_0}\lambda_{tR_0}
                       \overline{\chi_{mt}(R_0)}.       \tag{5}
\]

The label coefficient is zero unless `tR_0` is in the permitted label
set. This retains every original support restriction. The character
in the inner sum enforces `(m,R_0)=1` under (3).

The distinct reduced fractions `y/m`, with `Nm <= C L`, are separated
modulo the Eisenstein lattice by at least a constant times `L^{-1}`
in complex absolute value. Indeed a nonintegral difference has a
nonzero integral numerator over `m m'`, and
`|m m'| <= C L`. The elementary additive large sieve in two real
dimensions therefore gives

\[
 \sum_{Nn\le X}|(T_L\lambda)(n)|^2
   \ll_C (X+L^2)\sum_m\sum_{y\bmod m}^{*}|A_{m,y}|^2.  \tag{6}
\]

For completeness, (6) follows by majorizing the disk `|n|<=sqrt(X)`
by a Gaussian, applying lattice Poisson to its Gram matrix, and using
the separation just proved. Packing separated points bounds each
Gram row by `O(X+L^2)`; Schur's bound proves (6). Positive extension
from good primary rows to the whole lattice is legitimate.

For fixed `m`, the characters `chi_{mt}` in the outside sum of (5)
are pairwise distinct as `t` varies. If `t != t'`, some prime exponent
differs by a nonzero integer of absolute value at most five. Their
quotient at that prime is a nonprincipal sextic power character on
the units modulo `m`. Hence character orthogonality, followed by
`phi(m)<=Nm`, gives

\[
 \sum_{y\bmod m}^{*}|A_{m,y}|^2
 \le \sum_t\frac{Nt}{L}|a_{mt}|^2
       \left|\sum_{R_0}\lambda_{tR_0}
          \overline{\chi_m(R_0)}
          \overline{\chi_t(R_0)}\right|^2.             \tag{7}
\]

The sixth-power-free hypothesis on the labels is essential at this
orthogonality step. With arbitrary labels, exponents of `t` can
coincide modulo six.

The imported sextic sieve implies the following unrestricted-row
version, for sixth-power-free columns of norm at most `N`:

\[
 \sum_{Nm\le M}\left|\sum_{NR_0\le N}b_{R_0}
                                       \chi_m(R_0)\right|^2
 \ll_\epsilon(MN)^\epsilon\Psi_{\rm all}(M,N)
                                  \sum_{R_0}|b_{R_0}|^2,
\]

\[
 \Psi_{\rm all}(M,N)=M+N M^{1/6}
                      +M^{5/6}N^{1/3}+M^{1/3}N^{5/6}.
                                                               \tag{8}
\]

To prove (8), write `m=m_0 q^6` uniquely, with `m_0`
sixth-power-free. For each fixed `q`, retain the fixed column mask
`(q,R_0)=1` and apply the imported theorem to `m_0`. Summing its
four terms over `Nq <= M^{1/6}` gives (8); the first, third, and fourth
terms use respectively convergent sums with exponents six, five, and
two. This also proves the conjugated orientation used in (7).

For a fixed `t`, use (8) with `M=C L/Nt` and `N=K/Nt`, extending the
permitted modulus subset positively. The fixed multiplier
`overline(chi_t(R_0))` is a bounded column coefficient. After
multiplication by `Nt/L`, the resulting cost is bounded by a constant
times

\[
 1+(Nt)^{-1/6}\left(KL^{-5/6}
             +K^{1/3}L^{-1/6}+K^{5/6}L^{-2/3}\right).  \tag{9}
\]

Cases `M<1` or `N<1` are empty. Finally sum over `t`. A fixed label
`R` occurs only for divisors `t|R`; its divisor count is `O_epsilon(K^epsilon)`.
Equations (6)--(9) prove (2), after using smaller internal subpowers.
QED.

## A natural-length corollary

For `K <= sqrt(X)`, let `F` be a fixed smooth compactly supported
function on `[0,infinity)`. Then

\[
 T(n,R)=K^{-1/2}\sum_c\frac{g_6(nR,c)}{\sqrt{Nc}}
                                      a_c F(Nc/K),
 \qquad |a_c|\le1,
\]

satisfies

\[
                    \|T\|_{\rm op}^2
                   \ll_{\epsilon,F}(XK)^\epsilon X K^{1/6}.
                                                               \tag{10}
\]

Split into modulus dyads `L<=C_F K`. Relative to (1), the squared
normalization contributes `L/K`. The right side of (2) is therefore
at most a subpower times

\[
 X\left(\frac LK+L^{1/6}
               +L^{5/6}K^{-2/3}+L^{1/3}K^{-1/6}\right)
                         \ll_F X K^{1/6}.
\]

Dyadic Cauchy costs a logarithm, absorbed into the subpower. In
particular the modulus-one term has squared norm `O(X)`, rather than
the `O(XK)` that would arise with an unscaled coefficient one.

This corollary applies only to an actual finite kernel with the
displayed `K^{-1/2}` normalization. It does not license replacing a
continued Dirichlet series by such a kernel, and it does not handle
the larger scales `Nr (Nd)^4/U` produced by primitive inversion.
