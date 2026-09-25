# Relative arithmetic boundary representations

**Date:** 25 September 2026  
**Status:** proposed research note; written component proofs and exact finite checks, not an independently reviewed RH proof.  
**Central proposal:** study the source-faithful, cutoff-sensitive comparison between arithmetic dilation and additive Fourier geometry. Do not replace this comparison by positivity in a completed auxiliary model.

## 0. What this pass does and does not claim

This note constructs an explicit arithmetic operator system, computes its joint defects, proves a severe obstruction to an attractive prime-completion strategy, and gives exact source-restoration and cutoff-composition laws. It does not prove an RH-sensitive native upper bound or identify the Weil quadratic form with an independently positive norm.

The affine C*-algebra, Cuntz relations, finite Fourier banks, Mellin Plancherel theorem, and the number-theoretic simplicial complex are established mathematics. The proofs here deliberately make the normalizations and source comparisons explicit. No external priority is claimed for the elementary consequences or for the completion obstruction; a literature-priority review has not been completed.

The proposed synthesis is narrower than a general call for “cohomology for RH”: keep the arithmetic representation, all residue channels, the numerical cutoff, its escape maps, and the additive Fourier realization together. A comparison theorem for that specific system would be an advance. Simply naming that missing theorem is not an advance toward RH.

### Repository reading scope

The live reading covered main's README, PROGRAMMES, REFUTATIONS, the structural/family section of CURRENT_RESULTS, issues #763 and #902, recent PR descriptions, the source and Mellin sections of MHB32 in #904 at `8c506696d8ad7772ccaf48fbb8678fcd889e8beb`, and the CQT32 README in #906 at `ddc25eafe85d637b6c7e8a7e276b39e4998fd648`.

It was not a complete repository audit. No existing repository validator or CI suite was replayed. Main and the research branches were not changed. The files in this packet were generated and checked locally.

The MHB32 manuscript is particularly instructive: its exact Mellin form retains a complex square, not an absolute square; its improved bandwidth factor does not reduce the quadratic input-energy exponent. CQT32 already treats completion changes carefully. The present relative construction should be compared with that work, not advertised as the invention of completion accounting.

## 1. The arithmetic representation and the actual source

Let H_Z = l2(Z), with orthonormal basis e_n. Define

\[
Ue_n=e_{n+1},\qquad V_a e_n=e_{an}\quad(a\ge1).
\]

Then U is unitary, each V_a is an isometry, and

\[
V_aV_b=V_{ab},\qquad V_aU=U^aV_a.
\tag{1.1}
\]

For 0 <= r < a put B_(a,r)=U^r V_a. These are the residue-branch isometries:

\[
B_{a,r}^*B_{a,s}=\delta_{rs}I,\qquad
\sum_{r=0}^{a-1}B_{a,r}B_{a,r}^*=I.
\tag{1.2}
\]

These are the standard arithmetic affine/Cuntz relations, not a newly invented algebra. They preserve addition and multiplication simultaneously, rather than retaining an abstract free monoid of prime symbols.

Let P_N project onto e_1,...,e_N. The literal finite Möbius vector is

\[
P_N\prod_{p\le N}(I-V_p)e_1=\sum_{n\le N}\mu(n)e_n.
\tag{1.3}
\]

Proof: expanding the finite product chooses a subset of primes. Its product is squarefree and its coefficient is (-1) to the subset size. Unique factorization identifies the coefficient with mu(n). Terms beyond N are removed by P_N. This is coefficientwise equality, not merely equality of a scalar observable.

No zeros are inserted into a spectrum, no arithmetic phases are randomized, and no convenient replacement for mu is used.

## 2. Full residue channels and the half-density normalization

For j=0,...,a-1 define

\[
W_{a,j}=\frac1{\sqrt a}\sum_{r=0}^{a-1}
 e^{2\pi i jr/a} U^rV_a.
\tag{2.1}
\]

Finite Fourier orthogonality and (1.2) give

\[
W_{a,j}^*W_{a,k}=\delta_{jk}I,\qquad
\sum_j W_{a,j}W_{a,j}^*=I.
\tag{2.2}
\]

Most importantly, the literal arithmetic branch is restored exactly by

