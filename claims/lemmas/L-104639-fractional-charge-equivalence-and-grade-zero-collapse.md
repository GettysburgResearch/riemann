# L-104639 — The fractional current is equivalent to the shallow canonical charge, and the seven-grade family collapses at grade zero

Claim ID: `L-104639`
Status: **PROVED EXACT BINDING CORRECTION TO THE INTERPRETATION OF `L-104633`**
Created: 2026-08-30
Depends on: `L-104630--L-104633`, `L-106674`
RH status: **not assumed**

Let

\[
Q=Q_{A,B}=P_{K_B}(I-P_{K_A})P_{K_B}\succeq0,
\qquad
\mathfrak C(A,B)=\operatorname{tr}Q,
\]

and retain the fractional multipliers

\[
W_{a,H}
={H^{a-1}\over\Gamma(a)}
 M_{\xi^a e^{-H\xi}},
\qquad
\widetilde W^{(5)}_{a,H}
={H^{a-1}\over\Gamma(a)}
 M_{\xi^a r_{5,H}(\xi)}.
\]

Put

\[
\delta_0={7H_0^2\over3\kappa_0},
\qquad
m=\deg B,
\qquad
\varepsilon_{a,H_0,\eta}
=
1-\left({H_0\over H_0+2\eta}\right)^a.
\]

Assume that every zero of the denominator factor considered here has height at
most \(\eta\).

## 1. Two-sided fractional-charge comparison

The fifth-current sandwich of `L-104630` is

\[
e^{-H\xi-\frac{7H^2}{3\kappa_0}}
\le r_{5,H}(\xi)\le e^{-H\xi}.
\]

Consequently, for \(0<H\le H_0\),

\[
\boxed{
e^{-\delta_0}W_{a,H}
\preceq
\widetilde W^{(5)}_{a,H}
\preceq
W_{a,H}.
}
\tag{L-104639.1}
\]

Define the shallow fractional residual

\[
\mathfrak I_{H_0}(A,B)
=
\int_0^{H_0}
\operatorname{tr}
\left(Q\widetilde W^{(5)}_{a,H}\right)dH.
\tag{L-104639.2}
\]

The exact Calderón identity gives

\[
\mathfrak C(A,B)
=
\int_0^\infty\operatorname{tr}(QW_{a,H})\,dH.
\]

The tail theorem `L-104631.8` gives

\[
0\le
\int_{H_0}^\infty\operatorname{tr}(QW_{a,H})\,dH
\le m\varepsilon_{a,H_0,\eta}.
\tag{L-104639.3}
\]

Combining (L-104639.1)--(L-104639.3) yields the exact two-sided comparison

\[
\boxed{
e^{-\delta_0}
\left(
\mathfrak C(A,B)-m\varepsilon_{a,H_0,\eta}
\right)
\le
\mathfrak I_{H_0}(A,B)
\le
\mathfrak C(A,B).
}
\tag{L-104639.4}
\]

Equivalently,

\[
\boxed{
\mathfrak C(A,B)
\le
e^{\delta_0}\mathfrak I_{H_0}(A,B)
+
m\varepsilon_{a,H_0,\eta}.
}
\tag{L-104639.5}
\]

Thus the fractional-current premise is not a weaker source estimate waiting to
be promoted to the inner factors.  Up to precisely the already declared
gamma tail, it is the shallow canonical-correlation charge itself.

## 2. The topological unit spectrum is already inside the premise

Put

\[
d=(\deg B-\deg A)_+.
\]

By `L-106674`, \(Q\) has at least \(d\) eigenvalues equal to one.  Hence

\[
d\le\mathfrak C(A,B).
\]

Equation (L-104639.5) therefore gives

\[
\boxed{
d
\le
e^{\delta_0}\mathfrak I_{H_0}(A,B)
+
m\varepsilon_{a,H_0,\eta}.
}
\tag{L-104639.6}
\]

For the sharp-input constants of `L-104632`,

\[
e^{\delta_0}<{1001\over1000},
\qquad
{m\over N}\le2+o(1),
\qquad
\varepsilon<{17\over50000}.
\]

