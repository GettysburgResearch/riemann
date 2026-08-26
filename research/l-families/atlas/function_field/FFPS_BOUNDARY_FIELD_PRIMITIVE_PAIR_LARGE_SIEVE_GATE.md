# The high primitive beta sector is a five-channel Möbius large-sieve problem

Status: **exact dyadic-shell/common-factor decomposition, exact
Möbius--Gram and harmonic Boolean-sieve normal forms; conditional
square-root-scale large-sieve criterion sufficient for RH; the large-sieve
estimate and RH are not proved**

Bounded exact replay:
[ffps_boundary_field_primitive_pair_large_sieve_gate.py](ffps_boundary_field_primitive_pair_large_sieve_gate.py).
Canonical summary:
[ffps_boundary_field_primitive_pair_large_sieve_gate.json](ffps_boundary_field_primitive_pair_large_sieve_gate.json).

Frozen source: the primitive-ray localization theorem at 2582feec6.
Its Markdown, producer, JSON, and test are pinned by the replay.

## 0. Outcome

The primitive-ray theorem localizes the RH-equivalent beta Gram correlation
to reduced ratios of growing height. This packet opens that residual sector
one step further.

Put

\[
 (c_0,c_1,c_2)=(1,-2,1),
 \qquad
 \mathfrak A=
 \{(0,0),(1,0),(2,0),(0,1),(0,2)\}.
\tag{0.1}
\]

For \((\alpha,\gamma)\in\mathfrak A\), define

\[
 h_{\alpha,\gamma}(a,b)
 =\max(67^\alpha a,67^\gamma b).
\tag{0.2}
\]

If \(d\) is squarefree and 67-free and \(H\le U\le2H\), let

\[
\boxed{
\begin{aligned}
 \mathcal P_{\alpha,\gamma}(d;H,U)
 :=\sum_{\substack{
   a,b\ {\rm squarefree}\\
   67\nmid ab,\ (a,b)=1,\ (ab,d)=1\\
   H<h_{\alpha,\gamma}(a,b)\le U}}
 {\mu(a)\mu(b)\over\sqrt{ab}}\,
 \mathcal R\!\left(
   \log{67^\alpha a\over67^\gamma b}
 \right).
\end{aligned}}
\tag{0.3}
\]

Here \(\mathcal R\) is the exact compact autocorrelation from the
source-locked ratio-sixteen criterion. Thus it silently erases pairs outside
the ratio band.

Let \(\mathcal S_H(X)\) be the off-diagonal beta Gram contribution whose
reduced ratio has height in \((H,2H]\). Then

\[
\boxed{
\begin{aligned}
 \mathcal S_H(X)
 &=
 \sum_{(\alpha,\gamma)\in\mathfrak A}
 \sum_{r=0}^{2-\max(\alpha,\gamma)}
 {c_{r+\alpha}c_{r+\gamma}
  \over67^{r+(\alpha+\gamma)/2}}\\
 &\qquad\cdot
 \sum_{\substack{
  d\le X/(67^rH)\\
  d\ {\rm squarefree},\ 67\nmid d}}
 {1\over d}\,
 \mathcal P_{\alpha,\gamma}\!\left(
 d;H,\min\left(2H,{X\over67^rd}\right)
 \right).
\end{aligned}}
\tag{0.4}
\]

This is an exact finite identity. In particular, the moving prefix boundary
is retained inside the final argument of \(\mathcal P\); it has not been
replaced by a full shell or an asymptotic radial density.

For \(X\ge2\), put \(J=\lceil\log_2 X\rceil\). Every off-diagonal reduced
ratio has integer height at least two, so

\[
 \boxed{
 \mathcal O(X)=\sum_{j=0}^{J-1}\mathcal S_{2^j}(X).}
\tag{0.5}
\]

The five oriented channels reduce to three independent panels:

\[
 \mathcal P_{1,0}=\mathcal P_{0,1},
 \qquad
 \mathcal P_{2,0}=\mathcal P_{0,2},
\tag{0.6}
\]

by swapping \(a,b\) and using the evenness of \(\mathcal R\).

Equation (0.4) exposes a standard-shaped sufficient theorem. Define the
maximal weighted square mean

