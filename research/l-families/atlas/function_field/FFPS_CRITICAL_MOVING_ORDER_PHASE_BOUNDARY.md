# The critical moving-order beta criterion has a logarithmic phase boundary

Status: **exact critical moving-order RH-equivalence region, exact variance
boundary constant for the certified comparison, and a sharp method
firewall; no beta-energy estimate, proof of RH, or GRH result**

Bounded replay:
[ffps_critical_moving_order_phase_boundary.py](ffps_critical_moving_order_phase_boundary.py).
Canonical summary:
[ffps_critical_moving_order_phase_boundary.json](ffps_critical_moving_order_phase_boundary.json).

Frozen sources:

| source quartet | commit |
|---|---|
| fixed-support beta mesoscopic microscope | **d30994d59d27adb6d9686a10854ae097092bf54b** |
| infinite dyadic box band-pass smoother | **b631040b76d696dbc69cadde7af240077f605c94** |

The producer pins all eight Git blobs. No live source module is imported.

## 0. Outcome

Let

\[
 L=\log X,\qquad
 T_*(X)=\exp\sqrt{(\log2)L},
\tag{0.1}
\]

where every logarithm is natural. Let \(P\) be the normalized tilted tent
from the frozen microscope and put

\[
 \sigma^2=\operatorname {Var}_P X
 ={2(e^2-3e+1)\over(e-1)^2}.
\tag{0.2}
\]

For fixed

\[
 0\le\alpha\le1,\qquad c>0,
\tag{0.3}
\]

define the moving order

\[
\boxed{
 m_{\alpha,c}(X)
 =\left\lceil
 {cT_*(X)^2\over(\log X)^\alpha}
 \right\rceil.}
\tag{0.4}
\]

Write \(\mathcal E_m(X)\) for the fixed-support beta-ladder energy at
order \(m\). The proved phase region is

\[
\boxed{
\begin{array}{ll}
0\le\alpha<1,\ c>0:
&\mathrm{RH}\Longleftrightarrow
\mathcal E_{m_{\alpha,c}(X)}(X)=X^{o(1)},\\[4pt]
\alpha=1,\ c\ge\sigma^2:
&\mathrm{RH}\Longleftrightarrow
\mathcal E_{m_{1,c}(X)}(X)=X^{o(1)}.
\end{array}}
\tag{0.5}
\]

In particular, the canonical member at the smallest certified fixed
leading constant in the declared ceiling family is

\[
\boxed{
 m_\dagger(X)
 =\left\lceil
 {\sigma^2
 \exp\!\left(2\sqrt{(\log2)(\log X)}\right)
 \over\log X}
 \right\rceil,}
\tag{0.6}
\]

and

\[
\boxed{
 \mathrm{RH}
 \Longleftrightarrow
 \mathcal E_{m_\dagger(X)}(X)=X^{o(1)}.}
\tag{0.7}
\]

This improves the first critical moving order by a full factor
\(\log X\). Its spectral scale is

\[
 {\sqrt{m_\dagger(X)}\over\sigma}
 ={T_*(X)\over\sqrt{\log X}}(1+o(1)),
\tag{0.8}
\]

strictly below the edge of the unresolved window. The infinite dyadic
smoother pays the remaining upper layer.

The constant \(\sigma^2\) is not guessed from a finite scout. It is the
quadratic decay coefficient of the exact characteristic function:

\[
 \log|\widehat P(u)|^2
 =-\sigma^2u^2+O(u^4).
\tag{0.9}
\]

For \(\alpha=1\), the ladder suppression at \(T_*\) is
\(\exp\{-(\sigma^2/c)L+o(L)\}\), while the fixed smoother supplies
\(\exp\{-L+o(L)\}\). Their equality occurs at \(c=\sigma^2\).

No failure of the criterion is asserted for \(\alpha=1,c<\sigma^2\), or
for smaller orders. The present positive comparison simply stops
certifying that region.

## 1. Exact small-argument law

The tilted tent factors as \(P=p_V*p_V\), with

\[
 p_V(v)={e^v\over e-1}\mathbf1_{[0,1]}(v).
\tag{1.1}
\]

Its exact Fourier modulus is

