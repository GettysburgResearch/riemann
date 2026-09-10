# Infinite-core metric obstruction and a tail-complete trace-sign attempt

**SC26 — 2026-09-10. Proposed component proofs, pending independent review.**
The requested unconditional RH proof was not obtained. This manuscript proves
an obstruction for the **actual** theta-source operator, supplies a complete
trace-based alternative criterion, and tests a proposed source-positivity
completion against a fully controlled countermodel. The all-order sign for the
actual theta source remains **OPEN**, not a routine verification left to referees.

Source: PR #834 at `f0e34780f4fe91bd5d07e791e8855189838c3df5`,
`standalone/2026-09-09-centered-theta-determinant/PROOF.md`, blob
`ef01f74c50d4efacb615176cbfed4a3de2fd1147`. Its original manuscript is unchanged.
That source rules out bounded positive metrics on the full space and every
finite derivative cut. Section 3 below addresses the **infinite intersection**
left open there. This is not a claim of an externally new general spectral or
moment criterion. Classical mechanisms and precise imports are identified below.

## 1. The unchanged source and the inherited characteristic construction

Keep exactly

\[
\Xi(z)=\xi(1/2+iz)=\int_{\mathbb R}\phi(t)e^{izt}\,dt,
\quad
\phi(t)=\sum_{n\ge1}(4\pi^2n^4e^{9t/2}-6\pi n^2e^{5t/2})
                         e^{-\pi n^2e^{2t}}.
\]

Jacobi inversion gives evenness. For nonnegative t every summand is positive;
reflection gives positivity everywhere. Write

\[
w=\phi/\Xi(0),\quad c(z)=\Xi(z)/\Xi(0),\quad
F(x)=\int_{-\infty}^x w(t)\,dt,\quad Q=1-F,
\quad H_w=L^2(\mathbb R,w(t)dt).
\]

The inner product is conjugate-linear in its first slot. All exponential
moments exist. In particular

\[
\mu_2=\int t^2w(t)dt\in(0,\infty),\qquad
c(iy)=\int w(t)\cosh(yt)dt>0\quad(y\in\mathbb R).                 \tag{1}
\]

The latter excludes imaginary-axis zeros without assuming RH.

The centered antiderivative and odd trace-class operator of the source are

\[
(Kf)(x)=\int_{\mathbb R}(1_{t<x}-Q(t))f(t)dt,
\qquad T=-K^2|_{H_o},                                               \tag{2}
\]

where H_o is the odd subspace. The integral in (2) uses **Lebesgue dt**, not
w(t)dt. Keep its cancellation; the separated Volterra pieces need not be bounded.
The source proves, and this manuscript imports with that precise domain,

\[
(Kf)'=f,\quad \langle1,Kf\rangle=0,\quad
\|K\|_{HS}^2=I_w=\int_{\mathbb R}\frac{FQ}{w}<\infty,
\quad \det_{H_o}(I-z^2T)=c(z).                                      \tag{3}
\]

For orientation, the integral bound follows from
\(w(t)\asymp e^{9t/2-\pi e^{2t}}\) at positive infinity and reflection:
\(Q(t)/w(t)=O(e^{-2t})\). The determinant is not a new assumption about zero
locations. On a bounded interval the centered Volterra/rank-one calculation
gives the centered moment-generating function; symmetric conditional cutoffs
converge in Hilbert--Schmidt norm, and parity removes determinant regularization.
The full proof and its classical determinant imports are in the pinned source.
We have not rerun its numerical package or formalized its operator-domain proof.

Define

\[
q_j=w^{(j)}/w,\qquad
W_\infty=\{f\in H_w:\langle q_j,f\rangle=0\text{ for every }j\ge0\}.
\]

Every q_j belongs to H_w. The source's identities
\(K^*q_0=0\), \(K^*q_{j+1}=-q_j\) show that W_infinity is closed and K-invariant.
Parity also preserves it. Put

\[
K_\infty=K|_{W_\infty},\qquad
T_\infty=T|_{W_\infty\cap H_o}.                                    \tag{4}
\]

These are restrictions in the original weighted Hilbert metric, not quotients
with a freely selected norm.

## 2. Exact zero states and the sharp two-vector metric cost

For u nonzero, direct differentiation and mean subtraction give

\[
K e^{ut}=\frac{e^{ut}-M(u)}u,\qquad M(u)=\int e^{ut}w(t)dt=c(-iu).
                                                                    \tag{5}
\]

If c(z)=0, then \(e^{izt}\) is an eigenvector with eigenvalue \(1/(iz)\).
It belongs to W_infinity because, with vanishing endpoint terms,

