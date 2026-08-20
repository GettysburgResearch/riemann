# L-100181 — Exact source-labelled desmoothing identity

Claim ID: `L-100181`  
Status: **PROVED EXACT ALGEBRAIC REDUCTION; ORIENTED MASS ESTIMATE OPEN**  
Created: 2026-08-20  
RH status: **unproved**

Let `F` be any signed source observation carrying a parity label, and let a one-prime finite Euler completion act by

\[
\mathcal A_p=I+rS_p,\qquad r=p^{-1/2}.
\]

At the labelled-source level, `A_p` does not erase the old occurrence. It adjoins one new occurrence with the **same sign** and shifted endpoint. If the native source before completion already contains the corresponding Euler pair `I-rS_p`, then

\[
(I+rS_p)(I-rS_p)=I-r^2S_{p^2}.
\]

Thus finite squaring is exactly a same-prime parity-pair cancellation, not a scalar smoothing. Desmoothing by the alternating operator `(I+rS_p)^(-1)` is unnecessary if the paired occurrences are kept until the physical observation: the completed source differs from the native source by the explicit signed correction

\[
 rS_pF,
\]

with complete prime-owner provenance.

For a finite cutoff `Z`, iterating gives an exact labelled expansion

\[
\mathscr A_ZF
=F+\sum_{\emptyset\ne A\subseteq\mathcal P_Z}
 r_A S_AF,
\]

with no duplicate owner. Hence

\[
F
=\mathscr A_ZF-
\sum_{\emptyset\ne A}r_AS_AF.
\]

The first term is globally positive on the critical Bernstein corridor by `L-100180`. The remaining conclusion-producing task is therefore an **oriented labelled correction estimate**, not operator inversion: prove that the logarithmic negative mass of the explicit correction sum is subpower after cancellation by its inherited native parity labels.

This formulation preserves every source occurrence and exposes the exact place where a valid proof must save over source-blind absolute values.
