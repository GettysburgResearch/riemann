# L-19881 — The `Y_4=0` triangular repair cone is a null gauge for the prime radial dictionary

Claim ID: `L-19881`  
Status: **PROPOSED EXACT RADIAL-GAUGE THEOREM — PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-09-w`  
Created: 2026-08-14  
Dependencies: `L-19880`; PR #470 `L-91687`; PR #468 `L-91378`  
Scope: exact interaction between radix-four repair and prime radial source; no SONTR or RH claim

## 1. Radix-four inverse

Let the ordinary-to-detail operator be

\[
 (\mathcal B_4g)(q)=g(q)-2g(4q).
 \tag{L-19881.1}
\]

On finitely supported columns its positive inverse is

\[
 \boxed{
 (\mathcal R_4s)(q)
 =\sum_{k\ge0}2^k s(4^kq).}
 \tag{L-19881.2}
\]

For one detail unit `e_Q`,

\[
 \mathcal R_4e_Q
 =\sum_{k\ge0:\,4^k\mid Q}2^k e_{Q/4^k}.
 \tag{L-19881.3}
\]

Thus a detail correction at `Q` can alter only the ordinary columns in its
radix-four ancestor chain

\[
 Q,Q/4,Q/4^2,\ldots.
 \tag{L-19881.4}
\]

## 2. Exact score and radial visibility

The dual weight of PR #468 is

\[
 Y_4(Q)
 =\sum_{k\ge0:\,4^k\mid Q}
  2^k\Lambda(Q/4^k).
 \tag{L-19881.5}
\]

Consequently

\[
 \boxed{
 \sum_q\Lambda(q)(\mathcal R_4e_Q)(q)=Y_4(Q).}
 \tag{L-19881.6}
\]

Because every summand in (L-19881.5) is nonnegative,

\[
 \boxed{
 Y_4(Q)=0
 \iff
 \Lambda(Q/4^k)=0
 \text{ for every admissible }k.}
 \tag{L-19881.7}
\]

In particular, no ordinary ancestor of a `Y_4`-zero detail column is a prime
power.

Apply the native-to-radial transform of `L-19880` to the ordinary slack
`mathcal R_4e_Q`. Every radial coefficient is multiplied by `Lambda(q)`, so
(L-19881.7) gives

\[
 \boxed{
 \mathscr L_{\rm native\to radial}
 [\mathcal R_4e_Q]=0
 \qquad\text{whenever }Y_4(Q)=0.}
 \tag{L-19881.8}
\]

Thus the `3962` zero-weight columns found by PR #470 are not merely score-free.
They are exactly invisible to the prime radial Clark source.

## 3. General detail slack

For a nonnegative detail slack

\[
 s^{(4)}=\sum_Qs^{(4)}(Q)e_Q,
 \tag{L-19881.9}
\]

ordinary slack is `mathcal R_4s^(4)` and

\[
 \boxed{
 \sum_q\Lambda(q)(\mathcal R_4s^{(4)})(q)
 =\sum_QY_4(Q)s^{(4)}(Q).}
 \tag{L-19881.10}
\]

Combining (L-19881.10) with `L-19880.22`, the total prime radial slack is

\[
 \boxed{
 \begin{aligned}
 \sum_{q=p^k}s(\sigma,r;q)
 ={}&2\lambda_{\sigma,r}^2
 \int_0^\infty e^{-\lambda_{\sigma,r}x}\\
 &\times\sum_QY_4(Q)s_{e^x}^{(4)}(Q)\,dx.
 \end{aligned}}
 \tag{L-19881.11}
\]

Therefore only the positive-`Y_4` quotient of the native repair cone consumes
prime radial source. The `Y_4=0` cone is a true gauge direction for the radial
prime dictionary.

## 4. Consequence for the `SONTR` campaign

A source-owned native current may first be corrected inside the `Y_4=0` cone to
repair coefficientwise nonnegativity or triangular geometry. Such a correction:

```text
changes the native physical row;
changes ordinary and detail capacities on non-prime-power columns;
changes neither native von-Mangoldt score nor prime radial source coefficients.
```

Only after the null-gauge campaign is exhausted does one need to spend
positive-`Y_4` slack. This gives a canonical two-stage optimization:

```text
stage 1: solve every activation/cutoff cell modulo the radial null gauge;
stage 2: minimize the positive-Y4 quotient subject to source ownership.
```

The theorem does not prove that stage 1 is always feasible, nor that stage 2 has
bounded cost. Those remain finite/source-provenance obligations in `SONTR`.
