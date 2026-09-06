# An exactly balanced rational source: a different route from block gain

Status: proposed component proofs; independent mathematical review required.
**The uniform full-source block gain, the new subpower-energy estimate, and RH
are NOT proved.** This is an author continuation, not a Reviewer C verdict.

Frozen parent: PR #805 at `0f8724bbd86c1de8f40eacbf30129321e0ebc8aa`.
The previous parity optimum is a relaxation. This packet imposes its missing
scalar normalization exactly, constructs an actual finite arithmetic source,
and proves polynomial-horizon approximation without PNT or zero information.
A separate all-scale coherent-source construction shows why even asymptotic
optimality of the detail cannot supply the remaining full-norm estimate.

## 0. Setup and scope

Work over the reals in
\[
 H=\ell^2(\mathbb N_{\ge1},[n(n+1)]^{-1}),\quad
 \chi(n)=1,\quad h_k(n)=\{n/k\},\quad h_1=0.
\]
Every sequence is zero at 0 and is extended constantly to each cell
\([n,n+1)\), making its norm the integral against \(dt/t^2\).
Let \(B_N=\operatorname{span}(h_2,\ldots,h_N)\), and let \(\delta_N\)
be the squared distance from \(\chi\) to \(B_N\). The previous target
\(\delta_N-\delta_{2N}\ge c\delta_N^2\) is still open.

Use the parent identities
\[
 D_2f(n)=f(\lfloor n/2\rfloor),\quad
 D_2h_k=h_{2k}-h_2/k,\quad \|D_2\|=2^{-1/2}.
\]
On odd cells put \(Jf(1)=f(1)\), \(Jf(n)=f(n)-f(n-1)\) for odd
\(n\ge3\). Its norm is \(\|d\|_K^2=\sum_{n\text{ odd}}d(n)^2/(2n^2)\).
For odd \(k\), define
\[
 H_1=2h_2,\qquad H_k=2h_2/k-h_k\ (k\ge3).
\]
Then \(JH_k(n)=\mathbf1_{k\mid n}\). On
\(O_M=\{1\le k\le M:k\text{ odd}\}\), the exact detail Gram is
\[
 Q_{kl}=\frac{\pi^2}{16}\frac{\gcd(k,l)^2}{k^2l^2}
        =\frac{\pi^2}{16\operatorname{lcm}(k,l)^2}. \tag{0.1}
\]
This follows by summing over all odd multiples of the lcm. The Jordan
identity \(\sum_{d\mid n}J_2(d)=n^2\) gives the positive factorization
\[
 Q=\frac{\pi^2}{16} D_0 E\,\operatorname{diag}(J_2(d))E^T D_0,
 \quad (D_0)_{kk}=k^{-2},\quad E_{kd}=\mathbf1_{d\mid k}.
\]
Here \(J_2(d)=d^2\prod_{p\mid d}(1-p^{-2})\). The divisor-closed set
\(O_M\) makes \(E\) invertible; its inverse is the Mobius incidence
matrix. Thus all finite inverses used below exist. These ingredients and
the Hilbert-space machinery are classical; no priority is asserted.

## 1. BL26.1: solve BOTH scalar constraints exactly

For every integer \(M\ge3\), set the following *rational* numbers:
\[
 S_M=\sum_{d\in O_M}\frac{\mu(d)^2}{J_2(d)},\quad
 A_M=\sum_{d\in O_M}\frac{\mu(d)\varphi(d)}{J_2(d)},\quad
 D_M=\sum_{d\in O_M}\frac{\varphi(d)^2}{J_2(d)},\quad
 K_M=S_MD_M-A_M^2.
\]
Define rational vectors
\[
 v_{k,M}=k^2\!\sum_{\substack{d\in O_M\\k\mid d}}
 \frac{\mu(d/k)\mu(d)}{J_2(d)},\qquad
 w_{k,M}=k^2\!\sum_{\substack{d\in O_M\\k\mid d}}
 \frac{\mu(d/k)\varphi(d)}{J_2(d)}.
\]
The new source coefficients are
\[
 \boxed{\lambda_{k,M}=\frac{D_Mv_{k,M}-A_Mw_{k,M}}{K_M}.} \tag{1.1}
\]
Their defining property is
\[
 \boxed{\lambda_{1,M}=1,\qquad
        \sum_{k\in O_M}\lambda_{k,M}/k=0.} \tag{1.2}
\]
These are literal rational equalities, not limiting estimates.

