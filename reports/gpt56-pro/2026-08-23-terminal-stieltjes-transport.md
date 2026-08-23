# Terminal Stieltjes transport for the Xi boundary programme

Date: 2026-08-23  
Workspace: PR #729  
Scientific status: **RH unproved**

## Advance

The boundary Cauchy function has an exact monotone window coordinate once the
sharp critical-residue sign is available. For nested windows,

\[
H_{\rm in}=H_{\rm out}+\sum_c{\rho_c\over z-c}.
\]

At a real anchor `x_*`, every crossed pole contributes the Hamburger atom

\[
t_c={1\over c-x_*},
\qquad
w_c={-\rho_c\over(c-x_*)^2}.
\]

Therefore

\[
L_k^{\rm in}=L_k^{\rm out}
+
\sum_cw_cv_k(t_c)v_k(t_c)^T.
\]

When the crossed critical points are real and `rho_c<=0`, the increment is
positive semidefinite.

For a parity-symmetric Xi window at the origin, the pair `+/-c` becomes the
positive Stieltjes atom

\[
s_c=c^{-2},
\qquad
W_c=-2\rho_c c^{-2},
\]

and both origin matrices `[beta_(r+s)]` and `[beta_(r+s+1)]` increase inward.
On the safe axis the same pair contributes

\[
{-2\rho_c\over c^2+y^2}.
\]

## Quantifier improvement

For a fixed inner window and a fixed finite order,

\[
\lambda_{\min}(S_{\rm inner})
\ge
\lambda_{\min}(S_{\rm outer}).
\]

Hence exact positivity at outer windows is unnecessary. It is enough that,
along one cofinal sequence, the negative part of each fixed-order terminal
matrix tends to zero. This defines `TAIR105360`.

The exact conclusion graph is

\[
\mathrm{CRVH105330}
\wedge
\mathrm{TAIR105360}
\Longrightarrow
\mathrm{PRES105220}
\wedge
\mathrm{BRP105220}
\Longrightarrow
\mathrm{RH}.
\]

Neither producer gate is proved for Xi.

## Concrete source target

A stronger but simpler sufficient terminal condition is

\[
\beta_0(\Omega_N)\to a\ge0,
\qquad
\beta_n(\Omega_N)\to0
\quad(n\ge1\text{ fixed}).
\]

Then the terminal matrices converge order by order to the positive affine
model. This is named `AATR105360` and remains open.

## Firewall

`H(z)=z-z^3` has `H(iy)/(iy)=1+y^2>0` for every real `y`, but
`[beta_1]=[-1]`. Thus safe-axis scalar positivity cannot replace the complete
Stieltjes hierarchy.

## Replay

```text
PASS_X_105360_TERMINAL_STIELTJES_TRANSPORT
43 exact rational checks
```

The replay verifies only pole-to-atom identities, the two rank-one Stieltjes
updates, and safe-axis consistency. It does not evaluate Xi or establish any
RH-bearing sign theorem.
