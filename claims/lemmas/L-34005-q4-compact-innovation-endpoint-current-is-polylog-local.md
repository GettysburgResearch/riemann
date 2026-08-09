# L-34005 — The Q=4 compact-innovation endpoint current is a fixed-width local generalized-prime sum

Claim ID: `L-34005`  
Title: Every adverse endpoint row of the main-pole-killing Q=4 innovation current collapses to at most three explicit local generalized-prime coefficients and is therefore logarithmic pointwise  
Status: **PROPOSED COMPLETE EXACT / ELEMENTARY THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro-09-v`  
Created: 2026-08-09  
Parent: PR #341  
Dependencies: PR #342 `L-34003`; general prefix/carry identity `L-34001`  
Scope: fixed endpoint children `r=1,2,3`; no global current bound or RH conclusion

## 1. Compact Q=4 innovation source

Retain the one-step compact source of PR #342

\[
 B_\circ(s)=(1-4^{-s})B_4(s)
 ={1-4^{1-s}\over\zeta(s)},
\tag{L-34005.1}
\]

with coefficient sequence `b_circ`, inverse

\[
 A_\circ(s)={\zeta(s)\over1-4^{1-s}},
\]

and generalized-prime sequence

\[
 \boxed{
 \Lambda_\circ(n)
 =\Lambda(n)+(\log4)\sum_{a\ge1}4^a\mathbf1_{n=4^a}.
 }
\tag{L-34005.2}

The exact bare-source collapse is

\[
 \boxed{
 \mathbf1*b_\circ=\varepsilon-4\delta_4.
 }
\tag{L-34005.3}

Define its first source current

\[
 q_\circ=b_\circ*\Lambda_\circ=-b_\circ\log.
\tag{L-34005.4}

Convolving (L-34005.4) with `1` and using (L-34005.3) gives

\[
 \boxed{
 \mathbf1*q_\circ
 =c_\circ
 :=(\varepsilon-4\delta_4)*\Lambda_\circ.
 }
\tag{L-34005.5}

Thus

\[
 \boxed{
 c_\circ(m)
 =\Lambda_\circ(m)
  -4\mathbf1_{4\mid m}\Lambda_\circ(m/4).
 }
\tag{L-34005.6}

## 2. The huge four-adic generalized-prime coefficients cancel exactly

The extra term in (L-34005.2) is exponentially large at `m=4^a`, but it disappears from the compact current after (L-34005.6).

For `a>=2`,

\[
\begin{aligned}
 c_\circ(4^a)
 &=[\log2+(\log4)4^a]
   -4[\log2+(\log4)4^{a-1}]\\
 &=-3\log2.
\end{aligned}
\tag{L-34005.7}

At `m=4`,

\[
 c_\circ(4)=\log2+4\log4=9\log2.
\tag{L-34005.8}

Away from the exact four-adic tower, the extra term of (L-34005.2) is absent, so

\[
 c_\circ(m)
 =\Lambda(m)-4\mathbf1_{4\mid m}\Lambda(m/4)
\tag{L-34005.9}

unless one of `m,m/4` is a four-adic power, already covered above.

Consequently there is an absolute constant `C` such that

\[
 \boxed{
 |c_\circ(m)|\le C\log(2m)
 \qquad(m\ge1).
 }
\tag{L-34005.10}

One may take, for instance, `C=9` from the displayed cases and the elementary bound `Lambda(m)<=log m`.

Moreover `c_circ` is supported only on:

```text
ordinary prime powers;
four times ordinary prime powers;
the four-adic tower (already included in the two preceding descriptions but with the exact cancellation above).
```

No dense Möbius source remains after the prefix convolution.

## 3. A general fixed-child carry identity

Let `f` be any arithmetic sequence and put

\[
 c=\mathbf1*f,
 \qquad
 C_f(x)=\sum_{m\le x}c(m).
\]

For the endpoint split `n=r+(n-r)`, the general prefix/carry identity `L-34001` gives

\[
 \mathcal L_{n,r}(f)
 =C_f(n)-C_f(n-r)-C_f(r).
\]

Therefore

\[
 \boxed{
 \mathcal L_{n,r}(f)
 =\sum_{h=0}^{r-1}c(n-h)
  -\sum_{m=1}^{r}c(m).
 }
\tag{L-34005.11}

This is exact for every fixed positive integer `r<n`.

The endpoint carry row of an arbitrary inverse source is therefore local after one prefix convolution: a child of size `r` samples only the final `r` coefficients of `1*f`, plus one fixed boundary constant.

## 4. Apply to the three adverse Q=4 compact-source rows

PR #342 proves that the bare compact source has favorable carry sign whenever both children are at least four. Hence the only cofinal adverse positions are

\[
 r\in\{1,2,3\}
\]

and their reflections.

Apply (L-34005.11) with `f=q_circ` and use (L-34005.5):

\[
 \boxed{
 Q_\circ(n,r)
 :=\mathcal L_{n,r}(q_\circ)
 =\sum_{h=0}^{r-1}c_\circ(n-h)-C_r,
 }
\tag{L-34005.12]

where the fixed constant is

\[
 C_r=\sum_{m=1}^{r}c_\circ(m).
\]

Thus explicitly

\[
 Q_\circ(n,1)=c_\circ(n)-C_1,
\]

\[
 Q_\circ(n,2)=c_\circ(n)+c_\circ(n-1)-C_2,
\]

\[
 Q_\circ(n,3)=c_\circ(n)+c_\circ(n-1)+c_\circ(n-2)-C_3.
\tag{L-34005.13}

(The closing square bracket in tag `L-34005.12]` is typographical only.)

Equation (L-34005.10) immediately yields

\[
 \boxed{
 |Q_\circ(n,r)|\ll_r\log(2n),
 \qquad r=1,2,3.
 }
\tag{L-34005.14}

The reflected positions `n-r` give the same bound by row symmetry.

## 5. Endpoint block energy is soft

On any logarithmic parent block `e^J<=n<e^(J+1)`, the pointwise endpoint-current bound is

\[
 |Q_\circ(n,r)|\ll_r1+J.
\]

Hence any fixed finite endpoint family has square energy bounded by a polynomial in `J` after the standard compact block normalization. In particular, the three adverse bare-source contacts do **not** carry the RH-scale current obstruction.

This is much stronger than merely routing `[n,r]` through balanced trees: before any tree conversion, their actual source-convolved current has already collapsed to a fixed-width local generalized-prime expression.

## 6. Consequence for the compact-innovation programme

For `B_circ`, the source geometry is now:

```text
both children >=4:
    bare source charge = +3;

one child in {1,2,3}:
    adverse bare source, but first current = O(log n) explicitly;

both children <4:
    finite parent boundary only.
```

Thus a future reflected proof may place the complete cofinal endpoint collar in the polynomial forcing ledger without importing BTP, WSTS, Mertens, or an RH-scale prime estimate.

The remaining RH-bearing current is necessarily an **interior/source-recombined** phenomenon, not an endpoint contact.

## 7. Proof boundary

Closed exactly / elementarily, subject to review:

1. prefix current `1*q_circ=(epsilon-4 delta_4)*Lambda_circ`;
2. cancellation of the exponentially large four-adic generalized-prime coefficients;
3. the fixed-child local carry identity;
4. explicit width-one/two/three endpoint formulas;
5. logarithmic pointwise bound for every cofinal adverse endpoint current;
6. polynomial endpoint block-energy classification.

Still open:

1. the source-complete interior reflected recurrence;
2. domination of the compact interior current by newly created reserve or another conclusion-producing mechanism;
3. RH.
