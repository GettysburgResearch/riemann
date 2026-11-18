# Third independent review: clipped polynomial certificates through a small relative HS error

Reviewer: semantic_skeptic. Date: 17 November 2026. Independently reconstructed the claim before reading `audits/adversarial_reviews/hilbert_schmidt_moment_transfer_round3.md`, then compared the exact source argument and polynomial arithmetic. No build or eigenvalue computation is used.

**Conclusion:** the general finite clipping lemma, global Lipschitz constant6 for the specified quartic, exact dimension/count normalization and conditional D-moment consequence are correct. The bridge does not require a limiting spectral law, absence of a zero atom, positivity of F, or higher-moment transfer to G. Its use still requires the actual prime-side moment input and the separately justified block/count geometry.

## 1. General polynomial clipping, including all endpoints

Let q be a real polynomial with q(x)<=0 on x<=0 and q(x)<=1 on x>0. Put h=max(q,-1). Then q<=h<=1_(0,infinity), including x=0, and -1<=h<=1.

The global Lipschitz assertion is valid for **every** such polynomial. A constant q must be<=0 and gives constant h. A nonconstant polynomial bounded above on R has even degree and a negative leading coefficient, hence tends to minus infinity at both ends. Its active set{q>=-1} is compact, with finitely many interval boundaries; |q'| has a finite maximum there. On the complement h is constant, and h is continuous at all boundaries. Partitioning any segment at those finitely many boundaries and applying the ordinary mean-value inequality proves a global Lipschitz bound. If the active set is empty, h is simply constant-1. No derivative bound outside the active set is needed.

This argument is for a fixed q in an asymptotic application. A dimension-dependent q remains valid in the finite inequality, but then its Lipschitz constant must be carried explicitly and controlled.

## 2. Finite Hermitian transfer without an operator-Lipschitz assertion

For Hermitian F,G on the same d>=1 dimensional space, sorted eigenvalues alpha_i,beta_i obey Hoffman–Wielandt:

sum_i(alpha_i-beta_i)²<=||F-G||_HS².

For clarity, this follows from the doubly stochastic eigenbasis-overlap matrix and the rearrangement inequality for sorted real eigenvalues. It includes negative eigenvalues and noncommuting matrices. Cauchy–Schwarz then gives

|Tr h(F)/d-Tr h(G)/d|<=Lip(h)||F-G||_HS/sqrt(d).

These are trace inequalities. No general assertion that a scalar Lipschitz function is operator-Lipschitz is being used.

Since q<=h<=1_(0,infinity), spectral calculus of each individual matrix gives the exact finite inequality

n_+(G)/d
 >=Tr h(G)/d
 >=Tr h(F)/d-Lip(h)||F-G||_HS/sqrt(d)
 >=Tr q(F)/d-Lip(h)||F-G||_HS/sqrt(d).                         (1)

Strict positivity is handled correctly at eigenvalue0 because h(0)<=0. No limiting-law or zero-atom assumption enters(1). Only moments of F through the fixed degree of q appear on its right.

## 3. The explicit quartic and its global constant

Let

p(x)=1-7x/4+2x²/3,

q(x)=1-p(x)²
 =(7/2)x-(211/48)x²+(7/3)x³-(4/9)x^4.

For x<=0, p(x)>=1, so q(x)<=0. For all x, q(x)<=1. Hence the general lemma applies.

Completing the square gives

p(x)=(2/3)(x-21/16)²-19/128,

(p')²=(8/3)(p+19/128).

Where h=max(q,-1) is nonconstant, q>=-1 implies |p|<=sqrt2. Therefore

|q'|²=4p²(p')²=(32/3)p²(p+19/128)
 <=(64/3)(sqrt2+19/128)
 <(64/3)(3/2+19/128)=211/6<36.

The nonnegative factor p+19/128 is ensured by the completed-square identity. Outside the active region h is constant; continuity at its boundaries gives the global Lipschitz bound6. The corners of the clipped function cause no gap in this argument.

Writing m_j(F)=Tr F^j/d and rho=||F-G||_HS/sqrt(d), equation(1) becomes

n_+(G)/d
 >=(7/2)m1(F)-(211/48)m2(F)+(7/3)m3(F)-(4/9)m4(F)-6rho.       (2)

The polynomial expansion, derivative relation and rational inequality211/6<36 agree with the independently inspected exact Fraction record `experiments/results/hs_clipped_certificate_round3.json`.

## 4. Exact block charge and dimension factor

Assume the separate zero-side count inequalities

n_+(G)<=s1+s2+pairs,

N>=s1+2s2+2pairs,

with N>0 and nonnegative counts. They imply s1>=2n_+(G)-N. Put r=d/N. Combining with(2) gives exactly

s1/N>=2r Tr q(F)/d-1-12r rho.                                (3)

The factor r multiplies both the objective and error. It cannot be dropped at finite height or when the limiting dimension ratio differs from1. The actual F and G must live on the same identified finite space and have the stated normalized difference; a law-matched but unrelated model matrix cannot replace F in(3).

For the unbuffered block G0, the charge N refers to the zeros in that same interval. If a buffered count or additional o(N) term is used instead, it must be carried separately rather than silently replaced by this exact formula.

## 5. Single higher-moment combination and its conditional meaning

Suppose along the relevant height sequence

r_T=d_T/N_T->1,

rho_T=||F_T-G0_T||_HS/sqrt(d_T)->0,

m1(F_T)->1, m2(F_T)->4/3.

Define D_T=84m3(F_T)-16m4(F_T). Then the exact polynomial identity gives

Tr q(F_T)/d_T=(D_T-85)/36+o(1).

For every finite real D0 with liminf D_T>=D0, applying(3) and taking lower limits proves

liminf s1_T/N_T>=(D0-103)/18.                                (4)

Equivalently one may write the bound with liminf D_T when finite. No separate convergence of the third and fourth moments is necessary. To simplify an expression containing r_T times the variable D_T, boundedness should be justified rather than assumed: q<=1 gives D_T<=121+o(1), and a finite lower liminf supplies an eventual lower bound. Alternatively, derive(4) directly with the fixed lower bound D0 before taking the limit.

The arithmetic threshold to beat2/3 is liminf D_T>115. If the additional prime-side moments were m3->2 and m4->13/4, then D_T->116, the objective tends to31/36 and(4) yields13/18. This is a **conditional sufficient moment statement**; no such arithmetic bound is proved in this review. A sine-Gram model moment computation does not by itself establish it for the prime matrix.

The normalized Hilbert–Schmidt hypothesis permits rare large negative outliers, and does not transfer arbitrary higher polynomial moments to G0. The clipped certificate avoids that issue by transferring the bounded globally Lipschitz function h and retaining the polynomial moments only on F. A density bound such as(4), even with value1, does not imply RH or exclude isolated/sparse off-line zeros.

For actual zeta counts, a dyadic-window liminf can be passed to cumulative counts by the separately standard additivity/dyadic-summation step. Pure finite-matrix algebra alone does not supply that counting background.

Classification: **Independently checked with no issue found in the inspected portion.** No operator error tending to0, higher-moment comparison for G0, new prime asymptotic, complete source-theorem audit or RH claim is made.
