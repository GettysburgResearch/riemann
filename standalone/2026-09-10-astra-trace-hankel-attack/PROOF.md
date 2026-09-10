# THA26 — positive Gaussian sums, Bernstein structure and the all-rank boundary

Date: 2026-09-10. **Proposed component proofs, requiring independent review.**
This is research, not an integration verdict. The attempted end-to-end RH proof
does not close: the unweighted all-rank inequality in Section 7 is not proved.
No off-critical zero of the actual zeta function is asserted.

The starting observation is the exact whole-xi determinant in PR #834 at
`f0e34780f4fe91bd5d07e791e8855189838c3df5`. Its singular-value operator is positive,
but that does not supply spectral reality. Here we prove more positivity at the
actual source, then test the proposed passage from that positivity to reality.
The numerical zero inputs are explicitly imported, not recomputed.

There is no claim of novelty for Hadamard products, Hamburger moment criteria,
Bernstein theory, or interpolation. Related power-sum criteria for xi already
appear in Ruiming Zhang, arXiv:1510.03420. The present proposed contributions are
the explicit whole-tail reserve/interpolation arguments, their quantitative
source applications, and the tests of the attempted finishing steps.

## 1. Exact source, counting conventions and imported data

Let

\[
 \Xi(z)=\xi(1/2+iz),\qquad
 \xi(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)
\]

with the entire removable values, and let

\[
 \phi(t)=\sum_{n\ge1}(4\pi^2n^4e^{9t/2}-6\pi n^2e^{5t/2})
                             e^{-\pi n^2e^{2t}},\quad
 Z=\Xi(0),\quad w=\phi/Z.
\]

The classical theta representation is
\(\Xi(z)=\int_{\mathbb R}\phi(t)e^{izt}dt\). Jacobi inversion gives evenness;
for t>=0 each summand is positive. Thus w is a positive even probability density
with all exponential moments. Its fixed differentiated tails follow by retaining
n=1 and bounding the rest of the series. These facts and the xi product are
classical source inputs, not conclusions from a finite zero table.

Enumerate every xi zero with **positive real part** as
\(z_j=\gamma_j+i\eta_j\), with analytic multiplicities. These correspond to
zeta zeros of positive ordinate, and \(|\eta_j|<1/2\). The family is invariant
under complex conjugation. One representative for each +/- pair, not a single
representative for a four-zero off-line orbit, enters the following sums:

\[
 \lambda_j=z_j^{-2},\qquad s_m=\sum_j\lambda_j^m\quad(m\ge1),\qquad
 g(t)=\frac{\Xi(i\sqrt t)}{\Xi(0)}.
\tag{1}
\]

The even Taylor series defines g as an entire function: no square-root branch
is introduced. The genus-zero product, with all multiplicities, is

\[
 g(t)=\prod_j(1+t/z_j^2),\qquad
 f(t)=\log g(t),\qquad p(t)=f'(t)=\sum_j\frac1{t+z_j^2},\quad t\ge0.
\tag{2}
\]

The real logarithm in (2) is legal because \(\Xi(iy)>0\) for every real y.
We never presume a global logarithm across unknown complex zeros. Absolute
summability in (1) follows from the classical product or the count bound below.

For the bounded source applications we import:

* the Platt--Trudgian theorem that all nontrivial zeros with positive ordinate
  at most \(H=3\cdot10^{12}\) lie on the critical line;
* one zero in each of the 25 disjoint ordinate intervals in INPUTS.json, each
  of width 1/100, from the LMFDB zeta-zero data. In particular one real zero
  \(\gamma_1\) satisfies \(14<\gamma_1<15\).

Simplicity is unnecessary. The 25 intervals are much wider than the precision
reported by the source. Authentication of our copy does not independently prove
these primitive zero assertions or rerun their producing computation.

For the trace-class operator \(T=-K^2|_{H_o}\) in #834, its determinant identity
implies \(s_m=\operatorname{Tr}T^m\). If \(\kappa_k\) are the cumulants of w,
comparison of \(\log\int e^{ut}w(t)dt\) with (2) gives

\[
 s_m=\frac{(-1)^{m+1}\kappa_{2m}}{2(2m-1)!}.
\tag{3}
\]

The power-sum results below follow directly from the classical source/product;
the operator interpretation additionally uses the precise proposed determinant
and multiplicity theorem of #834. Its full analytic proof and code were not
independently replayed in this packet.

