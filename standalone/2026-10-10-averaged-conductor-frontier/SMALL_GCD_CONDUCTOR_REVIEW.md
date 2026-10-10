# Independent review of the small-gcd conductor reduction

Reviewer: audit_formalization. Date: 2026-10-10.

**Verdict:** the stated reduction and its conditional averaged extraction pass this independent mathematical audit. No must-fix was found. This is a review of a new composition of stated estimates; the remaining signed arithmetic estimate is not proved.

## Binding and source scope

| Reviewed item | Bytes | SHA-256 |
|---|---:|---|
| SMALL_GCD_CONDUCTOR_REDUCTION.md | 16,386 | 9a371bd84f63b7fae2a3983c05829f2d69e2bbed918ab3eed119a2e7a11125a2 |

The reviewed note is in the same directory as this report. The following exact published sources were read directly from Git objects for this pass:

- PR #917, commit 6b4723042b3d250024eef45cb1924f88f28e902c: OSCILLATING_OVERLAPS.md, Sections 2–5, SHA-256 271f4f71bda533810ee49f6498f4ffbc42c3f0cb37c59151f9f703e715f58397.
- PR #914, commit 0cc0428fedbbfc340044c7451b3d392c1da9a103: CONDUCTOR_SECTORS.md, Sections 7–10, SHA-256 c160bbb1b1d7c6bcc5514d496ad41f15fd17ea3d36206b0d05cfa0d7d6503983.
- PR #917, the same commit: SCALE_AVERAGED_CRITERION.md, SHA-256 c6c543037312480fae6154f7a059248fe14658ecff6251aaecb80fe0fdbfd9c0. Its complete extraction and moving-cutoff proof are separately reviewed in SCALE_AVERAGED_SOURCE_AUDIT.md.

The cubic squarefree large sieve and the fixed universal nonvanishing Mellin test remain explicitly identified analytic inputs. This review does not newly prove those inputs, fully rebuild the imported analytic manuscript, or perform a Lean kernel build. No published file was changed.

## 1. Inherited oscillating-gcd estimate

The exact valuation decomposition \(u=\varepsilon v^3ab^2\) includes all nonzero element rows and permits \(v\) to share primes with the squarefree parts. The factor \({\bf1}_{(n,v)=1}\) is retained in the arbitrary coefficient before the squarefree cubic sieve. Finite bad-prime and unit factors are fixed or partitioned, not silently deleted.

On a row block \(P=V^3AB^2\), \(F=VAB\), and \(M=\max(A,B)\), the displayed monomial comparisons are correct:

\[
F\le P,\qquad (F/M)^3/P=A^2B/M^3\le1,
\qquad (F/M^{1/3})^3/P^2=A/(MV^3B)\le1.
\]

Thus the all-row cubic bracket is exactly \(H+H^{1/3}L+(HL)^{2/3}\). The \(H^{1/3}L\) term correctly retains the cube-copy rows.

For an exact gcd \(c\), the residual \(a,b,c\) are squarefree and pairwise coprime. Freezing \(a,b\) leaves the literal cubic phase \(\chi_c(u)^2\), with all exclusion masks, inside the sum to which the sieve applies. There are \(O(D^2/L^2)\) frozen pairs on \(Nc\asymp L\), and the varying coefficient has squared mass \(O(L)\). Minkowski gives norm powers
\[
\sqrt H L^{-3/2},\qquad H^{1/6}L^{-1},
\qquad H^{1/3}L^{-7/6}.
\]
All are negative, so the tail dyads sum geometrically. Squaring yields the three terms of the reviewed (1.2), with arbitrary positive losses reassigned as needed. The support and bounded-small-scale statements avoid extending an ideal-count estimate into an invalid nonempty range.

## 2. Exact signed composition

The split \(A^2=T_{\ge C}+R_{<C}\) is performed at the polynomial level. The sharp norm triangle comes before smoothing, so no selected signed covariance is incorrectly treated as nonnegative.

