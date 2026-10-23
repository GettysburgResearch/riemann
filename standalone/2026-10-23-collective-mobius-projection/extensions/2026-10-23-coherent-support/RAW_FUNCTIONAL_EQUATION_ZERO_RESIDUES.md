# Raw functional equation: gamma cancellation and zero residues

This is an exploratory scope calculation, not a new estimate for the full raw remainder. It uses the exact finite-vector identity in the imported `COMPLETED_FE_KERNEL.md`, equations (7)--(10). All finite ray components and fixed rescalings remain present.

Write `Z_i(r,u)=zeta_S(6u-5)D_i(r,u)` and `G(s)=Gamma(6s)/Gamma(s)`. Dividing the completed reflection at `u=1-s` by its completion introduces

\[
 \frac{G(s)}{G(-s)}\,
 \frac{\zeta_E(1+6s)}{\zeta_S(1-6s)}.                 \tag{R1}
\]

Here `G_f(-s)zeta_S(1+6s)=zeta_E(1+6s)` has already restored the bad Euler factors on the numerator side. The denominator still has its deleted Euler factors. They must remain in the exact finite local multiplier; they are not uniformly bounded across all lines used below.

For `A=sqrt(|disc E|)/(2pi)`, the ordinary Dedekind functional equation is

\[
 \zeta_E(1-6s)=A^{12s-1}
       \frac{\Gamma(6s)}{\Gamma(1-6s)}\zeta_E(6s).
\]

Consequently the archimedean part simplifies exactly to

\[
 \frac{G(s)}{G(-s)}
 \frac{\Gamma(1-6s)}{A^{12s-1}\Gamma(6s)}
       =6A^{1-12s}\frac{\Gamma(1-s)}{\Gamma(s)}.       \tag{R2}
\]

On `Re s>1/6`, the remaining full zeta ratio has the absolutely convergent expansion

\[
 \frac{\zeta_E(1+6s)}{\zeta_E(6s)}
   =\sum_b a(b)(Nb)^{-6s},\qquad
 a(p^k)=-(Np-1)(Np)^{-k}\quad(k\ge1).                \tag{R3}
\]

Thus `|a(b)|<=1`. For an annular smooth Mellin test, the kernel made from `Gamma(1-s)/Gamma(s)` has rapid decay as its argument tends to zero and an `O(x^-1)` expansion as its argument tends to infinity. The latter comes from the first numerator pole at `s=1`; it is not the rapidly decreasing large-argument kernel of the completed identity. Fixed logarithmic derivatives obey the corresponding bounds.

The essential contour obstruction comes before expanding R3. The original raw integrand contains

\[
 D_i(r,1-s)=\frac{Z_i(r,1-s)}{\zeta_S(1-6s)}.          \tag{R4}
\]

At every nontrivial Dedekind zero `rho`, R4 has a possible pole at

\[
             s_\rho=(1-\rho)/6.                       \tag{R5}
\]

The source proves regularity of the completed vector `Z` there. Regularity does **not** prove divisibility by the zero of the denominator. If `rho` is simple and the relevant completed component does not vanish, the residue in the `s` variable is

\[
 -\frac{Z_i(r,(5+\rho)/6)}{6\zeta_S'(\rho)}.           \tag{R6}
\]

It must be multiplied by the original Mellin test and scale factors. Multiple zeros require their full principal parts. The new gamma factors in R2 are regular and nonzero at R5, so they do not themselves remove these contributions. Finite local factors likewise cannot be discarded; any cancellation has to be established for the exact vector product.

The shift from `Re s=-eta` to a line on which R3 converges therefore needs these zero residues, unless a new theorem proves the relevant completed-vector divisibility. This note neither asserts nor excludes that a particular component vanishes at a particular zero. It identifies the missing statement needed to cross all of them without residues.

As a diagnostic, the remaining transformed series, *after* accounting for the zero residues and fixed local singularities, has the formal modulus estimate

\[
 C+D^{5/6}C^{1/3},\qquad C=DH/U,                     \tag{R7}
\]

from the existing scalar modulus-dyad bound. Indeed its amplitudes are `C^(1/2)` and `D^(5/12)C^(1/12)` times the absolute `b` sum; the second sum up to `C^(1/6)` costs another `C^(1/12)`. R7 is not a bound for the full raw expression without the retained residues. In particular it cannot replace the signed-completion theorem already proved in this packet.

The possible zero residues have raw-scale amplitude `U^(-(1-Re rho)/6)`. This matches the exponent supplied by the signed reciprocal-completion Mertens argument and explains why removing that factor without controlling the residues would be a substantive additional theorem.