**Proof and optimality.** Cauchy--Schwarz gives \(K_M>0\): the two
vectors \(\mu(d)/\sqrt{J_2(d)}\), \(\varphi(d)/\sqrt{J_2(d)}\)
are not proportional already at \(d=1,3\). Write \(u_k=1/k\) and
\(R=(16/\pi^2)Q\). The divisor factorization gives
\[
 Rv=e_1,\qquad Rw=u,\qquad
 v_1=S_M,\ w_1=A_M,\ u^Tv=A_M,\ u^Tw=D_M.
\]
For the last identities one may interchange the finite divisor sums and
use \(\sum_{k\mid d}k\mu(d/k)=\varphi(d)\). Formula (1.2) follows.
Also
\[
 Q\lambda=\frac{\pi^2}{16K_M}(D_M e_1-A_Mu). \tag{1.3}
\]
For any perturbation \(z\) with \(z_1=u^Tz=0\),
\(z^TQ\lambda=0\). Positive definiteness proves that (1.1) uniquely
minimizes the complete detail error subject to (1.2).

Indeed, if \(d_a(n)=\sum_{k\in O_M,k\mid n}a_k\) on odd \(n\),
\[
 \|\mathbf1_{\{1\}}-d_a\|_K^2=\tfrac12-a_1+a^TQa.
\]
The minimum on the constrained affine space is exactly
\[
 \boxed{\eta_M=\frac{\pi^2D_M}{16K_M}-\frac12>0.} \tag{1.4}
\]
Strict positivity holds because \(d_a\) is periodic on odd integers,
with value 1 on infinitely many odd integers congruent to 1 modulo all
the finitely many odd generators, not just at 1. The coefficients are
rational even though the minimum contains \(\pi^2\). End of proof.

At \(M=4\), the coefficients are exactly \((\lambda_1,\lambda_3)=(1,-3)\).
At \(M=16\), \(\lambda_9=-20880/57769\ne0\). Unlike the unconstrained
parity optimum, this construction does not erase nonsquarefree odd indices.
It still defines a particular trial, NOT the full-space optimizer \(g_N\).

## 2. BL26.2: unconditional rates for the balanced coefficients

Put \(L=1+\log M\). For every \(M\ge4096\),
\[
 \boxed{0<\eta_M\le4L^2/M,\qquad
 |
 \lambda_{k,M}-\mu(k)|\le20kL^2/M\quad(k\in O_M).} \tag{2.1}
\]
Neither PNT nor any cancellation estimate for \(\mu\) is required.

**Proof.** First, for odd \(n\),
\[
 \frac{\varphi(n)^2}{J_2(n)}=
 \prod_{p\mid n}\left(1-\frac2{p+1}\right)
 \ge 1-\sum_{p\mid n}\frac2{p+1}.
\]
Summing over odd integers at most \(M\), bounding prime divisors by all
odd integers at least 3, and using the spacing \(2d\) of their odd
multiples gives
\[
 D_M\ge(1-\log2)M-\tfrac12H_{\lfloor(M+1)/2\rfloor}
 \ge\tfrac3{10}M-\tfrac12(1+\log M)\ge M/5\quad(M\ge32). \tag{2.2}
\]
For the first inequality use
\(\sum_{d\ge3,d\text{ odd}}1/[d(d+1)]=\log2-1/2\).
For the last, check \(M=32\) using \(\log2<7/10\); the difference
is increasing thereafter. Also \(|A_M|\le L\), since
\(\varphi(n)/J_2(n)\le1/n\).