\[
\langle q_j,e^{izt}\rangle=\int w^{(j)}(t)e^{izt}dt=(-iz)^j c(z)=0.   \tag{6}
\]

If z is a multiple zero, \(te^{izt}\) also belongs to W_infinity, by
differentiating (6). Differentiation of (5), at u=iz, gives

\[
(K-1/u)(te^{ut})=-e^{ut}/u^2\ne0.                                  \tag{7}
\]

Thus a multiple zero supplies an actual nontrivial Jordan chain in the
infinite core; it is not lost by the restriction.

On the odd space, direct use of (5) gives for all nonzero z

\[
T\sin(zt)=z^{-2}\sin(zt)-z^{-1}c(z)t.                               \tag{8}
\]

At a zero this is an eigenvector identity. At a multiple zero, differentiating
(8) gives

\[
(T-z^{-2})(t\cos(zt))=-2z^{-3}\sin(zt)\ne0.                         \tag{9}
\]

Both states are in the odd infinite core, by (6) and its derivative.

**Two-vector lemma.** Suppose u,v have norm one, \(r=|\langle u,v\rangle|<1\),
and a bounded self-adjoint G satisfies \(aI\le G\le bI\), a>0, and
\(\langle u,Gv\rangle=0\). Then

\[
\frac ba\ge\frac{1+r}{1-r}.                                        \tag{10}
\]

Indeed change the phase of v so its ordinary inner product with u is r.
The two G-quadratic values at u+v and u-v are the same, say S. Their ordinary
squared norms are 2(1+r), 2(1-r). Hence
\(a\le S/[2(1+r)]\) and \(b\ge S/[2(1-r)]\), proving (10).
It is sharp on the two-dimensional span: assign eigenvalues 1/(1+r) and
1/(1-r) to the orthogonal vectors u+v and u-v. This makes u,v G-orthogonal.
The checker reproduces six rational instances of this sharp construction.

## 3. No bounded positive metric exists even on the infinite core

**SC26-1.** There is no bounded G=G*>=aI, a>0, on W_infinity satisfying

\[
K_\infty^*G+GK_\infty=0.                                           \tag{11}
\]

There is also no such G on the odd infinite core satisfying

\[
T_\infty^*G=GT_\infty.                                             \tag{12}
\]

The result is unconditional for the actual theta source. It does **not**
disprove RH, exclude unbounded metrics, or exclude a different Hilbert--Polya
construction. It removes one specific proposed finishing route, including the
infinite restriction left open in the predecessor.

**Proof for K.** Suppose (11) holds. Conjugation by G^(1/2) makes K_infinity
skew-adjoint. Thus its eigenvalues are imaginary and it has no nontrivial
Jordan chains. Equations (5)--(7) would force every Xi zero to be real and
simple. These conclusions are consequences of the supposition, not unproved
inputs to an unconditional argument.

Use the classical unconditional zero-count asymptotic

\[
N(H)=\frac H{2\pi}\log\frac H{2\pi}-\frac H{2\pi}+O(\log H).        \tag{13}
\]

Here N counts positive zeta ordinates with analytic multiplicity. Under the
supposition they are now distinct positive real Xi zeros. There are
\((1+o(1))H\log H/(2\pi)\) of them in [H,2H]. By summing consecutive gaps,
for every sufficiently large H two distinct such zeros gamma,eta satisfy

\[
0<\delta=\eta-\gamma\le4\pi/\log H.                                \tag{14}
\]

No numerical zero locations, pair-correlation conjecture, or independent
simplicity conjecture is being used.

The states u_gamma=e^(i gamma t) have norm one and exact correlation

\[
\langle u_\gamma,u_\eta\rangle=c(\delta),\qquad
1-c(\delta)\le\mu_2\delta^2/2,                                    \tag{15}
\]

by 1-cos x<=x^2/2. Strict positivity of w on the real line gives
|c(delta)|<1 when delta is nonzero; c(delta)>0 for all sufficiently small delta.
Distinct eigenvalues must be G-orthogonal. Apply (10) and (15):

\[
\kappa(G):=\|G\|\|G^{-1}\|
\ge\frac4{\mu_2\delta^2}-1
\ge\frac{(\log H)^2}{4\pi^2\mu_2}-1.                               \tag{16}
\]

The right side is unbounded, contradicting a fixed bounded coercive G.

**Proof for T.** Under (12), conjugation by G^(1/2) is self-adjoint.
Equation (8) forces z^(-2) real at every Xi zero. Such z is real or purely
imaginary, and (1) excludes the latter. Equation (9) excludes multiple zeros.
Consequently the same counting and pair selection apply.

