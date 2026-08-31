# Two moderate nodes coupled to two high nodes

Status: PROPOSED source-exact theorem; review and bounded replay pending.
Scope: two nodes in [32,256], at most two further nodes at least 2^40,
with every confluence inside either cluster. No claim covers a low/high
collision or three nodes below 256.

Use the Architecture E notation
\[
 Y(x)=\xi(\tfrac12+x),\qquad F=Y'/Y,\qquad
 H(x,y)=\frac{F(x)+F(y)}{x+y},\qquad C(x,y)=\frac1{x+y}.
\]

**Theorem E22.** If \(32\le x_1,x_2\le256\) and each of at most two
\(y_j\) is at least \(2^{40}\), then on the corresponding finite
exponential-jet space
\[
             H\succeq \frac1{50}C.                         \tag{E22.1}
\]
Both moderate nodes and both high nodes may separately coalesce. For four
distinct nodes in this order, the normalized final Newton residual is at least
\[
 \frac1{100y_2(x_1+y_2)^2(x_2+y_2)^2(y_1+y_2)^2}.           \tag{E22.2}
\]
This is a different extension from the one-low-node packet: it allows a
two-dimensional moderate block, rather than lowering a scalar threshold.

## 1. A two-dimensional source block is already coercive at 32

The proof of 'FOUR_NODE_HIGH_AXIS.md' applies in every smaller dimension with
its dimension-dependent constants. Let \(L\) be the finite Malmquist matrix
for two nodes at least 32. Put \(c=1/2\). The Hermitian logarithm bound loses
only \(1/2\) off the diagonal. Since
\[
 \frac{32+c}{2\pi}>\frac{455}{88}>\frac92>e^{3/2},
\]
it contributes more than \(1/4\). Here \(\pi<22/7\) is the same positive
integral bound used in E4. The last exponential comparison follows from the
degree-16 Taylor upper bound \(e^3<81/4\).

The negative-shift resolvent majorant is
\[
 J_2(32)=\frac1{32-c}+\frac{64}{(32-c)^2}=\frac{382}{3969}<\frac1{10}.
\]
The exact accretive-resolvent identity therefore bounds its negative
Hermitian part by \(cJ_2(32)^2<1/200\). The positive-shift resolvent has
nonnegative Hermitian part.

The literal digamma remainder has norm at most
\(3/(32+c)<1/10\). The weighted Malmquist constant in dimension two has
square \(2(1+25)=52<8^2\). After \(\Lambda(m)\le m\), the complete Euler-prime
remainder is bounded by
\[
 8\sum_{m\ge2}m^{-15}
 \le8\left(2^{-15}+\frac{2^{-14}}{14}\right)
 =\frac1{3584}<\frac1{3000}.                               \tag{E22.3}
\]
This retains both the archimedean and prime source terms. Consequently
\[
 \operatorname {Re}F(L)>
 \left(\frac14-\frac1{200}-\frac1{10}-\frac1{3000}\right)I
 =\frac{217}{1500}I>\frac18I.                              \tag{E22.4}
\]
The argument acts directly on the repeated-node jet space, so (E22.4) is
uniform through \(x_1=x_2\).

We will also need an upper norm bound when the nodes are at most 256. The
scalar source decomposition gives \(0<F(x)<\tfrac12\log(2x)+1<4\).
Every strict upper entry of \(F(L)\) is less in modulus than
\[
 1+\frac1{10}+\frac1{10}+\frac1{10}+\frac1{3000}<\frac75:
\]
these are respectively the logarithm, two rational resolvents, digamma
remainder and Euler-prime remainder. Hence
\[
                         \|F(L)\|<\frac{27}{5}<6.           \tag{E22.5}
\]

## 2. Exact two-by-two Sylvester interface

