# The high primitive beta sector is a five-channel Möbius large-sieve problem

Status: **exact dyadic-shell and common-factor decomposition; conditional
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

## 5. Proof and scope ledger

| statement | grade |
|---|---|
| five-channel common-factor identity (0.4) | **PROVED EXACT** |
| dyadic reconstruction (0.5) | **PROVED EXACT** |
| five-to-three reciprocity reduction (0.6) | **PROVED EXACT** |
| square-root normalization (3.1) | **PROVED UNCONDITIONALLY** |
| PRIMLS implies RH | **PROVED AS A CONDITIONAL IMPLICATION** |
| PRIMLS estimate (0.8) | **OPEN / NOT PROVED** |
| RH implies PRIMLS | **NOT CLAIMED** |
| RH or GRH | **NOT PROVED** |

The packet makes no external novelty claim. It isolates a theorem-shaped
analytic gate for future comparison with averaged Chowla estimates,
dispersion methods, bilinear forms, or family large sieves.

## 6. Bounded replay

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
the conditional scope and resource caps. It enumerates no zeta zero, finite
field, curve, conductor family, or \(L\)-function.
