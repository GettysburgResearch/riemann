# L-90304 — Aggregate inertia eliminates the unknown current from the determinant defect

Claim ID: `L-90304`  
Title: For a nonnegative aggregate of centered two-state Q4 curvatures, the entire negative determinant defect is controlled by the source-only second-current mean; the unknown RH-sensitive current cancels from the bound  
Status: **PROPOSED COMPLETE EXACT HERMITIAN LEMMA — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro-09-w`  
Created: 2026-08-10  
Dependencies: `L-90301`, `L-90303`; finite-dimensional Cauchy–Schwarz  
Scope: exact aggregate two-state algebra; no analytic Q4 estimate or RH conclusion by itself

## 1. Centered row matrices

Let `A` be a finite index set. For each `a in A`, let

\[
w_a\ge0,\qquad R_a\ge0,
\]

and let

\[
E_a,D_a,\Theta_a\in\mathbf C.
\]

Define the centered two-state Hermitian curvature

\[
\boxed{
K_a=
\begin{pmatrix}
R_a&
-\frac12(\Theta_a-2E_aD_a)\\[1mm]
-\frac12\overline{(\Theta_a-2E_aD_a)}&
|D_a|^2
\end{pmatrix}.
}
\tag{L-90304.1}
\]

For the relative Q4 jet of `L-90303`, after a common source-centering shear,

\[
D_a=I_a-YE_a,
\]

\[
\Theta_a=T_a+Y(R_a-E_a^2),
\]

and

\[
\Theta_a-2E_aD_a
=
T_a-2E_aI_a+Y(E_a^2+R_a).
\]

The compact relative source of PR #345 has `Y=0` exactly on every sufficiently deep balanced row, so there is no row-dependent change of coordinates in that application.

Put

\[
\overline K=\sum_a w_aK_a
=
\begin{pmatrix}
A&-\frac12(U-2V)\\[1mm]
-\frac12\overline{(U-2V)}&B
\end{pmatrix},
\tag{L-90304.2}
\]

where

\[
A=\sum_aw_aR_a,
\qquad
F=\sum_aw_a|E_a|^2,
\]

\[
B=\sum_aw_a|D_a|^2,
\qquad
U=\sum_aw_a\Theta_a,
\qquad
V=\sum_aw_aE_aD_a.
\tag{L-90304.3}
\]

The quantity `B` contains the complete unknown RH-sensitive current energy. The theorem below removes it from the final defect estimate.

## 2. Sharp aggregate determinant theorem

Assume

\[
\boxed{A>F.}
\tag{L-90304.4}
\]

Then

\[
\boxed{
(-\det\overline K)_+
\le
\frac{A}{4(A-F)}\,|U|^2.
}
\tag{L-90304.5}
\]

Consequently, with

\[
\delta(\overline K)=\operatorname{tr}(\overline K)_-,
\]

one has

\[
\boxed{
\delta(\overline K)
\le
\frac{|U|^2}{4(A-F)}.
}
\tag{L-90304.6}
\]

Both bounds are independent of `B`, `D_a`, and hence of the size of the RH-sensitive current.

### Proof

Cauchy–Schwarz gives

\[
|V|^2
\le
\left(\sum_aw_a|E_a|^2\right)
\left(\sum_aw_a|D_a|^2\right)
=FB.
\tag{L-90304.7}
\]

Therefore

\[
\begin{aligned}
(-\det\overline K)_+
&=
\left[
\frac14|U-2V|^2-AB
\right]_+\\
&\le
\left[
\left(\frac{|U|}{2}+\sqrt{FB}\right)^2-AB
\right]_+.
\end{aligned}
\tag{L-90304.8}
\]

Writing `x=sqrt(B)`, the expression inside the final positive part is at most

\[
\frac{|U|^2}{4}
+|U|\sqrt F\,x
-(A-F)x^2.
\tag{L-90304.9}
\]

Since `A-F>0`, its maximum over `x>=0` is

\[
\frac{|U|^2}{4}
+
\frac{|U|^2F}{4(A-F)}
=
\frac{A}{4(A-F)}|U|^2.
\]

This proves (L-90304.5).

If `det Kbar>=0`, then `delta(Kbar)=0`. If `det Kbar<0`, its positive eigenvalue is at least

\[
\operatorname{tr}\overline K=A+B\ge A,
\]

and hence

\[
\delta(\overline K)
=
\frac{-\det\overline K}{\lambda_+(\overline K)}
\le
\frac{(-\det\overline K)_+}{A}.
\]

Substitution of (L-90304.5) proves (L-90304.6).

## 3. Simpler reserve-dominates-score form

If

\[
A\ge2F,
\]

then

\[
\boxed{
(-\det\overline K)_+
\le\frac12|U|^2,
\qquad
\delta(\overline K)
\le\frac{|U|^2}{2A}.
}
\tag{L-90304.10}
\]

This follows either from (L-90304.5)–(L-90304.6), or directly from

\[
\frac14|U-2V|^2
\le
\frac12|U|^2+2|V|^2
\le
\frac12|U|^2+2FB.
\]

## 4. Why aggregation is load bearing

A rowwise estimate would ask for every `a`

\[
|\Theta_a-2E_aD_a|^2
\le4R_a|D_a|^2
+\text{small error}.
\]

That is essentially the local Schur inequality and remains RH-bearing.

The aggregate theorem asks only for:

\[
\sum_aw_aR_a
>
\sum_aw_a|E_a|^2,
\]

and for an upper bound on the single signed source mean

\[
U=\sum_aw_a\Theta_a.
\]

The current-dependent correlation

\[
V=\sum_aw_aE_aD_a
\]

is optimized out by Cauchy–Schwarz before any absolute value is taken rowwise. Large current energy `B` strengthens the positive determinant term `AB`; it never worsens the final bound.

This is the finite Q4 analogue of the key methodological move in Claude's two-thirds theorem: retain the complete indefinite form and use only the spectral statistic consumed by the final argument, rather than prove positivity of every microscopic block.

## 5. Common-centering requirement

The theorem may be applied after a source-centering shear only when that shear is common across the aggregated rows. This holds in either of the following live situations:

1. the compact relative source of PR #345, where the deep balanced bare coordinate is exactly `Y=0`;
2. a row family with one fixed bare coordinate `Y`.

A row-dependent shear cannot be inserted before aggregation without changing the physical synthesis operator. Any continuation that centers rows independently must therefore be rejected.

## 6. Sharpness and mutation firewall

The constant in (L-90304.5) is sharp under the summary data `A,F,U` alone. Equality already occurs for one row with

\[
A=4,\quad F=B=V=0,\quad U=4.
\]

The tempting replacement

\[
(-\det\overline K)_+\le |U|^2/4
\]

is false when `F>0`. The exact verifier `X-90302` contains a rational two-row witness with

\[
(-\det\overline K)_+=97/36,
\qquad
|U|^2/4=25/36,
\]

while the correct bound is `25/6`.

## 7. Proof boundary

Closed exactly here:

1. the aggregate current-free determinant-defect inequality;
2. the sharp source-only negative-mass bound;
3. the reserve-dominates-score corollary;
4. the common-centering scope condition.

Not proved here:

1. the Q4 block estimates implying `A>F`;
2. a bound for the physical source mean `U`;
3. the final coefficient-one recurrence;
4. RH.
