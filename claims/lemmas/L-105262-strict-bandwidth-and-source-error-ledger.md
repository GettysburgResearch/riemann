# L-105262 — Strict-bandwidth source ledger and the surviving edge row

Claim ID: `L-105262`  
Status: **PROVED REDUCTION USING PINNED SOURCE ESTIMATES**  
Created: 2026-08-24  
Depends on: L-105323; L-105342; L-105423; L-105520; L-105253  
RH status: not assumed

Choose

\[
\lambda=\frac{999}{1000}.
\tag{1}
\]

The hard one-sided frame has

\[
d_T=(\lambda+o(1))N_1(T,2T).
\tag{2}
\]

Its two-copy physical cutoff is

\[
\alpha=2\lambda=\frac{999}{500}<2.
\tag{3}
\]

Therefore the ordinary long-polynomial Montgomery--Vaughan range applies; the endpoint-critical \(\alpha=2\) model theorem is not needed. Since \(\mathcal D_4(\alpha)\le\mathcal D_4(2)\), L-105261 remains valid.

The following rows are already \(o(d_T)\) at this fixed strict bandwidth:

1. entry-dependent reciprocal coefficient freezing, by L-105323 with \(X=T^\lambda\);
2. the omitted reciprocal Dirichlet tail, by L-105342/L-105253;
3. finite-degree polynomial conditioning, by L-105251;
4. the hard-frame dimension ledger, by L-105423;
5. common-factor and confluent critical blocks, by L-105343/L-105500.

No smooth taper is required: the observations are the source-fixed hard one-sided exponential frame. The direct full-signature \(F/F'\) consumer also avoids the auxiliary companion-pole ledger of the Lorentz-energy route.

After these reductions, the only unproved conclusion-facing row is

```text
EDGEFLUX105260:
  the normalized negative trace contributed by the actual Xi
  vertical/horizontal contour closure, safe-line-to-strip remainder,
  and any non-source archimedean endpoint term is
  < (647/19980-o(1)) d_T.
```

The constant is the exact room left after the strict-bandwidth dimension loss and the \(1/60\) polarization payment:

\[
1-\frac{0.95}{999/1000}-\frac1{60}=\frac{647}{19980}.
\tag{4}
\]

This lemma does not assert `EDGEFLUX105260`.