\[
 \mathfrak L_{\alpha,\gamma}(D,H)
 =
 \sum_{\substack{d\le D\\d\ {\rm squarefree}\\67\nmid d}}
 {1\over d}
 \sup_{H\le U\le2H}
 |\mathcal P_{\alpha,\gamma}(d;H,U)|^2.
\tag{0.7}
\]

Consider the conditional gate

\[
\boxed{
 {\rm PRIMLS}:\qquad
 \mathfrak L_{\alpha,\gamma}(D,H)
 \ll_\varepsilon (2DH)^\varepsilon}
\tag{0.8}
\]

for every \(\varepsilon>0\), uniformly in \(D,H\ge1\), and for
\((\alpha,\gamma)=(0,0),(1,0),(2,0)\).

Then

\[
 \boxed{{\rm PRIMLS}\Longrightarrow{\rm RH}.}
\tag{0.9}
\]

No estimate in (0.8) is proved. PRIMLS is deliberately posed as a stronger
uniform sufficient hypothesis, not as an equivalent reformulation of RH.
Its value is that it is an averaged, sifted two-point Möbius theorem at the
natural square-root scale, rather than another name for the complete beta
correlation.

Two further exact normal forms sharpen what that theorem would have to do.
First, every primitive shell is the difference of two rectangles, and
Möbius inversion of primitive coprimality writes each rectangle as a signed
sum of one-dimensional Gram inner products. Second, on every finite
squarefree divisor cube, harmonic averaging in the sieve variable has an
exact biased-Boolean Parseval formula. Its zero frequency is the harmonic
mean of the panel and survives orthogonality. Thus averaging over the common
factor is a useful organization, but it is not by itself a cancellation
mechanism.

## 1. Exact common-factor swap

Fix a nonzero beta pair and reduce it as \(m=ga,n=gb\), with \((a,b)=1\).
The source support gives uniquely

\[
 a=67^\alpha a_0,
 \qquad
 b=67^\gamma b_0,
 \qquad
 (\alpha,\gamma)\in\mathfrak A,
\tag{1.1}
\]

where \(a_0,b_0\) are squarefree, 67-free, and coprime. The common factor is

\[
 g=67^r d,
 \qquad
 0\le r\le2-\max(\alpha,\gamma),
\tag{1.2}
\]

where \(d\) is squarefree and coprime to \(67a_0b_0\). Exactly as in the
frozen ray theorem,

\[
 {\beta(m)\beta(n)\over\sqrt{mn}}
 =
 {c_{r+\alpha}c_{r+\gamma}
  \over67^{r+(\alpha+\gamma)/2}}
 {1\over d}\,
 {\mu(a_0)\mu(b_0)\over\sqrt{a_0b_0}}.
\tag{1.3}
\]

Now impose the primitive-height shell

\[
 H<h_{\alpha,\gamma}(a_0,b_0)\le2H
\tag{1.4}
\]

and the physical prefix \(m,n\le X\). For fixed \(r,d\), the latter simply
cuts the upper endpoint to

\[
 U_{r,d}=\min\left(2H,{X\over67^rd}\right).
\tag{1.5}
\]

The shell is empty unless \(d\le X/(67^rH)\). Substitution of
(1.3)--(1.5), followed by a finite interchange of the \(d\) and
\((a_0,b_0)\) sums, proves (0.4). This is the promised removal of the
\(W_q\) notation: its common squarefree factor becomes the large-sieve
variable \(d\), and its coprimality condition becomes the sieve
\((a_0b_0,d)=1\) inside \(\mathcal P\).

No convergence theorem is used. Every sum is finite, the exceptional 67
orientations are retained, and all source signs remain inside the Möbius
pair panel.

## 2. Exact dyadic reconstruction

For an off-diagonal pair, the reduced coprime coordinates cannot both equal
one. Its primitive height is therefore an integer at least two. If
\(m,n\le X\), that height is at most \(X\).

The half-open shells

\[
 (1,2],(2,4],\ldots,(2^{J-1},2^J],
 \qquad J=\lceil\log_2X\rceil,
\tag{2.1}
\]

partition those heights exactly. Terms in the final shell with height larger
than \(X\) vanish through the prefix in (1.5). This proves (0.5).

The channel identities (0.6) follow from the bijection
\((a,b)\mapsto(b,a)\). The height condition, squarefree and sieve conditions
are preserved, and

