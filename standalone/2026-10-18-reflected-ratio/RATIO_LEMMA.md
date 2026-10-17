# Reuse the zero-free rectangle on both sides of the functional equation

Status: proposed component proof, written and checked by one author. No independent referee or formal certification. This lemma is a deduction from classical Hecke functional equations and elementary complex analysis. It is not a hypothesis that all family members are zero-free, nor a new proof of RH.

## 1. Precise family assumptions

Fix a number field F, a finite set S, a finite list of infinity/S types and a unitary finite-order Hecke family. Write chi for a nonprincipal primitive character, with its fixed omitted S Euler factors retained in L^S. The inducing conductor has norm Q <= C U. All constants may depend on F,S, the finite types, the fixed strip margins and arbitrary exponent losses, but not on the individual row or U.

Use the following classical properties: the Euler logarithm is uniformly bounded on every fixed half-plane Re s >= 1+delta; L^S has polynomial growth in U and height on fixed strips; and

  L^S(w,chi)=epsilon_chi G_chi(w) Q^(1/2-w) L^S(1-w,bar chi),        (1)

where |epsilon_chi|=1 and G_chi is the complete archimedean and finite-S ratio. On any fixed closed strip 0<Re w<1, G_chi is bounded by a fixed power of 2+|Im w|. Its inverse is likewise controlled away from its fixed boundary poles. There are only finitely many types. We never identify Q with U, only use the upper bound when its exponent is positive. If chi is originally imprimitive, use its inducing character and carry every omitted Euler factor; the fixed S factors are harmless on these closed positive strips. Arbitrarily many moving omissions outside S are NOT part of this lemma.

For fixed 1/2<sigma<1, suppose this particular row has no zero of L^S(s,bar chi) in

  Re s >= sigma, |Im s| <= 4 U^rho,                     (2)

for a fixed rho>0. This is the defining property of a selected class. No assertion that every row satisfies (2) is made.

## 2. Two-sided bounds from one zero-free rectangle

**Lemma 1.** Fix e>0 sufficiently small in terms of 1-sigma and sigma-1/2. For every lambda>0 and all sufficiently large U,

  |L^S(v,bar chi)| + |L^S(v,bar chi)^(-1)| <= C_(e,lambda) U^lambda (3)

when sigma+e <= Re v <= 1+3e and |Im v| <= 2 U^rho. The same exceptional set (2) works for every lambda.

**Proof.** Center a disk at 2+it, |t|<=2U^rho. Give the outer disk radius
R=2-sigma-e/4, a smaller outer radius r_o=2-sigma-e/2, target radius
r_t=2-sigma-e, and Euler disk radius r_i=1-e/4. For e small enough,

  0<r_i<r_t<r_o<R.

For large U, the outer disk lies in (2), so L has a single analytic logarithm f on it, normalized by its Euler logarithm at the center. The Euler disk lies in Re s>=1+e/4, hence |f|<=C_e there, including on its boundary. Polynomial L growth gives Re f<=C log U on the outer disk (rho and the field are fixed). Borel--Caratheodory, together with the center bound, therefore gives |f|<=C_e log U on the disk of radius r_o. Apply the three-circles theorem to the analytic function f, not to L or 1/L separately. On radius r_t it gives

  |f| <= C_e (log U)^vartheta,
  vartheta=log(r_t/r_i)/log(r_o/r_i)<1.

The horizontal target segment is contained in this disk. Therefore both
exp(Re f) and exp(-Re f) are <=exp(C_e(log U)^vartheta)<=C_(e,lambda)U^lambda.
This proves (3). The large-U condition and constant may change with lambda,
not the exceptional rectangle. Principal characters were excluded so there
is no unremoved pole at one inside the disk. QED.

The two-sided conclusion, rather than merely the reciprocal half, is the point of the new use below. The complex-analysis argument itself is classical and already underlies the repository's reciprocal estimate.

## 3. Reflected numerator / denominator ratio

**Theorem 2.** Under (2), put

  Re s=sigma+3e, Re w=1-sigma-e.                        (4)

For independent ordinates |Im s|,|Im w|<=2U^rho and every lambda>0,

  |L^S(w,chi)/L^S(s,bar chi)|
     <= C U^(sigma-1/2+e+lambda) (2+|Im w|)^C_F.        (5)

The two imaginary parts need not be negatives of one another.

**Proof.** By (1), the numerator contains L^S(1-w,bar chi), which is the SAME character as in the denominator. Its real part is sigma+e and its height is -Im w, so (3) applies. The reciprocal in the denominator is also bounded by (3). Allocate half of the desired lambda to each use. The remaining conductor power is Q^(sigma-1/2+e), with positive exponent. Thus Q<=C U is legitimate. Retain G_chi, the root number and the fixed Euler factors, using their stated height bounds. This proves (5). No equality of the two ordinates, independence of character selection or cancellation between unrelated L-functions is used. QED.

**Selected-family corollary.** If a set of such rows in U<=Na<2U has cardinality O(U^nu), then its sum of absolute ratios has norm exponent

  nu+sigma-1/2+e+lambda.                               (6)

If a correction H_a(s,w,z) is uniformly O(U^lambda) on the same class, it may be inserted, reallocating lambda. This includes the original correction on the enlarged domain read in #971, at the contours in COMPOSITION.md. Nothing in this corollary asserts a moment bound for 1/L on a class containing denominator zeros.

Compared with applying ordinary convexity to L(1-sigma,chi), whose individual exponent is sigma/2, the leading saving in (5) is

  sigma/2 - (sigma-1/2) = (1-sigma)/2.                  (7)

At sigma=3/4 this is exactly 1/8 in the exponent of U. This comparison uses the same zero-free row class. It is not a claim to save U^(1/8) in the complete unselected family.

## 4. Source implications and boundaries

In the CT Poisson summand the numerator is L^S(w,chi_u) and the denominator is L^S(xi,bar chi_u). The conjugate in the functional equation is therefore precisely the one needed. Their ordinates remain independent in the double Mellin integral, which is allowed by (5).

The old correction restrictions 3 Re(xi)>2 and 3 Re(xi)+Re(w)>5/2 would rule out parts of the useful contour. The new application needs #971's explicitly summed correction domain, NOT a substitution into the old domain. With z=1/2 and (4), the enlarged domain has Re(xi+w)=1+2e>1; it crosses neither the mixed pole nor any denominator zero. #975's transverse finite part is not an input.

No numerator fourth, eighth, or all-order moment is needed for (5). The complete composition below retains only the already used second mean for the full good class and for the small-frequency class. The terminal class, which has no zero-free threshold, retains ordinary convexity and the Euler reciprocal to the right of one.

The actual fixed-principal critical energy and generalized native inverse-Mobius moments remain unproved. This is not an exact cancellation of the full physical integrals: only the rowwise estimate (5) is claimed.
