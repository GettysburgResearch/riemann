# The duplicate-67 source is a boundedly invertible scale filter in the critical window

Status: **exact prefix-scale identities, exact weighted maximal and
multiplicative-block isomorphisms, and a sharp duplicate-factor no-go;
the remaining Möbius block estimate, RH, and GRH are open**

Bounded exact replay:
[ffps_duplicate67_critical_scale_filter_firewall.py](ffps_duplicate67_critical_scale_filter_firewall.py).
Canonical summary:
[ffps_duplicate67_critical_scale_filter_firewall.json](ffps_duplicate67_critical_scale_filter_firewall.json).

Frozen predecessor:
\(070be728e8d434bfb72645e23f9894acf920d3c0\).
The replay pins the successor handoff and all three input theorem quartets:
the critical-window smoother, the assembled Perron bridge, and the exact
Barnes/max-leakage packet.

## 0. Outcome

Put \(q=67\), \(L=\log q\), and
\[
 \omega(t)=q^{-1/2-it}=q^{-1/2}e^{-itL},
 \qquad a=|\omega(t)|=q^{-1/2}<1.
\tag{0.1}
\]
Define the ordinary, duplicate-\(q\), and \(q\)-free Möbius prefixes
\[
\begin{aligned}
 M_X(t)&=\sum_{n\le X}{\mu(n)\over n^{1/2+it}},\\
 D_X(t)&=\sum_{n\le X}{\beta(n)\over n^{1/2+it}},
 \qquad
 \beta(n)=\mu(n)-\mathbf1_{q\mid n}\mu(n/q),\\
 A_X(t)&=\sum_{\substack{n\le X\\q\nmid n}}
 {\mu(n)\over n^{1/2+it}}.
\end{aligned}
\tag{0.2}
\]
Every prefix below one is zero.

The first result is an exact finite scale ladder:
\[
 \boxed{
 D_X=M_X-\omega M_{X/q},\qquad
 M_X=A_X-\omega A_{X/q},}
\tag{0.3}
\]
and hence
\[
 \boxed{
 D_X=A_X-2\omega A_{X/q}+\omega^2A_{X/q^2}.}
\tag{0.4}
\]
The inverses terminate exactly:
\[
\boxed{
\begin{aligned}
 M_X&=\sum_{k\ge0}\omega^kD_{X/q^k},\\
 A_X&=\sum_{k\ge0}(k+1)\omega^kD_{X/q^k}.
\end{aligned}}
\tag{0.5}
\]

Thus the visible \(67\)-adic coefficient vector \((1,-2,1)\) is a
**squared scale filter**, not a frequency notch. Its inverse has absolutely
summable scale coefficients because \(a<1\).

This remains true after every positive Fourier weighting. Let \(\nu\) be
any positive measure for which the prefixes lie in \(L^2(\nu)\), and put
\[
 \mathfrak M_\nu(X)=
 \sup_{1\le Y\le X}\|M_Y\|_{L^2(\nu)},
\quad
 \mathfrak D_\nu(X)=
 \sup_{1\le Y\le X}\|D_Y\|_{L^2(\nu)},
\quad
 \mathfrak A_\nu(X)=
 \sup_{1\le Y\le X}\|A_Y\|_{L^2(\nu)}.
\tag{0.6}
\]
Then
\[
\boxed{
 (1-a)\mathfrak M_\nu(X)
 \le\mathfrak D_\nu(X)
 \le(1+a)\mathfrak M_\nu(X)}
\tag{0.7}
\]
and
\[
\boxed{
 (1-a)^2\mathfrak A_\nu(X)
 \le\mathfrak D_\nu(X)
 \le(1+a)^2\mathfrak A_\nu(X).}
\tag{0.8}
\]
All constants depend only on \(q\), not on \(X\), the frequency window, or
the detector.

For the critical measure
\[
 d\nu_X(t)=
 {1\over2\pi}|\widehat B_{r,\infty}(t)|^2
 \mathbf1_{\{|t|\le
 \exp(\sqrt{(\log2)(\log X)})\}}\,dt,
\tag{0.9}
\]
the imported tail theorem is uniform over \(1\le Y\le X\). Consequently
\[
\boxed{
\begin{aligned}
\mathrm{RH}
&\Longleftrightarrow
 \mathfrak D_{\nu_X}(X)^2=X^{o(1)}\\
&\Longleftrightarrow
 \mathfrak M_{\nu_X}(X)^2=X^{o(1)}\\
&\Longleftrightarrow
 \mathfrak A_{\nu_X}(X)^2=X^{o(1)}.
\end{aligned}}
\tag{0.10}
\]
Equation (0.10) is not offered as another route by itself. It is a sharp
firewall:

