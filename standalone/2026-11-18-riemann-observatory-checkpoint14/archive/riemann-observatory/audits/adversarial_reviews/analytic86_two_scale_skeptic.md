# Independent audit of the two-scale deterministic-grid criterion

18 November 2026. The proposed modulus bound and the sharp **universal** tightness criterion hold. Fix \(0<C<\infty\), finite \(p>1\), \(a,b>1\), and deterministic finite real sequences \(A_n\ge1\), \(0<\epsilon_n\le1\), \(\epsilon_n\to0\). The criterion from the grid estimate below is \(A_n\epsilon_n^{b-1}\to0\). Necessity means that if this fails, there exist grids and processes with tight initial values satisfying the very same fixed \(C\) which are not tight. It says nothing necessary about an individual process or a prescribed grid sequence. The case \(C=0\) is trivial and not part of the sharpness claim. [Proposal](uniform85_two_scale_tightness_lemma.md)

## Standalone interpolation and modulus proof

Suppose all grid-node increments at row \(n\), with grid distance \(h\), satisfy
\[
 \|X_n(t_j)-X_n(t_i)\|_p^p\le C\min(h^a+\epsilon,A h^b).
\]
In this proof fix one row and set \(w=(\epsilon/A)^{1/b}\), \(\lambda=\epsilon/w\), \(a'=\min(a,p)\), \(b'=\min(b,p)\). These satisfy \(0<w\le1\) and \(a',b'>1\).

The node bound immediately implies the following envelope at nodes:
\[
 H(h)=h^{a'}+\epsilon\min\{1,(h/w)^{b'}\}.
