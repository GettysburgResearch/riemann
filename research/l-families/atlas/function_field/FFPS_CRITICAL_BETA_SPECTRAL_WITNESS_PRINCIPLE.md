# The critical beta energy has a single weighted spectral witness principle

Status: **exact subpower-lattice \(\ell^2\)-to-\(\ell^\infty\) reduction,
exact common-period maximal-prefix theorem, and exact duplicate-\(67\)
witness isomorphism; the witness estimate and RH remain open**

Bounded replay:
[ffps_critical_beta_spectral_witness_principle.py](ffps_critical_beta_spectral_witness_principle.py).
Canonical summary:
[ffps_critical_beta_spectral_witness_principle.json](ffps_critical_beta_spectral_witness_principle.json).

Frozen source commit:
8192514ed68f50b8e2a9cff9e1bedab2478bb5c1.
The replay pins the theorem quartets for the critical Fourier lattice and
the duplicate-\(67\) scale-filter firewall.

## 0. Outcome

The critical beta energy does not merely reduce to \(X^{o(1)}\) Fourier
coordinates. At the exponent scale relevant to RH, its complete retained
\(\ell^2\) norm is equivalent to its **largest single weighted coordinate**.

Retain the predecessor notation

\[
 L_X=\log X+S+\delta,\qquad
 t_{k,X}={2\pi k\over L_X},\qquad
 K_*(X)=\left\lceil {L_Xe^{\sqrt{(\log2)(\log X)}}\over2\pi}\right\rceil.
\tag{0.1}
\]

Define

\[
 Z_X(k)=L_X^{-1/2}\widehat B(t_{k,X})D_X(t_{k,X}),
 \qquad 0<|k|\le K_*(X).
\tag{0.2}
\]

The retained energy is

\[
 \mathcal Q_*(X)=\sum_{0<|k|\le K_*(X)}|Z_X(k)|^2,
\tag{0.3}
\]

because \(\widehat B(0)=0\). There are only \(2K_*(X)=X^{o(1)}\)
coordinates, so

\[
\boxed{
 \max_{0<|k|\le K_*}|Z_X(k)|^2
 \le \mathcal Q_*(X)
 \le 2K_*(X)\max_{0<|k|\le K_*}|Z_X(k)|^2.}
\tag{0.4}
\]

The discarded lattice energy is unconditionally \(X^{o(1)}\). Therefore

\[
\boxed{
\mathrm{RH}\Longleftrightarrow
\max_{0<|k|\le K_*(X)}
{|\widehat B(t_{k,X})|^2\over L_X}
|D_X(t_{k,X})|^2=X^{o(1)}.}
\tag{0.5}
\]

Equivalently, if RH fails, then there are \(\eta>0\), an unbounded sequence
\(X_j\), and retained indices \(k_j\) for which

\[
 |Z_{X_j}(k_j)|^2\ge X_j^\eta.
\tag{0.6}
\]

Thus every hypothetical failure of RH has a single power-sized witness on
the exact subpower Fourier lattice.

The weighting is load-bearing. Equation (0.5) is **not** equivalent to an
unweighted maximum of \(|D_X(t_{k,X})|\): the fixed smoother can be tiny or
zero at noncentral frequencies. A uniform unweighted bound would be a
sufficient stronger theorem, not a consequence claimed here.

There is a second sharpening. Use the one common period \(L_X\) for every
prefix \(Y\le X\), and define

\[
\mathfrak W_F(X)=
\sup_{1\le Y\le X}
\max_{0<|k|\le K_*(X)}
{|\widehat B(t_{k,X})|^2\over L_X}|F_Y(t_{k,X})|^2.
\tag{0.7}
\]

Here \(F=D,M,A\) denotes respectively the beta, ordinary-Möbius, or
\(67\)-free Möbius prefix. Then

\[
\boxed{\mathrm{RH}\Longleftrightarrow
\mathfrak W_D(X)=X^{o(1)}.}
\tag{0.8}
\]

With \(a=67^{-1/2}\), the exact scale identities give

\[
\boxed{
(1-a)^2\mathfrak W_M
\le\mathfrak W_D
\le(1+a)^2\mathfrak W_M,}
\tag{0.9}
\]

and

\[
\boxed{
(1-a)^4\mathfrak W_A
\le\mathfrak W_D
\le(1+a)^4\mathfrak W_A.}
\tag{0.10}
\]

So the exceptional duplicate-\(67\) source creates no hidden small direction
even at the level of the worst individual weighted spectral witness.

## 1. Why one coordinate is equivalent to the retained energy

For any finite vector \(z=(z_1,\ldots,z_N)\),

\[
 \|z\|_\infty^2\le\|z\|_2^2\le N\|z\|_\infty^2.
\tag{1.1}
\]

