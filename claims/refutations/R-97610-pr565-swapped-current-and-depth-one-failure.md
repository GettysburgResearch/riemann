# R-97610 — PR #565's swapped current is not the native positive restriction

Status: **EXACT REFUTATION OF THE PROOF INTERFACE**
RH: unproved.

For an even one-atom source and `r=p^(-1/2)`:

\[
(1,0)-r(1,0)=(1-r,0)\ge0
\]

is the genuine same-channel positive restriction. PR #565 uses

\[
(1,0)-r(0,1)=(1,-r),
\]

which is not a positive paired source. Parity swap belongs to signed observation/placement, not to a positive source subtraction.

The all-history identity also fails at one rough prime. With

\[
s=1-r,\quad\lambda=r,\quad\alpha=r^2,
\]

PR #565's current and recursive subtraction give

\[
sF(x)+\lambda(F(x)+rF(x/p))-\alpha F(x/p)=F(x).
\]

The native one-prime Euler factor is

\[
F(x)-rF(x/p).
\]

Thus the proposed recursion is wrong by `rF(x/p)` at depth one. Repairing `1/40` to `1/42` does not repair this source coefficient.
