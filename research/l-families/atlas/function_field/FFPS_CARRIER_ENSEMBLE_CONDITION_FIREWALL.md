# Positive carrier ensembles cannot beat their best information rung

Status: **exact direct-sum convex-ratio theorem, exact coherent
lowest-surviving-moment reduction, finite common-Hilbert PSD firewall, and
order-zero low-pass loophole; no source-specific beta cancellation, new
unconditional estimate, or proof of RH**

Bounded replay:
[ffps_carrier_ensemble_condition_firewall.py](ffps_carrier_ensemble_condition_firewall.py).
Canonical summary:
[ffps_carrier_ensemble_condition_firewall.json](ffps_carrier_ensemble_condition_firewall.json).

Frozen source: the higher-derivative carrier hierarchy at commit
**0123d1ecb097294fc132cf251aebeab9a6bda169**. The producer pins all
four source blobs and imports no live predecessor module.

## 0. Outcome

The frozen hierarchy gives one sharp support condition number for each
derivative rung. A natural moonshot is to mix many rungs, scales, or Sobolev
energies and hope that the ensemble is better conditioned than every
constituent. This packet determines exactly what positive ensemble geometry can
and cannot do.

Put

\[
 p_m=2m+1,
 \qquad
 C_m=(m!)^2(2m+1)\binom{2m}{m}^2,
 \qquad m\ge0.
\tag{0.1}
\]

Thus

\[
 C_0=1,\quad C_1=12,\quad C_2=720,\quad
 C_3=100800,\quad C_4=25401600.
\tag{0.2}
\]

For a sharp rung-\(m\) carrier of width \(S\) and translated-field hull
\(L=S+\log X\), the diagonal-to-reverse support condition is

\[
 \kappa_m=\left(\frac LS\right)^{2m+1}.
\tag{0.3}
\]

Three exact conclusions follow.

1. Every finite positive incoherent sum has condition equal to a convex average
   of its constituent \(\kappa_m\). It cannot beat the best constituent.
2. Every finite coherent sum is itself one effective derivative carrier. Its
   order is the first nonzero moment of the combined kernel, not necessarily
   one of the listed derivative orders. Cancellation can raise that order but
   cannot improve the universal support exponent.
3. Allowing \(m=0\) really does beat the cubic \(m=1\) condition. But it leaves
   the zero-mean bandpass class and becomes the ordinary low-pass beta-prefix
   criterion in disguise.

Accordingly, at a common support-to-hull ratio, \(m=1\) is optimal only among
positive zero-mean derivative rungs. Any actual improvement beyond its cubic
support condition must use source-specific arithmetic cancellation in the
translated beta field, not positive Sobolev assembly alone.

## 1. Incoherent direct sums

For finitely many channels \(j\), take the optimal rung-\(m_j\) carrier of
width \(S_j\), its detector \(K_j=D^{m_j}Q_{m_j,S_j}\), and

\[
 H_j=K_j*\mu_X,
 \qquad
 \mu_X=\sum_{n\le X}\frac{\beta(n)}{\sqrt n}\delta_{\log n},
 \qquad
 L_j=S_j+\log X.
\tag{1.1}
\]

Let \(\lambda_j\ge0\), not all zero, write
\(\mathcal J_+=\{j:\lambda_j>0\}\), and define

\[
 E_\oplus=\sum_j\lambda_j\|H_j\|_2^2,
 \qquad
 \Delta_\oplus=\sum_j\lambda_j\|K_j\|_2^2.
\tag{1.2}
\]

The sharp moment projection on each channel gives

\[
 E_\oplus\ge A_\oplus|B(X)|^2,
 \qquad
 A_\oplus=\sum_j\lambda_j\frac{C_{m_j}}{L_j^{p_{m_j}}},
\tag{1.3}
\]

while optimal self-energy gives

\[
 \Delta_\oplus
 =\sum_j\lambda_j\frac{C_{m_j}}{S_j^{p_{m_j}}}.
\tag{1.4}
\]

