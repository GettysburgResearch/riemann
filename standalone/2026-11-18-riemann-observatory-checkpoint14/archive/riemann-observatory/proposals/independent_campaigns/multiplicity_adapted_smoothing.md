# Multiplicity-adapted smoothing: an exact polynomial stress test

Status: independently derived elementary exercise; not a new RH theorem and no novelty claim. Independent review is pending unless recorded separately. Source versions: Burnol math/0103058v2 and Bettin–Conrey–Farmer 1211.5191v1, accessed 2026-11-17.

## Precise research goal and source alignment

Bettin–Conrey–Farmer (BCF), Theorem 2, printed preprint p.3, assume **simple** zeros of a polynomial P, all on or outside the unit circle. If 1/P(z)=sum a_n z^n, their window W_N=sum_{n=0}^N(1-n/N)a_n z^n has squared H² error asymptotic to the number of unit-circle roots divided by N (when that number is positive). Their Theorem 1, p.2, requires RH plus sum_{|Im rho|<=T}|zeta'(rho)|^{-2} << T^{3/2-delta} for some delta>0, which already forces simplicity. Burnol Theorem 1.4, printed p.4, allows multiple boundary roots and gives optimal asymptotic error constant sum m_alpha²|P(alpha)|² for a target polynomial P. These are compatible: an **optimal** polynomial exists for repeated roots, but the BCF particular window need not be optimal without simplicity.

Question: can one adapt the window to multiplicity without losing the sharp constant? First test the smallest forbidden case Q(z)=(1-z)^2, target 1. This is a finite-dimensional approximation question, not an assertion about a multiple zero of zeta.

## Derived proposition E-TOY-001: the original window fails

For every integer N>=1, put

W_N(z)=sum_{n=0}^N (1-n/N)(n+1)z^n.

Then

1-(1-z)^2 W_N(z)=(2/N)sum_{k=1}^N z^k-z^{N+1}.

Consequently its squared norm in L²(S¹,dtheta/(2pi)) is 1+4/N and tends to 1, not 0.

Proof. The reciprocal Taylor coefficients of (1-z)^2 are n+1. Multiplying the window by 1-2z+z² takes its second coefficient difference. This equals -2/N for coefficient indices 1 through N; the coefficient of degree N+1 is 1. The constant coefficient is 1. Subtract from 1. Parseval gives N(2/N)²+1. This calculation also holds at N=1, where the window is just 1.

This is an explicit counterexample to an attempted extension that deletes the word "simple" from BCF Theorem 2 while keeping the same window. It is **not** an error in their theorem.

## Derived proposition E-TOY-002: exact multiplicity-adapted optimum

Let N>=0, L=N+2, D=(L+1)(L+2), and

A_N(z)=sum_{n=0}^N [(n+1)(L-n)(L-n-1)/D]z^n.

Among all complex polynomials A of degree at most N, A_N uniquely minimizes ||1-(1-z)^2 A||². Its residual is

R_N(z)=sum_{k=0}^L [2(2L+1)-6k]/D * z^k,

and its squared error is

||R_N||²=2(2L+1)/((L+1)(L+2)) ~ 4/N.

Proof. Residuals R=1-(1-z)^2 A are exactly degree<=L polynomials satisfying R(1)=1 and R'(1)=0; divisibility of 1-R by (1-z)^2 proves the converse. Parseval identifies norm with sum |r_k|². The minimum-norm coefficient vector with constraints sum r_k=1 and sum k r_k=0 lies in the span of vectors (1)_k and (k)_k. Write r_k=a+bk. The constraint Gram matrix is

G=[[L+1,L(L+1)/2],[L(L+1)/2,L(L+1)(2L+1)/6]].

Its determinant is (L+1)²L(L+2)/12>0 because L>=2. Solving G(a,b)^t=(1,0)^t gives a=2(2L+1)/D and b=-6/D. The squared norm is (a,b)G(a,b)^t=a. Summing the residual coefficients twice gives the stated A_N. Strict convexity, or orthogonality r_j-2r_{j+1}+r_{j+2}=0 for 0<=j<=N, proves uniqueness.

The coefficient window relative to a_n=n+1 is (L-n)(L-n-1)/D, approaching (1-n/N)^2 in the scaling n/N fixed. The exact finite-N correction matters for the minimizer. Burnol's asymptotic constant 2² is recovered without assuming any zeta theorem.

## What is established and what is not

Established here by an elementary proof: the two formulas and optimality for one double root. Independently executable exact rational checks are in experiments/code/multiple_root_smoothing.py. The checks are not the proof and are not interval numerics. General multiplicities, multiple roots, and zeta analogues are not established here. These finite-dimensional facts are likely known consequences of discrete reproducing kernels; novelty was not researched exhaustively.

The connection is mathematically specific: a boundary root of multiplicity m creates m derivative constraints. Burnol's multiplicity-squared constant is a jet Gram-matrix inverse entry; the linear BCF window only has enough endpoint cancellation for the simple-root case. Deleting reciprocal derivative moments in the infinite-zero theorem would require new control of both higher Laurent principal parts and collective tail contributions. A quadratic window that repairs a repeated polynomial root does not establish those controls.

## Next steps and failure tests

1. Derive finite-N optimal windows for (1-z)^m for fixed m, using derivative evaluation Gram matrices (falling-factorial moments), and compare with order-m Cesàro windows. A precise target is the endpoint leverage expression 1-(L!)²/((L-m)!(L+m)!) for L=N+m; this formula is **not proved in this note**.
2. Treat two boundary roots whose angular separation is c/N. Burnol's fixed-distinct-root asymptotic gives separate blocks; at this scale off-diagonal Gram entries no longer vanish. Determine the uniform transition constant and whether it interpolates between two simple roots and a double root.
3. In the zeta setting, formulate a multiplicity-aware residue bound using principal parts of 1/zeta rather than 1/zeta'(rho). Determine an explicit summability hypothesis before contour shifting. This is conditional analysis, not an RH route by itself.
4. Test clustered simple polynomial roots numerically against exact coefficient projection; record condition numbers and validated residual bounds. Main counterexample risk: a window adapted to a repeated root can be suboptimal for separated simple roots.

Significance: useful barrier and testbed for generalized smoothing claims; direct RH significance modest. Difficulty: elementary for a single repeated polynomial root; substantial for uniform root clusters; very high for an infinite-zero arithmetic analogue.
