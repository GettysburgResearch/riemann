# Independent review of the gcd coefficient and its common row sequence

Reviewer: `fractional_native`, independently of the note's author.

**Verdict: PASS within the stated source-dependent scope.** I reviewed
the exact gcd grouping and the analytic argument in Sections 3--5, and
checked their stated component consequences. I found no unresolved
mathematical issue in this deduction. It remains a component theorem:
the note does not prove its complementary tail or a new zero-free
region.

## Exact reviewed bytes

| File | Bytes | SHA-256 | Git blob |
|---|---:|---|---|
| `GCD_NATIVE_COEFFICIENT.md` | 23,719 | `515e0cc01061507d1de50f8dab73424c82f97d8c9db67e2201213ae046bb7c45` | `2cac689a44863471e9a46576e096c45e93d89a35` |
| `check_gcd_native.py` | 12,228 | `82f35606a0d220e3053e225c6d6f0495d26c4125eee14e1a34bf2a5dc7f18ee0` | `e69128edb0e5af8911df565bc5933e6b53d7291b` |

Reporting-only authentication update: at root's request, native_gain
renamed the output key to `cases_with_a_above_both_cutoff_scales` and
replayed the amended checker under `python -O`. No acceptance predicate,
calculation, or count changed. The checksum above includes that
five-byte reporting correction; the independent mathematical verdict is
unchanged.

The author initially supplied a note hash before its status-header
update. The hashes above bind this review to the current bytes actually
read, including the reference to the parent's separate review. This
file does not replace or modify `REVIEW_GCD_NATIVE_COEFFICIENT.md`.
No remote publication or mathematical commit authentication is asserted
by these local Git blob hashes.

## What was independently checked

### Exact grouping and full support

The smooth identity
$\mu=m_1+m_2-m_1*m_2*1$ is exact through the product of the two
agreement ranges; for equal cutoffs this is the note's
$\mu=2m_y-m_y*m_y*1$. The full smooth outer coefficient is supported
through $4y^2=8D$. It is legitimate to retain all of that support after
reflection. A term with original outer norm above $2D$ is zero only
after its entire dual sum has been recombined. Truncating such terms
before gcd grouping would change the coefficient and invalidate the
subsequent Euler factorization.

For $r=da,n=db,(a,b)=1$, the product of original and primitive
conjugate character values is exactly
$\psi_u(a)\overline{\psi_u^*(b)}1_{(d,P_u)=1}$.
This uses unit modulus only on the genuine unit support. The common
extra puncture remains on $a$ and $d$; it is not imposed falsely on the
primitive dual variable $b$. The ratio kernel loses $d$ precisely
because $Nn/Nr=Nb/Na$.

### The three-way prime allocation

On $(a,P)=1$, write $a=a_1a_2^2$ with the displayed squarefree and
coprimality conditions. At primes in $a_2$, both Möbius factors must
contain the prime. At each prime in $a_1$, the exact condition “at
least one factor” is the sum of the two single-factor conditions minus
their intersection. The three allocations $l,r,h$ in equation (12)
therefore retain every legal pair, including repeated-prime terms.

The forced divisors are $d_L=a_2lh,d_R=a_2rh$. I checked both

\[
 \frac{Na}{Nd_LNd_R}=\frac1{Nh}
 \quad\text{and}\quad
 (-1)^{\omega(h)}\mu(d_L)\mu(d_R)=\mu(a_1).
\]

No additional restrictions $(x,z)=1$, $(x,r)=1$, or $(z,l)=1$
may be inserted after $h_1=d_Lx,h_2=d_Rz$. The harmonic sums
in the note impose exactly the correct separate restrictions.

### Scalar reciprocal control and the shifted harmonic formula

The zero-free premise used here is only for the scalar
$\zeta_E$, because the gcd character has canceled. It is not a
zero-free theorem for the angular row family.

For fixed $\beta>\beta_0$, the logarithmic disk argument in
Section 4.1 is valid. At large height the disk avoids the pole at one;
its Euler-normalized logarithm is bounded on the radius-one disk.
Borel--Caratheodory and three-circles with fixed interior radii turn
polynomial strip growth into a subpower reciprocal bound. On bounded
heights the reciprocal extends holomorphically across the pole with a
zero, so compactness is the correct remaining argument.

The Mellin formula
$\widehat w(s)=-s^{-1}\int_1^2w'(x)x^s\,dx$
has just the pole at zero with residue one, and has rapid vertical
decay away from that pole. In shifting to
$\operatorname{Re}s=\beta-1$, the pole is canceled by the simple
zero of $F_{Pd}(1+s)$ at $s=0$. The finite deleted Euler products
are regular and nonzero there. No unmentioned residue survives.
The horizontal estimates are uniform in the common fixed strip.