For clarity we reconstruct the relation to the previous unconstrained
optimum. Put \(C=8/\pi^2<1\), \(a^*=Cv\), and
\[
 \bar a=C\left(v-(A_M/D_M)w\right).
\]
The vector \(\bar a\) minimizes the detail error with just the homogeneous
constraint \(u^Ta=0\), without fixing its first coordinate. Its error is
\[
 \bar e_M=e_M+\frac{4}{\pi^2}\frac{A_M^2}{D_M},\quad
 e_M=\frac4{\pi^2}\sum_{\substack{d>M\\d\text{ odd}}}
                   \frac{\mu(d)^2}{J_2(d)}\le\frac1{2M}. \tag{2.3}
\]
These equalities follow either by one constrained quadratic minimization,
or from (0.1); the last bound uses the absolute Euler product at exponent 2.
By (2.2), \(\bar e_M\le3L^2/M\). Moreover
\[
 \bar a_1=1-2\bar e_M=C K_M/D_M>0,\quad
 \lambda=\bar a/\bar a_1,\quad
 \eta_M=\bar e_M/(1-2\bar e_M). \tag{2.4}
\]
For \(M\ge4096\), \(3L^2/M<1/8\); check the endpoint with
\(L<10\) and use the monotonic decrease of \(L^2/M\). Thus
\(\bar a_1>3/4\), proving the bound on \(\eta_M\).

For squarefree odd \(k\), absolute Euler products give
\[
 a_k^*=C\mu(k)\frac{k^2}{J_2(k)}
 \sum_{\substack{m\le M/k\\m\text{ odd},\ (m,k)=1}}
                         \frac{\mu(m)^2}{J_2(m)}.
\]
The completed sum equals \(\mu(k)\) after multiplication by its prefactor.
Since \(n^2/J_2(n)\le\pi^2/8\) for odd \(n\), and
\(\sum_{m>x}m^{-2}\le2/x\) for \(x\ge1\),
\[
 |a_k^*-\mu(k)|\le\frac{\pi^2k}{4M}<\frac{5k}{2M}.
\]
At nonsquarefree \(k\), both \(a_k^*\) and \(\mu(k)\) vanish.
Using \(\varphi(n)/J_2(n)\le1/n\) also gives
\( |w_{k,M}|\le k(1+\log(M/k))\le kL\).
Equations (2.2)--(2.4) yield
\[
 |\bar a_k-\mu(k)|\le8kL^2/M,\quad
 |1-\bar a_1|\le6L^2/M,
\]
and hence \(|\lambda_k-\mu(k)|\le(4/3)(8k+6)L^2/M\le20kL^2/M\).
This proves (2.1) and, in particular, coefficientwise convergence to \(\mu\).

## 3. BL26.3: actual-source primitive and exact pole cancellation

Define the finite source
\[
 \boxed{F_M=\sum_{k\in O_M}\lambda_{k,M}(h_{2k}-h_k)\in B_{2M}.} \tag{3.1}
\]
Every generator is the original fractional-part generator. There is no
free coarse component or prescribed zero data. This is a special trial
inside the full dictionary, not a replacement equality for its span.

Let \(d_M(n)=\sum_{k\mid n,k\in O_M}\lambda_{k,M}\) on odd integers.
The exact alternative forms are
\[
 F_M(n)=\sum_{k\in O_M}\lambda_{k,M}
       (\lfloor n/k\rfloor-\lfloor n/(2k)\rfloor)
       =\sum_{\substack{m\le n\\m\text{ odd}}}d_M(m). \tag{3.2}
\]
The slope in \(h_{2k}-h_k\) cancels by (1.2). Finite differencing the
floors proves the second equality: at even \(n\), the two divisibility
indicators cancel, and at odd \(n\) their difference is \(\mathbf1_{k\mid n}\).
Thus \(F_M(1)=F_M(2)=1\) exactly. Both slope cancellation and initial
normalization have been imposed, rather than estimated using PNT.

For the finite Dirichlet polynomial
\(P_M(s)=\sum_{k\in O_M}\lambda_{k,M}k^{-s}\),
\[
 P_M(1)=0,\qquad
 \boxed{\int_1^\infty F_M(t)t^{-s-1}\,dt
       =\frac{(1-2^{-s})\zeta(s)P_M(s)}s\quad(\Re s>0).} \tag{3.3}
\]
To prove (3.3), first use (3.2) in \(\Re s>1\) and sum the absolutely
convergent divisor series. The left side is holomorphic in \(\Re s>0\)
because \(F_M\) is a bounded periodic function. On the right the only
possible pole in that half-plane is at 1, removed by the exact equation
\(P_M(1)=0\). The identity theorem finishes the proof. In particular, every
nontrivial zeta zero with real part greater than 1/2 is annihilated by every
one of these finite sources; none is canceled in the TARGET \(1/s\).

