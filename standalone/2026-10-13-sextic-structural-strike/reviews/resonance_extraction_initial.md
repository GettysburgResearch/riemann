# Content review of the resonant subcritical short trace

**Reviewed file:**
`standalone/2026-10-13-sextic-structural-strike/RESONANT_SHORT_TRACE.md`.

**Frozen SHA-256:**
`f76370ff79f9ff5be3fd13dc440b4801e4bb8b2db7363a6c143d6cd3cbb41459`.

**Verdict:** the written proof establishes the claimed refutation of the
literal subcritical CT1 contract for every fixed \(k\ge2\) and
\(1/3<\sigma<1/2\), with the stated source specialization. I found no
load-bearing mathematical gap in the source composition or the all-order
extension. This is a content review at the exact file hash; it does not
integrate the result, verify RH, or certify the imported prime ideal theorem.

**Independence disclosure:** I authored the component
`SHORT_FACTOR_NONSMALLNESS.md`, SHA-256
`0af49f68a90bc19253e6543abd2e8d8af295a2bb133c5ebb59686e516655a935`.
I also contributed the original two-cluster degree-two calculation and
some explicit fourth-order constants during development. I therefore do
not present this report as an independent discovery or a fully independent
review of that lemma. I freshly reconstructed the root's complete source
specialization, all-order combinatorics, positivity of the whole trace,
prime summation, and extraction of a contradiction. A separate reviewer
without these contributions should also check the load-bearing chain.

## 1. Exact source material read

At the source commit `2f8b6a3898a722d0602a91dea73bac344a3bb7dd`, I read the
complete local copies of:

- `PRIME_SLOT_CANCELLATION.md`, especially P1–P2 and P8;
- `SHORT_POLYNOMIAL_COLLISION_TRANSPORT.md`, especially SC1–SC4;
- `COMPLEMENTARY_SHORT_TRACE_CONTRACT.md`, CT1–CT5;
- `WIDE_SUBCRITICAL_TUBE.md`, WT1–WT3.

I separately read PR #914's actual `CONDUCTOR_SECTORS.md`, Section 2. Its
source hash is
`c160bbb1b1d7c6bcc5514d496ad41f15fd17ea3d36206b0d05cfa0d7d6503983`.
The declared majorant is fixed, nonnegative, radial, smooth, and at least
one on the unit disk. That last condition licenses the unit-row lower bound;
it is not supplied merely by the word “Schwartz.” The actual P8 source
specification explicitly imports this majorant.

