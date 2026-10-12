# A viable moving Mellin contour and its exact arithmetic price

**Status:** proposed uniform bounds for the finite collision factor and
a sufficient, still-open native short-polynomial moment criterion.
The contour is allowed to approach \(1/2\) from below as the physical
scale grows. No new full moment or zero-free boundary is asserted.

**Scope:** the exact finite source factors in PR #911, all independent
Mellin frequencies, all physical element rows and their literal zeros,
fixed finite-order \(\nu,S\), and all source incidence masks. The
conditional arithmetic input below concerns the actual sharp norm
truncations; it is not inferred from a smooth moment without an endpoint
or maximal adapter.

**Relation to earlier work:** PR #916 already proves the finite
collision reconstructions and their sharp critical logarithmic
coefficient cost. The companion HISTORICAL_CONNECTIONS.md identifies
and applies that result. This note instead quantifies how far the
*uncompressed finite Euler factor* may move below \(1/2\) while
retaining a uniform subpower bound, and prices a sufficient arithmetic
input on that moving contour. The fixed-below-half trace refutation is
in SIGNED_TRACE_OBSTRUCTION.md.

## 1. The factor and the contour parameters

Fix \(r=2k\), \(k\ge1\), and \(\sigma_0\in(1/3,1/2)\).
For sufficiently large \(Y\), choose
\[
0\le\delta_Y\le\tfrac12-\sigma_0,\qquad
\sigma_Y=\tfrac12-\delta_Y,\qquad
L=\log Y,\qquad a_Y=2\delta_Y L.
\tag{1.1}
\]
The sequence \(\delta_Y\) need not be monotone. Let
\(\eta_u(n)=\nu(n)\chi_n(u)\), with the literal zeros retained,
and let \(\theta_i=\eta_u\) on the \(k\) left slots and
\(\theta_i=\bar\eta_u\) on the \(k\) right slots.

For any squarefree source incidence mask \(Q\), define
\[
\mathcal Q_{r,Y,Q,u}(\mathbf s)=
\prod_{\substack{p\notin S,\ p\nmid Q\\Np\le Y}}
\frac{1-\sum_i\theta_i(p)(Np)^{-s_i}}
     {\prod_i(1-\theta_i(p)(Np)^{-s_i})}.
\tag{1.2}
\]
At \(p\mid u\), every local variable is zero and the factor is one.
No condition on the norm of \(Q\) is needed for the upper bound in
this section; the physical source imposes its own polynomial bound
when the factor is used in Section 4.

### Theorem 1.1. Uniform factor bound

There is a constant depending only on the fixed data and \(\sigma_0\)
such that, for every nonzero row, every mask \(Q\), and every vector
of independent real frequencies,
\[
\boxed{
|\mathcal Q_{r,Y,Q,u}(\sigma_Y+i\mathbf t)|
\le
\exp\!\left[
C\left(\log\log Y+\frac{e^{a_Y}}{1+a_Y}\right)\right].
}
\tag{1.3}
\]
Consequently
\[
\frac{e^{a_Y}}{1+a_Y}=o(\log Y)
\tag{1.4}
\]
implies the all-row, all-mask, all-frequency bound
\[
|\mathcal Q_{r,Y,Q,u}(\sigma_Y+i\mathbf t)|=Y^{o(1)}.
\tag{1.5}
\]
The little-oh is uniform in those variables. Replacing \(o(\log Y)\)
by \(O(\log Y)\) gives a fixed polynomial bound.

**Proof.** The exact pair factorization in PR #911, P3--P6, or its
local Taylor expansion, gives
\[
\frac{1-\sum_i z_i}{\prod_i(1-z_i)}
=\prod_{i<j}(1-z_i z_j)\,E_p(\mathbf z).
\tag{1.6}
\]
The nonconstant terms of \(E_p\) have degree at least three, and
its finite products are uniformly bounded on
\(\Re s_i\ge\sigma_0>1/3\). This is an upper bound: zeros of the
local numerator cause no difficulty. The finitely many small
prime denominators are uniformly separated from zero, and the
large-prime majorant is \(1+O((Np)^{-3\sigma_0})\).
Thus, uniformly in all phases and deletions,
\[
|\mathcal Q_{r,Y,Q,u}|
\le C\exp\!\left(C_r\sum_{Np\le Y}
                  (Np)^{-1+a_Y/L}\right).
\tag{1.7}
\]

