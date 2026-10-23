# Two precise limits of an all-field zero-free bootstrap

23 October 2026. Exploratory global-route audit. The propositions below are
elementary deductions from the indicated standard inputs. They do not prove RH,
improve a zero-free boundary, or rule out all arguments involving number fields.
Their purpose is to identify exactly what a proposed field-construction bridge
must add beyond Artin formalism and a common zero-free half-plane.

Assume, for discussion, that every finite-order Hecke L-function over every
number field is holomorphic and nonzero on `Re(s)>beta`, apart from its
principal pole at 1, where `1/2<beta<1`. Call this premise H(beta).

## 1. A valid extension that does not move the boundary

H(beta) implies that every finite-image Artin L-function is holomorphic and
nonzero in the same half-plane away from 1. At 1 its pole order is the
multiplicity of the trivial representation. Indeed, Brauer induction writes
its character as an integer combination of characters induced from
one-dimensional characters of subgroups. Class field theory identifies their
L-functions with finite-order Hecke L-functions. Induction and multiplication
hold at the same complex argument s. The resulting quotient has no zero or
pole away from 1 under H(beta). Frobenius reciprocity gives the stated order
at 1. No assertion of Artin holomorphy outside this half-plane is used.

Thus the formalism legitimately enlarges the representation family. It does
not by itself turn beta into a smaller number.

## 2. No finite Artin identity can rescale the argument

Consider any finite product and quotient of finite-order Hecke L-functions
over number fields, with integer exponents. After induction to Q and passing
to a common finite Galois extension, it is the L-function of a virtual
finite-image representation V. Removing finitely many Euler factors is harmless
for the following assertion.

**Proposition.** For an integer `m>=2` and any fixed complex a, this product
cannot have the same unramified Euler factors as `zeta(ms+a)` outside a finite
set. The same assertion holds for a nonzero integral power of that target.

**Proof.** Infinitely many rational primes split completely in the common
Galois extension. At any such prime the Artin local factor is

    det(1-Frob_p T | V)^(-1) = (1-T)^(-d),  d=dim V in Z.

The proposed target factor is `(1-p^(-a) T^m)^(-r)`, with `r!=0`. Equality of
these analytic germs at T=0 forces `d=0` by the coefficient of T. The first
factor is then identically1, whereas the coefficient of T^m in the second is
`r p^(-a)!=0`, a contradiction. This also excludes a global identity of
normalized Dirichlet series with these local factors: uniqueness of absolutely
convergent Dirichlet series recovers the prime-power coefficients. QED.

In particular, neither `zeta(ms)` followed by reflection nor the centered
rescaling `zeta(ms-(m-1)/2)` is produced by a finite Artin/Hecke induction,
product, quotient, tensor, or exterior-power construction. The last two
operations still give finite-image representations, so the same split-prime
test applies. A real Tate twist leaves the finite-order/unitary family and
cannot silently inherit H(beta).

This proposition excludes this exact rescaling mechanism, not every possible
identity or inequality involving these families. In particular it makes no
claim about infinite limits, analytic functorial operations of another kind,
or a new arithmetic estimate.

## 3. The natural infinite-family limit is necessarily non-normal

There is a sharper obstruction to replacing a finite identity by a compactness
argument. For each integer y choose a prime `q_y>y`, tending to infinity, such
that the primitive quadratic character `chi_y(n)=(n/q_y)` satisfies

    chi_y(p)=-1 for every prime p<=y.                         (N1)

The construction is elementary. Impose `q_y=5 mod8`; for every odd p<=y choose
a nonzero quadratic nonresidue a_p modulo p and impose `q_y=a_p mod p`.
The Chinese remainder theorem gives a reduced residue class. Dirichlet's
theorem gives arbitrarily large primes in it. Since `q_y=1 mod4`, quadratic
reciprocity and the supplementary law at2 prove N1. Each character is
nonprincipal and primitive of prime conductor q_y.

