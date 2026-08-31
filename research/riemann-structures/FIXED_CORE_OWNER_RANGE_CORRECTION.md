# Full cores, not reduced cores, control the fixed-core owner ranges

Status: **exact source-range correction and corrected Hilbert-valued local
bound**. The short-range interval lemma in L-106124 remains valid under
its own hypotheses. Its application to the full physical owner ranges drops
the common-core factor \(g\). The canonical coefficient control below shows
that the resulting extra \(g^{-2}\) bound cannot hold uniformly on the
correct source range.

This does not identify the canonical coefficient projection with the complete
retained-gamma family. It is not a lower bound for that full family and does
not refute an RH statement. The correction concerns a named range import and
its uniform local coefficient estimate.

## 1. The exact discrepancy

The frozen parent L-102958 uses full cores
\[
 N=Pa^2,\quad M=Qb^2,\qquad P\le a,\quad Q\le b.
\]
From \(1/8\le N/M\le8\), it proves
\[
 Q\le2a,\qquad P\le2b.                                      \tag{1}
\]
After common-core extraction \(a=gc,\ b=gd\), these are
\[
 \boxed{Q\le2gc,\qquad P\le2gd.}                            \tag{2}
\]
The same common \(g^2\) cancels from \(N/M\), but it does not cancel
from the separate inequalities \(P\le gc,\ Q\le gd\).

L-106124 explicitly calls \(c,d\) the reduced cores. Its equation (1)
instead imports \(P\ll d,\ Q\ll c\), without a \(g\) factor.
Its abstract residue-cell argument is correct for those narrower intervals.
Equation (2), however, does not put the complete physical source in them.

This is a uniformity issue. Treating \(g\) as one fixed number can hide the
factor in an implied constant. L-106124's displayed \(g^{-2}\) claim
requires a constant uniform in \(g\) and would permit summation over the
common core. Its global conductor recombination is explicitly left open;
no completed global summation is attributed to that note here.

## 2. Corrected finite Hilbert-valued bound

Fix \(g,c,d\ge1\), odd distinct primes \(\ell,\rho\) with
\(\ell\mid c,\ \rho\mid d\), and
\((d,\ell)=(c,\rho)=1\). Let \(a_{P,Q}\) lie in a complex Hilbert
space and be supported on any subset of
\[
 1\le P\le2gd,\qquad 1\le Q\le2gc.
\]
All declared owner, coprimality or class masks may be retained by coefficient
deletion. Put
\[
 F_{h,k}=\sum_{P,Q}a_{P,Q}
 e_\ell(-hQd^2)e_\rho(kPc^2).
\]
Complete additive orthogonality and Cauchy within each residue cell give
\[
 \begin{aligned}
 \sum_{h=0}^{\ell-1}\sum_{k=0}^{\rho-1}\|F_{h,k}\|^2
 &\le
 \ell\rho
 \left\lceil\frac{2gc}{\ell}\right\rceil
 \left\lceil\frac{2gd}{\rho}\right\rceil
 \sum_{P,Q}\|a_{P,Q}\|^2\\
 &\le(\ell+2gc)(\rho+2gd)\sum_{P,Q}\|a_{P,Q}\|^2\\
 &\le9g^2cd\sum_{P,Q}\|a_{P,Q}\|^2 .
                                                               \tag{3}
 \end{aligned}
\]
The last inequality uses \(\ell\le c,\rho\le d,g\ge1\).
The same upper bound holds after deleting the zero phases. No cancellation,
prime-distribution theorem, or source identification is needed for (3).

