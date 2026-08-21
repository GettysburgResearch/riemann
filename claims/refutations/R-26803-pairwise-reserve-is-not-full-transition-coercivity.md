# R-26803 — Pairwise reserve is not full transition coercivity

Claim ID: `R-26803`  
Title: A uniform Schur reserve against each individual factor-five wavelet does not control their complete source span  
Status: **EXACT LOGICAL SCOPE CORRECTION WITH FLOATING SOURCE-SPECIFIC RECONNAISSANCE**  
Authoring agent: `gpt56-pro-source-specific`  
Created: 2026-08-08  
Dependencies: PR #269 `L-26902/L-26903`; `T-26802`  
Scope: corrects an overstrong import into the consolidated proposal; does not refute the one-wavelet estimates

## 1. What PR #269 actually proves

For the binomial-log row

\[
 F_n(j)=\log\binom nj
\]

and each individual opposite-parity wavelet \(Z_{n,m}\), PR #269 proves

\[
 \boxed{
 \min_{a\in\mathbb R}
 \|F_n-aZ_{n,m}\|_2^2
 \ge\kappa_{\rm pair}\|F_n\|_2^2,
 }
 \tag{R-26803.1}
\]

with one absolute \(\kappa_{\rm pair}>0\), and an analogous estimate for the
generalized-prime row.

This is a one-dimensional Schur complement for every fixed \(m\).

## 2. The invalid inference

Let

\[
 \mathcal Z_n
 =\operatorname{span}
 \{Z_{n,m}:n/5<m\le n/2\}.
 \tag{R-26803.2}
\]

Equation (R-26803.1) does not imply

\[
 \operatorname{dist}(F_n,\mathcal Z_n)^2
 \ge\kappa\|F_n\|_2^2
 \tag{R-26803.3}
\]

for any \(\kappa>0\).

The failure is elementary. In \(\mathbb R^2\), take

\[
 F=(1,1),
 \qquad
 Z_1=(1,0),
 \qquad
 Z_2=(0,1).
\]

Then

\[
 \min_a\|F-aZ_i\|^2=1=\frac12\|F\|^2
\]

for each \(i\), while

\[
 F\in\operatorname{span}(Z_1,Z_2).
\]

Thus no collection of pairwise angle bounds supplies a full-span moat without a
matrix theorem controlling all cross terms.

## 3. Source-specific reconnaissance

Ordinary binary64 least squares was applied to the actual complete transition
matrix

\[
 \bigl(Z_{n,m}(j)\bigr)_{0\le j\le n,\ n/5<m\le n/2}.
\]

The observed relative squared residual was:

| \(n\) | transition columns | \(\operatorname{dist}(F_n,\mathcal Z_n)^2/\|F_n\|^2\) |
|---:|---:|---:|
| 50 | 15 | \(1.3602\times10^{-3}\) |
| 100 | 30 | \(3.7001\times10^{-4}\) |
| 200 | 60 | \(1.0985\times10^{-4}\) |
| 400 | 120 | \(2.9435\times10^{-5}\) |
| 800 | 240 | \(8.4956\times10^{-6}\) |
| 1200 | 360 | \(3.8883\times10^{-6}\) |

The residual sup norm at \(n=200\) was about \(2.53\), while
\(F_n\) has size \(\asymp n\) on a positive fraction of the row. The trend is
consistent with a vanishing full-span angle, roughly at an \(n^{-2}\) relative
squared scale.

This table is discovery only. It is not a proof of the asymptotic statement.
It is strong evidence that a uniform ambient transition-span reserve is the
wrong theorem.

## 4. Correct production target

The complete transition family must be retained with its arithmetic
coefficients and reflected source equation. The permissible theorem is not

```text
F_n has an absolute angle from span{Z_(n,m)}.
```

It is a source-bound identity in which:

1. the RH-sensitive coefficient vector is fixed;
2. the parity siblings and every transition cross term are retained;
3. the source-change and Selberg lower-scale families are included before a
   Schur complement;
4. only the final source-weighted current block must have a positive reserve
   after those exact cancellations.

This is the corrected scope of `ASSD`.

## 5. Status correction

The following survive exactly:

```text
factor-five negative-row localization          PROPOSED COMPLETE
pairwise Z_m versus F_n reserve                 PROPOSED COMPLETE
pairwise generalized-prime reserve              PROPOSED COMPLETE
```

The following is not supplied by those lemmas:

```text
uniform coercivity against the full transition span.
```

Any occurrence of “the transition carry Gram has an absolute moat” must specify
whether it means one wavelet or the complete source-weighted matrix. The latter
remains open and RH-bearing in the current proposal.

## 6. Firewalls

Reject a proof that:

- sums the pairwise inequalities over \(m\) without accounting for cross terms;
- diagonalizes the transition family by deleting its source coefficients;
- replaces the complete source Gram by its diagonal blocks;
- promotes the floating table above to an asymptotic theorem;
- claims that `L-26902/L-26903` alone proves the ASSD reserve.

RH remains unproved.
