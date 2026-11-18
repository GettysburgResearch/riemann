# Corpus agent's independent growing-multiplicity review

Reviewer: `/root/corpus`. Date:2026-11-17. Restored under an agent-specific filename after the originally chosen shared filename was reused by another reviewer. This preserves the independent proof scope; it does not incorporate the other reviewer's results.

Reviewed `proposals/independent_campaigns/growing_multiplicity_transition_round3.md`. Classification: independently checked with no issue found in the inspected proof. Scope: the elementary transition theorem **conditional on the stated previously derived exact polynomial-model error formula**. This review did not independently reconstruct that variational formula or transfer it to Dirichlet polynomials.

Write `L=N+m`, `C=L+1/2`, `x_j=j+1/2`, `r=(m-1/2)/C`. Since `N,m>=1`, `0<r<1`. The exact formula gives

\[
 1-E_{N,m}=\prod_{j=0}^{m-1}\frac{C-x_j}{C+x_j},\qquad
 -\log(1-E)=2\sum_j\operatorname{artanh}(x_j/C).
\]

The convergent artanh series, for `0<=u<=r<1`, gives

\[
 0\le\operatorname{artanh}u-u
 =\sum_{k\ge1}\frac{u^{2k+1}}{2k+1}
 \le\frac{u^3}{3(1-r^2)}.
\]

The exact midpoint sums are `sum x_j=m²/2` and `sum x_j³=m²(2m²-1)/8`. Therefore `A=m²/C <= -log(1-E) <= A+B` for exactly the proposed `B=m²(2m²-1)/(12C³(1-r²))`. Exponentiation proves the two bounds, and their difference is at most `e^-A B`, since `1-e^-B<=B`. No fixed-m assumption was used.

If `m²/N -> λ<infinity`, then `m=O(sqrt N)`, `C/N->1`, `r->0`, `A->λ`, and `B=O(m^4/N^3)=O(1/N)->0`. This includes λ=0 and proves the limit `1-e^-λ`. If `m²/N -> infinity`, split into `m<=N` and `m>N`: respectively `C<=3N` and `C<=3m` for all permitted integers. Thus `A>=m²/(3N)` or `A>=m/3`, both divergent in their respective regimes. The lower bound `E>=1-e^-A` proves saturation at one, including m comparable to or much larger than N, where B need not be small.

For the iff assertion put `y=m²/N`. If `y->0`, then `A/y->1`, `A->0`, and `B/A=(2m²-1)/(12C²(1-r²))->0`, so `E/y->1`. Conversely, if y fails to tend to zero, a subsequence has `y>=ε>0`. Either a bounded subsequence tends to a finite λ>0, on which `E/y -> (1-e^-λ)/λ<1`, or an unbounded subsequence tends to infinity, on which `E/y<=1/y->0`. Both contradict `E/y->1`. The full y sequence need not have a limit.

Finally `y-A=m²(m+1/2)/(NC)` exactly, while `0<=A-(1-e^-A)<=A²/2`. Combining those with `e^-A B<=B` proves the claimed absolute remainder. Constants, midpoint cube sum, all m/N regimes, and the subsequence necessity argument check. The exact threshold is `m=o(sqrt N)` within this polynomial-degree model. Multi-cluster extensions and any arithmetic scaling map remain separate work.