\[
V_a=\frac1{\sqrt a}\sum_{j=0}^{a-1}W_{a,j}.
\tag{2.3}
\]

The summands have orthogonal ranges. Thus retaining all channels restores the source without an additional norm loss. Retaining only the zero channel does not.

Write W_a=W_(a,0). Then

\[
W_aW_b=W_{ab}.
\tag{2.4}
\]

Indeed, multiplication of the sums uses V_a U^s=U^(as)V_a, and the integers r+as, 0<=r<a, 0<=s<b, enumerate 0,...,ab-1 exactly.

### 2.1 Exact comparison with real dilation

Define an isometry J:l2(Z)->L2(R,dx) by

\[
Je_n=\mathbf1_{[n,n+1)}.
\]

For a>0 let

\[
(D_af)(x)=a^{-1/2}f(x/a).
\]

D_a is unitary. Direct evaluation on every basis vector gives

\[
D_aJ=JW_a\qquad(a\text{ a positive integer}).
\tag{2.5}
\]

The factor a^(-1/2) is forced by the norm of a union of a disjoint unit intervals. It is not chosen because RH mentions 1/2.

With the Fourier transform Ff(xi)=integral f(x)exp(-2*pi*i*x*xi)dx,

\[
\mathcal F D_a=D_{1/a}\mathcal F.
\tag{2.6}
\]

Equations (2.5)-(2.6) are a genuine finite/infinite-place comparison of dilation normalizations. They are not a trace formula for zeta and do not imply that its zeros are on a line.

### 2.2 The source-restoration cost cannot be omitted

Let R_a=V_aV_a^*, the projection onto multiples of a. Then

\[
R_aW_a=a^{-1/2}V_a,\qquad
\|R_aW_af\|^2=a^{-1}\|f\|^2.
\tag{2.7}
\]

Recovering the literal source branch from the coarse channel therefore multiplies its norm by sqrt(a). This is an exact identity, not a rough estimate. The full bank (2.3) avoids this loss by retaining the other channels.

For a=2, the unnormalized coarse vector is e_2+e_3. Replacing V_2 by that vector preserves the e_2 coefficient only by creating an erroneous e_3 coefficient. A scalar positive model that suppresses this discrepancy is not the arithmetic source.

### 2.3 There is no additive-preserving unitary identification of the two coarse systems

For a>=2,

\[
V_a^*UV_a=0,\qquad
W_a^*UW_a=\frac{a-1}{a}I+\frac1aU.
\tag{2.8}
\]

Proof: U moves a multiple of a into a disjoint residue class. For W_a, shifting a block of a adjacent basis vectors leaves a-1 entries in the original block and moves one to the next block.

Consequently, a unitary that preserves U cannot conjugate V_a to W_a. This obstruction already occurs at one prime. The desired comparison must retain extra channels or use a more general correspondence; it cannot be a source-preserving change of orthonormal basis between the coarse representations.

### 2.4 Composite channels and changes of factor order

Both families {W_(a,j) W_(b,k)} and {W_(b,k) W_(a,j)} are complete orthogonal banks with ab channels. Relative to the common residue branches U^r V_(ab), each is a unitary ab-by-ab matrix. Therefore their change-of-factor-order matrix is unitary, with operator norm exactly one, for all a,b.

The coefficients are explicit. For r+as=t,

\[
W_{a,j}W_{b,k}
=\frac1{\sqrt{ab}}\sum_{r=0}^{a-1}\sum_{s=0}^{b-1}
 e^{2\pi i(jr/a+ks/b)} U^{r+as}V_{ab}.
\tag{2.9}
\]

This includes the nontrivial carry/reindexing phases. It is not legitimate to declare independently chosen scalar channels equivalent under a prime-order swap.

The checker verifies the complete change-of-order matrices for (a,b)=(2,3),(2,5),(3,5), in exact cyclotomic arithmetic. The universal norm-one result follows from the displayed orthogonal-bank proof, not from those finite examples.

## 3. A source-faithful real realization and its joint defect

Let mathcal R_a be multiplication on L2(R) by

\[
r_a(x)=\mathbf1_{\{\lfloor x\rfloor\equiv0\pmod a\}}.
\]

