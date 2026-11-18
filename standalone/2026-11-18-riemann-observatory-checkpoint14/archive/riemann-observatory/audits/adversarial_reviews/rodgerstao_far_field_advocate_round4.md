# A signed far-field reconstruction for Rodgers–Tao's X4 term

Researcher: `li_advocate`, 2026-11-17. Primary source: **PAPER-S004**, Rodgers–Tao, arXiv:1801.05914v5, pp47–52, especially the X4 term on pp49–50. Status: independently derived repair candidate, sent for parent and semantic-skeptic challenge. No novelty claim, no certification of the entire proof, and no assertion that the main theorem is false.

## Why a replacement estimate is needed

The literal printed Lemma21(ii), p46, has a prefactor \(\log_+T\) multiplying the sum of inverse distances over all pairs. On the classical configuration \(x_j=\xi_j\), that positive sum itself has size at least \(cT\log^3T\), while the renormalized energy is zero. Consequently the extra prefactor cannot be bounded by \(O(T\log^3T)\) on that configuration. A separate source-scope review records this issue; it is not resolved by restricting to nearby pairs, which retain a harmonic logarithm.

The critical use on p50 bounds the signed far sum by \(o(\log T)\), then takes an absolute value of the near sum. The following uses the *constant leading term* of the signed far field instead. The constant disappears by pair antisymmetry. It requires only the macroscopic classical-location estimates and a weighted inverse-square bound, not the literal Lemma21(ii).

## Definitions and hypotheses

Write
\[
\Psi(y)=\frac y{4\pi}\log\frac y{4\pi}-\frac y{4\pi},\qquad
\xi(u)=\Psi^{-1}(u),\quad u\ge0,
\]
using the increasing inverse on \([4\pi e,\infty)\). For integer \(j>0\), put \(\xi_j=\xi(j)\), \(\xi_{-j}=-\xi_j\). Suppose \(x_j\) is increasing on \(\mathbb Z^*\), odd, and
\[
x_j=\xi_j+O(\log(2+|j|)).\tag{A}
\]
The constant in (A) is fixed as \(T\to\infty\); Rodgers–Tao Corollary10 gives precisely this property, uniformly in their specified time interval.

Let \(j\sim_T k\) mean \(0<|j-k|<(T^2+|j|+|k|)^{1/10}\), let
\(\psi_T(j)=(1+|j|/(T\log T))^{-100}\), and define the symmetric-principal-value far sum
\[
A_k=\sum_{i:i\not\sim_T k,\ i\ne k}'\frac1{x_k-x_i}.
\]
Assume the nonnegative weighted inverse-square sum satisfies
\[
S_2:=\sum_{j\ne k}\frac{\psi_T(j)\psi_T(k)}{(x_k-x_j)^2}
\le C M_T,\qquad M_T\ge T\log^3T.\tag{B}
\]
The source's valid renormalization estimate Lemma18 supplies this with \(M_T=T\log^3T+\widetilde E_T\), at the times where those quantities are finite.

We claim
\[
X_4:=\sum_{j\sim_T k}\frac{\psi_T(j)\psi_T(k)}{x_k-x_j}A_k=o(M_T).
\tag{C}
\]
All constants may depend on the constant in (A). The claim concerns a fixed configuration; no differentiation or interchange of time integration is involved.

## 1. The classical far field has a constant limit

Uniformly for \(T^{7/10}\le k\le T^{11/10}\), let \(R=\lfloor T^{1/5}\rfloor\). Then
\[
A_k^\xi=-\frac\pi8+O\left(\frac{\log^C T}{R}+\frac{R\log^C T}{k}\right).
\tag{1}
\]
The negative-index version follows by odd symmetry, changing the sign of the constant.

First replace the exact nearby relation by the symmetric integer cutoff \(0<|i-k|\le R\). Indeed, throughout this bulk range and for \(|i-k|\asymp T^{1/5}\),
\((T^2+|i|+|k|)^{1/10}=T^{1/5}+O(T^{-7/10})\).
The two cutoffs can therefore differ by at most a fixed number of integer indices. Classical spacing bounds make their total contribution \(O(\log T/R)\).

Put \(x=\xi(k)\). Pair positive and negative summation indices with the function
\[
p(u)=\frac1{x-\xi(u)}+\frac1{x+\xi(u)}=\frac{2x}{x^2-\xi(u)^2}.
\]
It is increasing separately on \([0,k)\) and \((k,\infty)\), because
\(p'(u)=\xi'(u)((x-\xi(u))^{-2}-(x+\xi(u))^{-2})>0\).
Its tail is integrable. Thus monotone sum–integral comparison outside \([k-R,k+R]\) has error bounded by endpoint values, namely \(O(\log k/R+1/x)\). The omitted negative partners are restored with \(g(u)=1/(x+\xi(u))\); their sum–integral error is \(O(1/x)\). Equivalently, the symmetric-cutoff discrete far sum differs from
\[
\operatorname{PV}\!\int_0^\infty p(u)du
-\operatorname{PV}\!\int_{k-R}^{k+R}\frac{du}{x-\xi(u)}
\tag{2}
\]
by \(O(\log k/R+1/x)\). Endpoint rounding changes only the same order of error.

