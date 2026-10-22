# L-91412 — The cutoff-centered causal row kernel has one sign change

Claim ID: `L-91412`  
Status: **PROVED EXACT SIGN-GEOMETRY THEOREM; FINAL SIGN SEPARATE**  
Created: 2026-08-13  
Depends on: `L-91410`, `L-91411`, and the proved cutoff inequality `c>y`  
RH status: **unproved**

Fix `p>=67`, `1<=y<=67`, `2<=j<=66`, and let `c>y` be the score-Lorenz cutoff. For an active source node `d`, define

\[
G_{j,c}(d)=K_R^{(j)}(d)K_S(c)-K_S(d)K_R^{(j)}(c).
\]

Because `K_S>0`,

\[
G_{j,c}(d)=K_S(d)K_S(c)[q_j(d)-q_j(c)].
\]

If `d<=y`, `L-91410` gives `q_j(d)>=phi_j(p)`. Since `c>y`, the cutoff is child-inactive and

\[
q_j(c)=\phi_j(py/c)<=\phi_j(p).
\]

Hence `G_(j,c)(d)>=0` for every child-active node. If `d>y`, then

\[
q_j(d)=\phi_j(py/d),
\]

and the monotonicity of `phi_j` gives

\[
G_{j,c}(d)>=0\quad(d<=c),
\qquad
G_{j,c}(d)<=0\quad(d>=c).
\]

Thus the complete centered source kernel has one known sign change, even though the uncentered causal ratio is not continuously monotone in the child-active region.

The cutoff determinant is exactly

\[
\boxed{
\Delta_{j,c}(p,y)=
\sum_{d\mid P_{61}}\mu(d)G_{j,c}(d)
}
\]

with causal zero extension. Therefore the remaining row-provenance gate is one signed finite-divisor transform of a one-crossing kernel. It may be attacked by a directed activation-cell proof, a discrete ordered transport, or a positive transform factorization.

```text
child-active centered kernel             NONNEGATIVE EXACT
frontier before cutoff                    NONNEGATIVE EXACT
frontier after cutoff                     NONPOSITIVE EXACT
one sign change                           EXACT
cutoff determinant identity               EXACT
signed finite-divisor transform sign      OPEN
Riemann Hypothesis                        UNPROVEN
```
