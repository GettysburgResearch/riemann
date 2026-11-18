# A nonuniform zero-jet limit: two roots at separation c/N

Status: elementary finite-polynomial result derived in this investigation; no novelty claim. Independent review pending. This extends the exact double-root exercise, rather than making any assertion about zeta zeros.

## Source mechanism and precise target

Burnol, math/0103058v2 §2 pp.5–6, obtains independent Cauchy Gram blocks for **fixed distinct** boundary roots, with each multiplicity m contributing m² to the leading prediction-error constant. BCF1211.5191v1 Theorem2,p.3, treats fixed simple roots, with a triangular reciprocal Taylor window. The polynomial question below tests uniformity when two roots approach each other at the resolution scale 1/N. All source roots remain on the unit circle; the approximation target is1 and the measure is dtheta/(2pi).

## Proposition E-CLUSTER-001: exact finite Gram formula

Let N>=0, L=N+2, theta real with theta not in2pi*Z, and

Q_theta(z)=(1-z)(1-exp(-i theta)z).

Let E_N(theta)=inf_{deg A<=N}||1-Q_theta A||²_H²(S¹). Put d=L+1 and S=sum_{k=0}^L exp(i k theta). Then

E_N(theta)=[2d-2 Re S]/[d²-|S|²].

The denominator is strictly positive. The minimizer is unique.

Proof. A residual R of degree<=L comes from an admissible A exactly when R(1)=R(exp(i theta))=1. Evaluation vectors are v_0=(1)_(k=0)^L and v_theta=(exp(-i k theta))_(k=0)^L. They are linearly independent since theta is not a multiple of2pi, so their Gram matrix has determinant d²-|S|²>0. The least-norm vector satisfying both evaluations is in their span. Inverting the 2x2 Gram matrix and applying to (1,1) gives the formula. Complex conjugation conventions change S to its conjugate but leave numerator and denominator unchanged. Strict convexity gives uniqueness. Conversely the two evaluations imply divisibility of1-R by Q_theta, with quotient degree<=N.

## Proposition E-CLUSTER-002: scaled transition

For every fixed nonzero real c,

lim_{N→infinity} L E_N(c/L)=F(c),

where

F(c)=[2-2 sin(c)/c]/[1-(2 sin(c/2)/c)²].

Its continuous extension at c=0 has F(0)=4, while F(c)→2 as |c|→infinity.

Proof. The Riemann sum S/d converges to J(c)=integral_0^1 exp(icx)dx=exp(ic/2)*2sin(c/2)/c. For c!=0, |J(c)|<1 by strictness in the triangle inequality, so multiplying the exact formula by L and taking the limit yields F. Taylor expansions sin c/c=1-c²/6+O(c⁴), (2sin(c/2)/c)²=1-c²/12+O(c⁴) give F(0)=4. Boundedness of sine gives the limit2 at infinity.

At theta=0, Q_0=(1-z)^2. Its exact optimum, independently derived in E-TOY-002, is 2(2L+1)/((L+1)(L+2)); hence the c=0 scaled limit also equals4.

## Noncommuting limits and a precise obstruction

For each fixed theta not in2pi*Z, the geometric sum S is O_theta(1). Therefore L E_N(theta)→2. On the other hand, at each fixed N, the limit theta→0 of E_N(theta) equals the double-root optimum. Expanding S gives

lim_{theta→0}E_N(theta)=[sum k²]/[d sum k²-(sum k)²]
                         =2(2L+1)/((L+1)(L+2)).

Thus lim_{theta→0}lim_{N→infinity} L E_N(theta)=2, whereas lim_{N→infinity}lim_{theta→0} L E_N(theta)=4. A fixed-distinct-root block diagonalization is not uniform down to separations of order1/N. This is an exact mathematical witness against an unjustified exchange of limits, not an error in Burnol's fixed-root theorem.

## Why individual inverse derivatives can be misleading

At either root of Q_theta, |Q_theta'|=|1-exp(i theta)|. Therefore each inverse derivative grows as1/|theta| when the roots coalesce, even though the **grouped optimal approximation error** has the finite transition above. With theta=c/L this is of size L/|c|. The normalized evaluation Gram condition number tends

