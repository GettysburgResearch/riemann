# The selected physical minor is singular at infinite horizon

## 1. Exact source and scope

This is a theorem about the particular twenty-row minor used in the frozen
physical-tail campaign, not a failure of infinite-source faithfulness.

The source is \(\ell_x(z)=(1-x)\sqrt{1-z^2}+x\sqrt{1-z}\) at the three
fixed primes \(2,3,5\). Write
\[
 b_n=[z^n]\sqrt{1-z},\qquad
 a_n=\begin{cases}b_{n/2}&2\mid n,\\0&2\nmid n,\end{cases}
 \qquad d_n=b_n-a_n.
\]
Thus the local coefficient is \(a_n+d_nx\). The letter \(d_n\) here is a
scalar coefficient, whereas \(dx_i\) below denotes a differential.

The literal local and curvature formulas are in
`native_physical_tail_scout.py`, frozen at
`3ba479241acf9db1554af067d5e2bea85533dde5`,
blob `24ef243220c8159f78505717d639d88287fbf439`.
The actual selection and unchanged extended implementation are frozen in
`63e1742ec319c532baa36f6568809f6a6b32e6e2`;
the extension producer blob is
`bb69109f81bca6e814a87c82be86ac7b92934d27`.
The twenty reduced ratios are \(1/b\), with
\[
 b\in(2,3,4,5,6,8,9,10,12,15,16,18,20,25,30,40,45,50,60,75).
\]
The selected zero-based curvature coordinates, in the frozen order, are
\[
 (0,3,5,12,2,6,8,1,13,4,15,25,7,16,14,18,20,22,24,26).
\]
We first prove a dependence of complete thirty-six-coordinate rows. It
therefore persists under this or any other choice of twenty columns.

This note does not change the old \(900\), \(2^{20}\), or \(2^{48}\)
`UNKNOWN_TAIL_NOT_CONTRACTIVE` results. It does not claim that the selected
minor is singular at any finite horizon. The exact limiting rank is not
computed: the proved upper bound is fifteen.

## 2. Infinite alias factorization

Put \(p_1=2,p_2=3,p_3=5\) and \(q_i=1/p_i\). For a local shift
\(\beta\ge0\), define the absolutely convergent quadratic and scalar
\[
 \begin{split}
 N_{i,\beta}(x)
   &=\sum_{k\ge0}q_i^k(a_k+d_kx)(a_{k+\beta}+d_{k+\beta}x),\\
 D_{i,\beta}
   &=\sum_{k\ge0}q_i^k
       (d_ka_{k+\beta}-a_kd_{k+\beta}).
 \end{split}                                                   \tag{2.1}
\]
The four frozen local entries are precisely the coefficients of
\(1,x,x^2\) in the summand of \(N_{i,\beta}\), followed by the summand of
\(D_{i,\beta}\). In particular,
\[
 D_{i,0}=0                                                     \tag{2.2}
\]
term by term, not merely after summation.

For \(b=\prod_i p_i^{\beta_i}\), the ratio \(1/b\) has aliases
\((n,m)=(g,bg)\), where \(g=\prod_i p_i^{k_i}\), and the actual reduced
physical weight is \(1/g=\prod_iq_i^{k_i}\). The further factor
\(1/\sqrt b\) in the physical frequency coefficient is a nonzero row
scalar and has no effect on any rank conclusion.

