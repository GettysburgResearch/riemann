# Exact first four expected sine-Gram moment limits

Proposer: analytic_frontier.17November2026. Status: independent reconstruction supporting the already mapped SG310 claim, with exact finite bookkeeping and separate independent review. No additional theorem ID is introduced. No novelty, arithmetic prime-side moment or RH claim.

Let X be the stationary unit-intensity sine determinantal process withk(t)=sin(pi t)/(pi t),k(0)=1 and correlation densitiesrho_l(x_0,...,x_(l-1))=det[k(x_i−x_j)]. For X_R=X intersect[0,R], letG_R=(k(x−y)) and define

mu_R=(1/R)E sum_j delta_(lambda_j(G_R)).

BecauseE#X_R=R, mu_R is a probability measure. The result is

lim_(R->infinity) integral t^j dmu_R(t)=(1,4/3,2,13/4)_j forj=1,2,3,4.

The source correlation convention/existence input is the same explicitly cited Soshnikov primary source in sine_gram_all_moments_round3.md. This calculation does not claim a new construction of the process or convergence of all its moments.

## 1. Coincidence partitions and justification of limits

ExpandtrG_R^m as an ordered cyclic sum of m point indices, and classify a word by its set partition into l distinct vertices. Label blocks by first appearance. Campbell's factorial-moment formula then integrates each word over ordered distinct coordinates with densityrho_l. There is no additional1/l! factor; each ordered tuple of distinct points corresponds to precisely one assignment to these canonically labeled blocks.

After settingu_j=x_j−x_0, the normalized root-coordinate integration is

w_R(u)=[1−(max(0,u_1,...)-min(0,u_1,...))/R]_+.

It lies in[0,1] and tends pointwise to1. Hadamard's inequality gives0<=rho_l<=1, since the sinc kernel Gram matrix is positive semidefinite with diagonal1. Thus a dominating function is the absolute product of the cyclic trace-edge kernels, with loops removed.

For m<=4 the only such quotient graphs are: one vertex; two vertices with2or4parallel edges; a triangle; a double-edge two-leaf star; or the simple4-cycle. They are all absolutely integrable. In particular|k| belongs toL^p for everyp>1. For the triangle use Young/Hölder withp=3/2. For the4-cycle, |k|*|k| belongs toL² by Young withp=4/3, and the integral is its squaredL² norm. The double-edge star factors into twoL² norms. The remaining cases are simpler. Therefore dominated convergence proves each per-length term has its full-line limit.

Each determinant permutation adds only factors of absolute value<=1, so its terms have the same dominator. All subsequent signed determinant expansions and Fubini interchanges are legitimate; no formal delta-function integration is required.

## 2. Elementary Fourier integrals

Use Fourier transformexp(−2pi itxi), and putb=1_[-1/2,1/2]. Thenk=Fourier_inverse(b), b*b=Lambda(xi)=(1−|xi|)_+, andB=b*b*b is

B(xi)=3/4−xi² for|xi|<=1/2,

B(xi)=(3/2−|xi|)²/2 for1/2<=|xi|<=3/2,

and0otherwise. Parseval/convolution give

A2=integralk²=1,

A4=integralk⁴=integralLambda²=2/3,

A6=integralk⁶=integralB²=11/20,

J222=doubleintegralk(x)²k(y)²k(x−y)²=integralLambda³=1/2,

J331=doubleintegralk(x)³k(y)³k(x−y)=integral_[-1/2,1/2]B²=9/20.

The triangle111 integral is1 byk*k=k; triangle311 isA4=2/3. For4-cycles, the integrals with cyclic edge powers1111,3111,3131,2222 are respectively1,2/3,9/20,2/5. The last isintegralLambda⁴. A4-cycle with a doubled diagonal also has integralA4=2/3, by integrating its two degree2 vertices.

## 3. The remaining K4 graph is a diamond volume

Let

I=tripleintegralk(x)k(y−x)k(z−y)k(z)k(y)²k(z−x)² dxdydz.

Replace the two squared diagonal factors by their inverse Fourier transformsLambda(alpha),Lambda(beta). For fixedalpha,beta, integrate the modulated cycle. OrdinaryL² convolution/Parseval expresses it as the length of the intersection of the four unit intervals shifted by0,alpha,beta,alpha+beta. That length is

[1−|alpha|−|beta|]_+.

For completeness, integratingx first gives Fourier multiplierb(xi)b(xi+beta); integratingz givesb(xi)b(xi−beta). Their product's Fourier convolution at−alpha givesb(xi)b(xi+beta)b(xi+alpha)b(xi+alpha+beta). All these operations are valid inL²/L¹, and absolute integrability of the cycle justifies the preceding Fubini step.

Therefore

I=integralLambda(alpha)Lambda(beta)[1−|alpha|−|beta|]_+ dalphadbeta

=4integral_(a,b>=0,a+b<=1)(1−a)(1−b)(1−a−b) dadb

=11/30.

This graph isK4 with a pair of opposite edges doubled. Relabeling vertices leaves its integral unchanged.

## 4. Third moment

There is one all-equal word, contributing1. The three two-vertex partitions each contributeA2−A4=1/3. The all-distinct triangle timesrho3 contributes

1−3(2/3)+2(1/2)=0.

Thusm3=1+1=2.

## 5. Fourth moment: complete table

The all-equal partition contributes1.

There are four3+1partitions and two contiguous2+2partitions, all givingA2−A4=1/3. The one alternating2+2partition givesA4−A6=7/60. Thus the two-vertex contribution is127/60.

Among the six three-vertex partitions, four merge cyclically adjacent positions and give the same triangle/rho3 integral0. The two opposite-position merges give a double-edge star timesrho3, whose integral is

1−2(2/3)−1/2+2(9/20)=1/15.

Thus the three-vertex contribution is2/15.

For the all-distinct four-vertex partition, expand the determinant by permutation type:

| Permutation class | Count | Sign | Integral per term |
|---|---:|---:|---:|
| identity |1|+|1|
| transposition, adjacent or diagonal |6|−|2/3|
| two transpositions on opposite cycle edges |2|+|9/20|
| two transpositions on the two diagonals |1|+|I|
|3-cycle |8|+|1/2|
|4-cycle aligned with the trace cycle |2|−|2/5|
| other4-cycle |4|−|I|

The total is

1−6(2/3)+2(9/20)+I+8(1/2)−2(2/5)−4I

=11/10−3I=0.

The repeated3-cycle diagram reduces toJ222 by integrating the remaining degree2 vertex; each crossed4-cycle is another relabeling ofK4 with opposite doubled edges. These facts account for every determinant permutation.

Consequentlym4=1+127/60+2/15=13/4. The same expansion givesm1=1 andm2=1+(1−2/3)=4/3.

## Evidence, assumptions and use

experiments/code/sine_gram_fourth_exact.py independently enumerates restricted-growth set partitions and determinant permutations, canonically identifies the undirected multigraphs, and checks all signed rational contributions. It separately integrates the diamond polynomial by the exact formula integral_simplex a^i b^j=i!j!/(i+j+2)!. Observed output is sine_gram_fourth_exact.json. The script verifies bookkeeping and exact finite integrals; the Fourier and dominated-convergence proofs above remain ordinary analysis, not numerical evidence or a Lean theorem.

This closes the pure-model verification of the particular first four values used in the conditional certificate. It neither proves the same values for a zeta prime-side matrix nor proves existence/uniqueness of every higher sine-Gram moment limit. Those remain separate mathematical tasks. The source-specific conditional13/18 certificate remains conditional on its arithmetic interface.