For every fixed positive integer n, eventually
`chi_y(n)=(-1)^Omega(n)`. Since `|chi_y(n)|<=1`, dominated convergence of the
Dirichlet series, uniform on compact subsets of `Re(s)>1`, gives

    L(s,chi_y) -> sum_n (-1)^Omega(n) n^(-s)
               = product_p (1+p^(-s))^(-1)
               = zeta(2s)/zeta(s).                          (N2)

**Proposition.** Under H(beta), for every `0<r<1-beta`, the family
`{L(s,chi_y)}` is not locally bounded on the disk `|s-1|<r`. In particular,
there is no conductor-independent uniform bound on the closed disk
`|s-1|<=r`.

**Proof.** Suppose it were locally bounded on that disk. Montel's theorem
gives a subsequence converging locally uniformly there to a holomorphic
function G. The intersection of the disk with `Re(s)>1` is nonempty; N2
identifies G there with `zeta(2s)/zeta(s)`, so G is not identically zero.
For a sufficiently small neighborhood of1, the latter quotient has a
holomorphic continuation with a simple zero at1, because zeta has a simple
pole at1 and `zeta(2)!=0`. The identity theorem therefore gives `G(1)=0`.
But H(beta) makes every member of the sequence zero-free throughout the
disk. Hurwitz's theorem says that a locally uniform holomorphic limit is
either identically zero or zero-free, a contradiction. QED.

The proof only needs the assumed zero-free property for this quadratic
sequence. It uses actual primitive L-functions with their usual functional
equations, not arbitrary model Euler products. The normal-family premise
is consequently incompatible with H(beta) for this construction, even
though convergence to the Euler-product limit on `Re(s)>1` is exact.

One can also see the danger without any zero-free hypothesis from the finite
products `product_(p<=y)(1+p^(-s))^(-1)`: they are holomorphic and zero-free
on `Re(s)>0` and converge as in N2 on `Re(s)>1`, but cannot be locally bounded
on a disk about1 by the same argument. A common zero-free domain is not a
normal-family estimate.

## 4. What a successful bridge would still require

The finite formalism preserves s; the infinite prescribed-prime sequence has
an unavoidable failure of conductor-independent local boundedness. Thus a
new contraction must use additional quantitative arithmetic cancellation,
a renormalization whose nonzero analytic limit and zero correspondence are
proved, or a different structural mechanism. Neither Artin positivity nor
Hurwitz alone supplies the missing step. These conclusions are obstacles to
the two stated routes, not evidence against RH or a logical impossibility
theorem for every consequence of H(beta).

## Primary-source anchors

* David Rohrlich, *PCMI lectures*, Lecture3, section1.3, gives additivity,
  inductivity and dimension-one compatibility of Artin L-functions:
  <https://math.bu.edu/people/rohrlich/pcmi.pdf>. The displayed induction
  identity retains the argument s. The web search indexed this passage;
  a full PDF fetch timed out, so this note does not claim a new full-source
  audit of Rohrlich's lectures.
* Kiran Kedlaya, *Notes on analytic number theory*, sections22.2,22.4,22.5,
  supplies the Euler determinant, induction framework and split-prime
  Chebotarev statement used in the local obstruction:
  <https://kskedlaya.org/ant/chap-artin.html>. The current page was read on
  23 October2026. The stronger integer-valued Brauer induction in section1
  is a standard separate input; the argument could equivalently use rational
  induction after raising to a common positive integral power.
* D.H. Lehmer, Emma Lehmer and Daniel Shanks, *Integer sequences having
  prescribed quadratic character*, Mathematics of Computation24(1970),
  documents prescribed quadratic-sign constructions:
  <https://oeis.org/A002189/a002189.pdf>. Here N1 is proved directly from CRT,
  quadratic reciprocity and Dirichlet's theorem, rather than imported from
  its numerical tables.

All deductions and their limitations are written above. No finite experiment
would certify the infinite normal-family statement, and none is offered as
such a certificate.
