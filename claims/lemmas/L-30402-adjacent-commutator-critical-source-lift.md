# L-30402 — Adjacent commutators lift every divisor source at critical capacity cost

Claim ID: `L-30402`  
Title: The adjacent central-tree commutator is a bounded map from the square-root atomic source norm to Cycle-Debt capacity, and actual shifted parity fibers cost only logarithmically  
Status: **PROPOSED COMPLETE EXACT/ANALYTIC LEMMA**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-08  
Dependencies: PR #272 `L-27205/L-27207`; PR #303 `L-30201/L-30202`  
Scope: finite divisor sources and actual critical shifted fibers; no assertion about the completeness of a particular boundary manifest

## 1. Adjacent-tree source map

Let

\[
E_h=T_{h+1}-T_h
\qquad(h\ge1)
\]

be the adjacent central-tree commutator.  PR #272 proves

\[
L_q(E_h)=\mathbf1_{q\mid h+1}
\qquad(q\ge2).
\tag{L-30402.1}
\]

For a finite signed divisor source

\[
\sigma=(\sigma_m)_{2\le m\le N},
\]

define

\[
\boxed{
\Phi(\sigma)=\sum_{m=2}^N\sigma_mE_{m-1}.
}
\tag{L-30402.2}
\]

Then exactly

\[
\boxed{
L_q(\Phi(\sigma))
=\sum_{\substack{m\le N\\q\mid m}}\sigma_m.
}
\tag{L-30402.3}
\]

Thus every formal divisor source has a complete balanced split-flow
representative.  No central-capacity matching is required.

## 2. Capacity norm of one commutator

Use the Cycle-Debt weight

\[
\omega_{n,j}=\sum_{q=2}^n\frac{\chi_{n,j}(q)}{\sqrt q},
\qquad
\omega_{n,j}\le2\sqrt n.
\]

Put

\[
W_h=\sum_e\omega_e|E_h(e)|.
\]

The exact recursions of PR #272 are

\[
E_{2r}=[2r+1,r]-[2r,r]+E_r,
\]

\[
E_{2r+1}=[2r+2,r+1]-[2r+1,r]+E_r.
\]

Hence, for `h>=2`,

\[
W_h\le4\sqrt{h+1}+W_{\lfloor h/2\rfloor}.
\tag{L-30402.4}
\]

Since

\[
\frac{\sqrt{\lfloor h/2\rfloor+1}}{\sqrt{h+1}}
\le\sqrt{\frac23}
\qquad(h\ge2),
\]

induction from `E_1=[2,1]` gives the explicit uniform bound

\[
\boxed{
W_h\le24\sqrt{h+1}.
}
\tag{L-30402.5}
\]

The important scale is `sqrt(h)`, not the unweighted `O(log h)` edge count.

## 3. Bounded source-to-flow theorem

Define the critical atomic source norm

\[
\boxed{
\|\sigma\|_{\mathrm{at}}
=\sum_{m=2}^N\sqrt m\,|\sigma_m|.
}
\tag{L-30402.6}
\]

By (L-30402.2) and (L-30402.5),

\[
\boxed{
\mathcal N_\omega(\Phi(\sigma))
\le\|\Phi(\sigma)\|_{\omega,1}
\le24\|\sigma\|_{\mathrm{at}}.
}
\tag{L-30402.7}
\]

This is a source-complete alternative to `SFC`: rather than demand an incoming
positive central edge, realize the uncovered source exactly and pay only its
actual critical capacity norm.

## 4. Paired parity source and the relative switch

For `A>=B>=0`, the paired source

\[
A e_{2k}-B e_{2k+1}
\]

has the carry-equivalent representative

\[
\boxed{
\Psi_k(A,B)
=(A-B)E_{2k-1}+B(S_k-C_k),
}
\tag{L-30402.8}
\]

where

\[
C_k=[4k,2k],
\qquad
S_k=[4k,2k-1].
\]

Only `C_k` is negative in the second term.  Consequently

\[
\boxed{
\mathcal N_\omega(\Psi_k(A,B))
\le24\sqrt{2k}(A-B)+4\sqrt k\,B.
}
\tag{L-30402.9}
\]

If an actual incoming central edge is available, the relative replacement of
PR #303 can reduce this debt further.  Formula (L-30402.9) is unconditional and
already sufficient at the critical exponent.

## 5. Actual shifted fibers are logarithmic

For the actual source coefficients on PR #303,

\[
A_k(q,s)=\frac{(2kq-1)^{-s}}{2k},
\qquad
B_k(q,s)=\frac{((2k+1)q)^{-s}}{2k+1},
\qquad s\ge\frac12,
\]

one has `A_k>=B_k>=0`.  The elementary bound

\[
2kq-1\ge kq
\]

and (L-30402.9) give

\[
\mathcal N_\omega(\Psi_k(A_k,B_k))
\le C q^{-s}k^{-s-1/2}.
\tag{L-30402.10}
\]

Therefore, uniformly for `s>=1/2`,

\[
\boxed{
\sum_{k\le K}
\mathcal N_\omega(\Psi_k(A_k(q,s),B_k(q,s)))
\le C q^{-1/2}(1+\log K).
}
\tag{L-30402.11}
\]

For `s>1/2` the logarithm can be replaced by an absolute constant depending on
`s-1/2`.

Positive finite-difference jets and exact Euler remainders preserve the order
`A_k>=B_k` by `L-30202`.  By linearity, the same bound holds after positive
superposition, with the right side replaced by the corresponding atomic source
norm.

## 6. Why the source-blind `1/n` mutation overprices the proof

The toy source `c_n=1/n` in `R-30202` produces a sibling amount of order `1/n`.
Its capacity cost is order `n^{-1/2}` and is therefore macroscopically large.

The actual critical boundary coefficient contains the additional half-power:

\[
B_k(q,1/2)\asymp q^{-1/2}k^{-3/2}.
\]

After the square-root capacity weight its cost is `q^(-1/2)k^(-1)`, whose
complete `k`-sum is logarithmic.  The zero-defect mutation and the critical
Cycle-Debt theorem are therefore quantitatively different statements.

## 7. Proof boundary

Closed exactly or elementarily:

1. the complete adjacent-commutator source map;
2. the `24 sqrt(h+1)` capacity bound;
3. the bounded atomic-source lift;
4. the paired parity representative;
5. logarithmic debt for every actual shifted critical fiber.

Open:

1. verification that the complete finite Euler/Peano boundary manifest has
   polylogarithmic total atomic norm after common-destination recombination;
2. the resulting all-generation Cycle-Debt estimate;
3. RH.
