# L-91323 — Every physical Hardy input has a conservative model/amplitude/leakage delay colligation

Claim ID: `L-91323`  
Status: **PROVED EXACT THREE-CHANNEL HARDY DELAY COLLIGATION**  
Created: 2026-08-13  
Depends on: `L-91322`, `R-91011`, `L-91035`  
Upgrades: the physical-input/base-map item left open in `L-91322`  
RH status: **unproved**

## 1. Canonical coordinates for the full positive Hardy space

Let `Theta` be inner on the upper half-plane and write

\[
 H^2_+=K_\Theta\ \widehat\oplus\ \Theta H^2_+.
 \tag{L-91323.1}
\]

The map

\[
 \boxed{
 \mathcal U_\Theta(g,q)=g+\Theta q
 }
 \tag{L-91323.2}
\]

is unitary from $K_\Theta\oplus H^2_+$ onto `H^2_+`.

On the output side use the orthogonal decomposition

\[
 L^2(\mathbb R)
 =K_\Theta\ \widehat\oplus\ \Theta H^2_+
 \ \widehat\oplus\ H^2_-.
 \tag{L-91323.3}
\]

Let `P_Theta` denote the projection onto `Theta H^2_+`. The coordinate map

\[
 \boxed{
 \mathcal W_\Theta F
 =\left(
 P_{K_\Theta}F,
 M_{\overline\Theta}P_\Theta F,
 P_-F
 \right)
 }
 \tag{L-91323.4}
\]

is unitary from `L^2` onto
$K_\Theta\oplus H^2_+\oplus H^2_-$.

## 2. Raw delay as a three-channel isometry

For `tau>=0`, define

\[
 \boxed{
 \mathcal V_{\Theta,\tau}
 =\mathcal W_\Theta
  M_{e^{-i\tau\,\cdot}}
  \mathcal U_\Theta.
 }
 \tag{L-91323.5}
\]

Since the middle multiplier is unitary on `L^2` and `U_Theta` is an isometry
into `L^2`, `V_(Theta,tau)` is an isometry

\[
 K_\Theta\oplus H^2_+
 \longrightarrow
 K_\Theta\oplus H^2_+\oplus H^2_-.
 \tag{L-91323.6}
\]

Retain the resident and leakage operators of `L-91322`:

\[
 T_\tau=P_{K_\Theta}M_{e^{-i\tau\,\cdot}}|_{K_\Theta},
 \qquad
 L_\tau^K=P_-M_{e^{-i\tau\,\cdot}}|_{K_\Theta}.
 \tag{L-91323.7}
\]

Define the amplitude-to-model forcing and amplitude leakage by

\[
 \boxed{
 B_\tau
 =P_{K_\Theta}M_{e^{-i\tau\,\cdot}}M_\Theta:
 H^2_+\to K_\Theta,
 }
 \tag{L-91323.8}
\]

\[
 \boxed{
 L_\tau^\Theta
 =P_-M_{e^{-i\tau\,\cdot}}M_\Theta:
 H^2_+\to H^2_-.
 }
 \tag{L-91323.9}
\]

Then

\[
 \boxed{
 \mathcal V_{\Theta,\tau}
 \binom{g}{q}
 =
 \begin{pmatrix}
  T_\tau & B_\tau\\
  0 & S_\tau^*\\
  L_\tau^K & L_\tau^\Theta
 \end{pmatrix}
 \binom{g}{q}.
 }
 \tag{L-91323.10}
\]

The zero in the lower-left positive-Hardy block is exact. Indeed,
`bar Theta g` belongs to `H^2_-`, and multiplication by
`exp(-i tau dot)` preserves `H^2_-`. The amplitude block is exactly `S_tau^*`
because the two `Theta` multipliers cancel before applying `P_+`.

The forcing block has the useful commutator form

\[
 \boxed{
 B_\tau
 =S_\tau^*M_\Theta-M_\Theta S_\tau^*.
 }
 \tag{L-91323.11}
\]

Thus a delayed physical input need not begin in the model space. Its completed
amplitude coordinate drives the resident model state through one explicit
Hardy commutator.

## 3. Full polarized packet identity

For any finite packet

\[
 F_j=g_j+\Theta q_j\in H^2_+,
 \qquad
 \tau_j\ge0,
 \qquad
 c_j\in\mathbb C,
\]

orthogonality of the three output channels gives

\[
\boxed{
\begin{aligned}
 \left\|
  \sum_jc_je^{-i\tau_j\,\cdot}F_j
 \right\|_{L^2}^2
 ={}&
 \left\|
  \sum_jc_j(T_{\tau_j}g_j+B_{\tau_j}q_j)
 \right\|_{K_\Theta}^2\\
 &+
 \left\|
  \sum_jc_jS_{\tau_j}^*q_j
 \right\|_{H^2_+}^2\\
 &+
 \left\|
  \sum_jc_j(L_{\tau_j}^Kg_j+L_{\tau_j}^\Theta q_j)
 \right\|_{H^2_-}^2.
\end{aligned}}
 \tag{L-91323.12}
\]

This is the exact full cross-carrier and cross-delay Gram decomposition for
arbitrary positive-Hardy inputs. No assumption `F_j in K_Theta` is needed.

## 4. Upper-triangular state semigroup and leakage cocycle

The positive-Hardy state transition in the coordinates (L-91323.1) is

