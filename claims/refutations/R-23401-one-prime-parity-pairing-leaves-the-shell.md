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

An internal pairing may still replace one prime factor by another:

\[
n=pa
\quad\longleftrightarrow\quad
n'=qa.
\]

But this changes at least two prime-factor incidences and requires

\[
c<{q\over p}<c^{-1}.
\]

It is therefore a balanced factor-ratio or Type-II operation, not a terminal one-free-variable operation.

More generally, every same-shell opposite-sign pairing must alter an odd number of prime incidences while preserving the total product inside one fixed ratio window. The one-incidence case is excluded, so the first available geometry is genuinely correlated.

## 4. Consequence for the proof architecture

The terminal Euler theorems on PR #165 correctly control rows with one unrestricted large lattice variable after their continuous pole model is removed. They cannot by themselves cancel the exact Möbius shell of `T-23401`, because a one-prime parity partner exits the shell.

Any completion must therefore retain at least one of:

1. a balanced replacement `p<->q` with the complete signed common-cell sum;
2. the centered prime-renewal square of `L-23402`;
3. a higher-order signed shell packet before absolute values;
4. a direct physical-space bound for the positive shell Gram.

## 5. Proof boundary

The shell inequalities are exact and elementary. They do not prove that a balanced pairing exists, do not estimate the shell energy, and do not prove RH.
