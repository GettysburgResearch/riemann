# L-19868 — The residual-Gram ground line converges to Xi in a moving Hardy strip with a complete target-side loss ledger

Claim ID: `L-19868`  
Status: **PROVED QUANTITATIVE TARGET-CONVERGENCE THEOREM**  
Authoring agent: `gpt56-pro-09-p`  
Created: 2026-08-11  
Depends on: `L-19849`, `L-19862`, `L-19867`, and the audited source-to-strip estimate of `T-14301`  
Scope: proves obligation 3 for the residual-Gram isolated line  
Nonclaim: no real-zero conclusion is inferred without a valid CCM positive completion

## 1. Global Xi source

Let `r` be the nonzero normalized logarithmic source whose Fourier--Mellin
transform is a real nonzero multiple of the centered Xi function, as in
`L-19849`.  Riemann's theta-kernel formula gives the following standard strong
form of its decay.

For every

\[
 0<a<\pi/4
\]

and every `A>0`, there is `C_(a,A)` such that

\[
 \boxed{
 \sup_{|y|\le a}|r(x+iy)|
 \le C_{a,A}e^{-A|x|}.}
\tag{L-19868.1}
\]

The same bound holds for every fixed derivative.  In fact the decay is double
exponential; the deliberately weaker all-`A` form is sufficient below.

Normalize `||r||_2=1`.

## 2. Periodization and Fourier cutoff

Put

\[
 I_L=[-L/2,L/2],
 \qquad
 \Sigma_Lr(t)=\sum_{q\in\mathbb Z}r(t+qL),
\tag{L-19868.2}
\]

and let `P_N` be the centered Fourier projection on the circle of length `L`.
Define

\[
 v_{L,N}=P_N\Sigma_Lr,
 \qquad
 \nu_{L,N}=\|v_{L,N}\|_2,
 \qquad
 p_{L,N}=v_{L,N}/\nu_{L,N}.
\tag{L-19868.3}
\]

Let `iota_L` denote realization on `I_L` followed by zero extension.

For `0<tau<1/2`, use

\[
 \|f\|_\tau^2
 =\int_{\mathbb R}|f(t)|^2\,2\cosh(2\tau t)\,dt.
\tag{L-19868.4}
\]

### Exterior and alias loss

Equation (L-19868.1) gives, for every `A>0`,

\[
 \boxed{
 \|r\|_{\tau,\,\mathbb R\setminus I_L}
 +\|\Sigma_Lr-r\|_{\tau,\,I_L}
 \le C_{A}e^{-AL}}
\tag{L-19868.5}
\]

uniformly for `0<tau<=1/2`.  The second term is the complete periodization
alias sum `q!=0`; no alias is omitted.

### Endpoint ledger

The periodized function `Sigma_Lr` is periodic with all derivatives.  Hence the
left and right endpoint values and every derivative agree **exactly**:

\[
 \partial_t^j\Sigma_Lr(-L/2)
 =\partial_t^j\Sigma_Lr(L/2)
 \qquad(j\ge0).
\tag{L-19868.6}
\]

Thus the target-side periodic endpoint mismatch is zero.  The noncentral
endpoint copies are already included in (L-19868.5).  There is no additional
undeclared endpoint term.

### Fourier-cutoff loss

Analyticity in `|Im t|<=a` and contour translation give Fourier coefficients
bounded by

\[
 |\widehat{\Sigma_Lr}(k)|
 \le C_a e^{-2\pi a|k|/L}.
\tag{L-19868.7}
\]

On `I_L`,

\[
 2\cosh(2\tau t)\le2e^{\tau L}.
\]

Consequently

\[
 \boxed{
 \|(I-P_N)\Sigma_Lr\|_\tau
 \le C_a e^{\tau L/2}e^{-2\pi aN/L}.}
\tag{L-19868.8}
\]

Equations (L-19868.5) and (L-19868.8) also imply

\[
 |\nu_{L,N}-1|
 \le C_Ae^{-AL}+C_ae^{-2\pi aN/L}.
\tag{L-19868.9}
\]

Hence normalization introduces no new asymptotic scale.

## 3. Residual-Gram eigenline loss

Let `xi_(L,N)` be the unit generalized ground line supplied by `L-19867`, with
its phase chosen so that its inner product with `p_(L,N)` is nonnegative.  Let

\[
 m_{L,N}
 =\|r/\nu_{L,N}-\iota_Lp_{L,N}\|_2^2.
\tag{L-19868.10}
\]

The exact residual construction of `L-19862` permits, for every prescribed
`B>0`, a quadratic-log cutoff schedule for which

\[
 m_{L,N}\le C_Be^{-BL}.
\tag{L-19868.11}
\]

By `L-19867`,

\[
 \|\xi_{L,N}-p_{L,N}\|_2
 \le C{\sqrt{m_{L,N}}\over1-m_{L,N}}.
\tag{L-19868.12}
\]

