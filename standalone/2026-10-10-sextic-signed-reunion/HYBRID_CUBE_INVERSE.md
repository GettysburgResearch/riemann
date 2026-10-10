# Smooth cube inversion with two Möbius savings

**Status:** proposed source-conditional theorem. This note combines the exact two-scalar inverse in PR #921 with the short/long regrouping in PR #923. It improves the quantitative bound for the literal balanced Gauss polynomial over all nonzero element rows and retains the refined moving-auxiliary costs. It does not estimate the signed centered fourth-moment covariance or prove a new zero-free boundary.

**Authorship:** spectral_descent_attack. Independent mathematical review is required before publication as reviewed mathematics.

**Frozen dependencies:**

- PR #921, commit `4e6d4aa57ae4cb04d76b2b31279ac367951b469a`, `standalone/2026-10-10-sextic-centered-covariance/CUBE_INVERSE.md`, SHA-256 `a865338882111bf3bc96ffc539dd93f3b2ee59390499caaf14852ed8cde77804`: exact inverse, both scalar estimates, complete block factorization, and the joint support cutoff.
- The same commit and directory, `ARBITRARY_ROW_MOMENTS.md`, SHA-256 `a12605808006c07f1a413e743545441e0541577367c8ea1bbe09a7fc493cc52a`: all-row block adapter and refined auxiliary costs, especially Sections 5–7. Its input is the actual coefficient factorization, not a norm inequality with arbitrary coefficients substituted.
- PR #923, commit `1a1152008706f7e24fa1efe4990588f8f99c5d8d`, `standalone/2026-10-10-sextic-separated-cores/SHORT_CUBE_RAW_GAIN.md`, Git blob `9f3beb9b3d5a5e683e932ea2882dbdbae120596b`, SHA-256 `8d97d0a4e6a0eef6ca0178e0dca7ff6e2cd059d594eba1e45fee47d57563cc40`, and `ALL_ROW_COMPLETION_AND_RAW_GAIN.md`, Git blob `6518adf695643c31e380028ef327fec58631b8f9`, SHA-256 `a0e6bd5517a81f44d2a18bd32dc4f0db623b9951c17068e56af7009c8914fdec`: the physical long-inverse regrouping and its all-row classical estimate. We prove the smooth-cutoff version below.
- PR #913, commit `6498d6cc2eded03159c7332b25fd224ad07f89c1`, `standalone/2026-10-10-sextic-moment-descent/REFINED_ALL_ROW_SIEVE.md`, SHA-256 `6879e094fb63969ddc88c637bf633cf46360d144d2b1615573647e734b4141e8`, Theorem 3.4.

The theta inputs retain their stated OpenAI/math foundation at `adc7f1241b42e322a6451854ab7e4b4c146bf78a`. The stronger scalar exponent remains conditional on the imported canonical/angular theorem. The classical all-row sieve is a separately named input; no higher inverse moment is assumed.

## 1. Literal family and hypotheses

Use the Eisenstein field, fixed bad set S, primary generators, and literal nonunit zeros of the sources. Put

\[
a_\xi(n)=\overline{\alpha(n)}\gamma_2(n)\xi(n),
\qquad \lambda(n)=\overline{\alpha(n)}\xi(n).
\]

Here lambda denotes the multiplicative coefficient in this note, not a generator of the ramified prime. For fixed smooth compactly supported tests, define the normalized polynomial

\[
P_{A,B}(k;\mathfrak q)=\frac1{\sqrt{AB}}
\sum_{\substack{an\ {\rm squarefree}\\(an,S)=1}}
a_\xi(an)\chi_{an}(k\mathfrak q^4)
W_1(Na/A)W_2(Nn/B).
\tag{1.1}
\]

The auxiliary ideal \(\mathfrak q\) is squarefree, primary and outside S; write \(Q=N\mathfrak q\). No restriction \((k,\mathfrak q)=1\) is imposed. The row sum below includes every nonzero element in \(H\le Nk<2H\), all units and every repeated or bad-prime factor. Assume \(D\ge2\), \(H,Q\ge1\), all bounded by fixed powers of D, and initially take \(A=B=D\).

