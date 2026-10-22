# Hyperbolic truncation gives the full Gram rate with growing punctures

22 October 2026. **Proposed source-dependent analytic strengthening.**
The `root` researcher proposed the fixed-puncture squarefree-divisor
split. The `short_power` researcher extended it to growing punctures
and derived the hyperbolic refinement proved here in full. Independent
review of this refinement must exclude the latter author's self-checks.

The imported input is the sixth-power-free sextic sieve of de Faveri,
[arXiv:2610.04045v1, Theorem 1.1](https://arxiv.org/html/2610.04045v1),
in the Eisenstein primary-ideal convention stated in Xu--Sang,
[arXiv:2610.17675v2, (2.3) and Remark 2.1](https://arxiv.org/html/2610.17675v2).
Ordinary finite-character lattice Poisson summation, elementary
ideal counting, and divisor bounds supply the remaining arguments.
No zero-free premise is used. No new zero-free boundary is claimed.

## 1. Exact matrices and theorem

Work over E=Q(sqrt(-3)), with good primary ideal representatives outside 6,
zero-extended sextic symbols chi_z(R)=(R/z)_6, and a fixed nonnegative,
nonzero w in C_c^infinity((0,infinity)). Let Q be a good ideal and let the
labels R be any subset of the good sixth-power-free ideals q_R<=K, each
appearing once. Every ideal variable below, including d,e,n in the
divisor expansions, is good unless another condition is explicitly given.
Put

\[
G_{R,S}=\frac1U\sum_{z\ {\rm good\ sf}}w(q_z/U)
 \mathbf1_{(z,Q)=1}\chi_z(R)\overline{\chi_z(S)},
\tag{1}
\]

\[
D_{R,R}=\frac{\operatorname{Res}_{s=1}\zeta_E(s)}{\zeta_E(2)}
 \int_0^\infty w(x)\,dx
 \prod_{\mathfrak p\mid6QR}(1+q_{\mathfrak p}^{-1})^{-1}.
\tag{2}
\]

Equivalently, G is the Gram matrix of the vectors
U^(-1/2)sqrt(w(q_z/U))u(z)overline{chi_z(R)}1_((z,Q)=1), for any common
unimodular phase u(z). That phase cancels in (1).

**Theorem.** Fix 0<delta<1/2 and A>=0. For every epsilon>0, uniformly for
U,K>=2, K<=U^(1/2-delta), and NQ<=U^A,

\[
\boxed{\quad
\|G-D\|_{\rm op}
    \ll_{w,\delta,A,\epsilon}(UKNQ)^\epsilon\frac K{\sqrt U}.
\quad}
\tag{3}
\]

Consequently the error is O(U^(-delta+epsilon)) after redistributing
the small powers, and G is invertible for sufficiently large U, with
||G||+||G^(-1)||<<U^epsilon. The diagonal, label class, and natural zeros
are exactly those in (1)--(2). No assertion is made for
arbitrary row deletion, duplicate labels, or all bounded U.

## 2. Exact expansion and a hyperbolic head

After the common phase cancels, insert mu_E(z)^2=sum_(d^2|z)mu_E(d).
The puncture forces (d,Q)=1; on z=d^2m, expand
1_((m,Q)=1)=sum_(e|radQ,e|m)mu_E(e), and set m=en. Let H(Y) be the
unnormalized Gram matrix on all good ideals n, of smooth norm scale Y,
and define the contraction

\[
                 C_{d,e}(R,R)=\chi_d(R)^2\chi_e(R).
\]

Then exactly,

\[
G=\frac1U\sum_{(d,6Q)=1}\mu_E(d)
 \sum_{e\mid\operatorname{rad}Q}\mu_E(e)
 C_{d,e}H\left(\frac{U}{q_d^2q_e}\right)C_{d,e}^{*}.
\tag{4}
\]

All sums are finite on the support of the test. No coprimality of d and n
or e and n is imposed. Every collision zero is retained in C_{d,e} and H.

For a parameter L>=1, keep the entire signed head

\[
                             q_d^2q_e\le L.
\tag{5}
\]

The tail is its complement. In particular the head is not a rectangular
cutoff in the two divisors.

For R!=S the full zero-extended coefficient of H(Y) is periodic with
modulus norm at most C K^2, and its complete mean vanishes. Indeed R/S
has a good-prime valuation in {-5,...,-1,1,...,5}; the corresponding
nontrivial tame character cannot be canceled by the fixed bad-place
sector. Primes with equal R,S valuations still appear as zeros in the
full period rad(RS). The growing Q no longer appears in that period:
its exact expansion is already outside H.

Lattice Poisson summation therefore bounds each off-diagonal entry of
H(Y) by O_(w,J)(Y(CK^2/Y)^J) for Y>=CK^2 and every fixed J. The diagonal
has the ordinary coprimality mean plus the same kind of error. In (5),
Y>=U/L. Summing the normalized errors, using
sum_d q_d^(-2)<infinity and sum_(e|Q)q_e^(-1)<<(NQ)^epsilon, then the
row-sum norm over O(K) labels, gives

\[
\|\mathrm{Head}-\mathrm{HeadMain}\|_{\rm op}
 \ll (NQ)^\epsilon K\left(\frac{CK^2L}{U}\right)^J.
\tag{6}
\]

Only the regime CK^2L/U<=1 is used.

## 3. Restoring the diagonal

The full diagonal main term before the divisor completion is the
coprimality density at 6R times

\[
\sum_{(d,6QR)=1}\frac{\mu_E(d)}{q_d^2}
 \sum_{\substack{e\mid\operatorname{rad}Q\\(e,R)=1}}
                           \frac{\mu_E(e)}{q_e}.
\tag{7}
\]

Its local Euler factors give exactly D in (2), including primes shared
by Q and R. Explicitly the d-sum is
zeta_E(2)^(-1)prod_(p|6QR)(1-q_p^(-2))^(-1), while the e-sum is
prod_(p|Q,p not dividing R)(1-q_p^(-1)). Multiplication by the
coprimality density at 6R leaves exactly
zeta_E(2)^(-1)prod_(p|6QR)(1+q_p^(-1))^(-1).

For every e, including q_e>L, ordinary ideal counting gives

\[
\sum_{q_d>\sqrt{L/q_e}}q_d^{-2}
                \ll(q_e/L)^{1/2}.
\tag{8}
\]

When the cutoff is below one, the left side is bounded and the right
side is at least one, so (8) remains valid. Thus the omitted diagonal
main term is bounded by

\[
\sum_{e\mid\operatorname{rad}Q}q_e^{-1}
         \sum_{q_d>\sqrt{L/q_e}}q_d^{-2}
 \ll L^{-1/2}\sum_{e\mid\operatorname{rad}Q}q_e^{-1/2}
 \ll (NQ)^\epsilon L^{-1/2}.
\tag{9}
\]

The original coprimality restrictions only decrease this absolute bound.

## 4. The full tail has the same four costs as the fixed-puncture proof

The sixth-power decomposition of unrestricted row ideals, retaining
natural zeros as diagonal contractions, gives from the imported sieve

\[
\|H(Y)\|_{\rm op}\ll(YK)^\epsilon
 \{Y+KY^{1/6}+Y^{5/6}K^{1/3}+Y^{1/3}K^{5/6}\}.
\tag{10}
\]

Indeed, write uniquely n=n_0 t^6 with n_0 sixth-power-free. Then
chi_n(R)=1_((t,R)=1)chi_(n_0)(R), a diagonal contraction of the labels.
Apply the imported sieve at scale Y/q_t^6: its Y, Y^(5/6)K^(1/3),
and Y^(1/3)K^(5/6) terms sum against the convergent powers
q_t^(-6), q_t^(-5), and q_t^(-2), respectively. Its K term is repeated
O(Y^(1/6)) times, giving KY^(1/6).

Bound the tail in (4) by the sum of these positive norms. At fixed e,
the actual nonempty range has q_d<<sqrt(U/q_e); use this upper bound
for the second and fourth terms. For the first and third retain the
tail cutoff q_d>sqrt(L/q_e). In addition to (8),

\[
\sum_{q_d>\sqrt{L/q_e}}q_d^{-5/3}
                         \ll(q_e/L)^{1/3}.
\tag{11}
\]

Again (11) is valid when q_e>L by enlarging a bounded sum. The four
contributions, including division by U, are respectively

\[
\begin{array}{c|c}
\text{term of (10)}&\text{bound at fixed }e\\\hline
Y & L^{-1/2}q_e^{-1/2}\\
KY^{1/6} & KU^{-1/2}q_e^{-1/2}\\
Y^{5/6}K^{1/3} & U^{-1/6}K^{1/3}L^{-1/3}q_e^{-1/2}\\
Y^{1/3}K^{5/6} & U^{-1/2}K^{5/6}q_e^{-1/2}.
\end{array}
\tag{12}
\]

All four have the same divisor weight q_e^(-1/2). The Euler-product
bound sum_(e|radQ)q_e^(-1/2)=prod_(p|Q)(1+q_p^(-1/2))<<(NQ)^epsilon
therefore proves, together with (6) and (9),

\[
\begin{split}
\|G-D\|_{\rm op}\ll{}&
 (NQ)^\epsilon K\left(\frac{CK^2L}{U}\right)^J\\
 &+(UKNQ)^\epsilon\left\{
 L^{-1/2}+KU^{-1/2}
 +U^{-1/6}K^{1/3}L^{-1/3}+U^{-1/2}K^{5/6}\right\}.
\end{split}
\tag{13}
\]

The sieve loss in (10) is uniform on all nonempty actual scales; bounded
ones are covered by a fixed constant. No new arbitrary-coefficient
claim is made by the signed expansion.

## 5. Optimized rate and inverse

Choose a fixed eta with 0<eta<2delta, sufficiently small for the final
epsilon, and put

\[
                      L=(U/K^2)U^{-\eta}.
\tag{14}
\]

Then L>=U^(2delta-eta), and CK^2L/U=CU^(-eta). Choose the fixed Poisson
decay order J after eta so that the first line of (13) is negligible,
also after its polynomial Q allowance.

Writing r=K/sqrt(U), the four tail quantities become

\[
 rU^{\eta/2},\qquad r,\qquad rU^{\eta/3},\qquad rK^{-1/6}.
\tag{15}
\]

Each is at most rU^(eta/2) because K>=1. Decreasing all intermediate
losses proves (3). The elementary lower bound
min_R D_(R,R)>>_(w,epsilon)(NQK)^(-epsilon), together with NQ<=U^A,
then makes ||G-D|| smaller than half the least diagonal for sufficiently
large U. The min-max principle proves the stated inverse bound.

This refinement concerns Gram conditioning only. The root's
fixed-puncture optimized split is consistent with (14) when e=1.
An improved estimate for a projected Kubota operator still retains its
separate analytic dependencies, and no bound for its complementary
operator follows. The high-conductor inverse estimate needed by the
zero-free detector remains open.