At the critical cutoff,

\[
 N=2K_*(X)
 =\exp\!\left(\sqrt{(\log2)(\log X)}+O(\log\log X)\right)
 =X^{o(1)}.
\tag{1.2}
\]

Multiplication by \(N\) therefore does not change an \(X^{o(1)}\) target.
Equations (0.3)--(0.4) follow immediately.

The predecessor gives

\[
 \mathcal E(X)=\mathcal Q_*(X)+\mathcal R_*(X),
 \qquad 0\le\mathcal R_*(X)\le X^{o(1)},
\tag{1.3}
\]

and

\[
 \mathrm{RH}\Longleftrightarrow\mathcal E(X)=X^{o(1)}.
\tag{1.4}
\]

Equations (1.1)--(1.4) prove both directions of (0.5). The witness statement
(0.6) is simply the logical negation: failure of an \(X^{o(1)}\) maximum
means a fixed positive exponent occurs along an unbounded subsequence.
It is not a quantitative theorem tying that exponent to a particular zero.

This reduction changes the shape of the live target:

~~~text
continuum beta energy
  -> exact guarded Fourier lattice
  -> subpower many retained coordinates
  -> one worst weighted coordinate.
~~~

It does not estimate that coordinate.

## 2. The lattice weights form an exact probability law

Apply the same guarded Fourier-series Parseval identity to the kernel \(B\)
itself. Since its support length \(S\) is strictly smaller than \(L_X\),

\[
\boxed{
{1\over L_X}\sum_{k\in\mathbf Z}
|\widehat B(t_{k,X})|^2=\|B\|_2^2.}
\tag{2.1}
\]

The dyadic stair estimate, now without a Dirichlet polynomial, gives

\[
 {1\over L_X}\sum_{|k|>K_*(X)}
 |\widehat B(t_{k,X})|^2
 =O\!\left(X^{-1+o(1)}\right).
\tag{2.2}
\]

Indeed, the \(M\)-th frequency stair contributes

\[
 O\!\left(2^{-M^2+4M-2}\right),
\tag{2.3}
\]

and the critical starting stair has
\((\log T_*)^2/\log2=\log X\).

Put

\[
 w_{k,X}={|\widehat B(t_{k,X})|^2\over L_X},
 \qquad
 W_*(X)=\sum_{0<|k|\le K_*}w_{k,X}.
\tag{2.4}
\]

Then

\[
 W_*(X)=\|B\|_2^2+O(X^{-1+o(1)}).
\tag{2.5}
\]

For large \(X\), normalize

\[
 \pi_X(k)={w_{k,X}\over W_*(X)}.
\tag{2.6}
\]

This is an exact finite probability distribution and

\[
 \mathcal Q_*(X)
 =W_*(X)\,\mathbf E_{\pi_X}
 |D_X(t_{k,X})|^2.
\tag{2.7}
\]

Hence the retained RH criterion is also a weighted second-moment theorem for
one explicitly normalized random lattice frequency. This probability view
does not remove the small-weight caveat: rare coordinates with tiny
\(w_{k,X}\) may carry large raw values without affecting the energy.

## 3. One common lattice for every prefix

For \(1\le Y\le X\), the compact field

\[
 H_Y(u)=\sum_{n\le Y}{\beta(n)\over\sqrt n}B(u-\log n)
\tag{3.1}
\]

is supported in \([0,\log Y+S]\subset[0,\log X+S]\). It can therefore be
periodized on the same guarded interval of length \(L_X\). Exact Parseval
gives

\[
 \int_{\mathbf R}|H_Y(u)|^2du
 ={1\over L_X}\sum_{k\in\mathbf Z}
 |\widehat B(t_{k,X})|^2|D_Y(t_{k,X})|^2.
\tag{3.2}
\]

The critical tail proof is uniform over \(Y\le X\), because
\(|D_Y(t)|\le4\sqrt X\). Thus the discarded part of every row is
\(X^{o(1)}\).

If RH holds, every complete prefix energy is \(Y^{o(1)}\), and the standard
finite-small-prefix argument gives

\[
 \sup_{Y\le X}\int|H_Y|^2=X^{o(1)}.
\tag{3.3}
\]

Each retained coordinate is bounded by its row energy, proving the forward
direction of (0.8). Conversely, the row \(Y=X\), equation (0.4), and the
unconditional tail recover the endpoint energy criterion. This proves
(0.8).

The common period matters: all prefixes and all scale shifts now live in
the same finite weighted coordinate system before any supremum is taken.

## 4. The duplicate-\(67\) filter remains invertible witness by witness

At every common-lattice frequency set

\[
 \omega_k=67^{-1/2-it_{k,X}},
 \qquad |\omega_k|=a=67^{-1/2}.
\tag{4.1}
\]