Set f_gamma(t)=sin(gamma t), v_gamma=f_gamma/||f_gamma||. Exactly

\[
\|f_\gamma\|^2=\tfrac12[1-c(2\gamma)]\longrightarrow\tfrac12,
\]

by the Riemann--Lebesgue lemma. For all sufficiently large gamma its norm is
at least 1/2. Pointwise Lipschitz continuity of sine on the real axis gives
\(\|f_\eta-f_\gamma\|\le\delta\sqrt{\mu_2}\). Normalization then yields

\[
\|v_\eta-v_\gamma\|\le4\delta\sqrt{\mu_2},\qquad
1-\langle v_\gamma,v_\eta\rangle\le8\mu_2\delta^2.                  \tag{17}
\]

For the small gaps under consideration the correlation is positive. Distinct
positive eigenvalues force G-orthogonality, so

\[
\kappa(G)\ge\frac1{4\mu_2\delta^2}-1
\ge\frac{(\log H)^2}{64\pi^2\mu_2}-1,                              \tag{18}
\]

again impossible. No rate in the Riemann--Lebesgue lemma was required.

Equations (16),(18) also give quantitative necessary costs for metrics on
finite spans containing these states, whenever those real simple zeros are
present. They are not unconditional assertions that RH or simplicity holds.
The obstruction concerns an equivalent positive norm: it does not preclude
real spectrum of a compact highly nonnormal operator.

## 4. A trace criterion that does not demand a bounded metric

The failed metric route imposes more than spectral reality, notably
semisimplicity and uniform angular separation. We therefore attack only the
needed reality, allowing algebraic multiplicity.

We first give a complete power-sum lemma. This is in the classical
Grommer/Chebotarev moment-test tradition; no external novelty is claimed.
The explicit tail accounting is included so it cannot be replaced by a
finite zero census.

Let (lambda_j) be a finite or countable nonzero complex multiset, closed under
conjugation with matching positive integer multiplicities, and
\(\sum_j|\lambda_j|^2<\infty\). Repetitions count multiplicities. Define

\[
s_n=\sum_j\lambda_j^{n+2},\qquad H_d=(s_{i+j})_{0\le i,j\le d}.
\]

All these sums converge absolutely. The matrices are real symmetric.

**SC26-2.** All H_d are positive semidefinite if and only if every lambda_j
is real. This statement allows repeated values; it is not a simplicity test.

**Proof.** For a real polynomial p,

\[
\mathcal L(p^2)=\sum_j\lambda_j^2p(\lambda_j)^2
=\sum_{a,b}p_a p_b s_{a+b}.                                        \tag{19}
\]

If all values are real, every summand is nonnegative. Conversely suppose
alpha is nonreal, of multiplicity h. Choose 0<r<|alpha| and let S be the
finite set of distinct spectral values of modulus greater than r. It is
conjugation invariant. Let L_alpha and L_baralpha be their Lagrange cardinal
polynomials on the **entire** set S. For integer m>=0 put

\[
p_m(z)=z^m\left[i\alpha^{-m-1}L_\alpha(z)
             -i\bar\alpha^{-m-1}L_{\bar\alpha}(z)\right].           \tag{20}
\]

Conjugation shows p_m has real coefficients. It equals i/alpha and
-i/baralpha at the selected pair and vanishes at every other value in S.
Thus the complete outer contribution to (19) is exactly -2h.

Let
\(C=\max_{|z|\le r}(|L_\alpha(z)|+|L_{\bar\alpha}(z)|)\).
The remaining **entire** tail satisfies

\[
\left|\sum_{|\lambda_j|\le r}\lambda_j^2p_m(\lambda_j)^2\right|
\le\frac{C^2}{|\alpha|^2}
       \left(\frac r{|\alpha|}\right)^{2m}
       \sum_{|\lambda_j|\le r}|\lambda_j|^2\longrightarrow0.       \tag{21}
\]

For a finite m the full value is negative. Hence a finite H_d fails PSD.
This proves the converse, with every large value annihilated and the complete
small-value tail paid. Polynomial degree and coefficient size may be very
large; no uniformly inexpensive witness algorithm is asserted.

## 5. Apply the criterion to the literal theta operator

By (3), the nonzero eigenvalues of T are z^(-2), one per pair of Xi zeros
+/-z, with full algebraic multiplicity. The imported classical trace-class
determinant identities give

\[
s_n=\operatorname{Tr}T^{n+2}=\sum_j\lambda_j^{n+2}.                 \tag{22}
\]

