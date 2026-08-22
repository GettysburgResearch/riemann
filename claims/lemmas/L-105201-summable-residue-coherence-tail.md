# L-105201 — Summable critical-residue coherence in the high Xi derivative tail

Claim ID: `L-105201`
Status: **PROVED UNCONDITIONALLY**
Created: 2026-08-23
Depends on: `L-105200`, `L-104517`, `L-104522`
RH status: **not assumed**

Put

\[
f_m=\Xi^{(m)},
\qquad
a_m={M_{m-1}\over M_{m+1}}=\kappa_m^{-2}.
\]

For a real zero `c` of `f_m`, define the derivative-ratio residue

\[
\rho_{m,c}={f_{m-1}(c)\over f_{m+1}(c)}.
\tag{L-105201.1}
\]

Fix `T>0`. By `L-104517`, for all sufficiently large `m`, every zero of
`f_m`, `f_(m+1)` and `f_(m+2)` in a fixed complex rectangle containing
`[-T,T]` is real and simple, and each such zero lies in a unique shrinking
sine/cosine cell. In particular, at a zero `c` of `f_m`,

\[
|f_{m+1}(c)|\gg M_{m+1}
\tag{L-105201.2}
\]

uniformly in `c`.

## 1. Uniform residue carrier

From

\[
\Delta_m=f_{m+1}+\kappa_m^2f_{m-1},
\]

we obtain at `f_m(c)=0`

\[
\rho_{m,c}
=-a_m+a_m{\Delta_m(c)\over f_{m+1}(c)}.
\]

Using `L-105200.9` and (L-105201.2),

\[
\boxed{
\rho_{m,c}
=-a_m(1+\varepsilon_{m,c}),
\qquad
|\varepsilon_{m,c}|\ll_T {1\over m},
}
\tag{L-105201.3}
\]

uniformly over all real zeros `c` in `[-T,T]`.

Thus all high-order residues have the correct negative orientation, and they
are uniformly locked to one harmonic carrier.

## 2. Summable coherence defect

Let

\[
R_m(T)=\#\{c\in[-T,T]:f_m(c)=0\},
\]

\[
M_{1,m}(T)=-\sum_c\rho_{m,c},
\qquad
M_{2,m}(T)=\sum_c\rho_{m,c}^2,
\]

and define the residue coherence

\[
C_m(T)={M_{1,m}(T)^2\over R_m(T)M_{2,m}(T)}.
\tag{L-105201.4}
\]

If `x_c=1+epsilon_(m,c)`, then

\[
C_m(T)={\bigl(\sum_cx_c\bigr)^2\over
R_m(T)\sum_cx_c^2}.
\]

For `delta_m=max_c|epsilon_(m,c)|<1`,

\[
1-C_m(T)
={\operatorname{Var}(x_c)\over\operatorname{Mean}(x_c^2)}
\le {\delta_m^2\over(1-\delta_m)^2}.
\]

Therefore

\[
\boxed{
1-C_m(T)\ll_T {1\over m^2}.
}
\tag{L-105201.5}
\]

In particular,

\[
\boxed{
\sum_{m\ge M}\bigl(1-C_m(T)\bigr)
\ll_T {1\over M}.
}
\tag{L-105201.6}
\]

This is stronger than `C_m(T)->1`: the coherence loss is summable.

## 3. Summable multiplicative coherence tail

The one-step transfer theorem `L-104522` uses the factor

\[
c_m(T)=2C_m(T)-1.
\]

For `M` sufficiently large, `c_m(T)>0`, and

\[
\log\prod_{m=M}^Nc_m(T)
\ge -O_T\left(\sum_{m=M}^Nm^{-2}\right).
\]

Hence

\[
\boxed{
\inf_{N\ge M}
\prod_{m=M}^N\bigl(2C_m(T)-1\bigr)
\ge \exp\bigl(-O_T(1/M)\bigr),
}
\tag{L-105201.7}
\]

and the right side tends to one as `M->infinity`.

Thus the **multiplicative coherence factors** in the high-derivative tail have no macroscopic loss. The separate endpoint `-1` in the one-step count theorem is not summed here; `R-105201` keeps that boundary charge on the endpoint/winding ledger. Any interior residue-coherence loss is confined to a finite derivative prefix.

## 4. Growing windows

The same proof gives

\[
1-C_m(T_m)\ll {T_m^2\over m^2}
\]

whenever `T_m sqrt(log m/m)->0`. The fixed-window form is singled out because
its derivative-order loss is summable without further assumptions.

## Scope

The theorem does not control the finite derivative prefix and does not prove
that Xi itself is real-rooted. It converts the post-integration Xi programme
from an infinite-tail problem into a finite-prefix problem plus explicit
endpoint/winding transport.
