# Complete actual shifted moments are strictly log-convex at every order

Status: complete actual-source analytic theorem with exact rational guards.
For the COMPLETE actual Xi logarithmic moments at shift t=1,

\[
 C_k(1)C_{k+2}(1)>C_{k+1}(1)^2\qquad\text{for EVERY integer }k\ge1.
                                                                  \tag{AH1}
\]

The entire unknown real/complex tail and all multiplicities remain. More
quantitatively, put c=3/4, b_n=c^n*C_(n+1)(1) and

\[
 H_n=\begin{pmatrix}b_n&b_{n+1}\\b_{n+1}&b_{n+2}\end{pmatrix}.
 \quad H_n\succeq\frac{I}{1125000\,600^{n+1}}
                 \quad\text{for EVERY integer }n\ge0.             \tag{AH2}
\]

This holds on all complex coefficient vectors. It is all-order positivity
of size-two Hankel matrices, not positivity of every Hankel size or RH.
The source inputs are the independently accepted complete count-free real
head through5419, the first two actual root intervals, classical strip
half-width1/2, inverse-square summability, and complete actual theta/Jensen
upper count N(x)<x*log(x)<=x^2 for x>=1024. No new root, moment or native
quadrature computation is performed.

## AH3. Exact complete source and the retained real head

For every positive-real representative rho=gamma+i*beta, let
z_rho=c/(rho^2+1), with positive integer multiplicity m. Then

\[
 H_n=\frac1c\sum_\rho m_\rho z_\rho^{n+1}
                 \begin{pmatrix}1&z_\rho\\z_\rho&z_\rho^2\end{pmatrix}.
                                                                  \tag{AH3}
\]

Conjugates are retained separately; the complete sum is a real symmetric
matrix. At complex nodes its terms are not positive Hermitian Gram terms.
For a complex vector (a_0,a_1), the literal term is
z^(n+1)(a_0+a_1*z)(conj(a_0)+conj(a_1)*z)/c, so replacing it with an
absolute square at the same complex node would be invalid.

The first two actual real roots are authenticated inside
(14.1347,14.1348) and (21.02,21.03). Their positive real nodes z_1,z_2
satisfy the exact rational bounds

\[
 z_1-z_2>1/500,\quad z_2>1/600,\quad z_1^2+z_2^2<1.
\]

For V with rows (1,z_1),(1,z_2), det(V^T*V)=(z_1-z_2)^2 and
trace(V^T*V)<3. Its least eigenvalue is at least determinant/trace, hence
V^T*V>I/750000. Both selected multiplicities are at least one. Every
other complete real-head term is positive semidefinite. Therefore

\[
              H_{n,\mathrm{head}}\succ
                   \frac{I}{562500\,600^{n+1}}.                  \tag{AH4}
\]

All roots at or below R=5419 belong to that complete real head.

## AH5. Uniform full-tail bound for n>=2

For every remaining gamma>R, |z|<=alpha=c/(R^2+c)<1/39000000.
Closed-head Stieltjes summation and N(x)<x*log(x) give

\[
 \begin{split}
 \sum_{\gamma>R}m|z_\rho|
 &\le c\sum_{\gamma>R}m(\gamma^2+c)^{-1}\\
 &\le2c\int_R^\infty x^2\log(x)/(x^2+c)^2\,dx\\
 &\le2c\int_R^\infty\log(x)/x^2\,dx
   =2c(\log R+1)/R<20c/R.
 \end{split}                                                       \tag{AH5}
\]

The nonpositive closed-head endpoint is discarded safely; the upper
endpoint vanishes. The final strict bound uses R<(27/10)^9<e^9, proved
by exact fractions and e>65/24>27/10. This also establishes absolute
summability of all matrix terms.

For complex coefficients, Cauchy–Schwarz bounds both polynomial factors
in AH3, without assuming a complex-node absolute-square representation.
Consequently the absolute tail quadratic form is bounded by

\[
 \frac{20}{R}\frac{\alpha^n}{1-\alpha^2}\|a\|^2
    <\frac1{250}\left(\frac1{39000000}\right)^n\|a\|^2.          \tag{AH6}
\]

Relative to AH4 its price is less than1350000/65000^n, which is below1/2
at n=2 and decreases thereafter. Thus AH2 follows for EVERY n>=2.
No enumeration of the infinitely many orders is used.

## AH7. Exact conjugate-pair compensation at n=0 and n=1

The preceding absolute estimate is too crude for the two low orders.
The full conjugate-pair algebra keeps its positive rank-one part. Write
z=x+i*y for one unknown pair, whose conjugate has the same multiplicity m.
Since D=rho^2+1 has Re D>=gamma^2+c and |Im D|<=gamma,

\[
 x>0,\quad |y|/x<1/\gamma<1/R,\quad |z|\le c/\gamma^2.
\]

At n=0 the pair matrix before2m/c is

\[
 \begin{pmatrix}x&x^2-y^2\\x^2-y^2&x^3-3xy^2\end{pmatrix}.
\]

Completing its real-coefficient square, valid also on complex vectors,
bounds its quadratic form below by
-y^2*|z|^2/x*|a_1|^2. At n=1 the corresponding first diagonal is
x^2-y^2>0, off-diagonal x^3-3xy^2 and second diagonal
x^4-6x^2*y^2+y^4. Its determinant is exactly
-y^2*(x^2+y^2)^2, so the same Schur completion gives lower bound
-y^2*|z|^4/(x^2-y^2)*|a_1|^2.

Every real tail occurrence is positive semidefinite and can be retained
or discarded in a lower bound. Counting BOTH members of each nonreal pair
with their multiplicities, their per-occurrence negative prices obey

\[
 \frac1c\frac{y^2|z|^2}{x}\le c^2\gamma^{-8},\qquad
 \frac1c\frac{y^2|z|^4}{x^2-y^2}\le2c^3\gamma^{-10}.             \tag{AH7}
\]

For the first inequality use
y^2*|z|^2/x=c^3*(Im D)^2/[Re D*|D|^4]. For the second use
x^2-y^2>=x^2/2 and |D|>=Re D>=gamma^2. These inequalities retain
the complete pair and cannot be inferred by deleting its negative part.

Closed-head Stieltjes summation with N(x)<=x^2 gives
sum_(gamma>R)m*gamma^(-p)<=p*R^(2-p)/(p-2), for p>2. Thus the whole
negative prices at n=0 and n=1 are respectively at most

\[
        4c^2/(3R^6),\qquad5c^3/(2R^8).                          \tag{AH8}
\]

The checker verifies that each is strictly below half of its AH4 head
gap. This completes AH2 for n=0 and n=1 as well. Every complex vector,
every unknown pair, the complete tail count and all multiplicities have
been included; ordinary samples or presumed tail reality are not used.

## AH9. Implication and exact remaining hierarchy

The positive determinant in AH2 equals
c^(2n+2)[C_(n+1)(1)*C_(n+3)(1)-C_(n+2)(1)^2], proving AH1 at
ALL k=n+1>=1. This also directly establishes positivity of the associated
scalar diagonal moments at this fixed shift.

The complete all-size Hankel criterion remains unproved. A finite real
head can dominate signed high nodes in every size-two test without making
every larger polynomial test positive. The constructive off-real witness
argument still requires some finite higher-degree test if an off-real
occurrence exists. This theorem supplies no all-size passage, cofinal
census, simplicity conclusion or RH statement.
