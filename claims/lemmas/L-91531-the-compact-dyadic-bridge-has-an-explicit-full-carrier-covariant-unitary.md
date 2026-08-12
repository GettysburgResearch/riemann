# L-91531 — The compact dyadic bridge has an explicit full-carrier covariant unitary

Claim ID: `L-91531`  
Status: **PROVED EXACT FINITE-INTERVAL SECTOR CHANGE FOR ALL CARRIERS**  
Created: 2026-08-12  
Depends on: `L-91530`  
RH status: **unproved**

## 1. Finite-interval exponential tilts

For every real `q`, define the probability measure

\[
\boxed{
 d\mu_q(t)
 =\frac{e^{-qt}}{F_L(q)}
  \mathbf1_{0<t<L}\,dt,
 \qquad L=\log2.
}
\tag{L-91531.1}

\]

The interval is compact, so this is finite for every real `q`, including the
old pole nodes.

Its carrier kernel is

\[
\boxed{
 \left\langle e^{-ixt},e^{-iyt}\right\rangle_{L^2(\mu_q)}
 =\frac{F_L(q+i(x-y))}{F_L(q)}.
}
\tag{L-91531.2}

\]

## 2. Explicit tilt unitary

Fix `0<omega<1/2`. Define

\[
\boxed{
 (\mathcal U_{\omega,q}f)(t)
 =\sqrt{\frac{F_L(q)}{F_L(q+2\omega)}}
  e^{-\omega t}f(t).
}
\tag{L-91531.3}

\]

Then

\[
\boxed{
 \mathcal U_{\omega,q}:
 L^2(\mu_{q+2\omega})
 \longrightarrow
 L^2(\mu_q)
}
\tag{L-91531.4}

\]

is unitary. Indeed,

\[
\begin{aligned}
 \|\mathcal U_{\omega,q}f\|_{L^2(\mu_q)}^2
 &={F_L(q)\over F_L(q+2\omega)}
   {1\over F_L(q)}
   \int_0^L|f(t)|^2e^{-(q+2\omega)t}dt\\
 &=\|f\|_{L^2(\mu_{q+2\omega})}^2.
\end{aligned}
\]

## 3. Full carrier covariance

Let

\[
 (M_xf)(t)=e^{-ixt}f(t).
\]

Since `U_(omega,q)` is multiplication by a real positive function,

\[
\boxed{
 \mathcal U_{\omega,q}M_x
 =M_x\mathcal U_{\omega,q}
 \qquad(x\in\mathbb R).
}
\tag{L-91531.5}

\]

Therefore the unitary intertwines the **complete carrier family**, not only one
real vector. For every finite carrier packet,

\[
\boxed{
 \left\langle M_xf,M_yg\right\rangle_{\mu_{q+2\omega}}
 =\left\langle
  \mathcal U_{\omega,q}M_xf,
  \mathcal U_{\omega,q}M_yg
 \right\rangle_{\mu_q}.
}
\tag{L-91531.6}

\]

All cross-carrier terms are preserved exactly.

## 4. Scalar bridge ratio

The compact ratio in `L-91530` is an exponential-tilt expectation:

\[
\boxed{
 \frac{F_L(q+2\omega)}{F_L(q)}
 =\int_0^L e^{-2\omega t}\,d\mu_q(t)
 \in(2^{-2\omega},1).
}
\tag{L-91531.7}

\]

Thus the pole-canceling factor is a positive finite-interval contraction. Its
source and target tilts are linked by the explicit carrier-covariant unitary
above.

## 5. Relation to the previous Householder result

`L-91431` constructed a rank-one Householder mapping one normalized paired eta
state to another. That map could not intertwine the full carrier family.

The compact bridge behaves differently: its Radon--Nikodym ratio is bounded on
`[0,L]`, and (L-91531.3) gives a canonical multiplication unitary for every
carrier at once. The dyadic/gamma pole component of `EPDOB_omega` is therefore
closed at full polarization.

## 6. Delays and Fock lift

Physical delay acts as multiplication by an additional phase on the same
finite interval and hence commutes with `U_(omega,q)` in the same way. Reflection
supplies the opposite Hardy orientation.

Second quantization gives

\[
 \Gamma_s(\mathcal U_{\omega,q})
\]

on the finite-interval bosonic source. It preserves coherent-state Grams
exactly.

## 7. Exact boundary

```text
finite-interval tilt measures                    POSITIVE
compact bridge carrier kernel                    EXACT
safe-to-hard compact tilt unitary                 EXACT
all carrier cross terms                          EXACT
all delays and reflection                        EXACT
bosonic lift                                     EXACT
unbounded paired eta tail                        OPEN
completed eta/beta source-to-model map            OPEN / RH-BEARING
Riemann Hypothesis                               UNPROVED
```