> The duplicate-\(67\) factor supplies no \(X\)-dependent contraction in
> the actual critical window. Any proof must use arithmetic cancellation
> already present in ordinary Möbius prefixes, or signed interactions that
> are destroyed by the positive maximal norm.

The same obstruction survives \(67\)-adic short multiplicative blocks and
absolute-value bilateral Perron estimates. The smallest positive block
estimate left by these failed attacks is stated in Section 6.

## 1. Exact coefficient and prefix algebra

The beta definition gives
\[
\begin{aligned}
D_X(t)
&=\sum_{n\le X}{\mu(n)\over n^{1/2+it}}
 -\sum_{qm\le X}{\mu(m)\over(qm)^{1/2+it}}\\
&=M_X(t)-\omega(t)M_{X/q}(t),
\end{aligned}
\tag{1.1}
\]
which proves the first identity in (0.3), including the sharp endpoint.

Every squarefree integer divisible by \(q\) is \(qm\) with \(q\nmid m\) and
\(\mu(qm)=-\mu(m)\). Therefore
\[
 M_X=A_X-\omega A_{X/q}.
\tag{1.2}
\]
Applying the same filter twice proves (0.4). Coefficientwise, for
squarefree \(q\)-free \(u\),
\[
 \beta(q^iu)=
 \begin{cases}
 \mu(u),&i=0,\\
 -2\mu(u),&i=1,\\
 \mu(u),&i=2,\\
 0,&i\ge3.
 \end{cases}
\tag{1.3}
\]

Iterating (1.1) gives
\[
 M_X=\sum_{k=0}^{K}\omega^kD_{X/q^k}
 +\omega^{K+1}M_{X/q^{K+1}}.
\tag{1.4}
\]
For \(K=\lfloor\log_qX\rfloor\), the last prefix is zero. This proves the
first inverse in (0.5). The formal identity
\[
 {1\over(1-z)^2}=\sum_{k\ge0}(k+1)z^k
\tag{1.5}
\]
proves the second.

No limiting Dirichlet series, endpoint smoothing, or hypothesis on Möbius
cancellation is used.

## 2. Weighted maximal scale isomorphism

For every \(Y\le X\), (1.1), Minkowski, and
\(|\omega|=a\) give
\[
 \|D_Y\|_{L^2(\nu)}
 \le \|M_Y\|_{L^2(\nu)}
 +a\|M_{Y/q}\|_{L^2(\nu)}.
\tag{2.1}
\]
Taking the supremum proves the upper half of (0.7). Conversely, (0.5)
gives
\[
\begin{aligned}
\|M_Y\|_{L^2(\nu)}
&\le\sum_{k\ge0}a^k
 \|D_{Y/q^k}\|_{L^2(\nu)}\\
&\le{1\over1-a}\mathfrak D_\nu(X).
\end{aligned}
\tag{2.2}
\]
This proves the lower half. Applying the argument twice, or using
\[
 \sum_{k\ge0}(k+1)a^k=(1-a)^{-2},
\tag{2.3}
\]
proves (0.8).

The result applies to every measurable frequency window, positive Fourier
weight, and fixed linear translation-invariant filter for which the norms
are finite. Such a filter merely replaces \(d\nu\) by its multiplier
modulus squared times \(d\nu\). In particular:

- the infinite dyadic smoother does not change the scale conditioning;
- adding any fixed finite-difference notch does not change it;
- linear reflection/differential preprocessing before the nonlinear
  reflection square does not change it.

The last statement is deliberately limited to linear preprocessing. The
horizon-dependent reflection norm is nonlinear and is not claimed to
commute with the scale filter.

## 3. Why the critical maximal criterion follows

Let
\[
 d\nu_\infty(t)=
 {1\over2\pi}|\widehat B_{r,\infty}(t)|^2dt.
\tag{3.1}
\]
The imported detector theorem says
\[
 \mathrm{RH}\Longleftrightarrow
 \|D_X\|_{L^2(\nu_\infty)}^2=X^{o(1)}.
\tag{3.2}
\]
For any nonnegative function \(E(Y)=Y^{o(1)}\),
\[
 \sup_{1\le Y\le X}E(Y)=X^{o(1)}:
\tag{3.3}
\]
given \(\delta>0\), all sufficiently large \(Y\) contribute at most
\(X^\delta\), while the finitely many smaller prefixes contribute a fixed
constant. Hence (3.2) is equivalent to its maximal version.

