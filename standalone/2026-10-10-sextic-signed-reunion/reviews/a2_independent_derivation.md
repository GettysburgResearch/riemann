# A two-cutoff bound for the full arithmetic A2 family

**Status:** proposed conditional composition theorem. Assuming the explicitly stated moving-exclusion block adapter, a truncation of the arithmetic correction makes the improved short cube inverse summable. This proves a stronger positive norm bound for the full arithmetic A2 completion over all rows. The signed centered covariance and full inverse fourth moment remain open.

**Authorship:** spectral_descent_attack. The local deletion adapter and this composition require their own independent reviews. The conclusion is not inferred from a generic completed norm inequality.

**Sources:**

- PR #914, `0cc0428fedbbfc340044c7451b3d392c1da9a103`, `standalone/2026-10-10-sextic-moment-conductor-core/A2_COMPLETION.md`, SHA-256 `d99eade56807077b07e5ec1325001f1592115db216e1e10e6a3906a3e01f0aad`. We use equations (4.3)–(4.5), fixed-auxiliary normalization (5.8), and the classical-tail proof of Theorem 5.4.
- The companion `pass2_spectral_hybrid_cube.md`, especially its modular block hypothesis and equations (7.1)–(7.2), with the exact PR #921 and #923 sources bound there.
- The separate original-column deletion adapter must establish the coefficients and constants in (1.3)–(1.4) below. It is an explicit premise of this note until independently proved and source-bound in the assembled packet.

The imported theta and angular assumptions of the companion are retained. The arithmetic A2 identity itself is finite and native; it does not import an unproved analytic extension of a Weyl-group Dirichlet series.

## 1. Objects and the local-adapter premise

Use the exact primary convention and literal nonunit zeros of the source. For squarefree good ideals q0 and f define the unnormalized literal polynomial

\[
P_{q_0}(A,B;k,f)=
\sum_{\substack{ab\ {\rm squarefree}\\(ab,q_0S)=1}}
a_\xi(ab)\chi_{ab}(k)\chi_{ab}(f)^4
W_1(Na/A)W_2(Nb/B),
\tag{1.1}
\]

and the full arithmetic completion

\[
Q_{q_0}(A,B;k,f)=
\sum_{\substack{n_1,n_2\\(n_1n_2,q_0S)=1}}
\mathfrak a_\xi(n_1,n_2)
\chi_{n_1n_2}(k)\chi_{n_1n_2}(f)^4
W_1(Nn_1/A)W_2(Nn_2/B).
\tag{1.2}
\]

Here \(\mathfrak a_\xi\) is exactly the normalized globally twisted A2 coefficient defined in the source. At a good prime its supported valuation pairs are (0,0),(1,0),(0,1),(1,2),(2,1),(2,2), with values 1,a_p,a_p,b_p,b_p,b_pa_p; no (1,1) term is added.

Write

\[
F=Nf,\qquad Z=N\!\left(q_0/(q_0,f)\right),\qquad
J=FZ,\qquad K=F^{2/3}Z^{1/3}.
\tag{1.3}
\]

Thus \(K\le J^{2/3}\). The required local-adapter premise is that the **actual two-Möbius block factorization** for the normalized literal polynomial \(P_{q_0}/\sqrt{AB}\) has the three costs (1,J,K), preserving both scalar characters, every zero mask, and the joint support cutoff of the companion. In particular the companion's short and long bounds (7.1)–(7.2) apply at every smaller rectangle and every moving q0,f.

When a correction triple c,d,e occurs below, it is disjoint and coprime to q0 f S. Its child parameters are q0'=q0 cde and f'=ef. Consequently (1.3) gives exactly

\[
J'=J\,Nc\,Nd\,Ne,
\qquad
K'=K\,(Nc\,Nd)^{1/3}(Ne)^{2/3}.
\tag{1.4}
\]

The overlap at e has been used: e belongs to both q0' and f'. This is why its cost is different from that of c or d. There is no assumption that the old q0 and f are coprime.

All parameters have fixed polynomial bounds in a common D>=2. The stronger scalar input has exponent beta=11/12; below we first allow every fixed \(1/2<\beta\le1\). The row norm sums every nonzero element in \(H\le Nk<2H\), with H>=1.

## 2. Exact arithmetic correction and its fixed-auxiliary norm

The finite source identity at A=B=D is

\[
Q_{q_0}(D,D;k,f)=
\sum_{\substack{c,d,e\ {\rm disjoint\ squarefree}\\(cde,q_0fS)=1}}
\Omega_{c,d,e}(k,f)
P_{q_0cde}(A',B';k,ef),
\tag{2.1}
\]

