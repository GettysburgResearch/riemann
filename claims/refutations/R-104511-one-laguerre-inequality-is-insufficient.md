# R-104511 — One global Laguerre inequality does not imply real-rootedness

Claim ID: `R-104511`  
Status: **PROVED EXACT COUNTEREXAMPLE**  
Created: 2026-08-22  
RH status: **not assumed**

Consider

\[
p(x)=x^3+x^2+3x+1.
\]

Its derivative is

\[
p'(x)=3x^2+2x+3>0
\]

because its discriminant is `-32`. Hence `p` has exactly one real zero. Its
cubic discriminant is

\[
\operatorname{disc}(p)=-76<0,
\]

so it has one nonreal conjugate pair.

Nevertheless its first Laguerre expression is strictly positive everywhere:

\[
\begin{aligned}
p'(x)^2-p(x)p''(x)
&=3x^4+4x^3+2x^2+7\\
&=3\left(x^2+\frac23x\right)^2+\frac23x^2+7\\
&>0.
\end{aligned}
\]

Equivalently, the phase of `p-i p'` is strictly increasing on the real line,
but the companion still has one zero in the lower half-plane.

Therefore none of the following is sufficient by itself:

```text
the pointwise inequality p'^2-p p'' >= 0;
nonnegative diagonal values of one derivative-ratio Pick kernel;
monotonicity of one boundary phase.
```

The missing datum is the total Hermite–Biehler/Cauchy index. This is why the
programme must retain both local phase velocity and global half-plane index.