The classical prime-ideal theorem gives the fixed-field upper
bound \(\pi_K(t)\ll_K t/\log t\) for \(t\ge2\). Partial summation,
uniformly for \(0\le a\le(1-2\sigma_0)L\), yields
\[
\sum_{Np\le Y}(Np)^{-1+a/L}
\ll 1+\frac{e^a}{L}
       +
       \int_{\log2}^{L}\frac{e^{av/L}}v\,dv.
\tag{1.8}
\]
After subtracting the integral with numerator one, the remaining
integral is at most
\[
\int_0^1\frac{e^{ax}-1}{x}\,dx
=\sum_{m\ge1}\frac{a^m}{m\,m!}.
\tag{1.9}
\]
It is \(O(1)\) for \(0\le a\le1\); for \(a\ge1\), the elementary
inequality \(1/m\le2/(m+1)\) bounds it by \(2e^a/a\).
The boundary term \(e^a/L\) is absorbed by
\(C e^a/(1+a)\) in the permitted range of \(a\).
Therefore (1.8) is
\[
\ll \log L+\frac{e^a}{1+a}.
\tag{1.10}
\]
Substitution into (1.7) proves (1.3), and (1.4) proves (1.5).
\(\square\)

## 2. Explicit depths and the factor's polynomial threshold

One particularly simple choice is
\[
\boxed{
\sigma_Y=\frac12-\frac{\log\log Y}{2\log Y}.
}
\tag{2.1}
\]
Here \(a_Y=\log\log Y\), and Theorem 1.1 gives
\[
|\mathcal Q_{r,Y,Q,u}|
\le
\exp\!\left(O\!\left(\frac{\log Y}{\log\log Y}\right)\right)
=Y^{O(1/\log\log Y)}.
\tag{2.2}
\]
Every independent frequency is covered; there is no shrinking-tube
restriction in this upper bound.

The scale where the displayed Euler majorant becomes polynomial is
\[
a_Y=\log\log Y+\log\log\log Y+O(1).
\tag{2.3}
\]
For example, subtracting a quantity tending to infinity, with the
result still nonnegative and differing from \(\log\log Y\) by
\(o(\log\log Y)\), gives (1.4). Formula (1.4), rather than this
example, is the precise sufficient condition.

This threshold has a converse for the **factor alone**, not for a
native trace or moment. Choose the fixed cross-incidence mask \(P\)
from Section 1 of SIGNED_TRACE_OBSTRUCTION.md, with the present
\(\sigma_0,r\), and retain the unit row \(u=1\).
For \(x\in[1,5/4]\), set every slot to
\[
s=\sigma_Y+\frac{ix}{\log Y}.
\tag{2.4}
\]
At a prime \(p\notin SP\), the pair coefficient in the local
logarithm is real:
\[
\gamma_p=k^2+k(k-1)\Re(\nu(p)^2),
\qquad k\le\gamma_p\le k(2k-1).
\tag{2.5}
\]
The local expansion, uniform because \(\sigma_Y\ge\sigma_0\), gives
\[
\log|\mathcal Q_{r,Y,P,1}(s,\ldots,s)|
=-\sum_{\substack{p\notin SP\\Np\le Y}}
\gamma_p(Np)^{-1+a_Y/L}
 \cos\!\left(2x\frac{\log Np}{L}\right)+O(1).
\tag{2.6}
\]

Suppose along a sequence
\[
\frac{e^{a_Y}}{1+a_Y}\ \ge c_0 L
\tag{2.7}
\]
for a fixed \(c_0>0\). Then \(a_Y\to\infty\).
On \(Np\ge Y^{9/10}\), the cosine in (2.6) is uniformly negative
for \(x\in[1,5/4]\), since its argument lies in \([9/5,5/2]\).
The prime-ideal theorem and partial summation on
\([Y^{1-1/a_Y},Y]\subset[Y^{9/10},Y]\) give
\[
\sum_{Y^{9/10}<Np\le Y}(Np)^{-1+a_Y/L}
\gg \frac{e^{a_Y}}{a_Y}.
\tag{2.8}
\]
Here is a uniform error check. Put \(A=Y^{1-1/a_Y}\),
\(\beta=1-a_Y/L\), and write
\(\pi_K(t)=\operatorname{Li}(t)+R(t)\). The prime-ideal theorem
gives \(|R(t)|\le\varepsilon_Y t/\log t\) on
\([Y^{9/10},Y]\), where \(\varepsilon_Y\to0\).
Partial summation bounds the absolute error in
\(\int_A^Y t^{-\beta}\,d\pi_K(t)\) by
\[
\varepsilon_Y\left(
\frac{e^{a_Y}}L+
\frac{e^{a_Y-1}}{L-L/a_Y}+
\beta\int_{L-L/a_Y}^L\frac{e^{a_Yv/L}}v\,dv
\right)
\ll\varepsilon_Y\frac{e^{a_Y}}{a_Y}.
\tag{2.8a}
\]
The main \(\operatorname{Li}\) integral, after \(v=\log t\),
is the same integral without \(\beta\); it is comparable to
\(e^{a_Y}/a_Y\). This proves (2.8) uniformly, including when
\(a_Y\) is a fixed fraction of \(L\). It uses no
conductor-varying prime theorem.