This proves the exact, absolutely convergent formula (19) even when
the harmonic scale is below one. An empty original sum is represented
by an integral equal to zero, rather than by an ad hoc change of
contour or removal of a local term.

### Separation of the row-dependent puncture

On the actual natural support, $(a,P)=1$ implies $(d_L,P)=(d_R,P)=1$.
Consequently the identity
$F_{Pd}=F_PE_d$ is exact. It would be false without this
coprimality condition; the retained original zeros are what license it.

After substitution, $\mathcal B_a(s,z)$ is independent of the physical
row for fixed contour points. Its norm factors are
$(Na\,Nh)^{1-\beta}/Nh$, leaving
$(Na)^{1-\beta}(Nh)^{-\beta}$ per allocation.
The finite Euler factors and allocation count are divisor-bounded
uniformly in both heights. All dependence on $P_u$ is confined to
the two scalar factors $F_{P_u}(1+s)F_{P_u}(1+z)$.
Their uniform absolute bound is integrable against the two Mellin
densities. Thus a common divisor-bounded column sequence is actually
obtained; a merely pointwise coefficient estimate is not being treated
as a uniform large-sieve operator norm.

### Physical rows, puncture divisors, and the small dual scale

The reuse of the full-column sieve has the same scope I audited in
`REVIEW_SIGNED_NATIVE.md`. Fixing the powerful part $v$ leaves squarefree
rows $w$, a common coefficient phase $\chi_a(v)$, and the common mask
$(a,b)=1$ after a dual $b$ is frozen. The primitive values at $b,e$,
root number, and new $F_{P_u}$ factors are bounded row scalars. They
do not become independently chosen column coefficients.

The actual dual scale is $L_0=q_vB\,Ne/D$, while the primitive
conductor remains separate from the puncture. I checked the prefactor
identity displayed after (27): the factor $1/Ne$ cancels exactly
against the actual dual count. Dropping it before choosing the scale
would give a different, incorrect puncture cost.

The bound
$\sum_{L\ {\rm dyadic},L\ge1}L(1+L/L_0)^{-j}\ll L_0$
is valid also for $L_0<1$, by rapid decay with $j>1$.
The finite $e$ sum costs only a divisor factor. The powerful-row
ledger uses the true bound
$\sum_{Nv\asymp V_0}N\operatorname{rad}(v)\ll V_0^{1+\epsilon}$.
Its three terms are the displayed
$U^2B/(DV_0)$, $UB^2/D$, and
$U^{5/3}B^{5/3}/(DV_0^{2/3})$; their dyadic summations give exactly
equation (1).

The integral exchanges occur after the exact coefficient identity, and
the finite rows, finite $a,e$, rapid dual sum, and Mellin majorant do
justify Fubini and Minkowski in that order.

## Checker replay

I ran
`python -O third-pass/check_gcd_native.py`
from the packet's corresponding filesystem location. It passed:

- 98 weighted Heath--Brown identities;
- 3,105 allocation identities, including 495 repeated-prime cases and
  2,767 cases with $a>\max(y_1,y_2)$;
- 30 exact zero-extended character gcd groupings;
- 81 coprime Euler-mask factorizations;
- 2,130 rational exponent predicates.

The deliberately wrong variants were detected: 184 failures from
dropping the both-divisible allocation, 365 from deleting the gcd mask,
649 from truncating the full smooth outer support, 24 from a false
dual puncture mask, 30 from deleting the primitive/natural gcd mask,
and 175 from overlapping Euler-mask factorization.

These tests check finite algebra in a free-prime model and the scalar
arithmetic. The last 2,767-case category is reported by the frozen
checker under the key `cases_with_a_above_both_cutoff_scales`; the actual
predicate is $a>\max(y_1,y_2)$, which need not force every allocation's
harmonic scale below one. The exact counted condition above avoids
that overinterpretation. Subunit harmonic scales do occur in the
finite tests, and the separate analytic argument was checked for
every $X>0$. These tests do not certify the analytic sources.

## Limits of the verdict

The all-scale scalar zero-free premise, full-column sieve, ordinary
functional equation and common smooth calculus remain imported inputs.
I relied on the exact pinned source text and the earlier independently
reviewed native reflection scope; I did not independently re-prove the
entire external zero-free theorem.

The new component is indexed by a reduced gcd-ratio numerator and
contains all original outer product scales coherently. It must not be
identified with the original-product head, far tail, or middle band in
`INVERSE_POWER_COMPONENT.md` or `ASYMMETRIC_HB_TAIL.md`.
Their overlaps would require a separate exact estimate.

At reduced numerator norm comparable to $D$, the extra harmonic factor
is of constant size. The note correctly leaves that complement open.
Its proved component gain and its conditional discussion do not amount
to a full inverse moment improvement, a new zero-free region, or RH.
