# R-30102 — The parent-`4k` sibling switch escapes the finite endpoint

Claim ID: `R-30102`  
Title: PR #301's nonnegative realization of the parity dipole is not an admissible PR #272 flow for the complete top half of the source  
Status: **EXACT FINITE SUPPORT REFUTATION OF `L-29807.1`–`L-29807.6` AS A COMPLETE ENDPOINT FLOW**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Frozen target: PR #301 at `060943ce211f97b59c1ce60e1a74dff8154dceb1`  
Dependencies: PR #272 `L-27205/L-27207`; PR #301 `L-29807`  
Scope: finite balanced-flow admissibility; the unrestricted carry identity at parent `4k` survives

## 1. The finite flow space

At endpoint

\[
X=2Y,
\]

PR #272's balanced fragmentation and Cycle-Debt space contains only split edges

\[
[n,j]
\qquad
\text{with }2\le n\le2Y.
\tag{R-30102.1}
\]

Its complete odd-node source contains the dipoles

\[
e_{2k}-e_{2k+1},
\qquad
1\le k\le Y-1,
\tag{R-30102.2}
\]

through the adjacent-tree commutators `E_(2k)` in `L-27207`.

## 2. The proposed nonnegative switch

`L-29807` realizes one source dipole by comparing the central and nearest-sibling splits

\[
c_k=[4k,2k],
\qquad
s_k=[4k,2k-1].
\tag{R-30102.3}
\]

The unrestricted carry identity

\[
\chi_{s_k}(q)-\chi_{c_k}(q)
=
\mathbf1_{q\mid2k}-\mathbf1_{q\mid2k+1}
\tag{R-30102.4}
\]

is correct. But both edges have parent `4k`.

For every

\[
\frac Y2<k<Y,
\]

one has

\[
\boxed{4k>2Y=X.}
\tag{R-30102.5}

Thus the proposed realizing edges are outside the finite flow space even though the source nodes `2k,2k+1` are inside it.

There are

\[
Y-1-\lfloor Y/2\rfloor
\]

such top-half source dipoles, not one exceptional endpoint row.

## 3. Small exact control

Take

\[
Y=4,
\qquad
X=8,
\qquad
k=3.
\]

The source dipole

\[
e_6-e_7
\]

is a legitimate PR #272 endpoint-8 source. `L-29807` assigns the splits

\[
[12,6],
\qquad
[12,5],
\]

whose parent `12` exceeds the endpoint `8`.

The exact in-endpoint object supplied by PR #272 is instead

\[
E_6=T_7-T_6,
\]

with sparse recursion

\[
E_6=[7,3]-[6,3]+E_3.
\]

It is signed. The parent-`4k` identity does not turn it into a coefficientwise nonnegative endpoint-8 flow.

## 4. Why the parent `4k` is intrinsic to this adjacent switch

For adjacent splits `[n,j-1]` and `[n,j]`, the binomial ratio is

\[
\frac{\binom n{j-1}}{\binom n j}
=
\frac{j}{n-j+1}.
\tag{R-30102.6}

To obtain the divisor dipole between `2k` and `2k+1`, one needs

\[
j=2k,
\qquad
n-j+1=2k+1,
\]

which forces

\[
\boxed{n=4k.}
\tag{R-30102.7
}

Hence this particular one-switch realization cannot simply be moved to a smaller parent while preserving the same exact divisor-source image.

## 5. Impact on the zero-debt claim

`L-29807.6` asserts that summing the parent-`4k` assignments gives a coefficientwise nonnegative flow realizing the complete common odd-commutator tail. Equations (R-30102.5)–(R-30102.7) show that this flow is not an admissible finite endpoint flow on the complete source.

Consequently:

1. the unrestricted local switch identity survives;
2. zero negative capacity debt is valid only for source pairs with `4k<=2Y`;
3. the top-half source must be realized by the signed in-endpoint commutators or another explicit admissible construction;
4. its Cycle Debt cannot be declared zero;
5. the top-half family cannot be placed in the existing finite collar merely by counting it as one first-omitted term.

The following frozen claims therefore fail:

```text
L-29807 complete common-tail flow      FALSE AS STATED
L-29807 zero paired-tail debt          UNPROVEN FOR THE TOP HALF
L-29807 DCD excess polylogarithmic     UNPROVEN
T-29802 as an RH proof                 REJECTED AS WRITTEN
```

## 6. Surviving repair direction

A valid continuation must use one of:

1. an explicit cycle deformation converting the signed `E_(2k)` family into nonnegative in-endpoint flow at controlled capacity cost;
2. a direct source-complete estimate of the paired odd leakage and `E_(2k)` commutators in the exact Cycle-Debt metric;
3. a strict lower-scale route for every top-half dipole.

The unrestricted parent-`4k` identity alone is not such a continuation.