Let \(1/2<\beta\le1\). We retain the two identical scalar premises from PR #921: each of the actual negative-allocation and inverse-cube coefficients satisfies, uniformly in its moving squarefree row index and exclusions,

\[
\sum_{(g,CS)=1}\mu(g)\eta(g)\overline{\alpha(g)}^3
\chi_s(g)^3V(Ng/L)
\ll D^\epsilon L^\beta\|V\|_{C^J}.
\tag{1.2}
\]

The fixed ray characters eta may differ in the two applications. The conductor and exclusion have fixed polynomial bounds, and a common finite smooth seminorm order is available. Counting supplies beta=1. The named angular argument supplies beta=11/12 with an arbitrary small loss under its declared canonical premises.

## 2. A smooth exact short/long identity

Choose once a smooth function omega on the nonnegative reals, equal to one on [0,1], zero on [2,infinity), and bounded between zero and one. Let \(R\ge1\). In the exact source identity

\[
P_{D,D}(k;\mathfrak q)=
\sum_h\frac{\mu(h)\lambda(h)^3\chi_h(k\mathfrak q^4)^3}{Nh}
\mathcal C^{(h)}_{D,D/(Nh)^3}(k\mathfrak q^4),
\tag{2.1}
\]

define the short part \(\mathcal S_R\) by multiplying each h term by omega(Nh/R). Define the long part by the complementary factor. Equation (2.1) is finite on physical support, so

\[
P_{D,D}=\mathcal S_R+\mathcal L_R
\tag{2.2}
\]

is exact at each nonzero row. This smooth truncation is necessary to use (1.2) with a fixed number of seminorms; no unsmoothed sharp cutoff is left in a scalar Möbius sum.

Expand the physical cube index b in the long part and put d=hb. Complete multiplicativity, including its zero values, gives

\[
\mathcal L_R(k)=\sum_{Nd>R}
\frac{c_R(d)\lambda(d)^3\chi_d(k\mathfrak q^4)^3}{Nd}
P^{[d]}_{D,D/(Nd)^3}(k;\mathfrak q),
\tag{2.3}
\]

where \(P^{[d]}\) has the normalization of (1.1) at its displayed child scales and the additional outer mask \((a,d)=1\), and

\[
c_R(d)=\sum_{h\mid d}\mu(h)\,[1-\omega(Nh/R)].
\tag{2.4}
\]

The ideal d may have prime powers. There is no imposed \((h,b)=1\) and no imposed \((n,d)=1\). The outer masks \((a,h)=1\) and \((a,b)=1\) combine exactly to \((a,d)=1\). If Nd<=R, every divisor h has Nh<=R, so (2.4) is zero. On the physical support, Nd is at most a fixed multiple of \(D^{1/3}\), and

\[
|c_R(d)|\le\tau_K(d)\ll_\epsilon D^\epsilon.
\tag{2.5}
\]

The character \(\chi_d(k\mathfrak q^4)^3\) keeps its zero when d meets either the row or the auxiliary. Nothing in (2.3) fills in that zero.

## 3. The short bound keeps both Möbius cancellations

### Lemma 3.1

Under (1.2), for \(1\le R\le D^{1/3}\),

\[
\boxed{
\|\mathcal S_R\|_2^2\ll D^\epsilon
\left[
HD+QH^2D^{\beta-1/2}R^{5/2-\beta}
+Q^{2/3}H^{4/3}D^{2/3}R^{2\beta}
\right].}
\tag{3.1}
\]

The endpoints may be multiplied by fixed support constants without changing the estimate.

**Proof.** Insert the exact reunited support cutoff before separating the positive Ramanujan allocations. With the source dyadic labels

\[
EFG\asymp D,\qquad Nh\asymp Z,\qquad
G^2Z^3\ll D,\qquad Z\ll R,
\tag{3.2}
\]

the smooth short multiplier is omega((Z/R)(Nh/Z)). Its rescaled derivatives are uniformly bounded on every nonempty dyad; Z/R is bounded there. It therefore enters the same Mellin separation as the already inserted joint cutoff. All common-divisor length shifts preserve the rescaled ratios.