The smooth majorant is applied to the entire nonnegative square \(|R_{<C}|^2\), and its expansion has both small-gcd restrictions. The controlled sector estimates from #914 are estimates for positive sums of absolute contributions. Therefore restricting to this residual-by-residual tuple subset preserves them, without requiring a new sieve estimate for the restricted coefficients.

The union of \(g_1=1\) and the nonprincipal \(\mathcal E\le H\) sector contains every principal tuple. It must be counted once, as the note does. Its complementary sum has both side gcds below \(C\), \(g_1\ne1\), and \(Ng_1\sqrt{Ng_2}>H\). The selector is invariant under exchanging the two tuple sides, so the sum is real. The exact identity
\[
\sum_u\Phi(u/\sqrt H)|R_{<C}(u)|^2
=\mathcal U_C^\Phi(D,H)+O_\epsilon(HD^{2+\epsilon})
\]
then proves both the signed upper reduction and the lower bound
\(\mathcal U_C^\Phi\ge-K_\epsilon HD^{2+\epsilon}\). The proof does not rely on a pointwise absolute bound for the remaining signed sum. Constants are uniform in the moving \(C\), since the accounting only restricts a positive sum.

## 3. Cutoff, strictness, and extraction

Dividing the three tail terms by \(HD^2\) gives exactly
\[
C\ge D^{2/3},\qquad
C\ge DH^{-1/3},\qquad
C\ge(D^6/H)^{1/7}.
\]
For \(H=D^h\), \(1<h\le11/10\), their maximum is \(D^{(6-h)/7}\). The comparisons use \(h\le4/3\) and \(h\ge3/4\), respectively, both valid in the stated interval. The decrease from the previous cutoff exponent is \((4-3h)/28>0\).

The strictness pattern has two mutually coprime gcd ideals of scale \(D^\gamma\) and four separate singleton factors of scale \(D^{1-\gamma}\), where
\[
(6-h)/7<\gamma<(4-h)/4.
\]
Then \(Ng_1\asymp D^{4(1-\gamma)}\), \(Ng_2\asymp D^{2\gamma}\), and
\(\mathcal E\asymp D^{4-3\gamma}>D^h\). Both gcds fall into the old residual domain but outside the new one. Also \(Q\asymp D^{1-\gamma}\) on each side, so these scale patterns are outside a subpower singleton periphery. As stated in the note, this witnesses a strict domain reduction, not a lower bound on any signed summand or monotonicity of a signed sum under deletion. Feasible nonempty support remains required.

With the universal test and the new cutoff, the exact signed estimate can be integrated directly. The reviewed hypothesis explicitly uses the one-sided symbol \(\le\), and requires every positive loss and every sufficiently large scale. It implies
\[
\int_X^{2X}M_4(D,D^h)\frac{dD}{D}
\ll X^{h+2+e+\epsilon}.
\]
The pinned scale-averaged extraction then gives the strict half-plane
\[
\Re s>\frac12+\frac{5h}{24}+\frac e4.
\]
The premise is only an upper bound on the signed integral; it does not require an absolute integral or a pointwise upper bound. The already-proved lower bound follows from the full residual norm and controls any possible negative part at the harmless scale.

For fixed \(h=1+\theta\), the threshold is \(17/24+5\theta/24+e/4\). Reaching the strict threshold \(17/24\) uses \(e=0\) and hypotheses along fixed \(h\downarrow1\), with the large-scale limit taken separately for each \(h\). A fixed character gives its fixed-row twist family; a statement for every fixed finite-order character requires the arithmetic premise for every such character. No bound uniform in a growing conductor is needed for this forward extraction.

## 4. Remaining unproved input

The signed dyadic-scale estimate in reviewed (4.2) is still unproved. The note correctly leaves the small-gcd nearly coprime core and its singleton correlations unresolved. It makes no new unconditional fourth-moment, \(17/24\), or zero-free theorem claim. Its new content is the valid simultaneous restriction and the corresponding weaker sufficient arithmetic target.