Now use the exact critical tail estimate with
\[
 T_X=\exp(\sqrt{(\log2)(\log X)}).
\tag{3.4}
\]
For every \(Y\le X\), its proof gives
\[
\begin{aligned}
\log\left(
 {1\over2\pi}\int_{|t|\ge T_X}
 |\widehat B_{r,\infty}(t)|^2|D_Y(t)|^2dt
\right)
&\le
\log Y-{(\log T_X)^2\over\log2}
+O(\log T_X+1)\\
&\le O(\sqrt{\log X}).
\end{aligned}
\tag{3.5}
\]
Thus the supremum of all discarded tails is \(X^{o(1)}\). The full maximal
beta criterion is equivalent to the truncated one. Equations
(0.7)--(0.8), applied with \(\nu_X\), prove (0.10).

This maximal prefix is load-bearing. At one isolated endpoint, the inverse
(0.5) necessarily calls smaller prefixes. The maximal envelope retains
them at only constant cost.

## 4. Short multiplicative blocks do not create a gain

Fix \(X\), write
\[
 M_k=M_{X/q^k},\qquad D_k=D_{X/q^k},
\tag{4.1}
\]
and let both sequences terminate when their prefix is below one. Define
\[
 U_k=M_k-M_{k+1},\qquad V_k=D_k-D_{k+1}.
\tag{4.2}
\]
These are the ordinary and beta sums on consecutive multiplicative
\(q\)-blocks. Equation (0.3) gives
\[
 \boxed{V_k=U_k-\omega U_{k+1}.}
\tag{4.3}
\]

Take \(H=L^2(\nu)\) and regard \(U=(U_k)\) as a finite
\(\ell^2(\mathbf Z_{\ge0};H)\) sequence. The forward scale shift has norm at
most one, while multiplication by \(\omega\) has norm \(a\). The triangle
and reverse-triangle inequalities give
\[
\boxed{
 (1-a)^2\sum_k\|U_k\|_H^2
 \le\sum_k\|V_k\|_H^2
 \le(1+a)^2\sum_k\|U_k\|_H^2.}
\tag{4.4}
\]
The constants are optimal for the abstract scale operator: increasingly
long aligned and alternating scale modes approach the two endpoints.

Thus passing to short multiplicative blocks and then taking positive
squares cannot extract a duplicate-\(67\) saving. It discards cross-block
signs while leaving the block-square burden unchanged up to a constant.

## 5. Bilateral Perron sees a bounded holomorphic unit

For every \(w\) with \(\Re w\ge1/2\),
\[
 |q^{-w}|\le q^{-1/2}=a.
\]
Consequently
\[
\boxed{
 1-a\le|1-q^{-w}|\le1+a,}
\tag{5.1}
\]
and
\[
 {1\over1-q^{-w}}=\sum_{k\ge0}q^{-kw}
\tag{5.2}
\]
converges absolutely throughout that closed half-plane.

For the two beta multipliers in the bilateral Perron formula, whenever
\(\Re w_1,\Re w_2\ge1/2\),
\[
\boxed{
(1-a)^2
\le|(1-q^{-w_1})(1-q^{-w_2})|
\le(1+a)^2.}
\tag{5.3}
\]
The exceptional numerator therefore:

- cancels no reciprocal-zeta pole;
- cancels neither Perron denominator;
- creates no small Fourier interval;
- changes every absolute-value estimate only by a \(q\)-dependent constant.

Signed expansion of this unit may still interact with residues or other
source channels. Equation (5.3) is a no-go for an **absolute contraction**,
not for every possible signed contour argument.

The Neumann series (5.2), the prefix inverse (0.5), and the block inverse in
Section 4 are the same scale isomorphism in three coordinates.

## 6. The smallest positive block estimate left alive