For each fixed cell \(n\), (2.1) and (3.2) prove
\[
 \boxed{F_M(n)\longrightarrow1\quad(M\to\infty).} \tag{3.4}
\]
The exact comparison identity is
\(\sum_{k\text{ odd}}\mu(k)(\lfloor n/k\rfloor-\lfloor n/(2k)\rfloor)=1\).
Only \(k\le n\) occur; it is the divisor identity \(\mu*1=\varepsilon\)
on the odd integers. No conditionally convergent infinite Mobius sum is
exchanged with a limit.

## 4. BL26.4: polynomial observation horizon and full tail bounds

For \(M\ge4096\) and integers \(1\le n\le M\),
\[
 \boxed{|F_M(n)-1|\le20n^2L^2/M.} \tag{4.1}
\]
Indeed each coefficient difference in (3.2) contributes at most
\((20kL^2/M)(n/k)\), and at most \(n\) indices contribute.
Consequently, for \(1\le R\le M\),
\[
 \sum_{n\le R}\frac{|F_M(n)-1|^2}{n(n+1)}
       \le400L^4R^3/M^2. \tag{4.2}
\]

Let \(E_M=\|F_M\|_H^2\), the FULL norm. For every \(k\ge1\),
\( |h_{2k}-h_k|\le1/2\), and
\(\|h_{2k}-h_k\|^2\le1/(2k)\): on \(n<k\) use \(n/(2k)\),
and on \(n\ge k\) use \(1/2\) and the telescoping weights.
By (2.1), \(|\lambda_k|\le21L^2\). Thus
\[
 \boxed{E_M\le882M L^4.} \tag{4.3}
\]
This unconditional linear-power upper bound is NOT subpower. It follows
from the triangle inequality and \(\sum_{k\le M}k^{-1/2}\le2\sqrt M\).

Also \(|1-F_M(n)|\le11M L^2\) for every \(n\), so
\[
 \sum_{n>T}\frac{|1-F_M(n)|^2}{n(n+1)}
       \le\frac{121M^2L^4}{T+1}. \tag{4.4}
\]
The squared norm of \(F_M\) itself has the same upper bound with 121
replaced by \(441/4\).

Taking \(R=\lfloor\sqrt M\rfloor\) and \(T=M^3\), the early ERROR and
far ERROR tend to zero, at bounds \(400L^4/\sqrt M\) and \(121L^4/M\).
Hence, if
\[
 C_M=\sum_{\lfloor\sqrt M\rfloor<n\le M^3}
                      \frac{|F_M(n)|^2}{n(n+1)},
\]
then \(E_M=C_M+1+o(1)\). The early norm tends to 1 by (4.2) and
Cauchy--Schwarz, and the far norm tends to zero by (4.4).
This localizes the missing ENERGY estimate; no cancellation in the middle
range is claimed. That potentially long sum is a theorem target, not a
request to run a campaign.

## 5. BL26.5: another end-to-end sufficient target, without uniform block gain

The new explicit target is
\[
 \boxed{\mathrm{BL26.E}:\quad
 E_M= M^{o(1)}.} \tag{5.1}
\]
More explicitly, \(\forall\epsilon>0\ \exists C_\epsilon\ \forall M\ge3\),
\(E_M\le C_\epsilon M^\epsilon\). It suffices on any fixed cofinal
sequence, for example \(M=2^j\), \(j\ge2\). Even a zero lower limit of
\(\log(1+E_M)/\log M\) suffices. **None of these estimates is proved.**
No equivalence with RH or implication from RH to this particular source
family is asserted.

Here is the quantitative implication, which IS proved. If
\(\zeta(\rho)=0\), \(\beta=\Re\rho>1/2\), then
\[
 \boxed{\liminf_{M\to\infty}\frac{\log(1+E_M)}{\log M}
       \ge\frac{2\beta-1}{2-\beta}>0.} \tag{5.2}
\]
Zeros in \(\Re s>1\) are already excluded by the absolute Euler product;
it is enough to consider \(1/2<\beta\le1\).

