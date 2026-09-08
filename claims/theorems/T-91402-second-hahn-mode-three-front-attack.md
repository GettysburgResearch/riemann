# T-91402 — The three live fronts meet in the second Hahn/Jacobi mode

Claim ID: `T-91402`  
Status: **RESEARCH SYNTHESIS WITH EXACT NEW LEMMAS; RH UNPROVED**  
Created: 2026-08-12  
Depends on: `L-91401`–`L-91407`; PRs #396, #399, #401  
RH status: **unproved**

## 1. Common finite operator

The beta-binomial Hahn generator has exact eigenvalues

\[
 0,1,\frac52,\frac92,\ldots,
 \qquad \lambda_j=\frac{j(j+3)}4.
\]

The first two modes encode mass and barycenter. The complement begins at the uniform gap `5/2` and is generated physically by adjacent martingale butterflies.

This identifies one common mechanism behind the three leading routes.

## 2. Factor-54 reset

The endpoint butterfly packets are two-moment neutral, so their Hilbert shadow begins in the `j=2` sector and has the uniform resolvent bound `2/5` from `L-91405`.

The remaining issue is not coercivity. It is coefficientwise signed radix-four capacity. `L-91407` proves that this requires a cone-valued full-output margin; ordinary positive target disintegration is insufficient. The decisive finite computation is the exact rational dual margin in that enlarged cone.

## 3. Cauchy/Jordan boundary

The final Green numerator removes low-order storage data and leaves one contact-density boundary. `L-91402` reduces its sign to an explicit knot sequence, while `R-91401` rules out independent one-Green FKG estimates in the small-scale middle regime.

The Hahn result nominates the correct replacement: retain the contact and both Green orders as one degree-two shadow packet and seek its adjacent-edge Schur square. The gap `5/2` supplies a dimension-free inverse once the exact source packet is placed in the two-moment complement.

## 4. Brownian/theta boundary

`L-91406` proves that the beta-binomial Stein variability is exactly the sum of the first two Hahn modes, and that its Beta(2,2) limit is the single quadratic Jacobi mode

\[
 -\frac14(v^2-	frac15).
\]

Thus the arbitrary-phase defect of PR #401 is finite-dimensional after the positive constant-Stein bulk is removed. The remaining Theta–DtN theorem may be attacked as one low-rank Schur complement between

```text
rank-two Brownian boundary bulk;
one quadratic Jacobi port;
the explicit theta variance square.
```

No higher Jacobi mode enters the Stein defect.

## 5. Exact next proof objects

1. **Route A:** an exact signed-detail output-cone/Farkas certificate for the complete factor-54 reset.
2. **Route B:** an explicit degree-two Hahn edge-square identity for the pre-knot Green boundary packet.
3. **Route C:** the finite low-rank Schur matrix coupling the quadratic Jacobi port to the theta variance reserve, followed by a stable `N->infinity` limit.

Any one of these may complete its route. None is delegated to reviewers as an omitted proof; each remains explicitly open.
