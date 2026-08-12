# L-91630 — The paired-eta tail has an exact full-carrier weighted Julia dilation

Claim ID: `L-91630`  
Status: **PROVED EXACT POSITIVE SECTOR-CHANGING DILATION**  
Created: 2026-08-12  
Depends on: `L-91430/L-91431`; `L-91530`  
Corrects the scope of: the same-space unboundedness discussion in `L-91530`  
RH status: **unproved**

## 1. Physical paired-eta set

Let

\[
 \mathcal E
 =\bigcup_{m\ge1}
  [\log(2m-1),\log(2m)].
\]

For `Re z>0`,

\[
 \boxed{
 I_\eta(z)
 :=\int_{\mathcal E}e^{-zy}dy
 =\frac{\eta_D(z)}{z}.
 }
\]

Indeed, integration over the `m`-th interval gives

\[
 \frac{(2m-1)^{-z}-(2m)^{-z}}{z},
\]

and the paired eta series converges absolutely in this half-plane.

## 2. Weighted carrier spaces

Fix

\[
 \sigma>\omega>0.
\]

Put

\[
 \mathcal H_-:=L^2(\mathcal E,e^{-(\sigma-\omega)y}dy),
 \qquad
 \mathcal H_+:=L^2(\mathcal E,e^{-(\sigma+\omega)y}dy).
\]

For a carrier `t in R`, let

\[
 e_t(y)=e^{-ity}.
\]

Then

\[
 \boxed{
 \langle e_t,e_u\rangle_{\mathcal H_-}
 =I_\eta(\sigma-\omega+i(t-u)),
 }
\]

and

\[
 \boxed{
 \langle e_t,e_u\rangle_{\mathcal H_+}
 =I_\eta(\sigma+\omega+i(t-u)).
 }
\]

Thus both full carrier kernels have positive Hilbert realizations.

## 3. Exact weighted Julia column

On `H_-`, define the multiplication functions

\[
 \boxed{
 m_\omega(y)=e^{-\omega y},
 \qquad
 d_\omega(y)=\sqrt{1-e^{-2\omega y}}.
 }
\]

Pointwise,

\[
 |m_\omega(y)|^2+|d_\omega(y)|^2=1.
\]

Therefore the column

\[
 \boxed{
 \mathcal J_\omega f
 =\begin{pmatrix}m_\omega f\\d_\omega f\end{pmatrix}
 }
\]

is an isometry

\[
 \mathcal H_-
 \longrightarrow
 \mathcal H_-\oplus\mathcal H_-.
\]

For all carriers `t,u`,

\[
 \boxed{
 \langle m_\omega e_t,m_\omega e_u\rangle_{\mathcal H_-}
 =I_\eta(\sigma+\omega+i(t-u)),
 }
\]

and

\[
 \boxed{
 \begin{aligned}
 \langle d_\omega e_t,d_\omega e_u\rangle_{\mathcal H_-}
 ={}&I_\eta(\sigma-\omega+i(t-u))\\
 &-I_\eta(\sigma+\omega+i(t-u)).
 \end{aligned}
 }
\]

Hence

\[
 \boxed{
 K_{\sigma-\omega}^{\eta}
 =K_{\sigma+\omega}^{\eta}
  +K_{\sigma,\omega}^{\eta,\rm detail},
 \qquad
 K_{\sigma,\omega}^{\eta,\rm detail}\succeq0.
 }
\]

This is a full polarized carrier identity, not a one-vector Householder
statement.

## 4. Sector-changing unitary

Multiplication by `m_omega` is also the unitary

\[
 \boxed{
 \mathcal U_{\sigma,\omega}:
 \mathcal H_+\longrightarrow\mathcal H_-,
 \qquad
 (\mathcal U_{\sigma,\omega}f)(y)=e^{-\omega y}f(y).
 }
\]

Indeed,

\[
 \|\mathcal U_{\sigma,\omega}f\|_{\mathcal H_-}^2
 =\int_{\mathcal E}|f(y)|^2e^{-(\sigma+\omega)y}dy
 =\|f\|_{\mathcal H_+}^2.
\]

The unitary commutes with every carrier modulation `e^{-ity}` and with every
multiplicative physical-delay phase.

The inverse multiplier `e^{\omega y}` is unbounded on either **fixed common
space**, as observed on `L-91530`.  That fact does not obstruct the correct
sector-changing unitary between the two weighted spaces.

## 5. Source interpretation

The hard paired-eta source is exactly

```text
safe returned paired-eta state
+ positive eta innovation detail.
```

No unbounded same-space inverse is needed.  The previous representation
firewall is therefore narrowed: the paired-eta tail itself has a complete
positive full-carrier source dilation.

What remains is to combine this dilation with the compact dyadic/gamma bridge,
the residual gamma source, and the critical/stable model map.

## 6. Exact boundary

```text
paired eta physical set                         EXACT
hard and safe full-carrier kernels              EXACT POSITIVE
weighted Julia column                           EXACT
eta detail kernel                               EXACT POSITIVE
full-carrier sector-changing unitary             EXACT
same-space inverse                              UNBOUNDED BUT IRRELEVANT
completed source-to-model exhaustion             OPEN / RH-BEARING
Riemann Hypothesis                              UNPROVED
```
