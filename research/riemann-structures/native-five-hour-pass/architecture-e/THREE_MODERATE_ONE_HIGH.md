# Three moderate nodes coupled to one high node

Status: SOURCE-EXACT THEOREM; independently reviewed and replayed at the
frozen checkpoint recorded in `THREE_CLUSTER_REPLAY.md`.
Scope: three nodes in [64,256], one further node at least 2^34, and all
confluences in the moderate block.

With the Architecture E notation \(Y(x)=\xi(1/2+x)\), \(F=Y'/Y\),
\(H(x,y)=(F(x)+F(y))/(x+y)\), \(C(x,y)=1/(x+y)\), the result is:

**Theorem E31.** If \(64\le x_1,x_2,x_3\le256\) and \(y\ge2^{34}\), then
\[
                         H\succeq\frac1{200}C.              \tag{E31.1}
\]
For distinct nodes in this order, the normalized last Newton residual is at
least
\[
                  \frac1{400y\prod_{i=1}^3(x_i+y)^2}.       \tag{E31.2}
\]
The statement includes the full threefold moderate jet. It is not obtained
from a sampled order-three PSD packet.

## 1. Literal three-dimensional source reserve at 64

Apply the finite E4 operator decomposition in dimension three at minimum
node 64. The logarithmic Hermitian loss is now 1. Since
\[
 \frac{64+1/2}{2\pi}>\frac{903}{88}>10>e^{23/10},
\]
the logarithm contributes more than \(3/20\). The inequalities
\(\pi<22/7\) and \(e^{23/10}<10\) have exact positive-integral/Taylor proofs.

For \(c=1/2\), put \(q=(64+c)/(64-c)=129/127\). The exact negative-shift
resolvent majorant is
\[
 J_3=\frac1{64-c}+\frac{128}{(64-c)^2}(1+q)
     =\frac{163330}{2048383}.
\]
Its Hermitian loss is \(cJ_3^2<1/300\). The complete digamma remainder is at
most
\[
                         \frac9{64+c}=\frac6{43}.
\]
The dimension-three weighted Malmquist constant has square
\(2(1+25+625)=1302<37^2\). After \(\Lambda(m)\le m\), the literal prime
remainder is at most
\[
 37\sum_{m\ge2}m^{-31}
 \le37(2^{-31}+2^{-30}/30)
 =\frac{37}{2013265920}<10^{-7}.                           \tag{E31.3}
\]
Both negative source remainders have therefore been retained, and
\[
 \operatorname {Re}F(L)>
 \left(\frac3{20}-\frac1{300}-\frac6{43}-10^{-7}\right)I
 >\frac1{200}I.                                            \tag{E31.4}
\]
The finite jet construction proves this directly through every collision.

For later use, the scalar diagonal is below 4 on [64,256]. Every strict
upper entry of \(F(L)\) has modulus below
\[
                1+\frac1{10}+\frac1{10}+\frac17+10^{-7}
                <\frac32.
\]
These terms are the half-logarithm, two rational resolvents, the complete
digamma remainder and the Euler series. Hence the row/column norm bound gives
\[
                              \|F(L)\|<7.                   \tag{E31.5}
\]

## 2. One-column source interface

In the orthonormal Malmquist basis,
\[
 A=\begin{pmatrix}L&v\\0&y\end{pmatrix},\qquad
 v_i=2\sqrt{x_i y}.
\]
The exact Sylvester column \(r=(yI-L)^{-1}v\) gives
\[
 F(A)=\begin{pmatrix}F(L)&w\\0&F(y)\end{pmatrix},\qquad
 w=rF(y)-F(L)r.                                            \tag{E31.6}
\]
For \(y\ge16\cdot256\), the three-node resolvent product has diagonal at most
\(1/(y-256)\). Adjacent upper entries are at most
\(512/(y-256)^2\), and the one far entry is at most
\(1024/(y-256)^2\), because its single intermediate product is below 2.
Thus
\[
 \|(yI-L)^{-1}\|
 \le\frac1{y-256}+\frac{2048}{(y-256)^2}<\frac2y.           \tag{E31.7}
\]
The final inequality follows on writing \(u=y/256\ge16\):
\(u/(u-1)+8u/(u-1)^2<2\). Also
\[
                 \|v\|^2=4y(x_1+x_2+x_3)\le3072y<56^2y.
\]
Therefore \(\|r\|<112/\sqrt y\). The scalar source bound
\(F(y)<\tfrac12\log(2y)+1\) and (E31.5) give
\[
                 \|w\|<
 \frac{112}{\sqrt y}[\tfrac12\log(2y)+8].                  \tag{E31.8}
\]
At \(y\ge R=2^{34}\) the scalar-over-square-root function decreases, and
\[
 \|w\|<\frac{112(35/2+8)}{2^{17}}
       =\frac{2856}{131072}<\frac7{200}.                   \tag{E31.9}
\]

## 3. Schur conclusion and boundary

The high scalar satisfies \(F(y)>1/8\) by E4. Subtract
\(\delta=1/400\) from \(\operatorname {Re}F(A)\). The moderate block remains
above \(I/400\), the high scalar above \(49/400\), and the Hermitian
off-column has norm below \(7/400\). Since
\[
                  (1/400)(49/400)=(7/400)^2
\]
and the off-column inequality is strict, the block Schur complement is
positive. Hence \(\operatorname {Re}F(A)>\delta I\). The finite source Gram
identity gives the relative factor \(2\delta=1/200\) in (E31.1), and the
Cauchy/Newton residual gives (E31.2).

This theorem advances the three-moderate-node domain using the actual gamma
and Euler source decomposition. It does not require a strictness upgrade to
the integrated order-three theorem. Nodes below64 in a three-dimensional
moderate block, four all-moderate nodes, and RH remain open. The separate
bounded scout identifies the fully confluent endpoint chamber as numerically
hard, but no scout result is used here.
