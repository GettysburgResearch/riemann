# Controlled negative Ising couplings: a global Fourier strip and a compactness barrier

Status: **PROPOSED complete component theorems; independent review required.**
These theorems enlarge the allowed finite models to include negative pair
couplings. They do not construct a cofinal theta approximation, prove a new
zeta zero-free boundary, or resolve RH.

The disk contraction argument is the classical Asano--Ruelle mechanism.
The proof below gives its elementary disk special case directly. The local
budget, positive-reference comparison, and continuous variance barrier are
derived here for the repository's weighted Fourier normalization. No worldwide
priority claim is made.

## 1. Model and an allocatable band budget

Let G be a finite graph without self-loops, with arbitrary finite real pair
couplings J_e and real fields h_i. Under the probability law proportional to

\[
 \exp\left(\sum_{e=\{i,j\}}J_e\sigma_i\sigma_j+
                  \sum_i h_i\sigma_i\right),\qquad \sigma_i\in\{-1,1\},
\]

put

\[
 Y=\sum_i w_i\sigma_i,\qquad w_i\ge0,\qquad
 \varphi(z)=\mathbb E e^{izY}.
\]

Parallel edges may first be combined by adding their couplings. Fix b>=0.
For every negative edge e={i,j}, choose nonnegative endpoint budgets
\(\alpha_{e,i},\alpha_{e,j}\) satisfying

\[
 \tanh\alpha_{e,i}\tanh\alpha_{e,j}\ \ge\ \tanh|J_e|.       \tag{1}
\]

There is no endpoint cost for a nonnegative edge. Require at every vertex

\[
 |h_i|+\sum_{\substack{e\ni i\\J_e<0}}\alpha_{e,i}
                         \ \le\ b w_i.                  \tag{2}
\]

The budgets can be asymmetric. In particular, a larger observable weight can
pay more of the cost of an incident negative edge. A zero-weight vertex must
have zero field and no incident negative edge. Such vertices, including the
old unobserved hub, are permitted.

A simple symmetric choice is

\[
 \alpha_{e,i}=\alpha_{e,j}
    =\frac12\operatorname{arcosh}(e^{2|J_e|}),             \tag{3}
\]

because \(\tanh^2(\operatorname{arcosh}(c)/2)=(c-1)/(c+1)\).
Thus a sufficient directly computable budget is

\[
 |h_i|+\frac12\sum_{\substack{e\ni i\\J_e<0}}
       \operatorname{arcosh}(e^{2|J_e|})\le b w_i.         \tag{4}
\]

For a single negative edge with no fields, (1)--(2) allow

\[
 \tanh|J_{ij}|\le \tanh(bw_i)\tanh(bw_j).                 \tag{5}
\]

All couplings and probabilities remain finite. Negative couplings are admitted
with a paid zero-band cost, rather than being assigned a Lee--Yang property.

### Theorem A: global strip for the complete finite model

If (1)--(2) hold, every zero of \(\varphi\) lies in

\[
                         |\operatorname{Im}z|\le b.     \tag{6}
\]

There is no restriction on the number of vertices, cycles, or positive
couplings. The result includes every spin configuration.

## 2. Proof of the strip theorem

### 2.1. A two-variable edge

Write c=exp(-2J)>0. Up to a nonzero positive factor, the edge polynomial is

\[
                  p_c(x,y)=1+c(x+y)+xy.                 \tag{7}
\]

If c<=1 it is nonzero whenever |x|,|y|<1. For c<1, the zero in y would be
\(-(1+cx)/(c+x)\), and

\[
 |1+cx|^2-|c+x|^2=(1-c^2)(1-|x|^2)>0.
\]

The case c=1 is \((1+x)(1+y)\). If the denominator is zero when c<1,
the numerator is nonzero and there is no zero in y.

For c>1, let 0<r_i,r_j<1 satisfy

\[
                      1+r_i r_j\ge c(r_i+r_j).          \tag{8}
\]

This implies \(r_i<1/c\) and \(r_j<1/c\). For |x|<=r_i, elementary
minimization of the fractional linear map gives