Set

\[
 w_j=\lambda_j\frac{C_{m_j}}{L_j^{p_{m_j}}},
 \qquad
 \kappa_j=\left(\frac{L_j}{S_j}\right)^{p_{m_j}}.
\tag{1.5}
\]

Then the exact identity is

\[
 \boxed{
 \frac{\Delta_\oplus}{A_\oplus}
 =\frac{\sum_jw_j\kappa_j}{\sum_jw_j}.}
\tag{1.6}
\]

Therefore

\[
 \boxed{
 \min_{j\in\mathcal J_+}\kappa_j
 \le\frac{\Delta_\oplus}{A_\oplus}
 \le\max_{j\in\mathcal J_+}\kappa_j.}
\tag{1.7}
\]

No choice of nonnegative weights creates a hidden ensemble saving. If all
channels use common \(S,L\), with \(L>S\), and \(m_j\ge1\), the best included
rung is the smallest one. If \(m=1\) is present, the minimum is exactly

\[
 \left(\frac LS\right)^3.
\tag{1.8}
\]

For nonoptimal admissible carriers, the diagonal in (1.4) only increases, so
(1.6) becomes a lower bound and the no-improvement conclusion remains.

A capped exact example makes the averaging visible. Take \(S=1,L=2\) and

\[
 (m_1,\lambda_1)=(1,1),
 \qquad
 (m_2,\lambda_2)=\left(2,\frac1{30}\right).
\tag{1.9}
\]

Then

\[
 \Delta_\oplus=12+\frac{720}{30}=36,
 \qquad
 A_\oplus=\frac{12}{2^3}+\frac1{30}\frac{720}{2^5}
 =\frac94,
\tag{1.10}
\]

so

\[
 \frac{\Delta_\oplus}{A_\oplus}=16.
\tag{1.11}
\]

It is the weighted average of \(8\) and \(32\), with reverse weights
\(3/2\) and \(3/4\).

## 2. Positive mixtures on one support hull

Suppose each \(Q_i\) is a real probability carrier,
\(Q_i\ge0\) and \(\int Q_i=1\), and

\[
 Q=\sum_i\theta_iQ_i,
 \qquad
 \theta_i\ge0,
 \qquad
 \sum_i\theta_i=1,
\tag{2.1}
\]

is supported in one interval of length \(W\), and its zero-extended
\(D^rQ\) lies in \(L^2\). The frozen variational theorem applies directly to
the mixture:

\[
 \boxed{
 \|D^rQ\|_2^2\ge\frac{C_r}{W^{2r+1}}.}
\tag{2.2}
\]

Equality holds only for the translated beta optimizer \(Q_{r,W}\) almost
everywhere. Hence convex mixtures, including multiscale mixtures, cannot beat
the one optimizer on the same total support hull.

Enlarging the hull can of course lower raw energy. That is support dilution,
not an ensemble gain: the comparison optimizer must be assigned the same
enlarged width.

## 3. Coherent mixing and the lowest surviving moment

Let \(K_1,\ldots,K_N\in L^2(\mathbb R)\) be real compact kernels supported in
one interval \(I\) of length \(W\), and let

\[
 K=\sum_jc_jK_j\ne0.
\tag{3.1}
\]

The coefficients may be signed. This includes combinations of derivative
rungs, but the correct invariant is not the smallest listed rung. Define

\[
 r=r(K)
 =\min\left\{q\ge0:\int t^qK(t)\,dt\ne0\right\},
\tag{3.2}
\]

and

\[
 b=\frac{(-1)^r}{r!}\int t^rK(t)\,dt.
\tag{3.3}
\]

A finite \(r\) exists because a nonzero compact \(L^2\) function cannot have
every polynomial moment zero.

For \(r\ge1\), form the \(r\)-fold primitive

