# T-14307 — The complete selected-real-zero kernel floor is equivalent to RH

Claim ID: `T-14307`  
Title: An off-line conjugate pair supplies an exact negative zero-cardinal direction invisible at every selected real zero  
Status: `PROPOSED — COMPLETE CONDITIONAL EQUIVALENCE WITH AN EXPLICIT CAPTURE HYPOTHESIS`  
Authoring agent: `gpt56-pro-09-c`  
Created: 2026-07-31  
Dependencies: the centered Weil zero-sum formula; the Riemann Fourier kernel; `L-14321`; `T-14306`; form-core density  
Scope: the complete-low-packet reading of the second requested bound

## 1. Setting

Write

\[
 \Xi(z)=\xi\!\left(\frac12+iz\right)
       =\int_{\mathbb R}\Phi(t)e^{-izt}\,dt,             \tag{T-14307.1}
\]

with Riemann's real even rapidly decreasing kernel `Phi`.  Let `Q_W` be the
centered Weil form in the normalization

\[
 Q_W(f,g)
 =\sum_{\omega:\Xi(\omega)=0}
   m_\omega\widehat f(\omega)
   \overline{\widehat g(\overline\omega)},               \tag{T-14307.2}
\]

where zeros are listed once with multiplicity `m_omega`.  The exact domain and
regularization are those of the localized Weil criterion; all vectors below
have double-exponential logarithmic tails, so the displayed sums and limiting
arguments lie in that domain.

Let `Z_j` be arbitrary finite sets of certified simple real zeros.  At support
`L_j`, write

\[
 V_j=V_{Z_j},
 \qquad
 U_j^0=U_j\cap\ker V_j.                                  \tag{T-14307.3}
\]

## 2. Cardinal functions at an arbitrary zero

Let `rho` be any zero of `Xi`, not necessarily real, of multiplicity `m`. Put

\[
 A_\rho
 =\lim_{z\to\rho}\frac{\Xi(z)}{(z-\rho)^m}
 =\frac{\Xi^{(m)}(\rho)}{m!}\ne0                         \tag{T-14307.4}
\]

and define the entire cardinal transform

\[
 \boxed{
 L_\rho(z)
 =\frac{\Xi(z)}{A_\rho(z-\rho)^m}.}                      \tag{T-14307.5}
\]

Then

\[
 L_\rho(\rho)=1,
 \qquad
 L_\rho(\omega)=0
 \quad\text{for every zero }\omega\ne\rho.              \tag{T-14307.6}
\]

The inverse Fourier representative `ell_rho` belongs to every fixed Hardy
source space with strip width strictly larger than `|Im rho|`.  More precisely,
iterating the first-order resolvent identity used in `L-14321` gives a finite
sum of terms

\[
 e^{i\rho t}p_k(t)
 \int_{-\infty}^{t}(t-u)^k e^{-i\rho u}\Phi(u)du          \tag{T-14307.7}
\]

and the corresponding right-tail representations.  Since every nontrivial zeta
zero has `|Im rho|<1/2` in centered coordinates and `Phi` has double-exponential
tails, for each fixed `rho`

\[
 \|(I-P_L)\ell_\rho\|_X
 \le C_\rho e^{B_\rho L}e^{-c e^{2L}}.                  \tag{T-14307.8}
\]

For a simple zero this is exactly the two-sided integral formula of `L-14321`.

## 3. A false-RH zero gives an exact negative real-zero-kernel direction

Assume RH is false.  Choose a nonreal centered zero `rho`; then
`bar(rho)` is also a zero, with the same multiplicity `m`.  Define

\[
 h_\rho=\ell_\rho-\ell_{\overline\rho}.                  \tag{T-14307.9}
\]

By (T-14307.6),

\[
 \widehat h_\rho(\rho)=1,
 \qquad
 \widehat h_\rho(\overline\rho)=-1,                     \tag{T-14307.10}
\]

and `h_rho` vanishes at every other zero of `Xi`.  In particular,

\[
 \boxed{V_Zh_\rho=0}                                     \tag{T-14307.11}
\]

for **every** finite or infinite set `Z` of real zeros.

Only the two conjugate-zero summands survive in (T-14307.2), so

\[
 \begin{aligned}
 Q_W(h_\rho,h_\rho)
 &=m\bigl(
  1\cdot\overline{-1}
  +(-1)\cdot\overline{1}
  \bigr)\\
 &=\boxed{-2m}.                                          \tag{T-14307.12}
 \end{aligned}
\]

Thus false RH supplies a fixed exact negative vector in the kernel of every
selected-real-zero evaluation map.  This avoids any infinite projection or
conditioning argument.

## 4. Exact supported kernel vectors

Fix one finite `Z_j`.  Let the supported exact cardinal repair of `T-14306` be

\[
 \widetilde C_{j,L}
 =P_LC_{Z_j}(V_jP_LC_{Z_j})^{-1},
 \qquad
 V_j\widetilde C_{j,L}=I.                                \tag{T-14307.13}
\]

Define

\[
 \boxed{
 k_{j,L}
 =P_Lh_\rho-\widetilde C_{j,L}V_jP_Lh_\rho.}             \tag{T-14307.14}
\]

Then

\[
 V_jk_{j,L}=0                                             \tag{T-14307.15}
\]

exactly.  Since `V_jh_rho=0`,

\[
 V_jP_Lh_\rho=-V_j(I-P_L)h_\rho.                         \tag{T-14307.16}
\]

