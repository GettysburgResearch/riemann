# L-99130 — Positive dyadic inverse and a common reciprocal-Julia profile

Claim ID: `L-99130`  
Status: **PROVED EXACT DIRICHLET/COEFFICIENT THEOREM**  
Created: 2026-08-19  
Frozen base: PR #611 at `9d0b0521e5ace8c96df63a85a68f60a789b09923`  
RH status: **not assumed**

Let `z>=5` be a prime cutoff and let

\[
 M_z(s)=\prod_{p\ge z}(1-p^{-s})
\]

be the literal squarefree future-prime Möbius source. Put `x=2^{-s}` and define

\[
 B_z(s)=(1-x)(1-x/2)M_z(s)
       ={1\over2}(1-x)(2-x)M_z(s),
\tag{L-99130.1}
\]

\[
 R_z(s)=\zeta(s)M_z(s)
       =\prod_{p<z}(1-p^{-s})^{-1}.
\tag{L-99130.2}
\]

The coefficients of `R_z` are exactly the nonnegative indicator of the
`z`-smooth integers.

The local dyadic factor in (L-99130.1) has the positive inverse

\[
\boxed{
 H_2(s)={2\over(1-2^{-s})(2-2^{-s})}
       =\sum_{k\ge0}(2-2^{-k})2^{-ks}.
}
\tag{L-99130.3}
\]

Indeed the coefficient of `x^k` is
`sum_(ell=0)^k 2^{-ell}=2-2^{-k}`. Hence

\[
\boxed{M_z=H_2B_z.}
\tag{L-99130.4}
\]

At the physical half-order normalization this is the literal activation-correct
identity

\[
 \mathcal M_z(Y)=\sum_{k\ge0}(2-2^{-k})2^{-k/2}
                  \mathcal B_z(Y/2^k),
\tag{L-99130.5}
\]

with only finitely many active terms at every real `Y`.

Finally,

\[
\boxed{R_z=G_\diamond B_z,}
\qquad
G_\diamond(s)={\zeta(s)\over(1-2^{-s})(1-2^{-s-1})}.
\tag{L-99130.6}
\]

Thus every moving-cutoff two-row state shares the same signed profile `B_z` and
the same cutoff-independent positive reciprocal-Julia compiler `G_diamond`.
No rough-density surrogate or continuum activation is used.