\[
 \mathcal R\!\left(\log{67^\alpha a\over67^\gamma b}\right)
 =
 \mathcal R\!\left(\log{67^\gamma b\over67^\alpha a}\right)
\tag{2.2}
\]

because \(\mathcal R\) is even.

## 3. Why PRIMLS is the square-root-scale gate

On one nonempty panel, ratio-sixteen support and
\(H<h_{\alpha,\gamma}(a,b)\le2H\) force both physical reduced coordinates
to be comparable with \(H\), up to fixed factors. There are \(O(H^2)\)
ordered pairs. Each normalized coefficient in (0.3) has size
\(O_{\mathcal R}(1/H)\), again up to fixed powers of 67. Hence

\[
 \sum_{\text{one panel}}
 \left|
 {1\over\sqrt{ab}}
 \mathcal R\!\left(
 \log{67^\alpha a\over67^\gamma b}
 \right)\right|^2
 \ll_{\mathcal R}1.
\tag{3.1}
\]

Thus a random-sign or large-sieve benchmark is
\(|\mathcal P_{\alpha,\gamma}|=H^{o(1)}\), not \(H^{1/2}\) or \(H\).
The harmonic average over \(d\) naturally costs only a logarithm. This is
exactly the normalization encoded by (0.8).

Assume PRIMLS. For the moving endpoint (1.5), weighted Cauchy gives

\[
\begin{aligned}
 &\left|
 \sum_{\substack{d\le D\\d\ {\rm squarefree}\\67\nmid d}}
 {1\over d}\,
 \mathcal P_{\alpha,\gamma}(d;H,U_d)
 \right|\\
 &\quad\le
 \left(\sum_{d\le D}{1\over d}\right)^{1/2}
 \mathfrak L_{\alpha,\gamma}(D,H)^{1/2}\\
 &\quad\ll_\varepsilon
 (1+\log D)^{1/2}(2DH)^{\varepsilon/2}.
\end{aligned}
\tag{3.2}
\]

There are five oriented channels, at most three exceptional radial rows
\(r\), and \(O(\log X)\) primitive-height shells. In every nonempty
application, \(D,H\le X\) up to a fixed factor. Therefore
(0.4)--(0.5) and (3.2) give

\[
 |\mathcal O(X)|=X^{o(1)}.
\tag{3.3}
\]

The frozen near-correlation theorem identifies (3.3) with RH. This proves
the conditional implication (0.9).

The converse is not asserted. RH controls the assembled source-locked
off-diagonal form; it does not automatically provide the channelwise,
maximal-in-\(U\), weighted \(L^2(d^{-1})\) estimate demanded by PRIMLS.

## 4. Shifted-correlation interpretation

In the central channel \((\alpha,\gamma)=(0,0)\), set \(k=a-b\).
Coprimality becomes

\[
 (a,b)=1\Longleftrightarrow(b,k)=1.
\tag{4.1}
\]

Thus (0.3) is exactly an average of shifted correlations

\[
 \mu(b+k)\mu(b)
\tag{4.2}
\]

over a two-dimensional region with \(|k|=O(H)\), a compact log-ratio
weight, squarefree support, and the additional sieve
\((b(b+k),d)=1\). The other two independent panels replace the pair of
linear forms by

\[
 (67a,b)
 \qquad\text{or}\qquad
 (67^2a,b).
\tag{4.3}
\]

This is the intended analytic interface: PRIMLS is a maximal, harmonically
averaged Chowla/large-sieve statement for three explicit linear-form
geometries. Ordinary pointwise control of a single shift, or an unsigned
divisor bound, does not supply the two-dimensional square-root cancellation
in (0.8).

## 5. Exact Möbius--Gram normal form

The two-dimensional primitive condition can be removed exactly. For real
\(T\ge0\), define the closed rectangle

\[
 \mathcal G_{\alpha,\gamma}(d;T)
 =\sum_{\substack{
   a,b\ {\rm squarefree},\ 67\nmid ab,\ (ab,d)=1,\ (a,b)=1\\
   67^\alpha a\le T,\ 67^\gamma b\le T}}
 {\mu(a)\mu(b)\over\sqrt{ab}}
 \mathcal R\!\left(\log{67^\alpha a\over67^\gamma b}\right).
\tag{5.1}
\]

The shell is simply

