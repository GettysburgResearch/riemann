# Independent internal review of the thin-band affine interface

Reviewer: `/root`. The author of the reviewed note and checker is
`/root/middle_joint`. I authored the separate detector consumer and
proposed some of the surrounding research questions, but did not write
this determinant/prime derivation or its checker. This is an internal
mathematical review, not external peer review or formal verification.

## Exact reviewed objects

| File | SHA256 |
|---|---|
| `OFF_DIAGONAL_TRANSFER.md` | `e7ea068397e9c3b18e5ac31123d876c81bf3c3f73de0fd0b5a5c551ca2307626` |
| `check_off_diagonal_transfer.py` | `46c7f59ed6acfc3bc2d006f40eac5a54198943fc0a805367fec74fcdfef53a3e` |

**Assessment: pass for the exact identities, elementary resonant bound,
and stated conditional implication. The signed affine estimate remains
open.** The note does not transfer the source's scalar fixed-shift HLC
conclusion to the required Hecke-family expression.

## 1. Coefficient collection and the entire resonant locus

The collected coefficient is the actual divisor convolution
`lambda(n)=sum_(m|n) A(m) Xi(m)`. The bound by the three-factor ideal
divisor function is valid because the original expansion is over
`a b c=n`, with all cutoff magnitudes at most one. It is not legitimate
to replace this coefficient by the original Mobius coefficient; the
note does not do so.

The pair diagonal has its original `1/D` normalization and actual
`|psi_u(n)|^2` mask. Bounded physical-row weight and elementary ideal
counting give its `O(U D^epsilon)` bound.

The equal-sixth-core part is a complete block-square sum for every row,
so its nonnegativity is valid even with complex fixed twists and natural
zeros. The pair count is at most
`C D^(1/3) sum_(Na<=2D) (Na)^(-1/3)=O(D)`. I checked the exponent
`1/6` for each sixth-power multiplier and the stated partial-summation
bound. After the original normalization, all divisor coefficient costs
can be absorbed into `D^epsilon`. This includes unequal columns of the
same sixth-power-free core.

The proof correctly avoids replacing a natural character evaluated at
`a t^6` by its value at `a`: primes in `t` can introduce natural zeros.
The finite checker includes an explicit failure of that replacement.

## 2. The determinant and its two contents

The crossed coordinates `P=(m1,c2)`, `Q=(m2,c1)` give exactly
`det(P,Q)=m1 c1-m2 c2`. The norm bound is `Nh<=8D`, by the triangle
inequality in the complex embedding and `Nn_i<2D`. Since the chosen
generators are primary, their difference is in `3 O_E`. Equality of
norms does not imply equality of these generators or a zero determinant.

The phase identity has the required conjugation on the second endpoint.
Writing `P=gP0`, `Q=lQ0` gives the exact determinant multiplier `g l`.
In the character pair, the two factors at `g l` cancel only to the
natural indicator `1_((gl,P_u)=1)`, not to one. The coefficient arguments
and both norm profiles retain these same contents. The reindexing is a
discrete bijection and introduces no Jacobian.

Thus the source's primitive rational path space cannot simply be used
for the unprocessed native endpoints. The note states both the field
difference and the necessary content ledger.

## 3. Prime extraction and its sign

On this specific band, the short factor has norm below `2 U^.004`
while the product exceeds `U^.735`. Hence the extracted long factor
has norm at least a fixed positive constant times `U^.731`; it is
eventually nonunit. Its upper norm is below `2 U^.773`, whereas the
long cutoff scale is `2 U^(r-.004)`, with `r>=1.16`. Both original
long cutoff functions are identically one on the band. This
simplification does not remove either short cutoff or either Mobius
sign.

The prime-only identity
`mu(b) log Nb = -sum_(dp=b,(d,p)=1) mu(d) log Np`
is valid for both squarefree and nonsquarefree b. The coprimality
condition kills the otherwise erroneous repeated-prime term. Applying
it only to the first long factor yields the exact affine relation
`(a1 d c1) p-(a2 c2) b2=h` and retains the three outer Mobius signs,
the second long Mobius sign, both character orientations and all masks.

The factor `log U/log(Nd Np)` in the common weight is bounded with
the licensed derivative orders on the actual long support. With that
factor included, I checked the overall sign and scale in

`J = Delta - T_U/(D log U)`.

The complete aggregate is real because this is an identity for the
Hermitian squared mean; individual affine summands are allowed to be
complex. The sufficient inequality is consequently a **lower** bound
for `T_U`. A claimed upper bound of the same sign would not control J.
The reviewed note has the correct direction.

The equal-sixth-core portion of the extracted signed aggregate is
`D log U` times a difference of its block-square contribution and the
pair diagonal. Its absolute value is therefore covered by the two
already proved row-volume bounds. No separate per-shift cancellation
is inferred.

## 4. Conditional consumer and unproved interfaces

The target exponent `(1+5r)/6-1/1000` is strictly greater than one
on the full stated r interval, so the elementary diagonal is absorbed
in the proposed moment budget. Chebyshev with the actual buffered
witness threshold then gives the original thin-band count. This is the
same native object used by the separately reviewed detector consumer.

The resulting zero-free boundary remains conditional on the displayed
signed affine input and the imported analytic framework. The HLC paper
does not supply uniformity in the original physical-row sextic twists,
the polynomially many two-dimensional shifts, the anisotropic ideal
boxes, the endpoint contents, or the required full signed aggregate.
The note identifies those gaps explicitly. Inert-prime projective
cardinalities are correctly distinguished from the rational model.

## 5. Independent execution and limits

I read the complete note and checker and independently ran
`python -I -S -B -O check_off_diagonal_transfer.py` from the shared
workspace. It passed. The checker uses actual primary Eisenstein
ideals and exact arithmetic in sixth roots of unity. Its positive
completely additive rational prime weights correctly test the same
prime-extraction identity as logarithms, without presenting a numerical
logarithm approximation as exact arithmetic.

The executed cases include both sextic orientations, non-squarefree
physical rows, repeated primes across the two inverse factors,
nontrivial primitive contents, natural zero masks, and unequal
sixth-core-resonant columns. The acceptance predicates survive
optimization. The adversarial controls make the sign, conjugation,
content, repeated-prime and missing-zero errors observable.

This execution checks finite algebra. The asymptotic ideal-counting
bound is justified by the proof in the note; the open affine bound and
the external analytic framework are not established by these tests.
## 6. Immutable remote-object attestation

After the mathematical freeze was published, I fetched the complete
note and checker from `GettysburgResearch/riemann` at the exact commit
`8b2c6d50ad2d729c681745717c615095bd8f1d9d` through the GitHub file
API. Both returned UTF-8 contents matched the locally reviewed frozen
contents exactly. The remote tree independently matched these blobs:

| Object | Git blob |
|---|---|
| `OFF_DIAGONAL_TRANSFER.md` | `3ead6e25fdb589ae49b65cc98e8f3eb09d77be25` |
| `check_off_diagonal_transfer.py` | `8f425487c8def88e5df0e8c3f78a040b3024dc95` |

The corresponding SHA256 values remain the reviewed values in this
record and `MANIFEST.json`. The exact-commit attestation adds no new
mathematical premise or stronger conclusion. The signed affine lower
bound and the resulting unconditional zero-free statement remain open.
