# L-34005 — The radix-four Q=4 reserve increment has a uniform critical moat

Claim ID: `L-34005`  
Title: On the complete quarter-balanced cone, the new deterministic Q=4 reserve created by one exact radix-four dilation is `Theta(n log n)` cofinally  
Status: **PROPOSED COMPLETE UNCONDITIONAL COFINAL THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-09  
Dependencies: PR #325 `L-32405/L-32411/L-32414`; `L-34002`; elementary Stirling bounds  
Scope: deterministic Q=4 reserve increment only; no physical-current domination or RH conclusion

## 1. Setup

For a quarter-balanced row

\[
 n/4\le j\le3n/4,
\]

put

\[
 P=P_4(n,j),\qquad S=S_4(n,j),\qquad R=P^2-S,
\]

and define

\[
\Delta_4R(n,j)=R_4(4n,4j)-16R_4(n,j).
\tag{L-34005.1}
\]

Let

\[
E(n,j)=P_4(4n,4j)-4P_4(n,j).
\tag{L-34005.2}
\]

PR #325 gives

\[
S_4(4n,4j)\le16S_4(n,j),
\]

so the exact expansion from `L-34002` yields

\[
\boxed{
\Delta_4R
=8PE+E^2+16S-S^+
\ge8PE.
}
\tag{L-34005.3}
\]

Thus it suffices to prove a logarithmic lower bound for the radix-four first-moment innovation `E`.

## 2. Binomial-ratio form of the innovation

PR #325 `L-32411` proves

\[
\boxed{
E(n,j)
=\log\frac{\binom{4n}{4j}}{\binom nj^4}
 +3\log4\,\kappa_4(n,j),
}
\tag{L-34005.4}
\]

where the carry count `kappa_4` is nonnegative. Hence

\[
E(n,j)\ge
\log\frac{\binom{4n}{4j}}{\binom nj^4}.
\tag{L-34005.5}
\]

Put

\[
p=j/n,\qquad q=1-p.
\]

The quarter-balanced assumption gives

\[
pq\ge3/16.
\tag{L-34005.6}
\]

Define the binomial mode probabilities

\[
b_n=\binom njp^jq^{n-j},
\qquad
b_{4n}=\binom{4n}{4j}p^{4j}q^{4n-4j}.
\]

Then exactly

\[
\frac{\binom{4n}{4j}}{\binom nj^4}
=\frac{b_{4n}}{b_n^4}.
\tag{L-34005.7}
\]

## 3. Elementary bounds for the two mode probabilities

Since `4j` is a mode of the binomial distribution `Bin(4n,p)`, its probability is at least the average of its `4n+1` probabilities:

\[
\boxed{
b_{4n}\ge{1\over4n+1}.}
\tag{L-34005.8}
\]

For the upper bound on `b_n`, use the elementary Stirling inequalities

\[
m!\ge \sqrt m\,(m/e)^m\qquad(m\ge1),
\]

and

\[
n!\le e\sqrt n\,(n/e)^n.
\]

They give

\[
\begin{aligned}
b_n
&=\frac{n!}{j!(n-j)!}
   \left(\frac jn\right)^j
   \left(\frac{n-j}{n}\right)^{n-j}\\
&\le e\sqrt{\frac n{j(n-j)}}
 =\frac e{\sqrt{npq}}.
\end{aligned}
\]

Using (L-34005.6),

\[
\boxed{
b_n\le {4e\over\sqrt{3n}}<{7\over\sqrt n}.}
\tag{L-34005.9}
\]

The deliberately loose rational constant `7` avoids any need for a sharp Stirling constant.

## 4. Polynomial growth of the binomial ratio

Combining (L-34005.7)--(L-34005.9),

\[
\frac{\binom{4n}{4j}}{\binom nj^4}
\ge
\frac{n^2}{2401(4n+1)}.
\]

Since `4n+1<=5n` for `n>=1`,

\[
\boxed{
\frac{\binom{4n}{4j}}{\binom nj^4}
\ge {n\over12005}.
}
\tag{L-34005.10}
\]

Therefore

\[
\boxed{
E(n,j)\ge\log n-\log12005.
}
\tag{L-34005.11}
\]

uniformly on the full quarter-balanced cone.

In particular, for

\[
n\ge N_0:=12005^2,
\]

one has

\[
\boxed{E(n,j)\ge\frac12\log n.}
\tag{L-34005.12}
\]

The threshold is intentionally crude and finite.

## 5. Uniform `n log n` lower moat

PR #325 gives on the quarter-balanced cone

\[
P_4(n,j)\ge {n\over4}\log2.
\tag{L-34005.13}
\]

Insert (L-34005.12)--(L-34005.13) into (L-34005.3):

\[
\Delta_4R(n,j)
\ge
8\left({n\log2\over4}\right)
\left({\log n\over2}\right).
\]

Hence, for every `n>=N_0` and every quarter-balanced `j`,

\[
\boxed{
\Delta_4R(n,j)
\ge (\log2)\,n\log n.
}
\tag{L-34005.14}
\]

Together with `L-34002`, which gives

\[
\Delta_4R(n,j)<480n\log(2n),
\]

we obtain the two-sided cofinal scale law

\[
\boxed{
(\log2)n\log n
\le\Delta_4R(n,j)
<480n\log(2n)
}
\tag{L-34005.15}
\]

uniformly over the complete quarter-balanced cone.

## 6. Consequence for the proof search

The one-step reserve budget cannot collapse on a sparse family of balanced rows. It is uniformly of the exact critical order `n log n`.

Therefore the discovery inequalities from `O-34001`, if true, do not exploit a huge quadratic moat. They would place the RH-sensitive current/innovation inside a deterministic reserve of the same scale as the conjectural square-root fluctuation energy.

This sharpens the closing target to a dimensionless uniform statement such as

\[
\sup_{n,j}
\frac{|I_4(n,j)|^2}{\Delta_4R(n,j)}<\infty
\]

outside a fixed finite base. Such a theorem is still RH-bearing and is **not** inferred here.

## 7. Proof boundary

Closed unconditionally, subject to review:

1. the lower identity `Delta_4R>=8PE`;
2. the polynomial binomial-ratio lower bound;
3. the logarithmic first-moment innovation moat;
4. the uniform `Omega(n log n)` reserve increment;
5. together with `L-34002`, the two-sided `Theta(n log n)` scale law.

Open:

1. a current/innovation domination by this reserve;
2. the coefficient-one neutral recurrence;
3. RH.
