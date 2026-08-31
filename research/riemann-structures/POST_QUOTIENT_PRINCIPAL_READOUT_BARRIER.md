# The principal readout amplifies an actual restricted source diagonal

Status: **exact restricted-source energy/diagonal theorem, not a complete
native moment counterexample**. RH remains unproved. This result uses the
canonical coefficient projection of the frozen FCM/NMO packets, with its
actual positive coefficients and four literal Boolean histories per pair.
It does not identify the projection with the complete retained-gamma source
or exclude cancellation by complementary contributions. Its energy tends
to zero absolutely even though its ratio to its own diagonal grows.

The [source-first adapter](SOURCE_FIRST_BOOLEAN_PRINCIPAL_ADAPTER.md) controls
the principal-weighted coefficient and Boolean-history diagonal through the
correctly ordered raw quotient and completion. The next operation is to sum
records inside the principal family before squaring. The theorem below
quantifies a loss at that operation on an actual source vector; it does not
use freely chosen coefficients or a state-dimension argument.

## 1. The exact projected family and its literal diagonal

Freeze one rectangle from
[FCM-1/3](FIXED_CONDUCTOR_POWER_RANK_BARRIER.md), with the source normalization
of [NMO (1.1)--(1.5)](NATIVE_RESTRICTED_MELLIN_OBSERVABILITY.md). Write

\[
 Y=U^6,\quad U^2/4<g<U^2/3,\quad
 N_i=25g^2P_i,\quad M_j=49g^2Q_j\in(Y,11Y/10),\quad L=mn.
\tag{1}
\]

All pairs are in the single fibre
\(\iota=(g,5,7,+1,+1)\), and the single raw residue cell \((1,4)\).
The one-sided cores are \(5g,7g\), each with exactly two Boolean histories
of coefficient \(+1\). The selected owner share is \(1/15\) on each side.
Use the principal character coordinate and the precise coefficient-level
projection declared in NMO; all additional source labels remain outside
this claim. In the conjugated-left convention of L-106120,

\[
 F(t)=\sum_{i,j}c_{ij}e^{it\log r_{ij}},\qquad
 c_{ij}=\frac4{225\sqrt{N_iM_j}}>0,\qquad r_{ij}=N_i/M_j.
\tag{2}
\]

Each arithmetic pair is the sum of **four** identical literal-history
amplitudes \(c_{ij}/4\). With \(c_q=(q+1)/(q-1)\), the actual T-106140
principal weight on this fixed fibre is

\[
 w=g^2\,5\,7\,c_5c_7=70g^2.
\tag{3}
\]

For the native Fourier convention, set

\[
 \Gamma(v)=\frac1{2\pi}\int_{\mathbb R}|\widehat\kappa(t)|^2e^{itv}\,dt,
 \qquad
 E=\frac w{2\pi}\int|\widehat\kappa(t)|^2|F(t)|^2\,dt,
 \qquad D_{\rm lit}=\frac{w\Gamma(0)}4\sum_{i,j}c_{ij}^2.
\tag{4}
\]

Thus \(E-D_{\rm lit}\) is the restricted principal literal Wick form.
The newly defined arithmetic-pair diagonal is \(D_{\rm pair}=4D_{\rm lit}\);
it is not the inherited literal diagonal. Source-dual coordinates give the
same expressions: \(\widetilde c=35gc\), principal coefficient \(2/35\),
and \((2/35)\widetilde c^2=wc^2\).

## 2. A positive native Gram kernel on the entire frequency-difference range

The exact primitive kernel computation in
[SCB section 3](SUBCRITICAL_OBSERVED_BOOLEAN_BLOCK.md) gives

\[
 \Gamma(0)=(384+128\sqrt2)\log2-288,\qquad
 \Gamma(0)\le384,\qquad
 |\Gamma(v)-\Gamma(0)|\le512|v|.
\tag{5}
\]

This uses the full variation, including endpoint jumps, of the actual
compactly supported real kernel. In particular \(\Gamma\) is real and even.
We need (5) on differences of two Mellin frequencies, not just on one
frequency. An elementary rational estimate suffices:

\[
 \sqrt2>\frac{707}{500},\qquad
 \log2=2\sum_{a\ge0}\frac{3^{-(2a+1)}}{2a+1}
 >\frac{842}{1215}>\frac{693}{1000},
\]

and hence

\[
 \Gamma(0)-\frac{512}{5}
 >\left(384+128\frac{707}{500}\right)\frac{693}{1000}
       -288-\frac{512}{5}>1.
\tag{6}
\]

Every \(r_{ij}\in(10/11,11/10)\). Therefore
\(|\log r_{ij}-\log r_{ab}|<2\log(11/10)<1/5\), and

\[
 \boxed{\Gamma(\log r_{ij}-\log r_{ab})>1}
\tag{7}
\]