\[
\boxed{
 |\widehat P(u)|^2
 =
 \left[
 {1+\dfrac{4e}{(e-1)^2}\sin^2(u/2)\over1+u^2}
 \right]^2.}
\tag{1.2}
\]

Use

\[
 \sin^2(u/2)={u^2\over4}-{u^4\over48}+O(u^6),
\qquad
 \log(1+x)=x-{x^2\over2}+O(x^3).
\tag{1.3}
\]

Substitution in (1.2) gives

\[
 \log|\widehat P(u)|^2
 =
 2\left({e\over(e-1)^2}-1\right)u^2+O(u^4)
 =-\sigma^2u^2+O(u^4).
\tag{1.4}
\]

The remainder is uniform on one fixed neighborhood of zero.

The order-\(m\) fixed-support weight is

\[
 w_m(t)=t^2|\widehat P(t/m)|^{2m}.
\tag{1.5}
\]

For \(m=m_{\alpha,c}(X)\) and \(|t|\le T_*(X)\),

\[
 {t\over m}
 \ll {L^\alpha\over T_*(X)}
 \longrightarrow0.
\tag{1.6}
\]

Multiplying (1.4) by \(m\) gives, for \(t\ne0\), the uniform expansion

\[
\boxed{
 \log{w_m(t)\over t^2}
 =-{\sigma^2t^2\over m}
 +O\!\left({t^4\over m^3}\right).}
\tag{1.7}
\]

At \(t=0\), (1.7) is understood by continuous extension. If

\[
 y={cT_*^2\over L^\alpha},\qquad m=\lceil y\rceil,
\tag{1.7a}
\]

then \(m/y=1+O(1/y)\). At the endpoint \(t=T_*\), the ceiling changes
the quadratic exponent by

\[
 O\!\left({L^{2\alpha}\over T_*^2}\right)=o(1),
\tag{1.7b}
\]

while the quartic error below is
\(O(L^{3\alpha}/T_*^2)=o(1)\). The replay evaluates the ceiling from
the exact formula for \(\sigma^2\) at 90 and 130 decimal digits and
refuses unstable rows. This avoids silently replacing the declared
integer by the ceiling of a binary64 proxy. The proof itself uses the
literal integer order, with rounding absorbed uniformly.

At the largest allowed \(t\), the error is

\[
 {T_*^4\over m^3}
 \ll {L^{3\alpha}\over T_*^2}=o(1).
\tag{1.8}
\]

Thus the error in (1.7) is \(o(1)\) uniformly throughout the complete
critical window.

## 2. The frozen smoother envelope

Fix once and for all one infinite dyadic detector
\(B_{r,\infty}\), with fixed \(r\ge1,\varepsilon>0,\ell>0\). Its
probability-smoother factor is

\[
 \Phi_\ell(it)
 =\prod_{k\ge1}
 {1-e^{-i\ell t/2^k}\over i\ell t/2^k}.
\tag{2.1}
\]

For

\[
 M=\lfloor\log_2(\ell|t|)\rfloor\ge3,
\tag{2.2}
\]

the frozen exact stair theorem gives

\[
 |\Phi_\ell(it)|^2
 \le2^{-(M-1)(M-2)}.
\tag{2.3}
\]

All remaining fixed factors in \(\widehat B_{r,\infty}\) are bounded on
the real Fourier axis. Hence

\[
 |\widehat B_{r,\infty}(t)|^2
 \ll_{r,\varepsilon,\ell}
 2^{-(M-1)(M-2)}
\tag{2.4}
\]

whenever (2.2) holds. The band-pass difference also gives the global
bound

\[
 |\widehat B_{r,\infty}(t)|^2\ll t^2.
\tag{2.5}
\]

If

\[
 {T_*(X)\over L}\le|t|\le T_*(X),
\tag{2.6}
\]

then

\[
 \log|t|
 =\sqrt{(\log2)L}+O(\log L).
\tag{2.7}
\]

The floor in (2.2) costs only \(O(\log|t|)\), so (2.3) yields

\[
\boxed{
 |\widehat B_{r,\infty}(t)|^2
 \le\exp\{-L+o(L)\}}
\tag{2.8}
\]

