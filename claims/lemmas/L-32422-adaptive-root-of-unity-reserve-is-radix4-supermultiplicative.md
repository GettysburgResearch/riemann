# L-32422 — Adaptive root-of-unity reserve is radix-four supermultiplicative

Claim ID: `L-32422`  
Title: Once the finite root-of-unity frame separates all active four-adic levels, its exact Hermitian Selberg reserve grows by at least sixteen under one radix-four dilation  
Status: **PROPOSED COMPLETE EXACT THEOREM — ANALYTIC ORDINARY PART + FINITE SMALL-ROW GATE; INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-09  
Dependencies: `L-32421`; `L-32414` ordinary fourfold slack argument; ordinary Selberg–Kummer identity  
Scope: endpoint-adaptive direct-sum reserve; no RH conclusion by itself

## 1. Separated multichannel reserve

Fix an integer endpoint `n>=4` and a quarter-balanced split `n=j+k`. Let

\[
R=\lfloor\log_4 n\rfloor.
\]

Choose an integer

\[
\boxed{M>2(R+1).}
\tag{L-32422.1}
\]

This slightly stronger condition than `L-32421` separates all active four-adic levels both at `(n,j)` and at the scaled row `(4n,4j)`.

By `L-32421`, after root-of-unity Fourier orthogonalization the Hermitian first-moment energy at `(n,j)` is

\[
P_{\rm ord}(n,j)^2
+\sum_{4^r\le n}d_r^2c_r,
\qquad
 d_r=4^r\log4,
\quad
 c_r=\chi_{n,4^r}(j),
\]

while the complete averaged Selberg forcing is exactly the ordinary forcing `S_ord(n,j)`. Therefore

\[
\boxed{
R_M(n,j)
=R_{\rm ord}(n,j)
 +\sum_{4^r\le n}d_r^2c_r,
}
\tag{L-32422.2}
\]

where

\[
R_{\rm ord}=P_{\rm ord}^2-S_{\rm ord}\ge0.
\]

No mixed local arithmetic remains in this formula.

## 2. Exact scaling of the local-square sector

At the aligned scaled row `(4n,4j)`, the radix-four carry digits satisfy

\[
 c'_1=0,
 \qquad
 c'_{r+1}=c_r
 \quad(r\ge1).
\tag{L-32422.3}
\]

Since

\[
 d_{r+1}=4d_r,
\]

one gets exactly

\[
\boxed{
\sum_{4^s\le4n}d_s^2c'_s
=16\sum_{4^r\le n}d_r^2c_r.
}
\tag{L-32422.4}

Thus the entire local source storage scales by exactly sixteen.

## 3. Ordinary first moment scales by at least four

Ordinary Kummer gives

\[
P_{\rm ord}(n,j)=\log\binom nj.
\]

Choosing `j` elements independently from each of four disjoint `n`-blocks injects into the set of all `4j`-subsets of a `4n`-set, so

\[
\binom{4n}{4j}\ge\binom nj^4.
\]

Hence

\[
\boxed{
P_{\rm ord}(4n,4j)\ge4P_{\rm ord}(n,j).
}
\tag{L-32422.5}

## 4. Ordinary second moment scales by at most sixteen

Let

\[
S_{\rm ord}(n,j)
=H_2(n)-H_2(j)-H_2(k),
\qquad
H_2(N)=\sum_{m=1}^{N}\log^2m.
\]

The grouped fourfold estimate in the proof of `L-32414`, Sections 3–4, is an ordinary-zeta statement independent of the Q=4 local correction. For every balanced row with `k>=6` it proves the stronger inequality

\[
\boxed{
16S_{\rm ord}(n,j)-S_{\rm ord}(4n,4j)
\ge12\log2\,P_{\rm ord}(n,j)>0.
}
\tag{L-32422.6}

For completeness, if `j<=k<=5`, quarter balance leaves the same eleven rows listed in `L-32414`. The exact directed logarithm replay `X-32414` already evaluates the ordinary grouped part before the local Q=4 terms are added; its ordinary margins are all strictly positive. Equivalently those eleven finite inequalities can be replayed directly from `H_2` with the same rational atanh enclosures.

Therefore, on every quarter-balanced row,

\[
\boxed{
S_{\rm ord}(4n,4j)\le16S_{\rm ord}(n,j).
}
\tag{L-32422.7}

## 5. Ordinary reserve is radix-four supermultiplicative

Combining (L-32422.5) and (L-32422.7),

\[
\begin{aligned}
R_{\rm ord}(4n,4j)
&=P_{\rm ord}(4n,4j)^2-S_{\rm ord}(4n,4j)\\
&\ge16P_{\rm ord}(n,j)^2-16S_{\rm ord}(n,j)\\
&=16R_{\rm ord}(n,j).
\end{aligned}
\]

Thus

\[
\boxed{
R_{\rm ord}(4n,4j)\ge16R_{\rm ord}(n,j).
}
\tag{L-32422.8}

This is an exact deterministic entropy inequality; no prime estimate enters.

## 6. Complete adaptive-frame scaling

Use (L-32422.2), (L-32422.4), and (L-32422.8):

\[
\begin{aligned}
R_M(4n,4j)
&=R_{\rm ord}(4n,4j)
 +16\sum_r d_r^2c_r\\
&\ge16R_{\rm ord}(n,j)
 +16\sum_r d_r^2c_r\\
&=16R_M(n,j).
\end{aligned}
\]

Therefore

\[
\boxed{
R_M(4n,4j)\ge16R_M(n,j).
}
\tag{L-32422.9}

The same endpoint-adaptive channel count `M>2(R+1)` is valid simultaneously at the two compared scales. The normalized critical frame constant remains exactly five by `L-32421`, independent of `M`.

## 7. Why this is useful

The direct-sum construction now has four exact properties simultaneously:

```text
all active local levels separated;
all mixed local Selberg forcing removed;
critical frame constant = 5 independent of channel count;
complete reserve scales >=16 under the exact radix-four dilation.
```

Thus neither local-source collision nor reserve degeneration is intrinsic to the final RH obstruction. A future reflected proof may work in this endpoint-adaptive finite direct sum and focus solely on the principal reciprocal-zeta current and its delayed frame state.

This theorem does not itself control that principal current. The adaptive channel bank is a finite proof coordinate, not an unconditional RH estimate.

## 8. Proof boundary

Closed exactly, subject to independent review:

1. separated reserve formula (imported from `L-32421`);
2. exact sixteenfold local-square scaling;
3. fourfold ordinary Kummer scaling;
4. sixteenfold ordinary Selberg upper scaling;
5. sixteenfold ordinary reserve scaling;
6. sixteenfold complete adaptive-frame reserve scaling.

Still open:

1. source-convolved independent-frequency no-double-spend placement of the principal current;
2. coefficient-one delayed recurrence;
3. RH.
