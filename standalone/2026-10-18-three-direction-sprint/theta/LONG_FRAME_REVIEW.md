# Independent review of the long arithmetic row frame

Reviewed `../eisenstein/LONG_ARITHMETIC_FRAME.md`, actual-byte SHA256
`e049ac3c8dcacf05be3520bc8eef504562573c91683a7944f52a48498ba1d7f0`.
This is an internal component reconstruction, not external referee acceptance.

I independently checked the finite frame proof and its declared source
application, using the pinned paper10/v2 Section7 adjoint and the separately
reviewed unrestricted principal energy. No blocking issue was found at the
explicit squarefree-physical-row, matched-base-section scope.

The frame has no row-profile factor. Its diagonal count retains the full
coprimality mask. Distinct squarefree rows have a nonprincipal good local
character at a symmetric-difference prime, which a fixed S-supported ray
character cannot cancel. Common-prime zeros are retained by divisor
expansion. Primitive planar Poisson gives the stated square-root-conductor
bound at both `X<=NC` and `X>=NC`; the latter uses the absent zero
frequency. Fixed ray restrictions only add fixed constants. After the
`U^(-1)` normalization, the off-diagonal row Schur bound is
`U*(UK)^epsilon`, below the diagonal `K/U` when `K>=U^(2+eta)`.

The inverse identity `F=S^(-1)Psi(Psi*F)` is exact, and its left-inverse
squared norm is `||S^(-1)||`. No column orthogonality, short-label Gram
assumption or assertion that a mainterm lies in the adjoint range is
needed. The smooth target multiplier h and conjugation in (9)--(10)
also match the actual coordinate orientation. Complete conjugation
changes every coefficient and common profile, the sign of the norm
height and the calibration solution; the real response matrix preserves
the stated bounds. In particular the proof
does not divide by a small original row weight.

Restoring the complete unrestricted-label principal energy gives exactly
the stated `U^(4/3)L^(2/3)K^(-1/3)` prefactor and, at the adaptive corner,
`U^(1/15-eta/3+epsilon)` for its synthesis contribution. The ENTIRE
residue vector minus the specified matched mainterm is retained in t,
including all principal terms of unmatched sections and the nonconstant
Type-I error. The separate adjoint contour error also remains in the
exact reconstruction. The generic
contour Cauchy bound still gives `U L K^(1/2)`, hence the displayed
`U^(7/2+eta/2)` cost. Neither it nor the other error is removed by the
frame identity.

Finally the cumulative-phase example is a valid check: the row phase
is unitary, the new smooth adjoint profile has zero raw residue Mellin
value, and the physical norm remains unchanged. Thus the file correctly
distinguishes a paid principal component from a full norm bound.
Unrestricted numerator labels do not eliminate the physical-squarefree
restriction, and other ray sections still need their exact density
match. No full mixed estimate or new zero-free region is certified here.