\[
 \left|\frac{1+cx}{c+x}\right|
 \ge\frac{1-c|x|}{c-|x|}
 \ge\frac{1-cr_i}{c-r_i}\ge r_j.                         \tag{9}
\]

For the first inequality, square the ratio and write
x=r exp(i theta). Its derivative with respect to cos(theta) has the sign of
\((c^2-1)(1-r^2)\), so the minimum is attained on the negative real ray.
The second inequality follows by differentiating the positive real ratio.
Thus (7) is nonzero on the open bidisk of radii r_i,r_j.

Set \(r_i=e^{-2\alpha_i}\), \(r_j=e^{-2\alpha_j}\). Then

\[
 \frac{1+r_i r_j}{r_i+r_j}
 =\frac{\cosh(\alpha_i+\alpha_j)}{\cosh(\alpha_i-\alpha_j)}
 =\frac{1+\tanh\alpha_i\tanh\alpha_j}
        {1-\tanh\alpha_i\tanh\alpha_j}.
\]

Since \(c=e^{2|J|}\), condition (8) is exactly (1).

### 2.2. Disk contraction, including its short proof

Suppose a polynomial is affine separately in x and y, and write

\[
                         P(x,y)=A+Bx+Cy+Dxy.
\]

Other variables can be fixed at any allowed values. Suppose P does not vanish
for |x|<r_1, |y|<r_2. Then its contraction

\[
                              \widetilde P(z)=A+Dz       \tag{10}
\]

does not vanish for |z|<r_1 r_2.

Indeed A=P(0,0) is nonzero. The polynomial
\(P(r_1t,r_2t)=A+(Br_1+Cr_2)t+Dr_1r_2t^2\) has no zeros in |t|<1.
If D is nonzero, the product of its two roots has modulus at least one.
Consequently \(|D|r_1r_2\le|A|\), proving (10). If D=0 the conclusion is
immediate. This argument holds for each fixed choice of every other variable,
and so can be iterated on a multiaffine polynomial.

### 2.3. Contraction gives the actual graph partition function

Give each endpoint incidence of an edge its own variable. Multiply (7) over
the edges. An isolated vertex contributes a factor 1+x_i of radius one.
At a vertex, contract its incidence variables successively, retaining only the
terms in which every incidence is absent or every incidence is present.
The result is precisely

\[
 \mathcal Z(\boldsymbol z)
 =\sum_{S\subseteq V}
       \left(\prod_{\substack{e=\{i,j\}\\
                    |\{i,j\}\cap S|=1}} e^{-2J_e}\right)
       \prod_{i\in S}z_i.                              \tag{11}
\]

This differs from the usual zero-field Gibbs polynomial by the positive
constant exp(-sum_e J_e). The contraction does not remove any physical
configuration: a subset S is exactly its set of up spins. It removes only
the inconsistent incidence assignments introduced by the edge factorization.

By (9)--(10), (11) is nonzero when, simultaneously for every vertex,

\[
 |z_i|<R_i,\qquad
 R_i=\exp\left(-2\sum_{\substack{e\ni i\\J_e<0}}
                                      \alpha_{e,i}\right).   \tag{12}
\]

Spin reversal also gives
\(\mathcal Z(\boldsymbol z)=(\prod_i z_i)
                   \mathcal Z(\boldsymbol z^{-1})\).
Hence it is nonzero if all |z_i|>1/R_i.

For the Fourier observable, take \(z_i=\exp(2h_i+2izw_i)\). The extra
factor \(\exp(-\sum_i h_i-iz\sum_i w_i)\) and the normalization are nonzero.
If all w_i>0, condition Im z>b puts every activity strictly inside (12);
condition Im z<-b puts every activity strictly outside the reciprocal radii.
This proves (6).

For w_i=0, (2) forces h_i=0 and every incident edge to be nonnegative.
Replace each such weight by epsilon>0, leaving all other data fixed.
The same band bound applies. The finite normalized exponential polynomials
converge locally uniformly as epsilon decreases to zero. Hurwitz's theorem
on each exterior half-plane gives either a nonvanishing limit or an
identically zero limit. The latter is impossible since the limit is entire
and \(\varphi(0)=1\). This includes all allowed zero-weight vertices.

