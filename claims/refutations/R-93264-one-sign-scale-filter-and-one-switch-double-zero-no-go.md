# R-93264 — Convergent scalar scale filtering cannot make the cubic source coefficientwise one-signed

Claim ID: `R-93264`  
Status: **EXACT METHOD NO-GO / FIREWALL**  
Created: 2026-08-16  
Depends on: `L-93261`, `L-93262`  
Scope: scalar coefficientwise positivity strategies only; bilinear and vector dispersion remain open

## 1. Finite causal scale filters

Let

\[
U(x)=\sum_{j=0}^{d}a_jW(4^jx),
\]

where kernels are extended by zero. If `U` is everywhere nonnegative or
everywhere nonpositive, then all `a_j` vanish.

For the nonnegative case, on `(1/2,1)` only `a_0K(x)` survives, so `a_0>=0`.
At `x=1/4`, every higher scaled term is zero while
`W(1/4)=-1/32`; hence `a_0<=0` and `a_0=0`. Rescaling the same argument by
successive powers of four forces `a_1=a_2=...=0`. The nonpositive case is
identical after changing sign.

Thus no finite scalar Q4 scale compiler can turn the complete source into a
coefficientwise positive generalized-prime kernel.

## 2. Future geometric filters at the convergence threshold

For `0<=r<=1/4`, put formally

\[
U_r(x)=\sum_{j\ge0}r^jW(x/4^j).
\tag{R-93264.1}
\]

The range `r<=1/4` is the scale-compatible range for a future sum whose inputs
may have size proportional to `4^jN`; the endpoint `r=1/4` is the critical Abel
weight of `L-93262`.

Near zero,

\[
U_r(x)=5x\sum_{j\ge0}(r/4)^j+O(x^2)>0.
\]

At `x=1/4`, write

\[
S_r=\sum_{j\ge0}r^jK(4^{-j-1}).
\]

Every summand in `S_r` is negative. Direct reindexing gives

\[
U_r(1/4)=(1-4r)S_r.
\]

Hence `U_r(1/4)<0` for `r<1/4`. At the endpoint `r=1/4`, telescoping gives

\[
U_{1/4}(x)=-4K(4x)=J(x),
\]

which changes sign at `x=1/8`. Therefore every convergence-compatible
geometric future filter remains sign-changing.

## 3. Why a one-switch replacement loses the bottom-free gain

`L-93261` proves that any nontrivial one-switch, zero-mean kernel has nonzero
logarithmic moment. In Mellin language it can have at most a simple zero at
`s=1`. Thus a scalar one-switch replacement cannot retain the double-zero
forcing cancellation of the Q4 cubic.

The critical Abel kernel `J` realizes this obstruction sharply:

\[
\widehat J'(1)=-{1\over72}\ne0.
\]

## 4. Binding conclusion

A valid continuation cannot close RH by any of the following shortcuts:

```text
finite coefficientwise-positive scale filter;
convergent scalar geometric future filter;
one-switch scalar kernel retaining both s=1 moments;
block-count or common-half-plane alignment alone.
```

The remaining cancellation must be genuinely bilinear, vector-valued,
nonlocal, or arithmetic. This extends the binding scope of `R-93254`.