Order the moderate cluster first. In the orthonormal Malmquist basis,
\[
 A=\begin{pmatrix}L&V\\0&B\end{pmatrix},\qquad
 V_{ij}=2\sqrt{x_i y_j}.
\]
The spectra are disjoint. There is a unique row-block \(R_*\) solving
\[
                         R_*B-LR_*=V.                       \tag{E22.6}
\]
Thus, with \(P=\left(\begin{smallmatrix}I&R_*\\0&I\end{smallmatrix}\right)\),
\[
 AP=P\operatorname {diag}(L,B),\qquad
 F(A)=\begin{pmatrix}F(L)&W\\0&F(B)\end{pmatrix},\quad
 W=R_*F(B)-F(L)R_*.                                        \tag{E22.7}
\]
This is finite holomorphic functional calculus. It assumes no closable
ambient operator. It also proves the exact obstruction statement: a bootstrap
from a merely semidefinite lower block can work only if \(W^*\) kills its
nullspace. An arbitrarily small nonzero component along a null vector makes
the Hermitian block indefinite. This is why the canonical order-three PSD
statement alone cannot replace the quantitative estimate (E22.4).

Write \(r_1,r_2\) for the columns of \(R_*\), and \(v_j\) for those of \(V\).
The triangular high source block gives
\[
 (y_1I-L)r_1=v_1,\qquad
 (y_2I-L)r_2=v_2-2\sqrt{y_1y_2}\,r_1.                      \tag{E22.8}
\]
The exact two-node resolvent product gives, for \(y\ge2^{16}\),
\[
 \|(yI-L)^{-1}\|
 \le\frac1{y-256}+\frac{512}{(y-256)^2}<\frac2y.            \tag{E22.9}
\]
The last inequality is the positive polynomial
\(y^2-1280y+131072>0\), increasing after 640 and positive at \(2^{16}\).
Also
\[
 \|v_j\|^2=4y_j(x_1+x_2)\le2048y_j<46^2y_j.
\]
Equations (E22.8)--(E22.9) therefore give
\[
                  \|r_1\|<\frac{92}{\sqrt{y_1}},\qquad
                  \|r_2\|<\frac{460}{\sqrt{y_2}}.          \tag{E22.10}
\]

For the two-dimensional high block, E4 gives
\(\operatorname {Re}F(B)>I/8\), every strict upper entry of \(F(B)\) has
modulus below 2, and
\(F(y)<\tfrac12\log(2y)+1\). Combining this with (E22.5) and (E22.10),
\[
 \begin{aligned}
 \|w_1\|&<\frac{92}{\sqrt{y_1}}
                  [\tfrac12\log(2y_1)+7],\\
 \|w_2\|&<\frac{184}{\sqrt{y_1}}+
          \frac{460}{\sqrt{y_2}}[\tfrac12\log(2y_2)+7].
 \end{aligned}                                             \tag{E22.11}
\]
The displayed scalar-over-square-root function decreases on this domain.
At \(R=2^{40}\), using \(\log2<1\),
\[
 \|W\|\le\|w_1\|+\|w_2\|
 <\frac{552(55/2)+184}{2^{20}}
 =\frac{15364}{2^{20}}<\frac1{64}.                         \tag{E22.12}
\]
The estimate allows arbitrary ratios and collision within the high cluster.

## 3. Schur conclusion and exact boundary

Subtract \(\delta=1/100\) from \(\operatorname {Re}F(A)\). Both diagonal
blocks remain at least \(23I/200\), while the Hermitian off-block has norm
less than \(1/128\). Since
\[
                   (23/200)^2>(1/128)^2,
\]
the block Schur complement is positive. Hence
\(\operatorname {Re}F(A)>\delta I\). The finite source Gram identity gives
(E22.1), with relative factor \(2\delta=1/50\), and the exact Newton/Cauchy
residual gives (E22.2).

The theorem pays the literal Euler-prime and gamma remainders in both source
blocks. Its moderate-block estimate is analytic and uniform, not a finite PSD
census. The proposed replay checks the finite Sylvester identities, original
exponential functions and every rational inequality. It does not prove the
continuum estimates by sampling.

The remaining gaps are substantial: nodes below 32 in a two-dimensional low
block, a moderate third node, and the full four-node safe axis remain open.
The Sylvester nullspace criterion makes precise why unquantified order-three
semidefiniteness does not by itself close any of these gaps. RH is not proved.