PR #921's exact full-cusp factorization and two-scalar lemma give the following three block monomials after extension to all rows and after the refined auxiliary reindexing:

\[
\begin{split}
&\frac{HD}{F}G^{2\beta-3}Z^{2\beta-2},\\
&\frac{QH^2D}{DF^2}G^{2\beta-1}Z^{2\beta+1},\\
&Q^{2/3}(H^2D)^{2/3}F^{-2}G^{2\beta-2}Z^{2\beta}.
\end{split}
\tag{3.3}
\]

In the second line, retaining the displayed D/D emphasizes its origin from \(H^2A/B\). This is the block statement before the full Z optimization; it is not obtained by applying the final norm estimate separately to each h.

For completeness, the two scalar savings have the following exact arithmetic basis. Expand \((e,g)=(e,h)=1\), write \(e=d_1d_2e'\), \(g=d_1g'\), \(h=d_2h'\), and retain \((g',h')=1\). Removing the latter by its shared-divisor identity leaves scalar exclusions containing \(f d_1d_2\) and the shared divisor ell. The norm costs are

\[
(Nd_1)^{-\beta-1/2}(Nd_2)^{-\beta-1/2}(N\ell)^{-2\beta}.
\tag{3.4}
\]

Their sums converge because beta>1/2. The residual e' may meet ell; an extra coprimality restriction there would change the exact identity. Both scalar characters keep their zeros. The all-cusp Gauss factor remains in the separate e and theta-column vectors. Repeated row primes, auxiliary overlaps, units and bad-prime powers are handled before the three monomials in (3.3), as in the frozen all-row source. In particular no new factor depending on h has been inserted into the theta-column vector.

The first line of (3.3) is at most HD. In the second, beta>1/2 and (3.2) give

\[
G^{2\beta-1}\ll
D^{\beta-1/2}Z^{-3\beta+3/2};
\]

its product with \(Z^{2\beta+1}\) is bounded by
\(D^{\beta-1/2}R^{5/2-\beta}\). The last line is bounded using
\(G^{2\beta-2}\ll1\) and \(Z\ll R\). F is at least a fixed positive constant on a nonempty block. Minkowski over the logarithmically many smooth dyads and the summable correction and cusp labels proves (3.1), after distributing epsilon losses. The original support and all nonempty bounded child scales below one are treated exactly as in the frozen block theorem. □

The powers \(R^{19/12}\) and \(R^{11/6}\) at beta=11/12 improve PR #923's \(R^{7/4}\) and \(R^2\). That improvement is precisely the second scalar Möbius saving.

## 4. The long bound has no auxiliary-conductor cost

### Lemma 4.1

For the same row range,

\[
\boxed{
\|\mathcal L_R\|_2^2\ll D^\epsilon
\left[H+H^{1/6}D^2R^{-3}+H^{2/3}D^{4/3}R^{-2}\right].}
\tag{4.1}
\]

This estimate uses the classical all-row sieve and the exact regrouping, without the angular scalar premise.

**Proof.** At a fixed d, group the squarefree physical product an in \(P^{[d]}\). Its row-independent coefficient includes the outer mask, the fixed tests, and \(\chi_{an}(\mathfrak q)^4\). The normalized squared coefficient mass is \(O(D^\epsilon)\), by ideal counting and the fixed-order divisor bound. Thus the refined all-row sieve gives, uniformly in d and the auxiliary,

\[
\|P^{[d]}_{D,D/(Nd)^3}(\cdot;\mathfrak q)\|_2^2
\ll D^\epsilon
\left[H+H^{1/6}\frac{D^2}{(Nd)^3}
+\frac{H^{2/3}D^{4/3}}{(Nd)^2}\right].
\tag{4.2}
\]

No sieve at the artificially enlarged row height \(HQ^4\) is used. The fixed auxiliary is absorbed into bounded column coefficients. The exterior row factor in (2.3) is a contraction after its zero has been retained.

Take the square root of (4.2), multiply by (2.5)/(Nd), and apply Minkowski. The base H term costs a finite harmonic sum. For the other two terms, ideal counting gives

\[
\sum_{Nd>R}(Nd)^{-5/2}\ll R^{-3/2},\qquad
\sum_{Nd>R}(Nd)^{-2}\ll R^{-1}.
\]

The harmless divisor weights and logarithms are absorbed into D^epsilon. Squaring proves (4.1). This accounts for all d, including powers, and every row. □

## 5. The uniform hybrid theorem and a larger diagonal-size range

### Theorem 5.1

Under the exact hypotheses above, for every \(1\le R\le D^{1/3}\),

\[
\boxed{\begin{split}
\sum_{k\asymp H}|P_{D,D}(k;\mathfrak q)|^2
\ll D^\epsilon\big[&HD
+QH^2D^{\beta-1/2}R^{5/2-\beta}
+Q^{2/3}H^{4/3}D^{2/3}R^{2\beta}\\
&+H+H^{1/6}D^2R^{-3}
+H^{2/3}D^{4/3}R^{-2}\big].
\end{split}}
\tag{5.1}
\]

This follows directly from (2.2), Lemmas 3.1–4.1, and the Hilbert-space triangle inequality. The literal polynomial is the only object on the left.

### Corollary 5.2

The energy in (5.1) is \(O(D^{2+\epsilon})\) whenever

\[
\boxed{1\le H\le
D^{\,18(5-2\beta)/(77-2\beta)}
Q^{-36/(77-2\beta)}.}
\tag{5.2}
\]

In particular, the source-conditional beta=11/12 gives

\[
\boxed{H\le D^{342/451}Q^{-216/451}.}
\tag{5.3}
\]

Counting, beta=1, gives \(H\le D^{18/25}Q^{-12/25}\).

**Proof.** Choose \(R=H^{1/18}\). Condition (5.2) is exactly the statement that the second term of (5.1) is at most D squared. It implies H<=D and hence the allowed R range. The fifth term is exactly D squared; the first, fourth and sixth terms are then smaller.

For the third term, write H=D^h and Q=D^q. The permitted triangle is

\[
h,q\ge0,\qquad
q+\frac{77-2\beta}{36}h\le\frac{5-2\beta}{2}.
\]

The third-term exponent is linear on this triangle. At its h=0 vertex it is \((7-2\beta)/3\le2\). At its q=0 vertex it is at most two because

\[
\frac{18(5-2\beta)}{77-2\beta}
\le\frac{12}{12+\beta},
\]

equivalently \(6\beta^2+53\beta-26\ge0\), true for beta>=1/2. The origin is also harmless. This proves the corollary. □

The exponent 342/451 is about 0.758315. It improves the literal all-row range 114/151 in PR #923; neither number is a zeta zero-free boundary.

## 6. Two explicit optimized regimes without the auxiliary

Set Q=1 and beta=11/12. For \(1\le H\le D^{111/253}\), take

\[
R=D^{8/29}H^{-7/29}.
\]

The third and fifth terms of (5.1) coincide. Every other term is no larger, and

\[
\boxed{
\sum_{k\asymp H}|P_{D,D}(k)|^2
\ll D^{34/29+\epsilon}H^{155/174},
\qquad1\le H\le D^{111/253}.}
\tag{6.1}
\]

For \(D^{111/253}\le H\le D^{19/22}\), take

\[
R=D^{19/55}H^{-2/5}.
\]

The second and fifth terms coincide, all remaining terms are smaller, and

\[
\boxed{
\sum_{k\asymp H}|P_{D,D}(k)|^2
\ll D^{53/55+\epsilon}H^{41/30},
\qquad D^{111/253}\le H\le D^{19/22}.}
\tag{6.2}
\]

For explicit verification, at the first cutoff the second term is
\(D^{99/116}H^{563/348}\), and its comparison with (6.1) is exactly
H<=D^(111/253). At the second cutoff the third term is
\(D^{13/10}H^{3/5}\), giving the reverse comparison. The other terms
have positive margins throughout the displayed intervals. Both cutoffs lie in [1,D^(1/3)], and the formulas agree at their junction.

At H equal to the square root of D, (6.2) gives

\[
\boxed{
R=D^{8/55},\qquad
\sum_{k\asymp D^{1/2}}|P_{D,D}(k)|^2
\ll D^{1087/660+\epsilon}.}
\tag{6.3}
\]

The exponent is about 1.646970, improving PR #923's 379/228 by exactly 16/1045. This is an upper-bound improvement for this specified Gauss polynomial, under the same angular premise, not a statement about an original inverse fourth moment.

## 7. A modular form for further local adapters

Suppose a fixed arithmetic multiplier has a proved local factorization preserving both scalar variables, all source masks, and the joint support. Suppose its block costs in the three monomials are \((1,J,K)\), with J,K>=1 and polynomial bounds. Then the identical proof gives (5.1) with Q replaced by J and Q^(2/3) replaced by K.

This requires the block factorization just stated. A final completed norm inequality alone does not justify saving the inverse h sum. The separately proved `MOVING_COLUMN_MASKS.md`, SHA-256 `068c7c993bdf09e17c2c06182ca8bc631e6ed34d8df6ccf29c46e1f2333ae0ee`, supplies precisely this factorization for the original exclusion q0 and auxiliary f, with

\[
J=Nf\,N(q_0/(q_0,f)),\qquad
K=(Nf)^{2/3}N(q_0/(q_0,f))^{1/3}.
\]

That new local proof is an explicit additional source of this moving-exclusion corollary; its original q0,f overlaps and all row zeros are retained.

The classical long bound remains unchanged whenever the fixed arithmetic multiplier and exclusions are bounded row-independent column factors in the literal product. If K<=J^(2/3), Corollary 5.2 remains valid with J in place of Q. The two physical axes may be interchanged, including their fixed tests, because the literal product coefficient is symmetric in a and n.

For general ordered scales \(1\ll m\le M\), with nonempty bounded child scales treated by fixed constants, the short and long estimates used in this modular form are

\[
\|\mathcal S_R\|_2^2\ll D^\epsilon
\left[Hm+JH^2mM^{\beta-3/2}R^{5/2-\beta}
+KH^{4/3}m^{4/3}M^{-2/3}R^{2\beta}\right],
\tag{7.1}
\]

\[
\|\mathcal L_R\|_2^2\ll D^\epsilon
\left[H+H^{1/6}mM R^{-3}+(HmM)^{2/3}R^{-2}\right].
\tag{7.2}
\]

The same proof uses \(G\le\sqrt M Z^{-3/2}\) in the second monomial, even when that upper bound is larger than m; a weaker valid bound is enough. One may use any R>=1 of polynomial size: if it exceeds the support-limited cube range, the long part is empty and the displayed upper bounds remain valid. Consequently (7.1) is available uniformly at the smaller rectangles of an arithmetic correction. Summing those corrections still requires its own convergence or cutoff argument; no automatic all-A2 transfer is asserted here.

A fixed smooth compactly supported two-variable test V(Na/m,Nn/M) is also permitted in (7.1)–(7.2) and hence in the balanced hybrid theorem. Choose one-variable cutoffs equal to one on its support, and Mellin-expand V in its two normalized coordinates. The resulting product tests have finite seminorms bounded by a fixed polynomial in the two imaginary Mellin variables. The Mellin transform of V has arbitrarily many integrable polynomial moments. The exact short/long decomposition is linear in the test, and its smooth h cutoff has uniformly rescaled derivatives, so Minkowski and absolute Mellin integration preserve both bounds. This proves the extension without inserting an arbitrary arithmetic coefficient.

Sharp row balls follow by applying the same R to all inward annuli and summing the positive powers H, H², H^(4/3), H^(1/6), H^(2/3). For a fixed scalar Schwartz row profile, keep the physical axes, auxiliary, exclusion and R fixed, and enlarge only the reference parameter on outward annuli. The resulting preliminary subpower and the largest row power H² are absorbed by a sufficiently large fixed decay order. Thus the hybrid estimates have the same row-profile scope as the inherited positive block estimates.

## 8. Boundary of the result

All row types, the exact inverse masks, and the single moving auxiliary are included. The first fourth-moment dual scale remains approximately D^(3-theta), far outside these useful short ranges. The retained signed auxiliary average and the centered subtraction at equality of reconstructed product columns are not bounded here. The spectral threshold and the known zero-free boundary are unchanged.