uniformly on the upper band (2.6).

## 3. Low and high window comparison

Split the critical window into

\[
\mathcal I_{\rm low}
=\{|t|\le T_*/L\},
\qquad
\mathcal I_{\rm high}
=\{T_*/L\le|t|\le T_*\}.
\tag{3.1}
\]

### Low window

For \(t\in\mathcal I_{\rm low}\), (1.7) gives

\[
 {\sigma^2t^2\over m}
 \ll L^{\alpha-2}=o(1).
\tag{3.2}
\]

Therefore

\[
 w_m(t)\ge e^{-o(1)}t^2.
\tag{3.3}
\]

Combine this with (2.5):

\[
 |\widehat B_{r,\infty}(t)|^2
 \le X^{o(1)}w_m(t)
 \qquad(t\in\mathcal I_{\rm low}).
\tag{3.4}
\]

### High window, \(0\le\alpha<1\)

On the complete high window, the largest ladder suppression in (1.7) is

\[
 {\sigma^2T_*^2\over m}
 ={\sigma^2\over c}L^\alpha+o(1)=o(L).
\tag{3.5}
\]

Equations (2.8) and (3.5) give

\[
 |\widehat B_{r,\infty}(t)|^2
 \le e^{-L+o(L)}w_m(t)
 \le X^{o(1)}w_m(t).
\tag{3.6}
\]

### High window, \(\alpha=1\)

Now the endpoint ladder exponent is

\[
 {\sigma^2\over c}L+o(L).
\tag{3.7}
\]

If \(c>\sigma^2\), comparison with (2.8) has a fixed power saving. At
\(c=\sigma^2\), the two leading exponents cancel and leave an
\(\exp(o(L))=X^{o(1)}\) loss. Thus for every \(c\ge\sigma^2\),

\[
 |\widehat B_{r,\infty}(t)|^2
 \le X^{o(1)}w_m(t)
 \qquad(t\in\mathcal I_{\rm high}).
\tag{3.8}
\]

Together, (3.4), (3.6), and (3.8) prove

\[
\boxed{
 |\widehat B_{r,\infty}(t)|^2
 \le X^{o(1)}w_{m_{\alpha,c}(X)}(t)
 \quad(|t|\le T_*)}
\tag{3.9}
\]

throughout the region (0.5). The \(o(1)\) depends only on the fixed
detector parameters and the declared \((\alpha,c)\), never on the beta
coefficients.

## 4. Proof of the RH equivalences

Let

\[
 D_X(t)=\sum_{n\le X}{\beta(n)\over n^{1/2+it}}.
\tag{4.1}
\]

Multiply (3.9) by the positive measure

\[
 {1\over2\pi}|D_X(t)|^2dt
\tag{4.2}
\]

and integrate over \(|t|\le T_*\). This gives

\[
\begin{aligned}
 {1\over2\pi}\int_{|t|\le T_*}
 |\widehat B_{r,\infty}(t)|^2|D_X(t)|^2dt
 \le X^{o(1)}\mathcal E_{m_{\alpha,c}(X)}(X).
\end{aligned}
\tag{4.3}
\]

The frozen smoother theorem proves unconditionally

\[
 {1\over2\pi}\int_{|t|\ge T_*}
 |\widehat B_{r,\infty}(t)|^2|D_X(t)|^2dt
 =X^{o(1)}.
\tag{4.4}
\]

At the exact threshold, (4.4) is subpower; it is not asserted to be
bounded or decaying.

If the moving-order energy is \(X^{o(1)}\), equations (4.3)--(4.4) imply
that the full fixed-smoother energy is \(X^{o(1)}\). The latter is an
exact fixed-kernel RH criterion. This proves the reverse direction in
(0.5).

For the forward direction, every order in (0.4) satisfies

\[
 \log m_{\alpha,c}(X)
 =2\sqrt{(\log2)L}-\alpha\log L+O(1)
 =o(L).
\tag{4.5}
\]

Thus \(m_{\alpha,c}(X)=X^{o(1)}\). The frozen microscope proves

\[
 \mathrm{RH}\Longrightarrow
 \mathcal E_{m(X)}(X)=X^{o(1)}
\tag{4.6}
\]

