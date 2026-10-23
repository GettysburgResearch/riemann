# The completed sextic reflection kernel and exact decompletion

Date: 22 October 2026. Status: native analytic deduction from the
version-pinned finite-vector functional equation below; independent review
requested. Scope: a full sextic Kubota series, every finite local component
needed for its reflection, and a smooth scalar Mellin transform. This note
does not prove a bound for the moving-coprimality primitive series, a
complementary operator estimate, or a smaller zero-free boundary.

The proposed use of completion followed by an optimized reciprocal-Euler
split is signed_kernel's. This note supplies joint_continuation's separate
verification of the finite-vector kernel, its analytic contour shifts,
and the exact treatment of residues under completion and decompletion.

## 1. Sources and conventions

The primary functional-equation source is Reinier Bröker and Jeff
Hoffstein, *Fourier coefficients of sextic theta series*,
[arXiv:1312.0568v1](https://arxiv.org/html/1312.0568v1), specifically
Theorem 2.4, the definition of `Psi` preceding (3.1), (3.1),
(3.8)--(3.10), and the ramified and unramified local gamma formulas
immediately following (3.10). The downloaded HTML snapshot has SHA256

`2dabda8ba741c1d43fd3cf81ea36a8b059fa5febf98b3840fd0af487055e1b34`.

Its local path is
`work/round3_sources/broker_hoffstein_1312.0568v1.html`.
The plain-text extraction is a reading aid, not an independently obtained
source; its SHA256 is
`04f0ecd6561f169f5af213f956718ef72a1caaec96161e7d1faeb8bc92d63279`.

The translation to good primary Eisenstein moduli and the complete fixed
216-component family is the source-qualified normalization in Section 2
of rStation paper 10, version 2:

<https://rstation.ai/api/v1/papers/riemann_hypothesis_10/versions/2/download>.

The snapshot `work/round2_sources/paper10-v2.md` has SHA256
`525c899dd4dd5cb0ed15db43f63fb6e25cc140f98358e9d41ddfe897f5a23a7a`.
Only this finite-vector normalization and analytic continuation are
imported here. In particular no residue-density statement for the full
216-component family is assumed.

Let `K=Q(omega)`, let `q_a=Na`, and let `S_f` be the two prime ideals
above 2 and 3. A good modulus is prime to 6. Write

\[
 D_j(r,u)=\sum_{c\ {\rm good}}
             a_j(c)\frac{g_6(r,c)}{q_c^u},\qquad
 Z_j(r,u)=\zeta_S(6u-5)D_j(r,u).                         \tag{1}
\]

Here the `a_j` are the fixed local-class indicators, or equivalently
their fixed finite Fourier transforms into characters of the local
sixth-power quotient. The full vector is retained. The Gauss orientation
is exactly `g_6(r,c)=sum_x chi_c(x)e(rx/c)`. All its natural zeros and
all nonsquarefree moduli remain present.

The numerator `r` is good. The fixed conversion between the trace
character in the primary source and the self-dual additive character
in (1) changes `r` by a fixed factor supported at `S_f` and changes the
modulus coefficient by a fixed sixth-order ray character. Such factors
are included in the finite data below. This conversion has fixed
valuations at `S_f`; it introduces no growing local conductor.

Fix `w` in `C_c^infinity((0,infinity))`, and define

\[
 \widehat w(z)=\int_0^\infty w(x)x^z\,\frac{dx}{x},
 \qquad
 E_{Y,i}(r)=\frac1{2\pi i}\int_{(1+\eta)}
       Z_i(r,u)\widehat w(u-\tfrac12)Y^{u-1}\,du,
 \quad 0<\eta<1/12,\quad Y>0.                         \tag{2}
\]

The constants below depend on fixed local data and smooth seminorms of
`w`, but not on `r` or `Y`. The norm of `r` is the only growing factor
in the conductor rescaling. No sign condition on `w` is needed.

## 2. Finite Laurent form of the bad-place transition matrix

Put

\[
 G(s)=\frac{\Gamma(6s)}{\Gamma(s)},\qquad
 G_f(s)=\prod_{p\in S_f}(1-q_p^{-1+6s})^{-1}.
                                                               \tag{3}
\]

In Bröker--Hoffstein's notation,

\[
 \Psi_i(r,s)=y_r^{-s}G(s)Z_i(r,1+s),\qquad
 y_r=c_Sq_r^{-1/2},
\]

where `c_S>0` is fixed, after the fixed additive-character conversion.
Their equation (3.1) is a finite-vector identity

\[
 \boldsymbol\Psi(r,s)=C_SG_f(s)T(r,s)
                                  \boldsymbol\Psi(r,-s),       \tag{4}
\]

with a fixed nonzero normalization constant `C_S`.

For the good numerator family, every entry of `T(r,s)` is a finite
Laurent polynomial in the variables `q_p^{-s}`, with coefficients
depending only on a fixed finite local class of `r`. This assertion
follows analytically from source (3.10), rather than from the numerical
matrix observation in its Section 4.5. Indeed, write `z=q_p^{-s}`.
An unramified local gamma factor has the form

\[
 (\xi z)^{-d_p}
 \frac{1-q_p^{-1}(\xi z)^{-1}}{1-\xi z}\,q_p^{-d_p/2},
 \qquad \xi^6=1.                                      \tag{5}
\]

The prefactor `1-z^6` in source (3.10) cancels its only denominator,
since `1-xi z` divides `1-z^6`. A ramified local gamma factor is a
monomial in `z`, multiplied by a fixed local Gauss constant. All
local quotient sums in that transition formula are finite. The
remaining norm factor in (3.10) is a monomial whose exponents are
fixed because the numerator's bad-place valuations are fixed.

There is a source-notation correction in this statement. Both the
version-1 HTML and PDF print the `h`-index in (3.10) as
`O_S/O_S^{*6}`, without the star in the numerator. The transition
calculation uses the finite S-unit quotient `O_S^*/O_S^{*6}`.
This correction is supported by the source's preceding finite
construction: Lemmas 2.1--2.2 identify

\[
 A=K_S^*/K_S^{*6},\qquad
 H=\operatorname{im}(O_S^*)\simeq O_S^*/O_S^{*6},
 \qquad |A|=6^{2\#S},\quad |H|=6^{\#S}.
\]

The component representatives are those of `A/H`, and Remark 2.3
gives their S-unit equivariance. Passing between functions on `A`
and these equivariant components is a finite character-orthogonality
projection over `H`. It is this `H` index that occurs in the
transition formula; its displayed normalizing denominator
`6^(2#S)` is `|A|`. Thus the finite quotient is determined before
any local gamma factor is evaluated. The literal printed quotient
of all S-integers is infinite, and cannot define that transition
projection or a convergent sum: the displayed summand has no decay
in `h`. We record the missing star explicitly rather than using
such an infinite sum or inferring the Laurent property from the
numerical Section 4.5.

Thus, after a finite partition by `[r]`, the product
`C_S c_S^(-2s)T(r,-s)` is a finite sum of terms

\[
                \kappa_{ij\ell,[r]}\lambda_{ij\ell,[r]}^s,
       \qquad \lambda_{ij\ell,[r]}>0.                 \tag{6}
\]

The number of terms, their coefficients, and their positive scales
belong to a fixed finite set. Expanding the numerator-class indicators
into finite ray characters is legitimate; no character depending on
a growing prime is introduced.

## 3. Exact reflected identity and cancellation of the theta pole

Use (4) with `-s` in place of `s`. It gives

\[
 Z_i(r,1-s)=C_Sc_S^{-2s}q_r^s
       \frac{G(s)}{G(-s)}G_f(-s)
                  \sum_jT_{ij}(r,-s)Z_j(r,1+s).        \tag{7}
\]

Both the numerator and the chosen sextic Gauss orientation are
unchanged. There is no complex conjugation of the residue symbol in
this functional equation.

In (2), put `u=1-s`. Initially the `s` line is `Re s=-eta`; apply
(7), then move the line to any fixed `sigma>1/2`. This shift is
legitimate as follows. For `-eta<=Re s<=0`, the left side of (7)
is regular by the source continuation in `1<=Re u<=1+eta<7/6`.
For `Re s>=0`, each `Z_j(r,1+s)` has at most a simple pole at
`s=1/6`. The factor `1/G(-s)` has a simple zero there:
`G(-1/6)=Gamma(-1)/Gamma(-1/6)` has a simple pole.
All remaining factors in (7) are regular at `s=1/6`, by (3) and
Section 2. This cancels the reflected theta pole. There is no
additional residue in the reflected identity.

The source's regularity at `s=0` also matters. Although
`zeta_K(1+6s)` has a pole there, it is not permissible to treat it
separately during this contour shift; the completed vector is
regular there by Theorem 2.4. Only after moving to `sigma>1/2`
do we expand its Dirichlet series. Polynomial vertical growth of
the completed series and the rapid vertical decay of `widehat w`
justify the horizontal limits.

On that final line,

\[
 G_f(-s)\zeta_S(1+6s)=\zeta_K(1+6s)
                =\sum_{b\ {\rm integral}}q_b^{-1-6s}. \tag{8}
\]

The ideal `b` ranges over **all** integral ideals, including the
bad primes. This is exactly the source identity used in (3.8)--(3.9).
The good-modulus series `D_j(r,1+s)` is absolutely convergent on this
line as well. Consequently (2) becomes the exact finite sum

\[
 \boxed{\displaystyle
 E_{Y,i}(r)=
 \sum_{j,\ell}\kappa_{ij\ell,[r]}
 \sum_{c\ {\rm good}}\sum_{b\ {\rm integral}}
   \frac{a_j(c)g_6(r,c)}{q_cq_b}
   K_w\!\left(\frac{q_cq_b^6Y}
                       {\lambda_{ij\ell,[r]}q_r}\right).}
                                                               \tag{9}
\]

Here

\[
 K_w(x)=\frac1{2\pi i}\int_{(\sigma)}
          \frac{G(s)}{G(-s)}\widehat w(\tfrac12-s)x^{-s}\,ds.
                                                               \tag{10}
\]

An equivalent finite Fourier basis replaces the indicators `a_j`
by fixed ray characters. Formula (9) retains all these components
and all fixed rescalings. A smooth common profile in `q_r/D` is
therefore the correct result when `r` is later summed in an annulus;
freezing `q_r` at the center of that annulus is unnecessary.

## 4. Kernel estimates, derivatives, and subunit scales

For every nonnegative integer `j`, every `A>0`, and
`0<delta<1/6`,

\[
 |(x\partial_x)^jK_w(x)|\ll_{j,A,\delta,w}
 \begin{cases}
 x^{1/6-\delta},&0<x\le1,\\
 x^{-A},&x\ge1.
 \end{cases}                                             \tag{11}
\]

To prove the first estimate, move the contour in (10) to
`Re s=-1/6+delta`. The multiplication formula gives

\[
 G(s)=c\,6^{6s}\prod_{k=1}^5\Gamma(s+k/6),
\]

so its first left-hand pole is at `s=-1/6`; no pole is crossed.
The reciprocal `1/G(-s)` is entire. For the second estimate move
to `Re s=A`, where the integrand has no poles. On every fixed
vertical line away from a numerator pole, Stirling's formula gives
a gamma quotient of polynomial growth, with exponent `10 Re s`
at large height. Its exponential factors cancel. The annular smooth
Mellin transform has arbitrarily fast vertical decay. Applying an
Euler derivative inserts a power of `-s` and does not change the
argument. The same proof controls every fixed finite common-profile
seminorm after composing with norm coordinates in fixed annuli.

In particular, a transform in (9) is not a compactly supported
modulus sum. If its effective scale `H=q_r/(Yq_b^6)` is below one,
the sum is controlled by the large-argument decay in (11); it must
not be set equal to zero. For example, suppose an independently
proved scalar modulus-dyad bound at `q_c asy L`, `L>=1`, has amplitude

\[
 B(L)\ll (LDNQ)^\epsilon
                 \bigl(L^{1/2}+D^{5/12}L^{1/12}\bigr),          \tag{12}
\]

uniformly for the required common-profile seminorms. Multiplying by
the envelope in (11) and summing dyadically gives

\[
 \ll (DNQ\max(1,H))^\epsilon
              \bigl(H^{1/2}+D^{5/12}H^{1/12}\bigr).             \tag{13}
\]

For `H>=1`, the powers on dyads `L<=H` are respectively
`1/2+1/6-delta` and `1/12+1/6-delta`, both positive; hence their
sum is controlled by the final dyad. The dyads `L>=H` converge
after choosing `A` large. For `0<H<1`, every modulus dyad has
`L>=1`, so large-argument decay gives the stronger bound
`H^A(1+D^(5/12))(DNQ)^epsilon`. This implies (13) for `A>=1/2`.
Thus no inverse-moment estimate with an empty row ball below one
is needed. Statement (13) is a deterministic kernel consequence of
the stated dyad input (12), not an assertion of that arithmetic
input for arbitrary coefficients.

## 5. Original completion, its residue, and exact raw removal

Let `rho_i(r)=Res_(u=7/6) D_i(r,u)`, and define the finite physical sum

\[
 S_i(Y;r)=Y^{-1/2}\sum_{c\ {\rm good}}
               \frac{a_i(c)g_6(r,c)}{\sqrt{q_c}}w(q_c/Y).
\]

Moving the original contour (2) to the absolutely convergent
half-plane gives the exact identity

\[
 E_{Y,i}(r)=\sum_{b\ {\rm good}}q_b^{-1}S_i(Y/q_b^6;r)
       -\zeta_S(2)\widehat w(2/3)Y^{1/6}\rho_i(r).     \tag{14}
\]

The completion variable here is good, as opposed to the all-ideal
variable in (9). The sum in (14) is finite for every `Y`, because
`w` is annular. If `supp w` is contained in `[a,b]` and `bY<1`, it
is empty and the remainder is exactly the negative displayed
residue. This physical emptiness statement concerns (14), not
the reflected kernel series (9).

Finally put

\[
 E^D_{U,i}(r)=\frac1{2\pi i}\int_{(1+\eta)}
            D_i(r,u)\widehat w(u-1/2)U^{u-1}\,du.
\]

On this line `Re(6u-5)>1`, so the reciprocal Euler series is
absolutely convergent. It gives, with every scale retained,

\[
 \boxed{\displaystyle
 E^D_{U,i}(r)=\sum_{a\ {\rm good}}\frac{\mu(a)}{q_a}
                              E_{U/q_a^6,i}(r).}       \tag{15}
\]

The residue normalization is consistent term by term:

\[
 \zeta_S(2)\sum_{a\ {\rm good}}\frac{\mu(a)}{q_a}
                              (U/q_a^6)^{1/6}
   =\zeta_S(2)U^{1/6}\sum_a\frac{\mu(a)}{q_a^2}
   =U^{1/6}.                                          \tag{16}
\]

Thus (15) subtracts exactly the raw full-series theta residue. It
does not lose or duplicate it. No raw functional equation is used
to cross zeros of a reciprocal zeta factor, and this lemma requires
no zero-free premise. Neither (9) nor (15) performs the additional
divisor inversion necessary to pass from the full series to the
primitive series with its moving exclusion.