\]
Here one uses the coarse bound at \(h\ge w\) and the fine bound at \(h\le w\). For a fractional increment of the polygonal interpolation lying in a cell of total length \(d\ge h\), the \(p\)-th power costs a factor \((h/d)^p\). The inequality \(h^p d^{a-p}\le h^{a'}\) follows by splitting on \(a\le p\) or \(a\ge p\), using \(h\le d\le1\). If \(d\ge w\), the coarse error term is \(\epsilon(h/d)^p\), bounded by \(\epsilon\) for \(h\ge w\) and by \(\epsilon(h/w)^{b'}\) for \(h<w\). If \(d\le w\), then
\[
 (h/d)^p A d^b=\epsilon(h/w)^p(d/w)^{b-p}
 \le \epsilon(h/w)^{b'}
\]
by splitting on \(b\ge p\) or \(b\le p\). This controls arbitrarily short pieces inside long cells. Across cells split into the two partial cells and the intervening full grid interval. The at-most-three-term inequality in \(L^p\), and monotonicity of \(H\) in its argument, give \(\|Z(t)-Z(s)\|_p^p\ll H(t-s)\) for the interpolation \(Z\). The proof uses no lower grid spacing. The cap \(p\) is necessary in general for fractional interpolation, since within a single nonconstant affine segment the \(p\)-th moment is exactly a nonzero constant times \(h^p\).

Write \(M_j\) for the maximum absolute adjacent increment at a dyadic mesh of size \(2^{-j}\). Summing \(p\)-th moments over its \(2^j\) edges bounds \(E M_j^p\ll 2^j H(2^{-j})\). For a pair at distance at most \(2^{-k}\), round its endpoints down to the level-\(k\) mesh and refine both endpoint approximants. The level-\(k\) gap spans at most two adjacent edges, and each finer-level correction spans at most one edge per endpoint. By continuity this yields \(\omega(Z,2^{-k})\le 2\sum_{j\ge k}M_j\). Minkowski and geometric summation give the first sum \(O(2^{-k(a'-1)/p})\). For the second term, let \(h_j=2^{-j}\). Its \(p\)-norm terms are, up to constants,
\[
 \lambda^{1/p}\begin{cases}
 (w/h_j)^{1/p},&h_j\ge w,\\
 (h_j/w)^{(b'-1)/p},&h_j\le w.
 \end{cases}
\]
Both sides sum geometrically toward the crossover. Starting above \(w\) costs \(O(\lambda^{1/p})\); starting below costs \(O(\lambda^{1/p}(2^{-k}/w)^{(b'-1)/p})\). Enclosing arbitrary \(\delta\) by a dyadic mesh within factor two proves
\[
 \|\omega(Z,\delta)\|_p\ll
 \delta^{(a'-1)/p}
  +\lambda^{1/p}\min\{1,(\delta/w)^{(b'-1)/p}\}.
\]
The constants are independent of the row, grid and parameters \(A,\epsilon\). If zero-error rows are allowed as a separate extension, omit the second term there instead of using an undefined ratio with \(w=0\). The direct coarse power suffices.

Since \(\lambda^b=A\epsilon^{b-1}\), the stated parameter condition implies \(\lim_{\delta\downarrow0}\limsup_n P(\omega(Z_n,\delta)>\eta)=0\) for each \(\eta>0\). Together with tight initial values, this is the usual tightness criterion on \(C([0,1])\). Each individual finite-grid interpolation is a random continuous function with tight law, so finite exceptional rows are harmless. A uniform modulus-in-probability is computable in principle from effective constants and parameter moduli. Identification of a path distribution, or a quantitative bounded-Lipschitz comparison to a specified limit, still needs finite-dimensional law information. The interpolation estimate does not supply it.

## Sharpness with the quantifiers fixed

Suppose the parameter condition fails. Along an infinite subsequence there is \(c>0\) such that \(\lambda\ge c\), hence \(w\le\epsilon/c\to0\). On those rows use \(m=\lfloor1/w\rfloor\) cells with common spacing \(d=1/m\ge w\). Choose \(J\) uniformly among \(1,\ldots,m-1\). Put \(X(J/m)=v>0\) and give all other nodes value zero. On remaining rows use the identically zero process. At every nonidentical pair the probability of a nonzero difference is at most \(2/(m-1)\). For \(w\le1/4\), the moment is thus at most \(4v^p w\le (4v^p/c)\epsilon\). Each pair distance is at least \(w\), so both given bounds are at least \(\epsilon\) before multiplication by \(C\). Choosing \(v^p\le Cc/4\) verifies the required inequality for the prescribed \(C>0\). Any exceptional initial rows can also be identically zero.

At every fixed collection of times the finite-dimensional laws tend to zero: a time lies in at most the two cells relevant to any possible neighboring spike node, and the probability of hitting it is \(O(1/m)\). This applies both to polygons and right-continuous steps. The polygonal sup norm is \(v\) and its modulus at distance \(d\to0\) is at least \(v\) along the chosen subsequence. It is not \(C\)-tight. The step paths also fail \(J_1\)-tightness along that subsequence. If there were a \(J_1\) weak limit, its marginal evaluations would be zero on some dense deterministic set of almost sure continuity times and at the terminal time, where evaluation is continuous in \(J_1\). Such a path is zero by right continuity. On the other hand the supremum norm of the path is continuous under \(J_1\) convergence, since each Skorokhod time change is onto. The limit would have supremum \(v\), a contradiction.

This is a row-by-row counterexample for every failing pair of parameter sequences. A non-growing \(A_n\) cannot produce that failure when \(\epsilon_n\to0\); unbounded \(A_n\) by itself does not imply it. Infinitely many sparse bad rows are enough because the subsequence prevents tightness. The counterexample does not claim necessity when one chooses a sparse prescribed grid, or when the random family has additional structure. If only the coarse bound \(C(h^a+\epsilon)\) is given, the same spike construction at pitch comparable to \(\epsilon\) defeats universal tightness for every strictly positive error sequence, however fast it decays.

## Direct exponents, step transfer and the RH application

For \(1<q\le\min(a,b)\), the ratio of the grid envelope to \(h^q\) is at most \(1+\epsilon w^{-q}\). For \(h\le w\), use \(A h^{b-q}\le A w^{b-q}\). Beyond \(w\), use \(h^{a-q}+\epsilon h^{-q}\). Testing \(h=1\) and \(h=w\) gives a matching bound up to an absolute factor. This proves the claimed equivalence for the direct scalar envelope. Bounded \(A\) uniformly gives \(h^b\), and \(q>b\) fails at arbitrarily small \(h\) in any positive-error row. If \(A\) is unbounded, \(a<b\) and \(a<q\le b\), evaluating at \(h=A^{-1/(b-a)}\) gives exact envelope \(h^a\) and contradicts a uniform \(h^q\) bound. This is a statement about the entire scalar envelope over all \(h\), not about the set of actually realized distances in one array. The grid exponent caps at \(p\) after linear interpolation.

For a right-continuous step with node values, its uniform distance from its interpolation is the maximum adjacent jump, with the supremum approached from the left of a cell's endpoint. This is at most the polygonal modulus at the deterministic maximum mesh. Under the interpolation-tightness criterion, mesh tending to zero suffices to make the two families uniformly close in probability, as does a direct bound forcing the maximum jump to zero. Their \(J_1\) distance is no larger. Without either extra control there need not be a continuous step limit, as the fixed two-node grid already shows. Finite-dimensional convergence of interpolants identifies their continuous path limit. When only step finite-dimensional convergence is given, first justify the transfer by one of these conditions. For deterministic time changes with a continuous limiting clock, use the polygonal modulus at the sup-norm clock discrepancy, then composition with the continuous limiting clock. The same estimate of discrepancies alone would not make a discontinuous limiting clock continuous.

In the RH shrinking-band application \(p=4,\ a=b=2,\ A=L^2,\ \epsilon=L^{-M}\) apart from the fixed comparison constant. Thus \(\lambda=L^{1-M/2}\) and universal tightness requires exactly \(M>2\) for these two supplied bounds alone. For a direct exponent the scalar-envelope test requires \(q(1+M/2)\le M\), giving \(2M/(M+2)\). When \(M\le2\) this number is at most one, so no \(q>1\) follows from the direct test. When arbitrary fixed log savings are available one obtains each fixed \(q=2-\eta\) by \(M\ge2(2-\eta)/\eta\). In the prime application the actual reciprocal clock and vanishing coordinate jumps provide the extra step transfer. The conclusion remains conditional on the two arithmetic increment estimates and the finite-dimensional comparison. [Prime process proof](uniform81_shrinking_band_process.md) · [Independent arithmetic and clock audit](analytic82_shrinking_process_skeptic.md)

**Disposition.** No mathematical blocker found. The necessary condition is for a guarantee over arbitrary deterministic grids and processes with positive fixed bound constant. The step-transfer and clock qualifications above are scope conditions, not new restrictions on the interpolated theorem. No canonical edit.
