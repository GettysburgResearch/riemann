# T-93243 — The Q4 endpoint criterion reduces completely to a distinct-prime Gram correlation

Claim ID: `T-93243`  
Status: **PROPOSED CONDITIONAL RH-EQUIVALENT CRITERION — DEPENDS ON UNREVIEWED `T-93010`; RH UNPROVED**  
Created: 2026-08-15  
Depends on: `L-93242`; PR #474 at `56eeaccb2b041fdf68b6e718bad85032ecbdc66a`, especially the proposed endpoint-PIG equivalence `T-93010`  
Scope: exact reduction of the frozen Q4 endpoint criterion; no unconditional distinct-prime estimate

## 1. Distinct-prime functional

Use the complete prime-base endpoint rows \(R_{N,p}\in\mathbb R^N\) from `L-93242` and define

\[
\mathfrak C_{\ne p}(N)
=
\frac{2}{N^2}
\sum_{p<r}\langle R_{N,p},R_{N,r}\rangle.
\tag{T-93243.1}
\]

The same-prime diagonal is

\[
\mathfrak D_\circ(N)
=
\frac1{N^2}
\sum_p\|R_{N,p}\|_2^2.
\tag{T-93243.2}
\]

`L-93242` proves unconditionally that

\[
0\le\mathfrak D_\circ(N)\le576\log^2N
\tag{T-93243.3}
\]

and exactly that

\[
\boxed{
\mathscr P_\circ(N)
=
\mathfrak D_\circ(N)+\mathfrak C_{\ne p}(N).
}
\tag{T-93243.4}
\]

Thus every same-prime tower, including the four-adic correction, is already polylogarithmic. All remaining growth of the complete endpoint PIG belongs to the distinct-prime Gram correlation.

## 2. Conditional RH equivalence

The frozen theorem `T-93010` proposes

\[
\mathrm{RH}
\iff
\mathscr P_\circ(N)\ll(\log N)^A
\quad(N\ge2)
\]

for some fixed exponent \(A\).

On that input, (T-93243.3)--(T-93243.4) give

\[
\boxed{
\mathrm{RH}
\iff
|\mathfrak C_{\ne p}(N)|
\ll(\log N)^B
\quad(N\ge2)
\text{ for some fixed }B.
}
\tag{T-93243.5}
\]

Indeed, if the endpoint PIG is polylogarithmic, then

\[
|\mathfrak C_{\ne p}|
\le
\mathscr P_\circ+
\mathfrak D_\circ
\ll(\log N)^{\max(A,2)}.
\]

Conversely, a polylogarithmic bound for \(|\mathfrak C_{\ne p}|\), together with (T-93243.3), makes \(\mathscr P_\circ\) polylogarithmic, so the reverse implication in `T-93010` yields RH.

## 3. Quantitative off-line obstruction

The pole-to-energy clause of `T-93010` proposes that a zero \(\rho\) with

\[
\beta=\operatorname{Re}\rho>\frac12
\]

forces, for every \(0<\varepsilon<\beta-1/2\),

\[
\mathscr P_\circ(N)
\ne O\left(N^{2\beta-1-2\varepsilon}\right).
\tag{T-93243.6}
\]

Since \(\mathfrak D_\circ(N)\) is only polylogarithmic, the distinct-prime functional alone must satisfy

\[
\boxed{
\limsup_{N\to\infty}
\frac{\mathfrak C_{\ne p}(N)}
 {N^{2\beta-1-2\varepsilon}}
=+\infty.
}
\tag{T-93243.7}
\]

In particular the cross-prime correlation is forced to be large in the positive direction along a sequence. By `L-93242`, every such endpoint also has a canonical rank-one half-space witness supported on at least

\[
\frac{\mathscr P_\circ(N)}{576\log^2N}
\]

distinct prime bases.

## 4. What this closes and what it does not

This theorem closes the **same-prime-removal problem** for the complete Q4 endpoint criterion: no same-prime tower, endpoint term, or four-adic gauge remains in the RH-bearing gate.

It does not prove the remaining estimate

\[
|\mathfrak C_{\ne p}(N)|\ll(\log N)^B.
\]

That is now a pure distinct-prime theorem in one positive row-space normalisation. A proof may be sought through the weighted-Goldbach expansion, the singular cosine-antiderivative expansion, or directly through the rank-one row witness, but those are alternative coordinates for the same remaining object.

## 5. Proof boundary

Native and exact in this packet:

- complete prime-base row decomposition;
- polylogarithmic same-prime diagonal;
- reduction from PIG to a pure distinct-prime Gram correlation;
- quantitative rank-one inverse theorem.

Imported and still awaiting independent review:

- `T-93010`, including endpoint PIG \(\Longleftrightarrow\) RH and its off-line pole-to-energy clause.

Open:

- unconditional polylogarithmic control of \(\mathfrak C_{\ne p}(N)\);
- RH.