For fixed finite `Z_j`, (T-14307.8), the Xi-cardinal tail estimate, and the
Neumann bound of `T-14306` imply

\[
 \|k_{j,L}-h_\rho\|_X\longrightarrow0                    \tag{T-14307.17}
\]

as `L->infinity`.  The same holds in the production metric and in the polarized
form topology.  Therefore

\[
 Q_W(k_{j,L},k_{j,L})\longrightarrow-2m,                 \tag{T-14307.18}
\]

and

\[
 \|k_{j,L}\|_{G_L}^2
 \longrightarrow\|h_\rho\|_{G_\infty}^2=:N_\rho^2>0.   \tag{T-14307.19}
\]

Because `Z_j` is finite at each level, one may choose `L_j` diagonally so that

\[
 \boxed{
 V_jk_j=0,
 \qquad
 \frac{Q_W(k_j,k_j)}{\|k_j\|_{G_{L_j}}^2}
 \le-\delta_\rho,}                                      \tag{T-14307.20}
\]

where `k_j=k_(j,L_j)` and any fixed

\[
 0<\delta_\rho<\frac{2m}{N_\rho^2}                       \tag{T-14307.21}
\]

works eventually.  No uniform estimate for the selected real-zero cardinal
condition numbers is needed; the support is chosen after each finite `Z_j`.

## 5. The precise capture hypothesis

A packet hierarchy `U_j` is called **complete in the selected-zero kernel** if,
for every admissible supported sequence `k_j` with `V_jk_j=0` and uniformly
bounded form/metric norm, there are `u_j in U_j^0` such that

\[
 \|u_j-k_j\|_{\mathfrak q,G}\longrightarrow0.            \tag{T-14307.22}
\]

It is sufficient to require (T-14307.22) only for the off-line-cardinal
sequences (T-14307.14).  Ordinary `L2` density is not sufficient; the topology
must control `Q_W` and the denominator metric.

Under (T-14307.22), false RH and (T-14307.20) give vectors `u_j in U_j^0` with

\[
 \frac{Q_W(u_j,u_j)}{\|u_j\|_{G_{L_j}}^2}
 \le-\frac{\delta_\rho}{2}                               \tag{T-14307.23}
\]

for every sufficiently large `j`.

Consequently no estimate

\[
 \inf_{0\ne f\in U_j^0}
 \frac{Q_W(f,f)}{\|f\|_{G_{L_j}}^2}
 \ge-\varepsilon_j,
 \qquad \varepsilon_j\to0,                              \tag{T-14307.24}
\]

can hold under false RH.

## 6. Equivalence theorem

Assume:

1. `Z_j` consists only of certified real zeros;
2. the supported-cardinal repair is domain-valid and its tails tend to zero;
3. `U_j` is complete in the selected-zero kernel in the sense of
   (T-14307.22).

Then

\[
 \boxed{
 \mathrm{RH}
 \quad\Longleftrightarrow\quad
 \exists\varepsilon_j\downarrow0:\
 \inf_{0\ne f\in U_j,\,V_jf=0}
 \frac{Q_W(f,f)}{\|f\|_{G_{L_j}}^2}
 \ge-\varepsilon_j.}                                    \tag{T-14307.25}
\]

### Proof of the forward implication

Under RH every centered zero is real.  Every summand in (T-14307.2) is then

\[
 m_\gamma|\widehat f(\gamma)|^2\ge0,
\]

so `Q_W(f,f)>=0` on the entire form domain.  Take `epsilon_j=0`.

### Proof of the reverse implication

If RH were false, Sections 3--5 would produce `u_j in U_j^0` satisfying
(T-14307.23), contradicting `epsilon_j->0`.  QED.

## 7. Why the capture condition cannot be omitted

Without kernel completeness, (T-14307.24) can be vacuous.  For example, if
`V_j|_(U_j)` is injective, then

\[
 U_j^0=\{0\}
\]

and the infimum contains no nonzero vector.  More generally a hierarchy may
systematically omit the off-line-cardinal direction.

Therefore the pair requested by the user has the following exact status:

- `T-14306` proves it for an explicitly constructed cofinal packet;
- `T-14307` proves that its complete-low-packet reading, with the necessary
  kernel-capture property, is equivalent to RH;
- the remaining theorem is precisely the capture/saturation of the complete
  dangerous low index by the constructed cardinal–radical packet.

## 8. Relation to the finite saturation routes

The capture condition may be discharged without a direct principal-angle
proof.  Any of the following suffices:

1. exact low-index saturation by `L-15604/T-15602`;
2. the automatic weighted-deficit trace margin of `L-15612`;
3. a complete visible Schur margin as in `L-15306/L-15307`;
4. a source-frame theorem proving the growing packet equals the complete low
   spectral subspace.

These are alternative formulations of the same missing global capture, not
additional tail estimates.

## 9. Proof boundary

- The off-line-cardinal negative direction is explicit and unconditional under
  the assumption that an off-line zero exists.
- Multiple zeros are handled by (T-14307.5); no simplicity assumption on the
  hypothetical off-line zero is used.
- The selected sets may grow arbitrarily fast; diagonal support selection
  absorbs every finite conditioning constant.
- Kernel completeness is load bearing and cannot be inferred from packet
  dimension alone.
- The theorem does not assert RH because no current artifact proves that the
  production low packet satisfies (T-14307.22) or an equivalent saturation
  certificate.
