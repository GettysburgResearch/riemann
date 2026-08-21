# L-21912 — Generalized-Stieltjes interface for the Xi Mellin zeros

Claim ID: `L-21912`  
Title: A positive generalized Stieltjes representation of the logarithmic-curvature function of the canonical Xi interpolant forces every one of its zeros to be real and negative  
Status: **PROPOSED EXACT CONDITIONAL LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-02-p`  
Created: 2026-08-07  
Updated: 2026-08-07 after the Hadamard-constant and continuum-shadow audit  
Dependencies: `L-21910`, `T-21904`, `L-21914`; Sokal's characterization of generalized Stieltjes functions  
Scope: explicit positive-measure form of the final real-rootedness theorem

## 1. The tilted logarithmic law

For real

\[
 x>-\frac12,
\]

put

\[
 Z_\Xi(x)=\int_0^\infty u^{2x}\Phi(u)\,du
 \tag{L-21912.1}
\]

and define the probability law

\[
 \boxed{
 d\mathbb P_x(u)
 =\frac{u^{2x}\Phi(u)}{Z_\Xi(x)}\,du.}
 \tag{L-21912.2}
\]

Let

\[
 Y=\log u
\]

under `P_x`, and denote its cumulants by

\[
 \kappa_r(x),
 \qquad r=1,2,\ldots.
 \tag{L-21912.3}
\]

The superexponential decay of `Phi` makes every logarithmic moment finite.
Differentiation under the integral gives

\[
 \boxed{
 \frac{d^r}{dx^r}\log Z_\Xi(x)
 =2^r\kappa_r(x).}
 \tag{L-21912.4}
\]

## 2. Exact cumulant formula for the canonical interpolant

On the positive half-line, `L-21910` gives

\[
 C_\Xi(x)
 =\operatorname{const}\,
 4^{-x}\Gamma\!\left(x+\frac12\right)^{-1}Z_\Xi(x).
 \tag{L-21912.5}
\]

Therefore

\[
 \boxed{
 (\log C_\Xi)'(x)
 =-\log4-\psi\!\left(x+\frac12\right)
  +2\kappa_1(x),}
 \tag{L-21912.6}
\]

and, for every integer `r>=2`,

\[
 \boxed{
 (\log C_\Xi)^{(r)}(x)
 =2^r\kappa_r(x)
  -\psi_{r-1}\!\left(x+\frac12\right),}
 \tag{L-21912.7}
\]

where `psi_j` is the polygamma function of order `j`.

Define the logarithmic-curvature function

\[
 \boxed{
 \mathcal S_\Xi(z)
 =-\frac{d^2}{dz^2}\log C_\Xi(z)
 =\left(\frac{C_\Xi'}{C_\Xi}\right)^2
  -\frac{C_\Xi''}{C_\Xi}.}
 \tag{L-21912.8}
\]

On the real half-line,

\[
 \boxed{
 \mathcal S_\Xi(x)
 =\psi_1\!\left(x+\frac12\right)
  -4\operatorname{Var}_x(Y).}
 \tag{L-21912.9}
\]

More generally,

\[
 \boxed{
 \mathcal S_\Xi^{(n)}(x)
 =\psi_{n+1}\!\left(x+\frac12\right)
  -2^{n+2}\kappa_{n+2}(x).}
 \tag{L-21912.10}
\]

Thus the entire zero problem has been rewritten as an all-order comparison
between one tilted logarithmic cumulant sequence and the gamma cumulants.

## 3. A generalized Stieltjes certificate

A real function belongs to the generalized Stieltjes class of order two when it
has a representation

\[
 f(z)=a+
 \int_{[0,\infty)}\frac{d\rho(t)}{(z+t)^2},
 \qquad a\ge0,\quad\rho\ge0,
 \tag{L-21912.11}
\]

on the slit plane, with the usual convergence condition.

The proof-facing certificate proposed here is

\[
 \boxed{
 \mathcal S_\Xi(z)
 =a+\int_{[1/2,\infty)}
   \frac{d\rho_\Xi(t)}{(z+t)^2},
 \qquad a\ge0,\quad\rho_\Xi\ge0.}
 \tag{L-21912.12}
\]

The support starts at `1/2` because `C_Xi(x)>0` for every real `x>-1/2`.

## 4. Why the certificate forces real-negative zeros

Let `lambda` be a zero of `C_Xi` of multiplicity `m`. Locally,

\[
 C_\Xi(z)=(z-\lambda)^m h(z),
 \qquad h(\lambda)\ne0,
\]

and hence

\[
 \boxed{
 \mathcal S_\Xi(z)
 =\frac{m}{(z-\lambda)^2}
  +\text{holomorphic}.}
 \tag{L-21912.13}
\]

The right side of (L-21912.12) is holomorphic off the negative real ray
`(-infinity,-1/2]`. Therefore (L-21912.13) is incompatible with any nonreal
zero or any real zero to the right of `-1/2`.

Consequently

\[
 \boxed{
 \mathcal S_\Xi\in\mathcal S_2
 \text{ with support in }[1/2,\infty)
 \Longrightarrow
 C_\Xi\text{ has only real zeros below }-1/2.}
 \tag{L-21912.14}
\]

By `T-21904`, this implies

\[
 \boxed{\mathrm{RH}.}
 \tag{L-21912.15}
\]

No zero-spacing, simplicity, Bernstein interpolation, or Pick hypothesis is
needed.

## 5. Converse geometry and the Hadamard constant

Suppose conversely that all zeros of `C_Xi` are real and equal to
`-alpha_j`, with multiplicities `m_j`, where `alpha_j>=1/2`, and that

\[
 \sum_j\frac{m_j}{(1+\alpha_j)^2}<\infty.
 \tag{L-21912.16}
\]

A genus-one Hadamard representation gives

\[
 \boxed{
 \mathcal S_\Xi(z)
 =a_0+\sum_j\frac{m_j}{(z+\alpha_j)^2}}
 \tag{L-21912.17}
\]

for one real constant `a_0` determined by the quadratic exponential factor of
the entire function.

Real-rootedness alone does **not** force `a_0>=0`. The positive Stieltjes
representation (L-21912.12) is equivalent to the zero geometry together with

\[
 \boxed{a_0\ge0.}
 \tag{L-21912.18}
\]

For a genuine Laguerre–Pólya representation the Gaussian factor is
`exp(-a z^2)` with `a>=0`, and then `a_0=2a>=0`. Without that sign, the converse
is only a signed-constant representation.

When (L-21912.18) holds, the representing measure is

\[
 d\rho_\Xi(t)=\sum_jm_j\delta_{\alpha_j}(dt).
 \tag{L-21912.19}
\]

The atomic weights are the zero multiplicities because the left side is a
logarithmic derivative of an entire function.

## 6. Real-variable proof protocol

Sokal's theorem gives a complete real-variable characterization of the class
`S_2`. For a smooth real function `f` on `(0,infinity)`, define

\[
 \boxed{
 F_{n,k}^{[2]}(x)
 =(-1)^n
  \sum_{j=0}^k{\binom kj}
  \frac{\Gamma(n+k+2)}{\Gamma(n+j+2)}
  x^j f^{(n+j)}(x).}
 \tag{L-21912.20}
\]

Then

\[
 \boxed{
 f\in\mathcal S_2
 \quad\Longleftrightarrow\quad
 F_{n,k}^{[2]}(x)\ge0
 \text{ for all }n,k\ge0,\ x>0.}
 \tag{L-21912.21}
\]

Apply this to the translated function

\[
 f(x)=\mathcal S_\Xi(x-1/2),
 \qquad x>0.
 \tag{L-21912.22}
\]

Using (L-21912.10), every inequality in (L-21912.21) becomes an explicit finite
linear combination of:

```text
polygamma values;
tilted logarithmic cumulants of Phi;
positive powers of x.
```

This is the exact all-order final theorem. It is a family of real inequalities,
not a contour, zero census, or unbounded matrix packet.

## 7. The first continuum member is closed

The weakest member is

\[
 \mathcal S_\Xi(x)>0,
 \tag{L-21912.23}
\]

or equivalently

\[
 \boxed{
 4\operatorname{Var}_x(\log u)
 <\psi_1\!\left(x+\frac12\right).}
 \tag{L-21912.24}
\]

`L-21914` proves this for every real `x>-1/2` by an exact change of variables
from Csordas–Varga Proposition 2.3. Thus

\[
 \boxed{F_{0,0}^{[2]}(x)>0\quad(x>0)}
 \tag{L-21912.25}
\]

is closed on the complete continuum, not merely at integer moments.

The remaining Sokal inequalities have `n+k>0`. The classical theorem does not
supply them.

## 8. What a genuine completion must do

A proof of (L-21912.12) may proceed in either of two equivalent ways.

### Positive-measure construction

Construct `rho_Xi` directly from the theta series, ideally by writing

\[
 \psi_1\!\left(x+\frac12\right)
 -4\operatorname{Var}_x(\log u)
 =a+\int_{1/2}^\infty\frac{d\rho_\Xi(t)}{(x+t)^2}.
 \tag{L-21912.26}
\]

### Real-variable hierarchy

Prove every inequality in (L-21912.21), with the cumulant substitutions from
(L-21912.10).

A proof of complete monotonicity alone is insufficient: generalized Stieltjes
membership is strictly stronger, and the extra `k`-indexed inequalities are
load bearing.

## 9. Status boundary

Closed exactly:

- the tilted cumulant formulas;
- the explicit logarithmic-curvature function;
- generalized Stieltjes representation implies real-negative zeros;
- the Sokal real-variable certificate;
- the continuum first member;
- the corrected Hadamard-constant scope.

Open:

- construction of the positive measure `rho_Xi`;
- the inequalities (L-21912.21) with `n+k>0`;
- real-rootedness of `C_Xi`;
- RH.

This lemma turns the final component into one precise positive-measure problem
but does not assert that the measure has been constructed.