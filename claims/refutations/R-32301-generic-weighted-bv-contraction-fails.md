# R-32301 — Generic weighted-BV contraction of the central residual is false

Claim ID: `R-32301`  
Title: The central residual can increase the natural square-root weighted adjacent variation even at endpoint nine  
Status: **EXACT FINITE REFUTATION**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-08  
Scope: rejects an ambient weighted-variation contraction; source-specific variation estimates remain possible

## 1. The tempting norm

For a finitely supported sequence `h`, define

\[
V(h)=\sum_{n\ge2}\sqrt n\,|h(n+1)-h(n)|.
\tag{R-32301.1}
\]

For endpoint `X`, let the exact finite central residual be

\[
(\mathcal T_Xh)(q)
=\sum_{k\ge1}
[h(2kq-1)-h((2k+1)q)],
\tag{R-32301.2}
\]

with zero extension outside `2<=n<=X`.

A universal estimate

\[
V(\mathcal T_Xh)\le\rho V(h),\qquad \rho<1,
\]

would close many boundary-cascade proposals.  It is false.

## 2. Endpoint-nine counterexample

Take `X=9` and

\[
h(n)=\mathbf1_{n=9}.
\]

Then the only nonzero adjacent differences of `h` occur at `n=8,9`, so

\[
\boxed{
V(h)=\sqrt8+\sqrt9=2\sqrt2+3.
}
\tag{R-32301.3}
\]

Directly from (R-32301.2),

\[
\mathcal T_9h(3)=-1,
\qquad
\mathcal T_9h(5)=1,
\]

and all other output coordinates are zero.  Hence

\[
\boxed{
V(\mathcal T_9h)
=\sqrt2+\sqrt3+2+\sqrt5.
}
\tag{R-32301.4}
\]

Moreover

\[
\sqrt3>\frac53,
\qquad
\sqrt5>2,
\qquad
\sqrt2<\frac32,
\]

so

\[
\sqrt3+\sqrt5-\sqrt2
>\frac53+2-\frac32
=\frac{13}{6}>1.
\]

Therefore

\[
\boxed{
V(\mathcal T_9h)>V(h).
}
\tag{R-32301.5}
\]

The radical bounds above are certified by integer squares.

## 3. Consequence

The correct lesson from PR #305/#310 and PR #316 is not that **every** boundary contracts in a universal BV norm.  It is that the actual activated critical boundary has much smaller native variation than its isolated divisor-source norm.

A valid continuation must retain source structure: stopped powers, parity activation, scale self-similarity, or exact Cycle-Debt optimization.  Generic BV operator norm estimates are too strong.

In particular this refutation blocks the speculative shortcut

```text
large atomic norm
 -> replace by generic weighted variation
 -> invoke one universal contraction.
```

It does not affect the source-specific logarithmic variation theorem on PR #316 or the complete shifted log-coordinate reserve on PR #313.

## 4. Proof boundary

Refuted exactly:

- uniform strict contraction of `V` for arbitrary finite sequences.

Unaffected:

- source-specific variation estimates;
- static stopped-half-power Cycle Debt;
- PR #272 optimized Cycle Debt;
- RH, which remains unproved.