## 2. A self-contained coarse zero count and complete tail bound

### THA26.N: for every real T>=100, N(T)<=T log T

Here N(T) counts all nontrivial zeta zeros with 0<ordinate<=T, including
multiplicities and both members of each off-line pair of positive ordinate.
This deliberately weak estimate is derived here. The sharper published
Hasanalizade--Shen--Wong bounds were consulted as comparison, but are not needed.

**Proof.** First Z>1/100. For 0<=t<=1/10, use
\(3<\pi<22/7\), \(e^{1/4}<4/3\), \(e^{1/5}<5/4\), and e<3.
The n=1 summand is greater than

\[
 \left(36-6\frac{22}{7}\frac43\right)e^{-4}
 =\frac{76}{7}e^{-4}>\frac{10}{81}.
\]

All other summands are positive. Integration over [-1/10,1/10] gives
\(Z>2/81>1/100\). The exponential bounds use
\(e^x<1/(1-x)\) for 0<x<1 and the elementary exponential series.

By positivity and evenness,
\(\max_{|z|\le2T}|\Xi(z)|\le\Xi(2iT)=\xi(1/2+2T)\).
Put a=T+1/4 and k=ceil(a). Splitting the gamma integral at 1 gives
\(\Gamma(a)\le1+\Gamma(k)\le2(T+2)^{T+2}\).
The integral test gives \(\zeta(2T+1/2)\le2\), and the remaining polynomial
prefactor is at most 3T^2. Dropping the factor \(\pi^{-a}\le1\) therefore gives

\[
 \max_{|z|\le2T}|\Xi(z)|\le12T^2(T+2)^{T+2}.
\tag{4}
\]

Each counted zero and its negative have modulus at most
\(\sqrt{T^2+1/4}<(101/100)T\). Jensen's inequality in the disk of radius 2T
therefore implies

\[
 2N(T)\log(200/101)
 \le\log\frac{\max_{|z|\le2T}|\Xi(z)|}{Z}.
\]

The logarithm on the left is >2/3. On the right, using log1200<8,
\(\log(T+2)\le\log T+2/T\), and logT>4 for T>=100, we obtain

\[
 \log1200+2\log T+(T+2)\log(T+2)
 <(T+4)\log T+11
 <(T+27/4)\log T<\tfrac43T\log T.
\]

This proves the claim. Jensen can be obtained by a limiting radius when a zero
is on the outer circle; none of the inner contributions is discarded. The
count is complete, not a sum over the computed low zeros. QED.

Partial summation now gives, for H>=100,

\[
 \sum_{\gamma_j>H}\gamma_j^{-2}
 =-\frac{N(H)}{H^2}+2\int_H^\infty\frac{N(t)}{t^3}dt
 \le\frac{2(\log H+1)}H.
\tag{5}
\]

The omitted upper endpoint is zero because N(T)/T^2 tends to zero. At the
imported height, logH<29, so we may use the exact rational constants

\[
 r=H^{-2},\qquad B=60/H=2\cdot10^{-11}.
\tag{6}
\]

Every possibly nonreal lambda is in |lambda|<=r, and the sum of absolute values
of **all** lambda terms above H is at most B. This is a complete analytic tail
bound, not an assumption that the remaining zeros lie on the line.

## 3. A positive Gaussian zero sum and a genuine Bernstein theorem

Define a scalar spectral sum, not a presumed self-adjoint heat semigroup,

\[
 \vartheta(u)=\sum_j e^{-z_j^2u},\qquad u>0.
\tag{7}
\]

It converges absolutely, locally uniformly in u>0. Its terms may be complex;
conjugate pairing makes the whole sum real. This \(\vartheta\) is not the
original Jacobi theta function or the original density phi.

### THA26.B: positive at every time, with an explicit real reserve

Under the stated finite-height input and the complete tail bound (6),

\[
 \vartheta(u)\ge(1-16B)e^{-\gamma_1^2u}
              >(1-16B)e^{-225u}>0\qquad(u>0).
\tag{8}
\]

Consequently f(t)=log g(t) is a Bernstein function on [0,infinity): it is
nonnegative and its derivative is completely monotone. Precisely,

\[
 (-1)^k p^{(k)}(t)>0\quad(k\ge0,\ t\ge0),\qquad
 g(t)^{-a}\ \text{is completely monotone for every real }a>0.
\tag{9}
\]

