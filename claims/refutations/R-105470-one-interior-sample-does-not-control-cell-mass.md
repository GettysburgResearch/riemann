# R-105470 — One interior sample cannot control an affine cell's logarithmic L1 mass

Claim ID: `R-105470`

Status: **PROVED EXACT FIREWALL**

Fix an integer cell \((m,m+1)\) and any prescribed interior point
\(X_0\in(m,m+1)\).  Put

\[
q(X)=\sqrt X-\sqrt{X_0}.
\tag{R-105470.1}
\]

Then \(q\) has the exact cell form permitted by `L-105470`, and

\[
q(X_0)=0.
\]

Nevertheless

\[
\boxed{
\int_m^{m+1}|q(X)|{dX\over X}>0.
}
\tag{R-105470.2}
\]

Indeed, after \(t=\sqrt X\), the integrand is
\(2|t-\sqrt{X_0}|/t\), which is positive away from one point.

More strongly, multiplying (R-105470.1) by an arbitrary scalar makes the cell
mass arbitrarily large while preserving the zero sample.

## Binding consequence

None of the following is a valid substitute for `F1HARDY105470`:

```text
midpoint sampling;
one sample per integer cell;
a sign assertion at one selected point of each cell;
a quadrature rule with no endpoint or slope information.
```

Two endpoint values are sufficient by `L-105470.10`; one interior value is not.
This firewall is independent of arithmetic and cannot be repaired by changing
the owner gauge.
