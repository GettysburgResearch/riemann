# Complete actual size-four Hankel positivity at every shift index

Status: complete actual-source analytic theorem with exact rational guards.
At the fixed shift t=1 put c=3/4 and b_n=c^n*C_(n+1)(1), using the
COMPLETE actual Xi logarithmic moments. Then

\[
 H_n^{[4]}=(b_{n+i+j})_{0\le i,j\le3}
 \succeq\frac{I}{30000000000000000000\,1250^{n+1}}
                         \quad\text{for EVERY integer }n\ge0.     \tag{F4.1}
\]

The lower bound holds on every complex coefficient vector. Every unknown
real/complex occurrence and positive multiplicity remains. The all-size
Hankel criterion and RH remain open. No new native root, moment, jet or
quadrature computation is performed; the finite checker evaluates only
exact rational guards and authenticates already accepted source inputs.

The source inputs are the independently accepted complete count-free real
head through R=5419, its first FOUR actual root intervals, strip half-width
A=1/2, inverse-square summability and actual theta/Jensen upper count
N(x)<x*log(x) for x>=1024. This is a bounded-head implication, not a
historical-count or all-height location assumption. The exact paired
source convention and source adapter are the same as in
`ALL_ORDER_TWO_BY_TWO_HANKEL.md`, SHA256
f1a0ac4be55d892708980ae47e05391054e9cd6e30e1ecb907d2b2cfafd463c8.

## F4.2. A full real-head Gram bound from four actual nodes

For z_rho=c/(rho^2+1), the complete matrix has the literal representation

\[
 H_n^{[4]}=\frac1c\sum_\rho m_\rho z_\rho^{n+1}
       (1,z_\rho,z_\rho^2,z_\rho^3)^T
       (1,z_\rho,z_\rho^2,z_\rho^3).                             \tag{F4.2}
\]

The complex-node terms are not positive Hermitian Gram terms. Conjugates
are retained separately, making the entire matrix real symmetric. The
first four actual REAL roots are authenticated inside

    (14.1347,14.1348), (21.02,21.03), (25.01,25.02), (30.42,30.43).

Their real nodes satisfy z_1>z_2>z_3>z_4>1/1250 and z_i<1/250.
The pairwise gaps have strict lower bounds with reciprocal denominators

\[
 d_{12}=500,\ d_{13}=400,\ d_{14}=350,\
 d_{23}=2100,\ d_{24}=1200,\ d_{34}=2700.                         \tag{F4.3}
\]

Let V be the four-row Vandermonde matrix with row (1,z_i,z_i^2,z_i^3).
Column j of V^(-1) is the coefficient vector of the exact Lagrange
polynomial prod_(i!=j)(x-z_i)/prod_(i!=j)(z_j-z_i). Each numerator has
squared coefficient norm below

\[
 1+(3/250)^2+(3/250^2)^2+(1/250^3)^2<2.
\]

The gap bounds consequently give

\[
 \begin{split}
 \|V^{-1}\|_F^2
 &<2\{(500\cdot400\cdot350)^2+(500\cdot2100\cdot1200)^2\\
 &\hspace{16mm}+(400\cdot2100\cdot2700)^2+(350\cdot1200\cdot2700)^2\}\\
 &=16044560000000000000<20000000000000000000.
 \end{split}                                                       \tag{F4.4}
\]

Thus V^T*V>I/20000000000000000000. Both realness and distinctness are
already certified by the actual root intervals; no midpoint inverse is
used. Every other complete real-head term is positive semidefinite, and
each selected actual multiplicity is at least one. Therefore

\[
 H_{n,\mathrm{head}}^{[4]}\succ
       \frac{I}{15000000000000000000\,1250^{n+1}}.                \tag{F4.5}
\]

## F4.6. Complete tail norm for every n>=5

AH5–AH6 in the size-two source proof apply unchanged to a polynomial of
degree three: the product of the two complex-coefficient polynomial
factors is bounded by ||a||^2*sum_(k=0)^3|z|^(2k), at most
||a||^2/(1-alpha^2), where alpha=c/(R^2+c)<1/39000000. The complete
count tail has sum m|z|<20c/R. Thus