\[
 \boxed{
 \mathcal P_{\alpha,\gamma}(d;H,U)
 =\mathcal G_{\alpha,\gamma}(d;U)
  -\mathcal G_{\alpha,\gamma}(d;H).}
\tag{5.2}
\]

Let \(K_{\rm bd}\) be the compact boundary kernel whose autocorrelation is
\(\mathcal R\). For squarefree \(k\) coprime to \(67d\), put

\[
 V^{(\alpha)}_{k,d,T}(t)
 =\sum_{\substack{
  n\le T/(67^\alpha k)\\
  n\ {\rm squarefree},\ (n,67kd)=1}}
 {\mu(n)\over\sqrt n}
 K_{\rm bd}\!\left(t-\log(67^\alpha n)\right).
\tag{5.3}
\]

Then finite Möbius inversion gives

\[
\boxed{
 \mathcal G_{\alpha,\gamma}(d;T)
 =\sum_{\substack{
   k\le T/67^{\max(\alpha,\gamma)}\\
   k\ {\rm squarefree},\ (k,67d)=1}}
 {\mu(k)\over k}
 \left\langle
 V^{(\alpha)}_{k,d,T},V^{(\gamma)}_{k,d,T}
 \right\rangle_{L^2(\mathbf R)}.}
\tag{5.4}
\]

Indeed, insert

\[
 1_{(a,b)=1}=\sum_{k\mid(a,b)}\mu(k),
\tag{5.5}
\]

write \(a=kx,b=ky\), and use squarefreeness. The source signs become
\(\mu(x)\mu(y)\), the normalization contributes \(1/k\), and the common
factor cancels from the logarithmic ratio. Expanding the inner product in
(5.4) now recovers the rectangle term by term.

For the central channel, (5.4) is the signed energy identity

\[
 \mathcal G_{0,0}(d;T)
 =\sum_k{\mu(k)\over k}\|V^{(0)}_{k,d,T}\|_2^2.
\tag{5.6}
\]

This is a useful reduction to one-dimensional prefix fields, but not a
positivity proof: the outer coefficients in (5.6) have Möbius sign, the
exceptional channels are cross inner products, and (5.2) subtracts two
prefix rectangles. Taking absolute values at any of those three interfaces
would discard the cancellation sought by PRIMLS.

## 6. Exact harmonic Boolean-sieve transform

Fix one panel, \(H,U\), and a squarefree \(67\)-free modulus \(Q\). Split
the unsieved panel by its exact incidence with \(Q\):

\[
 W_e
 =\sum_{\substack{
   a,b\ {\rm squarefree},\ 67\nmid ab,\ (a,b)=1\\
   H<h_{\alpha,\gamma}(a,b)\le U,\ (ab,Q)=e}}
 {\mu(a)\mu(b)\over\sqrt{ab}}
 \mathcal R\!\left(\log{67^\alpha a\over67^\gamma b}\right),
 \qquad e\mid Q.
\tag{6.1}
\]

For every \(d\mid Q\), the sieve is the exact disjointness transform

\[
 \boxed{
 \mathcal P_{\alpha,\gamma}(d;H,U)
 =\sum_{\substack{e\mid Q\\(d,e)=1}}W_e.}
\tag{6.2}
\]

It is invertible, with

\[
 \boxed{
 W_e=\sum_{c\mid e}(-1)^{\omega(c)}
 \mathcal P_{\alpha,\gamma}
 \!\left({Q\over e}c;H,U\right).}
\tag{6.3}
\]

There is also an exact orthogonal form adapted to the \(d^{-1}\) weight in
PRIMLS. Put

\[
 Z_Q=\sum_{d\mid Q}{1\over d}
 =\prod_{p\mid Q}\left(1+{1\over p}\right),
 \qquad
 \nu_Q(d)={1\over Z_Qd}.
\tag{6.4}
\]

Under \(\nu_Q\), the indicators \(X_p(d)=1_{p\mid d}\) are independent
Bernoulli variables with mean \(1/(p+1)\). For \(S\mid Q\), define

\[
 \phi_S(d)=\prod_{p\mid S}\left(X_p(d)-{1\over p+1}\right),
 \qquad
 N_S=\|\phi_S\|_{L^2(\nu_Q)}^2
 =\prod_{p\mid S}{p\over(p+1)^2},
\tag{6.5}
\]

