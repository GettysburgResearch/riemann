# L-106023 — Function-field square phases are a Kummer--Fourier family with exact principal embedding

Claim ID: `L-106023`  
Programme aliases: `LFAM2.KUMMER_FOURIER_SQUARE_PHASE`, `LFAM2.OWNER_CONDUCTOR_LOCAL_MODEL`  
Status: **PROVED EXACT FINITE-FIELD MECHANISM; GLOBAL TRACE MOMENT OPEN**  
Created: 2026-08-24  
Depends on: `L-106020`; `L-106003`  
Programme issues: #743, #736, #737  
RH status: **not assumed**

Let `k=F_Q` have odd cardinality `Q`, let `psi` be a fixed nontrivial additive
character, let `u in k^*`, and let `(v_x)_(x in k^*)` be a finite
Hilbert-valued packet. Define

\[
F_h=\sum_{x\in k^*}v_x\psi(hux^2),
\qquad h\in k.
\tag{L-106023.1}
\]

For every multiplicative character `eta` with `eta(-1)=1`, put

\[
M_\eta=\sum_{x\in k^*}v_x\eta(x).
\tag{L-106023.2}
\]

The same Gauss transform as in `L-106020` gives

\[
\boxed{
\sum_{h\in k^*}\|F_h\|^2
={Q+1\over Q-1}\|F_0\|^2
+{2Q\over Q-1}
\sum_{\substack{\eta(-1)=1\\\eta\ne1}}
\|M_\eta\|^2.
}
\tag{L-106023.3}
\]

Hence

\[
\boxed{
\|F_0\|^2
\le {Q-1\over Q+1}
\sum_{h\in k^*}\|F_h\|^2.
}
\tag{L-106023.4}
\]

This theorem uses only finite-field character orthogonality and the exact
Gauss norm. It does not invoke the Riemann hypothesis for curves.

## Geometric interpretation

The square map

\[
[2]:\mathbf G_m\longrightarrow\mathbf G_m
\]

has kernel `{+1,-1}`. Its pushforward separates into the trivial and quadratic
Kummer sectors. Finite Fourier transform against the Artin--Schreier phase

\[
\mathcal L_{\psi(hux^2)}
\]

turns these sectors into the two Gauss-weight classes visible in
(L-106023.3). The nonprincipal even characters are Kummer sheaves
`L_eta`; the principal/quadratic square-root fibre is the untwisted core
channel.

Thus the local geometric mechanism behind the CV/XD owner phases is not generic
purity or a zero-radius statement. It is the explicit Kummer--Artin--Schreier
Fourier transform of the square map.

## Global function-field target

For an owner irreducible `mathfrak r`, the residue field is

\[
k_\mathfrak r=F_q[T]/(\mathfrak r).
\]

The owner-excluded polynomial Vaughan packet can be twisted by the even Kummer
characters of `k_mathfrak r^*` exactly as in `L-106022`. Complete residue-field
sums obey (L-106023.3).

The remaining theorem is to control the **incomplete degree-restricted and
Möbius/Vaughan-weighted** Kummer--Artin--Schreier traces coherently as the owner
irreducibles vary. A satisfactory proof must state:

```text
the actual sheaf or cohomological complex;
its conductor and exceptional/resonant strata;
memberwise versus family-averaged scope;
the treatment of the principal/quadratic root fibre;
the corresponding number-field hybrid character/exponential-sum estimate.
```

This target is the sharpened `FFSOCM106023` interface in `T-106020`. A proof in
function fields would identify a mechanism; it would not transfer number-field
RH automatically.