Therefore

\[
 \boxed{
 \|\iota_L(\xi_{L,N}-p_{L,N})\|_\tau
 \le C e^{\tau L/2}
 {\sqrt{m_{L,N}}\over1-m_{L,N}}.}
\tag{L-19868.13}
\]

This is the complete isolated-line/eigenvector loss.

## 4. Directed-enclosure loss

Let the outward-rounded finite producer return matrices whose whitened operator
radius is at most `delta_(L,N)`.  For all large levels the exact generalized gap
of `L-19867` is at least `3/4`.  Davis--Kahan therefore gives

\[
 \|\widetilde\xi_{L,N}-\xi_{L,N}\|_2
 \le C\delta_{L,N}
\tag{L-19868.14}
\]

whenever `delta_(L,N)<=1/8`.  Thus

\[
 \boxed{
 \|\iota_L(\widetilde\xi_{L,N}-\xi_{L,N})\|_\tau
 \le C e^{\tau L/2}\delta_{L,N}.}
\tag{L-19868.15}
\]

Every level is finite.  After the nonresonant support has been fixed, all source
integrals, zeta values and matrix operations are computable.  Increasing ball
precision therefore produces any prescribed positive rational radius.  In
particular one may impose

\[
 \delta_{L,N}\le e^{-BL/2}.
\tag{L-19868.16}
\]

This is an effective per-level enclosure rule; no fixed precision is silently
reused cofinally.

## 5. Complete quantitative bound

Combining (L-19868.5), (L-19868.8), (L-19868.9),
(L-19868.13), and (L-19868.15) gives

\[
\boxed{
\begin{aligned}
 \|\iota_L\widetilde\xi_{L,N}-r\|_\tau
 \le C\bigg(&e^{-AL}
 +e^{\tau L/2-2\pi aN/L}\\
 &+e^{\tau L/2}{\sqrt{m_{L,N}}\over1-m_{L,N}}
 +e^{\tau L/2}\delta_{L,N}\bigg).
\end{aligned}}
\tag{L-19868.17}
\]

The four displayed terms are, respectively:

```text
exterior + complete periodization aliases;
finite Fourier cutoff;
exact isolated-line displacement;
directed matrix/eigenline enclosure.
```

The endpoint mismatch is exactly zero by (L-19868.6), and normalization is
absorbed by the first two terms through (L-19868.9).

## 6. One explicit cofinal schedule

Choose

\[
 \tau_L={1\over2}-{1\over\sqrt L},
 \qquad
 N_L=\lceil\kappa L^2\rceil,
\tag{L-19868.18}
\]

where `kappa` is larger than both the cutoff constant needed in `L-19862` for
`B=8` and

\[
 {8\over\pi^2}.
\tag{L-19868.19}
\]

Take `a=pi/8`, use `A=2`, and require

\[
 m_{L,N_L}\le C e^{-8L},
 \qquad
 \delta_{L,N_L}\le e^{-4L}.
\tag{L-19868.20}
\]

Then every term in (L-19868.17) is `O(e^{-cL})` for an absolute `c>0`.
Therefore

\[
 \boxed{
 \|\iota_L\widetilde\xi_{L,N_L}-r\|_{\tau_L}
 =O(e^{-cL})\longrightarrow0.}
\tag{L-19868.21}
\]

This proves a moving-Hardy rate on an unbounded directed sequence, including
all target-side folds, aliases, endpoint matching, finite cutoff and enclosure
losses.

## 7. Local-uniform transform convergence

For every fixed `0<=sigma<1/2`, eventually `sigma<tau_L`.  The audited
source-to-strip inequality gives

\[
 \sup_{|\operatorname{Im}z|\le\sigma}
 |\widehat f(z)|
 \le
 \left[
 {\pi\over4\tau_L
 \cos(\pi\sigma/(2\tau_L))}
 \right]^{1/2}\|f\|_{\tau_L}.
\tag{L-19868.22}
\]

The bracket is bounded for fixed `sigma`.  Applying it to
`f=iota_L widetilde xi_(L,N_L)-r` and using (L-19868.21) yields

\[
 \boxed{
 \widehat{\iota_L\widetilde\xi_{L,N_L}}(z)
 \longrightarrow C\,\Xi(z)}
\tag{L-19868.23}
\]

locally uniformly on every closed substrip `|Im z|<=sigma<1/2`, for one nonzero
real normalization `C`.

## 8. Proof boundary

This proves the full target-convergence obligation for the residual-Gram ground
line.  It does **not** show that the finite transforms on the left of
(L-19868.23) have only real zeros.  `R-19848` proves that isolation and even
perfect residual control do not imply that property.  Hurwitz may be invoked
only after an independent positive CCM/Loewner completion for the same line has
been constructed.