\[
 |a^*H_{n,\mathrm{tail}}^{[4]}a|
       <\frac1{250}(1/39000000)^n\|a\|^2.                       \tag{F4.6}
\]

Relative to F4.5 this is at most
75000000000000000000*(1250/39000000)^n. Its exact rational value at
n=5 is below1/2, and its ratio decreases at every further integer index.
This proves F4.1 uniformly at every n>=5.

## F4.7. Polynomial conjugate-pair compensation for n=0,...,4

Absolute error is too crude at low orders. Let z=x+i*y be one remaining
nonreal node, whose conjugate has the same multiplicity m. For a complex
coefficient vector a, write

\[
 R_a=\sum_{k=0}^3a_k\Re(z^k),\quad
 I_a=\sum_{k=0}^3a_k\Im(z^k),\quad w=z^{n+1}=u+i*v.
\]

The full pair quadratic form before2m/c is exactly

\[
 u(|R_a|^2-|I_a|^2)-2v\Re(R_a\overline{I_a})
       =u|R_a-(v/u)I_a|^2-\frac{|w|^2}{u}|I_a|^2.              \tag{F4.7}
\]

For every unknown gamma>R, Re(rho^2+1)>=gamma^2+c and
|Im(rho^2+1)|<=gamma. Hence |arg(z)|<1/gamma<1/R. For0<=n<=4,
|(n+1)arg(z)|<5/R, so cos((n+1)arg(z))>1/2 and u>|w|/2.
This uses only cos(theta)>=1-theta^2/2 and5/R<1. The complete positive
square in F4.7 is retained before bounding its negative price.

The exact telescoping identity for z^k-conj(z)^k gives
|Im(z^k)|<=k*|z|^(k-1)*|y|. Cauchy–Schwarz thus gives

\[
 |I_a|^2\le\|a\|^2y^2(1+4|z|^2+9|z|^4)<2y^2\|a\|^2.
\]

Combining these bounds, and counting both members of each pair, the
per-occurrence negative price is at most

\[
       \frac4c|z|^{n+1}y^2
              \le4c^{n+2}\gamma^{-2n-8}.                       \tag{F4.8}
\]

Here |z|<=c/gamma^2 and |y|<=c/gamma^3. Real unknown occurrences are
positive semidefinite and cause no negative price. This argument holds
for complex a; replacing complex-node terms with an absolute square
would give a different, invalid proof.

For any p>=8, closed-head Stieltjes summation and N(x)<x*log(x) give

\[
 \begin{split}
 \sum_{\gamma>R}m\gamma^{-p}
 &\le p\int_R^\infty x^{-p}\log(x)\,dx\\
 &=pR^{1-p}\left(\frac{\log R}{p-1}+\frac1{(p-1)^2}\right)
       <\frac{512}{49}R^{1-p}.                                 \tag{F4.9}
 \end{split}
\]

The last constant follows from logR<9 and the decreasing factors
p/(p-1)<=8/7,1/(p-1)<=1/7. The negative closed-head endpoint and the
vanishing upper endpoint are paid exactly as in the earlier tail proof.
Setting p=2n+8 in F4.8 bounds the ENTIRE signed low-order tail below by

\[
 -\frac{2048c^2}{49R^7}(c/R^2)^n\|a\|^2.                    \tag{F4.10}
\]

Relative to F4.5 its upper price is

\[
 \frac{2048c^2}{49R^7}(15000000000000000000\cdot1250)
                       (1250c/R^2)^n.
\]

The exact prefactor is below1/2 and1250c/R^2<1. This covers all five
low orders and completes F4.1 at EVERY n>=0. All sums used above are
absolutely convergent by the same complete source count.

## F4.11. Exact hierarchy boundary

Every principal size-three and size-two submatrix is positive as well.
The separate size-two certificate has a stronger quantitative constant
and remains unchanged. The all-order size-four result is larger than a
finite moment table: it covers infinitely many actual native moments
using one complete spectral source argument.

The universal Hankel criterion requires all polynomial degrees, not just
degrees at most three and their index shifts. No passage to unbounded
matrix size, all mixed signs or RH is supplied. The complete unknown tail
can remain signed in larger polynomial tests. A finer known-head norm or
a whole-source high-degree mechanism is still needed for that criterion.