These facts do not assume spectral normality. Jordan blocks contribute
according to algebraic multiplicity; their strictly nilpotent parts have trace zero.
For a complete source bound, write the parity blocks of K as A,B. Then

\[
\sum_j|\lambda_j|^2\le\|T\|_1^2
\le\|A\|_{HS}^2\|B\|_{HS}^2\le I_w^2/4.                         \tag{23}
\]

The Schatten product and eigenvalue inequalities in (23) are classical;
I_w is the complete integral (3), not an omitted physical tail. One can
therefore replace the last sum in (21) by I_w^2/4 for this operator.
No numerical value of I_w is certified here.

Define the cumulants by the exponential-series convention
\(\log M(u)=\sum_{n\ge1}\kappa_n u^n/n!\) near u=0, with M(0)=1.
The logarithm is used **only near zero**;
no global zero-free logarithm is presumed. Comparing the logarithms in (3)
gives the predecessor's exact formula

\[
\operatorname{Tr}T^m=
\frac{(-1)^{m+1}\kappa_{2m}}{2(2m-1)!},\qquad m\ge1.                \tag{24}
\]

Thus the matrices in question have the source-defined entries

\[
(H_d)_{ij}=
\frac{(-1)^{i+j+3}\kappa_{2i+2j+4}}
     {2(2i+2j+3)!}.                                                 \tag{25}
\]

There is no zero-table input in (25). Every fixed matrix is determined by
finitely many complete theta moments and polynomial cumulant identities.

**Exact conditional ending.** If (25) is PSD for every integer d>=0,
SC26-2 makes every nonzero T eigenvalue real. Negative ones would give a
pure imaginary Xi zero, excluded by (1). Therefore every eigenvalue is
positive, every Xi zero is real by (3), and RH follows. Conversely RH gives
all these matrices PSD by (19). Repeated zeta zeros are allowed throughout.

Equivalently the remaining statement is

\[
\boxed{\operatorname{Tr}[T^2p(T)^2]\ge0
       \quad\text{for EVERY real polynomial }p.}                   \tag{OPEN}
\]

This is a signed trace, **not**
\(\operatorname{Tr}([Tp(T)]^*[Tp(T)])\). The latter is nonnegative for every
operator and does not imply (OPEN). Similarly positivity of the ordinary
moment matrices of w does not imply positivity of the cumulant matrices (25).
For example the first two requirements include

\[
\kappa_4\le0,\qquad
10\kappa_4\kappa_8\ge21\kappa_6^2,
\]

as well as the other principal-minor conditions. The first displayed inequality
alone and finitely many higher checks do not close the argument.

## 6. The source-shape finishing attempt fails inside the same operator class

A proposed way to prove (OPEN) would use only positivity, evenness, strong
log-concavity, all exponential moments, and the compact centered-integration
construction. The following explicit density has **all** these properties
but fails (OPEN) already at p=1:

\[
\epsilon=1/1024,\qquad
w_\epsilon(x)=Z_\epsilon^{-1}(1+x^4/16)e^{-x^2-\epsilon x^4}.        \tag{26}
\]

This is a deliberately **changed** source, not theta, not zeta, and not an RH
counterexample. It only disproves this source-insensitive final inference.

**Strong log-concavity.** Set b=1/16 and y=sqrt(b)x^2>=0. Exactly

\[
[\log(1+bx^4)]''=\frac{4\sqrt b\,y(3-y^2)}{(1+y^2)^2}
\le6\sqrt b=3/2.
\]

Indeed \(y(3-y^2)/(1+y^2)^2\le3y/(1+y^2)\le3/2\).
Consequently \((-\log w_\epsilon)''\ge1/2+12\epsilon x^2\).
The density is positive, even, smooth, and has every exponential moment.
For x>=2 its potential derivative is at least 4 epsilon x^3 and is increasing.
Therefore \(Q_\epsilon(x)/w_\epsilon(x)\le1/(4\epsilon x^3)\).
Reflection pays the other tail, so the complete Hilbert--Schmidt integral
is finite. The same construction (2),(3), with this changed density, gives
an actual trace-class T_epsilon. This is not merely a finite matrix model.

**Exact complete-moment certificate.** Define

\[
g_j=\frac1{\sqrt\pi}\int_{\mathbb R}x^{2j}e^{-x^2}dx
=\frac{(2j)!}{4^j j!},\quad a_j=g_j+g_{j+2}/16,
\]

and
\(A_j=\pi^{-1/2}\int x^{2j}(1+x^4/16)e^{-x^2-\epsilon x^4}dx\).
The global inequalities 1-y<=e^(-y)<=1 for y>=0 yield

\[
a_j-\epsilon a_{j+2}\le A_j\le a_j.                               \tag{27}
\]