These statements do **not** assert that f is a *complete* Bernstein function,
nor that p is a Stieltjes function. Either stronger source property would
require an additional argument; see Section 7.

**Proof of (8).** Keep one unit of the real low-zero contribution as a reserve.
An off-line conjugate pair, of common multiplicity m, contributes

\[
 2m e^{-cu}\cos(du),\qquad c=\gamma^2-\eta^2,\quad d=2\gamma|\eta|<\gamma.
\]

Only a negative cosine needs payment. In that case du>1, so u>1/gamma.
Since gamma>H>=100 and gamma_1^2<225,
\(c-\gamma_1^2\ge\gamma^2/2\). Hence its negative contribution relative to the
reserve is bounded by

\[
 2m e^{-(c-\gamma_1^2)u}\le2m e^{-\gamma/2}\le16m/\gamma^2.
\tag{10}
\]

The last inequality follows from the quadratic term of e^(gamma/2).
Sum (10) over off-line conjugate pairs. Their representative sum is bounded
by the full positive-ordinate sum (5), so 16B is a safe upper payment; no
factor-of-two improvement is needed. All unallocated real and positive-cosine
terms are nonnegative. This proves (8) simultaneously for every u>0.
The reserve is paid once, with constant shares, not reused without accounting.

**Proof of (9).** All real parts of z_j^2 are positive. Also
\(\sum_j1/\Re(z_j^2)<\infty\): below H there are finitely many real nonzero
zeros, and above H the real part is at least gamma_j^2/2. Thus Fubini applies
absolutely to the complex series before positivity is used, giving

\[
 p(t)=\int_0^\infty e^{-tu}\vartheta(u)du,\qquad
 (-1)^k p^{(k)}(t)=\int_0^\infty u^k e^{-tu}\vartheta(u)du>0.
\tag{11}
\]

Every fixed derivative is justified by the corresponding absolutely summable
inverse powers. Integrating in t gives the exact representation

\[
 f(t)=\int_0^\infty(1-e^{-tu})\frac{\vartheta(u)}u\,du.
\tag{12}
\]

Its Levy integrability follows from integrability of vartheta near zero and its
exponential decay at infinity. Both follow from the same absolute sums; no
unproved zero-free half-plane or operator semigroup is required.
For a>0, repeated differentiation of exp(-af) has sign (-1)^k: the Bell
polynomial has positive coefficients in the signed derivatives of -af.
Equivalently, truncating the positive measure a*vartheta(u)du/u gives compound
Poisson Laplace transforms and their limit. Thus all reciprocal powers in (9)
are completely monotone, with the precise **squared-coordinate** t used here.
It is not a claim in the original variable s. QED.

### All scalar traces and all-rank *factorial-weighted* Hankel forms

Integration of (8) gives

\[
 s_m=\frac1{(m-1)!}\int_0^\infty u^{m-1}\vartheta(u)du
     \ge(1-16B)\gamma_1^{-2m}>(1-16B)15^{-2m}>0.
\tag{13}
\]

Thus all even cumulants in (3) have strict alternating signs. As an independent
simpler estimate, keeping the first zero and applying (6) directly gives
\(s_m\ge[1-225B(225/H^2)^{m-1}]15^{-2m}\), also positive for all m.
Neither is a novel general power-sum criterion; these are explicit applications
of a low real reserve and a paid complete tail.

More strongly, for **all** integers d,n>=1 and t>=0,

\[
 \left((n+i+j-1)!\sum_k(t+z_k^2)^{-(n+i+j)}\right)_{i,j=0}^{d-1}\succ0.
\tag{14}
\]

Indeed its real quadratic form is
\(\int_0^\infty u^{n-1}e^{-tu}|P(u)|^2\vartheta(u)du\), positive for every
nonzero polynomial P of degree<d. Complex coefficients follow from the real
symmetric matrix or the same Hermitian integral. In particular the matrix
\(((n+i+j-1)!s_{n+i+j})\) is positive definite at every rank.

**Do not remove the factorials.** They are not a diagonal congruence. Already
\(\det\bigl(1/(i+j+1)!\bigr)_{i,j=0}^1=-1/12\). Entrywise inverse-factorial
multiplication is not a positivity-preserving operation on arbitrary PSD
matrices. The all-rank assertion (14) is therefore not the all-rank RH assertion
in Section 7.