Since
\[
 M_X=\sum_{k\ge0}U_k,
\]
Cauchy gives
\[
 \|M_X\|_{L^2(\nu_X)}^2
\le(1+\lfloor\log_qX\rfloor)
\sum_k\|U_k\|_{L^2(\nu_X)}^2.
\tag{6.1}
\]
The same bound, with the first block omitted, controls
\(M_{X/q}=\sum_{k\ge1}U_k\).  Hence (0.3) also gives the completely
explicit implication
\[
 \|D_X\|_{L^2(\nu_X)}^2
 \le 2(1+a^2)(1+\lfloor\log_qX\rfloor)
 \sum_k\|U_k\|_{L^2(\nu_X)}^2.
\tag{6.1a}
\]
The factor \(1+\log_qX\) is \(X^{o(1)}\). Therefore the explicit estimate
\[
\boxed{
\begin{aligned}
\mathrm{MOBIUS\text{-}CRIT\text{-}BLOCK:}\qquad
\sum_{k\ge0}{1\over2\pi}
\int_{|t|\le T_X}
|\widehat B_{r,\infty}(t)|^2
\left|
M_{X/q^k}(t)-M_{X/q^{k+1}}(t)
\right|^2dt
=X^{o(1)}
\end{aligned}}
\tag{6.2}
\]
would imply the critical beta energy bound and hence RH.

This is a deliberately positive, and probably stronger, sufficient target;
it is not claimed equivalent to RH. It is the smallest estimate produced
by the present short-block attempt because:

1. every block is a literal multiplicative interval
   \((X/q^{k+1},X/q^k]\);
2. all Fourier signs inside a block remain intact;
3. only cross-block interference is discarded;
4. beta and ordinary-Möbius block energies are equivalent by (4.4).

No estimate for (6.2) is proved. Standard positive block orthogonalization
has merely exposed the remaining arithmetic burden.

## 7. Interpretation

The four requested attacks now have exact verdicts:

| attack | exact outcome |
|---|---|
| duplicate-\(67\) scale identity | boundedly invertible first difference; squared relative to the \(67\)-free source |
| bilateral Perron | exceptional numerator is a bounded holomorphic unit on \(\Re w\ge1/2\) |
| linear reflection/differential preprocessing | commutes with the weighted scale isomorphism |
| short multiplicative blocks | beta and ordinary-Möbius positive block energies differ by constants only |

This prevents a false source of optimism: the duplicated prime preserves
and orients the native source, but generates no asymptotic cancellation by
itself.

The live possibilities are narrower:

- retain signed cross-block interactions rather than positive block
  squares;
- prove arithmetic cancellation inside (6.2);
- use bilateral residue cancellation that genuinely depends on
  \(1/\zeta\), not only on its exceptional numerator;
- exploit nonlinear reflection geometry, which lies outside the linear
  isomorphism.

## 8. Proof and scope ledger

| statement | grade |
|---|---|
| prefix identities (0.3)--(0.4) | **PROVED EXACT, INCLUDING ENDPOINTS** |
| finite Neumann inverses (0.5) | **PROVED EXACT** |
| weighted maximal bounds (0.7)--(0.8) | **PROVED FOR EVERY POSITIVE FOURIER MEASURE** |
| critical maximal equivalence (0.10) | **PROVED FROM THE PINNED RH EQUIVALENCE AND CRITICAL TAIL** |
| short-block identity and Hilbert bounds (4.3)--(4.4) | **PROVED EXACT** |
| optimality of abstract block constants | **PROVED BY LONG SCALE MODES** |
| Perron-unit bounds (5.1)--(5.3) | **PROVED EXACT** |
| duplicate-\(67\) asymptotic contraction | **REFUTED FOR POSITIVE WEIGHTED MAXIMAL/BLOCK NORMS** |
| signed cross-block or bilateral residue cancellation | **OPEN / NOT REFUTED** |
| MOBIUS-CRIT-BLOCK | **OPEN SUFFICIENT TARGET** |
| critical beta estimate, RH, or GRH | **NOT PROVED** |

## 9. Bounded replay

~~~text
python -B research/l-families/atlas/function_field/ffps_duplicate67_critical_scale_filter_firewall.py --check
python -B -O research/l-families/atlas/function_field/ffps_duplicate67_critical_scale_filter_firewall.py --check
python -B -m unittest tests.test_ffps_duplicate67_critical_scale_filter_firewall
python -B -O -m unittest tests.test_ffps_duplicate67_critical_scale_filter_firewall
python -B -m ruff check research/l-families/atlas/function_field/ffps_duplicate67_critical_scale_filter_firewall.py tests/test_ffps_duplicate67_critical_scale_filter_firewall.py
python -B -m ruff format --check research/l-families/atlas/function_field/ffps_duplicate67_critical_scale_filter_firewall.py tests/test_ffps_duplicate67_critical_scale_filter_firewall.py
~~~

The replay uses integer coefficient identities, formal finite scale
filters, rational Hilbert controls, and sequences of length at most 12. It
enumerates no zeta zero and performs no floating-point computation.
