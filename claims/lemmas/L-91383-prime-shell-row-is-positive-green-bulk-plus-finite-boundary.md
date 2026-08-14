# L-91383 — A prime-shell row is one positive Green bulk plus one finite Kantorovich boundary

Claim ID: `L-91383`  
Status: **PROVED EXACT REDUCTION — UNIFORM DOMINATION OPEN**  
Created: 2026-08-14  
Depends on: `L-91344`  
RH status: **unproved**

## 1. Shell row

For the finite Euler row

\[
 D_{P,X}(j)=\sum_{d\mid P}\frac{\mu(d)}{\sqrt d}Q_{X/d}(j),
\]

define

\[
 \mathscr S_{P,p;X}(j)=D_{P,X}(j)-D_{P,X/p}(j).
\tag{L-91383.1}
\]

Let

\[
 \Delta_p^0F(X)=F(X)-F(X/p).
\]

Using the exact Green decomposition of `L-91344`,

\[
\boxed{
\begin{aligned}
 \mathscr S_{P,p;X}(j)={}&
 c_j\Delta_p^0\mathcal R_P(X)\\
 &-c_j\sum_{m=1}^{j-1}m^{-1/2}
       \Delta_p^0\mathcal G_P(X/m)\\
 &+\frac{j+2}{j\sqrt j}\Delta_p^0\mathcal G_P(X/j)\\
 &-\frac1{\sqrt{j+1}}
       \Delta_p^0\mathcal G_P(X/(j+1)),
\end{aligned}}
\tag{L-91383.2}
\]

where `c_j=2/[j(j-1)]`.

## 2. Positive bulk

For every `k` coprime to `P`,

\[
 \ell_X(k)-\ell_{X/p}(k)\ge0.
\]

Hence

\[
\boxed{
 \Delta_p^0\mathcal R_P(X)\ge0.
}
\tag{L-91383.3}
\]

The possible negative contribution is confined to the `j+1` scalar boundary
evaluations in (L-91383.2).

## 3. Centered boundary function

Put

\[
 \beta_P=\prod_{q\mid P}(1-q^{-1/2})
\]

and

\[
 E_{P,p}(z)=
 \Delta_p^0\mathcal G_P(z)-\beta_P\log p.
\tag{L-91383.4}
\]

Let the signed boundary measure on logarithmic scale be

\[
 \nu_j=
 -c_j\sum_{m=1}^{j-1}m^{-1/2}\delta_{-\log m}
 +\frac{j+2}{j\sqrt j}\delta_{-\log j}
 -\frac1{\sqrt{j+1}}\delta_{-\log(j+1)}.
\tag{L-91383.5}
\]

Write

\[
 s_j=\nu_j(\mathbb R)
\]

and let `W_j` be the minimum one-dimensional Kantorovich–Rubinstein norm of
`nu_j-s_j delta_a` over support anchors `a`.

The bounded-Lipschitz inequality yields

\[
\boxed{
 \int E_{P,p}(Xe^t)\,d\nu_j(t)
 \ge
 -|s_j|\|E_{P,p}\|_\infty
 -\mathcal W_j\operatorname{Lip}_{\log}E_{P,p}.
}
\tag{L-91383.6}
\]

Therefore

\[
\boxed{
\begin{aligned}
 \mathscr S_{P,p;X}(j)
 \ge{}&c_j\Delta_p^0\mathcal R_P(X)
 +\beta_P(\log p)s_j\\
 &-|s_j|\|E_{P,p}\|_\infty
 -\mathcal W_j\operatorname{Lip}_{\log}E_{P,p}.
\end{aligned}}
\tag{L-91383.7}
\]

## 4. Use

Equation (L-91383.7) is a fail-closed analytic campaign:

```text
positive rough-number Green bulk
versus
one finite bounded-Lipschitz boundary packet.
```

A uniform positive lower bound proves canonical shell-row positivity in the
chosen parameter region.  A negative directed cell refutes it there.

## 5. Boundary

The reduction is exact.  Uniform bounds strong enough for all primorial stages
are not proved here.

```text
shell Green decomposition            EXACT
positive shell Green bulk            EXACT
finite boundary support              EXACT
Kantorovich lower bound               EXACT
uniform positive domination          OPEN
Riemann Hypothesis                    UNPROVEN
```
