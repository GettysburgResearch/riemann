# The critical beta energy is an exact subpower-rank Fourier lattice form

Status: **exact Fourier-series compression, unconditional critical lattice
tail, and subpower-rank positive Gram theorem; the retained estimate and RH
remain open**

Bounded replay:
[ffps_critical_beta_fourier_lattice_compression.py](ffps_critical_beta_fourier_lattice_compression.py).
Canonical summary:
[ffps_critical_beta_fourier_lattice_compression.json](ffps_critical_beta_fourier_lattice_compression.json).

This packet imports the fixed infinite-smoother beta field and its critical
tail theorem at frozen commit
b631040b76d696dbc69cadde7af240077f605c94, pinned by all four Git blob
IDs in the replay. It changes the geometry of the remaining target: the
continuum energy is exactly a Fourier series, and all but \(X^{o(1)}\)
Fourier modes are unconditionally harmless.

## 0. Outcome

Fix once and for all the parameters
\(\ell,\varepsilon>0\), \(r\ge1\), and a guard \(\delta>0\). Let

\[
 B=B_{r,\infty},\qquad
 S=4\log2+r\varepsilon+\ell,
\tag{0.1}
\]

and

\[
 H_X(u)=\sum_{n\le X}{\beta(n)\over\sqrt n}B(u-\log n),
 \qquad
 D_X(t)=\sum_{n\le X}\beta(n)n^{-1/2-it}.
\tag{0.2}
\]

Because \(B\) is causal and supported in \([0,S]\), \(H_X\) is supported in
\([0,\log X+S]\). Put

\[
 L_X=\log X+S+\delta,
 \qquad t_k={2\pi k\over L_X}.
\tag{0.3}
\]

Fourier-series Parseval on the guarded interval gives the exact identity

\[
 \boxed{
 \mathcal E(X)=\int_{\mathbf R}|H_X(u)|^2du
 ={1\over L_X}\sum_{k\in\mathbf Z}
 |\widehat B(t_k)|^2|D_X(t_k)|^2.}
\tag{0.4}
\]

No quadrature, sampling limit, or band-limiting approximation occurs in
(0.4).

More generally, for fixed \(\kappa>0\), define

\[
 T_\kappa(X)=e^{\kappa\sqrt{\log X}},
 \qquad
 K_\kappa(X)=\left\lceil{L_XT_\kappa(X)\over2\pi}\right\rceil.
\tag{0.5}
\]

The exact dyadic Fourier stairs imply

\[
 \boxed{
 {1\over L_X}\sum_{|k|>K_\kappa(X)}
 |\widehat B(t_k)|^2|D_X(t_k)|^2
 \le X^{1-\kappa^2/\log2+o(1)}.}
\tag{0.6}
\]

At

\[
 \kappa_*=\sqrt{\log2},
 \qquad
 T_*(X)=e^{\sqrt{(\log2)(\log X)}},
\tag{0.7}
\]

the discarded lattice energy is \(X^{o(1)}\), while

\[
 2K_*(X)+1
 =\exp\!\left(\sqrt{(\log2)(\log X)}+O(\log\log X)\right)
 =X^{o(1)}.
\tag{0.8}
\]

Therefore

\[
 \boxed{
 \mathrm{RH}\Longleftrightarrow
 {1\over L_X}\sum_{|k|\le K_*(X)}
 |\widehat B(t_k)|^2|D_X(t_k)|^2=X^{o(1)}.}
\tag{0.9}
\]

The remaining RH-equivalent object has only \(X^{o(1)}\) spectral
coordinates. Moreover \(\widehat B(0)=0\), so the central coordinate is
identically absent and at most \(2K_*(X)\) retained coordinates are nonzero.

## 1. Exact Fourier-series proof

Extend \(H_X|_{[0,L_X]}\) periodically with period \(L_X\). The fixed guard
\(\delta\) places a zero interval between adjacent copies, so the \(L^2\)
norm on one period equals the norm on the real line. Its Fourier coefficient
is

\[
 \begin{aligned}
 c_k
 &={1\over L_X}\int_0^{L_X}H_X(u)e^{-it_ku}\,du\\
 &={1\over L_X}\widehat B(t_k)
   \sum_{n\le X}{\beta(n)\over\sqrt n}e^{-it_k\log n}\\
 &={1\over L_X}\widehat B(t_k)D_X(t_k).
 \end{aligned}
\tag{1.1}
\]

Fourier-series Parseval says

\[
 \int_0^{L_X}|H_X(u)|^2du
 =L_X\sum_{k\in\mathbf Z}|c_k|^2,
\tag{1.2}
\]

which is (0.4). Compact smoothness makes every series absolutely safe at
the level needed here; ordinary \(L^2\) Parseval would already suffice.

The choice of guard is inessential. Every fixed positive \(\delta\) gives
an exact identity, a slightly different frequency lattice, and the same
asymptotic rank.

## 2. The lattice tail has the same critical constant

The predecessor proves, when
\(M=\lfloor\log_2(\ell|t|)\rfloor\ge3\),

\[
 |\Phi_\ell(it)|^2
 \le2^{-(M-1)(M-2)}.
\tag{2.1}
\]

The remaining fixed multipliers in \(\widehat B\) are bounded, and

\[
 |D_X(t)|\le4\sqrt X.
\tag{2.2}
\]

There are

\[
 O\!\left(1+{L_X2^M\over\ell}\right)
\tag{2.3}
\]