## 4. Complete-tail interpolation: unweighted positivity at bounded rank

Here is a generic useful form of the interpolation argument. Let a summable
conjugation-invariant multiset of nonzero complex numbers have power sums s_m.
Select d distinct positive members x_j, counted once each. Unselected terms
outside a disk of radius r are assumed positive real; inside the disk, the
sum of absolute values is at most B. Suppose x_j belongs to a certified interval
[l_j,u_j], listed in strictly decreasing, disjoint order, with l_j>r.
Define the interval separation

\[
 \Delta_{jk}=\begin{cases}l_j-u_k,&j<k,\\l_k-u_j,&k<j,\end{cases}\quad
 L_j=\prod_{k\ne j}\frac{u_k+r}{\Delta_{jk}},\qquad
 \epsilon_{d,n}=Br^{n-1}\sum_{j=1}^d\frac{L_j^2}{l_j^n}.
\tag{15}
\]

### THA26.I: a uniform Hermitian form bound

For every real polynomial P of degree<d and every integer n>=1,

\[
 \sum_k\lambda_k^n P(\lambda_k)^2
 \ge(1-\epsilon_{d,n})\sum_{j=1}^d x_j^n P(x_j)^2.
\tag{16}
\]

In particular epsilon<1 proves strict positive definiteness of

\[
 H_d^{[n]}=(s_{n+i+j})_{i,j=0}^{d-1}.
\tag{17}
\]

The left side of (16) is real after conjugate pairing. It is an **analytic
square at complex lambda**, not a modulus square silently substituted there.

**Proof.** Lagrange interpolation gives P(lambda)=sum_j P(x_j)ell_j(lambda).
On the tail disk, |ell_j(lambda)|<=L_j. Weighted Cauchy--Schwarz gives

\[
 |P(\lambda)|^2\le
 \left(\sum_jx_j^nP(x_j)^2\right)\sum_j\frac{L_j^2}{l_j^n}.
\]

Moreover \(\sum_{\rm disk}|\lambda|^n\le Br^{n-1}\). Their product bounds
the absolute value of the full disk contribution. Every other unselected term
is positive real and nonnegative on real polynomial squares. Adding those
terms proves (16). The finite head quadratic form is strictly positive on
nonzero degree<d polynomials by distinct-node interpolation. QED.

Each term in epsilon_(d,n+1) is the corresponding term in epsilon_(d,n)
multiplied by r/l_j<1. Thus one calculation at n0 proves the same inequality
for **every integer n>=n0**, not just a finite sweep of n values.

### THA26.X: application to the original xi source

Use H,r,B from (6) and the 25 ordinate intervals (a_j,b_j) in INPUTS.json,
with \(l_j=b_j^{-2}\), \(u_j=a_j^{-2}\). All possibly nonreal terms are above H,
while every remaining term below H is positive real. The exact rational
products and complete analytic tail therefore give

\[
 \epsilon_{25,2}<\frac1{5\,000\,000},\qquad
 H_{25}^{[n]}\succeq
 (1-1/5\,000\,000)\left(\sum_{j=1}^{25}x_j^{n+i+k}\right)_{i,k=0}^{24}
 \succ0\quad(n\ge2).
\tag{18}
\]

For orientation, the first epsilon is about 1.950612096005081e-7.
The exact outward rational enclosure is in result.json. The same calculation
with the first nine nodes gives epsilon_(9,1)<1/3, hence H_9^[n]>0 for every
n>=1. Taking principal submatrices includes all smaller ranks.

This is a genuine all-shift/full-tail result at bounded rank. No numerical
approximation of the actual s_m entries, Hankel determinants or a finite zero
truncation defines the acceptance. Its primitive low-zero assertions and finite
verified height are still imported. It is not a rank-25 theorem about the
repository's different value-node Pick matrices.

The corresponding ten-node, shift-one **majorant** is above one. That merely
makes this particular bound inconclusive; it is not a negative actual matrix.
No maximality claim is made for the retained ranks, constants or interval widths.

## 5. A perturbation of the actual theta density survives all these tests

This attacks the proposed implication from the established positivity to RH.
It is not a counterexample to the Riemann Hypothesis.

### THA26.P: preserve the low zeros and bounded-rank hierarchy, add nonreal zeros