Define the commuting contractions

\[
S_a=\mathcal R_a D_a.
\tag{3.1}
\]

They obey

\[
S_aS_b=S_{ab},\qquad S_aJ=a^{-1/2}JV_a.
\tag{3.2}
\]

For the first identity, write x=ak+t with 0<=t<1 wherever r_a(x)=1. Then floor(x/a)=k, so r_a(x)r_b(x/a)=r_(ab)(x). The second identity follows by checking a unit-cell indicator.

Each S_a is a partial isometry. Its initial projection is

\[
S_a^*S_a=\mathbf1_{\{0\le\{x\}<1/a\}}.
\tag{3.3}
\]

For a finite prime set P, define the alternating joint initial-space defect

\[
\Delta_P=\sum_{A\subseteq P}(-1)^{|A|} S_{n_A}^*S_{n_A},
\qquad n_A=\prod_{p\in A}p.
\tag{3.4}
\]

It is multiplication by a one-periodic function. On 0<u<1 it is exactly

\[
B_P(u)=\sum_{d\mid P^\#}\mu(d)\mathbf1_{\{u<1/d\}},
\qquad P^\#=\prod_{p\in P}p.
\tag{3.5}
\]

This is an independently defined operator system producing the literal arithmetic signs. No target quadratic form was diagonalized in order to construct it.

For P containing every prime <=y,

\[
B_P(u)=M(\lfloor1/u\rfloor)
\quad\text{a.e. on }[1/(y+1),1].
\tag{3.6}
\]

Only squarefree d<=y can contribute there, and all of their prime factors are in P.

### 3.1 The joint defect is not positive, even for two primes

For P={2,3},

\[
B_P(u)=1-\mathbf1_{u<1/2}-\mathbf1_{u<1/3}+\mathbf1_{u<1/6}.
\]

It equals -1 on (1/6,1/3). Its unit-cell average, however, is positive:

\[
\int_0^1B_P(u)du=1-1/2-1/3+1/6=1/3.
\]

Thus positivity after cell averaging does not establish positivity of the actual joint defect. Any proposed multivariable dilation argument requiring this defect to be positive fails on the literal primes 2 and 3. This does not refute RH: RH does not assert positivity of Mertens sums.

### 3.2 Exact Euler and Mellin realizations

For Re(s)>0, finite integration gives

\[
\int_0^1 B_P(u)u^{s-1}du
=\frac1s\sum_{d\mid P^\#}\frac{\mu(d)}{d^s}
=\frac1s\prod_{p\in P}(1-p^{-s}).
\tag{3.7}
\]

Mellin Plancherel on Re(s)=1/2 yields

\[
\mathcal E(P):=\int_0^1|B_P(u)|^2du
=\frac1{2\pi}\int_{\mathbb R}
\frac{|\prod_{p\in P}(1-p^{-1/2-it})|^2}{1/4+t^2}\,dt.
\tag{3.8}
\]

There is no infinite Euler-product exchange in this calculation. For nonempty finite P, B_P vanishes near u=0, since sum_(d|P#)mu(d)=0.

For P={p:p<=y}, the native head in precisely the repository's unbalanced Mertens energy is

\[
\int_{1/(y+1)}^1|B_P(u)|^2du
=\sum_{k=1}^y\frac{M(k)^2}{k(k+1)}=:E_y.
\tag{3.9}
\]

The full norm in (3.8) includes an additional, non-native completion tail. The next section proves that this distinction is enormous, even after every composite term of the finite Euler product is retained.

## 4. Finite-prime completion has catastrophic full energy

**Theorem 4.1.** Let P_y consist of all primes <=y and define mathcal E(P_y) by (3.8). There is an absolute c>0 such that, for all sufficiently large y,

\[
\mathcal E(P_y)\ge \frac1{40\log y}
 \exp\!\left(c\frac{\sqrt y}{\log y}\right).
\tag{4.1}
\]

In particular this energy grows faster than every fixed power of y. The completed source agrees with the literal Möbius source through y. The obstruction is its artificial far tail, not a contradiction to RH.

### 4.1 A uniform resonant interval

Let

\[
I_y=\left[\frac{31\pi}{32\log y},\frac{33\pi}{32\log y}\right],
\qquad F_y(s)=\prod_{p\le y}(1-p^{-s}).
\]

For t in I_y, write theta_p=t log p and z_p=p^(-1/2)exp(-i theta_p).

If p^(31)>=y^(16), then theta_p lies between pi/2 and 33pi/32, so cos(theta_p)<=0 and log|1-z_p|>=0.

If p^(93)>=y^(64), then theta_p lies between 2pi/3 and 33pi/32. Thus cos(theta_p)<=-1/2, and

\[
|1-z_p|^2\ge1+p^{-1/2},\qquad
\log|1-z_p|\ge\frac1{2\sqrt p}-\frac1{4p}.
\tag{4.2}
\]

The last inequality uses log(1+x)>=x-x^2/2 for x>=0.

For the remaining small primes, use |1-z_p|>=1-p^(-1/2) and

\[
\log(1-x)\ge-2x\quad(0\le x\le1/\sqrt2).
\tag{4.3}
\]

For completeness, log(1-x)+2x is concave. On [0,3/4] its two endpoint values are 0 and 3/2-log(4)>0, because integrating the chord bound for the convex function 1/t gives log(2)<3/4. Also 1/sqrt(2)<3/4. This proves (4.3).

Consequently, uniformly on I_y,

\[
\log|F_y(1/2+it)|\ge L_y,
\tag{4.4}
\]

where

\[
L_y=
\sum_{\substack{p\le y\\p^{93}\ge y^{64}}}
\left(\frac1{2\sqrt p}-\frac1{4p}\right)
-2\sum_{p^{31}<y^{16}}\frac1{\sqrt p}.
\tag{4.5}
\]

No phase is selected independently for different primes. The same real t works throughout one explicit interval.

For y>=128, t<=1 on this interval: pi<4 and log(y)>=7log(2)>14/3 suffice. Its length is pi/(16log y). Equation (3.8) therefore gives the effective implication

\[
\boxed{\mathcal E(P_y)\ge\frac{\exp(2L_y)}{40\log y}}.
\tag{4.6}
\]

The lower bound uses only one positive-t interval, so no missing symmetry factor is needed.

### 4.2 The asymptotic growth

For all sufficiently large y, primes in [y/2,y] satisfy the positive condition in (4.5). Their number is asymptotic to y/(2log y), by the classical prime number theorem. Each contributes at least 1/(4sqrt y). The negative sum is at most

\[
2\sum_{n\le y^{16/31}}n^{-1/2}\le4y^{8/31}.
\]

Since 8/31<1/2, this is lower order than sqrt(y)/log(y). Hence L_y >= c_0 sqrt(y)/log(y) eventually. Substitution into (4.6) proves the theorem.

This asymptotic proof uses a standard PNT input, not RH. The finite certificate below does not use PNT.

### 4.3 Exact finite certificate at y=1,000,000

`completion_certificate.py` finds the primes by an integer sieve and performs every sign test with integer powers, not rounded logarithms:

- small-prime test: p^31<y^16;
- positive-prime test: p^93>=y^64;
- square-root bounds: floor(sqrt p), ceil(sqrt p), computed by integer square root;
- every contribution rounded downward to a dyadic rational with denominator 2^40.

It obtains the rigorous lower bound

\[
L_{10^6}\ge \frac{45547501421928}{1099511627776}>\frac{207}{5}=41.4.
\tag{4.7}
\]

The prime groups have sizes 204, 1391, and 76903 (small, middle, large). They total 78498.

The strict decimal energy conclusion uses positive rational Taylor sums, not a floating-point exponential. The checker verifies

\[
\sum_{k=0}^{80}\frac{14^k}{k!}>10^6,
\qquad
\sum_{k=0}^{220}\frac{(414/5)^k}{k!}>560\cdot10^{33}.
\]

The first gives log(10^6)<14. Combining the second with (4.6)-(4.7) gives

\[
\boxed{\mathcal E(P_{10^6})>10^{33}.}
\tag{4.8}
\]

An independent Möbius sieve, authentication of every coefficient through the Dirichlet inverse identity mu * 1 = delta up to 1,000,000, and outward dyadic summation give the native head enclosure

\[
\frac{1828822886912}{1099511627776}
\le E_{10^6}\le
\frac{1828823881550}{1099511627776}<2.
\tag{4.9}
\]

The endpoints display as approximately 1.6633047261 and 1.6633056308, respectively; the rational endpoints, not those decimals, are the certificate. The same computation gives M(10^6)=212.

Thus the non-native completion tail alone has energy greater than 10^33-2. This is a particularly strong warning against trying to bound the native prefix by the full norm of a prime-complete, otherwise attractive positive model.

Small finite-prime experiments are misleading here. Full exact energies through the first twenty primes grow only from 1/2 to about 5.4150; those computations never reach the asymptotic danger. The separate resonance certificate does not enumerate the 2^78498 divisors of the million-scale primorial.

## 5. The relative cutoff object and its exact composition law

Return to the native positive-index subspace of l2(Z). Let

\[
T_{a,N}=P_NV_aP_N,\qquad E_{a,N}=(I-P_N)V_aP_N.
\tag{5.1}
\]

E_(a,N) is the escape map: it records the part of an actual dilation crossing the actual integer cutoff. It is not reconstructed from a desired covariance matrix.

### 5.1 The first-exit cocycle

For all positive integers a,b,

\[
E_{ab,N}=E_{a,N}T_{b,N}+V_aE_{b,N}.
\tag{5.2}
\]

Proof: insert P_N+(I-P_N) between V_a and V_b. Once an index exceeds N, a positive integer dilation cannot return it to the prefix. This gives (5.2).

The two right-hand images are orthogonal. The first is supported in (N,aN]; the second is supported above aN. Therefore, for every native input x,

\[
\|E_{ab,N}x\|^2
=\|E_{a,N}T_{b,N}x\|^2+\|E_{b,N}x\|^2.
\tag{5.3}
\]

This is an exact Pythagorean composition law. Iteration gives

\[
E_{a_1\cdots a_r,N}
=\sum_{i=1}^r V_{a_1\cdots a_{i-1}}E_{a_i,N}
 T_{a_{i+1}\cdots a_r,N}.
\tag{5.4}
\]

For a fixed ordered factorization the summands have orthogonal images: they classify the unique first exit while applying the factors from right to left. Different ordered factorizations give the same full escape map, hence exact coherence relations between their decompositions.

This does NOT make different source monomials orthogonal. Summing many products with Möbius signs retains cross terms. The distinction is essential.

### 5.2 An exact positive block kernel, including mixed primes

Let g=gcd(a,b), a'=a/g, b'=b/g. Then

\[
\boxed{E_{a,N}^*E_{b,N}
=T_{b',N}T_{a',N}^*-T_{a,N}^*T_{b,N}.}
\tag{5.5}
\]

Proof: V_a^*V_b=V_(b')V_(a')^*. Insert P_N+(I-P_N) in the compressed product. A division that remains nonzero sends a positive prefix index downwards, so the first compressed term factors as written. The remaining term is exactly E_a^*E_b.

Explicitly, E_a^*E_b sends e_(a'k) to e_(b'k) for

\[
\frac{N}{\operatorname{lcm}(a,b)}<k\le
\frac{N}{\max(a',b')},
\tag{5.6}
\]

and is zero on all other basis vectors. Its exact rank is

\[
\left\lfloor\frac{N}{\max(a',b')}\right\rfloor
-\left\lfloor\frac{N}{\operatorname{lcm}(a,b)}\right\rfloor.
\tag{5.7}
\]

For any finite family of input vectors x_a,

\[
\sum_{a,b}\langle x_a,E_a^*E_bx_b\rangle
=\left\|\sum_a E_ax_a\right\|^2\ge0.
\tag{5.8}
\]

Thus the COMPLETE operator-valued kernel is positive, although its off-diagonal entries are partial shifts and need not be individually positive or Hermitian.

At N=12, a=2, b=3, the defect maps e_6 to e_9 and e_8 to e_12. It has rank two. Dropping the boundary term would already produce a false identity in this small example.

### 5.3 Completion as a relative class, not a free favorable representative

On the Mellin side, two finite-prime completions containing every prime <=y agree on [1/(y+1),1]. Their difference lies in the tail subspace L2((0,1/(y+1))). The quotient norm by that tail is exactly the native E_y norm in (3.9).

This quotient removes arbitrary completion energy honestly; it does not reduce the unknown native norm. The restriction maps from a larger cutoff to a smaller cutoff form a compatible system. Proving good growth of its actual classes is still a missing analytic theorem.

On the operator side, (5.2)-(5.8) record exactly what changes at the boundary. This is why the relative formulation is more informative than taking a full prime-product norm and hoping its positivity transfers.

## 6. Fourier images of the source masks are exact, but not scalar

The spatial masks obey

\[
\mathcal R_a\mathcal R_b=\mathcal R_{\operatorname{lcm}(a,b)}.
\tag{6.1}
\]

Their Fourier coefficients, with period a, are

\[
\widehat r_a(0)=1/a,\qquad
\widehat r_a(m)=e^{-\pi i m/a}\frac{\sin(\pi m/a)}{\pi m}\quad(m\ne0).
\tag{6.2}
\]

Consequently, Fourier conjugation sends mathcal R_a to an operator made of rational-frequency shifts m/a with these exact complex coefficients.

A precise interpretation avoiding unjustified absolute convergence is to use Fejér sums:

\[
\mathcal F\mathcal R_a\mathcal F^{-1}
=\operatorname{s-lim}_{M\to\infty}\sum_{|m|\le M}
\left(1-\frac{|m|}{M+1}\right)\widehat r_a(m)\,\tau_{m/a},
\tag{6.3}
\]

where (tau_h f)(xi)=f(xi-h). The Fejér approximations of r_a lie in [0,1] and converge almost everywhere, so the multiplication operators converge strongly by dominated convergence; unitary Fourier conjugation preserves that convergence.

This shows precisely how the native residue projection produces a coherent rational-frequency family. Its different denominators cannot be independently reweighted without changing the source. Products of the FULL Fourier images inherit the exact lcm projection identity (6.1).

These identities do not say that the repository's selected rational-angle windows commute with Mellin projection. No such commutation is asserted. An adapter to those particular kernels must retain the cutoff, the source, the centering term, and the full phase.

## 7. Why an ordinary finite trace is the wrong positivity model

Suppose the full arithmetic algebra admitted a finite normalized tracial state tau. From the residue relations,

\[
1=\tau(I)=\sum_{r=0}^{a-1}\tau(U^rV_aV_a^*U^{-r})
=a\tau(V_a^*V_a)=a,
\]

a contradiction for a>1. This is an elementary consequence of the classical Cuntz relations, not a new classification theorem.

The appropriate positive state in the established affine-algebra theory is nontracial: for the standard dynamics sigma_t(V_a)=a^(it)V_a, sigma_t(U)=U, the canonical KMS state has phi(V_aV_a^*)=1/a and phi(V_a^*V_a)=1. The relation between these two values is exactly the residue-density asymmetry.

For a state satisfying a beta-KMS condition for this fixed dynamics, the KMS identity would give phi(V_aV_a^*)=a^(-beta). Summing the a residue projections forces a^(1-beta)=1, hence beta=1. Cuntz proves the existence and uniqueness statements in the cited primary paper; this note only uses the displayed elementary normalization consequence.

This is not a reason that RH is already true. A positive bulk state and an arithmetic boundary evaluation are different functionals. The positive average and negative pointwise joint defect in Section 3 are a small exact demonstration of the distinction.

## 8. Screening a literal factorization-cohomology proposal

The following test is useful precisely because the result is simple, not because it supplies a new proof of RH.

Let K_x consist of finite prime sets S with product(S)<=x, including the empty face in augmented degree -1. This is Björner's number-theoretic complex. Its reduced Euler characteristic is -M(floor x).

There is a transparent compatible filtered chain basis. For each odd squarefree n with prime set S, let

\[
b_S=e_{\{2\}\cup S},\qquad c_S=\partial b_S
=e_S-e_2\wedge\partial e_S.
\]

Then partial(c_S)=0 and partial(b_S)=c_S. Every other face in c_S has weight 2n/p<n. Thus c_S is born at n and b_S at 2n. The basis change is triangular with diagonal one, over the integers, and splits the augmented filtered chain complex into two-term interval complexes [n,2n) in degree omega(n)-1.

This is a persistence-level description compatible with Björner's known Betti formulas; no external novelty is claimed. Every inclusion K_x->K_(2x) induces zero on reduced homology. Nevertheless the number of active bars is of order x and their signed count is M(x).

In particular, “show the factorization homology is eventually killed” would not prove RH: it is already killed within a factor-two change of cutoff. The missing information is the quantitative signed arithmetic behavior, not the mere lifetime of the topological classes.

The checker verifies the chain identities and the Euler/barcode identity through 4095. At that cutoff there are 831 active bars but M(4095)=-19. This is another reason not to call a large positive model or simple abstract homology a solution of the source problem.

## 9. What the proposed theory should try to construct next

The working object is the compatible system of

\[
\bigl(U,\{V_a\},\{W_{a,j}\},J,\mathcal F,
\{\mathcal R_a\},\{P_N\},\{E_{a,N}\},\{\Delta_P\}\bigr),
\]

with the exact relations proved above. It is not yet a Hodge theory, a motive, a cohomology with purity, or a Hilbert–Pólya operator.

The next substantial construction should be a **source-faithful, relative Fourier comparison**. It must compare the integer-cutoff joint-defect source with its full additive Fourier image without paying for the artificial prime-completion tail or dropping residue channels. The positive state used to control the comparison must be specified, along with its change-of-state cost to the actual source.

Three concrete promotion tests follow.

1. **Finite source comparison first.** Produce an exact operator-level comparison at a fixed finite prime set and variable numerical cutoff. It must reproduce both native coefficients and all entries of the boundary kernel (5.5), including the two-prime negative-defect and coarse-channel controls. A determinant match alone is insufficient.
2. **A genuine scale theorem.** Prove a quantitative statement for adjoining a prime or changing the cutoff on the actual relative object, using its Fourier recoupling and first-exit identities. A generic coefficient norm bound, an averaged state bound, or an assumed RH-equivalent bound is not the requested theorem. The theorem may be weaker than RH, but it must improve a source-specific quantity that is currently not controlled.
3. **Only then connect to an RH consumer.** Transfer the new scale theorem to a native energy, a complete Weil form, or an equivalent accepted criterion with every source and endpoint correction retained. The presence of an RH criterion at this last step is normal; treating it as the new mechanism would not be.

Potentially helpful independent tools are weighted operator correspondences, nontracial Hilbert-space geometry, exact multiresolution refinements, and relative versions of Fourier/Poisson comparison. These are research directions, not hidden assumptions in any theorem above.

The finite-prime completion theorem is a stop condition: a candidate whose only positivity lives in the full norm of B_(P_y) cannot provide a useful native bound by monotone domination. The bound exceeds 10^33 while the actual million-scale head is below 2. Any repair has to explain, mathematically, how its relative comparison avoids that cost.

### 9.1 Twists are literal source operations

For a completely multiplicative coefficient system chi, the same finite expansion gives

\[
P_N\prod_{p\le N}(I-\chi(p)V_p)e_1
=\sum_{n\le N}\mu(n)\chi(n)e_n.
\]

Thus Dirichlet-character twists can be retained member by member in the same operator and cutoff system. This is an exact coefficient identity, not a GRH theorem or a family-average transfer. Vanishing character values and missing Euler factors must remain explicit.

## 10. Scope of the conclusion

This pass supplies an explicit object with several independently meaningful operations; a uniform first-exit law; a full mixed-boundary Gram identity; exact source recovery; a joint-defect realization of the finite Euler product; and an analytic/exact-arithmetic obstruction to naive prime completion.

It does **not** supply a smaller native energy exponent, a new zero-free half-plane, a proof of RH, or a demonstrated shortening of the remaining proof. The proposed framework earns further investigation only if its next comparison or scale theorem does something the scalar formulations do not already do.

That is the intended change of research objective: construct a quantitative arithmetic comparison mechanism, rather than add another equivalent scalar endpoint or another abstract positivity model.