for every pair of retained arithmetic atoms. This is an integrated Gram
estimate. It does not use a pointwise lower bound at \(t=0\), where the
native detector's Fourier transform vanishes.

## 3. Sharp order of diagonal-relative amplification

**PQR-1.** For the actual source vector (2),

\[
 \boxed{\frac{25}{2904}L\ \le\ \frac E{D_{\rm lit}}\ \le\ 4L.}
\tag{8}
\]

To prove the lower bound, expand the finite square in (4) and apply (7):
\(E\ge w(\sum c)^2\). The physical interval gives

\[
 c_{\min}=\frac8{495Y}<c_{ij}<\frac4{225Y}=c_{\max},
 \qquad c_{\min}/c_{\max}=10/11.
\]

Consequently

\[
 \frac E{D_{\rm lit}}
 \ge\frac{4}{384}\frac{L^2c_{\min}^2}{Lc_{\max}^2}
 =\frac{25}{2904}L.
\]

For the upper bound, the autocorrelation inequality
\(|\Gamma(v)|\le\Gamma(0)\) and Cauchy--Schwarz give
\(E\le w\Gamma(0)(\sum c)^2\le w\Gamma(0)L\sum c^2\).
This proves (8). The upper inequality alone is elementary; the lower
inequality uses the actual positive native coefficients, the native kernel
and a growing admissible source rectangle.

FCM-3/4 supply rectangles of sharp order in their stated globally
owner-disjoint window/core class:

\[
 L=\Theta\!\left(\frac{Y^{1/3}}{(\log Y)^2}\right),\qquad
 L\ge\frac{36}{10^8}\frac{Y^{1/3}}{(\log Y)^2}.
\tag{9}
\]

Thus the squared norm of the principal readout on these actual restricted
vectors, relative to their literal diagonal, has this same sharp order.
The amplification of the norm on these vectors has order
\(Y^{1/6}/\log Y\). In particular no subpower
\(E\le Y^{o(1)}D_{\rm lit}\) estimate can hold uniformly over these
canonical coefficient restrictions. The conclusion is restriction-stable
only in the sense of refuting an estimate required to cover every such
restriction; it is not a lower bound for a completed signed source sum.

## 4. Why this is compatible with the full target remaining open

On the rectangles in (9), (1)--(8) also give

\[
 E=\Theta\!\left(Y^{-2/3}(\log Y)^{-4}\right),\qquad
 D_{\rm lit}=\Theta\!\left(Y^{-1}(\log Y)^{-2}\right).
\tag{10}
\]

Indeed \(w=\Theta(Y^{2/3})\), \(c=\Theta(Y^{-1})\), and the Gram
kernel is bounded above and below on the whole selected grid. These are
absolutely small energies. Neither (8) nor (10) contradicts an absolute
subpower principal moment bound. Adding the omitted source may cancel the
selected field; positivity of its own squared norm does not prevent that.

The concrete remaining T-106140 operation is

\[
 D_{\rm PP}=\int\sum_{\iota,\omega}|y_{\iota,\omega}(t)|^2\,d\nu(t)
 \quad\longrightarrow\quad
 P_{\rm PP}=\int\sum_\iota\left|\sum_\omega
 y_{\iota,\omega}(t)\right|^2\,d\nu(t),
\tag{11}
\]

where \(y=\sqrt{w_\iota}\,z\),
\(d\nu=|\widehat\kappa(t)|^2dt/(2\pi)\), and the complete gamma labels
and their inherited measure must remain. A diagonal-preserving spectator
tag does not make its subsequent identification an orthogonal operation.
For general gamma depending on \(t\), (11) must retain its actual inner
products; the simple scalar \(\Gamma\) expansion used here is justified
only for the declared constant-coefficient projection.

The source-first adapter settles a coefficient/history norm question before
(11). This theorem rules out paying (11) solely by a subpower diagonal
operator norm uniformly on the exhibited restrictions. It does not decide
the actual full-gamma vector, the global off-atomic additive/Kummer
cancellation, or the transfer of the previously paid squared-activity
remainder into the amplified family norm.

## 5. Provenance and bounded replay

The producer embeds exact commit/path/Git-blob locks for the frozen FCM,
NMO, SCB kernel and T-106140 sources. It reads the two already certified
NMO panels, with 9 and 12 arithmetic pairs, and performs no prime search.
It independently checks their physical coefficient squares, four-history
diagonal, principal/source-dual conversion, physical windows, all rational
frequency-ratio differences, and exact rational constants in (6)--(8).
Irrational amplitudes remain symbolic positive square roots; no floating
quadrature, square root, logarithm or rational replacement is used.

The all-horizon statements use the frozen FCM proof and (5)--(8), not finite
numerical extrapolation. The replay binds this note, producer and tests by
SHA-256 and uses strict canonical JSON comparison, including numeric types.
The root-run validation record and independent exact-SHA review are kept
separately so the bound files remain immutable after replay.