\[
 \mathcal R_{\Theta,\tau}
 =\mathcal U_\Theta^*S_\tau^*\mathcal U_\Theta
 =
 \begin{pmatrix}
  T_\tau&B_\tau\\
  0&S_\tau^*
 \end{pmatrix}.
 \tag{L-91323.13}
\]

Therefore

\[
 \boxed{
 \mathcal R_{\Theta,\tau+\sigma}
 =\mathcal R_{\Theta,\tau}
  \mathcal R_{\Theta,\sigma}.
 }
 \tag{L-91323.14}
\]

Besides the semigroup laws for the diagonal blocks, the off-diagonal forcing
obeys

\[
 \boxed{
 B_{\tau+\sigma}
 =T_\tau B_\sigma+B_\tau S_\sigma^*.
 }
 \tag{L-91323.15}
\]

Let

\[
 \mathcal E_{\Theta,\tau}(g,q)
 =L_\tau^Kg+L_\tau^\Theta q.
 \tag{L-91323.16}
\]

With `U^-_tau` the negative-Hardy delay, the escaped prefix satisfies

\[
 \boxed{
 \mathcal E_{\Theta,\tau+\sigma}
 =\mathcal E_{\Theta,\tau}
  \mathcal R_{\Theta,\sigma}
 +U^-_\tau\mathcal E_{\Theta,\sigma}.
 }
 \tag{L-91323.17}
\]

Equations (L-91323.14)--(L-91323.17) are the conservative state-space law for
an arbitrary positive-Hardy physical input.

## 5. Explicit resident coordinates for the Cauchy mother

The causal rational factor of `L-91031` belongs to `H^2_+`. For a carrier `x`,
write

\[
 F_{a,x}(u)=\Psi_a(u-x).
 \tag{L-91323.18}
\]

Its canonical Suzuki coordinates are

\[
 \boxed{
 g_{a,x}=P_{K_{\Theta_a}}F_{a,x},
 \qquad
 q_{a,x}=P_+(\overline{\Theta_a}F_{a,x}),
 \qquad
 F_{a,x}=g_{a,x}+\Theta_aq_{a,x}.
 }
 \tag{L-91323.19}
\]

These coordinates are explicit, not existential. Put

\[
 w_r=x+ira,
 \qquad r\in\{1,2,4\}.
\]

The exact partial fraction formula of `R-91008` writes `F_(a,x)` as a finite
linear combination of

\[
 (u-\overline{w_r})^{-1},
 \qquad
 (u-\overline{w_r})^{-2}.
\]

For every `w in C_+`, model-space projection gives

\[
 \boxed{
 P_{K_\Theta}\frac1{u-\overline w}
 =\frac{1-\overline{\Theta(w)}\Theta(u)}
        {u-\overline w},
 }
 \tag{L-91323.20}
\]

and differentiation in `bar w` gives

\[
 \boxed{
 P_{K_\Theta}\frac1{(u-\overline w)^2}
 =\frac{1-\overline{\Theta(w)}\Theta(u)}
        {(u-\overline w)^2}
 -\frac{\overline{\Theta'(w)}\Theta(u)}
        {u-\overline w}.
 }
 \tag{L-91323.21}
\]

Substituting the five exact partial-fraction coefficients from `R-91008`
therefore expresses `g_(a,x)` through the six finite data

```text
Theta_a(w_1), Theta_a'(w_1),
Theta_a(w_2), Theta_a'(w_2),
Theta_a(w_4), Theta_a'(w_4).
```

The delayed resident physical vector is now exactly

\[
 \boxed{
 r_{a,x,\tau}
 =T_{\Theta_a,\tau}g_{a,x}
  +B_{\Theta_a,\tau}q_{a,x}.
 }
 \tag{L-91323.22}
\]

This closes the physical Cauchy input-to-resident-coordinate map left open in
`L-91322`. It also shows why simply applying `T_(Theta,tau)` to the model
component can be incomplete: the completed amplitude component contributes the
forcing term `B_tau q`.

## 6. Consequence for the Fisher--Hankel endpoint

For any finite delayed Cauchy packet, the vector to which the resident
Fisher--Hankel inequality must be applied is

\[
 h=\sum_jc_jr_{a,x_j,\tau_j}
 =\sum_jc_j
  (T_{\tau_j}g_{a,x_j}+B_{\tau_j}q_{a,x_j}).
 \tag{L-91323.23}
\]

If this vector belongs to `Dom(A_a)`, `L-91322.17` gives the exact tangent plus
score-orthogonal reserve. The other two channels in (L-91323.12) are already
positive and retain every cross term.

The remaining analytic joint is therefore narrower:

```text
prove that the explicit forced resident vectors r_(a,x,tau)
lie in the Fisher-Hankel form domain and satisfy the completed
Jordan+gamma+pole source domination.
```

The physical base map and arbitrary-delay bookkeeping are no longer open.

## 7. Exact boundary

```text
full H2+ = model plus completed-amplitude coordinates       EXACT
raw delay three-channel isometry                            EXACT
amplitude-to-model forcing commutator                       EXACT
all physical cross-delay L2 Gram entries                    EXACT
upper-triangular state semigroup and leakage cocycle        EXACT
Cauchy physical input coordinates via model kernels         EXACT
forced delayed resident vector r_(a,x,tau)                  EXACT
Fisher-Hankel domain membership of forced vectors           OPEN
completed arithmetic domination on those vectors            OPEN / RH-BEARING
mixed orientation and bridge arithmetic block               OPEN
Riemann Hypothesis                                           UNPROVED
```