Let \(\Omega_b\) be the complete infinite curvature row, viewed as a
polynomial two-form. The frozen coefficient formula, with its original
factor two, gives
\[
 \Omega_b
 =\sum_{i<j}
  \left(D_{i,\beta_i}N'_{j,\beta_j}(x_j)
       -N'_{i,\beta_i}(x_i)D_{j,\beta_j}\right)
  \prod_{h\ne i,j}N_{h,\beta_h}(x_h)\,dx_i\wedge dx_j.           \tag{2.3}
\]
Here a prime denotes differentiation in that displayed coordinate.

For completeness, the identity behind the factor two is
\[
 (bc-ad)(eh+fg)-(ad+bc)(fg-eh)
   =2(bceh-adfg).
\]
It is the constant-coordinate instance of the frozen
\(D_iN'_j-N'_iD_j\) identity; the linear and quadratic coefficients give
the other frozen entries.

There is no conditional interchange hidden in (2.3). For every \(n\),
\(|a_n|\le1\) and \(|d_n|\le2\), so every local coefficient and determinant
summand has a uniform bound. Each coefficient of the three-prime
curvature is bounded by a constant times
\(\prod_iq_i^{k_i}\), whose complete sum is finite. Tonelli applied to
absolute values and then distributivity prove (2.3). The finite cutoff
\(nm=g^2b\le H\) exhausts these aliases, so its matrix \(A_H\) converges
entrywise, hence in every finite-dimensional matrix norm, to the matrix
\(A_\infty\) formed from (2.3).

## 3. Pure-prime rows collapse

Set \(N_i=N_{i,0}\). If \(b=p_i^\beta\) with \(\beta>0\), all shifts away
from \(i\) vanish. Equation (2.2) removes every term not involving \(i\)
and all terms containing the other local determinants. Thus
\[
 \boxed{\quad
 \Omega_{p_i^\beta}=D_{i,\beta}\,\Xi_i,\qquad
 \Xi_i=dx_i\wedge d\!\left(\prod_{j\ne i}N_j(x_j)\right).
 \quad}                                                       \tag{3.1}
\]
The form \(\Xi_i\) is independent of \(\beta\). In particular, the
shifted quadratic \(N_{i,\beta}\) disappears completely: in every
surviving term the \(i\)-th local factor is the scalar determinant.

The selected rows contain the following three disjoint pure-prime
families:
\[
 \begin{array}{c|c|c}
 p_i&b&\text{dimension of their infinite row span}\\ \hline
 2&2,4,8,16&\le1\\
 3&3,9&\le1\\
 5&5,25&\le1.
 \end{array}
\]
These eight rows span at most three dimensions. The other twelve rows
add at most twelve. Therefore
\[
 \boxed{\operatorname{rank}A_\infty\le15,\qquad
        \det A_\infty=0.}                                    \tag{3.2}
\]
No nonvanishing assertion about \(D_{i,\beta}\), and no assertion of
independence of the three \(\Xi_i\), is needed for this upper bound.

At finite \(H\), the alias restriction \(g^2b\le H\) couples the three
local summation indices. The complete product factorization used in
(3.1) is unavailable. Thus exact nonsingularity of the finite minors
does not conflict with (3.2). Along any unbounded sequence of horizons
for which \(A_H\) is invertible, its inverse norm tends to infinity:
otherwise a bounded subsequence of inverses would have a limit \(B\),
and passing to the limit in \(A_HA_H^{-1}=I\) would give
\(A_\infty B=I\).

### 3.1 A uniform collapse rate from the actual source

Let \(v_n\in\mathbb R^8\) be the monomial coefficient vector of the
multilinear polynomial \(\Lambda_n(x_1,x_2,x_3)\). It is zero unless
\(n\) is supported on \(2,3,5\). The local coefficient signs give
\[
 \sum_{n\ge0}(|a_n|+|d_n|)=2+\sqrt2.
\]
Indeed, the constant coefficient contributes \(1\); the positive even
indices contribute \(1+\sqrt2/2\), and the odd indices contribute
\(\sqrt2/2\). These identities follow by adding and subtracting
\(\sqrt{1-z}\) at \(z=1,-1\); the endpoint series converge absolutely.
Tensoring the three local coefficient vectors therefore gives
\[
 S:=\sum_{n\ge1}\|v_n\|_1=(2+\sqrt2)^3.                        \tag{3.3}
\]
The full thirty-six-coordinate source row \(C(n,m)\) is the coefficient
vector of \(2\,d\Lambda_n\wedge d\Lambda_m\). The coefficient norm is
submultiplicative under wedge products, and multilinearity gives
\(\|d\Lambda_n\|_1\le3\|v_n\|_1\). Consequently
\[
 \|C(n,m)\|_1\le18\|v_n\|_1\|v_m\|_1,\qquad
 \sum_{g\ge1}\|C(g,bg)\|_1\le18S^2=:M.                        \tag{3.4}
\]
These are bounds for the actual source, not for its finite local
majorant used in Section 5.

For an omitted alias \(g^2b>H\), one has \(g^{-1}<\sqrt{b/H}\).
Thus every selected row entry has tail at most
\(M\sqrt{b/H}\). There are twenty rows and columns, and \(b\le75\), so
\[
 \|A_H-A_\infty\|_2
 \le\|A_H-A_\infty\|_{\mathrm F}
 \le L H^{-1/2},\qquad L=20\sqrt{75}\,M.                     \tag{3.5}
\]
Here the Frobenius norm and singular values use precisely the frozen
twenty row and column coordinates, without a change of basis.

The last five singular values of \(A_\infty\) vanish by (3.2).
The singular-value perturbation bound therefore gives
\[
 \sigma_j(A_H)\le LH^{-1/2}\quad(16\le j\le20).
\]
Also \(\|A_H\|_2\le20M\) for \(H\ge1\), directly from (3.4) and
\(1/g\le1\). Hence
\[
 |\det A_H|\le(20M)^{15}L^5H^{-5/2},\qquad
 \|A_H^{-1}\|_2\ge L^{-1}H^{1/2}
 \quad\hbox{whenever }A_H\hbox{ is invertible}.                \tag{3.6}
\]
This proves a quantitative finite-to-infinite degeneration. It does
not assert a matching rate, exact limiting rank, or finite-horizon
singularity.

## 4. Why no strict uniform contraction can work for this minor

Fix an invertible finite anchor \(A=A_{H_0}\). Suppose a nonnegative
matrix \(T\) bounds every subsequent difference entrywise:
\[
 |A_H-A|\le T\qquad(H\ge H_0).
\]
Taking the limit also bounds \(|A_\infty-A|\). If
\[
 \bigl\|\,|A^{-1}|T\,\bigr\|_\infty<1,                          \tag{4.1}
\]
then \(\|A^{-1}(A_\infty-A)\|_\infty<1\). The Neumann lemma would make
\(A_\infty=A[I+A^{-1}(A_\infty-A)]\) invertible, contradicting (3.2).
Consequently (4.1) is impossible for an honest all-future bound for this
fixed selection, at every finite anchor.

The obstruction applies equally to another induced matrix norm, a
positive diagonal weighting, or a rational approximate inverse whose
rigorous residual-plus-tail bound is strictly below one. Such a
certificate would still imply invertibility of the same singular
limit. This does not prohibit proofs of nonsingularity at every
*finite* horizon by methods that do not place the limiting matrix
inside a uniform open neighborhood of invertible matrices.

The infinite full-source faithfulness theorem at
`822646ffea23d906c385f0273a8c45693e982c4d` concerns the entire
observation map, not this selected set of twenty frequencies.
An injective infinite observation need not remain injective after a
particular finite set of its coordinates is retained. No contradiction
or correction to that theorem follows.

## 5. The recorded \(2^{48}\) comparison: cutoff floor is negligible

This section records coarse exact inequalities for the existing
`native_physical_tail_extension.extension.json`, proof-object digest
`aa3f9ad57373bb321996f9e5615652ec5322ef8e0147af5fd18c51cf93f0f2a1`.
The artifact is frozen at `987ccb82d0bf097942389027c6e785925847e6a7`.
The root reported successful write/check/optimized-check execution and all
eighteen tests in each mode. The new coarse diagnostic inequalities below
remain a separate exact-rational check target. The mathematical argument in
Sections 2–4 does not depend on this numerical record.

Let \(U\) be the stored product-majorant upper matrix, and let
\(U_{\rm box}\) replace every stored local upper by its stored partial
sum through degree \(64\). Let \(P_H\) be the stored positive prefix.
Every alias at \(H=2^{48}\) has \(g\le2^{24}\), hence each local exponent
at most \(24<64\). Therefore the exact decomposition
\[
 T_H=U-P_H=(U-U_{\rm box})+(U_{\rm box}-P_H)                    \tag{5.1}
\]
has two nonnegative summands. The first is the fixed local-cutoff
remainder; the second is the positive tail still outside the
hyperbolic finite prefix but inside the local box.

The stored rational entries have the following deliberately coarse
bounds:
\[
 |(A_H^{-1})_{ij}|<10^{14},\qquad
 0\le U_{\rm local}<2,\qquad
 0\le R_{\rm local}<3\cdot10^{-25}.                            \tag{5.2}
\]
Every coordinate has at most two product terms and the sum of their
absolute scalar coefficients is at most two. The telescoping product
identity consequently gives
\[
 0\le(U-U_{\rm box})_{ij}
 <2\cdot3\cdot2^2\cdot3\cdot10^{-25}
 <10^{-23}.
\]
For twenty rows and columns this implies
\[
 \bigl\|\,|A_H^{-1}|(U-U_{\rm box})\,\bigr\|_\infty
 <20^2\,10^{14}\,10^{-23}=4\cdot10^{-7}.                       \tag{5.3}
\]
In contrast, the recorded total comparison norm is approximately
\(1.397\cdot10^3\). The failure is not caused by the degree-64 local
remainder. The positive unexhausted alias tail, amplified by a minor
approaching singularity, dominates the recorded comparison.

There is also an exact test against reweighting this *recorded*
nonnegative comparison matrix \(C=|A_H^{-1}|T_H\): all twenty stored row
sums exceed \(3\). For any positive vector \(w\), choose \(i\) with
\(w_i=\min_jw_j\). Then
\[
 \frac{(Cw)_i}{w_i}\ge\sum_jC_{ij}>3.
\]
Thus every positive diagonal weighting of this same matrix has
induced infinity norm greater than three. This is an elementary
statement about the stored bound, independent of Section 4's stronger
limiting obstruction.

The coarse inequalities (5.2) and the twenty row-sum comparisons are
a small exact-rational verification target for the root. They were
identified by read-only inspection here; no new scientific execution,
inverse computation, campaign mutation, or matrix certificate was
performed by this note's author.

## 6. What remains useful

The event-by-event campaign can still certify finite intervals for
this minor: limiting singularity does not invalidate an exact modular
rank witness at any finite event. It cannot combine with a strict
all-future Neumann bound for this selection, because Section 4 rules
out that latter condition.

A future effective infinite-horizon certificate must change the
selected observation coordinates or use a method that permits a
singular limiting minor. Replacing repeated pure-prime rows by mixed
prime frequencies is a motivated design change, not an already
certified replacement minor. This note makes no numerical assertion
about such a new selection, no claim that the limiting rank is
exactly fifteen, and no new statement about the original energy
minimum or the full gamma function.