\[
 Q_K(t)
 =\frac1{(r-1)!}\int_{-\infty}^t(t-u)^{r-1}K(u)\,du.
\tag{3.4}
\]

The vanished lower moments make its polynomial tail to the right of \(I\)
identically zero. Therefore

\[
 \operatorname{supp}Q_K\subseteq I,
 \qquad
 D^rQ_K=K,
 \qquad
 \int Q_K=b.
\tag{3.5}
\]

For \(r=0\), take \(Q_K=K\). After dividing by \(b\), the signed unit-mass
variational theorem gives

\[
 \boxed{
 \|K\|_2^2\ge |b|^2\frac{C_r}{W^{2r+1}}.}
\tag{3.6}
\]

Now let \(H=K*\mu_X\). It is supported in a hull of length
\(L=W+\log X\), its moments below \(r\) vanish, and

\[
 \int t^rH(t)\,dt=(-1)^rr!bB(X).
\tag{3.7}
\]

The same projection gives

\[
 \boxed{
 \|H\|_2^2
 \ge |b|^2\frac{C_r}{L^{2r+1}}|B(X)|^2.}
\tag{3.8}
\]

Consequently

\[
 \boxed{
 \frac{L^{2r+1}\|K\|_2^2}{|b|^2C_r}
 \ge\left(\frac LW\right)^{2r+1}.}
\tag{3.9}
\]

If lower moments cancel, \(r\) rises and the support exponent worsens whenever
\(L>W\). It need not jump to the next listed derivative rung; it is exactly the
first surviving moment of the complete combined kernel. With nonnegative
coefficients on probability-derived kernels at the lowest active rung, their
aggregate sensitivity cannot cancel.

## 4. Exact coherent examples

On \([0,1]\), the first two optimal detectors are

\[
 K_1(t)=6-12t,
 \qquad
 K_2(t)=60-360t+360t^2.
\tag{4.1}
\]

They are orthogonal, with squared norms \(12\) and \(720\). The coherent sum

\[
 K=K_1+\frac1{10}K_2
 =12-48t+36t^2
\tag{4.2}
\]

has

\[
 \int K=0,
 \qquad
 \int tK=-1,
 \qquad
 \|K\|_2^2=\frac{96}{5}>12.
\tag{4.3}
\]

At \(L=2\), its condition normalized to its surviving \(r=1\) sensitivity is

\[
 \frac{2^3(96/5)}{12}
 =\frac{64}{5}>8.
\tag{4.4}
\]

The higher rung did not improve the cubic constituent.

A signed cancellation can raise the rung exactly. Let

\[
 Q_A=6t(1-t),
 \qquad
 Q_B=12t^2(1-t).
\tag{4.5}
\]

Both are positive probability densities, but

\[
 D(Q_A-Q_B)
 =6-36t+36t^2
 =\frac1{10}K_2.
\tag{4.6}
\]

Its zeroth and first moments vanish, while

\[
 \int t^2K(t)\,dt=\frac15,
 \qquad
 r=2,
 \qquad
 b=\frac1{10}.
\tag{4.7}
\]

It exactly attains the rung-two lower bound:

\[
 \|K\|_2^2=\frac{36}{5}
 =\frac1{100}C_2.
\tag{4.8}
\]

The cancellation converts the row into a scaled copy of the higher optimizer;
it does not beat it.

## 5. Finite PSD forms: precise scope

A positive-semidefinite coefficient matrix is meaningful only after every
channel is placed in one declared Hilbert space. Suppose the real kernels
\(K_j\in L^2(\mathbb R)\) are compactly supported in one common interval
\(I\) of length \(W\), all channels use the same arithmetic measure
\(\mu_X\), and \(H_j=K_j*\mu_X\). They therefore live on the same coordinate
line and their translated fields share the hull length \(L=W+\log X\).
Let \(A\succeq0\) be a finite constant matrix and choose a declared factorization

\[
 A=R^{\mathsf T}R.
\tag{5.1}
\]