For the physical coefficient shape
\[
 a_{P,Q}=\frac{\gamma_{P,Q}}{g^2cd\sqrt{PQ}},
\]
a bound on the actual Hilbert norms
\(\|\gamma_{P,Q}\|\le G\) yields the explicit statement
\[
 \boxed{
 g^2\ell\rho\sum_{h\ne0,k\ne0}\|F_{h,k}\|^2
 \le
 9G^2\frac{\ell\rho}{cd}
 \left(\sum_P\frac1P\right)\left(\sum_Q\frac1Q\right).
 }                                                            \tag{4}
\]
The sums range over the allowed semiprime products; larger containing sums
may be used. Their reciprocal sums are polylogarithmic. Thus the corrected
local conclusion at the same coefficient-norm scope is
\[
 Y^{o(1)}\,\frac{\ell\rho}{cd}\le Y^{o(1)},                       \tag{5}
\]
not \(Y^{o(1)}/g^2\). If additional source labels remain, their inherited
measure and coefficient norms must be supplied before applying (4).
This statement does not itself establish those complete-gamma inputs.

The loss of \(g^2\) in (3) is a range loss. It is unrelated to the
literal-versus-grouped Wick correction or the missing nonprincipal atomic
phase cardinality in R-106131.

## 3. An actual canonical source tests the lost saving

Use the frozen dense-owner coefficient packet without changing its primes,
histories, shares or kernel. For \(Y=U^6\), choose primes in the seven
disjoint proportional windows of that packet, all immediately above \(U\).
At each fixed \(g,\ell,\rho\asymp U\), set
\[
 c=\ell,\quad d=\rho,\quad P=pq,\quad Q=rs.
\]
The complete left and right owner lists have
\[
 m,n\asymp U^2/(\log U)^2.
\]
They satisfy \(P,Q\asymp U^2\), while \(c,d\asymp U\).
Every member is in the same physical shell
\(Y<N,M<11Y/10\), satisfies the true full-core owner bounds, and has
two positive Boolean histories per side with canonical share \(1/6\).
Its aggregated bilateral coefficient is exactly
\[
 a_{P,Q}(t)=\frac{e^{it\log(N/M)}}{9\sqrt{NM}}.                  \tag{6}
\]
Thus the numerator \(\gamma_{P,Q}(t)=e^{it\log(N/M)}/9\)
has uniformly bounded norm in the original
\(L^2(d\nu)\), \(d\nu=|\widehat\kappa(t)|^2dt/(2\pi)\).
The four literal history amplitudes are each one quarter of (6);
we do not replace their Wick diagonal by a newly grouped diagonal.

For this uniform coefficient test take the physical horizon appearing as
\(X\) in L-106124 to be \(X=16Y=16U^6\). The frozen source indices
already satisfy \(N,M<11Y/10\); no larger independent parameter is needed
for this finite coefficient family. Thus \(X^{o(1)}=U^{o(1)}\) here.
No such conversion is claimed for a different application with an
independently enlarged horizon.

The window constants give, uniformly,
\[
 \frac{P}{d}>\frac9{10}g,\qquad
 \frac{Q}{c}>\frac9{10}g.                                     \tag{7}
\]
Hence no constant independent of \(g\) puts this source in the reduced-core
ranges of L-106124.1. This support discrepancy requires no assumption about
a full native gamma decoder.

For the observed energy control, split the lists by their actual quadratic
classes \(\tau=\chi_\rho(P)\) and \(\sigma=\chi_\ell(Q)\).
Choose a nonempty class with at least \(mn/4\) pairs, which exists by
pigeonhole. This is a legitimate coefficient deletion in the local
Hilbert-valued estimate. Write \(S(t)=\sum a_{P,Q}(t)\) over this class and
\[
 E_{\sigma,\tau}
 =g^2\ell\rho\,c_\ell c_\rho\,\|S\|_{L^2(d\nu)}^2,\qquad
 c_q=\frac{q+1}{q-1}.
\]
The frozen dense proof gives \(\Gamma(v)>1\) for all the within-class
frequency differences, where \(\Gamma(v)=\int e^{itv}d\nu(t)\).
It follows, uniformly in every such fixed triple, that
\[
 \boxed{E_{\sigma,\tau}\gg(\log U)^{-8}.}                       \tag{8}
\]
Only the ordinary PNT in fixed proportional intervals and the frozen exact
kernel bound enter this cofinal assertion. No growing-modulus prime theorem
is used.

