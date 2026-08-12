# L-91510 — The safe prime Julia cascade is the Herglotz dissipation of the parity Cayley impedance

Claim ID: `L-91510`  
Status: **PROVED EXACT PRIME-SECTOR POSITIVE-REAL REALIZATION; COMPLETED DOMAIN WALL OPEN**  
Created: 2026-08-12  
Depends on: `L-91323/L-91324` on PR #403; `L-91414/L-91415` on PR #412  
RH status: **unproved**

## 1. One safe local Euler node

Retain the universal safe local Julia node of `L-91323`:

\[
 m(z)=c\frac{1-\alpha z}{1-\beta z},
 \qquad
 d(z)=\delta\frac{1-z}{1-\beta z},
 \qquad 0<\alpha<\beta<1,
 \tag{L-91510.1}
\]

where

\[
 c=\frac{1-\beta}{1-\alpha},
 \qquad
 \delta^2=\frac{(\beta-\alpha)(1-\alpha\beta)}{(1-\alpha)^2}.
 \tag{L-91510.2}
\]

On the unit circle,

\[
 \boxed{|m|^2+|d|^2=1.}
 \tag{L-91510.3}
\]

Thus `m` is Schur and the column `(m,d)^T` is inner.

## 2. Parity Cayley impedance

Define

\[
 \boxed{
 h(z)=\frac{1-m(z)}{1+m(z)}.
 }
 \tag{L-91510.4}
\]

Because `m` is Schur, `h` has nonnegative real part in the disk. On the
boundary,

\[
\boxed{
 2\Re h
 =\frac{2(1-|m|^2)}{|1+m|^2}
 =\frac{2|d|^2}{|1+m|^2}.
}
\tag{L-91510.5}

Let `f,g` lie in the common Hardy multiplier core and put

\[
 E_f=\frac{1+m}{\sqrt2}f,
 \qquad
 O_f=\frac{m-1}{\sqrt2}f.
 \tag{L-91510.6}

Then

\[
 \boxed{O_f=-hE_f.}
 \tag{L-91510.7}

More importantly, the complete polarized dissipation identity is

\[
\boxed{
 \langle hE_f,E_g\rangle
 +\langle E_f,hE_g\rangle
 =\langle df,dg\rangle.
}
\tag{L-91510.8}

Indeed, the boundary multiplier on the left is

\[
 \frac12\left[
 h(1+m)\overline{(1+m)}
 +(1+m)\overline{h(1+m)}
 \right]
 =1-|m|^2=|d|^2.
\]

Thus the local Julia detail is exactly the dissipative part of the
positive-real parity impedance. This is a full cross-input identity, not only
a scalar norm equality.

## 3. Herglotz kernel

The positive-real kernel is

\[
\boxed{
 \mathscr H_h(z,w)
 =\frac{h(z)+\overline{h(w)}}{1-z\overline w}
 \succeq0.
}
\tag{L-91510.9}

Algebraically,

\[
 h(z)+\overline{h(w)}
 =\frac{2[1-m(z)\overline{m(w)}]}
 {(1+m(z))(1+\overline{m(w)})}.
 \tag{L-91510.10}

Hence the de Branges--Rovnyak defect of the returned Euler channel and the
Herglotz connection of the parity graph are the same positive kernel up to
explicit diagonal congruence.

## 4. Finite prime cascade

For an ordered finite family of local nodes `(m_j,d_j)`, define

\[
 M_N=\prod_{j=1}^N m_j,
 \qquad
 D_{j,N}=\left(\prod_{\ell<j}m_\ell\right)d_j.
 \tag{L-91510.11}

Repeated local Julia identities give

\[
\boxed{
 1-|M_N|^2=\sum_{j=1}^N|D_{j,N}|^2.
}
\tag{L-91510.12}

Let

\[
 h_N=\frac{1-M_N}{1+M_N},
 \qquad
 E_{N,f}=\frac{1+M_N}{\sqrt2}f.
 \tag{L-91510.13}

Then

\[
\boxed{
 \langle h_NE_{N,f},E_{N,g}\rangle
 +\langle E_{N,f},h_NE_{N,g}\rangle
 =\sum_{j=1}^N\langle D_{j,N}f,D_{j,N}g\rangle.
}
\tag{L-91510.14}

Thus every finite prime cascade is one passive positive-real impedance whose
dissipation space is exactly the ordered Julia-detail space.

## 5. Redheffer / hyperbolic addition law

If

\[
 h_j=\frac{1-m_j}{1+m_j},
\]

then the impedance of the product satisfies

\[
\boxed{
 h_{m_1m_2}
 =\frac{h_1+h_2}{1+h_1h_2}.
}
\tag{L-91510.15}

This is the scalar Redheffer star-product law and the hyperbolic tangent
addition formula. It gives a coefficient-one recursive construction of the
prime connection; no post hoc square root of a target Gram is introduced.

## 6. Infinite safe product

On every safe line `sigma>1`, `L-91324` gives convergence of the ordered prime
Julia cascade in the natural Hardy/Fock norm. Therefore

\[
 M_{a,\sigma}
 =\prod_p m_{p,a,\sigma}
 =\frac{Q_a(\sigma+i\cdot)}{Q_a(\sigma)}
\]

is Schur, and

\[
\boxed{
 h_{a,\sigma}
 =\frac{1-M_{a,\sigma}}{1+M_{a,\sigma}}
}
\tag{L-91510.16}

has a positive Herglotz kernel. The finite dissipations converge to the exact
all-prime Julia/Fock detail space.

## 7. Atomic-isolation interpretation

At a local prime resonance `z=1`,

\[
 d(1)=0,
 \qquad
 m(1)=1,
 \qquad
 h(1)=0.
 \tag{L-91510.17}

Hence a Fejer packet concentrating on one prime atom does not disappear from
the complete source geometry: its norm remains in the coefficient-one
returned channel. This is the precise safe-cascade mechanism missing from an
uncoupled continuous-versus-atomic comparison.

It does not by itself prove CPPD. The returned channel must still be coupled
to the completed gamma/pole domain wall and to the three-scale Cauchy
observation.

## 8. Exact boundary

```text
local Euler Julia node                         EXACT
parity Cayley impedance                        EXACT POSITIVE REAL
Julia detail = Herglotz dissipation             EXACT POLARIZED
finite prime cascade dissipation                EXACT
Redheffer/tanh composition                      EXACT
infinite safe prime Herglotz connection         EXACT
prime atomic-isolation loss                     CLOSED IN RETURNED CHANNEL
completed gamma/pole/domain-wall interconnection OPEN / RH-BEARING
Riemann Hypothesis                              UNPROVED
```
