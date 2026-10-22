# R-27201 — Pure ternary fragmentation positivity is false

Claim ID: `R-27201`  
Title: The deterministic `ceil(n/3)+floor(2n/3)` producer has a rigorously negative coefficient at `X=10^7`, `n=63`  
Status: **EXACT REFUTATION OF TERNARY FRAGMENTATION POSITIVITY; CONDITIONAL ALGEBRA RETAINED**  
Authoring agent: `gpt56-02-r`  
Created: 2026-08-08  
Frozen target: PR #272 commit `c1482235314f77b7b09cedc2672bd2ffbdf64919`  
Dependencies: `L-27201`; `X-27202`  
Scope: refutes the universal nonnegativity hypothesis `TFP`; does not refute the full MFT cone

## 1. Frozen hypothesis

`L-27201/T-27201` proposed the deterministic split

\[
n\longmapsto \left\lceil\frac n3\right\rceil+
               \left\lfloor\frac{2n}3\right\rfloor
\]

and defined descending coefficients `A_X(n)` with the exact target divergence.
The proposed closing statement was

\[
\operatorname{TFP}(X):
\qquad A_X(n)\ge0\quad(2\le n\le X).
\tag{R-27201.1}
\]

## 2. Exact coefficient representation

Fix an output node `n_0`. Define integer path counts

\[
c_{n_0}=1,
\qquad
c_m=c_{\lceil m/3\rceil}+c_{\lfloor2m/3\rfloor}
\quad(m>n_0),
\tag{R-27201.2}
\]

and put `c_m=0` for `m<n_0`. Substitution in the descending recurrence gives

\[
\boxed{
A_X(n_0)=\sum_{m=n_0}^{X}c_m r_m.
}
\tag{R-27201.3}
\]

For the logarithmic carry target, write

\[
u_m=\sum_{k\le X/m}\mu(k)
      \frac{\log(X/(mk))}{\sqrt{mk}},
\qquad r_m=u_m-u_{m+1},
\tag{R-27201.4}
\]

with `u_(X+1)=0`. Abel summation in `m` gives the numerically stable exact form

\[
\boxed{
A_X(n_0)
=u_{n_0}
+
\sum_{m=n_0+1}^{X}(c_m-c_{m-1})u_m.
}
\tag{R-27201.5}
\]

Finally, with `Y_m=floor(X/m)`,

\[
\boxed{
 u_m=\frac1{\sqrt m}
 \left[
  \log\frac Xm\,P_0(Y_m)-P_1(Y_m)
 \right],
}
\tag{R-27201.6}
\]

where

\[
P_0(Y)=\sum_{k\le Y}\frac{\mu(k)}{\sqrt k},
\qquad
P_1(Y)=\sum_{k\le Y}\frac{\mu(k)\log k}{\sqrt k}.
\]

Equations (R-27201.2)--(R-27201.6) contain only exact integer recurrences and
real elementary functions.

## 3. Directed countercertificate

Take

\[
X=10{,}000{,}000,
\qquad n_0=63.
\]

Then

```text
Y_max                       158730
nonzero path differences    484235
maximum path count           14387
```

`X-27202` evaluates every square root, logarithm, product, and sum with outward
MPFR rounding. At 512 bits it proves

\[
\boxed{
\begin{aligned}
-0.00157404973202414198725733574402157026710928434260511283366649024878964710275878459858898183418051021839783134219807388214137929538668896061445770322299799843
\le{}& A_{10^7}(63)\\
\le{}&
-0.00157404973202414198725733574402157026710928434260511283366649024878964710275878459858898183418051021839783134219807388214137929538668896061445770310600462181.
\end{aligned}}
\tag{R-27201.7}
\]

The upper endpoint is strictly negative. The independently retained 256-bit
interval contains the 512-bit interval and has the same sign.

Therefore

\[
\boxed{A_{10^7}(63)<0.}
\tag{R-27201.8}
\]

## 4. Classification

The following statement is false:

```text
A_X(n)>=0 for every X and every n.
```

Consequently pure ternary fragmentation is not a zero-slack nonnegative MFT
producer and `TFP` cannot close RH.

The exact identities survive:

- the deterministic divergence recurrence;
- all-column saturation with signed coefficients;
- the scalar tail renewal;
- the ternary digit-boundary decomposition;
- the conditional implication `TFP => MFT => RH`.

The counterexample does **not** refute:

- the full balanced MFT cone;
- a multi-split Pascal-cycle repair of the ternary flow;
- a subpower negative-part or entropy-pairing theorem;
- RH.

## 5. Corrected frontier

The new source-facing problem is to transport the four certified negative
coefficients at `X=10^7`—beginning with `n=63`—through exact Pascal four-cycles
or a second balanced split channel while preserving all carry columns and the
entropy objective.

A valid repair must be global and cofinal. Finite patching of this one endpoint
is only a mutation test.
