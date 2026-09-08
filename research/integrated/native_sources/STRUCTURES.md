# Full-factor spectral classification at every rank

[Guide](README.md) · [Proof library](SOURCE_INDEX.md) · [Earlier family results](../../../RESULTS.md#structures)

**Status:** reviewed component selection in an integration candidate. This is local rational spectral algebra, not a global automorphy or compatible-family theorem. The former branch-only source is now retained physically with its complete proof and original evidence.

## Current theorem and normalization

Let $r\ge1$ be an integer, $q>0$ rational, and $A,B,C$ rational raw traces. Fix the **positive** square root of $q$, and put $x=A/\sqrt q$, $y=B/\sqrt q$, $z=C/\sqrt q$. Define Dickson polynomials by

$$D_0(z)=2,\quad D_1(z)=z,\quad D_{n+1}(z)=zD_n(z)-D_{n-1}(z).$$

For a degree-two factor $1-tT+qT^2$, form tensor and symmetric-power factors using the full eigenvalue multisets. The equality

$$P_{\operatorname{Std}(A)\otimes\operatorname{Sym}^r(B)}(q^{r/2}T)
 =P_{\operatorname{Sym}^{2r+1}(C)}(T)$$

holds exactly when, for some $\sigma\in\{1,-1\}$, one of

$$x=\sigma^rD_{r+1}(z),\quad y=\sigma z,$$

$$x=\sigma^r z,\quad y=\sigma(z^2-2)$$

holds, or when

$$r\equiv3\pmod4,\qquad A=0,\qquad B^2=C^2=2q.$$

The exceptional family is disjoint from the graph loci at those ranks and occurs for rational raw data exactly when $2q$ is a rational square. For integral traces and positive odd integer $q$ it cannot occur. The dilation by $q^{r/2}$ is essential; a trace or a coefficient prefix does not determine equality of the full factors. No Hasse bound or actual elliptic-curve realization is assumed.

## Proof route

Normalize eigenvalues as $u^{\pm1}v^{r-2j}$ and $w^{2r+1-2k}$. Two adjacent tensor eigenvalues force $v^2=w^{2d}$. If $w$ is not torsion, equality of spectra becomes equality of integer weight multisets. The maximum-weight argument yields the two signed graph loci. Any nongraph complex solution has bounded torsion order. Rational raw data reduce the remaining possibilities to fixed square classes; affine residue counts along rank classes solve all ranks, rather than extrapolating a finite ladder.

The [full proof](../../../standalone/2026-09-07-astra-all-rank-spectral-intersection/PROOF.md) contains the finite torsion reduction, exact exception and recognition algorithm. The [original source record](../../../standalone/2026-09-07-astra-all-rank-spectral-intersection/SOURCES.json) credits the predecessor graph theorem. The selected review independently reconstructed the 4,320 affine rows; that is its stated finite coverage, not 4,320 unrelated theorem proofs.

## Scope beyond rational factors

Over arbitrary complex traces, the result controls reduced positive-dimensional loci and excludes noncyclotomic nongraph points at the stated torsion bound. It does not classify scheme multiplicities or every arbitrary-complex torsion residual. A separate monodromy obstruction requires its declared reductive joint group and connected target image containing $\mathrm{SL}_2$; it does not rule out or construct all abelian/CM-type realizations. Recognition cost is an exact arithmetic-operation count, not a bit-complexity claim.

**Significance and next task.** The theorem replaces repeated high-degree coefficient elimination by an all-rank classification while retaining an essential exception. A useful continuation is to establish a concrete compatible arithmetic realization under explicit monodromy hypotheses. Matching local factors alone is not that realization and supplies no RH or GRH conclusion.
