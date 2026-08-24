# L-102886 — A dyadic-frozen Vaughan cutoff removes transfer atoms from the negative-mass proof

Claim ID: `L-102886`  
Status: **PROVED EXACT BLOCKWISE DECOMPOSITION THEOREM**  
Created: 2026-08-24  
Depends on: corrected `L-102881`; `R-102869`  
RH status: **not assumed**

The derivative detector scalar

\[
\mathcal C^K_{p,q}(Y)
=\sum_{P^+(a)<q}{\mu(a)\over a}K_L(Y/a^2)
\]

is independent of every Vaughan cutoff.  Therefore the cutoff may be chosen proof-side, separately on each logarithmic block.

For

\[
I_j=[2^j,2^{j+1}),
\]

put

\[
\boxed{U_j=\lfloor2^{j/6}\rfloor.}
\tag{L-102886.1}

For every `Y in I_j`, apply the exact finite-Euler identity with the **fixed** cutoff `U_j`.  This gives

\[
\boxed{
\mathcal C^K_{p,q}(Y)
=\mathcal T^K_{p,q;j}(Y)+\mathcal B^K_{p,q;j}(Y)
}
\tag{L-102886.2}

pointwise throughout the block.

## 1. Type-I scale is unchanged

Since

\[
U_j\asymp Y^{1/6}
\qquad(Y\in I_j),
\]

`L-102880` gives uniformly

\[
\boxed{
(\mathcal T^K_{p,q;j})^{\rm full}(Y)
=O_K(Y^{-1/6}).
}
\tag{L-102886.3}

The stopped boundary remains the literal `P^+(m)<q` boundary.

## 2. Type-II support remains balanced

Because `a_(U_j,q)(n)=0` for `n<=U_j`, every nonempty balanced block satisfies

\[
r,s>U_j\gg Y^{1/6},
\qquad m\ll Y^{1/6},
\qquad rsm\asymp\sqrt Y,
\]

with only absolute dyadic constants changed.

## 3. No moving-source charge in logarithmic mass

Inside `I_j`, the cutoff is constant, so the separate derivative identities contain no transfer atom.  At the endpoint `2^(j+1)`, the proof decomposition is reset from `U_j` to `U_(j+1)`, but both decompositions equal the same fixed scalar `C^K_(p,q)`.

The endpoint set is countable and has zero `dY/Y` measure.  Therefore, provided Type-I and Type-II are recombined **before** taking a negative part on each block,

\[
\boxed{
\int_1^Y(\mathcal C^K_{p,q})_-{dt\over t}
=\sum_j\int_{I_j\cap[1,Y]}
(\mathcal T^K_{p,q;j}+\mathcal B^K_{p,q;j})_-{dt\over t}.
}
\tag{L-102886.4}
\]

No cutoff-transfer reserve appears in this conclusion-facing identity.

## Scope firewall

This theorem does not validate differentiating the dynamic decomposition channelwise; `R-102869` remains binding.  It replaces that unnecessary operation by a blockwise fixed source partition of the already-fixed derivative detector.

Thus `KUV102881` is not an independent arithmetic gate when the negative-mass proof is organized dyadically.  The smooth-boundary and balanced cross-current remain.