**Proof.** Fix \(0<a<1/(2-\beta)\), and put \(x=M^a\). For large
\(M\), (4.1), applied cellwise, gives
\[
 \left|\int_1^x(F_M(t)-1)t^{-\rho-1}dt\right|
 \le\frac{20L^2}{(2-\beta)M}x^{2-\beta}\longrightarrow0.
\]
The first integral of \(F_M\) therefore tends to \(1/\rho\). Equation
(3.3) at \(\rho\) shows that its remaining integral over \([x,\infty)\)
has modulus at least \(1/(2|\rho|)\) for sufficiently large \(M\).
Cauchy--Schwarz gives
\[
 \left|\int_x^\infty F_M(t)t^{-\rho-1}dt\right|
 \le\sqrt{E_M}\frac{x^{1/2-\beta}}{\sqrt{2\beta-1}},
\]
hence
\[
 E_M\ge\frac{2\beta-1}{4|\rho|^2}M^{a(2\beta-1)}.
\]
Let \(a\uparrow1/(2-\beta)\) after taking the lower limit. This proves
(5.2). Consequently (5.1) excludes every right-hand off-line zero; the
functional equation supplies the reflected half of RH. The finite source
was fixed before introducing \(\rho\). Multiplicities do not affect the
argument, since a single vanishing value suffices. End of proof.

A power upper bound \(E_M\ll M^\theta\), \(0\le\theta\le1\), would
more generally exclude zeros with
\(\Re\rho>(1+2\theta)/(2+\theta)\). The proved bound (4.3), with
exponent 1, reaches only the already known boundary 1. It is not an RH
improvement. Equivalently, it suffices to establish subpower growth of the
finite middle energy \(C_M\) in section 4.

As a simpler sufficient condition, a bounded subsequence of \(E_M\)
would give weak convergence \(F_M\rightharpoonup\chi\), by coordinatewise
convergence and density of finitely supported tests. Since all \(F_M\)
lie in the closed dictionary span, the classical Nyman--Beurling route
would then also apply. The quantitative proof above needs only subpower,
not boundedness, and does not import the converse direction of that criterion.

## 6. BL26.6: a coherent obstruction survives BOTH constraints

The remaining estimate does not follow from detail near-optimality.
The following counterconstruction uses the SAME integer dictionary, not a
new prime system or a prescribed zero set.

For even \(K\ge2\), let \(M=4K\) and define on \(O_M\)
\[
 z_k=\begin{cases}
 k,&K<k\le2K,\ k\text{ odd},\\
 -k,&3K<k\le4K,\ k\text{ odd},\\
 0,&\text{otherwise}.
 \end{cases}
\]
Both bands contain \(K/2\) indices. Thus \(z_1=0\), \(\sum z_k/k=0\).
Let \(F[z]\) mean (3.1) with these coefficients, and \(d_z\) its odd
jump sequence. Then
\[
 \boxed{\|d_z\|_K^2\le\frac{25}{2}K,\qquad
         \|F[z]\|_H^2>\frac3{32}K^3.} \tag{6.1}
\]
In particular the squared operator norm from detail to full source on this
homogeneous constrained space is at least \(3K^2/400\).

**Proof.** On every integer cell \(2K\le n\le3K\), none of the
second-band indices or third odd multiples of first-band indices has
entered (3.2). Hence
\(F[z](n)=\sum_{K<k\le2K,k\text{ odd}}k=3K^2/4\).
The sum of the weights on those cells is
\(1/(2K)-1/(3K+1)>1/(6K)\), proving the lower bound.
For the upper bound use (0.1), \(J_2(d)\le d^2\), and absolute values:
\[
 \|d_z\|_K^2\le\frac{\pi^2}{16}
     \sum_{d\le4K}H_{\lfloor4K/d\rfloor}^{\,2}
 \le\frac{\pi^2}{16}\,20K<\frac{25}{2}K.
\]
The last sum is at most
\(\int_0^{4K}(1+\log(4K/t))^2dt=20K\), by monotonicity and
\(H_n\le1+\log n\). End of proof.

