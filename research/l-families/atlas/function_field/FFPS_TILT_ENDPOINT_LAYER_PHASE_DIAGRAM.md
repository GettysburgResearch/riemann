# Large tilt creates a Gamma endpoint layer and fixes the safe moving-tilt window

Status: **exact fixed-rung endpoint-layer asymptotic through the first energy
correction, exact first-rung BV formula, and a sufficient moving-tilt RH-forward
window; no new beta estimate, converse outside the safe window, or proof of RH**

Bounded replay:
[ffps_tilt_endpoint_layer_phase_diagram.py](ffps_tilt_endpoint_layer_phase_diagram.py).
Canonical summary:
[ffps_tilt_endpoint_layer_phase_diagram.json](ffps_tilt_endpoint_layer_phase_diagram.json).

Frozen source: the spectral-zero-free carrier tilt at commit
**805ab873cb051c739f19978ebb772b2625adcffb**. The producer pins the
four source blobs and imports no live predecessor module.

## 0. Outcome

The small-tilt packet gives an energy cost quadratic in the tilt. This packet
determines the opposite regime and then joins both ends into a safe moving-tilt
criterion.

Fix a derivative rung \(m\ge1\), support \(S>0\), and put
\(T=|\tau|\). For the normalized centered beta moment-generating function,

\[
 \boxed{
 \Phi_m(T)
 =\frac{(2m+1)!}{2^{m+1}m!}
 e^T T^{-m-1}
 \left(1-\frac{m(m+1)}{2T}+O_m(T^{-2})\right).}
\tag{0.1}
\]

In the favored-endpoint coordinate

\[
 u=T(1-\operatorname{sgn}(\tau)x),
 \qquad \lambda=\frac{2T}{S},
\tag{0.2}
\]

the positive carrier converges after rescaling to the Gamma density

\[
 g_m(u)=\frac{u^me^{-u}}{m!},
 \qquad u\ge0.
\tag{0.3}
\]

Its \(m\)-th derivative is

\[
 g_m^{(m)}(u)=e^{-u}L_m(u),
\tag{0.4}
\]

where \(L_m\) is the ordinary Laguerre polynomial. The carrier energy therefore
has the sharp expansion

\[
 \boxed{
 \|D^mQ_{m,S,\tau}\|_2^2
 =\binom{2m}{m}\frac{T^{2m+1}}{S^{2m+1}}
 \left(1+\frac{m(2m+1)}{2T}+O_m(T^{-2})\right).}
\tag{0.5}
\]

Thus a large tilt does not cheaply improve conditioning. It concentrates the
carrier into an effective physical width

\[
 w=\frac{S}{2T}
\tag{0.6}
\]

and pays

\[
 \boxed{
 \|D^mQ_{m,S,\tau}\|_2^2
 \sim\frac{\binom{2m}{m}}{2^{2m+1}}w^{-2m-1}.}
\tag{0.7}
\]

At fixed support, the endpoint-layer energy diverges like \(T^{2m+1}\). The
limit density itself lives on a rescaled half-line and is not an admissible
compact Sobolev carrier at \(T=\infty\).

## 1. Endpoint expansion and Laguerre energy

At the favored endpoint write \(x=1-u/T\). Then

\[
 (1-x^2)^m
 =\left(\frac{2u}{T}\right)^m
 \left(1-\frac{mu}{2T}+O_m(T^{-2}(1+u^2))\right),
\tag{1.1}
\]

and \(e^{Tx}=e^Te^{-u}\). Watson's endpoint expansion, here obtainable by
termwise integration against \(u^me^{-u}\), gives (0.1).

After normalization, the rescaled density has the first correction

\[
 g_{m,T}(u)
 =g_m(u)
 \left(1+\frac{m}{2T}(m+1-u)+O_m(T^{-2}(1+u^2))\right).
\tag{1.2}
\]

Differentiating \(m\) times gives

\[
 g_{m,T}^{(m)}(u)
 =e^{-u}L_m(u)
 +\frac{m(m+1)}{2T}e^{-u}L_{m+1}(u)
 +O_m(T^{-2})
\tag{1.3}
\]

in the weighted \(L^2\) norm needed below. The exact Laguerre integrals are

\[
 \int_0^\infty e^{-2u}L_m(u)L_n(u)\,du
 =\frac{\binom{m+n}{m}}{2^{m+n+1}}.
\tag{1.4}
\]

In particular,

\[
 \int_0^\infty e^{-2u}L_m(u)^2\,du
 =\frac{\binom{2m}{m}}{2^{2m+1}},
\tag{1.5}
\]

and the ratio of the \(m,m+1\) cross integral to (1.5) is
\((2m+1)/(2m+2)\). Combining (1.3) with

\[
 D_t^mQ_{m,S,\tau}=(-1)^m\lambda^{m+1}g_{m,T}^{(m)}
\tag{1.6}
\]

