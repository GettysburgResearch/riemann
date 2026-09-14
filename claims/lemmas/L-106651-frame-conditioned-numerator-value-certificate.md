# L-106651 — Frame-conditioned numerator values give a valid collective transport certificate

Claim ID: `L-106651`  
Status: **PROVED EXACT FINITE INEQUALITIES**  
Created: 2026-08-26  
Depends on: `L-106630`, `L-106650`  
RH status: **not assumed**

Retain finite inner functions \(A,B\), with simple denominator zeros
\(b_1,\ldots,b_m\), normalized kernel Gram \(G\), and

\[
D=\operatorname{diag}(A(b_1),\ldots,A(b_m)).
\]

By `L-106650`,

\[
\mathfrak C(A,B)
=
\operatorname{tr}(G^{-1}D^*GD).
\tag{L-106651.1}
\]

The inverse Gram cannot be discarded.  It can, however, be paid exactly by a
declared frame bound.

## 1. Frame-ratio certificate

Assume

\[
\alpha I\preceq G\preceq\beta I
\qquad
(0<\alpha\le\beta).
\tag{L-106651.2}
\]

Then

\[
D^*GD\preceq\beta D^*D,
\qquad
G^{-1}\preceq\alpha^{-1}I.
\]

Taking positive traces gives

\[
\boxed{
\mathfrak C(A,B)
\le
\frac{\beta}{\alpha}
\sum_{\nu=1}^m|A(b_\nu)|^2.
}
\tag{L-106651.3}
\]

Thus a value-only upper bound is valid after, and only after, the actual
Cauchy frame ratio is retained.

More generally, for any positive diagonal weight \(W\) commuting with \(D\),
the same argument applied to \(W^{1/2}GW^{1/2}\) gives a weighted certificate.
No unrecorded whitening constant is permitted.

## 2. Explicit Gershgorin form

The normalized Cauchy Gram has diagonal entries one and

\[
|G_{\mu\nu}|
=
\frac{2\sqrt{y_\mu y_\nu}}
{\sqrt{(y_\mu+y_\nu)^2+(a_\mu-a_\nu)^2}},
\qquad
b_\nu=a_\nu+iy_\nu.
\tag{L-106651.4}
\]

Put

\[
r(B)
=
\max_\mu
\sum_{\nu\ne\mu}|G_{\mu\nu}|.
\tag{L-106651.5}
\]

If \(r(B)<1\), Hermitian Gershgorin gives

\[
(1-r(B))I\preceq G\preceq(1+r(B))I.
\]

Hence

\[
\boxed{
\mathfrak C(A,B)
\le
\frac{1+r(B)}{1-r(B)}
\sum_{B(b)=0}|A(b)|^2.
}
\tag{L-106651.6}
\]

Every term in (L-106651.4) is explicit in the companion-zero coordinates.

## 3. Product-of-distances form

If the selected numerator subfactor has zeros \(c_k\), then

\[
|A(b_\nu)|^2
=
\prod_k
\frac{|b_\nu-c_k|^2}{|b_\nu-\overline{c_k}|^2}.
\tag{L-106651.7}
\]

Therefore (L-106651.6) is a completely explicit collective certificate:
nearby numerator companions suppress the spectral value, while the declared
denominator frame ratio pays all coherent clustering.

The certificate is invariant under a simultaneous real translation and
positive dilation of all companion zeros.

## 4. Relation to the pairwise firewall

`R-106630` correctly refutes the unwhitened rule which simply adds rank-one
pseudohyperbolic costs.  Equation (L-106651.3) does not revive that rule:

```text
raw pairwise/value sum alone                      insufficient;
value sum times an actual Cauchy frame ratio       valid;
exact value sum plus nonnormality departure        sharp by L-106650.
```

When \(G\) is poorly conditioned, the frame certificate may be useless.  The
sharp replacement is the nonnormality identity of `L-106650`, not the
deletion of \(G^{-1}\).

## 5. Scope

```text
finite frame-conditioned value certificate         PROVED
explicit Gershgorin sufficient condition            PROVED
Xi shallow companion frame/value estimate           OPEN
```
