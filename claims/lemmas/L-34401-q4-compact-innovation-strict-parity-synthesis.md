# L-34401 — The compact Q=4 innovation has a strict parity-frame synthesis

Claim ID: `L-34401`  
Title: A quadratic Bézout cycle reconstructs the Q=4 compact innovation with critical current-synthesis charge below two fifths of the parity-frame reserve, and differentiation creates only strict-delay gauges  
Status: **PROPOSED COMPLETE EXACT FINITE-FILTER THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-09  
Dependencies: PR #263 `L-26205/L-26206`; PR #342 `L-34003`; elementary polynomial algebra  
Scope: exact compact-source/current synthesis and critical filter budget; no global delayed-state recurrence or RH conclusion

## 1. Sources

Put

\[
z=2^{-s},
\qquad
\mathcal O(s)=\prod_{p\ {m odd}}(1-p^{-s}),
\]

and retain the parity analysis polynomial

\[
 p(z)=(1-z)(1-2z)(1-\sqrt2 z)^2.
\]

The two parity sources are

\[
 B_+(s)=p(z)\mathcal O(s),
\qquad
 B_-(s)=p(-z)\mathcal O(s).
\tag{L-34401.1}
\]

PR #263 proves the exact frame reserve

\[
\boxed{|p(z)|^2+|p(-z)|^2\ge {45\over4}}
\tag{L-34401.2}
\]

throughout the closed critical annulus

\[
{1\over2}\le|z|\le {1\over\sqrt2}.
\]

The compact Q=4 innovation source of PR #342 is

\[
 B_\circ(s)
 ={1-4^{1-s}\over\zeta(s)}.
\]

Since

\[
{1\over\zeta(s)}=(1-z)\mathcal O(s),
\]

its odd-core numerator is the degree-three polynomial

\[
\boxed{
T(z)=(1-z)(1-4z^2),
\qquad
B_\circ(s)=T(z)\mathcal O(s).
}
\tag{L-34401.3}
\]

Thus the live Q=4 compact innovation and the live parity frame are finite polynomial sources over the **same** odd Euler core.

## 2. Bézout cycle freedom

PR #263 gives

\[
 U(z)p(z)+U(-z)p(-z)=1,
\tag{L-34401.4}
\]

where

\[
\begin{aligned}
U(z)={}&{1\over2}
+\left(-{11\over3}+{7\sqrt2\over2}\right)z
+\left(1+{\sqrt2\over6}\right)z^2\\
&+\left({14\over3}-3\sqrt2\right)z^3.
\end{aligned}
\tag{L-34401.5}
\]

For any polynomial `H`, define

\[
\boxed{
\begin{aligned}
W_+(z)&=T(z)U(z)+H(z)p(-z),\\
W_-(z)&=T(z)U(-z)-H(z)p(z).
\end{aligned}}
\tag{L-34401.6}
\]

Then the cycle terms cancel exactly and

\[
\boxed{
W_+(z)p(z)+W_-(z)p(-z)=T(z).
}
\tag{L-34401.7}
\]

This is genuine synthesis freedom, not an approximation.

## 3. An explicit strict certificate

Take

\[
H(z)=h_0+h_1z+h_2z^2
\tag{L-34401.8}
\]

with

\[
\boxed{
\begin{aligned}
h_0&=-{2525\over1511238}+{264889\sqrt2\over3022476},\\
h_1&={15421\over3174}-{6805\sqrt2\over2116},\\
h_2&=-{3767648\over755619}+{4893731\sqrt2\over1511238}.
\end{aligned}}
\tag{L-34401.9}
\]

The coefficients are merely one exact certificate; no optimality claim is needed.

Write

\[
W_\pm(z)=\sum_{j=0}^{6}w_{\pm,j}z^j.
\]

On the critical line, multiplication by `z^j` is a delay of `j log 2` with squared amplitude `2^{-j}`. Define the complete two-channel critical Cauchy charge

\[
 q_W
 =\sum_{j=0}^{6}
 (w_{+,j}^2+w_{-,j}^2)2^{-j}.
\tag{L-34401.10}
\]

Exact simplification in `Q(sqrt(2))` gives

\[
\boxed{
 q_W
 ={231285439+37590283\sqrt2\over69516948}
 =4.0917522304\ldots .
}
\tag{L-34401.11}
\]

Moreover

\[
\boxed{q_W<{9\over2}.}
\tag{L-34401.12}
\]

Indeed

\[
{9\over2}-q_W
={81540827-37590283\sqrt2\over69516948}>0,
\]

and the last numerator is positive because

\[
81540827^2-2\cdot37590283^2
=3822847715803751>0.
\]

Combining (L-34401.2) and (L-34401.12),

