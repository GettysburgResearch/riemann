# Scoped internal review of the long arithmetic frame

Reviewed actual file: `../eisenstein/LONG_ARITHMETIC_FRAME.md`.

SHA256: `e049ac3c8dcacf05be3520bc8eef504562573c91683a7944f52a48498ba1d7f0`.

This is a mathematical reconstruction of the displayed component proof,
not external acceptance or a review of a complete RH argument. The
reviewer contributed the principal-coordinate energy input and the
row-unitary gauge remark; those parts are therefore jointly derived,
rather than independently discovered by this review.

The finite frame calculation reconstructs. Physical rows are squarefree,
numerator labels unrestricted, and the unweighted row frame avoids an
inverse of a possibly vanishing original row weight. Its diagonal is
K/U times the positive Euler density. Distinct squarefree rows have
nonprincipal good primitive ratio character of conductor at most O(U^2),
with the common-prime zero mask retained. Primitive Poisson bounds each
off-diagonal entry by a prescribed subpower after the U normalization.
The O(U) row count and Schur bound give off-diagonal operator size
O(U^(1+epsilon)); K>=U^(2+eta) therefore gives the claimed lower frame
bound and inverse norm O((U/K)U^epsilon).

The exact identity F=(Psi*Psi^*)^(-1)Psi*a, a=Psi^*F, and the
left-inverse norm are correct with the file's row/column dimensions.
They justify synthesis of a specified coordinate component without
assuming that component is in the range of Psi^*. The decomposition
a=m+t+e retains BOTH unpaid vectors. In the full source, t includes
every unmatched section's principal part, as well as the nonconstant
Type-I error; it is not assumed to consist only of a base-section error.

The actual adjoint normalization U^(1/6)L^(1/3), its complex conjugations,
and its common product-profile coefficient match the stated primary
paper10 convention. Conjugating a coordinate conjugates the entire
arithmetic head and profile. The real response matrix then gives the
corresponding conjugate calibration solution. Using the unrestricted
true-weight energy input yields exactly the displayed synthesis factor
U^(4/3)L^(2/3)K^(-1/3), not an artificially normalized pole bound.

The two example exponents, 2/3-eta/3 and 1/15-eta/3, reconstruct.
They concern the matched principal component. The generic continuous
estimate still costs U*L*sqrt(K), hence U^(7/2+eta/2) at the corner.
No cancellation between that vector and the Type-I error is supplied.

The row-unitary gauge is also consistent: multiplying the frame by a
puts h*a in the linear adjoint profile; analysis coordinates conjugate
that profile. The cumulative phase has modulus one, is smooth and
equals one at both support ends, and its required Mellin moment is
exactly zero. It preserves the frame spectrum while the contour
remainder can retain the entire hard norm. Thus pole removal alone
does not prove a new operator bound.

No blocking error was found at this precise squarefree-physical-row,
matched-base-section, source-qualified scope. The all-power physical-row
adapter, unmatched principal sections, and both nonconstant vectors
remain explicitly open. No new complete mixed mean or zero-free region
is validated by this receipt.