There is an asymptotically optimal version of this obstruction. Take
\(K=2s^4\), \(M=8s^4\), integer \(s\ge2\), and perturb the *exact*
balanced minimizer by
\[
 \lambda^\pm=\lambda_{\cdot,M}\pm z/(Ks).
\]
Both constraints hold exactly, and both source sequences converge
cellwise to \(\chi\). By (1.3) their detail error is exactly
\[
 \eta_M+\frac{\|d_z\|_K^2}{K^2s^2}
 \le\eta_M\left(1+\frac{2000}{s^2}\right). \tag{6.2}
\]
Here \(\eta_M\ge e_M>1/(40M)=1/(160K)\), using the parent's elementary
odd-squarefree count for \(M\ge64\). Thus their relative excess over the
OPTIMAL constrained detail tends to zero.

Nevertheless the parallelogram identity gives
\[
 \boxed{\max\{\|F[\lambda^+]\|_H^2,
               \|F[\lambda^-]\|_H^2\}>3s^2/16.} \tag{6.3}
\]
Indeed their average squared norm is
\(E_M+\|F[z]\|^2/(K^2s^2)>3K/(32s^2)=3s^2/16\).
One may select the sign of the larger arithmetic norm, with no reference
to any hypothetical zero. This creates a source family with exact balance,
exact first-cell agreement, coefficientwise Mobius convergence, and
asymptotically optimal detail, but a full norm growing at least as a
positive constant times \(\sqrt M\). In particular those properties do
not prove BL26.E. This does NOT refute BL26.E for the unique exact
minimizer (1.1), nor the original full-source gain.

## 7. Bounded actual-source calculations and attempted closure

The directed replay evaluates only \(M=4,8,16\), using complete infinite
Grams through index 30 (hard cap 32). It obtains:

| M | full E_M | target pairing <chi,F_M> | full squared error |
|---|---|---|---|
|4|[0.906899682117,0.906899682118]|[0.549306144334,0.549306144335]|[0.808287393448,0.808287393449]|
|8|[0.810154169731,0.810154169732]|[0.734600804710,0.734600804711]|[0.340952560310,0.340952560311]|
|16|[0.888710277691,0.888710277692]|[0.842755232154,0.842755232155]|[0.203199813382,0.203199813383]|

These are deliberately fixed tests, not evidence for uniform boundedness.
They are weaker approximations than the full orthogonal projections, but
have an exact rational construction and the unconditional local limit.
The checker verifies the constrained optimum independently by a rational
KKT solve, and checks the primitive identity before evaluating a Gram.

The direct full-gain attack still has the unpriced actual correlation
\(I_N/\delta_N^2\) from the parent. The present alternative closes its
predecessor's signed scalar normalization by imposing it exactly and
retains nonsquarefree corrections. The determinant and detail error are
fully solved. The coherent construction in section 6 prevents the attempted
source-blind lift from closing the full norm. The only new RH-sufficient
claim proposed is BL26.E (or its finite-middle version); it remains open.
No claim that the alternative is known to be easier, no hidden bounded
inverse, and no convergence of a lifted norm from coefficientwise convergence
is used. RH remains unproved.


## 8. External cancellation estimates: the range mismatch remains

A separate attempt compared the original full Gram with the cotangent/Estermann
form of Nyman--Beurling energies. Maier--Rassias, arXiv:1806.05070, Theorem 2.1,
gives a fixed-power saving for their sums of the shape
`sum_{k^D <= n < 2 k^D} mu(n) g(n/k)` with `D>=2`. The theorem and its
printed range were inspected directly. It does not give a bound for arbitrary
coefficients, and its modulus is at most the square root of the summed range.
The present energy is a double quadratic form with constrained divisor-sum
weights (1.1), including comparable-index blocks and nonsquarefree correction
terms. No source-preserving transformation placing all those terms within
the imported estimate's range has been proved. Thus that saving is not used
as an unconditional substitute for (5.1). This is a boundary of this attempted
application, not a claim that the paper's methods cannot contribute.