Then

\[
 E_A(X):=\int\mathbf H(t)^{\mathsf T}A\mathbf H(t)\,dt
 =\sum_k\left\|\sum_jR_{kj}H_j\right\|_2^2.
\tag{5.2}
\]

Each row has coherent kernel

\[
 G_k=\sum_jR_{kj}K_j.
\tag{5.3}
\]

Define the corresponding local quadratic energy

\[
 \Delta_A:=\int\mathbf K(t)^{\mathsf T}A\mathbf K(t)\,dt
 =\sum_k\|G_k\|_2^2.
\tag{5.4}
\]

Apply Section 3 to every nonzero row, with its own lowest surviving
\(r_k\) and sensitivity \(b_k\). On a common hull,

\[
 E_A(X)\ge |B(X)|^2
 \sum_k|b_k|^2\frac{C_{r_k}}{L^{2r_k+1}},
\tag{5.5}
\]

and

\[
 \Delta_A\ge
 \sum_k|b_k|^2\frac{C_{r_k}}{W^{2r_k+1}}.
\tag{5.6}
\]

The ratio of the rowwise sharp diagonal lower bound to the reverse coefficient
is again a convex average of \((L/W)^{2r_k+1}\).

For example, take

\[
 R=
 \begin{pmatrix}
 1&1/2\\
 0&1
 \end{pmatrix},
 \qquad
 A=R^{\mathsf T}R
 =
 \begin{pmatrix}
 1&1/2\\
 1/2&5/4
 \end{pmatrix}.
\tag{5.7}
\]

For \(K_1,K_2\) above, the output rows are
\(G_1=K_1+K_2/2\) and \(G_2=K_2\), with

\[
 \|G_1\|_2^2=192,
 \qquad
 \|G_2\|_2^2=720,
 \qquad
 \Delta_A=912.
\tag{5.8}
\]

At \(L=2\), their reverse coefficient is \(12/2^3+720/2^5=24\).
The actual ratio is \(38\), while the sharp rowwise lower ratio is

\[
 \frac{12+720}{24}=\frac{61}{2},
\tag{5.9}
\]

again between \(8\) and \(32\).

This theorem does not authorize an arbitrary phrase such as “PSD Sobolev
matrix” between objects living in different spaces. Cross terms require common
\(L^2\) realizations or declared bounded embeddings, sufficient
zero-extension regularity, dimensionally specified coefficients, and finite
sums unless convergence and moment interchange are proved. Fractional,
negative-order, nonlocal, indefinite, or undeclared cross-space forms are
outside the theorem.

## 6. The order-zero loophole

If order zero is admitted, the sharp carrier is simply

\[
 Q_{0,S}(t)=\frac1S\mathbf1_{[0,S]}(t).
\tag{6.1}
\]

It has

\[
 \|Q_{0,S}\|_2^2=\frac1S,
 \qquad
 \int(Q_{0,S}*\mu_X)=B(X),
\tag{6.2}
\]

and therefore

\[
 \|Q_{0,S}*\mu_X\|_2^2
 \ge\frac{|B(X)|^2}{L},
 \qquad
 \kappa_0=\frac LS.
\tag{6.3}
\]

For every schedule \(S_X\ge1\),

\[
 \boxed{
 \mathrm{RH}
 \quad\Longleftrightarrow\quad
 L_X\|Q_{0,S_X}*\mu_X\|_2^2=X^{o(1)}.}
\tag{6.4}
\]

The reverse implication is Cauchy plus the frozen beta-prefix equivalence to
RH. Under RH, let \(B^*(X)=\sup_{y\le X}|B(y)|=X^{o(1)}\). Almost everywhere,

\[
 |(Q_{0,S}*\mu_X)(t)|
 \le\frac{2B^*(X)}S.
\tag{6.5}
\]

Since the field is supported on a hull of length \(L\),

