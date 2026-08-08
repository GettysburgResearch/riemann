# L-24524 — Negative variation is the only cost of central-Neumann saturation

Claim ID: `L-24524`  
Status: **PROPOSED COMPLETE REDUCTION; CNVD RATE OPEN**  
Scope: signed-to-sharp adapter for `L-24523`  
Issue: #245  
Date: 2026-08-08

Let `A_X(n)` be the exact central-Neumann coefficients of `L-24523`.

Define their square-root weighted negative variation by

\[
\boxed{
\mathcal V_X^-
=\sum_{n=2}^{X}\sqrt n\,(-A_X(n))_+.
}
\tag{L-24524.1}
\]

The purpose of this file is to prove that **only** this negative ledger needs to be bounded. The positive weighted variation then follows automatically from the exact carry load.

## 1. Every central row has square-root carry mass

Put

\[
W_n=\sum_{q=2}^{n}q^{-1/2}\chi_n^{\rm c}(q).
\tag{L-24524.2}
\]

For the central split, every integer

\[
q>\max(\lfloor n/2\rfloor,\lceil n/2\rceil)
\]

has parent floor equal to one and both child floors equal to zero. Hence `chi_n^c(q)=1` on the full terminal interval

\[
\lfloor n/2\rfloor+1<q\le n
\]

up to one harmless endpoint convention. Therefore there are absolute constants `0<c_0<C_0` such that

\[
\boxed{
c_0\sqrt n\le W_n\le C_0\sqrt n
\qquad(n\ge2).}
\tag{L-24524.3}
\]

For example, the upper bound follows from

\[
\sum_{q\le n}q^{-1/2}\le2\sqrt n,
\]

and any fixed `c_0<2(1-2^{-1/2})` works after adjusting finitely many small `n`.

## 2. Exact signed weighted load

Multiply the exact saturation identity `L-24523.11` by `q^{-1/2}` and sum over `q`. Finite interchange gives

\[
\boxed{
\sum_{n=2}^{X}A_X(n)W_n
=\sum_{q=2}^{X}{1\over q}\log{X\over q}.
}
\tag{L-24524.4}
\]

Elementary integral comparison gives

\[
\boxed{
0\le
\sum_{q=2}^{X}{1\over q}\log{X\over q}
\ll(\log X)^2.
}
\tag{L-24524.5}
\]

Write

\[
P_W=\sum_n(A_X(n))_+W_n,
\qquad
N_W=\sum_n(-A_X(n))_+W_n.
\]

Then (L-24524.4) says `P_W-N_W=O(log^2 X)`. By (L-24524.3),

\[
N_W\le C_0\mathcal V_X^-,
\]

and therefore

\[
P_W\ll(\log X)^2+\mathcal V_X^-.
\]

Using the lower side of (L-24524.3),

\[
\sum_n\sqrt n\,(A_X(n))_+
\ll(\log X)^2+\mathcal V_X^-.
\]

Adding the negative part proves

\[
\boxed{
\sum_{n=2}^{X}\sqrt n\,|A_X(n)|
\ll(\log X)^2+\mathcal V_X^-.
}
\tag{L-24524.6}
\]

Thus a one-sided negative-variation theorem automatically supplies the complete weighted total variation.

## 3. Central-Neumann Variation Descent (CNVD)

The load-bearing theorem is now the scalar estimate

\[
\boxed{
\textbf{CNVD:}\qquad
\mathcal V_X^-=X^{o(1)}.
}
\tag{L-24524.7}
\]

Equivalently, for every `epsilon>0`,

\[
\mathcal V_X^-\ll_\epsilon X^\epsilon.
\]

Under CNVD, (L-24524.6) gives

\[
\sum_n\sqrt n\,|A_X(n)|=X^{o(1)}.
\tag{L-24524.8}
\]

Combining `L-24523.15`--`L-24523.17` with the local bound `|ell_n-c_n|<<sqrt(n)` yields

\[
\boxed{
\mathcal P(X)=4\sqrt X+X^{o(1)}.
}
\tag{L-24524.9}
\]

In particular

\[
\mathcal P(X)\ge4\sqrt X-X^{o(1)},
\]