(1+|J(c)|)/(1-|J(c)|) ~48/c² as c→0.

The 2x2 inverse weights themselves have leading imaginary size6/(d c), so they diverge as c→0 at fixed d scaling, but cancellation between the two evaluation vectors produces a finite jet residual. Exact signs depend on conjugation convention.

This demonstrates the difference between bounding individual simple-root residues absolutely and controlling a whole root cluster. It supplies a reason to investigate clusterwise residue estimates when weakening negative derivative moment assumptions. It does **not** show that the BCF inverse-zeta-derivative hypothesis can be dropped: infinitely many arithmetic clusters, contour tails, and the distinction between additive gamma spacing and logarithmic cutoff still require proofs.

## Next mathematical steps

1. Prove bounds on E_N(theta) uniform simultaneously in N and theta, with explicit constants on |theta|<=c_0/L. The exact expression reduces this to sine inequalities.
2. Replace two roots by a fixed finite cluster theta_j=c_j/L. The limiting Gram kernel is integral_0^1 exp(i(c_j-c_k)x)dx; confluent limits introduce derivative evaluations. State separation-free estimates in a jet basis.
3. Determine whether an explicit reciprocal-coefficient smoothing achieves this cluster transition, or whether the finite Gram minimizer requires knowledge of the root locations.
4. For zeta, formulate a **conditional** bound on grouped principal-part residues that does not grow merely because a fixed cluster is close. First prove the analogous rational-function estimate for finite clusters with uniform constants.

Potential failure: a polynomial approximant allowed to depend on its exact roots need not translate into arithmetically usable coefficients. Uniformity in infinitely many clusters cannot be inferred from any fixed cluster calculation. Significance: useful uniformity obstruction and test model. Difficulty: elementary for two roots; substantial for general confluent clusters; very high for arithmetic transfer.

## Proposition E-CLUSTER-003: the simple-root triangular window is not uniform

For N>=1 let v=exp(-i theta), a_n=sum_{j=0}^n v^j (the reciprocal Taylor coefficients of Q_theta), and W_N=sum_{n=0}^N(1-n/N)a_n z^n. Then, writing T=sum_{k=1}^N v^k,

1-Q_theta(z)W_N(z)=(1/N)sum_{k=1}^N(1+v^k)z^k-(T/N)z^{N+1},

and

||1-Q_theta W_N||²=[2N+2 Re T+|T|²]/N².

Proof. The reciprocal coefficients satisfy a_n-(1+v)a_{n-1}+v a_{n-2}=0, with a_{-1}=0. Taking this difference of the weighted coefficients gives -(1+v^k)/N for1<=k<=N. The coefficient at N+1 is v a_{N-1}/N=T/N; all higher coefficients vanish. This gives the residual identity; Parseval and |v|=1 yield the norm formula. At theta=0 it recovers1+4/N exactly.

For fixed theta outside2pi*Z, T=O_theta(1), and the norm²~2/N as in the fixed-simple-root theorem. However, for each fixed real c!=0, with theta=c/N,

||1-Q_(c/N) W_N||² → |integral_0^1 exp(-icx)dx|²=(2sin(c/2)/c)².

Except when c is a nonzero integer multiple of2pi, the limiting error is strictly positive although both roots are simple at every finite N. The best error at the same angle is O(1/N) by E-CLUSTER-002 (using L/N→1). At exact resonances theta=2pi j/N with j not a multiple of N, T=0 and the triangular window error²=2/N; the exceptional cancellation is genuine, not a contradiction.

This is a second explicit negative result: fixed-simple-root asymptotic optimality cannot be used uniformly for a varying polynomial with root separation comparable to1/N. Any proposed infinite-zero transfer relying on uniformly optimal single-root triangular smoothing must address cluster cancellations. The construction is a moving-polynomial model and does not refute BCF's theorem for zeta or a fixed polynomial.

The function F is not monotone and should not be described as lying between2 and4. For example c=5pi/2 gives F(c)=(2-4/(5pi))/(1-8/(25pi²))<2. These oscillations reflect finite-scale interference between the two evaluation constraints; only the limiting values4 at zero and2 at infinity were claimed.