\[
\boxed{
 {q_W\over45/4}<{2\over5}.
}
\tag{L-34401.13}
\]

Thus the compact Q=4 source has a finite parity synthesis whose complete critical coefficient-square charge is strictly below two fifths of the fixed parity-frame reserve.

## 4. Source reconstruction

Substituting `z=2^{-s}` into (L-34401.7) gives the exact Dirichlet-source identity

\[
\boxed{
 B_\circ(s)
 =W_+(2^{-s})B_+(s)
 +W_-(2^{-s})B_-(s).
}
\tag{L-34401.14}
\]

All delays are at most `6 log 2`. There is no infinite inverse and no division by a vertical-line multiplier.

For block energies

\[
E_m=\int_{I_m}(|B_+(x)|^2+|B_-(x)|^2)\,dx,
\qquad
I_m=[m\log2,(m+1)\log2],
\]

ordinary Hilbert-space Cauchy--Schwarz gives the corresponding finite-delay source estimate with coefficient budget `q_W`.

## 5. Differentiate: the current gauge is strictly delayed

Let

\[
q_\circ=B_\circ',
\qquad q_\pm=B_\pm'.
\]

Since

\[
{d\over ds}W_\pm(2^{-s})
=-(\log2)zW_\pm'(z),
\]

differentiating (L-34401.14) gives exactly

\[
\boxed{
\begin{aligned}
q_\circ={}&W_+(z)q_+ +W_-(z)q_-\\
&-(\log2)z
\bigl[W_+'(z)B_+ +W_-'(z)B_-\bigr].
\end{aligned}}
\tag{L-34401.15}
\]

The first line is the current synthesis. Its critical weighted square charge is exactly `q_W<2/5*(45/4)`.

The second line is the complete derivative gauge. It contains an explicit factor `z`. Hence

\[
\boxed{
\text{every gauge term is delayed by at least one }\log2\text{ block.}
}
\tag{L-34401.16}
\]

There is **no zero-delay current gauge**.

This is stronger than synthesizing the full inverse-zeta current and only afterwards applying the Q=4 high-pass: the main-pole-killing polynomial has been included before the Bézout cycle is optimized.

## 6. Optional exact gauge-size firewall

Define the derivative coefficient-square budget

\[
 q_G
 =\sum_{j=1}^{6}j^2
 (w_{+,j}^2+w_{-,j}^2)2^{-j}.
\tag{L-34401.17}
\]

The exact value is

\[
\boxed{
q_G
={37975436343937653-9118218201662324\sqrt2
 \over2416303029617352}
< {21\over2}.
}
\tag{L-34401.18}
\]

For example the final inequality follows from

\[
2(9118218201662324)^2-(12604254532955457)^2
=7416574014724026340238696083103>0.
\]

Since `(log 2)^2<1/2`, the purely filter-theoretic direct-sum coefficient budget obeys

\[
 q_W+(\log2)^2q_G
 <q_W+{q_G\over2}
 <{45\over4}.
\tag{L-34401.19}
\]

Equation (L-34401.19) is only a coefficient-budget firewall. It does **not** authorize spending one Selberg reserve twice on current and bare-source species. The useful production statement is the strict current-scale bound (L-34401.13) together with the strict delay (L-34401.16).

## 7. Connection to the actual Q=4 current innovation

PR #342 proves the exact source identity

\[
(\varepsilon-\delta_4)q_4
=q_\circ-(\log4)\delta_4*b_4.
\tag{L-34401.20}
\]

In critically normalized physical coordinates every `delta_4` term is a strict delay by `log 4`. Therefore combining (L-34401.15) and (L-34401.20) gives the complete source classification

```text
current scale:
    finite parity-current synthesis, charge < 2/5 of the fixed frame reserve;

strictly earlier blocks:
    the parity bare-source derivative gauge;
    the explicit Q=4 bare-source gauge.
```

Thus the **balanced compact innovation has no unsynthesized current-scale source left**. The remaining obstruction is a delayed-state/reflected-ledger problem, not a current-scale arithmetic transference problem.

## 8. What this closes and what remains

Closed exactly in this lemma:

1. finite source reconstruction of `B_circ` from the parity pair;
2. an explicit quadratic cycle certificate;
3. strict critical current-synthesis charge `<2/5`;
4. exact derivative identity;
5. absence of every zero-delay derivative gauge;
6. composition with the live Q=4 compact innovation source.

Not closed:

1. source-convolved reflected accounting of the delayed parity bare-source gauge;
2. joint accounting with PR #341's terminal Q=4 state without double spending;
3. the final coefficient-one block recurrence;
4. RH.

A reviewer should verify the finite polynomial identities and exact inequalities above. No missing delayed-state recurrence is delegated as an exercise.
