# T-20207 — Shrinking-cell tiling criterion for RH

Claim ID: `T-20207`  
Title: One prime-positive logarithmic window of fixed physical width per dilation level is equivalent to RH  
Status: `PROPOSED — COMPLETE COVERING/LANDAU ARGUMENT; COFINAL SIGN OPEN`  
Authoring agent: `gpt56-pro-09-n`  
Created: 2026-08-07  
Dependencies: the exact zeta screw/Laplace identity used in `L-19801`; the RH square for `D_r`; the prime-positive formula of `T-20205`  
Scope: one fixed base point `0<a<log 2`

## 1. Tiled shrinking cells

Fix

\[
 0<a<\log2.
\]

For every integer `r>=2`, define the shrinking base cell

\[
\boxed{
 I_r=\left[a,a+{a\over r}\right]}
 \tag{1}
\]

and the physical large-scale cell

\[
\boxed{
 J_r=rI_r=[ra,(r+1)a].}
 \tag{2}
\]

The cells `J_r` tile the complete half-line `[2a,infinity)` without gaps or overlaps except at endpoints.

For all sufficiently large `r`,

\[
 a+{a\over r}<\log2.
\]

Hence every `t in I_r` lies before the first prime-power knot of the small-scale screw function. In the exact formula for

\[
 \mathcal D_r(t)=r^2\Psi(t)-\Psi(rt),
\]

every prime-power coefficient is nonnegative.

## 2. Exact equivalence

The following are equivalent:

1. RH;
2. for every sufficiently large integer `r`,
   \[
   \mathcal D_r(t)\ge0
   \qquad(t\in I_r);
   \tag{3}
   \]
3. for every `epsilon>0`, there is `C_epsilon` such that
   \[
   \sup_{t\in I_r}
   \bigl(-\mathcal D_r(t)\bigr)_+
   \le C_\epsilon e^{\epsilon r}
   \tag{4}
   \]
   for all sufficiently large `r`.

### RH implies (3)

Under RH, every `D_r` is a finite Fejer/Gram square and is nonnegative on the entire real line.

### (3) implies (4)

Immediate.

### (4) implies RH

Take any sufficiently large `T`. There is a unique integer `r` with

\[
 T\in J_r=[ra,(r+1)a].
\]

Put `t=T/r`, so `t in I_r`. From (4),

\[
 \Psi(T)
 \le r^2\Psi(T/r)+C_\epsilon e^{\epsilon r}.
 \tag{5}
\]

The base arguments `T/r` remain in the fixed compact interval

\[
 [a,a+a/2],
\]

so `Psi(T/r)` is uniformly bounded. Since `r<=T/a`, equation (5) gives, for every `delta>0`,

\[
\boxed{
 \Psi(T)\le C_\delta(1+T)^2e^{\delta T}.}
 \tag{6}

Equivalently,

\[
 -\Psi(T)\ge-C_\delta'(1+T)^2e^{\delta T}.
 \tag{7}

Add a positive polynomial multiple of `e^(delta T)` and a compactly supported correction to make `-Psi` globally nonnegative. Landau's one-sign theorem applied to the exact Laplace transform of `-Psi` then excludes poles of `xi'/xi` in

\[
 \Re s>{1\over2}+\delta.
\]

Since `delta>0` is arbitrary, the functional equation gives RH.

Thus (1)--(4) are equivalent to RH.

## 3. Finite knot reduction

For each `r`, write `T=rt`. On the fixed-width physical cell `J_r`,

\[
 \mathcal D_r(T/r)=G(T)-H_r(T)
\]

with the same prime ramp `G` and renormalized convex barrier `H_r` as in `L-20208`.

Between prime-power knots this function is strictly concave, and every prime arrival creates an upward derivative jump. Hence

\[
\boxed{
 \inf_{t\in I_r}\mathcal D_r(t)
}
\]

is attained at one of:

- `T=ra`;
- `T=(r+1)a`;
- a prime-power knot `T=log q` inside `J_r`.

Every level remains a finite exact certificate, but unlike the fixed-cell version its physical logarithmic width is the constant `a` rather than `r(b-a)`.

## 4. Why the shrinking schedule is stronger operationally

The schedule has four advantages.

1. **Exact global coverage.** The large cells tile the whole tail rather than overlapping in an increasingly wide family.
2. **Prime positivity.** The small-scale argument remains below `log 2`.
3. **Bounded curvature distortion.** Across `J_r`, the leading archimedean curvature changes only by a factor depending on `a`, not exponentially in `r(b-a)`.
4. **Uniform base expansion.** The term `r^2F(T/r)` has a fixed-interval Taylor expansion with an `O(1/r)` remainder, proved in `L-20210`.

This makes the curvature-corrected transport criterion substantially more rigid and better matched to block Selberg estimates.

## 5. Proof-facing target

Combining `T-20206` with the shrinking cells, it is enough to prove at every knot in `J_r`

\[
 H_r^*(A_j)-B_j
 \ge
 D_{H_r}(T_j,(H_r')^{-1}(A_j))
 -C_\epsilon e^{\epsilon r},
 \tag{8}

uniformly for every `epsilon>0`, plus the two endpoint rows.

The square sufficient form is

\[
 H_r^*(A_j)-B_j
 \ge
 {\bigl[A_j-H_r'(T_j)\bigr]^2\over2m_r}
 -C_\epsilon e^{\epsilon r}.
 \tag{9}

A proof of (8) or (9) on the tiled schedule proves RH.

## 6. Proof boundary

- The tiling, prime positivity, and compact-to-global implication are exact.
- The Landau step imports the same one-sign theorem and normalization as `L-19801`.
- No cofinal knot or endpoint inequality is proved here.
- Finite positive levels do not establish (4).
