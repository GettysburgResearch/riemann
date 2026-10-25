# Internal review: the coherent overlap and exact remaining corner

Reviewer: `/root/middle_joint`, independently of the author
`/root/coherent_identity`. This is an internal mathematical review, not
external peer review or formal verification of the imported analytic
framework.

Reviewed files:

- `COHERENT_IDENTITY.md`, SHA256
  `5bd8db8047d5474fd2d33c4691d94e9f38f97b7b97b67ad215ee0ac4fb45a068`.
- `check_coherent_identity.py`, SHA256
  `dc31cbdf26e3ac1da2c3917e63b9a42e736909c2ef8e0d9dcf15f6a59189e0ee`.

**Disposition: approved within the expressly stated source scope.** The
overlap estimate and the exact reduction are supported. The remaining
corner estimate is open and must retain that label. No new unconditional
zero-free region follows from this packet alone.

## Independent checks of the mathematical argument

I re-derived the common three-variable Mellin representation. The key
local identity is that the factor `(N r_0)^(-h)` shifts both original
convolution exponents by h. Consequently the harmonic coefficient is
exactly `F_P(1+s+h) F_P(1+z+h) b_a(s+h,z+h)`. There is no leftover
power `(N a)^(-h)`. At a prime and prime square the expression agrees
with the displayed local coefficients, including the repeated-prime
`xy/q` term. This is important: omitting that term or shifting only one
convolution exponent would change the theorem.

The contour order is valid. The initial lines have absolute harmonic
convergence. Moving s,z to positive eta at fixed negative h crosses no
cutoff pole; the following negative h shift keeps both scalar reciprocal
arguments at real part at least beta, strictly above the imported scalar
cap. The zero of the reciprocal at the scalar zeta pole causes no residue.
The finite Euler denominators have positive real arguments, and the far
cutoff Mellin transform is holomorphic on the negative half-plane.

I requested a clarification of the large-frequency tail argument. The
author made it before the reviewed hash above: scalar s,z,h remain on
the globally valid representation's lines, and their large-frequency
tails are estimated using the finite outer polynomial and the family's
absolute w line. Only the remaining low-frequency w integral is moved
inside the shared family buffer. This explicitly avoids assuming a
contour deformation of a sharply frequency-truncated scalar integral.
All actual family arguments contain the sums s+h or z+h and share one
height allowance; scalar global height control is not substituted for a
global family buffer.

The real coefficient factor is `T^(-theta) (2D/T)^eta`; combining it
with the k local factors and the outer shift gives
`(B/T)^theta (B/Nk)^(delta/2)`, up to the allocated subpower. The
P-dependence stays in scalar row factors, and the actual common local
coefficient is preserved. No arbitrary row-dependent column sequence is
submitted to a family moment.

The coprimality inversion retains its exact `1/Nk` weight and true
`(k,P_u)=1` indicator. Inverse ordinary reflection reinstates the
original natural c-character and returns its length to `D/(B/Nk)`.
The primitive e-values and the distinction between conductor and deleted
radical remain intact. Therefore the two same-bin pointwise lengths add
to r, and the coherent harmonic k sum proves the stated dyadic overlap.
This part depends on the joint buffered lemma in `MIDDLE_JOINT.md`,
which I authored; that authorship overlap is disclosed. Its independent
review is recorded separately.

I checked the envelope calculation without using a sampled optimizer.
The permitted r interval lies in the interior radical branch; a legal
delta=1/2 competitor already dominates the printed floor. The gap is
increasing because r<3/2. At r=29/25 the exact comparison is
`58/3 - (26381/6000)^2 = 42839/36000000 > 0`. Hence the claimed
overlap saving is strictly greater than 1/1000 uniformly, including the
smooth transition and fixed multiplicative endpoint constants.

## The exact corner and the limit on the conclusion

The cover uses the actual reflected variables. Since `Na<=R`, a term
with `1-G(R)` nonzero has R<2U and therefore H(a)=1 for
`H(a)=chi(Na/(2U))`. This proves `(1-H)(1-G)=0` term by term.
Monotonicity of the common cutoff gives K<=H. Thus
`1=H+G-KG-(H-K)G` is an exact coherent identity before taking norms.

The complete original outer support through 8D is required and is
present. Terms that vanish only after their full primal ordinary sum
cannot be deleted once a ratio selector has been inserted. The source
far theorem still applies to the complete G piece, while the newly
proved estimate applies to KG. These are genuinely estimates for the
same respective expressions, not inferred intersection bounds.

I independently re-derived the returned corner coefficient:
`D_corner = D_(H,1) - D_(K,G) - A(m) chi(Nm/U)`.
Its sign is correct. The harmonic k bounds yield the two stated scalar
errors; at beta=22/25 their bare exponents are -12/625 and -9/500,
both strictly below -1/60. The critical low returned coefficients
therefore persist with the opposite sign, as stated. This rules out a
false primal support inference, but proves no lower bound for the signed
mean and no impossibility of a future improvement.

The full native 1/1000 saving and the corner 1/1000 saving are equivalent
modulo the three established components by the two directions of the
Hilbert-space triangle inequality. The note correctly leaves the corner
estimate as an open hypothesis. The existing conditional consumer can
receive that hypothesis; its arithmetic premise has not been proved by
the reduction.

## Checker execution

I ran `python -O check_coherent_identity.py` independently. It passed.
The exact checks include three formal local Mellin identities, 256
masked harmonic Euler instances, 20 natural/primitive gcd instances,
1,433 termwise support and selector identities, and 140 corner
coefficient returns. Its negative controls detect a deleted overlap,
missing natural gcd mask, repeated-prime error, and excessive saving.

These finite checks validate algebra and scalar certificates; they do
not verify the external cap, density theorem, functional equation,
Mellin calculus, or the open corner moment. The proof and explicit
premises remain necessary.
