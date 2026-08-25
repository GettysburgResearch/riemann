# R-103001 — Positive scalar Euler activity is not positive physical operator observation

Claim ID: `R-103001`  
Status: **PROVED SCOPE FIREWALL**  
Created: 2026-08-25  
Depends on: `L-103007`  
RH status: **not assumed**

`L-103007` proves positivity after every local Euler variable is replaced by an ordered scalar activity.

The physical source uses instead

\[
x_p=p^{-1/2}U_p,
\]

where the translations `U_p` are different operators. Scalar order

\[
p_1^{-1/2}\ge p_2^{-1/2}\ge\cdots
\]

does not give an operator order between `U_{p_i}` and `U_{p_j}`.

A minimal translation fixture shows the distinction. Let `f` be supported in a short logarithmic interval, and choose two shifts `lambda_1<lambda_2` whose translated supports are disjoint. Then the scalar inequality

\[
r_1-r_2>0
\]

holds for `r_1>r_2`, while the physical difference

\[
r_1f(u-\lambda_1)-r_2f(u-\lambda_2)
\]

has both signs on its two support components.

Consequently

\[
\boxed{
\text{positive ordered scalar rectangle}
\not\Longrightarrow
\text{positive translated physical rectangle}.
}
\]

The valid use of `L-103007` is:

```text
identify and remove the deterministic homogeneous carrier;
retain the centered translated rectangle as the arithmetic frontier.
```

It is not valid to discard the centered physical fluctuation or to infer RH from the scalar carrier sign.