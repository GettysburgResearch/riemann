# Independent Fourier-compact balanced-trace review

2026-10-10 continuation; reviewer `/root/review_setup/kappa_proof_audit`.
Read-only review of frozen owner files; outputs and independent controls
were written only under `/tmp`.

Verdict: **scoped PASS** for F1–F8, the directed finite leading-prime face,
and its paid Schwartz replacement. The signed moving-conductor mean
OPEN-F9 remains open. No full-R2 lower bound or generalized moment bound
is inferred.

Frozen owner proof `FOURIER_COMPACT_BALANCED_TRACE.md` SHA256
`480cb96c363ddddf5d35306b0b25739c110b6f407e8101a43aaddae04605f120`;
checker `check_fourier_compact_trace.py` SHA256
`dddf8f7c12fe022e54e19d9994da6092fd7a3a7e9da1d1d67b6daf6f5c27c598`.
The imported A2 interface is directly hash-bound by that checker. The
underlying source `qrh11-12.tex` SHA256
`d9a8f15aa770cf883d0eabd2b775fad694ce20b44cba7928f5c0c9a6d8750d4d`
was separately read for the source conventions; the finite checker does
not independently prove Poisson summation or automorphic theta analysis.

## Analytic and source checks

* F1: the source character `e(z)=exp(4 pi i Im(z)/sqrt(3))` is trivial
  on O, and the measure `2/sqrt(3)` makes its lattice covolume one.
  Radial scaling gives the exact Poisson amplitude `H/sqrt(Nq)` and
  dual argument `H Nh/Nq`. Every local exponent is +1 or -1 on a
  distinct good prime, hence the character is primitive and the zero
  frequency is exactly absent. Four-column prime support is only a
  source subface; composite columns and the other critical faces remain.
* F2–F3: CRT's local additive coefficient is `(q/pi)^(-1)`, so its
  Gauss scaling is `chi_pi(q/pi)`. The conjugate Gauss identity retains
  `chi_pi(-1)`. Both factors appear in the balanced polynomial. Radial
  unit projection has the exact norm charge `(Np-1)/6 mod 6`, and
  retains all nonunit zeros. Charge-neutral complements conjugate the
  complete term because the surviving full character takes value one
  at -1.
* F4: the quotient of two fixed-conductor allocations is cubic exactly
  on their symmetric difference, and still has the nonunit mask at
  every remaining conductor prime. Complete-period means and covariance
  therefore have the stated values. This does not turn correlations
  between different conductors into cubic correlations or bound the
  signed linear trace.
* F6: the source Fourier phase has radial frequency `4 pi/sqrt(3)`.
  A radius-1/4 disk gives `2 J1((pi/sqrt(3))sqrt(x))/((pi/sqrt(3))sqrt(x))`.
  Squaring its normalized transform gives the disk-overlap constant
  `4 sqrt(3)/(2 pi^2 R^4)`. The alternating-series lower bound is valid
  on the full native ball and gives a strict majorant above one. Its
  spatial decay is integrable on the two-dimensional lattice.
* F7: the overlap derivative is at most `2R`, so the stated global
  Lipschitz constant and `90 delta` change are correct. The mollifier
  transform has distance from one at most `4 pi delta/sqrt(3)` on the
  unit ball, preserving the strict majorant. Odd Nq gives a positive
  rational gap from the next dual integer norm; the explicit gap guard
  preserves the whole support census. The lattice box bound `Nq/10`
  and at most six allocations give exactly
  `4H/sqrt(Nq) * (Nq/10) * 6 * 90 delta = 8640 delta sqrt(Nq)`.
  This pays replacement by a genuine nonnegative Schwartz source test.

## Two-mode replay and an independent CRT oracle

Native normal and optimized runs used the installed python-flint/FLINT
backend, precision 192, and wrote distinct outputs:

* `/tmp/review-fourier-compact-trace-normal.json`
* `/tmp/review-fourier-compact-trace-optimized.json`

They are byte-identical, SHA256
`fa2e817911ebaee9411f3b617149fa55ad98e9b7abc6e604dd6b3a1d6cc6aae8`.
All 70 conductors and 420 allocations are present; 58 allocations are
unit-neutral and 362 are killed. The exact support census has 90,930
active dual frequencies. The directed leading value is
`[3916.7665189976260644009926745000130837431873375545 +/- 2.52e-47]`.
The paid Schwartz error is
`[0.00015228517653103756358316921533289390529764635514408 +/- 3.58e-54]`.
Thus the specified prime face stays strictly positive after mollification.
The checker exercises both phase-omission controls and individual
positive/negative conductor terms.

The separately written `/tmp/review_fourier_trace_crt_oracle.py`, SHA256
`97a3884b024cfd7ddb5e0b6f70a1750af0d3a56792e77dd87ebc9838b3f9a564`,
constructs the four residue fields over 7 and 13 from quadratic roots
and discrete logs. It reconstructs unique primary generators without
using the owner's seeds or Euler-symbol lookup. For their actual
conductor q=91 it enumerates all 8,281 residue classes directly.
There are 5,184 unit classes and four neutral allocations. Their exact
first means are zero, their exact cubic covariance matrix is
`5184 I_4`, and every direct complete Gauss sum overlaps the owner's
source-normalized CRT product with absolute difference below 1e-45.
This independently authenticates the CRT orientation, additive phase,
local minus sign, and complete-period mask/orthogonality conventions.

Oracle normal and optimized outputs are byte-identical, SHA256
`1289000dbfb4867215f897dd6d2ae074cd1b4c322c9f12ddc661fb680f82165c`:

* `/tmp/review-fourier-trace-crt-oracle-normal.json`
* `/tmp/review-fourier-trace-crt-oracle-optimized.json`

The oracle does not duplicate the complete 70-conductor finite trace.
The two-mode owner replay does that. Neither finite calculation proves
an asymptotic signed trace estimate or supplies cancellation from the
remaining critical configurations.