and \(b_S=\mathbb E_{\nu_Q}[\mathcal P(d)\phi_S(d)]\). Direct product
expectation in (6.2) gives

\[
 \boxed{
 b_S=(-1)^{\omega(S)}
 \prod_{p\mid S}{p\over(p+1)^2}
 \sum_{\substack{e\mid Q\\S\mid e}}
 W_e\prod_{p\mid e/S}{p\over p+1}.}
\tag{6.6}
\]

Biased-Boolean Parseval is therefore

\[
\boxed{
 {1\over Z_Q}\sum_{d\mid Q}{|\mathcal P(d)|^2\over d}
 =\sum_{S\mid Q}{|b_S|^2\over N_S}.}
\tag{6.7}
\]

In particular,

\[
 b_1=\mathbb E_{\nu_Q}[\mathcal P(d)]
 =\sum_{e\mid Q}W_e\prod_{p\mid e}{p\over p+1},
 \qquad
 {1\over Z_Q}\sum_{d\mid Q}{|\mathcal P(d)|^2\over d}
 \ge |b_1|^2.
\tag{6.8}
\]

This is the exact zero-frequency obstruction. If only the \(Q\)-free
stratum \(W_1\) is present, every sieve row equals \(W_1\), and (6.8) is an
equality. More concretely, if \(p>U\) and \(p\nmid67d\), then

\[
 \mathcal P_{\alpha,\gamma}(pd;H,U)
 =\mathcal P_{\alpha,\gamma}(d;H,U),
\tag{6.9}
\]

because neither primitive coordinate can contain \(p\). Such large-prime
sieve coordinates are exact repetitions, not new orthogonal samples.

Equations (6.2)--(6.9) neither prove nor disprove PRIMLS. They prove a
narrower firewall: no abstract orthogonality in the common-factor label can
erase the harmonic mean. A successful estimate must also control that mean
through the Möbius pair signs, and then control the nonzero Boolean modes.
The full truncated average \(d\le D\) is not replaced here by a divisor
cube.

## 7. Proof and scope ledger

| statement | grade |
|---|---|
| five-channel common-factor identity (0.4) | **PROVED EXACT** |
| dyadic reconstruction (0.5) | **PROVED EXACT** |
| five-to-three reciprocity reduction (0.6) | **PROVED EXACT** |
| square-root normalization (3.1) | **PROVED UNCONDITIONALLY** |
| rectangle increment and Möbius--Gram identity (5.2)--(5.6) | **PROVED EXACT** |
| divisor-sieve transform/inversion (6.2)--(6.3) | **PROVED EXACT** |
| harmonic Boolean Parseval and zero-frequency fence (6.4)--(6.9) | **PROVED EXACT** |
| PRIMLS implies RH | **PROVED AS A CONDITIONAL IMPLICATION** |
| PRIMLS estimate (0.8) | **OPEN / NOT PROVED** |
| RH implies PRIMLS | **NOT CLAIMED** |
| RH or GRH | **NOT PROVED** |

The packet makes no external novelty claim. It isolates a theorem-shaped
analytic gate for future comparison with averaged Chowla estimates,
dispersion methods, bilinear forms, or family large sieves.

## 8. Bounded replay

~~~text
python -B research/l-families/atlas/function_field/ffps_boundary_field_primitive_pair_large_sieve_gate.py --check
python -B -O research/l-families/atlas/function_field/ffps_boundary_field_primitive_pair_large_sieve_gate.py --check
python -B -m unittest tests.test_ffps_boundary_field_primitive_pair_large_sieve_gate
python -B -O -m unittest tests.test_ffps_boundary_field_primitive_pair_large_sieve_gate
~~~

The replay pins every imported source blob; checks the beta local states and
all five exceptional channels; compares the direct finite off-diagonal
shells with the exchanged \(d\)-panel formula in an exact formal square-root
basis; verifies channel reciprocity and dyadic reconstruction; and enforces
the conditional scope and resource caps. It also checks the rectangle
increment and Möbius lift, the disjointness transform and its inverse, the
harmonic Boolean Parseval identity on the divisor cube of \(30\), and one
frozen large-prime sieve coordinate. It enumerates no zeta zero, finite
field, curve, conductor family, or \(L\)-function.
