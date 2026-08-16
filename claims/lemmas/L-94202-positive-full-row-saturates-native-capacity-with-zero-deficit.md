# L-94202 — The positive full Möbius row saturates every native coordinate with zero deficit

Claim ID: `L-94202`  
Status: **PROPOSED COMPLETE EXACT COMPOSITION LEMMA — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-16  
Depends on: `L-94201`; the finite carry identity; \(\mu*1=\varepsilon\) and \(\mu*\log=\Lambda\)  
RH status: **not assumed**

## 1. Native capacities

For \(q\ge2\), put
\[
 w_X(q)=\frac1{\sqrt q}\log\frac Xq\,\mathbf1_{q\le X},
\]
\[
 \Omega_X(q)=w_X(q)-2w_X(4q).
 \tag{L-94202.1}
\]

Let \(C_d(q)\) denote the ordinary average-binomial response of a finite row
\(d\), and
\[
 \Xi_d(q)=C_d(q)-2C_d(4q).
\]

By `L-94201`, \(c_X\) is a nonnegative finite physical row.

## 2. Exact ordinary saturation

The response of \(Q_Y\) is
\[
 C_{Q_Y}(q)
 =\frac1{\sqrt q}
 \sum_{m\le Y/q}\frac1{\sqrt m}\log\frac{Y}{qm}.
\]
Therefore
\[
\begin{aligned}
 C_{c_X}(q)
 &=
 \frac1{\sqrt q}
 \sum_{km\le X/q}
 \frac{\mu(k)}{\sqrt{km}}
 \log\frac{X}{qkm}\\
 &=
 \frac1{\sqrt q}
 \sum_{n\le X/q}
 \frac1{\sqrt n}\log\frac{X}{qn}
 \sum_{k\mid n}\mu(k).
\end{aligned}
\]
Only \(n=1\) survives:
\[
 \boxed{C_{c_X}(q)=w_X(q).}
 \tag{L-94202.2}
\]

Consequently
\[
 \boxed{\Xi_{c_X}(q)=\Omega_X(q)}
 \qquad(q\ge2).
 \tag{L-94202.3}
\]

Thus the positive row saturates, rather than merely lies below, every ordinary
and radix-four native capacity.

## 3. Exact literal score

Let
\[
 J_\Lambda(X)
 =\sum_{n\le X}\frac{\Lambda(n)}{\sqrt n}\log\frac Xn.
 \tag{L-94202.4}
\]
The literal score of one canonical packet is
\[
 \mathcal E(Y)
 =\sum_{m\le Y}\frac{\log m}{\sqrt m}\log\frac Ym.
\]
Hence
\[
\begin{aligned}
 \mathcal H(c_X)
 &=
 \sum_{km\le X}
 \frac{\mu(k)\log m}{\sqrt{km}}\log\frac{X}{km}\\
 &=
 \sum_{n\le X}\frac1{\sqrt n}\log\frac Xn
 \sum_{k\mid n}\mu(k)\log\frac nk\\
 &=J_\Lambda(X),
\end{aligned}
\]
because the inner convolution is \(\Lambda(n)\). Therefore
\[
 \boxed{\mathcal H(c_X)=J_\Lambda(X).}
 \tag{L-94202.5}
\]

## 4. Positive radix-four dual

Define
\[
 Y_4(q)=\sum_{a=0}^{v_4(q)}2^a\Lambda(q/4^a)\ge0.
 \tag{L-94202.6}
\]
The exact recurrence
\[
 Y_4(q)-2\mathbf1_{4\mid q}Y_4(q/4)=\Lambda(q)
\]
gives finite radix-four summation by parts:
\[
 \mathcal H(d)=\sum_qY_4(q)\Xi_d(q),
 \qquad
 J_\Lambda(X)=\sum_qY_4(q)\Omega_X(q).
 \tag{L-94202.7}
\]

For \(d=c_X\), (L-94202.3) yields
\[
 \boxed{
 J_\Lambda(X)-\mathcal H(c_X)
 =\sum_qY_4(q)[\Omega_X(q)-\Xi_{c_X}(q)]
 =0.
 }
 \tag{L-94202.8}
\]

The exact full row is therefore a zero-deficit native certificate at every
endpoint.

## 5. Type and ownership firewalls

No signed child is exported as a positive packet. The object placed in the
physical cone is the completely cancelled row \(c_X\), whose nonnegativity is
the content of `L-94201`.

No finite-Euler row is substituted for the full row. Equation (L-94201.2) uses
a finite prime product only because all omitted divisors are outside triangular
support.

No ordinary-only argument is used. The same row and same coefficients form
\(C(q)\), \(C(4q)\), and hence \(\Xi(q)\).

## 6. Boundary

```text
c_X nonnegative physical row                    L-94201
ordinary response                               w_X exactly
radix-four response                             Omega_X exactly
literal score                                   J_Lambda exactly
positive Y4-weighted deficit                    zero exactly
factor-67 recursive debt                        absent
finite/continuum comparison                     absent
auxiliary port                                  absent
Riemann Hypothesis                              not yet invoked
```
