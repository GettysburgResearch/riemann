# L-32713 — The Q=4 balanced reserve has asymptotic sixteenfold four-adic storage

Claim ID: `L-32713`  
Title: Under the exact dilation `(n,j)->(4n,4j)`, the Q=4 Selberg–Kummer reserve grows by an arbitrarily close to sixteen factor, and its row-normalized form grows by an arbitrarily close to four factor  
Status: **PROPOSED COMPLETE UNCONDITIONAL COFINAL THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-11  
Dependencies: PR #325 `L-32405`; PR #325 `L-32411`  
Scope: deterministic Q=4 reserve storage on balanced integer rows; no claim that the complete product-source block has already been routed into this storage

## 1. Setup

For a Q=4 carry row `e=(n,j)` put

\[
 P_4(e)=P_4(n,j),
 \qquad
 S_4(e)=S_4(n,j),
 \qquad
 R_4(e)=P_4(e)^2-S_4(e).
\]

Assume

\[
 \frac n4\le j\le\frac{3n}{4}.
\]

Then the dilated row

\[
 4e=(4n,4j)
\]

is quarter-balanced at parent `4n`.

## 2. Exact first-moment dilation

PR #325 `L-32411` proves

\[
 \boxed{
 P_4(4n,4j)-4P_4(n,j)
 =\log\frac{\binom{4n}{4j}}{\binom nj^4}
 +3\log4\,\kappa_4(n,j)
 \ge0,
 }
 \tag{L-32713.1}
\]

where `kappa_4` is the number of nontrivial base-four carry levels. Hence

\[
 \boxed{
 P_4(4e)\ge4P_4(e).
 }
 \tag{L-32713.2}
\]

## 3. The forcing fraction tends uniformly to zero

PR #325 `L-32405` gives, uniformly on the complete quarter-balanced cone,

\[
 \frac{S_4(m,l)}{P_4(m,l)^2}
 <\frac{240\log m}{m(\log2)^2}
 \tag{L-32713.3}
\]

for every sufficiently large parent `m`. The right side tends to zero.

Thus for every `delta>0` there is `M_delta` such that

\[
 \boxed{
 R_4(m,l)
 \ge(1-\delta)P_4(m,l)^2
 }
 \tag{L-32713.4}
\]

for every `m>=M_delta` and every quarter-balanced `l`.

## 4. Sixteenfold storage

Fix `epsilon>0` and choose

\[
 \delta=\frac{\epsilon}{16}.
\]

For every sufficiently large quarter-balanced row `e`, apply (L-32713.4) to `4e` and then (L-32713.2):

\[
\begin{aligned}
 R_4(4e)
 &\ge(1-\delta)P_4(4e)^2\\
 &\ge16(1-\delta)P_4(e)^2\\
 &=(16-\epsilon)P_4(e)^2\\
 &\ge(16-\epsilon)R_4(e),
\end{aligned}
\]

because `R_4(e)<=P_4(e)^2`. Therefore

\[
 \boxed{
 \forall\epsilon>0\ \exists N_\epsilon\ \forall n\ge N_\epsilon:
 \quad
 R_4(4n,4j)
 \ge(16-\epsilon)R_4(n,j)
 }
 \tag{L-32713.5}
\]

uniformly for

\[
 n/4\le j\le3n/4.
\]

Equivalently,

\[
 \boxed{
 \liminf_{n\to\infty}
 \inf_{n/4\le j\le3n/4}
 \frac{R_4(4n,4j)}{R_4(n,j)}
 \ge16.
 }
 \tag{L-32713.6}
\]

No assertion that the ratio is at most sixteen is made; the exact first-moment refinement can create additional storage.

## 5. Row-normalized storage

Define the normalized row reserve

\[
 \widetilde R_4(n,j)=\frac{R_4(n,j)}{n+1}.
 \tag{L-32713.7}
\]

From (L-32713.5),

\[
 \frac{\widetilde R_4(4n,4j)}
      {\widetilde R_4(n,j)}
 \ge
 (16-\epsilon)\frac{n+1}{4n+1}.
 \tag{L-32713.8}
\]

The right side tends to `4-epsilon/4`. Hence, for every `eta>0`,

\[
 \boxed{
 \exists N_\eta\ \forall n\ge N_\eta:\quad
 \widetilde R_4(4n,4j)
 \ge(4-\eta)\widetilde R_4(n,j)
 }
 \tag{L-32713.9}
\]

uniformly on the quarter-balanced cone.

This is the proof-facing form for a critical square-root block: a delayed copy from scale `n` to scale `4n` loses the amplitude factor `1/2`, hence the energy factor `1/4`, while the available normalized reserve grows by asymptotically four.

## 6. Finite-depth no-double-spend consequence

Fix `eta in (0,4)`. For every sufficiently large base row and every finite chain

\[
 e,4e,4^2e,\ldots,4^Ke,
\]

iteration of (L-32713.9) gives

\[
 \boxed{
 \widetilde R_4(4^ke)
 \ge(4-\eta)^k\widetilde R_4(e)
 \qquad(0\le k\le K),
 }
 \tag{L-32713.10}
\]

provided every parent lies beyond the common threshold.

Consequently a charge transported from `4^ke` down to `e` with the critical energy weight `4^{-k}` consumes at most

\[
 [4(4-\eta)]^{-k}
\]

of the reserve stored at the top row. The geometric sum is finite and strictly below one after discarding a fixed finite initial collar.

This statement concerns one declared dilation chain. It does not authorize two different product-source terms to spend the same top-row reserve.

## 7. Significance for the Q=4 recurrence

The Q=4 programme already has:

1. an exact coefficient-one all-pass scattering state;
2. a strict `1/2` amplitude delay in the source-renewal coordinate;
3. a cofinal current-inside-reserve inequality;
4. a fixed finite adverse source collar;
5. the finite positive Jordan deformation of `L-32712`.

The present theorem supplies the missing **capacity scaling**: the deterministic balanced reserve grows fast enough under each four-adic lift to pay an entire critical delayed descendant and still retain geometric slack.

The remaining obligation is now an exact source-complete routing theorem which places each term of the finite-deformation product block on one such dilation chain, with no duplicated destination and with the unitary scattering state as the only coefficient-one return.

## 8. Proof boundary

Closed here:

1. asymptotic sixteenfold unnormalized reserve storage;
2. asymptotic fourfold normalized reserve storage;
3. uniformity on every quarter-balanced row;
4. finite-depth geometric capacity along one four-adic chain.

Not closed here:

1. the exact product-source-to-chain routing;
2. independent-frequency no-double-spend across different chains;
3. the final coefficient-one block recurrence;
4. RH.