The primes below \(Y^{9/10}\) cost at most
\[
C\left(\log L+
          \frac{e^{(9/10)a_Y}}{1+a_Y}\right)
=o\!\left(\frac{e^{a_Y}}{1+a_Y}\right)
\tag{2.9}
\]
under (2.7), by the same upper estimate as (1.8)--(1.10).
Equations (2.5)--(2.9) therefore prove
\[
\boxed{
\log|\mathcal Q_{r,Y,P,1}(s,\ldots,s)|
\ge c\frac{e^{a_Y}}{1+a_Y}
\quad(x\in[1,5/4])
}
\tag{2.10}
\]
on that sequence.

It follows that:

- (1.4) is also necessary for a uniform \(Y^{o(1)}\) bound on the
  factor over all native rows, source masks, and frequencies.
- \(e^{a_Y}/(1+a_Y)=O(\log Y)\) is also necessary for such a
  uniform bound by some fixed power of \(Y\).

For the first assertion, a failure of (1.4) supplies a subsequence
of type (2.7), and (2.10) supplies a fixed positive power. For the
second, an unbounded ratio to \(\log Y\) supplies unbounded powers.
The sufficiency of both conditions was proved in Theorem 1.1.

These are sharp order thresholds for this uncompressed collision
factor. Multiplication by the literal short polynomials and signed
row summation can change its size. No necessity statement for
the filtered physical moment is deduced here.

## 3. A native arithmetic input that remains meaningful

Fix \(h>0\), the source's column-support constant \(b>0\), and
\(H=(Y/b)^h=D^h\). Fix a nonnegative Schwartz spatial majorant
\(\Phi\) on \(K\otimes_{\mathbb Q}\mathbb R\cong\mathbb R^2\),
with the source's prescribed radial and Fourier-support
properties when those are imposed. For an original row cutoff
\(0<Nu\le H\), require \(\Phi\ge1\) on the unit norm ball.
All constants below may depend on these fixed data.

For an eligible incidence allocation \(\mathbf q=(q_I)\), use
exactly the source labels
\[
c_i=\prod_{I\ni i}q_I,\qquad Q=\prod_Iq_I,\qquad Nc_i\le Y.
\tag{3.1}
\]
The \(q_I\) are pairwise coprime and squarefree, with \(|I|\ge2\).
The source's exterior multiplier \(\omega_{\mathbf q}(u)\)
retains every principal zero and has modulus at most one.

The short factors are the actual common-cutoff polynomials
\[
T_{i,Y,Q,u}(s)=
\sum_{\substack{Nn\le Y\\(n,SQ)=1}}
       \mu_K(n)\theta_{i,u}(n)(Nn)^{-s}.
\tag{3.2}
\]
Their cutoff is \(Y\), including when a later physical factor
scale \(D/Nc_i\) is smaller.

Assume (1.4). A sufficient arithmetic target, with a fixed
additional loss \(e\ge0\), is the following: for every
\(\epsilon>0\), fixed finite \(B,C\) give
\[
\boxed{
\sum_{u\ne0}\Phi(u/\sqrt H)
   \prod_{i=1}^{2k}
       |T_{i,Y,Q,u}(\sigma_Y+it_i)|
\le C H Y^{e+\epsilon}\prod_i(1+|t_i|)^B
}
\tag{3.3: open premise}
\]
at every sufficiently large \(Y\), every eligible \(Q\), and
all independent frequencies. This is a positive arithmetic
premise on native coefficients. It is not asserted here.

For example, Hölder makes (3.3) with \(e=0\) follow from the
stronger one-polynomial assertion
\[
\sum_{u\ne0}\Phi(u/\sqrt H)
 |T_{Y,Q,u}(\sigma_Y+it)|^{2k}
\ll_\epsilon H Y^\epsilon(1+|t|)^{B_0}
\tag{3.4: stronger open premise}
\]
uniformly in the same exclusions and scales, for the left
character and its conjugate. No input of that order is supplied.

Neither (3.3) nor (3.4) follows just by replacing a smooth
column test in an inherited theorem by a sharp cutoff. A proof
using smooth moments would have to supply its uniform interval,
maximal, or endpoint transfer, including the smaller scales and
moving exclusions. This note makes no converse or equivalence
claim between (3.3) and the physical moment.

## 4. Exact conditional incidence price

### Proposition 4.1. Sufficient moving-contour implication