The exact prefix identities are

\[
 D_Y(t_k)=M_Y(t_k)-\omega_kM_{Y/67}(t_k),
\tag{4.2}
\]

and

\[
 D_Y(t_k)=
 A_Y(t_k)-2\omega_kA_{Y/67}(t_k)
 +\omega_k^2A_{Y/67^2}(t_k).
\tag{4.3}
\]

Multiply by \(w_{k,X}^{1/2}\), then take the maximum over \(Y,k\).
The triangle inequality gives

\[
 \mathfrak W_D^{1/2}
 \le(1+a)\mathfrak W_M^{1/2}.
\tag{4.4}
\]

The terminating inverse

\[
 M_Y(t_k)=\sum_{j\ge0}\omega_k^jD_{Y/67^j}(t_k)
\tag{4.5}
\]

gives the reverse inequality

\[
 \mathfrak W_M^{1/2}
 \le(1-a)^{-1}\mathfrak W_D^{1/2}.
\tag{4.6}
\]

Squaring proves (0.9). The direct squared filter and

\[
 A_Y(t_k)=\sum_{j\ge0}(j+1)\omega_k^jD_{Y/67^j}(t_k)
\tag{4.7}
\]

give (0.10).

These are \(\ell^\infty\) witness bounds, not merely integrated \(L^2\)
bounds. The exceptional source factor is a boundedly invertible scale
coordinate change even after the continuum has been compressed to its worst
retained frequency.

## 5. What is genuinely left

The theorem identifies three increasingly sharp but equivalent beta targets:

\[
\boxed{
\begin{aligned}
\mathrm{RH}
&\Longleftrightarrow
\text{complete compact beta energy }=X^{o(1)}\\
&\Longleftrightarrow
\text{critical Fourier-lattice energy }=X^{o(1)}\\
&\Longleftrightarrow
\text{largest weighted retained coordinate }=X^{o(1)}.
\end{aligned}}
\tag{5.1}
\]

The maximal-prefix form is also invariant, up to fixed constants, under
replacement of beta by ordinary or \(67\)-free Möbius prefixes.

What remains open is a bound for

\[
\sup_{Y\le X}\max_{0<|k|\le K_*(X)}
{|\widehat B(t_{k,X})|\over\sqrt{L_X}}
\left|\sum_{n\le Y}{\mu(n)\over n^{1/2+it_{k,X}}}\right|.
\tag{5.2}
\]

Equation (5.2) is still RH-strength after the stated weighting. The packet
does not derive it from a large sieve, a zero-free region, orthogonality, or
the finite coordinate count.

## 6. Claim ledger

| statement | grade |
|---|---|
| finite \(\ell^2/\ell^\infty\) comparison | **PROVED EXACT** |
| single weighted witness criterion (0.5) | **PROVED FROM THE PINNED LATTICE THEOREM** |
| off-RH power-witness principle (0.6) | **PROVED AS THE LOGICAL NEGATION OF \(X^{o(1)}\)** |
| exact weight mass (2.1) | **PROVED BY GUARDED PARSEVAL** |
| retained weight asymptotic (2.5) | **PROVED FROM THE EXACT FOURIER STAIRS** |
| common-period prefix identity (3.2) | **PROVED EXACT** |
| maximal-prefix witness criterion (0.8) | **PROVED** |
| witness scale isomorphisms (0.9)--(0.10) | **PROVED EXACT** |
| unweighted raw maximum is RH-equivalent | **NOT CLAIMED; ONLY A STRONGER SUFFICIENT TARGET** |
| weighted witness estimate | **OPEN / RH-EQUIVALENT** |
| RH or GRH | **NOT PROVED** |

## 7. Bounded replay

~~~text
python -B research/l-families/atlas/function_field/ffps_critical_beta_spectral_witness_principle.py --check
python -B -O research/l-families/atlas/function_field/ffps_critical_beta_spectral_witness_principle.py --check
python -B -m unittest tests.test_ffps_critical_beta_spectral_witness_principle
python -B -O -m unittest tests.test_ffps_critical_beta_spectral_witness_principle
python -B -m ruff check research/l-families/atlas/function_field/ffps_critical_beta_spectral_witness_principle.py tests/test_ffps_critical_beta_spectral_witness_principle.py
python -B -m ruff format --check research/l-families/atlas/function_field/ffps_critical_beta_spectral_witness_principle.py tests/test_ffps_critical_beta_spectral_witness_principle.py
~~~

The replay uses a four-cell exact Gaussian DFT, finite rational Gaussian
scale sequences of depth nine at three frequencies, and elementary
\(\ell^2/\ell^\infty\) rows through dimension twelve. It enumerates no
prime, zero, curve, conductor, field, or \(L\)-function and performs no
floating-point computation.
