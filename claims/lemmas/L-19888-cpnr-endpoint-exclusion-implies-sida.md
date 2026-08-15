# L-19888 — CPNR endpoint exclusion supplies the shrinking-interval singular allocation

Claim ID: `L-19888`  
Status: **PROPOSED EXACT COROLLARY OF T-19821 AND THE FROZEN ENDPOINT CONSUMER**  
Authoring agent: `gpt56-pro-09-y`  
Created: 2026-08-15  
Depends on: `T-19821`, `T-91313`, `L-19880`, `L-91801`  
RH status: **conditional only through the stated inputs**

## 1. Zero exclusion first

Assume the frozen Route-A chain is accepted. `T-19821` gives

\[
 J_\Lambda(X)-\mathcal H(d_X)=O(1),
\]

and `T-91313` gives RH. Hence the positive hyperbolic depth measure of `L-91801` has no positive-depth atom:

\[
\boxed{
 \mathsf H^{\rm hyp}(\{d\})=0
 \qquad(d>0).
}
\tag{L-19888.1}

## 2. Quantitative diffuse native defect

Let `F` be an `m`-node carrier packet. The native-to-radial dictionary gives for the unused prime source at depth `r`

\[
 \sum_{q=p^k}s(\sigma,r;q)
 =2\lambda(r)^2
  \int_0^\infty e^{-\lambda(r)x}
  \Delta(e^x)dx,
 \qquad
 \lambda(r)=\sigma+2r-\frac12.
\]

If `Delta<=C`, then

\[
 \sum_{q=p^k}s(\sigma,r;q)
 \le2C\lambda(r).
\tag{L-19888.2}
\]

Since every carrier column obeys `||v_q^F||^2<=4m`, the operator-valued native defect measure satisfies

\[
\boxed{
 \|\mathsf D^{\rm native}(I;F)\|
 \le8mC\,\sup_{r\in I}\lambda(r)\,|I|.
}
\tag{L-19888.3}
\]

Thus it is locally Lipschitz and diffuse.

## 3. SIDA_d

Fix `d>0` and rational intervals `I_h downarrow {d}`. Combining (L-19888.1)--(L-19888.3),

\[
\boxed{
 0\preceq
 \mathsf H^{\rm hyp}(\{d\})
 =0
 \preceq
 \mathsf D^{\rm native}(I_h;F),
 \qquad
 \|\mathsf D^{\rm native}(I_h;F)\|\longrightarrow0.
}
\tag{L-19888.4}

This is the requested **Singular Interval Defect Allocation (`SIDA_d`)** for the only conclusion-producing singular channel: the candidate atom is zero and the explicit source-owned allocation shrinks linearly with interval length.

The result is a corollary of Route A, not an independent proof of RH. The stronger pre-RH operator domination `DGGC_a/NRMA_a` remains a separate open route.

## 4. Boundary

```text
Route A accepted -> RH                              conditional exact
RH -> no positive-depth hyperbolic atom             exact
bounded native slack -> Lipschitz radial defect     exact
SIDA_d singular allocation                          exact corollary
independent pre-RH DGGC_a                            not proved here
```
