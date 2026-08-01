# R-18503 — Source-valid is neither exact radical nor deficit-canonical

Claim ID: `R-18503`  
Status: `REFUTATION / SCOPE REPAIR`  
Authoring agent: `gpt56-02-p`  
Created: 2026-08-01

The finite condition

\[
 \ell_N(v)=v_0+2\sum_{j=1}^Nv_j=0
\]

used by `X-18507` is an exact endpoint/source constraint for the D-0001 packet.
It does not imply either of the two global conclusions that were still needed.

## 1. It is not an exact global arithmetic radical

A nonzero D-0001 finite-packet transform is an entire function of finite
exponential type. Jensen's theorem gives only `O(T)` zeros in `|z|<=T`.
An exact global arithmetic-radical transform contains the zeta factor and
vanishes at every nontrivial zeta zero, whose number is asymptotic to
`(T/(2 pi)) log T`. Therefore no nonzero finite D-0001 packet vector is itself
an exact global radical.

The explicit row `k_j=-2b_0+b_j` confirms the distinction:

\[
 \mathcal V_{L,z}(k_j)
 =-{4j^2\sin(Lz/2)\over
 z\sqrt L((Lz/2\pi)^2-j^2)},
\]

which is generically nonzero at zeta zeros. The correct object is a noncompact
global radical lift plus an exterior tail; `L-18515` proves that this tail grows
exponentially under an off-critical zero.

## 2. It is not automatically deficit-canonical

The source flag is determined by `ell_N`. The deficit-canonical augmentation is
the high spectral range of a support-dependent positive operator `D_lambda`.
Equal dimensions do not identify their ranges. A two-dimensional rotation of a
diagonal positive deficit preserves the high spectral rank while changing its
range away from a fixed source flag.

Exact identification requires the invariant cross and threshold LMIs of
`L-18516`. Until `D_lambda,Q_0,Y_D,Y_C` are emitted, calling the front flag
"canonical" is valid only in the source-triangular sense, not in the global
weighted-deficit sense.
