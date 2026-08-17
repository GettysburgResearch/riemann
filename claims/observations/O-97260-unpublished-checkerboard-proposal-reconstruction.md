# O-97260 — Reconstruction of the unpublished checkerboard/Cauchy–Binet proposal

Claim ID: `O-97260`  
Status: **WITHDRAWN HISTORICAL RECONSTRUCTION — NOT A PROVED THEOREM**  
Created: 2026-08-17  
Frozen comparison: PR #567 at `50e596560b4f6f423e87fd6718d74913d863df99`  
RH status: **unproved**

The unpublished assistant response described the following stronger chain.

For each endpoint `X`, retain every original squarefree source occurrence and
its complete ordered rough history. Let `A_X` be the source-atom set and
`\mathcal L_X` the terminal-owner set. The response proposed an owner-incidence
matrix `H_X`, a terminal target/scalar matrix `K_X`, and a root feature matrix
formed before history aggregation.

The intended terminal data were
\[
 K_X(\ell,:)=\bigl(t_\ell,r_\ell\bigr),
 \qquad r_\ell=5R_2(\ell)+3R_3(\ell),
\]
with odd-history labels placed in reversed parity orientation.

The proposed conclusion was:

1. every target prefix required by Hall is nonnegative;
2. every target/scalar \(2\times2\) minor has checkerboard sign;
3. activation-boundary limits preserve those signs;
4. compact and directed-tail domains cover every terminal;
5. Cauchy–Binet propagates the checkerboard through the owner incidence;
6. one global Hall coefficient vector gives
   \[
   \mathcal R_X=5c_X(2)+3c_X(3)\ge0;
   \]
7. the exact zero-safe Mellin numerator then gives RH.

This chain was never committed in that status. The present reconciliation
retains it only as a precise record of what was claimed.

The valid conditional form is
\[
 \boxed{\mathrm{TCPH}_X\Longrightarrow\mathrm{GPHT*}_X
 \Longrightarrow\mathcal R_X\ge0,}
\]
where `TCPH_X` must include the **global target/Lorenz prefix inequalities**, not
merely local terminal determinants.

Those global prefix inequalities are the missing producer. Once included,
`TCPH_X` is at least as strong as `GPHT*_X`; it is not a derivation of it.