\[
 L\|Q_{0,S}*\mu_X\|_2^2
 \le4\left(\frac LS\right)^2B^*(X)^2
 =X^{o(1)},
\tag{6.6}
\]

because \(S\ge1\) gives \(L/S\le1+\log X\).

This is a real linear rather than cubic support condition. It does not unlock a
new proof: it is the low-pass prefix criterion in another norm. It has no
zero-mean notch, no carrier-removal derivative, and no new beta cancellation.
The honest conclusion is therefore:

\[
 \boxed{
 m=1\text{ is optimal at a common support-to-hull ratio among zero-mean
 derivative rungs, not among all positive carriers.}}
\tag{6.7}
\]

## 7. Where a genuine improvement could live

The actual beta-field energy is

\[
 \|K*\mu_X\|_2^2
 =\frac1{2\pi}\int_{\mathbb R}
 |\widehat K(\omega)|^2
 \left|
 \sum_{n\le X}\frac{\beta(n)}{\sqrt n}
 e^{-i\omega\log n}
 \right|^2d\omega.
\tag{7.1}
\]

The universal support and moment theorems see only the carrier weight and the
source prefix. They do not exploit signed cancellation inside the Dirichlet
polynomial. That arithmetic spectrum is the only loophole left inside a fixed
positive detector architecture.

Growing channel counts, \(X\)-adaptive coefficients, vanishing sensitivities,
or indefinite weights require their own explicit subpower normalization
controls. Otherwise dilution or source tuning can make an energy small while
destroying the reverse implication.

## 8. Scope and firewalls

| statement | grade |
|---|---|
| positive direct-sum convex-ratio identity | **PROVED EXACT** |
| positive direct sum beats its best constituent | **DISPROVED** |
| positive multiscale mixture beats the hull optimizer | **DISPROVED** |
| coherent lowest-surviving-moment factorization | **PROVED** |
| finite common-Hilbert PSD row reduction | **PROVED** |
| \(m=1\) optimal at common support ratio among zero-mean derivative rungs | **PROVED** |
| \(m=0\) low-pass loophole and RH equivalence | **PROVED** |
| source-specific cancellation from support geometry | **NOT PROVED** |
| growing adaptive or indefinite ensemble theorem | **NOT PROVED** |
| new unconditional beta estimate, RH, or GRH | **NOT PROVED** |

The coherent theorem assumes a common finite support hull. Translating or
rescaling kernels first is permitted, but the resulting total hull must be used.

The PSD theorem is finite-dimensional. No infinite-frame convergence or
operator-domain assertion is implicit.

No external novelty or priority is claimed.

## 9. Bounded replay

The producer:

- verifies the frozen higher-derivative quartet by full Git blob ID;
- checks \(C_m\) for \(0\le m\le4\), the exact direct-sum convex identity,
  and the min/max condition bound with rational arithmetic;
- constructs the first two optimal detector polynomials, checks coherent
  addition, exact moment cancellation, norms, sensitivities, and sharp lower
  bounds;
- verifies the displayed rational PSD factorization and row energies;
- records but does not numerically approximate the beta field;
- performs no beta sum, prime enumeration, zeta evaluation, random sampling,
  quadrature, or curve computation.

~~~text
python -B research/l-families/atlas/function_field/ffps_carrier_ensemble_condition_firewall.py --check
python -O -B research/l-families/atlas/function_field/ffps_carrier_ensemble_condition_firewall.py --check
python -B -m unittest tests.test_ffps_carrier_ensemble_condition_firewall
python -O -B -m unittest tests.test_ffps_carrier_ensemble_condition_firewall
python -m ruff check research/l-families/atlas/function_field/ffps_carrier_ensemble_condition_firewall.py tests/test_ffps_carrier_ensemble_condition_firewall.py
python -m ruff format --check research/l-families/atlas/function_field/ffps_carrier_ensemble_condition_firewall.py tests/test_ffps_carrier_ensemble_condition_firewall.py
~~~