proves both coefficients in (0.5). The bounded replay verifies (1.4)--(1.5)
exactly with rational polynomial integration for \(1\le m\le6\).

## 2. Complete first-rung large-tilt expansion

For \(m=1\), the hyperbolic formula in the frozen packet can be reorganized as

\[
 S^3E_1(T)
 =\frac{T^3}{2}
 \frac{(4T^2-2T+1)-e^{-4T}(4T^2+2T+1)}
 {((T-1)+e^{-2T}(T+1))^2}.
\tag{2.1}
\]

Polynomial division gives

\[
 \boxed{
 S^3E_1(T)
 =2T^3+3T^2+\frac92T+6+O(T^{-1}).}
\tag{2.2}
\]

Exponentially small terms are absorbed by the displayed remainder. The first
two coefficients agree with (0.5), and the next two provide a stringent exact
check of the endpoint calculation.

## 3. Exact first-rung bounded-variation geometry

Write \(J=DQ_{1,S,\tau}\). With \(x=2t/S-1\),

\[
 J(t)
 =\frac{3e^{Tx}}{S^2\Phi_1(T)}
 \left(T(1-x^2)-2x\right)
\tag{3.1}
\]

up to reflection, which does not alter its norms. For every \(T\ge0\),

\[
 \boxed{
 \|J\|_\infty=\frac{6e^T}{S^2\Phi_1(T)}.}
\tag{3.2}
\]

The total variation of the zero-extended detector is

\[
 \boxed{
 \operatorname{Var}_{\mathbb R}J
 =\frac{24\cosh T}{S^2\Phi_1(T)},
 \qquad 0\le T\le\frac12,}
\tag{3.3}
\]

and, with \(r=\sqrt{T^2+2}\),

\[
 \boxed{
 \operatorname{Var}_{\mathbb R}J
 =\frac{12}{S^2\Phi_1(T)}
 \left(e^T+\frac{r-1}{T}e^{r-2}\right),
 \qquad T\ge\frac12.}
\tag{3.4}
\]

The two expressions meet at \(T=1/2\). The transition occurs when the sole
interior extremum reaches the endpoint geometry. In particular,

\[
 \|J\|_\infty+\operatorname{Var}J
 \sim4(3+2e^{-2})\frac{T^2}{S^2},
 \qquad
 \|J\|_1\sim\frac{4T}{eS}.
\tag{3.5}
\]

For fixed general \(m\), the endpoint layer similarly gives

\[
 \|D^mQ\|_\infty\asymp_m\lambda^{m+1},
 \quad
 \operatorname{Var}(D^mQ)\asymp_m\lambda^{m+1},
 \quad
 \|D^mQ\|_1\asymp_m\lambda^m.
\tag{3.6}
\]

Only the fixed-rung power laws, rather than a uniform growing-\(m\) constant,
are used below.

## 4. A moving-tilt RH-forward bound

Let

\[
 \ell=\log X,
 \qquad L=S+\ell,
 \qquad \Lambda=1+|\tau|,
\tag{4.1}
\]

and let \(B_0^*(X)=\sup_{y\le X}|B_0(y)|\). For the translated detector
\(H=J*\mu_X\), log-coordinate Abel summation and Young's convolution inequality
give the useful \(L^2\) estimate

\[
 \boxed{
 \|H\|_2
 \le |B_0(X)|\|J\|_2
 +B_0^*(X)\sqrt\ell\,\operatorname{Var}_{\mathbb R}J.}
\tag{4.2}
\]

The endpoint asymptotics plus compactness on every finite \(T\)-interval imply,
for fixed \(m\),

\[
 \|J\|_2^2\ll_m\frac{\Lambda^{2m+1}}{S^{2m+1}},
 \qquad
 \operatorname{Var}J\ll_m\frac{\Lambda^{m+1}}{S^{m+1}}.
\tag{4.3}
\]

Under RH, \(B_0^*(X)=X^{o(1)}\). Squaring (4.2), absorbing constants and the
mixed term, yields

\[
 \boxed{
 \mathcal E_{m,S,\tau}(X)
 \le X^{o(1)}\left[
 \left(\frac\Lambda S\right)^{2m+1}
 +\ell\left(\frac\Lambda S\right)^{2m+2}
 \right].}
\tag{4.4}
\]

For the RH-equivalent critical normalization

\[
 \mathcal R=L^{2m+1}\mathcal E,
 \quad
 \Theta=\frac{\Lambda L}{S},
 \quad
 \mathsf H=\frac{\Lambda\ell}{S},
\tag{4.5}
\]

one obtains

\[
 \mathcal R
 \le X^{o(1)}\Theta^{2m+1}(1+\mathsf H).
\tag{4.6}
\]

Hence the sharp sufficient window supplied by this bound is