where

\[
A'=\frac{D}{Nc(Nd)^2(Ne)^2},\qquad
B'=\frac{D}{(Nc)^2Nd(Ne)^2},
\tag{2.2}
\]

\[
\Omega_{c,d,e}(k,f)=
\sqrt{N(cde)}\lambda(cde)^3a_\xi(e)
\chi_{cd}(k)^3\chi_e(k)^4\chi_e(f)^4.
\tag{2.3}
\]

In particular its modulus is at most \(\sqrt{N(cde)}\), including the literal zero rows. Normalize the original Q by D and every child P by \(\sqrt{A'B'}\). The exact norm multiplier becomes

\[
w(c,d,e)=\sqrt{N(cde)}\sqrt{\frac{A'B'}{D^2}}
=\frac1{Nc\,Nd\,(Ne)^{3/2}}.
\tag{2.4}
\]

We keep f fixed when applying (2.4). A later average over the original f annulus may be taken from this uniform bound; no enlargement of a child auxiliary annulus is necessary.

Choose an arithmetic correction cutoff T>=1. Split (2.1) into \(N(cde)\le T\) and its complement. For each small correction, apply the companion's smooth short/long cube inversion with one common cutoff R>=1. The decompositions are finite and exact. The large correction sum is kept intact and estimated by the classical all-row coefficient bound.

## 3. Summing the short cube contributions below T

Interchange the physical axes, with their tests, when needed so that the smaller child scale is outer. For one half of the correction sum take \(Nc\le Nd\), and abbreviate their norms by c,d,e only within the positive calculations of this section. Then

\[
m=A'=\frac{D}{cd^2e^2},\qquad
M=B'=\frac{D}{c^2de^2},\qquad m\le M.
\]

The other half is identical after c,d and the two fixed tests are exchanged. Equal norms may be assigned to either half once.

The modular short estimate is

\[
Hm+J'H^2mM^{\beta-3/2}R^{5/2-\beta}
+K'H^{4/3}m^{4/3}M^{-2/3}R^{2\beta},
\tag{3.1}
\]

up to D^epsilon. The support-restricted cube range can be smaller than R in a child; the estimate remains a valid upper bound in that case. Every nonempty scale below one belongs to a fixed compact interval and changes only the fixed constants.

The square root of the first term times (2.4) has weight

\[
c^{-3/2}d^{-2}e^{-5/2},
\]

so its norm sum converges and contributes \(O((HD)^{1/2})\).

For the second term, substituting (1.4) and (2.2) gives exactly