the sharp lower bound consumed by the repository's square-screw/Landau theorem.

## 4. A sufficient recursive form

The exact support descent of `L-24523` suggests a stronger, directly inductive form. It is enough to prove that there exist absolute constants `A,C` such that

\[
\boxed{
\mathcal V_X^-
\le
\mathcal V_{\lfloor(X+1)/2\rfloor}^-
+C(1+\log X)^A
}
\tag{L-24524.10}
\]

for every sufficiently large `X`, after identifying the lower-scale target with the complete dyadic shell before positive/negative separation.

Iteration gives

\[
\mathcal V_X^-=O((\log X)^{A+1}).
\tag{L-24524.11}
\]

The phrase “complete dyadic shell” is load-bearing. The identity

\[
w_X(q)-w_Y(q)=q^{-1/2}\log(X/Y)
\]

cannot be estimated termwise: the boundary response of `q^{-1/2}` contains the reciprocal-zeta mode. The required recurrence must combine the upper shell and the lower target before taking negative parts. This is the same cancellation forced by the prime-density-drift correction and by canonical WSTS.

## 5. Connection to WSTS and the dyadic source

The newest repository consolidation proves that the logarithmically weighted dyadic shell-tail theorem `WSTS` is equivalent to RH. Therefore (L-24524.10) must not be advertised as a routine consequence of scale support alone.

The central-Neumann construction nevertheless changes the production problem in a useful way:

1. **all finite carry geometry is explicit** — no LP or unknown deformation remains;
2. **every unsatisfied stage descends by a factor two exactly**;
3. **only negative row variation costs anything**;
4. **the positive row mass is automatically paid by the `O(log^2 X)` weighted carry load**;
5. the remaining shell theorem acts on one deterministic coefficient sequence `A_X`, rather than on an existential family of signed flows.

A proof of WSTS may therefore be supplied constructively by proving (L-24524.10) for this one Neumann sequence.

## 6. Relation to constraint-dipole transport

`L-25301` shows that the parabolic seed has `Omega(sqrt X)` positive and negative von-Mangoldt weighted defect masses. A monotone cover fails because it deletes the positive side instead of transporting it.

The finite Neumann series performs a canonical signed transport:

\[
f_r\longmapsto
\Delta f_r\text{ on central rows}
\quad+\quad
f_{r+1}=T_Xf_r,
\]

with `supp(f_{r+1})` at half scale. Positive and negative coefficient creation is therefore organized by a fixed factor-two cascade. CNVD asks only that the **negative part of the completed cascade**, after all scales recombine, have subpower square-root mass.

This is strictly different from the refuted monotone Divisibility Cover, which required every correction atom to be nonnegative before signed recombination.

## 7. Nonnegative certificate after CNVD

CNVD first gives the sharp prime-ramp lower bound through the signed exact ledger. The branch already contains two finite adapters relevant after that scalar is known:

- proper prime powers cost only `O(log^2 X)` (`L-24517`);
- the ordinary-prime finite positivity geometry has zero additional geometric tax in the later affine deformation work imported by the repository consolidation.

Thus CNVD may be read either as a direct signed proof of the prime-ramp theorem or as the source estimate feeding a final nonnegative finite carry certificate. No monotone `sqrt(X)`-cost cover is reintroduced.

## 8. Firewall

A proof of CNVD is not permitted to use any of the following shortcuts:

- take `|T_Xf|` before the dyadic shell recombination;
- bound the response of `q^{-1/2}` separately from the upper shell;
- infer contraction from finite nilpotence;
- infer a cofinal rate from finite coefficient scans;
- use the unweighted ordinary-prime queue refuted by the density drift;
- discard the logarithmic/von-Mangoldt dual ray.

The continuum multiplier in `L-24523` shows exactly why these shortcuts fail.

## Proof boundary

Proved here:

- square-root lower and upper carry mass of every central row;
- exact signed weighted-load identity;
- one-sided negative variation controls full weighted variation;
- CNVD implies the sharp prime ramp and hence, through the existing consumer, RH;
- the displayed half-scale recurrence is sufficient for a polylogarithmic CNVD rate.

Open:

- unconditional CNVD or the recursive shell estimate (L-24524.10);
- RH.
