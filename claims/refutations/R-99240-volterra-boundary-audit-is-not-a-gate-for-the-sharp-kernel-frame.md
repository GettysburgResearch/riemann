# R-99240 — The rank-two Volterra boundary audit is valid but is not a gate for the SHARP row-kernel frame

Claim ID: `R-99240`  
Mathematical type: **SCOPE SEPARATION / MECHANISM FIREWALL**  
Created: 2026-08-19  
Related review: PR #638 (`T-99230`)  
RH status: **unproved**

PR #638 correctly proves that the second-order inverse

\[
 Vf=\frac{2x^2f''-xf'+f}{2\sqrt x}
\]

has nullspace `span{sqrt(x),x}` and that derivative jumps contribute separate
atoms. A construction relying only on its smooth density must therefore supply
knot atoms and two boundary anchors.

The fixed-row factorization of `L-99240` is a different operator. It begins
with the exact primitive identity

\[
 \int_m^Y(4\sqrt{Y/t}-3)
 \frac{4(m/t)^{3/2}-1}{3}\frac{dt}{t}
 =\log(Y/m).
\]

The lower limit `m`, the target normalization, and every activation are part
of this identity. Its positive kernel is proved directly, and its output is
checked against the finite canonical row before any continuum inversion.

Accordingly:

```text
PR #638 distributional formula                 retained exact;
PR #638 warning for second-order smooth density binding;
actual two-anchor certificate                  still open for that mechanism;
two-anchor certificate as prerequisite here    false;
SHARP row-kernel boundary normalization         exact / L-99240.
```

A reviewer should not infer that this scope separation proves the compact Hall
or causal identities. It removes only the equality-frame/anchor ambiguity.