\[
\begin{split}
w(c,d,e)\,[J'H^2mM^{\beta-3/2}R^{5/2-\beta}]^{1/2}
={}&[JH^2D^{\beta-1/2}R^{5/2-\beta}]^{1/2}\\
&\times c^{1/2-\beta}
d^{-3/4-\beta/2}e^{-1/2-\beta}.
\end{split}
\tag{3.2}
\]

The e sum converges, but the joint c,d sum does not converge at infinity for the beta range of interest. The cutoff is used here, rather than silently bounding that sum.

### Lemma 3.1: the precise truncated divisor loss

For T>=1 and \(1/2<\beta\le1\),

\[
\sum_{\substack{Nc\le Nd\\N(cde)\le T}}
(Nc)^{1/2-\beta}(Nd)^{-3/4-\beta/2}(Ne)^{-1/2-\beta}
\ll_\beta T^{7/8-3\beta/4}.
\tag{3.3}
\]

Dropping squarefreeness and coprimality only enlarges this nonnegative bound.

**Proof.** Fix e and set U=T/(Ne). For \(Nd\le\sqrt U\), ideal counting and partial summation bound the inner c sum by \((Nd)^{3/2-\beta}\). Its product with the d weight is \((Nd)^{3/4-3\beta/2}\). Summing gives \(U^{7/8-3\beta/4}\).

For \(Nd>\sqrt U\), use \(Nc\le U/(Nd)\). The inner sum is at most \((U/Nd)^{3/2-\beta}\), leaving

\[
U^{3/2-\beta}
\sum_{Nd>\sqrt U}(Nd)^{-9/4+\beta/2}
\ll U^{7/8-3\beta/4}.
\]

The exponent in the tail is strictly below minus one. Finally sum over e with weight \((Ne)^{-1/2-\beta}\), using the extra nonpositive power of Ne from U. That ideal sum converges because beta>1/2. This proves (3.3). □

After squaring, the second short monomial therefore acquires the precise factor \(T^{7/4-3\beta/2}\).

For the third term, (1.4) gives the norm weight

\[
c^{-5/6}d^{-11/6}e^{-11/6}.
\tag{3.4}
\]

Its ordered c,d sum converges: summing c<=d costs at most \((Nd)^{1/6}\), leaving the convergent d power minus five-thirds. The e sum also converges. Hence this monomial acquires no T power.

We have proved

\[
\boxed{\begin{split}
\|\text{small arithmetic, short cube part}\|_2^2
\ll D^\epsilon\big[&HD
+JH^2D^{\beta-1/2}T^{7/4-3\beta/2}R^{5/2-\beta}\\
&+KH^{4/3}D^{2/3}R^{2\beta}\big].
\end{split}}
\tag{3.5}
\]

No signed arithmetic sum has been enlarged as though it were nonnegative. The finite exact decomposition precedes the row norms; only the resulting positive norm accounting sums were enlarged.

## 4. The two long tails

For fixed correction c,d,e, the smooth long cube tail has norm squared

\[
H+H^{1/6}A'B'R^{-3}+(HA'B')^{2/3}R^{-2},
\tag{4.1}
\]

with every moving mask in its arbitrary bounded physical coefficient. Multiplying square roots by (2.4), the three divisor weights are

\[
(cd)^{-1}e^{-3/2},\qquad
(cd)^{-5/2}e^{-7/2},\qquad
(cd)^{-2}e^{-17/6}.
\tag{4.2}
\]

The first costs only the finite harmonic sums in c,d; the remaining two converge absolutely. Summing even beyond the small-correction set, in this nonnegative accounting step, gives

\[
\|\text{small arithmetic, long cube part}\|_2^2
\ll D^\epsilon
\left[H+H^{1/6}D^2R^{-3}+H^{2/3}D^{4/3}R^{-2}\right].
\tag{4.3}
\]

For the large arithmetic correction \(N(cde)>T\), use the direct classical all-row bound on each complete literal child. The same weights (4.2) occur with R absent. Grouping by C=cde, bounding its multiplicity by the fixed-order ideal divisor function, and summing the tails gives

\[
\|\text{large arithmetic part}\|_2^2
\ll D^\epsilon
\left[H+H^{1/6}D^2T^{-3}+H^{2/3}D^{4/3}T^{-2}\right].
\tag{4.4}
\]

Explicitly, the second norm sum is bounded by
\(\sum_{NC>T}(NC)^{-5/2}d_{3,K}(C)\ll T^{-3/2+\epsilon}\);
the third uses the exponent two and gives \(T^{-1+\epsilon}\).
The extra e powers in (4.2) improve both bounds. The harmonic base term retains its finite support and is only absorbed into D^epsilon. There is no falsely convergent Euler product at exponent one.

## 5. Main all-row A2 theorem

### Theorem 5.1

Under the exact local-adapter premise of Section 1 and the scalar premise with beta, for polynomially bounded R,T>=1,

\[
\boxed{\begin{split}
\sum_{k\asymp H}|Q_{q_0}(D,D;k,f)/D|^2
\ll D^\epsilon\big[&HD
+JH^2D^{\beta-1/2}T^{7/4-3\beta/2}R^{5/2-\beta}
+KH^{4/3}D^{2/3}R^{2\beta}\\
&+H+H^{1/6}D^2(R^{-3}+T^{-3})
+H^{2/3}D^{4/3}(R^{-2}+T^{-2})\big].
\end{split}}
\tag{5.1}
\]

All nonzero element rows and all original q0,f overlaps are retained. The statement concerns the full arithmetic completion (1.2), including its nonsquarefree product columns.

**Proof.** Apply the row Hilbert-space triangle inequality to the three exact portions and use (3.5), (4.3), and (4.4). All source constants are uniform at their declared polynomial scales. □

Taking T=R gives the simpler envelope

\[
\boxed{\begin{split}
\sum_{k\asymp H}|Q_{q_0}(D,D;k,f)/D|^2
\ll D^\epsilon\big[&HD
+JH^2D^{\beta-1/2}R^{17/4-5\beta/2}
+KH^{4/3}D^{2/3}R^{2\beta}\\
&+H+H^{1/6}D^2R^{-3}
+H^{2/3}D^{4/3}R^{-2}\big].
\end{split}}
\tag{5.2}
\]

This common choice is sufficient for the power optimization: all positive short terms increase with both R,T, while the combined tails are controlled by their smaller value. Replacing the larger cutoff by the smaller can only improve the positive-power envelope, up to fixed constants in the sum of tails.

### Corollary 5.2: a larger A2 diagonal-size range

Because K<=J^(2/3), (5.2) is \(O(D^{2+\epsilon})\) throughout

\[
\boxed{
1\le H\le
D^{36(5-2\beta)/(161-10\beta)}
J^{-72/(161-10\beta)}.}
\tag{5.3}
\]

At beta=11/12 this is

\[
\boxed{H\le D^{684/911}J^{-432/911}.}
\tag{5.4}
\]

The counting scalar beta=1 gives \(H\le D^{108/151}J^{-72/151}\).

**Proof.** Set R=T=H^(1/18). The second monomial becomes
\(J D^{\beta-1/2}H^{(161-10\beta)/72}\), so (5.3) is precisely its D-squared condition. The classical middle tail is exactly D squared. The remaining terms are bounded as in Corollary 5.2 of the companion. Indeed (5.3) implies its literal range, because

\[
\frac{72}{161-10\beta}\le\frac{36}{77-2\beta}
\quad\Longleftrightarrow\quad 6\beta\le7,
\]

and the common nonnegative bracket is \((5-2\beta)/2-\log_DJ\). This also gives H<=D and bounds the third monomial using K<=J^(2/3). □

The full A2 range is smaller than the literal hybrid range, as expected from the extra correction sum, but substantially larger than the direct full-cube-inverse range. None of these row exponents is a zero-free boundary.

## 6. Explicit balanced examples when q0=f=1

Assume the local adapter uniformly at the moving children even though the original q0=f=1. Then J=K=1 in the final estimate. At beta=11/12, (5.2) reads

\[
HD+H^2D^{5/12}R^{47/24}
+H^{4/3}D^{2/3}R^{11/6}
+H+H^{1/6}D^2R^{-3}+H^{2/3}D^{4/3}R^{-2}.
\tag{6.1}
\]

For \(1\le H\le D^{150/443}\), take
\(R=T=D^{8/29}H^{-7/29}\). The third and fifth monomials coincide and dominate, giving

\[
\boxed{
\sum_{k\asymp H}|Q_1(D,D;k,1)/D|^2
\ll D^{34/29+\epsilon}H^{155/174}.}
\tag{6.2}
\]

For \(D^{150/443}\le H\le D^{19/22}\), take
\(R=T=D^{38/119}H^{-44/119}\). The second and fifth monomials coincide and dominate, giving

\[
\boxed{
\sum_{k\asymp H}|Q_1(D,D;k,1)/D|^2
\ll D^{124/119+\epsilon}H^{911/714}.}
\tag{6.3}
\]

At the first cutoff, the ratio of the second to the common monomial has exponent \(-25/116+(443/696)\log_DH\), hence the junction 150/443. At the second cutoff the reverse comparison gives the same junction. The other four monomials have nonpositive relative exponents throughout the stated intervals, as may be checked by their affine endpoint values.

At H equal to the square root of D,

\[
\boxed{
R=T=D^{16/119},\qquad
\sum_{k\asymp D^{1/2}}|Q_1(D,D;k,1)/D|^2
\ll D^{2399/1428+\epsilon}.}
\tag{6.4}
\]

The full arithmetic A2 coefficient, its nonunit zeros and all repeated-prime rows are present in this estimate.

## 7. Fixed smooth tests, auxiliary averages, and remaining boundary

The proof is stated with product tests. A fixed smooth compactly supported bivariate test is covered by Mellin separation with integrable polynomially weighted transforms, using the same finite seminorm order. A fixed scalar Schwartz row weight is covered by annular summation and an enlarged reference parameter on each annulus. These statements do not cover a changing row-dependent bilinear kernel without its own uniform separation proof.

The estimate is uniform in the original fixed f. Thus it can be summed over a squarefree f annulus using J<=constant times F Nq0 and K<=J^(2/3); ideal counting supplies the expected O(F) number of terms. This is a positive auxiliary average. No signed cancellation between different f is obtained from that operation.

The original adverse fourth-moment dual height remains approximately D^(3-theta), beyond the useful ranges above. The one-sided signed covariance with its original coupled kernel and exact reconstructed product-column subtraction remains open. This theorem makes the moving A2 positive norm interface quantitative under the stated local adapter; it does not identify that positive norm with the desired centered signed expression.
