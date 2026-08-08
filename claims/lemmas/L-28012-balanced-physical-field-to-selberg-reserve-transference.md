# L-28012 — Balanced physical field to Selberg-reserve transference

Claim ID: `L-28012`  
Title: On every fixed balanced interior carry-position cone, the RH-sensitive atomized two-contact pole field is pointwise bounded by a polylogarithmic multiple of the explicit generalized-prime Selberg reserve  
Status: **PROPOSED COMPLETE SOURCE-BOUND TRANSFERENCE THEOREM — INDEPENDENT REVIEW REQUESTED**  
Authoring agent: `gpt56-pro-09-v`  
Created: 2026-08-08  
Corrected: 2026-08-08 to retain the zero-reserve endpoint-neighbor boundary explicitly  
Parent: PR #302  
Dependencies: `L-28009`--`L-28011`  
Scope: closes the physical-to-transverse carry estimate on balanced interior positions; no lower-scale recurrence or RH claim

## 1. The two fields in the same Dirichlet system

For integers `n>=2`, `0<=j<=n`, and `k=n-j`, retain the scaled two-contact
wavelet

\[
 Y_{n,m}(j)
 =\sum_{r\le n/m}b_2(r)\chi_{n,mr}(j).
\]

The RH-sensitive physical field sampled at the carry position `j/n` is

\[
 \boxed{
 Q_2(n,j)=\sum_{m\le n}\Lambda_2(m)Y_{n,m}(j).
 }
\tag{L-28012.1}
\]

The pole-canceling generalized-prime carry profile and complete Selberg forcing
are

\[
 P_2(n,j)=\sum_{q\le n}\Lambda_2(q)\chi_{n,q}(j),
\]

\[
 S_2(n,j)=\sum_{q\le n}C_2(q)\chi_{n,q}(j).
\]

Put

\[
 \boxed{R_2(n,j)=P_2(n,j)^2-S_2(n,j)\ge0.}
\tag{L-28012.2}
\]

`L-28009/L-28010` prove that `R_2` is an explicit source-bound positive reserve.

## 2. Exact generalized-Chebyshev formula for the physical field

Let

\[
 \Psi_2(x)=\sum_{m\le x}\Lambda_2(m)
\]

and define the top-half generalized-prime shell

\[
 \boxed{
 G_2(x)=\Psi_2(x)-\Psi_2(x/2).
 }
\tag{L-28012.3}

Since `1*b_2=epsilon-delta_2`, finite convolution gives

\[
 \boxed{
 Q_2(n,j)=G_2(n)-G_2(j)-G_2(k).
 }
\tag{L-28012.4}

This is the integer specialization of the Jensen-defect field in `L-28011`.

## 3. An elementary absolute shell bound

Every nonzero generalized-prime coefficient lies at an integer `m<=x` and
satisfies

\[
 0\le\Lambda_2(m)\le2\log(2x).
\]

There are at most `floor(x)` such integers. Hence, for every `x>=2`,

\[
 \boxed{
 0\le\Psi_2(x)\le2x\log(2x).
 }
\tag{L-28012.5}

Consequently

\[
 |G_2(x)|\le2x\log(2x),
\]

and, because `j,k<=n`,

\[
 \boxed{
 |Q_2(n,j)|\le6n\log(2n).
 }
\tag{L-28012.6}

No prime-number theorem or zero-free region is used.

## 4. Balanced interior lower bound and reserve

Fix

\[
 0<\eta\le\frac12
\]

and suppose

\[
 \eta n\le j\le(1-\eta)n,
 \qquad
 2\le j\le n-2.
\tag{L-28012.7}

Kummer positivity gives

\[
 P_2(n,j)\ge\log\binom nj\ge\eta n\log2.
\tag{L-28012.8}

`L-28009.26` gives

\[
 S_2(n,j)
 \le {2\log n\over\eta n\log2}P_2(n,j)^2.
\tag{L-28012.9}

Choose

\[
 N_\eta
 =\min\left\{N>=3:
 {2\log N\over\eta N\log2}\le\frac12
 \right\}.
\tag{L-28012.10}

For `n>=N_eta`,

\[
 \boxed{
 R_2(n,j)\ge\frac12P_2(n,j)^2.
 }
\tag{L-28012.11}

Combining (L-28012.6), (L-28012.8), and (L-28012.11) yields

\[
 \begin{aligned}
 |Q_2(n,j)|^2
 &\le36n^2\log^2(2n)\\
 &\le{36\log^2(2n)\over\eta^2\log^22}P_2(n,j)^2\\
 &\le\boxed{
 {72\over\eta^2\log^22}
 \log^2(2n)\,R_2(n,j)}.
 \end{aligned}
\tag{L-28012.12}

For the finitely many **interior** rows `n<N_eta`, `L-28009` gives strict
reserve. Taking the finite maximum of `|Q_2|^2/R_2` over those rows extends
(L-28012.12), after increasing the explicit constant, to every row satisfying
(L-28012.7).

The qualification `2<=j<=n-2` is load bearing. For odd `n`, the endpoint-neighbor
rows `j=1,n-1` have `R_2=0` but a nonzero pole field. They belong to the exact
two-contact boundary and may not be absorbed into the interior constant.

## 5. Carry-position interior normal Gram

Let `dnu(n,j)>=0` be any finite nonnegative measure supported on positions
satisfying (L-28012.7). Multiplying the corrected pointwise bound and summing
gives

\[
 \boxed{
 \sum_{n,j}d\nu(n,j)|Q_2(n,j)|^2
 \le C_\eta\log^2(2N)
 \sum_{n,j}d\nu(n,j)R_2(n,j),
 }
\tag{L-28012.13}

where `N` is the largest parent in the support and `C_eta` is explicit.

Under the exact piecewise-rational carry-position integration of `L-28011`, the
independent-frequency physical normal energy on the balanced **interior** of one
finite block is therefore controlled by a polylogarithmic multiple of the
complete source-matched Selberg reserve.

There is no unspecified physical-to-carry operator, no inverse condition
number, and no ambient-vector theorem.

## 6. Exact boundary disposition

The omitted positions are not an error term. They are the source coordinates

\[
 j\in\{0,1,n-1,n\}.
\]

The trivial positions `0,n` vanish. The two endpoint neighbors are exactly the
unweighted two-contact source of `L-28005/L-28007` and PR #269 `L-26904`.
Their contribution must be retained in the physical block and routed by the
bottom-charge/lower-scale recurrence.

Thus the repository's former RTCT/CISR gap now splits exactly as

```text
balanced interior physical field
    -> explicit transverse reserve
       CLOSED here;

endpoint-neighbor / unit-source boundary
    -> exact two-contact and bottom-charge coordinate
       RETAINED, not estimated here;
    -> strict lower-scale recurrence
       still open.
```

## 7. Proof boundary

Closed exactly or elementarily:

- the physical field as a generalized-Chebyshev shell defect;
- a source-independent elementary shell bound;
- a quantitative balanced-interior lower bound;
- a strict source-matched reserve;
- pointwise physical-to-reserve domination with explicit polylogarithmic loss;
- the induced finite interior normal-Gram inequality;
- the exact exclusion and routing of zero-reserve endpoint neighbors.

Open:

- the unweighted two-contact boundary recurrence;
- a subpower bottom-charge estimate;
- RH.
