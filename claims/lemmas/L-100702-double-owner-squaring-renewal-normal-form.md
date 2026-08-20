# L-100702 — Double-owner blocks admit an exact interior-squaring/positive-renewal normal form

Claim ID: `L-100702`  
Status: **PROVED EXACT COMPOSITION; TERMINAL SIGNED BLOCK ESTIMATE OPEN**  
Created: 2026-08-20  
Depends on: PR #691 `L-100600--L-100605`; PR #671 `L-99961`  
RH status: **not assumed**

Fix one off-diagonal double-owner block

\[
\mathcal D_{i,j}
=r_ir_jU_iU_j\prod_{i<h<j}(I-r_hU_h),
\qquad i<j.
\]

Only the primes in the finite open interval `(p_i,p_j)` remain unresolved.
Introduce the source-side completion

\[
\mathcal C_{i,j}
=\prod_{i<h<j}(I+r_hU_h).
\]

Commutation gives the exact identity

\[
\boxed{
\mathcal C_{i,j}
\prod_{i<h<j}(I-r_hU_h)
=
\prod_{i<h<j}(I-r_h^2U_h^2).
}
\tag{L-100702.1}
\]

No endpoint owner is altered. No inverse is used.

For the native half-order source `r_h=p_h^(-1/2)`, every completed interior
label has coefficient `p_h^(-1)`. Expanding the finite completion before
physical collapse gives a finite family of divisor-restricted packets. For
each exposed squarefree divisor `d`, PR #671 gives

\[
B_d(z)=\beta(d)B(z)G_d(z),
\qquad [n^{-z}]G_d(z)\ge0,
\tag{L-100702.2}
\]

and, on every fixed safe line,

\[
G_d(\sigma)\ll_{\sigma,\varepsilon}d^\varepsilon.
\tag{L-100702.3}
\]

Consequently every post-restriction dilation is positive. The entire sign of
the desquaring comparison is carried by the explicit divisor coefficient
`beta(d)`.

After applying a fixed compact physical observation `O_X`, each long-interval
block therefore has the exact normal form

\[
\boxed{
O_X\mathcal D_{i,j}f
=
\sum_d {\beta(d)\over\sqrt d}
\,\mathcal R_{i,j,d}(X),
}
\tag{L-100702.4}
\]

where each `mathcal R_(i,j,d)` is a positive dilation renewal of one
endpoint-frozen compact packet and has subpower Mellin mass.

For `i=j` there is no interior source. For `i<j` with `p_j/p_i<=8`, no
squaring is required: the block belongs to the fixed compact finite-band
sector. For `p_j/p_i>8`, (L-100702.4) is the deterministic long-interval
normal form.

## Deterministic terminal estimate

Define `DORN100702` to be the subpower logarithmic negative-mass estimate for
the exact sum of:

```text
diagonal singleton blocks;
short endpoint-ratio blocks p_j/p_i<=8;
long blocks in the normal form (L-100702.4).
```

All renewal kernels and coefficients are those of the literal source. Then

\[
\boxed{\mathrm{DORN100702}\Longrightarrow RH}
\tag{L-100702.5}
\]

through the minimal-wavelet negative-mass detector of PRs #674/#689.

The content of this lemma is that `DORN100702` contains no operator inverse,
no arbitrary future profile, and no unsigned rough reservoir. Its only signs
are the two explicit endpoint differences and `beta(d)`.