Therefore the premise
\(\mathfrak I_{H_0}/N<21/1000\) already forces

\[
\boxed{
{d\over N}
<
{1001\over1000}{21\over1000}
+
{17\over25000}
=
{21701\over10^6}.
}
\tag{L-104639.7}
\]

For the self-contained constants of `L-104635`, the premise
\(\mathfrak I_{H_0}/N<13/500\) already forces

\[
\boxed{
{d\over N}
<
{1001\over1000}{13\over500}
+
{13\over4000}
=
{7319\over250000}.
}
\tag{L-104639.8}
\]

These are exactly the respective shallow-charge allowances.  The fractional
premise therefore contains the new microscopic zero-count theorem; it does not
derive it from a source-only inequality.

## 3. The seven-grade family contains the exact minimizer at grade zero

Retain the notation of `L-104633`:

\[
X_H=P_{K_B}M_H,
\qquad
Z_{r,H}=P_{K_A}D^rX_H,
\qquad 0\le r\le6.
\]

At \(r=0\),

\[
\boxed{Z_{0,H}=P_{K_A}X_H.}
\tag{L-104639.9}
\]

For

\[
Y_H(c)=\sum_{r=0}^6c_rZ_{r,H},
\]

orthogonal projection gives

\[
\boxed{
\|X_H-Y_H(c)\|_{\mathcal S_2}^2
=
\|(I-P_{K_A})X_H\|_{\mathcal S_2}^2
+
\|P_{K_A}X_H-Y_H(c)\|_{\mathcal S_2}^2.
}
\tag{L-104639.10}
\]

Taking \(c=e_0=(1,0,\ldots,0)^T\) makes the second term zero.  Therefore

\[
\boxed{
\inf_{c\in\mathbb C^7}
\|X_H-Y_H(c)\|_{\mathcal S_2}^2
=
\|(I-P_{K_A})X_H\|_{\mathcal S_2}^2
=
\operatorname{tr}
\left(Q\widetilde W^{(5)}_{a,H}\right).
}
\tag{L-104639.11}
\]

The full projected inner-factor geometry has already entered through
\(P_{K_A}\) in the zeroth candidate.  The grades \(1,\ldots,6\) do not create a
source-to-inner-factor theorem.

## 4. Exact ridge correction

Let \(G_H,b_H\) be the Gram and cross vector of `L-104633.3`.  Equation
(L-104639.9) gives

\[
\boxed{b_H=G_He_0.}
\tag{L-104639.12}
\]

For \(\tau>0\), the ridge vector is

\[
c_{H,\tau}=(G_H+\tau I)^{-1}b_H.
\]

Substitution into the orthogonal decomposition yields

\[
\boxed{
\mathcal R^{(6)}_{H,\tau}
=
\operatorname{tr}
\left(Q\widetilde W^{(5)}_{a,H}\right)
+
\tau^2
e_0^*(G_H+\tau I)^{-1}
G_H
(G_H+\tau I)^{-1}e_0.
}
\tag{L-104639.13}
\]

The second term is nonnegative, and

\[
\boxed{
\inf_{\tau>0}\mathcal R^{(6)}_{H,\tau}
=
\operatorname{tr}
\left(Q\widetilde W^{(5)}_{a,H}\right).
}
\tag{L-104639.14}
\]

Hence `FRACKRYLOV104633` is a regularized restatement of the fractional
canonical charge.  If its regularizers tend to zero sufficiently, it is
asymptotically the same gate; if they do not, it is a strictly stronger gate.
In neither case does the frozen Bézout source identity prove it.

## Binding disposition

```text
fractional metric versus canonical shallow charge       EQUIVALENT UP TO DECLARED TAIL
topological unmatched dimension contained in premise    PROVED EXACT
seven-grade projected Krylov family                      COLLAPSES AT GRADE ZERO
ridge residual                                           EXACT CHARGE + POSITIVE REGULARIZER
source-module Bézout identity                            RETAINED EXACT
source-module identity -> inner-factor charge            NOT PROVIDED
SELFKRYLOV104636                                         UNPROVED
more than ninety percent                                 UNPROVED
Riemann Hypothesis                                       UNPROVED
```