If the native premise (3.3) holds, then for every permitted fixed
collection of compactly supported smooth original column tests,
\[
\boxed{
M_{2k}^{\Phi}(D,D^h)\ll_\epsilon D^{h+k+e+\epsilon}.
}
\tag{4.1: conditional}
\]
This is the full source smooth moment at that fixed order, with
every row and every incidence included. Its premise is open.

**Proof.** At each allocation, the exact norm-filtered identity
SC4 in the pinned source permits every positive real contour,
so it permits \(\sigma_Y\). Theorem 1.1, (1.4), the contraction
\(|\omega_{\mathbf q}|\le1\), and (3.3) bound its row trace by
\[
H Y^{e+\epsilon}\prod_i(1+|t_i|)^B,
\tag{4.2}
\]
after reallocating smaller preliminary losses. The Mellin
transforms of the original fixed tests decrease rapidly,
uniformly for \(\sigma_Y\in[\sigma_0,1/2]\). Integrating their
frequency weights is therefore uniform in \(Y\).

The contribution of this exact allocation is consequently at
most
\[
C H Y^{e+\epsilon}D^{2k\sigma_Y}
       \prod_i(Nc_i)^{-\sigma_Y}.
\tag{4.3}
\]
The incidence identity gives
\[
\prod_i(Nc_i)^{-\sigma_Y}
=\prod_I(Nq_I)^{-|I|\sigma_Y}
\le(NQ)^{-2\sigma_Y},\qquad NQ\le Y^k.
\tag{4.4}
\]
For each fixed \(\eta>0\), the number of allocations over \(Q\)
is \(O_\eta((NQ)^\eta)\), by the fixed-order divisor bound.
Uniformly in \(\sigma_Y\le1/2\), ideal counting gives
\[
\begin{aligned}
\sum_{\text{eligible }\mathbf q}\prod_i(Nc_i)^{-\sigma_Y}
&\ll_\eta
\sum_{NQ\le Y^k}(NQ)^{-2\sigma_Y+\eta}\\
&\ll_\eta Y^{k(1-2\sigma_Y+\eta)}.
\end{aligned}
\tag{4.5}
\]
The implied constant is uniform as \(\sigma_Y\uparrow1/2\):
the positive exponent \(1-2\sigma_Y+\eta\) is at least \(\eta\).
No hidden constant \(1/(1-2\sigma_Y)\) is used.

Finally, since \(Y=bD\),
\[
D^{2k\sigma_Y}Y^{k(1-2\sigma_Y)}
=D^k b^{k(1-2\sigma_Y)}\asymp_{b,k,\sigma_0}D^k.
\tag{4.6}
\]
Choose \(\eta\) and all preliminary losses sufficiently small
in terms of the desired \(\epsilon\). Summing (4.3) with
(4.5)--(4.6) proves (4.1). The fixed coefficient phases outside
the row trace have modulus at most one and all complete
incidence allocations have been summed. \(\square\)

The contour movement changes neither the critical arithmetic
budget nor the final conditional power. It provides a region
where the Euler representation itself has an appropriate
uniform size, so the remaining difficulty is explicitly the
native short-polynomial arithmetic in (3.3).

## 5. Sources and validation limits

The exact finite factor and SC4 are read at PR #911 commit

    2f8b6a3898a722d0602a91dea73bac344a3bb7dd

from PRIME_SLOT_CANCELLATION.md and
SHORT_POLYNOMIAL_COLLISION_TRANSPORT.md under

    research/exploratory/2026-10-10-two-hour-continuation/literature/

Their respective SHA-256 values are

    d37ad696b46c7dda15a7faf314c46cda2d7d67e25ac8d3288c7f138aac373c13
    c538719277b1e7de70a7e3f872fb2720668bd43ca57c9cffff6ff29b6766d5ac

The pre-existing compression and critical logarithmic cost are
PR #916, commit

    dd70e580a5ffdbe5b140784ba6cebd173cb84792

in standalone/2026-10-10-all-order-collision-removal/PROOF.md,
Sections 2--5. Its all-degree cycle completion and later finite
rectangle continuations are credited in HISTORICAL_CONNECTIONS.md;
they are not newly claimed here.

The prime-counting input is the same classical unconditional
prime-ideal theorem as in SIGNED_TRACE_OBSTRUCTION.md, with
primary reference Sami Omar, *A note on the Prime Ideal Theorem*,
Corollary 1:

https://www.wseas.us/e-library/conferences/corfu2004/papers/488-336.pdf

This note supplies analytic proofs of the factor bounds and the
conditional implication. It does not use numerical fit,
unbounded-order enumeration, or any assumed zero-free improvement.
It proves no instance of the new arithmetic premise (3.3).
