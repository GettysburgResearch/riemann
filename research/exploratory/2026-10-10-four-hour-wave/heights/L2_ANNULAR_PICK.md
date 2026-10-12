# Complete-count discrepancy and an L2 polynomial frame give global order 3500

Status: proposed quantitative theorem under the explicitly imported inputs
below; independent hostile review required. RH remains unproved. Earlier
compact, order-twelve, and maximum-polynomial packets are preserved.

## 1. Result and source boundary

Let `E(z)=xi(1/2+z)`, `F=E'/E`, and
`K(x,y)=(F(x)+F(y))/(x+y)` at positive real nodes. Use the complete squared-pole
source and the exact arbitrary-node congruence in
[ANNULAR_GLOBAL_PICK.md](ANNULAR_GLOBAL_PICK.md), sections 1--2.
Import its same classical source identities, published Trudgian argument
bound, and Platt--Trudgian verified critical-line range through the conservative
`H=3*10^12`. In particular the source-qualified deduction gives

\[
 |N_+(T)-\mathcal M(T)|<\tfrac14\log T\quad(T\ge H),
 \qquad
 \mathcal M'(T)=\frac1{2\pi}\log\frac{T}{2\pi}.
 \tag{L1}
\]

Here `N_+` counts all upper zeros, with multiplicity; one-sided limits handle
zero ordinates. The new argument uses this full discrepancy, rather than
only lower counts in a polynomial peak band.

For any even `256<=n<=3500` and any horizontal bound `a<=A<=1/2`, the following
sufficient criterion certifies every positive-node Pick packet through order
`n`:

\[
 \boxed{\mathcal R(n,A,H):=
 \frac{2025}{32}\frac{n^3}{H}
 +\frac{117045}{4096} A^2\frac{n^6}{H^2}
 +\frac{72}{5} A^2\frac{n^3+3n}{H^2}<1.}
 \tag{L2}
\]

The elementary auxiliary conditions in this proof hold throughout the stated
range and are checked exactly by the replay. At `n=3500,A=1/2`,

\[
 \mathcal R=
 \frac{144936588324740292828797}{160000000000000000000000}
 <\frac{11}{12}.
 \tag{L3}
\]

**Thus the proposed deduction certifies global Pick order 3500 from the
classical strip, complete zero-count discrepancy, and the published verified
height.** Distinct-node packets are positive definite. Repeated-node packets
are positive semidefinite. Node ratios and sizes are unrestricted.
This conclusion does not require the recent quasi-RH theorem.

The imports in (L1) are not rerun here. The analytic inequalities below are
essential; finite arithmetic controls alone are not a global proof.

## 2. Exact polynomial reformulation of an annular source

Fix any `n` distinct positive nodes and write `r=1+1/n`.
Partition the high-height source into `(L,rL]`, `L=H r^k`, `k>=0`.
As before normalize `rho_i=x_i^2/L^2`, `D=prod(1+rho_i)`, and

\[
 \phi(z)=D/\prod_i(\rho_i+z),\qquad \psi_j(z)=z^j\phi(z),\quad j=0,1.
\]

The two moment blocks have size `n/2`. Their quadratic forms are precisely

\[
 \sum_\alpha w_\alpha\psi_j(s_\alpha/L^2)P(s_\alpha/L^2)^2,
 \qquad \deg P\le d=n/2-1.
 \tag{L4}
\]

Conjugate grouping makes these expressions real. We compare each actual pole
with the **real squared height**, rather than with its shifted real part:

\[
 v=b^2/L^2\in[1,r^2],\quad
 \zeta=(-a^2+2iab)/L^2,\quad s/L^2=v+\zeta.
 \tag{L5}
\]

The reference real source in (L4) is positive. Its weight is exactly the
ordinary multiplicity measure `2 dN_+(b)`; both off-line reflected upper
zeros have the same squared height and are counted with their multiplicity.

Set `J=[1,r^2]`, `h=|J|/2=1/n+1/(2n^2)`, and
`t=(v-(1+r^2)/2)/h`. If `R(t)=P(v)`, put

\[
 Q=\int_{-1}^1 R(t)^2\,dt>0.
\]

## 3. Elementary L2 derivative and endpoint estimates

For every real polynomial `R` of degree at most `d`,

\[
 \|R^{(k)}\|_2\le(d+1)^{2k}\|R\|_2,
 \qquad
 |R(\pm1)|^2\le\frac{(d+1)^2}{2}Q.
 \tag{L6}
\]

