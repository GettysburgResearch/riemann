# R-23401 — One-prime parity pairing leaves every narrow Mertens shell

Claim ID: `R-23401`  
Title: For `c>1/2`, adding or deleting one prime factor cannot pair opposite Möbius signs inside the fixed-ratio shell  
Status: **PROVED SCOPE CORRECTION — ELEMENTARY**  
Authoring agent: `gpt56-pro-09-p`  
Created: 2026-08-07  
Dependencies: none  
Scope: terminal or one-variable sign-reversing pairings proposed for `T-23401`

## 1. Shell geometry

Fix

\[
\frac12<c<1,
\qquad x>0,
\]

and let

\[
\mathcal S_c(x)=\{n\in\mathbb N:cx<n\le x\}.
\]

If `n` lies in this shell and `p>=2` is prime, then

\[
pn>pcx>x,
\tag{R-23401.1}
\]

while

\[
\frac np\le\frac x2<cx.
\tag{R-23401.2}
\]

Therefore

\[
\boxed{
pn\notin\mathcal S_c(x),
\qquad n/p\notin\mathcal S_c(x).}
\tag{R-23401.3}
\]

The second statement is relevant when `p` divides `n`; otherwise `n/p` is not an integer anyway.

## 2. Möbius parity consequence

For squarefree `n` and a prime `p` not dividing it,

\[
\mu(pn)=-\mu(n).
\]

For squarefree `n` divisible by `p`,

\[
\mu(n/p)=-\mu(n).
\]

Equations (R-23401.1)--(R-23401.3) show that neither elementary sign reversal remains inside the shell.

Thus there is no involution of the form

```text
n <-> p n
```

or

```text
n <-> n/p
```

which cancels the shell sum internally.

At the first Farey ratio `c=2/3`, this applies exactly to

\[
M(x)-M(2x/3).
\]

## 3. What an internal sign reversal must do

A ratio-preserving replacement

\[
pa\longleftrightarrow qa
\]

may stay in the shell when

\[
c<q/p<c^{-1},
\]

but it removes one prime incidence and adds one. It changes two incidences and therefore **preserves** Möbius parity. It cannot by itself cancel opposite signs.

Every same-shell opposite-sign pairing must alter an odd number of prime incidences. The one-incidence case is excluded by Section 1. Hence the first possible local geometry changes at least three incidences, for example

\[
pa\longleftrightarrow qra,
\qquad
c<{qr\over p}<c^{-1},
\tag{R-23401.4}
\]

or its inverse. This is a genuinely balanced prime-versus-semiprime correlation, not a terminal one-free-variable pairing.

## 4. Consequence for the proof architecture

The terminal Euler theorems on PR #165 correctly control rows with one unrestricted large lattice variable after their continuous pole model is removed. They cannot by themselves cancel the exact Möbius shell of `T-23401`, because a one-prime parity partner exits the shell.

Any completion must therefore retain at least one of:

1. a balanced parity-changing `p <-> qr` common-cell sum;
2. the centered prime-renewal square of `L-23402`;
3. a higher-order signed shell packet before absolute values;
4. a direct physical-space bound for the positive shell Gram.

## 5. Proof boundary

The shell inequalities and parity count are exact and elementary. They do not construct a balanced pairing, do not estimate the shell energy, and do not prove RH.
