# L-106070 — A three-prime block palette gives a source-exact unramified character partition

Claim ID: `L-106070`  
Programme aliases: `LFAM1.SCALE_MATCHED_PALETTE`, `STRESS.LINEAR_MODULUS_COLOURING`, `LFAM2.BLOCK_CONDUCTOR_CHART`  
Status: **PROVED UNCONDITIONAL SOURCE-PARTITION THEOREM**  
Created: 2026-08-25  
Depends on: `R-106001`, `R-106070`; `L-102883`; `L-106001`, `L-106004`  
Programme issues: #743, #736, #737  
RH status: **not assumed**

Work after the complete carrier recombination, Wick quotient, horizon-safe
pair allocation, overlap renewals and owner-excluded stopped-Vaughan identity
of the parent packet.  No negative part or source-blind norm has yet been
applied.

Fix one dyadic balanced block

\[
u\in[U,2U),
\qquad
v\in[V,2V),
\qquad
m\in[M,2M),
\]

and put

\[
B=UVM.
\]

Every physical core in the block is

\[
c=uvm\in[B,8B).
\tag{L-106070.1}
\]

## 1. A bounded Bertrand palette

For \(j=0,1,2,3\), Bertrand's postulate supplies a prime

\[
\lambda_j\in
\bigl(2^{j+4}B,\,2^{j+5}B\bigr).
\tag{L-106070.2}
\]

The four intervals are disjoint.  At most one selected prime is the marked
physical prime \(67\).  Discard that candidate, if present, and retain any
three of the others.  Denote them

\[
\mathcal P_B=\{\ell_0,\ell_1,\ell_2\}.
\]

Then

\[
\boxed{
16B<\ell_j<256B,
\qquad
\ell_j\ne67.
}
\tag{L-106070.3}
\]

The palette depends only on the declared dyadic block.  It is fixed before any
owner pair, character, phase, norm, hypothetical zero or sign estimate is
introduced.

## 2. Linear owner colours

A clean HBC source atom has a two-prime squarefree owner label

\[
P=pq
\]

and physical index

\[
N=P c^2.
\]

Define its palette pattern

\[
\boxed{
A_B(P)=\{j\in\{0,1,2\}:\ell_j\mid P\}.
}
\tag{L-106070.4}
\]

Because \(P\) has at most two physical owner primes,

\[
|A_B(P)|\le2.
\]

For every pattern \(A\subseteq\{0,1,2\}\) with \(|A|\le2\), let
\(\Pi_{B,A}\) be the coefficient projector onto atoms with
\(A_B(P)=A\), and choose

\[
\boxed{
\ell(B,A)=\ell_{\min(\{0,1,2\}\setminus A)}.
}
\tag{L-106070.5}
\]

The projectors form an exact disjoint linear partition:

\[
\boxed{
R_{\mathcal B}
=
\sum_{\substack{A\subseteq\{0,1,2\}\\|A|\le2}}
R_{\mathcal B,A},
\qquad
R_{\mathcal B,A}:=\Pi_{B,A}R_{\mathcal B}.
}
\tag{L-106070.6}
\]

There are at most seven nonempty colours.  No source occurrence is duplicated.

The duplicate-labelled-\(67\) convention and the four marked local sectors do
not alter the partition: every palette prime is physically different from
\(67\), and the marked sector remains a finite source label inside its colour.

## 3. Every coloured block is unramified

For an atom in colour \(A\), (L-106070.5) gives

\[
\ell(B,A)\nmid P.
\]

Moreover, by (L-106070.1) and (L-106070.3),

\[
0<c<\ell(B,A).
\]

Therefore

\[
\boxed{
\ell(B,A)\nmid P c^2.
}
\tag{L-106070.7}
\]

This holds coefficientwise for every occurrence in the complete coloured
block, including all carrier, gauge, stopped-Vaughan and marked-prime labels.

Consequently the principal character modulo \(\ell(B,A)\) is identically one
on the declared block.  For any Dirichlet character \(\chi\) modulo this
prime, define at the final linear stage

\[
R_{\mathcal B,A;\chi}
=
\sum_{N\in\mathcal B,A} r_N\chi(N)\,v_N.
\tag{L-106070.8}
\]

Then

\[
\boxed{
R_{\mathcal B,A;\chi_0}
=R_{\mathcal B,A}
}
\tag{L-106070.9}
\]

coefficientwise.  No ramified completion term is needed on this declared
region because the region is literally disjoint from the ramified prime.

Equation (L-106070.9) is the separately proved residual-level exception
allowed by `R-106001`: it does **not** apply completion after an arbitrary
residual.  It first proves that the exact residual block contains no multiple
of its selected modulus.

## 4. Subpower partition cost

On one dyadic physical horizon there are at most

\[
O((\log X)^3)
\]

stopped-Vaughan triple blocks and at most seven colours per block.  Hence, for
any Hilbert norm,

\[
\boxed{
\left\|\sum_{\mathcal B,A}R_{\mathcal B,A}\right\|^2
\le
X^{o(1)}
\sum_{\mathcal B,A}\|R_{\mathcal B,A}\|^2.
}
\tag{L-106070.10}
\]

This Cauchy step is taken only after the complete all-chaos carrier has been
recombined inside each linear block.  It does not split the equal-core and
core-discrepancy negative parts forbidden by `R-102869`.

## Scope

The theorem proves a nonduplicating source partition and a colour-safe
power-scale modulus on every block.  It does not by itself bound the character
moment or root-residue occupancy.  The injective collision geometry is proved
in `L-106071`, and the modulus is paid by the retained block energy in
`L-106072`.