These are bounds for the **whole real-line integrals**, with no numerical
quadrature or truncated moment tail. Here

\[
(a_0,a_1,a_2,a_3,a_4)
=(67/64,79/128,297/256,1905/512,17115/1024).
\]

The normalized second and fourth moments are A_1/A_0 and A_2/A_0. As
\(a_0-\epsilon a_2>0\) and \(a_2-\epsilon a_4>0\), (27) proves

\[
\begin{split}
\kappa_4(w_\epsilon)
&\ge\frac{a_2-\epsilon a_4}{a_0}
-3\left(\frac{a_1}{a_0-\epsilon a_2}\right)^2\\
&=\frac{3930153304885749}{82494257251532800}>\frac3{64}.
\end{split}                                                        \tag{28}
\]

Using (24) for this actual changed-density operator therefore gives

\[
\operatorname{Tr}T_\epsilon^2=-\kappa_4(w_\epsilon)/12<-1/256.       \tag{29}
\]

This certifies nonreal spectrum somewhere, but does not compute a zero
location. The unperturbed epsilon=0 density already has
\(\kappa_4=294/4489\) and Fourier transform
\(e^{-z^2/4}(1-3z^2/67+z^4/268)\), whose quadratic discriminant in z^2 is
-58/4489. **That Gaussian-tailed unperturbed case is not used as a
Hilbert--Schmidt example**: its relevant integral diverges. The strictly
positive epsilon in (26) is essential to remain in the full compact-operator
class. Formula (28) avoids an unquantified perturbation argument.

## 7. Outcome, limitations, and the exact remaining task

The whole-problem attempt had two steps. A bounded positive metric on the
infinite core would have settled the spectrum, but Section 3 proves that
this is impossible for the actual operator. The weaker signed-trace route
avoids that obstruction and retains all multiplicities. Its complete
finite-witness/tail implication is proved in Sections 4--5. The attempt to
supply its sign using positive, even, strongly log-concave source structure
fails by the complete countermodel in Section 6.

What is **not** supplied is (OPEN) for the literal infinite theta series.
Neither an actual all-order Hankel lower bound, an arithmetic identity that
implies it, nor an alternative end-to-end RH proof has been obtained. This
criterion is not claimed easier than RH. Review is requested for the proved
components, not for an RH proof with its substantive premise delegated to
reviewers. No independent mathematical acceptance or external priority is
claimed. Existing source branches and canonical statuses are unchanged.

The finite checker reproduces the sharp two-vector algebra, synthetic
complete-tail witness formulas, formal moment/cumulant identities, Jordan
multiplicity controls, and the entire changed-density moment certificate.
It does not machine-prove the infinite arguments, evaluate the actual theta
spectrum, or certify any actual theta Hankel matrix. See README for source
reading depth and the exact executed commands.

## References and imported facts

1. GettysburgResearch/riemann, PR #834, exact source SHA/path/blob at the top.
   Whole proof read; centered operator, derivative domains, full theta tails,
   characteristic determinant and trace-class normalization are its inputs.
   No parent executable or historical certificate was rerun.
2. E. Hasanalizade, Q. Shen, P.-J. Wong, *Counting zeros of the Riemann zeta
   function*, arXiv:2107.06506, https://arxiv.org/abs/2107.06506 . Its displayed
   unconditional explicit counting bound implies (13). Only the classical
   asymptotic is used, not its numerical constants or a conditional error term.
3. A. Baricz, F. Stampach, *The Hurwitz-type theorem for the regular Coulomb
   wave function via Hankel determinants*, arXiv:1708.07729,
   https://arxiv.org/abs/1708.07729 . The abstract identifies the classical
   Grommer/Chebotarev inverse-zero-sum Hankel mechanism. It is attribution,
   not an imported proof: Section 4 supplies the entire needed argument.
4. NIST DLMF 25.4 and 25.10, https://dlmf.nist.gov/25.4 and
   https://dlmf.nist.gov/25.10 . Classical xi normalization, symmetry and
   zero-location conventions. No new numerical zero information is imported.
5. Standard compact-operator spectral theory, trace-class determinant
   identities, Schatten product inequalities, Riemann--Lebesgue, Gaussian
   moments, and finite Lagrange interpolation are classical. The parent
   identifies its determinant reference (Zumbrun, arXiv:1011.5695). Those
   general mechanisms are not claimed as new SC26 discoveries.

The two external arXiv abstracts were read. Their HTML-fulltext fetches failed;
no full-paper or PDF-page audit of them is claimed. No numerical constants
from those articles define the new bounded certificate.
