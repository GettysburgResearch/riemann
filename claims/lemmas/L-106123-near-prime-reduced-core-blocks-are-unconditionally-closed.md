# L-106123 — Near-prime reduced-core blocks are unconditionally closed

Claim ID: `L-106123`  
Programme aliases: `LFAM1.NEAR_PRIME_CORE_CLOSURE`, `LFAM2.FIXED_CORE_OWNER_LARGE_SIEVE`, `STRESS.ROUGH_COFACTOR_LOCALIZATION`  
Status: **PROVED UNCONDITIONAL SUBPOWER CLOSURE OF ALL LOW-CORE-MULTIPLICITY BLOCKS**  
Created: 2026-08-25  
Depends on: `L-106120--L-106122`; parent `L-102958--L-102959`  
Programme issues: #743, #736, #737  
RH status: **not assumed**

Work in one bilateral tensor block

\[
 C\le c<2C,
 \qquad
 D\le d<2D,
 \qquad
 P^-(c)=\ell,
 \qquad
 P^-(d)=\rho,
 \qquad
 (c,d)=1.
\tag{L-106123.1}
\]

Parent ratio-eight comparability gives, on every interacting physical pair,

\[
 P\ll D,
 \qquad
 Q\ll C,
\tag{L-106123.2}
\]

for the two semiprime owner products.  All implicit constants are absolute and
may be absorbed by a fixed number of dyadic owner blocks.

## 1. Fixed-core two-dimensional owner large sieve

Fix `g,c,d` and let `(a_{P,Q})` be arbitrary Hilbert-valued coefficients
supported on the owner ranges in (L-106123.2), with all clean-incidence masks
already inserted.  Define

\[
 F_{h,k}
 =
 \sum_{P,Q}a_{P,Q}
 e_\ell(-hQd^2)e_\rho(kPc^2).
\]

Because `d` is a unit modulo `ell` and `c` is a unit modulo `rho`, the square
factors merely permute residue classes.  Complete additive orthogonality and
Cauchy inside each residue cell give

\[
\boxed{
 \sum_{h=0}^{\ell-1}
 \sum_{k=0}^{\rho-1}
 \|F_{h,k}\|^2
 \le
 (\ell+O(C))(\rho+O(D))
 \sum_{P,Q}\|a_{P,Q}\|^2.
}
\tag{L-106123.3}
\]

Indeed an interval of length `O(C)` contains at most `O(1+C/ell)` owner
products in one residue modulo `ell`, and similarly on the other side.  The
bound is valid for arbitrary source-incidence masks because deleting
coefficients cannot increase the residue-cell multiplicity.

Since `ell<=C` and `rho<=D`,

\[
\boxed{
 \sum_{h\ne0,k\ne0}\|F_{h,k}\|^2
 \ll CD\sum_{P,Q}\|a_{P,Q}\|^2.
}
\tag{L-106123.4}
\]

## 2. Literal source coefficients

For one fixed reduced-core pair, the complete physical coefficient is

\[
 a_{P,Q}
 ={\gamma_{P,Q}\over g^2cd\sqrt{PQ}},
 \qquad
 |\gamma_{P,Q}|\le X^{o(1)}.
\]

The semiprime reciprocal sums are polylogarithmic, so

\[
 \sum_{P,Q}\|a_{P,Q}\|^2
 \ll
 {X^{o(1)}\over g^4c^2d^2}.
\]

Substituting in (L-106123.4),

\[
\boxed{
 \sum_{h\ne0,k\ne0}\|F_{h,k}\|^2
 \ll {X^{o(1)}\over g^4CD}.
}
\tag{L-106123.5}
\]

After multiplying by the tensor source-dual weight `g^2 ell rho`, one fixed
core pair costs at most `X^{o(1)}/g^2`.

## 3. Number of reduced cores in one least-prime block

Every `c` in (L-106123.1) is a multiple of `ell`, and every `d` is a multiple
of `rho`.  Therefore

\[
 \#\{c\}\ll {C\over\ell},
 \qquad
 \#\{d\}\ll {D\over\rho}.
\tag{L-106123.6}
\]

Let

\[
 \mathfrak n(C,D;\ell,\rho)
 ={C\over\ell}{D\over\rho}.
\tag{L-106123.7}
\]

Cauchy across the linear `(c,d)` source partition loses at most one factor
`mathfrak n`, and the sum of the fixed-pair energies contains at most another
factor of the same size.  Hence the complete block contribution is

\[
\boxed{
 \mathfrak M_{\rm BT}(C,D;\ell,\rho)
 \ll
 X^{o(1)}\mathfrak n(C,D;\ell,\rho)^2.
}
\tag{L-106123.8}
\]

The estimate includes all four tensor channels, in particular the untwisted
principal--principal member.

## 4. Closed sector

Consequently every block satisfying

\[
\boxed{
 {C\over\ell}{D\over\rho}=X^{o(1)}
}
\tag{L-106123.9}
\]

has subpower tensor moment and is unconditionally closed.

Writing

\[
 c=\ell u,
 \qquad
 d=\rho v,
\]

condition (L-106123.9) is simply

\[
 uv=X^{o(1)}.
\]

Thus the remaining frontier may assume that at least one source side contains
a genuinely power-sized rough cofactor.

## 5. Exact residual

Define

```text
BTRC106123:
  the bilateral tensor moment restricted to blocks with

      (C/ell)(D/rho) > X^epsilon

  for some fixed epsilon>0, equivalently with a power-sized product of rough
  cofactors u*v, is subpower after the same source recombinations.
```

For every fixed `epsilon`, all complementary blocks are closed by
(L-106123.8).  A slowly tending threshold gives the usual `X^o(1)` frontier.

## Meaning

The live obstruction is no longer arbitrary owner coherence.  It requires a
long squarefree rough history after both least core primes have been removed:

```text
c=ell*u,  every prime of u >= ell;
d=rho*v, every prime of v >= rho;
u*v is power-sized.
```

This is the precise source on which a second Buchstab/Vaughan decomposition,
a recursive Kummer tensor, or a geometric trace estimate must act.

## Scope

The lemma closes the near-prime/low-multiplicity core sector.  It does not
estimate `BTRC106123`, and therefore does not prove `BTPP`, `BTPN`, `BTNN`,
`BCI102990`, or RH.