## 4. Direct Gauss comparison, with its constant retained

On this fixed actual class,
\[
 \sum_{h=1}^{\ell-1}\chi_\ell(h)e_\ell(-hQd^2)
\]
is one scalar independent of \(Q\), of modulus \(\sqrt\ell\).
The corresponding rho sum has modulus \(\sqrt\rho\). Thus the double
quadratic-character weighted sum of \(F_{h,k}\) equals a scalar of
modulus \(\sqrt{\ell\rho}\) times \(S\).
Hilbert-valued Cauchy gives
\[
 \sum_{h\ne0,k\ne0}\|F_{h,k}\|^2
 \ge
 \frac{\ell\rho}{(\ell-1)(\rho-1)}\|S\|^2.
\]
Consequently
\[
 \begin{aligned}
 g^2\ell\rho\sum_{h\ne0,k\ne0}\|F_{h,k}\|^2
 &\ge
 \frac{\ell\rho}{(\ell+1)(\rho+1)}E_{\sigma,\tau}\\
 &\ge\frac9{16}E_{\sigma,\tau}
 \gg(\log U)^{-8}.                                           \tag{9}
 \end{aligned}
\]
The last numerical bound is conservative for odd primes at least three.
It does not identify a coefficient-one principal term in an unnormalized
Gauss frame.

An extension of L-106124.5 with a uniform \(Y^{o(1)}/g^2\) bound to
these correct physical ranges would instead be
\(U^{-2+o(1)}\), contradicting (9). The finite Hilbert interval lemma
on its stated shorter ranges is not contradicted: (7) shows exactly why
that hypothesis fails.

The corrected estimate (5) and (9) differ only by subpower/logarithmic
factors at \(c=\ell,d=\rho\). Thus the removed common-core saving cannot
be recovered uniformly from the coefficient magnitude and local geometry
alone. A stronger statement about the complete native vector would require
its actual extra structure and a separate proof.

## 5. Bounded replay and exact sources

The producer authenticates the frozen dense artifact and checks all sixteen
physical pairs, all four quadratic classes, the sixty-four inherited
histories and the exact coefficient squares. It checks the full-core and
reduced-core range ratios separately. It also reconstructs elementary
residue-cell capacities on small integer rectangles and retains the exact
Gauss comparison factor as a rational number.

The finite replay does not enumerate million-sized phase families, search for
primes, approximate Fourier integrals, or certify a large-\(U\) asymptotic.
Primality, Boolean history provenance and the original kernel control remain
authenticated imports from the frozen dense packet. The analytic argument
(7)--(9), not the finite fixture alone, proves the cofinal failure of the
uniform extension.

The four new owned files are bound together by the producer. Actual execution
and independent review are recorded by the publishing agent; no test run is
inferred from writing this note.

| Source | Frozen commit | Git blob |
|---|---|---|
| L-102958, ratio-eight full-core bounds | ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc | 3b72653ea5f05405c587be165faf7ab2c52c3f2b |
| L-106124, fixed-core owner-phase energy | 86cac1d64364015ec2cc0f8fbb6fc75dc041c12b | 8a2ad27963cf61660bb151c20eae2910b1eb4255 |
| L-106120, bilateral tensor family | 86cac1d64364015ec2cc0f8fbb6fc75dc041c12b | a8d829dc10611adb7bfb4853902bdff0ab02a065 |
| T-106140, complete principal/Wick measure | 86cac1d64364015ec2cc0f8fbb6fc75dc041c12b | d5be8e376c88b63de0be19e0d9e8791624e99ae2 |
| Dense-owner proof | 1fea3c9ce079325d19f5b43c6daa59c76afff921 | c1eeffbc6aa814f860875d58205e97a4d945dc2c |
| Dense-owner artifact | 1fea3c9ce079325d19f5b43c6daa59c76afff921 | 1c289fb3c7d8e959b010267751834ebad6914ec5 |

The producer gives the complete source paths. None of those frozen files is
edited. This correction should accompany future use of L-106124's local
application; its global conductor recombination was already open.