lattice points with
\(2^M/\ell\le|t_k|<2^{M+1}/\ell\). After the prefactor \(1/L_X\), equations
(2.1)--(2.3) bound this entire block by

\[
 O_{\ell,r,\varepsilon,\delta}
 \left(X\,2^{-M^2+4M-2}\right),
\tag{2.4}
\]

with a smaller guard term. Summing from
\(M_0=\log_2(\ell T)+O(1)\) gives

\[
 \log(\text{lattice tail})
 \le\log X-{(\log T)^2\over\log2}+O(\log T+\log\log X).
\tag{2.5}
\]

Substitution of (0.5) proves (0.6). Thus discretization costs no change in
the critical constant \(\sqrt{\log2}\).

## 3. A subpower-rank positive Gram

Expanding the finite sum in (0.9) gives

\[
 \mathcal Q_*(X)
 =\sum_{m,n\le X}{\beta(m)\beta(n)\over\sqrt{mn}}G_X(m,n),
\tag{3.1}
\]

where

\[
 G_X(m,n)
 ={1\over L_X}\sum_{|k|\le K_*(X)}
 |\widehat B(t_k)|^2e^{-it_k\log(m/n)}.
\tag{3.2}
\]

This is the Gram matrix of the \(2K_*+1\) weighted phase vectors

\[
 n\longmapsto
 L_X^{-1/2}\widehat B(t_k)n^{-it_k}.
\tag{3.3}
\]

Since \(\widehat B(0)=0\), the \(k=0\) vector vanishes. Hence

\[
 G_X\succeq0,
 \qquad
 \operatorname {rank}G_X\le2K_*(X)=X^{o(1)}.
\tag{3.4}
\]

Combining (0.4), (0.6), and (3.1) gives the unconditional additive
compression

\[
\boxed{
 \mathcal E(X)=\mathcal Q_*(X)+\mathcal R_*(X),
 \qquad 0\le\mathcal R_*(X)\le X^{o(1)},}
\tag{3.5}
\]

where \(\mathcal R_*\) is the discarded energy with an explicit stair bound.
Equation (3.5) does **not** bound \(\mathcal Q_*(X)\). Low rank alone
supplies no cancellation against the signed beta vector.

The remainder estimate is source-specific: it uses
\(|D_X(t)|\le4\sqrt X\). It is not an operator-norm approximation to the
full \(X\)-by-\(X\) compact-ratio Gram for arbitrary coefficient vectors.
Only the quadratic form evaluated on the complete beta vector is compressed
with the stated \(X^{o(1)}\) additive error.

This is nevertheless a new analytic interface: the complete compact-ratio
Möbius correlation can be studied through a nonuniform Fourier frame of
subpower dimension, without losing the source, the exceptional \(67\)
factor, positivity, or the exact RH threshold.

Increasing the fixed notch order changes the small-\(k\) weights and their
vanishing multiplicities. The coordinate \(t_0=0\) is the only one
**universally** forced to vanish for every \(X\) by the notch. Difference
and box factors can have other real zeros, and a special period \(L_X\) may
align some of them with nonzero lattice coordinates, but a higher fixed
notch order does not guarantee any further coordinate deletion or reduce
the general asymptotic rank bound below the same subpower scale.

## 4. What to attack next

The finite-rank form suggests several theorem-shaped attacks:

1. control all retained coordinates jointly rather than applying a maximal
   estimate to each \(D_X(t_k)\);
2. exploit the nearly arithmetic spacing \(2\pi/L_X\) with multiplicative
   short intervals in \(n\);
3. seek a dual vector or signed frame inequality which uses the complete
   beta source and the exact zero at \(k=0\);
4. compare the lattice at \(X\), \(X/67\), and \(X/67^2\) before taking a
   norm, preserving the duplicate-\(67\) scale relation.

The theorem does not assert any of these estimates. It rules out the need
to control a continuum of frequencies or a polynomial-rank spectral frame.

## 5. Claim ledger

| statement | grade |
|---|---|
| guarded Fourier-lattice identity (0.4) | **PROVED EXACT BY PARSEVAL** |
| lattice tail exponent (0.6) | **PROVED FROM THE EXACT STAIRS AND TRIVIAL BETA BOUND** |
| critical retained mode count \(X^{o(1)}\) | **PROVED** |
| critical lattice RH criterion (0.9) | **PROVED FROM THE PINNED ENERGY CRITERION** |
| finite-rank positive Gram representation | **PROVED EXACT** |
| additive subpower-rank compression (3.5) | **PROVED** |
| operator-norm compression for arbitrary source vectors | **NOT CLAIMED** |
| retained low-frequency estimate | **OPEN / RH-EQUIVALENT** |
| RH or GRH | **NOT PROVED** |

## 6. Bounded replay

~~~text
python -B research/l-families/atlas/function_field/ffps_critical_beta_fourier_lattice_compression.py --check
python -B -O research/l-families/atlas/function_field/ffps_critical_beta_fourier_lattice_compression.py --check
python -B -m unittest tests.test_ffps_critical_beta_fourier_lattice_compression
python -B -O -m unittest tests.test_ffps_critical_beta_fourier_lattice_compression
~~~

The replay checks Fourier-series normalization on three exact four-cell
Gaussian-integer examples, the exact dyadic lattice exponent
\(-M^2+4M-2\), the finite-rank count, frozen source blobs, and scope fences.
It does not discretize a zeta zero or numerically sample \(D_X\). It
enumerates no prime, conductor, curve, field, or \(L\)-function.
