# R-32702 — The paired generalized endpoint is not always equality; the endpoint inequality remains positive

Claim ID: `R-32702`  
Status: **EXACT SCOPE CORRECTION TO `L-32704.34`; MAIN COFINAL THEOREM RETAINED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-09  
Scope: the `j=1,n-1` endpoint sentence in `L-32704`; no change to the mixed four-adic decomposition or cofinal theorem

## 1. Incorrect subclaim

The first version of `L-32704`, Section 7, wrote

\[
P_\pm(n,1)^2=S_\pm(n,1).
\]

That equality is true for the ordinary von-Mangoldt source and for odd parents in the parity-paired generalized source, but it is **not** true for every even parent of the Euler-filtered generalized source.

For example, at `n=2` the paired defect is strictly positive.

The error is confined to the word/equation asserting endpoint equality. It is not used by the proof of the cofinal inequality.

## 2. Correct endpoint proof from the already-established decomposition

Retain the notation of `L-32704`:

\[
O=\log\operatorname{odd}\binom nj,
\qquad
E=\sum_{r\ge1}D_{2r}\chi_{n,4^r}(j),
\qquad
R=\sum_{r\ge1}D_{2r-1}\chi_{n,2^{2r-1}}(j).
\]

At `j=1`, the odd-prime endpoint is ordinary, so

\[
O(n,1)^2=S_{\rm odd}(n,1).
\]

Also every strict four-adic descendant has

\[
J_r=\left\lfloor\frac1{4^r}\right\rfloor=0,
\]

hence

\[
M_< =0.
\]

The current-row mixed boundary is still absorbed by the exact `2OE` cross term, and `L-32405` still gives `S_dyad<=E^2`. Therefore the already-proved master inequality `L-32704.25` specializes to

\[
\boxed{
\frac{P_+(n,1)^2+P_-(n,1)^2-S_+(n,1)-S_-(n,1)}2
\ge R(n,1)^2\ge0.}
\tag{R-32702.1}
\]

The same argument applies at `j=n-1` by symmetry.

Thus the correct endpoint statement is

\[
\boxed{
P_+(n,1)^2+P_-(n,1)^2
\ge S_+(n,1)+S_-(n,1),}
\tag{R-32702.2}
\]

with equality on odd parents and possible strict surplus on even parents.

## 3. Disposition

```text
L-32704.34 universal endpoint equality       FALSE / superseded here
endpoint paired inequality                  RETAINED EXACTLY
four-adic product-carry identity             UNAFFECTED
mixed-boundary cross-energy absorption       UNAFFECTED
cofinal all-row theorem L-32704.36           UNAFFECTED
RH                                           UNPROVED
```

Review `R-32702` together with `L-32704`; equation `L-32704.34` must not be cited in its original equality form.