The derivatives of the inverse satisfy
\(\xi'(u)=4\pi/\log(\xi(u)/(4\pi))\), and on \(|u-k|\le R\ll k\),
\[
\frac1{x-\xi(u)}=-\frac1{\xi'(k)(u-k)}+O(1/k).
\]
This follows either by differentiating once more or from the continuous version of source equation(45). The principal value of the odd first term over that symmetric interval is zero, leaving \(O(R/k)\). The principal values in the \(u\) and \(y=\xi(u)\) variables agree: the ratio of the two infinitesimal one-sided cutoff lengths tends to 1.

Changing variable to \(y\) in the first integral in (2) gives
\[
\operatorname{PV}\!\int_{4\pi e}^\infty
\left(\frac1{x-y}+\frac1{x+y}\right)
\frac{\log(y/(4\pi))}{4\pi}\,dy.
\]
Extending its lower endpoint to zero changes it by \(O(1/x)\); the density in the artificial bounded interval is just an integrable signed function, not a zero-count density assertion there. With \(y=xv\), the extended integral equals
\[
\frac1{2\pi}\operatorname{PV}\!\int_0^\infty
\frac{\log(x/(4\pi))+\log v}{1-v^2}\,dv=-\frac\pi8.
\]
Here \(\operatorname{PV}\int_0^\infty(1-v^2)^{-1}dv=0\). The second integral is an ordinary removable-singularity integral at 1; splitting at 1 and substituting \(v\mapsto1/v\) gives twice
\(\int_0^1\log v/(1-v^2)dv=-\sum_{n\ge0}(2n+1)^{-2}=-\pi^2/8\).
These observations prove (1), with room to spare in its logarithmic factors.

## 2. Moving the points by O(log j) does not change that constant

On the bulk range, every retained comparable positive index has \(|i-k|\ge R-O(1)\). By the classical spacing estimate, (A), and \(R\gg\log^2T\), the actual and classical separations are comparable. Their reciprocal difference is bounded by
\[
\frac{C\log(2+|i|+|k|)}{|\xi_i-\xi_k|^2}.
\]
Summing over comparable indices gives \(O(\log^3T/R)\). The remaining tails and opposite-sign indices give \(O(\log^CT/k)\) by the macroscopic spacing estimate. This comparison is absolutely summable, so it also justifies the principal-value transfer. Thus uniformly for \(T^{7/10}\le|k|\le T^{11/10}\),
\[
A_k=-\frac\pi8\operatorname{sgn}k+\delta_k,
\qquad |\delta_k|\le T^{-1/5}\log^C T.
\tag{3}
\]

A rough bound useful outside this bulk is
\[
|A_k|\le C\log^C(2+T+|k|).\tag{4}
\]
To see it, treat indices \(|i|\le C(|k|+T^{1/5})\) with the classical spacing comparison away from the excluded neighborhood; their reciprocal sum is at most logarithmic times a harmonic sum. For the remaining tail, pair \(i\) and \(-i\), obtaining \(2x_k/(x_k^2-x_i^2)\), which is absolutely summable. The lower cutoff \((T^2+2|k|)^{1/10}\) eventually exceeds every fixed power of \(\log(2+|k|)\), so (A) is harmless uniformly; bounded initial values can be absorbed in the constant. This proves (4) for sufficiently large \(T\).

## 3. Antisymmetry and weighted Cauchy–Schwarz

Use a **symmetric pair restriction** for good pairs: both indices satisfy \(T^{7/10}\le|j|,|k|\le T^{11/10}\). Nearby good indices have the same sign. The contribution of the constant term in (3) is exactly zero upon exchanging \(j,k\). Also
\[
Q_T:=\sum_{j\sim_T k}\psi_T(j)\psi_T(k)\ll T\log T\,T^{1/5}.
\tag{5}
\]
This follows by counting \(O((T^2+|k|)^{1/10})\) neighbors per index and using the polynomial decay of \(\psi_T\); for neighboring indices the weights are comparable. Consequently Cauchy–Schwarz and (B) bound the good-pair error by
\[
T^{-1/5}\log^CT\,(S_2Q_T)^{1/2}
\le T^{-1/10}\log^CT\,M_T=o(M_T).
\tag{6}
\]

For the remaining pairs, if one index has absolute value below \(T^{7/10}\), the other has absolute value at most \(2T^{7/10}\). The number of these nearby ordered pairs is \(O(T^{9/10})\). From (4), Cauchy–Schwarz, and (B), their contribution is at most
\[
\log^CT\,T^{9/20}M_T^{1/2}
\le T^{-1/20}\log^CT\,M_T=o(M_T).
\]
If one index exceeds \(T^{11/10}\), the other is at least half that large. The rapidly decaying weights make
\(\sum_{\mathrm{high\ nearby}}\psi_T(j)\psi_T(k)\log^{2C}(2+T+|k|)\)
smaller than a fixed negative power of \(T\): for example the squared weight decays as \((T\log T/|k|)^{200}\), whereas the number of neighbors grows only as \((T^2+|k|)^{1/10}\). Another weighted Cauchy–Schwarz application proves that this contribution is \(o(M_T)\). This treatment includes pairs crossing the bulk boundary, so no unjustified cancellation across a hard truncation is used. Together these estimates prove (C).

## Scope of the reconstruction

The argument repairs a specific *route for estimating X4* under (A)–(B). It is not a proof of every estimate in Proposition22 or of Theorem1, and does not make the printed global positive-sum Lemma21(ii) correct. The later p52 uses carry polynomial gains, so an extra fixed logarithm there may be absorbable; that still requires exact checking in a full repair. Source Lemma16's endpoint-distance bound is reviewed separately, with a valid nearest-endpoint replacement that retains its conclusion. Independent source comparisons and adjudication should be read before promoting any broader claim.