Set b=10^(-16), R=1+b/10, and
\(c=(R^2+1)/(R+1)^2\). Define

\[
 w_b(t)=cw(t)+\frac{1-c}{2}\{w(t-b)+w(t+b)\}.
\tag{19}
\]

This is a positive even smooth probability density. It has all exponential
moments and the same kind of rapidly decreasing differentiated tails needed
for the centered-antiderivative determinant. Its transform is exactly

\[
 F_b(z)=\frac{\Xi(z)}{\Xi(0)}
       \frac{R^2+1+2R\cos(bz)}{(R+1)^2}.
\tag{20}
\]

Every real xi zero remains a zero of the same multiplicity, because the second
factor is strictly positive on the real line. Its extra zeros are

\[
 z=\frac{(2k+1)\pi\pm i\log R}{b},\qquad k\in\mathbb Z.
\tag{21}
\]

They are genuinely nonreal, with \(0<|\Im z|<1/10\). All their positive real
parts exceed H. Thus the finite verified-height assertion and every selected
low real zero stay exactly unchanged. Coincidences with original nonreal zeros
would add multiplicity, not cancel them. These are zeros of **F_b**, not claimed
zeros of xi.

For the additional positive-real-part zeros,

\[
 \sum|z|^{-2}\le\frac{2b^2}{\pi^2}\sum_{k\ge0}(2k+1)^{-2}
                 =b^2/4,
\tag{22}
\]

and each inverse square has modulus less than r. Replace B by B+b^2/4 in (15).
The exact rational check still gives epsilon_(25,2)<1/5,000,000. Consequently
**the altered source satisfies every unweighted positivity conclusion (18) for
all shifts**, and also all scalar trace signs.

The same phase-payment proof (10), now including the additional high zeros,
gives a strictly positive Gaussian zero sum and the entire Bernstein and
factorial-weighted all-rank hierarchy (9),(14) for F_b as well. Yet (21)
precludes spectral reality. These combined properties are insufficient.

For completeness, the centered-antiderivative construction is still valid.
On the positive tail the shifted term w(t-b) dominates (19), so its logarithmic
derivative grows like a positive constant times e^(2t). Reflection treats the
negative tail. The source's FQ/w Hilbert--Schmidt integral is finite by the same
tail proof as #834. Its evenness and exponential moments give that packet's
centered determinant limit. No positive or self-adjoint spectral operator is
assumed in this deduction.

