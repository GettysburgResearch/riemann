# Independent review of complete moment norms and sextic absorption

Status: ACCEPT at the conditional analytic scopes stated in the two sources.
Scope: complete paired source tail in a known strip and complete finite
census; exact native moment enclosures are separate inputs. No new companion
slab, whole parameter-family certificate or RH claim is accepted here.

Reviewed exact files:

- `xi/outer-ray/MOMENT_NORM_TRANSPORT.md`, SHA-256
  `9279440530af0efc1f4c19b3dd9aca608ec9a5d6afde278687dc098b010967c4`.
- `xi/outer-ray/SEXTIC_ABSORPTION.md`, SHA-256
  `9d6a56bf4ea5553419d710ce96848122316886d0abbf4e8b490f46aca8d1f5e5`.

## Complete norms, MN1–MN7

The paired positive-real-part source representatives retain complete
conjugate blocks and multiplicities. Under the acute-angle inequality
`2k*atan(A/R)<pi/2`, cosine is positive and decreasing across every source
root angle. Thus each real projection is at least
`c_k*|rho|^-2k`; summing the complete source gives `c_k*S_2k<=t_k`.
The product already implies absolute inverse-square summability, which
justifies every higher inverse-power sum and logarithmic coefficient
extraction. The infinite actual source and finite central census supply a
nonempty tail for the stated strict positivity. The higher norm bound in
MN5 follows from `|rho|>R` term by term. The rational forms of the first
three cosines and sufficient guard `R>2k*A` are correct.

MN7 correctly subtracts the complete finite simple census from the complete
logarithmic coefficient. Native coefficient and selected-root intervals
must be authenticated separately. In particular the source's original
census at R=8192 keeps its imported historical FLINT count contract; the
smaller count-free censuses at 2048 and 2240 do not authenticate that larger
census. The lemma does not make that substitution.

## Two-pair construction, SA1–SA11

The strict K interval is equivalent to
`s2^(3/2)/sqrt(2)<s3<s2^(3/2)` for `s2=t2/K,s3=t3/K`.
The function `(3*s2*p-p^3)/2` decreases strictly on
`sqrt(s2)<p<sqrt(2*s2)`, with exactly these endpoint values. Its unique p
gives product `(p^2-s2)/2>0` and discriminant `2*s2-p^2>0`, hence a unique
unordered pair of distinct positive u,v. SA4 and the Gaussian reserve
`a=a1-K*(u+v)>0` follow with the stated strictness.

The base `G=Xi(0)*exp(-a*z^2)*P_R*(1-u*z^2)^K*(1-v*z^2)^K` is a real
Laguerre–Polya function. It matches exactly the complete logarithmic
coefficients of degrees two, four and six because the three displayed
moment identities hold. The quotient logarithm is analytic in the protected
disk: the original census factors cancel, the genuine tail factors have
modulus beyond R, and the artificial roots are excluded by `B^2*max(u,v)<1`.
No unknown source factor is removed from the residual.

Expanding the exact logarithmic derivatives leaves the genuine remainder
`-2*z^7*sum m/(rho^6*(rho^2-z^2))` and both artificial remainders
`2*K*z^7*u^4/(1-u*z^2)` and the v term. This verifies SA9, including its
signs and powers. Differentiation gives the factor
`7/(1-x)+2*x/(1-x)^2=(7-5*x)/(1-x)^2`; its derivative
`(9-5*x)/(1-x)^3` is positive on `[0,1)`. The full absolute bounds J1 and
J2 therefore apply throughout the disk. The stronger complete U8 bound
from t3 and the entire artificial contribution V4 are retained.

Real Gaussian polynomial approximants prove the lower companion sector for
G. The original census roots are simple, and its artificial multiple roots
are outside the protected disk. The real boundary Laguerre inequality is
strict there; the positive Gaussian reserve also supports strictness away
from the zeros. A compact family contained inside every strict guard thus
has positive uniform protected margins by continuity. Compactness must
actually be established for the family a future checker covers.

The full multiplier predicate SA11 follows from the separately derived
finite-census complement bound using `|q'/q|<=J1` and
`|q''/q|<=J1^2+J2`. These inequalities are necessary proof inputs to a
whole-family, whole-domain checker. A feasible K or a single accepted
parameter point cannot stand in for that missing computation.

No analytic gap found. The remaining native task is the complete parameter
family/domain certificate and its strict transfer predicate. No heavy
Gaussian or quartic runtime was repeated for this review; the analytic
source product and historical census remain explicitly imported.
