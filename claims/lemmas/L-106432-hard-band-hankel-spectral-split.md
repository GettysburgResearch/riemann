# L-106432 — Exact hard-band Hankel spectral split

Claim ID: `L-106432`  
Status: **PROVED EXACT AT HILBERT--SCHMIDT \(H^{1/2}\) SCOPE**  
Created: 2026-08-25  
Depends on: `L-105290`, `L-106431`  
RH status: **not assumed**

Use the Fourier convention

\[
\widehat f(\xi)=\frac1{2\pi}\int_{\mathbb R}f(t)e^{-it\xi}\,dt,
\qquad
f(t)=\int_{\mathbb R}\widehat f(\xi)e^{it\xi}\,d\xi.
\]

Let \(U\) be scalar or matrix valued, unimodular/unitary on the real line, and
assume its positive and negative half-derivative energies are finite. Under
the Paley--Wiener identification \(H^2(\mathbb C_+)\simeq L^2(0,\infty)\),
let \(P_H\) be multiplication by \(\mathbf 1_{[0,H]}\).

## 1. Restricted negative Hankel energy

For output frequency \(-x\), \(x>0\), and input frequency \(s>0\), the Hankel
kernel is

\[
K_U(x,s)=\widehat U(-(x+s)).
\]

Therefore Fubini and the substitution \(r=x+s\) give

\[
\boxed{
\|H_UP_H\|_{\mathcal S_2}^2
=
\int_0^\infty
\min(H,r)\,\|\widehat U(-r)\|_{\mathrm F}^2\,dr.
}
\tag{L-106432.1}
\]

The complementary input band satisfies

\[
\boxed{
\|H_UP_H^\perp\|_{\mathcal S_2}^2
=
\int_H^\infty
(r-H)\,\|\widehat U(-r)\|_{\mathrm F}^2\,dr.
}
\tag{L-106432.2}
\]

By reflection,

\[
\boxed{
\|H_{\overline U}P_H\|_{\mathcal S_2}^2
=
\int_0^\infty
\min(H,r)\,\|\widehat U(r)\|_{\mathrm F}^2\,dr,
}
\tag{L-106432.3}
\]

and

\[
\boxed{
\|H_{\overline U}P_H^\perp\|_{\mathcal S_2}^2
=
\int_H^\infty
(r-H)\,\|\widehat U(r)\|_{\mathrm F}^2\,dr.
}
\tag{L-106432.4}
\]

No sampling or inverse-frame hypothesis enters these identities.

## 2. Exact signed split

Define

\[
\mathcal V_H(U)
=
\int_0^\infty
\min(H,r)
\left(
\|\widehat U(-r)\|_{\mathrm F}^2
-
\|\widehat U(r)\|_{\mathrm F}^2
\right)dr
\tag{L-106432.5}
\]

and

\[
\mathcal D_H(U)
=
\int_H^\infty
(r-H)
\left(
\|\widehat U(-r)\|_{\mathrm F}^2
-
\|\widehat U(r)\|_{\mathrm F}^2
\right)dr.
\tag{L-106432.6}
\]

Then `L-105290/L-106431` become the literal spectral identity

\[
\boxed{
-\operatorname{wind}\det U
=
\mathcal V_H(U)+\mathcal D_H(U).
}
\tag{L-106432.7}
\]

In particular,

\[
\boxed{
-\operatorname{wind}\det U
\le
\|H_UP_H\|_{\mathcal S_2}^2
+
\bigl(\mathcal D_H(U)\bigr)_+.
}
\tag{L-106432.8}
\]

This is the correct hard-band version of the signed endpoint gate.

## 3. Circle version

If

\[
U(e^{it})=\sum_{n\in\mathbb Z}U_ne^{int}
\]

and \(P_d\) projects onto \(1,z,\ldots,z^{d-1}\), then

\[
\boxed{
\|H_UP_d\|_{\mathcal S_2}^2
=
\sum_{n<0}\min(d,|n|)\|U_n\|_{\mathrm F}^2,
}
\tag{L-106432.9}
\]

\[
\boxed{
\|H_UP_d^\perp\|_{\mathcal S_2}^2
=
\sum_{n<0}(|n|-d)_+\|U_n\|_{\mathrm F}^2.
}
\tag{L-106432.10}
\]

The positive-frequency formulas are obtained by replacing \(n<0\) with
\(n>0\). This finite identity supplies exact replay fixtures without
discretizing the continuous theorem.

## 4. Scope

The lemma identifies the actual quantities which must be estimated. It does
not identify the four-channel coefficient source of `L-106413` with the
hard-band projection \(P_H\), and it does not bound either integral for Xi.