Here is a proof sufficient for the constants. Let `L_k` denote the Legendre
polynomial with `L_k(1)=1`, and let
`q_k=sqrt((2k+1)/2)L_k` be the orthonormal basis. Integration by parts and
orthogonality give

\[
 L_k'=\sum_{j<k,\,j+k\text{ odd}}(2j+1)L_j.
\]

The derivative matrix in the orthonormal basis has entries
`sqrt((2k+1)(2j+1))` in those positions. Its squared Frobenius norm is at most

\[
 \sum_{j<k}(2j+1)(2k+1)<(d+1)^4.
\]

Hence its operator norm is below `(d+1)^2`; iterate while retaining this
upper degree bound. At either endpoint, the sum of squared basis values is
`sum_{k=0}^d (2k+1)/2=(d+1)^2/2`, giving the trace estimate by
Cauchy--Schwarz. In particular

\[
 \int_{-1}^1 |(R^2)'|\,dt\le2(d+1)^2Q.
 \tag{L7}
\]

These arguments derive the needed L2 inequality directly and do not import a
local-to-global matrix-monotonicity theorem.

## 4. Complete-count quadrature at arbitrary polynomial values

Write `N_+=mathcal M+E`. On the annulus, (L1) gives
`2 max|E|<(9/16)log L`: indeed `r<=9/8`, `log r<1/8`, and `log L>28`.
For any continuously differentiable `g`, Stieltjes integration by parts gives