I opened the primary page
[Burgin, arXiv:2406.08565v2](https://arxiv.org/html/2406.08565v2), and checked
Theorem 1, Lemma 1, and the immediately following explanation. They supply
the stated classical prime ideal theorem. I did not reconstruct its proof.
The web retrieval reference was `turn54view0`; the immutable article URL
is the durable source identifier for this report.

## 2. Reconstructed source specialization

CT1 quantifies over every eligible incidence allocation and all independent
frequencies. The squarefree ideal \(Q\) obtained by multiplying the fixed
small prime ideals outside \(S\) can be assigned to the single cross-pair
\(\{1,k+1\}\). Every other allocation ideal is one, so pairwise
coprimality is automatic. The only nontrivial column masks are
\(c_1=c_{k+1}=Q\). The source eligibility condition therefore holds once
\(Y\ge NQ\); the possibly enormous threshold is harmless for the
asymptotic contradiction.

P8's exterior multiplier on this exact allocation is
\(\chi_Q(u)\overline{\chi_Q(u)}\), hence the indicator of \((u,Q)=1\).
The source Möbius factor is \(\mu_K(Q)^2=1\), and the allowed choice
\(\nu=1\) removes no required character. Thus this is a legal source
specialization, not an arbitrary positive selection of terms in a signed
trace. Equal norm conjugate prime ideals remain separately present in
\(Q\), as the ideal formulation requires.

SC2's short coefficients at row one are exactly
\(\mu_K(n)\mathbf1_{(n,SQ)=1}\); their constant coefficient is one.
All slots have the common cutoff \(Y\) even though two eventual physical
column scales are shorter. The source CT1 explicitly demands that common
cutoff before norm filtering, so the proof has not silently enlarged the
polynomials being tested.

## 3. The sign argument applies to the whole row trace

At paired frequencies, right local variables are the complex conjugates
of their matching left variables. After the fixed small-prime deletion,
the numerator of each nonzero local collision factor is

\[
 1-2x\Re\sum_{j=1}^k v_j\ge1-2kx\ge\frac12,
 \qquad x=q^{-\sigma},\quad |v_j|=1.
\]

The corresponding denominator is \(\prod_j|1-xv_j|^2>0\). If a prime
divides the arithmetic row, every slot value there is zero and both
numerator and denominator are exactly one. This retains the source's
literal nonunit convention rather than replacing a zero by a phase.

The finite short product is \(\prod_j|T_{Y,u}(\sigma+it_j)|^2\ge0\).
Multiplying by the source majorant and the exact cross-pair mask preserves
nonnegativity. Therefore the complete trace is a sum of nonnegative real
terms at every paired vector used in the proof. Taking only the retained
row \(u=1\) is a legitimate lower bound. The exterior unit sum cannot
cancel that row: every other unit row is also nonnegative at these
frequencies.

For fixed \(Y\), the row sum is well defined. All finite numerator factors
are bounded by \(1+2kx\), the denominators have a positive row-uniform
lower bound \(\prod_{p}(1-x)^{2k}\), and every short factor has the
uniform ideal-counting bound. These are finite \(Y\)-dependent constants.
The Schwartz lattice sum converges absolutely. The proof therefore does
not need an unproved exchange involving an infinite row trace.

## 4. All-order opposite-cluster calculation

Write \(n_+=\lceil k/2\rceil\), \(n_-=\lfloor k/2\rfloor\), and
\(d=n_+-n_-\in\{0,1\}\). On the exact sign vector, the total of the
\(2k\) local phases is \(2d\), whereas their square sum is \(2k\).
Consequently their pair sum is

\[
 \frac{(2d)^2-2k}{2}=2d^2-k=-\gamma,
 \qquad \gamma=k-2d^2.
\]

For even \(k\), \(\gamma=k\); for odd \(k\ge3\),
\(\gamma=k-2\ge1\). This explains both the all-order validity and why
the proof starts at \(k=2\). The value would have the wrong sign at
\(k=1\).

For a prime norm in \([Y^{a_k},Y]\), each local phase differs from its
assigned sign by at most \(E=(1+\pi)/(100k^2)\). Since all actual and
assigned phases have modulus one, an individual product differs by at
most \(2E\). Summing over \(\binom{2k}{2}\) pairs gives

\[
 2\binom{2k}{2}E
 <\frac{2k(2k-1)5}{100k^2}
 =\frac{2k-1}{10k}<\frac15<\frac\gamma2.
\]

The pair sum is real because its variables occur in conjugate pairs.
Thus the bound by \(-\gamma/2\) is a real upper bound, with no missing
real-part operation. This is a continuum phase estimate: it does not
follow from testing finitely many sixth roots or finitely many values of
\(k\).

## 5. Logarithm and prime-weight estimates

I reconstructed the local logarithm directly, with
\(S_1=\sum_i v_i\). The linear terms in
\(\log(1-xS_1)-\sum_i\log(1-xv_i)\) cancel. The quadratic term is

\[
 \frac{x^2}{2}\left(\sum_i v_i^2-S_1^2\right)
 =-x^2\sum_{i<j}v_iv_j.
\]

Because \(2kx\le1/2\), the sum of the terms of degree at least three
is \(O_k(x^3)\) uniformly over all phases. The actual logarithm is real:
the numerator is positive and denominator logs can be paired as twice
their real parts. Summation of the error is bounded independently of
\(Y\), precisely because \(3\sigma>1\). This is where the stated
lower limit \(\sigma>1/3\) enters.

The positive top-prime contribution is at least a constant times
\(Y^{1-2\sigma}/\log Y\). Indeed the prime ideal theorem supplies
\(\gg Y/\log Y\) prime ideals in \([Y/2,Y]\), which lies in
\([Y^{a_k},Y]\) eventually. Each has weight at least
\(Y^{-2\sigma}\). All deleted primes are fixed and eventually lie
below that interval. Prime ideal multiplicities at split rational primes
are correctly counted by the prime ideal theorem; no rational-prime
substitution has been made.

The potentially negative lower-prime contribution is bounded by the sum
over all ideals through \(Y^{a_k}\), namely
\(O(Y^{a_k(1-2\sigma)})\). Since \(a_k<1\) and \(1-2\sigma>0\)
are fixed, this is strictly smaller than the positive top contribution.
Both strict inequalities are necessary; no endpoint \(\sigma=1/2\)
claim follows from this estimate.

## 6. Short-factor non-smallness and contradiction

The source polynomial satisfies the exact hypotheses of the authored
non-smallness lemma, including at every changing row and every changing
exclusion. For the root's application only the unit row and fixed \(Q\)
are needed. Its product comprises \(k\) factors, of which \(n_+\) have
shift zero and \(n_-\) have shift \(\pi/\log Y\). Repeated factors are
permitted by the lemma. The anchor at real part four, explicit derivative
bound, complex divided-difference remainder, and factorial Lagrange bound
therefore yield one grid point with
\(|F_Y|\ge\exp[-C\log Y\log\log Y]\).

The collision lower bound holds uniformly throughout the interval that
contains this grid. Hence the two estimates hold at the same frequency.
The whole trace is at least the unit-row term
\(Q_{\rm coll,Y,1}|F_Y|^2\), whose logarithm is bounded below by

\[
 cY^{1-2\sigma}/\log Y-C\log Y\log\log Y.
\]

The second term is negligible at fixed \(\sigma<1/2\). This is the
claimed superpolynomial lower bound, not a lower bound obtained by
taking absolute values separately inside a signed row sum.

Both opposite frequency clusters are nonempty, and their separation is
\(\pi/\log Y\). Membership in the actual WT1 tube would imply
\(\pi\le2\kappa\), whereas WT1 restricts
\(0<\kappa<\arcsin(1/\sqrt{2k})<\pi/2\). Thus the selected vector
is outside every permitted tube. Its components tend to zero, so no
polynomial frequency weight compensates for the lower bound.

The successful point may depend on \(Y\); that is allowed because CT1
is uniform over all independent frequencies at each scale. The fixed
mask \(Q\) is chosen before \(Y\to\infty\), and \(Y\ge NQ\) is
enforced. The source range of \(h\) is covered; extending this particular
counterexample to fixed \(h>0\) uses only that \(H\ge1\) eventually.

## 7. A new finding during review: P13 also fails by another mechanism

The frozen file correctly says that its second-order collision-growth
argument does not refute the original critical-line P13. During this
review I found a separate, simpler first-order refutation of P13 itself.
It is written in
`/workspace/scratch/6ec6134c1535/pass3_euler_trace_resonance.md`, SHA-256
`c8931a93f3fc47805143ab4074ca4e315656a87e58abd5e0e7ba59c03079fb10`.

Use the same legal positive mask, take all left frequencies equal to
\(\pi/\log Y\), and all right frequencies their negatives. On the
unit row, the original Euler numerator has factors

\[
 1-2kq^{-1/2}\cos(\pi\log q/\log Y).
\]

Top-prime cosines are negative, giving logarithmic growth of order
\(\sqrt Y/\log Y\); smaller primes have a lower power cost. Every row
remains positive after the same type of fixed small-prime deletion.
Thus the original numerator trace also defeats every fixed power bound,
without any short-factor interpolation. This works even for \(k=1\).

This finding does not invalidate Theorem 1.1 in the reviewed file. It
does mean the eventual combined narrative should not leave P13 as an
unresolved promising fallback. It is a new companion proof, which needs
its own nonauthor review rather than being inferred from this report.

## 8. Nonblocking presentation corrections and omitted work

The frozen root file contains several incomplete inline math delimiters,
such as literal `(2k\)`, `(1/5\)`, and `(N=...\)`. They do not change
the mathematics, but should be repaired before publication and the final
hash rebound. A sentence making the fixed-\(Y\) absolute convergence of
the row trace explicit would also improve the proof's self-containment;
the argument is given in Section 3 of this review.

I verified file hashes and reconstructed the mathematics symbolically.
I did not execute a numerical moment experiment, a finite prime-growth
fit, or a proof-assistant build. No finite computation is offered as
evidence for the prime ideal theorem, the asymptotic contradiction, or
the full moment hypothesis. The primary-source inspection checks the
imported theorem's statement, not its proof.

The exact SC4 norm-filtered identity and the negligible common conjugate
component survive this refutation. A lower bound at the paired locus is
not a lower bound for the signed full-dimensional Mellin integral. The
report approves only the specified auxiliary-contract refutation at the
frozen source hash and with the disclosed developmental overlap.
