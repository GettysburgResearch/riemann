# L-34002 — The radix-four Q=4 reserve increment is only critical scale

Claim ID: `L-34002`  
Title: Although the deterministic Q=4 reserve itself is quadratic, its exact excess under one radix-four dilation is nonnegative and only `O(n log n)` on the balanced cone  
Status: **PROPOSED COMPLETE UNCONDITIONAL THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-09  
Dependencies: PR #325 `L-32405`, `L-32411`, `L-32414`  
Scope: deterministic Q=4 row reserve scaling; no physical-current domination or RH conclusion

## 1. Reserve increment

For a quarter-balanced integer row

\[
 n\ge4,
 \qquad n/4\le j\le3n/4,
\]

write

\[
 P=P_4(n,j),
 \qquad S=S_4(n,j),
 \qquad R=P^2-S.
\]

At the exact radix-four dilation put

\[
 P^+=P_4(4n,4j),
 \qquad S^+=S_4(4n,4j),
 \qquad R^+=(P^+)^2-S^+.
\]

Define

\[
\boxed{
 \Delta_4R(n,j)=R^+-16R.
}
\tag{L-34002.1}
\]

PR #325 `L-32414` proves

\[
\boxed{
 \Delta_4R(n,j)\ge0
}
\tag{L-34002.2}
\]

on every quarter-balanced row.

The new point is an upper bound of the correct RH-critical size.

## 2. Exact decomposition

Let

\[
\boxed{
 E(n,j)=P^+-4P.
}
\tag{L-34002.3}
\]

`L-32414.3` gives the exact nonnegative formula

\[
\boxed{
 E(n,j)
 =\log\frac{\binom{4n}{4j}}{\binom nj^4}
 +3\log4\,\kappa_4(n,j),
}
\tag{L-34002.4}
\]

where `kappa_4` is the number of nontrivial base-four carry levels.

Expanding (L-34002.1),

\[
\begin{aligned}
\Delta_4R
 &=(4P+E)^2-S^+-16(P^2-S)\\
 &=\boxed{
 8PE+E^2+16S-S^+.
 }
\end{aligned}
\tag{L-34002.5}
\]

All three summands on the final line need not be individually positive, but `L-32414` proves their sum is.

## 3. A logarithmic upper bound for the binomial-ratio innovation

Put

\[
 p=j/n,
 \qquad 0<p<1.
\]

Consider the binomial probability

\[
 b_n=\binom nj p^j(1-p)^{n-j}.
\]

For `p=j/n`, the index `j` is a mode. Indeed the adjacent probability ratios are

\[
 {\Pr(X=j+1)\over\Pr(X=j)}={j\over j+1}<1,
\]

and

\[
 {\Pr(X=j)\over\Pr(X=j-1)}={n-j+1\over n-j}>1.
\]

Since the `n+1` binomial probabilities sum to one,

\[
\boxed{b_n\ge{1\over n+1}.}
\tag{L-34002.6}
\]

For `4n` with the same success probability `p`, the probability of `4j` is at most one:

\[
 \binom{4n}{4j}p^{4j}(1-p)^{4n-4j}\le1.
\]

Dividing by the fourth power of (L-34002.6) gives the completely elementary estimate

\[
\boxed{
 {\binom{4n}{4j}\over\binom nj^4}
 \le(n+1)^4.
}
\tag{L-34002.7}
\]

Therefore

\[
\boxed{
 \log{\binom{4n}{4j}\over\binom nj^4}
 \le4\log(n+1).
}
\tag{L-34002.8}
\]

No Stirling formula is used.

## 4. The four-adic carry count is logarithmic

There is at most one carry indicator at each radix-four level, so

\[
 \kappa_4(n,j)\le\lfloor\log_4n\rfloor.
\]

Hence

\[
 3\log4\,\kappa_4(n,j)
 \le3\log n.
\tag{L-34002.9}
\]

Combining (L-34002.4), (L-34002.8), and (L-34002.9),

\[
\boxed{
 0\le E(n,j)\le7\log(2n).
}
\tag{L-34002.10}
\]

uniformly on the complete quarter-balanced cone.

## 5. Critical-scale upper bound for the reserve increment

PR #325 `L-32405` gives

\[
 P_4(n,j)
 \le\sum_{q\le n}\Lambda_4(q)
 <{10\over3}n
\tag{L-34002.11}
\]

and, for every `n>=4735`,

\[
 0\le S_4(n,j)<15n\log n.
\tag{L-34002.12}
\]

Since `S^+>=0`, equation (L-34002.5) yields

\[
\begin{aligned}
 \Delta_4R
 &\le8PE+E^2+16S\\
 &<{560\over3}n\log(2n)
   +49\log^2(2n)
   +240n\log n.
\end{aligned}
\]

For `n>=2`, `log(2n)<=n`, hence

\[
49\log^2(2n)\le49n\log(2n).
\]

Therefore, uniformly for every quarter-balanced row with `n>=4735`,

\[
\boxed{
 0\le\Delta_4R(n,j)
 <480\,n\log(2n).
}
\tag{L-34002.13}
\]

The constant is deliberately loose; the scale is the important conclusion.

## 6. Why this is structurally important

The full Q=4 reserve has the deterministic cofinal size

\[
 R_4(n,j)\gg n^2.
\]

Its one-step radix-four increment instead has only the critical fluctuation scale

\[
\boxed{
 \Delta_4R(n,j)=O(n\log n).
}
\tag{L-34002.14}
\]

Thus a proof which can charge the RH-sensitive Q=4 current to the **new reserve created at one radix-four scale**, rather than repeatedly to the entire quadratic reserve, automatically lands on the square-root physical scale after the standard `X^{-1/2}` normalization.

This is exactly aligned with the coefficient-one neutral recurrence: the inherited reserve `16R(n,j)` is carried to the delayed state, while only `Delta_4R` is available to pay the current-scale innovation.

## 7. Proof-closing but unproved strengthening

The natural strengthening suggested by the new scale law is

\[
\boxed{
 |Q_4^{\rm phys}(4n,4j)|^2
 \le C\,\Delta_4R(n,j)
}
\tag{L-34002.15}
\]

with an absolute `C` outside a fixed finite base.

By (L-34002.13), such a theorem would give

\[
 |Q_4^{\rm phys}(4n,4j)|^2=O(n\log n),
\]

which is RH-strength after critical normalization. Equation (L-34002.15) is **not proved here**.

The point of this lemma is to identify an exact deterministic budget of the right size, not to infer the arithmetic domination from the size comparison.

## 8. Proof boundary

Closed exactly, subject to review:

1. reserve-increment identity (L-34002.5);
2. elementary binomial-ratio bound (L-34002.7);
3. uniform logarithmic first-moment innovation (L-34002.10);
4. nonnegative critical-scale reserve increment (L-34002.13).

Open:

1. domination of the physical current by the reserve increment;
2. the coefficient-one reflected/scattering recurrence;
3. RH.
