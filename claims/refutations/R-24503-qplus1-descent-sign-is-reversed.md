# R-24503 — The `q+1` descent sign is reversed

Claim ID: `R-24503`  
Status: `REFUTATION / EXACT SIGN CORRECTION`  
Scope: `L-24511` descending repair  
Issue: #245

For a real carry coordinate vector `b`, write

\[
v_r(b)=\sum_{m=2}^{X}b_m
\left(\mathbf1_{r\mid m}-\mathbf1_{r\mid m-1}\right).
\tag{R-24503.1}
\]

If one subtracts an amount `t>=0` from the single coordinate `b_m`, then

\[
\boxed{
\Delta v_r
=-t\left(\mathbf1_{r\mid m}-\mathbf1_{r\mid m-1}\right).
}
\tag{R-24503.2}
\]

The first version of `L-24511` proposed using `m=q+1` to reduce a positive
residual at a prime power `q`. But

\[
\mathbf1_{q\mid q+1}-\mathbf1_{q\mid q}=0-1=-1,
\]

so (R-24503.2) gives

\[
\boxed{
\Delta v_q=+t.
}
\tag{R-24503.3}
\]

It increases the `q`-row rather than repairing it.

The correct local index is `m=q`, for which

\[
\boxed{
\Delta v_q=-t.
}
\tag{R-24503.4}
\]

At every other prime power `r`, the exact side effect is

\[
\boxed{
\Delta v_r
=-t\,\mathbf1_{r\mid q}
+t\,\mathbf1_{r\mid q-1}.
}
\tag{R-24503.5}
\]

Thus the corrected operation has two favorable properties:

1. all negative side effects occur on prime-power divisors of `q`;
2. every positive side effect occurs at a strict lower index `r|q-1`.

For an ordinary prime `q>3`, every positive ordinary-prime destination satisfies

\[
r\le\frac{q-1}{2}.
\tag{R-24503.6}
\]

The correction has exact full objective cost

\[
\boxed{
t\log\frac q{q-1}.}
\tag{R-24503.7}
\]

## Disposition

The `q+1` sign and any theorem depending on it are rejected. The half-scale
descent idea survives after replacing `q+1` by `q`, but its cumulative cost
requires a new proof; it is supplied as an exact finite algorithm in
`L-24519` rather than silently repairing the old claim.
