# L-94052 — Phase locking shrinks the absolute saddle but preserves the prime-block variance scale

Claim ID: `L-94052`  
Status: **PROPOSED COMPLETE ASYMPTOTIC ON FROZEN PRIME INPUTS — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-16  
Depends on: `L-94050`; PR #390 coefficient-energy input; PR #483 prime-block grouping  
Scope: fixed filter order; no pointwise decorrelation conclusion

Fix an integer \(m\ge0\), and put

\[
b_{q,m}(n)
 ={\Lambda(n)\over\sqrt n}
  (D_L^{2m}h_q)(\log n).
\tag{L-94052.1}
\]

Define

\[
V_m(q)=\sum_{n\ge2}|b_{q,m}(n)|^2.
\tag{L-94052.2}
\]

Then, on the same classical input used by PR #390,

\[
\boxed{
V_m(q)=q+O_m(\sqrt q).
}
\tag{L-94052.3}
\]

## Proof sketch with the load-bearing normalization

The coefficient-energy range is \(\log n\asymp\sqrt q\), not the absolute-prime
saddle \(\log n\asymp q\). On this scale, every fixed shift by \(L\) is
\(O(q^{-1/2})\) after rescaling, and

\[
D_L1=1.
\tag{L-94052.4}
\]

Taylor expansion therefore gives, uniformly with a Gaussian majorant,

\[
(D_L^{2m}h_q)(\sqrt q\,v)
 =h_q(\sqrt q\,v)+O_m(q^{-1/2})(1+|v|^{C_m})e^{-v^2/8}.
\tag{L-94052.5}
\]

Partial summation against

\[
\sum_{n\le e^U}{\Lambda(n)^2\over n}
 ={U^2\over2}+O(U)
\tag{L-94052.6}
\]

then yields (L-94052.3).

Group powers by base prime:

\[
Y_{p,q,m}(x)
 =\sum_{r\ge1}b_{q,m}(p^r)p^{irx}.
\tag{L-94052.7}
\]

Since \(D_L^{2m}h_q\) is a fixed finite combination of shifted Gaussians, the
same-prime unequal-power tail is bounded by a constant depending only on \(m\).
Thus

\[
\boxed{
\sum_p|Y_{p,q,m}(x)|^2\ll_m q+1
}
\tag{L-94052.8}
\]

uniformly in the carrier.

If \(\mathcal M_m(q,x)<0\) at high centre, the gamma reserve and explicit
formula force

\[
|S_m(q,x)|\gg_m\log|x|.
\tag{L-94052.9}
\]

The exact Hilbert lemma `L-93240` then gives

\[
\boxed{
\#\{\text{positively projecting prime bases}\}
 \gg_m {\log^2|x|\over q+1}.
}
\tag{L-94052.10}
\]

The phase-lock filter therefore improves the absolute pointwise wedge without
turning the remaining carrier into a diagonal or cardinality contradiction.
This is exactly the firewall required by `R-93254`.
