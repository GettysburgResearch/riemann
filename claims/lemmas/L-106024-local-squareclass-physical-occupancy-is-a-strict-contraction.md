# L-106024 — Local squareclass physical occupancy is a sharp strict contraction

Claim ID: `L-106024`  
Programme aliases: `LFAM1.LOCAL_OCCUPANCY`, `STRESS.LOCAL_BPOE`, `LFAM2.KUMMER_OCCUPANCY`  
Status: **PROVED EXACT SHARP OPERATOR THEOREM**  
Created: 2026-08-24  
Depends on: `L-106020`  
Related reviewed frontier: `BPOE103300`  
Programme issues: #743, #736, #737  
RH status: **not assumed**

Fix an odd prime `p`, a nonzero residue `u`, and a Hilbert-valued packet
`(v_n)` supported away from `p`. Define the square-phase fields

\[
F_h=\sum_n v_n e_p(hun^2),
\qquad h\in\mathbf F_p.
\]

Let `mathscr H_(p,u)^sq` be the completion of such packets in the phase norm

\[
\|v\|_{\rm ph}^2
:=\sum_{h=1}^{p-1}\|F_h\|^2,
\tag{L-106024.1}
\]

modulo its null space. Define the local physical observation

\[
\mathscr O_{p,u}^{\rm sq}v:=F_0=\sum_n v_n.
\tag{L-106024.2}
\]

Then

\[
\boxed{
\|\mathscr O_{p,u}^{\rm sq}\|^2
={p-1\over p+1}<1.
}
\tag{L-106024.3}
\]

## Proof and sharpness

Aggregate the coefficients in residue classes and pair `c` with `-c`. Put

\[
w_{\{c,-c\}}=v_c+v_{-c},
\qquad
m={p-1\over2}.
\]

The exact phase energy is

\[
\|v\|_{\rm ph}^2
=p\sum_{j=1}^m\|w_j\|^2
-\left\|\sum_{j=1}^m w_j\right\|^2,
\tag{L-106024.4}
\]

whereas

\[
\mathscr O_{p,u}^{\rm sq}v=\sum_jw_j.
\]

For fixed `S=sum_j w_j`, convexity gives

\[
\sum_j\|w_j\|^2\ge{\|S\|^2\over m},
\]

with equality exactly when all `w_j=S/m`. Substitution yields

\[
\|v\|_{\rm ph}^2
\ge{p+1\over p-1}\|S\|^2,
\]

and the equality configuration proves sharpness.

Equivalently, in sign-pair coordinates the phase Gram is `pI-J`; its constant
mode has eigenvalue `(p+1)/2` and its orthogonal modes have eigenvalue `p`.

## Tensor occupancy

For source-owned square phases at distinct primes `p_1,...,p_k`, the local
physical observation is the tensor product and therefore

\[
\boxed{
\left\|\bigotimes_{j=1}^k
\mathscr O_{p_j,u_j}^{\rm sq}\right\|^2
=
\prod_{j=1}^k{p_j-1\over p_j+1}<1.
}
\tag{L-106024.5}
\]

## Relation to `BPOE103300`

The reviewed occupancy frontier `BPOE103300` concerns the complete observation
which also sums **different** source-owned occurrences and owner packets after
they are mapped to physical integers. Equation (L-106024.3) proves the local
observation norm for each clean squareclass packet; it does not make distinct
packets orthogonal after physical collapse.

Thus the occupancy operator now factors conceptually as

```text
source/phase amplitude
 -> local squareclass observation        SHARP CONTRACTION, PROVED
 -> coherent assembly of owner packets   OPEN
 -> physical shell.
```

The open assembly is the owner-conductor moment `SOCM106020`. No claim that
`BPOE103300`, `SOCM106020`, or RH is proved is made here.
