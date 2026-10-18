# Review of the growing residue counterterm

Status: **source-qualified internal component review. No full mixed mean,
continuous-family estimate, or new zeta boundary is approved.**

The coordinator reconstructed `eisenstein/GROWING_RESIDUE_DEBIAS.md`,
raw SHA256
`1f3cecc2064ea1429b06dd94f1328c7e56de981219c9eebe927822da21a51f66`.
The initial Gram construction was discussed with its author; this is an
independent reconstruction of the displayed proof, not an external
referee report or an independent discovery claim.

The complete squarefree-tail response is a genuine Gram matrix of the
divisibility indicators. Its density is c_W f(lcm(g,h)). The exact
factorization f(g)f(h) sum_(d|g,h)Nd gives a uniform lower spectral bound:
invert the incidence transform by divisor Mobius inversion, apply weighted
Cauchy, and use the divisor bound. Normalizing the complete counting error
gives entries D^-1/2 sqrt(Ngcd(g,h)) up to small powers. The displayed
Schur estimate therefore proves conditioning for every fixed margin
G<D^(1/2). It does not infer conditioning from finite examples.

The prefix response follows from the NAMED fixed-field zero-free input.
The weighted reciprocal Euler correction converges absolutely for positive
real part, and the deleted-g factor costs g^epsilon on the displaced line.
The pole of the cutoff Mellin transform at zero meets a zero of the
reciprocal zeta at one. Solving the normalized matrix gives the full
weighted coefficient bound, not just bounds for fixed g.

After extracting each g, the correction has the positive squarefree Euler
series of the scalar-tail proof with its coprimality mask. The additional
geometric factors have complete absolute coefficient mass g^epsilon at
real part 1/2. The source's unrestricted TWO-PLAIN theorem can therefore
pay the whole correction before the g sum is removed. This is the deep
import, stated at its actual scope. In particular this does not use an
unavailable inverse row-size estimate for D>U.

With beta=7/8 and G=D^(1/5-eta), all complete coefficient resources are
subpower and the correction has squared joint cost U^(1+epsilon).
Internal small exponents must be chosen after eta, as usual. At G=U^.3,
D=U the larger cost U^(9/8) and pointwise U^(1/16) are correctly
distinguished; the old unchanged-count conclusion is not asserted there.

The polar formula was checked against the full constant-term argument of
the pinned rStation paper8, Sections5.1 and7. Multiplication by a squarefree
R makes the progression modulus aR, whose valuations can be TWO. All
nonunit reduced-denominator unit characters are still nonprincipal, so
their constant terms vanish. The argument does not use primitive Gauss
factorization at an imprimitive prime-square modulus. Its nonconstant
transform has extra nonunit frequencies and must be treated separately.

The complete primitive density is Z_S v(rad(aR))/(Na NR). Expanding the
factor 1/v(gcd(a,R)) gives exactly the F_g constraints for g dividing R.
All shared primes and fixed numerator filters remain. The variable change
in the product profile supplies NR^(-1/6), with no hidden twist of a.
Thus every displayed squarefree R<=G polar response vanishes at once.

This is a useful growing family of zero-preserving detectors. It does
not establish stability through a later canonical initialization: its
new coefficients after multiplication by a Gauss phase need not be the
global divisor convolution. Nor does it pay the growing nonpolar errors
or the full continuous/complementary row space. Those are mathematical
gaps; the residue cancellation alone gives no new region.
