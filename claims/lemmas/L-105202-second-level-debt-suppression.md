# L-105202 — Quadratic suppression of the second-level critical-residue debt

Claim ID: `L-105202`
Status: **PROVED UNCONDITIONALLY ON FIXED HIGH-DERIVATIVE WINDOWS**
Created: 2026-08-23
Depends on: `L-105200`, `L-104517`, `L-105100`
RH status: **not assumed**

For a real zero `d` of `f_(m+1)=Xi^(m+1)`, define the local second-level debt
associated with `p=f_(m-1)` by

\[
\tau_{m,d}
={f_{m-1}(d)^2\over f_m(d)f_{m+2}(d)}.
\tag{L-105202.1}
\]

This is exactly the local term

\[
{p(d)^2\over p'(d)p'''(d)}
\]

that appears in `L-105100`.

Fix `T>0`. At `f_(m+1)(d)=0`, the centered defect identity gives

\[
\kappa_m^2f_{m-1}(d)=\Delta_m(d).
\]

By `L-105200`,

\[
|f_{m-1}(d)|\ll M_{m-1}{T\over m}.
\tag{L-105202.2}
\]

The uniform sine/cosine cell theorem gives

\[
|f_m(d)|\gg M_m,
\qquad
|f_{m+2}(d)|\gg M_{m+2}.
\tag{L-105202.3}
\]

Consequently

\[
|\tau_{m,d}|
\ll_T {1\over m^2}
{M_{m-1}^2\over M_mM_{m+2}}.
\tag{L-105202.4}
\]

Moment log-convexity gives

\[
{M_{m+1}^2\over M_mM_{m+2}}\le1.
\]

Since `a_m=M_(m-1)/M_(m+1)`, (L-105202.4) becomes

\[
\boxed{
|\tau_{m,d}|\ll_T {a_m^2\over m^2}.
}
\tag{L-105202.5}
\]

Summing over the real zeros of `f_(m+1)` in `[-T,T]`,

\[
\boxed{
\sum_d|\tau_{m,d}|
\ll_T
{R_{m+1}(T)a_m^2\over m^2}.
}
\tag{L-105202.6}
\]

On the other hand `L-105201` gives

\[
M_{2,m}(T)=R_m(T)a_m^2\bigl(1+O_T(1/m)\bigr).
\]

The adjacent zero counts are asymptotic by `L-104517`, so

\[
\boxed{
{\sum_d|\tau_{m,d}|\over M_{2,m}(T)}
\ll_T {1\over m^2}.
}
\tag{L-105202.7}
\]

Therefore the cross-residue debt exposed by PR #723 is quadratically smaller
than the real critical-residue second moment throughout the unconditional
high-derivative band.

## Scope

The estimate is local to a fixed original-height window and does not by itself
supply the global canonical-product localization requested in `T-105100`.
It proves, however, that the second-level debt is not the obstruction in the
high derivative tail; any serious debt is again confined to a finite-order or
moving-height regime.