## 3. The negative interactions also have an affordable growth cost

Let the positive reference law have the same observable weights, zero fields,
and couplings

\[
 J_e^+=\max(J_e,0).
\]

Write \(C_{ij}=\mathbb E_+(\sigma_i\sigma_j)\), and

\[
 V_+=\mathbb E_+Y^2=w^{\mathsf T}Cw,\quad
 K_-=\sum_{J_e<0}|J_e|,\quad
 H=\sum_i h_i\sigma_i,\quad
 A=\sum_{J_e<0}J_e\sigma_i\sigma_j.
\]

The real symmetric matrix C is positive semidefinite, has diagonal one, and
has nonnegative entries by the zero-field ferromagnetic correlation
inequality. The finite Lee--Yang Gaussian estimate, already proved in
PR #1001's strip theorem S3, is

\[
 \mathbb E_+\exp\left(\sum_i q_i\sigma_i\right)
 \le \exp(q^{\mathsf T}Cq/2),\qquad q_i\ge0.             \tag{13}
\]

For arbitrary signs in the fields, their absolute values can be used on the
right: expand the product of cosh factors and spin monomials, whose reference
expectations are nonnegative. Formula (13) is applied only to the positive
reference, never to the model with negative couplings.

Put \(d_i=\sum_{e\ni i,J_e<0}\alpha_{e,i}\) and \(q_i=|h_i|\).
The endpoint condition implies

\[
 |J_e|
 \le \tfrac12[\log\cosh(\alpha_{e,i}+\alpha_{e,j})
             -\log\cosh(\alpha_{e,i}-\alpha_{e,j})]
 \le \alpha_{e,i}\alpha_{e,j}.                         \tag{14}
\]

For the last inequality, integrate tanh t<=t between
\(|\alpha_{e,i}-\alpha_{e,j}|\) and
\(\alpha_{e,i}+\alpha_{e,j}\). It follows that

\[
 2K_-\le\sum_i\sum_{e\ni i}\alpha_{e,i}^2
          \le\sum_i d_i^2\le d^{\mathsf T}Cd.            \tag{15}
\]

Since d+q<=bw componentwise and C has nonnegative entries,

\[
 2K_-+\tfrac12 q^{\mathsf T}Cq
 \le d^{\mathsf T}Cd+\tfrac12q^{\mathsf T}Cq
 \le b^2 V_+.                                         \tag{16}
\]

Thus the entire negative interaction cost is controlled even if the number of
negative edges grows. No bounded-degree or bounded-total-weight premise was
inserted.

### Theorem B: reference variance and entire growth

Under (1)--(2), with \(v=\mathbb E Y^2\), one has

\[
 \boxed{\quad v\ge V_+\exp(-b^2V_+).\quad}               \tag{17}
\]

Moreover, for every complex z,

\[
 \boxed{\quad
 |\varphi(z)|\le
 \exp\left\{V_+\left(b^2+b|\operatorname{Im}z|
                           +\tfrac12|\operatorname{Im}z|^2\right)\right\}.
 \quad}                                               \tag{18}
\]

Neither statement assumes that the biased observable is centered.

**Proof.** Since |A|<=K_-, and A is unchanged by global spin reversal,

\[
 \mathbb E_+[Y^2e^{A+H}]
    =\mathbb E_+[Y^2e^A\cosh H]\ge e^{-K_-}V_+.
\]

The denominator is at most
\(e^{K_-}\mathbb E_+e^H
 \le e^{K_-+q^{\mathsf T}Cq/2}\).
Division and (16) give (17).

The denominator is also at least
\(e^{-K_-}\mathbb E_+e^H\ge e^{-K_-}\).
For y=|Im z|, the absolute numerator is at most
\(e^{K_-}\exp((q+yw)^{\mathsf T}C(q+yw)/2)\).
Use (16), q<=bw, and nonnegativity of C to bound the exponent by
\(b^2V_++byV_++y^2V_+/2\). This proves (18).

