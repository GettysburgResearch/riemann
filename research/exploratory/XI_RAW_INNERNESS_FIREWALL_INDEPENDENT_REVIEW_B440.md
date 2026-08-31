# Independent review: raw-innerness hypothesis firewall

Verdict: PASS for the theorem note frozen at
`b44052443c6c84025771efe1fd0ff805e36a5f5d`:
`research/exploratory/XI_RAW_INNERNESS_RH_EQUIVALENCE_FIREWALL.md`.
The scientific note is unchanged. This is a proof/hypothesis audit, not
an additional computational science packet.

The reviewer read the complete note and the stated global-height and
global-capture parent passages. The proof uses the literal already-centered
function f(z)=xi_R(1/2+iz), not an arbitrarily rescaled or translated entire
function, and one fixed real lambda>0.

## Necessity, without a simple-zero assumption

At an upper-half-plane zero b of multiplicity m write f(z)=(z-b)^m h(z),
where h(b) is nonzero. After canceling the common order m-1, the quotient

    Theta_0=(f-i lambda f')/(f+i lambda f')

has value -1 and derivative -2i/(lambda m) at b. Its denominator after
cancellation is i lambda m h(b), nonzero. Thus no pole or removable-zero
ambiguity is being used to infer the value. A holomorphic contractive
function attaining modulus one at an interior point would be constant,
contradicting the displayed nonzero derivative. Real symmetry then excludes
zeros in the lower half-plane too. This proves the RH implication even
from the weaker Schur condition, before requiring boundary innerness.

As an independent exact algebra control, SymPy reduced the quotient for
f(z)=(z^2+1)^m for each m=1,...,16. In every case it gave Theta_0(i)=-1 and
Theta_0'(i)=-2i/(lambda m). At lambda=1, z=i/2 it gave
-(4m+3)/(4m-3), an explicit value of modulus greater than one. These finite
controls support the algebra; the local h-factor argument proves all m.

## Sufficiency and derivative scope

Under RH the real-rooted canonical product has the required sign for the
imaginary part of its logarithmic derivative in the upper half-plane.
The resulting Cayley quotient is holomorphic and contractive there and
unimodular on the real boundary, hence inner. The real-rooted approximation
and Rolle/Hurwitz argument in the pinned parent supplies the corresponding
property for f5. Consequently the conjunction of the two specified raw
innerness hypotheses is equivalent to RH, as is the zeroth hypothesis alone.

The note does not claim that innerness of the fifth companion alone forces
RH. The elementary polynomial z^6+1, whose fifth derivative is 720z,
independently demonstrates why reversing the derivative implication would
be invalid in general. Lambda=0 is expressly excluded; the identity quotient
at zero parameter would give no zero-location information.

## Consequences for the programme

The equivalence is a statement about the specified RAW components. A
representation of their quotient as a ratio of inner functions, boundary
unimodularity alone, and an independently constructed physical source are
different hypotheses. None may be silently substituted for the conjunction.

The already reviewed Hardy-space capture theorems remain valid conditional
theorems. Raw Xi root/value certificates, finite Gram geometry and the
imaginary-axis asymptotic remain unconditional. But using the stated raw
innerness premise to establish RH by those capture estimates would be
circular. A future weaker observation/metric theorem must supply new,
source-faithful hypotheses; this review does not construct one.

No RH/GRH, cofinal capture, native decoder or priority claim is made.
