# L-90604 — Functional-equation symmetrization inherits the one-sided Bohr zeros off the critical line

Claim ID: `L-90604`  
Status: **PROPOSED COMPLETE ROUCHÉ TRANSFER THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-11  
Depends on: `L-90603`; uniform Stirling asymptotics  
Scope: finite Brownian functional-equation symmetrizations

## 1. Setup

For one of the positive cutoff mixtures of `L-90603`, write

\[
 m_N(s)=A(s)D_N(s),
 \qquad
 A(s)=\pi^{-s/2}\Gamma(1+s/2),
 \tag{L-90604.1}
\]

and symmetrise:

\[
 \mathcal X_N(s)=m_N(s)+m_N(1-s).
 \tag{L-90604.2}
\]

Then `X_N(s)=X_N(1-s)` and `X_N` has the required real symmetry.

### Theorem

Fix `1/2<beta<1`. Under the top-mass hypothesis of `L-90603`, every sufficiently large `N` has infinitely many zeros `rho_j` of `mathcal X_N` satisfying

\[
 |\operatorname{Im}\rho_j|\to\infty,
 \qquad
 \operatorname{Re}\rho_j\to\beta.
 \tag{L-90604.3}
\]

In particular, the finite functional-equation symmetrization has infinitely many zeros off `Re s=1/2`.

## 2. Simple one-sided vertical-limit zeros

By `L-90603`, after an arbitrarily small generic phase perturbation there is a simple torus zero `w_0` with

\[
 \frac12<\operatorname{Re}w_0<1.
\]

There are vertical shifts `t_j->infinity` and simple zeros

\[
 s_j=w_j+it_j,
 \qquad
 D_N(s_j)=0,
 \qquad
 w_j\to w_0,
 \tag{L-90604.4}
\]

such that

\[
 \frac{D_N'(s_j)}{it_j}\longrightarrow B_{N,\chi}'(w_0)\ne0.
 \tag{L-90604.5}
\]

The last statement follows by locally uniform convergence of the vertical translates and their derivatives.

Put

\[
 x=\operatorname{Re}w_0-\frac12>0.
 \tag{L-90604.6}
\]

## 3. Gamma imbalance off the central line

Uniform Stirling asymptotics on a fixed neighborhood of `w_0` give

\[
 \boxed{
 \frac{|A(1-s)|}{|A(s)|}
 \ll |\operatorname{Im}s|^{1/2-\operatorname{Re}s}
 =O(t_j^{-x+o(1)}).
 }
 \tag{L-90604.7}
\]

The finite Dirichlet polynomial `D_N(1-s)` has size `O_N(t_j)` there, while (L-90604.5) gives

\[
 |D_N'(s_j)|\asymp_N t_j.
 \tag{L-90604.8}
\]

## 4. Rouché near each one-sided zero

Take

\[
 r_j=t_j^{-x/2}.
 \tag{L-90604.9}
\]

On `|s-s_j|=r_j`, Taylor's theorem, (L-90604.5), and the finite exponential-polynomial derivative bounds give

\[
 |m_N(s)|
 \ge c_N|A(s_j)|t_jr_j
 \tag{L-90604.10}
\]

for all large `j`. The logarithmic derivative of `A` is `O(log t_j)`, and `r_j log t_j->0`, so replacing `A(s)` by `A(s_j)` costs only `1+o(1)`.

On the same circle, (L-90604.7) and the finite size bound for `D_N(1-s)` give

\[
 |m_N(1-s)|
 \le C_N|A(s_j)|t_jt_j^{-x+o(1)}.
 \tag{L-90604.11}
\]

Therefore

\[
 \frac{|m_N(1-s)|}{|m_N(s)|}
 \ll_N\frac{t_j^{-x+o(1)}}{r_j}
 =t_j^{-x/2+o(1)}\to0.
 \tag{L-90604.12}
\]

Rouché shows that `mathcal X_N=m_N(s)+m_N(1-s)` has one zero `rho_j` in the disk `|s-s_j|<r_j`. Hence

\[
 \rho_j-s_j\to0,
 \qquad
 \operatorname{Re}\rho_j\to\operatorname{Re}w_0>1/2.
 \tag{L-90604.13}
\]

Repeating for the infinitely many separated shifts proves the theorem.

## 5. Interpretation

Functional-equation symmetrization cannot repair a one-sided high-frequency zero away from the central line. On `Re s>1/2`, Stirling makes the reflected term polynomially smaller by the factor

\[
 |t|^{1/2-\operatorname{Re}s}.
\]

The dominant one-sided zero therefore survives with a vanishing displacement.

This phenomenon is independent of all bounded-height scans and of local-uniform convergence to xi.

## 6. Proof boundary

Proved here:

- exact survival of simple one-sided Bohr zeros under functional-equation symmetrization;
- infinitely many off-line zeros of each sufficiently large symmetrized positive cutoff mixture.

Not proved:

- any claim about the true xi function;
- RH.