\[
 \left|2\int_{(L,rL]}g\,dE\right|
 \le\frac9{16}\log L
 \left(|g(L)|+|g(rL)|+\int_L^{rL}|g'|\,db\right).
 \tag{L8}
\]

This is valid for the right-continuous multiplicity count and its one-sided
endpoint conventions; no individual zero is omitted.

The `t` density of `2 dmathcal M` is

\[
 \frac{Lh}{\sqrt v}\frac1{2\pi}
 \log\frac{L\sqrt v}{2\pi}.
\]

Using `pi>3`, `pi<4`, `log(2pi)<3`, `log L>28`, and
`r<=257/256`, this density lies strictly between

\[
 \frac19 Lh\log L\quad\text{and}\quad\frac16 Lh\log L.
 \tag{L9}
\]

For the lower bound, `25/(224r)>1/9` at `r<=257/256` follows from
`6400/57568>1/9`. This deliberately coarse bound is uniform in `L`.

For the unweighted polynomial square, (L6)--(L8) give the sampling estimate

\[
 \sum_\alpha w_\alpha |P(v_\alpha)|^2
 \le Lh\log L\left(\frac16+\frac{27n^3}{64L}\right)Q
 \le\frac15 Lh\log L\,Q.
 \tag{L10}
\]

The endpoint-plus-variation bound is `3(d+1)^2Q=3n^2Q/4`.
The last inequality requires `27n^3/(64H)<=1/30`, which holds even at
`n=3500`. The same bound applies to every real derivative polynomial, whose
degree is still at most `d`.

## 5. Reference positive quadratic form and its quadrature loss

On `J`, `phi(v)>=r^{-2n}>1/8`; `psi_j(v)>1/8` for `j=0,1`, since `v>=1`.
Also `psi_j(v)<2` and `|d psi_j/dv|<=2(n+1)`. Consequently
`|d psi_j/dt|<3` for `n>=8`.
Apply (L8) to `g=psi_j(v)P(v)^2`. Its endpoint-plus-variation norm is at most

\[
 [n^2/2+n^2+3]Q\le(25/16)n^2Q.
\]

Combining with the lower main density in (L9) yields

\[
 \sum_\alpha w_\alpha\psi_j(v_\alpha)P(v_\alpha)^2
 >Lh\log L\,Q\left(\frac1{72}-\frac{225n^3}{256L}\right).
 \tag{L11}
\]

The resulting relative quadrature loss against the main reserve `1/72` is
at most `(2025/32)n^3/L`. The complete argument bound controls a full
polynomial integral, replacing the single-peak frame's `n^8` loss.

## 6. Sampling controls variable complex displacements

The horizontal bound gives

\[
 Z:=\max|\zeta_\alpha|\le\frac{5A}{2L}\le\frac5{4L}.
\]

Indeed `2r<=9/4` and `a^2/L^2<=A/(4L)` at these heights.
Let `D_P=(d+1)^2/h<=n^3/4`. Taylor's finite polynomial series, (L6), the
sampling bound (L10), and the triangle inequality in the weighted discrete
L2 space give, for every `0<=tau<=1`,

\[
 \left(\sum_\alpha w_\alpha
 |P^{(j)}(v_\alpha+\tau\zeta_\alpha)|^2\right)^{1/2}
 \le \kappa D_P^j\sqrt{Lh\log L\,Q/5},
 \quad \kappa=17/16.
 \tag{L12}
\]

The displacements may vary independently with each zero. Each Taylor term
is bounded by `Z^k/k!` times the discrete norm of a real derivative polynomial,
so no constant-displacement assumption is used. The exponential factor is
at most `exp(D_P Z)`, and `D_P Z<=5n^3/(16L)<=1/32` in the stated range.
The elementary `exp(1/32)<32/31<17/16` proves the claimed factor.

## 7. Rational source weights on the displaced segments

On all segments in (L12), `Re z>=1-A^2/L^2`.
Bernoulli's inequality gives

\[
 |\phi(z)|\le(1-A^2/L^2)^{-n}<17/16
\]

provided `n A^2/H^2<1/17`, which holds with a large margin.
Also `|z|<4/3` and `1/|z|<17/16`.
Logarithmic differentiation therefore gives

\[
 |\psi_j|<2,\quad |\psi_j'|<3n,
 \quad |\psi_j''|<4n^2,\qquad j=0,1.
 \tag{L13}
\]

For clarity the derivative upper bounds before rounding are
`2(n+1)(17/16)` and `2(n+1)(n+2)(17/16)^2`.
These estimates remain uniform when node sizes and ratios tend to infinity.

## 8. Integrated strip error

For `f=psi_j P^2`, (L10) and (L13) give the real first-derivative bound

\[
 \sum_\alpha w_\alpha |f'(v_\alpha)|
 \le\frac15 Lh\log L\,Q(n^3+3n).
 \tag{L14}
\]

On displaced segments, (L12)--(L13) give

\[
 \sum_\alpha w_\alpha|f''(v_\alpha+\tau\zeta_\alpha)|
 \le\frac{\kappa^2}{5} Lh\log L\,Q
 [4n^2+12nD_P+8D_P^2]
 \le\frac{\kappa^2}{5}\frac9{16}
 n^6 Lh\log L\,Q.
 \tag{L15}
\]

The last bound uses `4/n^4+3/n^2+1/2<9/16` for `n>=8`.
This step is where L2 sampling removes the polynomial maximum loss.

For each conjugate pair, Taylor expansion at the real squared height has
real linear term `(-a^2/L^2)f'(v)`; the imaginary linear term cancels.
Using `|zeta|^2/2<=25A^2/(8L^2)`, (L14)--(L15), and conjugate weights gives
the total absolute perturbation bounded by

\[
 Lh\log L\,Q\left[
 \frac{A^2}{5L^2}(n^3+3n)
 +\frac{45\kappa^2}{128}A^2\frac{n^6}{L^2}\right].
 \tag{L16}
\]

This includes the real horizontal shift; it is not silently discarded.
The bounds are non-strict when `A=0`.

## 9. Global summation and quantitative meaning

Subtract (L16) from the real reserve (L11), and multiply by `72`.
Since `kappa^2=289/256`, the combined relative bound is exactly (L2), with
`H` replaced by `L`. It decreases as `L` increases. At `n=3500,A=1/2`, (L3)
therefore makes every high annular moment block positive definite for every
nonzero polynomial `P`.

The exact arbitrary-node congruence makes every distinct-node annular Pick
packet positive definite. The source through `H` consists of positive
critical rank-two kernels. Summing all annuli with complete source
convergence proves the global statement. Smaller packets are principal
submatrices after appending nodes; repeated nodes follow by limits or
coefficient-summing congruence.

This argument does not establish all-order positivity. Its leading cost is
`n^3/H`, so the known finite verified height limits the order. A possible
off-line quartet can remain present in a densely populated high annulus
while all these fixed finite orders are positive. The first negative packet,
if one exists, requires more complexity than this bound controls.

The improved quasi-RH strip reduces the explicit `A^2` perturbation term.
At this stage the full-count quadrature error is the dominant term, so the
new strip does not materially raise the rounded order-3500 conclusion.

## 10. Replay and provenance

[verify_l2_annular.py](verify_l2_annular.py) checks all rational sufficient
inequalities, the finite Legendre derivative/endpoint identities, integration
norm controls, and inherited proof hashes in normal and optimized Python.
Its finite controls do not independently prove the imported argument bound,
verified height, or complete Hadamard source. Sections 3--9 are the new
analytic proof; no finite table is promoted to a complete zero spectrum.