## 4. A continuous construction cannot escape the small-variance branch

Suppose a continuous deformation of finite models satisfies (1)--(2) at a
fixed b, preserves the second moment v>0, and has continuous V_+. Suppose it
starts with zero fields and nonnegative couplings, so initially V_+=v.

If b>0 and \(b^2v<1/e\), (17) traps V_+ below the smaller positive solution
V_- of

\[
                       V e^{-b^2V}=v.                  \tag{19}
\]

Indeed the left side increases up to V=1/b^2 and then decreases, with maximum
1/(e b^2). Inequality (17) excludes the open interval between the two roots,
and continuity prevents crossing it from the initial point. No assertion
that all feasible models belong to this component is made. For b=0 the
budget forces all fields to be zero and all couplings nonnegative.

For the theta normalization, take b=1/3 and use the complete theta source
\(v_\theta<4621/100000\). The explicit barrier

\[
                  V_+<r:=2323/50000=0.04646            \tag{20}
\]

follows from \(e^{-x}\ge1-x\) and the exact rational margin

\[
 r-r^2/9-4621/100000
                       =228671/22500000000>0.           \tag{21}
\]

At any first crossing of r, (17) and (21) would contradict the fixed value
of v. The proof applies to a finite concatenation of graph changes when its
reference variance is continuous, including added zero edges and vertices
of zero observable weight.

Consequently, a cofinal sequence of symmetric models produced in this
continuous component, matching the actual theta moments to unbounded order,
has the uniform entire bound (18) with V_+ replaced by r. Montel, coefficient
identification, and Hurwitz then give zero confinement for the actual
\(\Xi(z)=\xi(1/2+iz)\) in |Im z|<=1/3, and therefore the zeta boundary 5/6.
The cofinal construction is a missing hypothesis, not a result of this note.

The new freedom is explicit: the construction may cross a zero-coupling face
into a controlled negative-coupling region. It must pay (1)--(2), and an
infinite construction must still be established.

## 5. Sharp edge example and exact checks

For a single negative dimer with equal weights w>0 and no fields,

\[
 \varphi(z)=\frac{e^{-2J}+\cos(2wz)}{1+e^{-2J}},
 \qquad J<0.
\]

Its zero band is exactly
\(\operatorname{arcosh}(e^{-2J})/(2w)\), which equals the symmetric bound
(3)--(4). Thus the local edge constant cannot be reduced uniformly.

The finite checker verifies the full incidence contraction against direct
configuration enumeration for several graphs with positive and negative
couplings, using rational values of e^(-2J). It verifies the exact asymmetric
disk-budget identity and the rational variance-barrier margin. Its checks
are finite algebra, not a substitute for the arbitrary-size proofs above.

## Sources and proof dependencies

- J. L. Lebowitz, D. Ruelle, and E. R. Speer, *Location of the Lee--Yang zeros
  and absence of phase transitions in some Ising spin systems*,
  [arXiv:1204.0558v2](https://arxiv.org/pdf/1204.0558), especially the
  Asano--Ruelle framework in Section 2.
- D. Ruelle, *Characterization of Lee--Yang polynomials*, Annals of
  Mathematics 171 (2010), 589--603,
  [primary paper](https://annals.math.princeton.edu/wp-content/uploads/annals-v171-n1-p16-p.pdf).
- PR #1001 at f6beb3774ae7ff5eca4cb046786eae10e4f88abc, theorem S3 in
  standalone/2026-10-18-zeta-specific-family-and-strip/strip/PROOF.md,
  supplies the finite positive-reference Gaussian and correlation inputs.
  The source of the theta variance bound is the present packet's complete
  directed source through order 26, not numerical zeta zeros.

The disk contraction and edge argument are proved directly here. Their
classical provenance is retained rather than described as a new Lee--Yang
theorem. The all-order conclusion is conditional; no theta-matching model
with negative couplings has been certified in this note.