The perturbation can be made arbitrarily small in L1 by taking b down to zero:
\(\|w_b-w\|_1\le(1-c)b\|w'\|_1\). For all sufficiently small b, the same strict
25-rank margin persists. No relative error bound uniform on the far pointwise
tails is claimed. The exact theta/arithmetic formula and modular identity are
**not preserved** by (19). This is exactly the feature a successful proof must
still exploit. The earlier late-tail causal-source packet #823 is a related
stability obstruction, not a source theorem imported into this new calculation.

## 6. An independently reconstructible negative Hankel example

The preceding perturbation starts from the actual theta density, but changes
that source. Evaluating its first failing Hankel rank is neither needed nor attempted.
Here is a separate small rational control with a negative determinant.

Let U be uniform on [-1,1], V independent with values 0,+1/2,-1/2 and respective
probabilities 61/121,30/121,30/121. The density of U+V is positive and even on
its compact support, with transform

\[
 F_*(z)=\frac{\sin z}{z}
        \left(\frac{61}{121}+\frac{60}{121}\cos(z/2)\right).
\tag{23}
\]

It has real zeros k*pi and nonreal zeros
\(2(2k+1)\pi\pm2i\log(6/5)\), whose imaginary parts have modulus <2/5<1/2.
This is an actual probability density, not an arbitrary list of fake eigenvalues.
On its finite support the density is bounded above and below by positive
constants almost everywhere. The bounded-interval Volterra/rank-one determinant
proof works for this density as well: the cumulative distribution is absolutely
continuous, and all integrations by parts are legitimate. Continuity of the
density itself is not needed for that bounded-interval proof.

Its positive real inverse-square terms contribute \(\zeta(2m)/\pi^{2m}\).
The absolute contribution of the additional pairs is at most

\[
 2\,2^{-2m}(1-2^{-2m})\frac{\zeta(2m)}{\pi^{2m}}
 \le\frac38\frac{\zeta(2m)}{\pi^{2m}}.
\]

So all its scalar power sums are strictly positive. Nevertheless exact moment
integration, followed by cumulants (3), gives

\[
 \det(s^*_{2+i+j})_{i,j=0}^{3}
 =-\frac{19170822476692170759725788896551}
 {18160328599274715237536977953314688937542592738885632000000000}<0.
\tag{24}
\]

No approximate zero or numerical eigenvalue is used in (24). The supplied
program obtains the moments both by independent-sum convolution and by direct
integration of the three interval densities. It obtains the power sums both
by cumulant recursion and by a logarithmic-derivative/Newton recursion.
The full exact determinant then reproduces (24).

An arbitrary prescribed finite rank can also be hidden in this elementary
compact-density class. Replace 1/2 by a sufficiently small rational b and set
R=1+b/10, c=(R^2+1)/(R+1)^2. Scale lambda by pi^2. The selected real nodes are
1/j^2, the extra disk radius is b^2, and total extra mass is at most 4b^2.
For any fixed d, (15) tends to zero as b tends to zero, uniformly in n>=2.
At d=25, b=10^(-8), the exact bound is below 10^(-10). These sources still have
nonreal zeros within distance 1/10 of the real axis. This is a general
finite-rank/all-shift insufficiency theorem, not a bound for actual xi.

## 7. The exact end-to-end criterion and the unsuccessful final step

### THA26.C: the missing unweighted assertion really does close the proof

With s_m defined from the original xi source, the following are equivalent:

1. RH;
2. \(H_d^{[2]}=(s_{i+j+2})_{i,j=0}^{d-1}\succeq0\) for every d>=1;
3. \(\vartheta(u)\) in (7) is completely monotone on u>0.

This is an application of classical moment and Stieltjes-transform reasoning,
not a claimed new easier RH criterion. We give the complete implications to
identify exactly which assertion the attempted proof still lacks.

**RH implies 2 and 3.** Then all z_j are positive real. The positive atomic
measure \(\sum_j\lambda_j^2\delta_{\lambda_j}\) represents s_(k+2), giving 2.
The positive exponential sum in (7), with its absolute differentiated
convergence for u>0, gives 3.

**2 implies RH.** By the classical Hamburger moment theorem, the real sequence
m_k=s_(k+2) has a positive representing measure nu on the real line. Let
\(R_0=\sup_j|\lambda_j|<\infty\), C=sum_j|lambda_j|^2. Its even moments satisfy
\(0\le m_{2k}\le C R_0^{2k}\). Therefore nu is supported on [-R_0,R_0], by
bounding the mass outside [-R_0-epsilon,R_0+epsilon] with its even moments.
For |z|>R_0, absolute geometric summation gives

\[
 \int\frac{d\nu(x)}{z-x}=\sum_j\frac{\lambda_j^2}{z-\lambda_j}.
\tag{25}
\]

The left side is analytic off that real segment. On the right, lambda_j tends
to zero; the series is locally normally convergent away from zero and its
discrete poles. Identity continuation in either punctured half-plane excludes
any nonreal pole: the residue at a nonzero repeated lambda is its positive
integer multiplicity times lambda^2, and cannot vanish. Thus every lambda is
real. A negative lambda would correspond to a purely imaginary xi zero,
impossible because Xi(iy)>0. Every lambda is consequently positive, hence every
xi zero is real and RH follows. No ordering of complex poles, simple-zero
assumption or convergence at an unknown spectral edge is used.

**3 implies RH.** The Bernstein--Widder theorem represents vartheta as a positive
Laplace transform on [0,infinity). Combining with (11) by Tonelli makes p a
Stieltjes transform, analytic away from the negative real axis. Equation (2)
then cannot have a pole at -z_j^2 off that axis; residues are positive integer
multiplicities and cannot cancel. Negative z_j^2 is again excluded by
Xi(iy)>0. This gives RH. The converse already showed equivalence.

### What was tried and what remains unproved

The operator route would complete as follows:

\[
 \text{literal theta source}\longrightarrow
 \det(I-z^2T)=\Xi(z)/\Xi(0)
 \longrightarrow
 \operatorname{Tr}\!\left[(T P(T))^2\right]\ge0\quad\forall P\in\mathbb R[x]
 \longrightarrow\mathrm{RH}.
\tag{26}
\]

The middle condition in (26) is exactly assertion 2. This pass proves all scalar
traces, all factorial-weighted ranks, and all unweighted shifts at ranks through
25. It does not prove that middle condition for arbitrary polynomial degree.
Equation (19) shows why those successes cannot be promoted to it without new
information specific to the unmodified arithmetic source.

The alternate attempt uses p completely monotone from (11). However p is the
Laplace transform of the **positive** function vartheta; that does not make
vartheta completely monotone. The latter, not the former, is assertion 3.
Likewise inverse-factorial entrywise scaling does not turn (14) into assertion 2.
The perturbed actual-theta construction retains even those all-rank weighted
properties and nevertheless has explicit nonreal zeros.

For the actual trace-class operator, put A=T P(T). The precise missing bound
can also be written

\[
 \operatorname{ReTr}A^2=\|A\|_{HS}^2-\tfrac12\|A-A^*\|_{HS}^2\ge0.
\tag{27}
\]

This identity follows by expanding the Hilbert--Schmidt square; all products
are trace class. Positivity of the singular-value operator controls the first
norm, not the required comparison with the second. The ordinary square in
(27) must not be replaced by A* A. The known bounded-metric obstruction in
#834 also prevents the most immediate self-adjointization on its full space.
During closing, #834 advanced to `62bd9bbed134e20c1ee9cd92d008562079af9ceb`,
adding a real-zero-crowding argument against bounded metrics even on its
infinite spectral core. That new manuscript was read as research context,
not independently accepted or used to prove the present results. The original
determinant source is unchanged. No unbounded metric or source-specific
estimate settling (27) is constructed here.

**Outcome:** complete proposed proofs of the component assertions above, and
an exact test showing the attempted finishing promotions fail. The full RH
proof is not obtained. The unweighted all-rank assertion remains unproved.


## References and source-reading boundaries

**E1.** D. Platt and T. Trudgian, *The Riemann hypothesis is true up to
3·10^12*, arXiv:2004.09765; Bull. London Math. Soc., DOI 10.1112/blms.12460.
https://arxiv.org/abs/2004.09765 . The finite-height theorem statement is
imported. Its first PDF page was visually checked; its original numerical
campaign and full software environment were not rerun.

**E2.** LMFDB, Riemann zeta zero data,
https://www.lmfdb.org/L/download_zeros/1-1-1.1-r0-0-0 . The returned data reports
100-bit accuracy, and its cached header dates the download to 7 August 2026.
The first 25 values select the much wider rational intervals in INPUTS.json.
Those values are imported primitive data, not fresh interval computations.
Their accuracy is not established by hashing our copy.

**E3.** R. Zhang, *On Power Sums of Positive Numbers*, arXiv:1510.03420v2,
https://arxiv.org/abs/1510.03420v2 . The xi product and related moment/power-sum
criteria were consulted as classical source/literature context. Parsed paper
text was read; the attempted page-image fetch failed. No full external proof
review or priority audit is claimed.

**E4.** K. Schmuedgen, *The Moment Problem*, GTM 277, Springer (2017),
https://doi.org/10.1007/978-3-319-64546-9 . The classical Hamburger moment
existence theorem is an explicit imported theorem in Section 7, not a theorem
proved by our finite controls. The publisher's overview and chapter locations
were checked; the complete book was not read in this session.

**E5.** Classical Bernstein--Widder representation for completely monotone
functions (R. Schilling, R. Song and Z. Vondracek, *Bernstein Functions*,
second edition, 2012, https://doi.org/10.1515/9783110269338) is used only for the converse criterion in Section 7. The forward
complete-monotonicity statements in Section 3 are proved by the displayed
positive integral, rather than by assuming a Stieltjes or complete-Bernstein
property. Hadamard factorization, Jacobi inversion, Jensen's formula and the
usual entire xi normalization are standard named analytic inputs.

**R1.** The complete determinant and cumulant source is
`GettysburgResearch/riemann`, PR #834,
`standalone/2026-09-09-centered-theta-determinant/PROOF.md` at
`f0e34780f4fe91bd5d07e791e8855189838c3df5`, blob
`ef01f74c50d4efacb615176cbfed4a3de2fd1147`. It was read through the connector;
its author's code was not executed, and this packet is not its independent
acceptance. Classical source power sums are separated from that proposed
operator interpretation. Full per-file and later-delta records are in
[SOURCES.json](SOURCES.json).
