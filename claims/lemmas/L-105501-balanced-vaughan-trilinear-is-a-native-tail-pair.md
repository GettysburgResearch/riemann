# L-105501 — The balanced Vaughan trilinear is exactly one native tail pair

Claim ID: `L-105501`

Status: **PROVED EXACT SOURCE COMPRESSION AND SUBPOWER DIAGONALS**

Created: 2026-08-27

Depends on: native Vaughan identity `L-100311`; `L-105500`

RH status: **not assumed**

Let

\[
\mu_U(n)=\mu(n)\mathbf1_{n\le U},
\qquad
\nu_U=\mu-\mu_U=\mu(n)\mathbf1_{n>U},
\]

and

\[
a_U=\varepsilon-\mu_U*\mathbf1.
\]

The historical balanced source was written

\[
b_U=a_U*a_U*\mu.
\]

It is exactly a two-factor tail source.

## 1. Three elementary convolution identities

Using \(\mathbf1*\mu=\varepsilon\),

\[
\begin{aligned}
a_U
&=\varepsilon-\mu_U*\mathbf1\\
&=\mathbf1*(\mu-\mu_U)
=\mathbf1*\nu_U.
\end{aligned}
\]

Therefore

\[
\boxed{a_U=\mathbf1*\nu_U.}
\tag{L-105501.1}
\]

Convolving with \(\mu\),

\[
\boxed{a_U*\mu=\nu_U.}
\tag{L-105501.2}
\]

Consequently,

\[
\boxed{
b_U=a_U*a_U*\mu
=a_U*\nu_U
=\mathbf1*\nu_U*\nu_U.
}
\tag{L-105501.3}
\]

No estimate or truncation error enters these identities.

## 2. Both factors are genuinely long

For \(n\le U\),

\[
a_U(n)=0,
\qquad
\nu_U(n)=0.
\tag{L-105501.4}
\]

Hence every nonzero pair in \(a_U*\nu_U\) has both factors greater than \(U\).
The former three-variable packet has become one balanced two-field product.

For \(n>1\),

\[
a_U(n)
=
-\sum_{\substack{d\mid n\\d\le U}}\mu(d)
=
\sum_{\substack{d\mid n\\d>U}}\mu(d).
\tag{L-105501.5}
\]

## 3. Prime-color covariance

For any prime coloring of `L-105500`, put

\[
f_{U,\chi}^\pm=a_U*\mu_\chi^\pm.
\]

Then

\[
\boxed{b_U=f_{U,\chi}^+*f_{U,\chi}^-.}
\tag{L-105501.6}
\]

The extreme all-\(+\) gauge reduces (L-105501.6) to the canonical tail pair

\[
f_{U,+}=a_U*\mu=\nu_U,
\qquad
f_{U,-}=a_U.
\]

Thus prime color is a genuine source gauge: it redistributes the literal
Möbius factor between the two long fields without changing their product.

## 4. Source energy and equal products

The elementary bounds

\[
|a_U(n)|\le\tau(n),
\qquad
|\nu_U(n)|\le1
\]

give

\[
\sum_{n\le Z}\frac{|a_U(n)|^2}{n}
\ll(\log(2Z))^4,
\qquad
\sum_{n\le Z}\frac{|\nu_U(n)|^2}{n}
\ll\log(2Z).
\tag{L-105501.7}
\]

More generally,

\[
|f_{U,\chi}^\pm(n)|
\le d_3(n),
\qquad
\sum_{n\le Z}\frac{|f_{U,\chi}^\pm(n)|^2}{n}
\ll(\log(2Z))^9.
\tag{L-105501.8}

For one physical product, the number of factor pairs in
\(f_{U,\chi}^+*f_{U,\chi}^-\) is at most \(\tau(n)=n^{o(1)}\).
Hence the free diagonal and equal-product collapse are subpower.

No distinct-product estimate is asserted.
