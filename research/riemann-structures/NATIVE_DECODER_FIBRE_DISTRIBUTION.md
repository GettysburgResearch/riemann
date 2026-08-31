# A successful native decoder needs a correction on almost every selected rough fibre

Status: **immediate conditional corollary of the frozen complete-candidate
theorem**, not a new source identification or native moment estimate.
No producer, numerical experiment or additional test is needed for this
finite direct-sum argument.

The complete canonical candidate is large on a whole family of rough
conductor triples. If the intended native principal moment is subpower and
is compared with that candidate in the same principal Hilbert space, then a
correction confined to a sparse set of those triples cannot suffice.

## 1. Keep the original four-class blocks

Let \(U\) tend through sufficiently large dyadic integers, \(Y=U^6\).
Let \(\mathcal I_U\) be the triples
\(j=(g,\ell,\rho)\) from the last three of the seven prime windows in the
frozen dense-owner construction. Their number is
\[
 |\mathcal I_U|=\Theta\!\left(\frac{U^3}{(\log U)^3}\right).       \tag{1}
\]
For each \(j\), retain all four actual quadratic classes
\((\sigma,\tau)\). A block consists of the four complete principal
members, not a selected list of physical tuples or source histories.
Its norm is
\[
 \|W_j\|_{\mathcal H_j}^2
 =
 g^2\ell\rho\,c_\ell c_\rho
 \sum_{\sigma,\tau=\pm1}
 \int_{\mathbb R}|W_{g,\ell,\rho,\sigma,\tau}(t)|^2
 \frac{|\widehat\kappa(t)|^2}{2\pi}\,dt,
 \qquad c_q=\frac{q+1}{q-1}.                                  \tag{2}
\]
This is the original conductor weight and measure. Grouping four classes
into one block preserves the existing direct sum. It does not make a
physical coefficient projection orthogonal and does not move the family
square outside any native member.

Write \(W^B\) for the complete canonical arithmetic candidate with the
specific nonnegative ratio-eight mask in the frozen complete-fibre theorem.
Equations (6)--(7) and section 4 of that proof give a constant \(C>0\),
independent of \(U\) and of every selected triple, such that
\[
 \boxed{\|W^B_j\|_{\mathcal H_j}^2
              \ge\frac{C}{(\log U)^8}
       \qquad(j\in\mathcal I_U).}                             \tag{3}
\]
For clarity, the uniformity uses the same fixed positive observation
interval and kernel mass at every triple. The two owner counts are both
of order \(U^2/(\log U)^2\), their complete class-square count is at
least one quarter of \(m^2n^2\), the physical coefficients are bounded
below by a constant times \(U^{-6}\), and the weight is of order \(U^4\).
All constants are uniform in the seven fixed proportional windows.
No distribution result modulo the growing phase primes is used.

## 2. A conditional native comparison

Suppose that a proposed decoder supplies members in this same Hilbert
space and the identity
\[
 W_{\rm nat}=W^B+R.                                           \tag{4}
\]
This is a hypothesis about the readout, weights, measure, horizon and
complete members. It is not an identification proved here. In particular,
every native carrier or renewal term remains inside \(W_{\rm nat}\), and
\(R\) includes every leftover needed for the comparison.

Put \(P_{\rm nat}=\|W_{\rm nat}\|_{\mathcal H}^2\), using the uncentered
positive principal moment. Let
\[
 s_U=\frac{\sqrt C}{(\log U)^4},\qquad
 \mathcal E_U=
 \{j\in\mathcal I_U:
       \|W_{{\rm nat},j}\|_{\mathcal H_j}\ge s_U/2\}.
\]
Since the entire triple blocks are orthogonal coordinates of the already
defined direct sum,
\[
 \boxed{
 |\mathcal E_U|
 \le\frac{4(\log U)^8}{C}\,P_{\rm nat}.
 }                                                            \tag{5}
\]
If the intended bound \(P_{\rm nat}=U^{o(1)}\) holds, then
\(|\mathcal E_U|=U^{o(1)}\). This is negligible compared with (1).

For every \(j\in\mathcal I_U\setminus\mathcal E_U\), the reverse triangle
inequality, (3) and (4) give
\[
 \boxed{
 \|R_j\|_{\mathcal H_j}
 \ge \|W^B_j\|_{\mathcal H_j}
      -\|W_{{\rm nat},j}\|_{\mathcal H_j}
 \ge\frac{\sqrt C}{2(\log U)^4}.
 }                                                            \tag{6}
\]
Thus the required correction has at least this size on all but
\(U^{o(1)}\) of the \(\Theta(U^3/(\log U)^3)\) selected triples.

Summing (6) also recovers
\[
 \|R\|_{\mathcal H}^2
 \gg\frac{U^3}{(\log U)^{11}},
 \qquad
 \|R\|_{\mathcal H}
 \gg\frac{Y^{1/4}}{(\log Y)^{11/2}},                            \tag{7}
\]
under the same conditional native target. The extra information over the
global reverse-triangle bound is the distribution of this necessary
correction across the selected complete fibres.

## 3. What is ruled out, and what is not

Conditionally on (4) and the subpower native target, a repair supported on
only \(o(|\mathcal I_U|)\) of these triple blocks is impossible. More
generally, the correction cannot have norm smaller than the threshold in
(6) on most selected triples. A few exceptional owner products or a sparse
list of bad conductors do not account for this comparison.

This does not prove that the actual native moment is large, nor exhibit the
actual residual \(R\). It does not require every literal native atom to
cancel, and makes no pointwise-in-\(t\) cancellation claim. The hypothesis
concerns complete observed member functions in the original norm. A
different canonical candidate, different proved readout, or weaker signed
conclusion may have a different comparison problem.

The literal and grouped Wick diagonals are not used in (3)--(7). A paid
diagonal is not substituted for \(P_{\rm nat}\). No centered additive or
Kummer estimate, full retained-gamma decoder, or RH consequence follows
from this conditional counting argument.

## Exact sources

* [Complete Boolean fibre positivity obstruction](https://github.com/gfreund123/riemann/blob/4353858fbfedc3acacb568bf8357c39a16da093f/research/riemann-structures/COMPLETE_BOOLEAN_FIBRE_POSITIVITY_OBSTRUCTION.md):
  commit 4353858fbfedc3acacb568bf8357c39a16da093f,
  Git blob 21f7a6948568341acd8eed4c63175fce5be20c8a.
* [Dense-owner principal coefficient family](https://github.com/gfreund123/riemann/blob/1fea3c9ce079325d19f5b43c6daa59c76afff921/research/riemann-structures/DENSE_OWNER_PRINCIPAL_COEFFICIENT_FAMILY.md):
  commit 1fea3c9ce079325d19f5b43c6daa59c76afff921,
  Git blob c1eeffbc6aa814f860875d58205e97a4d945dc2c.
* [Original principal and Wick measure, T-106140](https://github.com/gfreund123/riemann/blob/86cac1d64364015ec2cc0f8fbb6fc75dc041c12b/claims/theorems/T-106140-wick-centered-additive-kummer-conjunction-frontier.md):
  commit 86cac1d64364015ec2cc0f8fbb6fc75dc041c12b,
  Git blob d5be8e376c88b63de0be19e0d9e8791624e99ae2.

The separate [observation-gap audit](NATIVE_DECODER_OBSERVATION_GAP.md)
states which source maps are currently supplied and which principal-norm
comparison is still missing. This corollary strengthens the test of that
comparison; it does not fill the missing arrow.