for every subpower integer order. This completes (0.5)--(0.7).

## 5. The certified phase boundary

At \(\alpha=1\), evaluate the two decay exponents at \(t=T_*\):

\[
\begin{array}{c|c}
\text{factor}&-\log(\text{size})\\ \hline
\text{ladder characteristic factor}
&(\sigma^2/c)L+o(L)\\
\text{dyadic smoother stair}
&L+o(L).
\end{array}
\tag{5.1}
\]

Therefore:

- \(c>\sigma^2\): the comparison has a fixed power margin;
- \(c=\sigma^2\): it has exactly a subpower margin;
- \(0<c<\sigma^2\): these two one-sided envelopes permit a power loss.

The third row is a method firewall, not a counterexample. An actual
criterion below the boundary could still be true because of:

- sharper arithmetic cancellation in \(D_X\);
- exact zeros or smaller values of the fixed smoother;
- a different fixed comparison detector;
- a multiscale reconstruction rather than pointwise domination.

Accordingly,

\[
 c<\sigma^2
 \quad\not\Longrightarrow\quad
 \text{failure of RH equivalence}.
\tag{5.2}
\]

Only the present certified positive comparison stops there.

## 6. Why this is useful

The first moving-order criterion used

\[
 m\asymp T_*^2.
\tag{6.1}
\]

The new boundary theorem shows that only

\[
 m\asymp {T_*^2\over\log X}
\tag{6.2}
\]

is needed. This matters structurally:

1. the detector's physical signed core has width
   \[
   m^{-1/2}
   \asymp{\sqrt{\log X}\over T_*};
   \]
2. its spectral Gaussian scale stops at \(T_*/\sqrt{\log X}\);
3. the log-square smoother, not the growing detector, controls the final
   \(\sqrt{\log X}\) frequency ratio;
4. the exact variance of \(P\) becomes a genuine phase-boundary constant.

This suggests an inverse-design problem: change the probability atom to
minimize its variance while retaining compact support, carrier safety,
BV control, and a source-faithful Landau consumer. The present packet does
not solve that optimization.

## 7. Scope ledger

| statement | grade |
|---|---|
| exact characteristic modulus (1.2) | **IMPORTED AND REDERIVED EXACT** |
| uniform ladder expansion (1.7) | **PROVED** |
| upper-band smoother law (2.8) | **PROVED FROM THE FROZEN STAIR ENVELOPE** |
| low/high comparison (3.9) | **PROVED** |
| RH-equivalence region (0.5) | **PROVED** |
| boundary order (0.6)--(0.7) | **PROVED** |
| \(\sigma^2\) as the certified boundary constant | **PROVED FOR THIS COMPARISON** |
| failure below the boundary | **NOT PROVED** |
| beta-energy estimate | **NOT PROVED** |
| RH or GRH | **NOT PROVED** |

Equivalent criteria for RH are common. No external novelty or priority is
claimed without a dedicated literature comparison.

## 8. Bounded replay

The producer:

- checks all eight frozen Git blobs;
- evaluates four logarithmic horizons;
- compares the exact characteristic decay to
  \(\sigma^2L^\alpha/c\);
- records five phase rows around the certified boundary;
- checks the exact dyadic stair exponent.

Every row is logarithmic or elementary. It evaluates no beta sum, zeta
zero, numerical zeta value, prime, finite field, curve, random sample,
quadrature, or contour.

~~~text
python -B research/l-families/atlas/function_field/ffps_critical_moving_order_phase_boundary.py --check
python -O -B research/l-families/atlas/function_field/ffps_critical_moving_order_phase_boundary.py --check
python -B -m pytest -q tests/test_ffps_critical_moving_order_phase_boundary.py
python -O -B -m pytest -q tests/test_ffps_critical_moving_order_phase_boundary.py
python -m ruff check research/l-families/atlas/function_field/ffps_critical_moving_order_phase_boundary.py tests/test_ffps_critical_moving_order_phase_boundary.py
python -m ruff format --check research/l-families/atlas/function_field/ffps_critical_moving_order_phase_boundary.py tests/test_ffps_critical_moving_order_phase_boundary.py
~~~