\[
 \boxed{
 (2m+1)\log\Theta+\log(1+\mathsf H)=o(\log X).}
\tag{4.7}
\]

The simpler condition

\[
 \boxed{
 (1+|\tau_X|)\frac{L_X}{S_X}=X^{o(1)}}
\tag{4.8}
\]

is sufficient. Because \(S_X\ge1\) implies \(L_X/S_X\le1+\log X\), every
subpower tilt \(|\tau_X|=X^{o(1)}\) is safe uniformly over every such support
schedule, for each fixed \(m\).

The reverse implication to RH is unchanged: the matched moment and support
projection do not depend on the tilt. Thus (4.7), together with the frozen
reverse inequality, gives the moving-tilt RH equivalence inside this safe
window.

## 5. Raw versus critical power phase diagrams

Suppose

\[
 S=X^{\sigma+o(1)},
 \qquad T=X^{\alpha+o(1)},
 \qquad \sigma>0,\quad\alpha\ge0,
\tag{5.1}
\]

with \(m\) fixed. The two terms of the raw RH-forward bound (4.4) have power
exponents

\[
 (2m+1)(\alpha-\sigma),
 \qquad
 (2m+2)(\alpha-\sigma).
\tag{5.2}
\]

Therefore

\[
 \boxed{\alpha\le\sigma
 \quad\Longrightarrow\quad
 \mathcal E_{m,S,\tau}(X)=X^{o(1)}\quad\text{under RH}.}
\tag{5.3}
\]

This raw-energy region is deliberately not called RH-equivalent. Multiplying by
the critical \(L^{2m+1}\) changes the power exponents to

\[
 (2m+1)\alpha,
 \qquad
 (2m+2)\alpha-\sigma.
\tag{5.4}
\]

Any polynomial tilt already makes the first exponent positive. The current
information therefore does not certify polynomial tilt for the critical
normalization, even when raw energy is subpower. This is a limitation of the
bound, not a converse theorem proving failure outside (4.7).

The improvement over a crude support-length estimate in (5.3) is real: the
tilted detector is exponentially localized near one endpoint, so the \(L^2\)
Abel estimate does not pay the long but almost empty formal support tail.

## 6. Orientation and firewalls

All energy and BV norms are even in \(\tau\). The RH-forward estimate works for
either sign. If a later Mellin--Landau argument divides by the carrier Laplace
transform in the closed right half-plane, the orientation remains load-bearing:
one must retain \(\tau>0\), which puts the carrier zero line in the left
half-plane.

| statement | grade |
|---|---|
| fixed-rung Gamma endpoint layer | **PROVED** |
| energy leading constant and first correction | **PROVED EXACT** |
| exact first-rung BV formula | **PROVED EXACT** |
| moving-tilt bound (4.4) under RH | **PROVED** |
| critical safe window (4.7) | **PROVED SUFFICIENT** |
| raw power chart (5.3) | **PROVED SUFFICIENT UNDER RH** |
| polynomial tilt fails outside the safe window | **NOT PROVED** |
| new unconditional beta estimate | **NOT PROVED** |
| RH or GRH | **NOT PROVED** |

The packet fixes \(m\) before \(T\to\infty\). It does not assert uniformity in
a joint growing-rung endpoint limit.

The Gamma layer concerns a carrier approaching a support endpoint, not a Gamma
factor of a completed \(L\)-function.

No external novelty or priority is claimed.

## 7. Bounded replay

The producer:

- verifies the frozen spectral-tilt quartet by full Git blob ID;
- expands the endpoint normalization constants and verifies the energy leading
  constant and first correction through exact Laguerre integrals for
  \(1\le m\le6\);
- records the exact first-rung algebraic coefficients
  \(2,3,9/2,6\), the raw and critical power charts, and the safe-window algebra;
- checks the first-rung BV branches at four fixed tilt values, including their
  join at \(T=1/2\);
- performs no beta sum, prime enumeration, zeta evaluation, Bessel-root search,
  random sampling, quadrature, or curve computation.

~~~text
python -B research/l-families/atlas/function_field/ffps_tilt_endpoint_layer_phase_diagram.py --check
python -O -B research/l-families/atlas/function_field/ffps_tilt_endpoint_layer_phase_diagram.py --check
python -B -m unittest tests.test_ffps_tilt_endpoint_layer_phase_diagram
python -O -B -m unittest tests.test_ffps_tilt_endpoint_layer_phase_diagram
python -m ruff check research/l-families/atlas/function_field/ffps_tilt_endpoint_layer_phase_diagram.py tests/test_ffps_tilt_endpoint_layer_phase_diagram.py
python -m ruff format --check research/l-families/atlas/function_field/ffps_tilt_endpoint_layer_phase_diagram.py tests/test_ffps_tilt_endpoint_layer_phase_diagram.py
~~~
