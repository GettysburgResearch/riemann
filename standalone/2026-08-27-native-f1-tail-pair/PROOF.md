# Native prime-color compactification and tail-pair F1 Hodge frontier

## Scientific status

This packet proves an exact source repair and an RH-equivalent native F1
reduction.  It does **not** prove the terminal estimate or the Riemann
Hypothesis.

Frozen inputs:

```text
PR #730  b3114562acbeb8c5890ef7a5fc59eed8db71d29a
PR #719  59654c02d13545d6c8c0972315db2628e9efa1f6
PR #751  98af0db6ec7f77d6333a77a3dac53c4698852f43
PR #685  4f69b7656f42dcb5ff250d13adc9f88e8d18f315
PR #705  027ea8bd5c879a190e9e22620c245a81f7b93b73
PR #715  99cc94c48bafd9b96141f7cef9f1e7aa83012747
```

The imported facts are:

- the corrected QPTI semiprime refutation on PR #719;
- the exact ordinary Vaughan identity;
- the positive ratio-four half-kernel multiplier;
- the fixed negative-mass Mellin–Landau consumer;
- the corrected same-`K1` largest-prime/Vaughan translation.

Everything else below is proved directly.

---

## 1. Source firewall: harmonic completion is not the balanced source

The completed harmonic QPTI field has atoms

\[
pq\,c^2
\]

with coefficient

\[
\frac{\mu(c)}
{\binom{\omega(c)+2}{2}\sqrt{pq}\,c}.
\]

Corrected PR #719 proves that its live core contributes

\[
-C_0\sqrt X\frac{\log\log X}{\log X}(1+o(1)),
\qquad C_0>0.
\]

Thus the harmonic completed producer is false.

The balanced F1 source uses instead

\[
b_U=a_U*a_U*\mu,
\qquad
a_U=\varepsilon-\mu_U*\mathbf1.
\]

Put

\[
\nu_U=\mu-\mu_U=\mu\mathbf1_{n>U}.
\]

Since \(\mathbf1*\mu=\varepsilon\),

\[
\begin{aligned}
a_U
&=\varepsilon-\mu_U*\mathbf1\\
&=\mathbf1*(\mu-\mu_U)\\
&=\mathbf1*\nu_U.
\end{aligned}
\tag{1.1}
\]

Convolving with \(\mu\),

\[
a_U*\mu=\nu_U.
\tag{1.2}
\]

Therefore

\[
\boxed{
b_U=a_U*a_U*\mu=a_U*\nu_U=\mathbf1*\nu_U*\nu_U.}
\tag{1.3}
\]

Both \(a_U\) and \(\nu_U\) vanish on \(n\le U\).  Hence

\[
\boxed{b_U(n)=0\qquad(n\le U^2).}
\tag{1.4}
\]

The fixed-core coefficient which creates the QPTI semiprime main is absent
from every cofinal balanced block.  Matching only the atom shape \(pq c^2\)
does not identify the sources.

This proves the source firewall.

---

## 2. Rigidity of an ordinary squarefree two-factor section

At one prime, seek squarefree local factors

\[
(1-\alpha x)(1-\beta x)
\]

whose ordinary product is \(1-x\) and has no \(x^2\) term.  Coefficient
comparison gives

\[
\alpha+\beta=1,
\qquad
\alpha\beta=0.
\]

Therefore

\[
\boxed{\{\alpha,\beta\}=\{0,1\}.}
\tag{2.1}
\]

The midpoint factorization is available in the prime-box Chow algebra because
\(h_p^2=0\):

\[
(1-\tfrac12h_p)^2=1-h_p.
\]

It is not an ordinary physical factorization; ordinary multiplication would
retain \(x_p^2/4\).

Now color every prime either `+` or `-`.  Define \(\mu_\chi^\pm\) to be the
Möbius function restricted to squarefree integers all of whose prime factors
have the indicated color.  Every squarefree integer has a unique decomposition

\[
n=n_+n_-
\]

according to its prime colors.  Hence

\[
\boxed{\mu=\mu_\chi^+*\mu_\chi^-.}
\tag{2.2}
\]

For \(\Re z>1\), this is the Euler factorization

\[
\left(\prod_{\chi(p)=+}(1-p^{-z})\right)
\left(\prod_{\chi(p)=-}(1-p^{-z})\right)
=\frac1{\zeta(z)}.
\tag{2.3}
\]

Thus the native physical two-copy section is the prime-color vertex cube.

---

## 3. Prime-color covariance of the balanced tail pair

For any coloring put

\[
f_{U,\chi}^\pm=a_U*\mu_\chi^\pm.
\]

By (2.2),

\[
\boxed{
b_U=f_{U,\chi}^+*f_{U,\chi}^-.}
\tag{3.1}
\]

In the extreme coloring with every prime in the `+` factor,

\[
f_{U,+}=a_U*\mu=\nu_U,
\qquad
f_{U,-}=a_U.
\tag{3.2}
\]

This is the canonical tail pair.

The elementary bounds

\[
|a_U(n)|\le\tau(n),
\qquad
|\nu_U(n)|\le1
\]

give

\[
\sum_{n\le Z}\frac{|a_U(n)|^2}{n}\ll(\log Z)^4,
\qquad
\sum_{n\le Z}\frac{|\nu_U(n)|^2}{n}\ll\log Z.
\tag{3.3}
\]

For general color,

\[
|f_{U,\chi}^\pm(n)|
\le\sum_{d\mid n}\tau(d)
=d_3(n),
\]

so

\[
\sum_{n\le Z}\frac{|f_{U,\chi}^\pm(n)|^2}{n}
\ll(\log Z)^9.
\tag{3.4}
\]

One product has at most \(\tau(n)=n^{o(1)}\) factor-pair representations.
Cauchy at a fixed product and (3.3)--(3.4) prove subpower free diagonal and
equal-product collapse.  Distinct products remain open.

---

## 4. Positive half-kernel factorization of the native detector

Let

\[
\widehat A(s)
=
\frac{(1-2^{-s})(1-\sqrt2\,2^{-s})}
{s(s-\frac12)}.
\tag{4.1}
\]

The corrected same-\(K_1\) multiplier is

\[
\widehat K_1(s)
=
\frac{(1-2^{-s})^2(1-\sqrt2\,2^{-s})^2(s+\frac32)}
{s^2(s-\frac12)}.
\tag{4.2}
\]

Therefore

\[
\boxed{
K_1=(D+\tfrac32)(D-\tfrac12)(A*_MA).
}
\tag{4.3}
\]

For a color gauge define

\[
F_{U,\chi}^\pm(X)
=
\sum_n\frac{f_{U,\chi}^\pm(n)}{\sqrt n}A(X/n).
\tag{4.4}
\]

Finite Mellin Fubini and (3.1) give the literal balanced current

\[
\boxed{
\mathcal B_U^{K_1}
=(D+\tfrac32)(D-\tfrac12)
(F_{U,\chi}^+*_MF_{U,\chi}^-).
}
\tag{4.5}
\]

No source completion or Wick projection appears in (4.5).

---

## 5. Cross-Hodge polarization and color-flatness

On logarithmic coordinates put

\[
f_\chi(u)=F_{U,\chi}^+(e^u),
\qquad
g_\chi(u)=F_{U,\chi}^-(e^u),
\]

and \((R_xg)(u)=g(x-u)\).  Define

\[
\mathcal A_\chi(x)
=\frac14\|f_\chi+R_xg_\chi\|_2^2,
\qquad
\mathcal D_\chi(x)
=\frac14\|f_\chi-R_xg_\chi\|_2^2.
\tag{5.1}
\]

Polarization gives

\[
(F_{U,\chi}^+*_MF_{U,\chi}^-)(e^x)
=\mathcal A_\chi(x)-\mathcal D_\chi(x),
\tag{5.2}
\]

and

\[
\mathcal A_\chi(x)+\mathcal D_\chi(x)
=\frac12(\|f_\chi\|_2^2+\|g_\chi\|_2^2),
\tag{5.3}
\]

which is constant in \(x\).

The cross-convolution (5.2) is independent of color.  Hence for two colors
\(\chi,\chi'\), subtraction of (5.2)--(5.3) gives

\[
\mathcal D_\chi(x)-\mathcal D_{\chi'}(x)=\text{constant}.
\tag{5.4}
\]

Put

\[
K_2=DK_1,
\qquad
L(D)=D(D+\tfrac32)(D-\tfrac12).
\]

Since \(L(D)\) kills constants, (4.5) becomes

\[
\boxed{
\mathcal B_U^{K_2}(e^x)
=-2L(D)\mathcal D_\chi(x)
=2L(D)\mathcal A_\chi(x).
}
\tag{5.5}
\]

Therefore

\[
\boxed{
(\mathcal B_U^{K_2})_-
=2(L(D)\mathcal D_\chi)_+.
}
\tag{5.6}

This is the native F1 Hodge gate.  Its differential current is independent of
prime color.

---

## 6. Explicit derivative kernel

Differentiating the corrected same-\(K_1\) wavelet gives

\[
\boxed{
K_2(y)=
\begin{cases}
4\sqrt y-3,&1\le y<2,\\
-4(1+\sqrt2)\sqrt y+3(1+2\sqrt2),&2\le y<4,\\
2(1+2\sqrt2)\sqrt y-6(1+\sqrt2),&4\le y<8,\\
-2\sqrt y+6,&8\le y<16,\\
0,&\text{otherwise}.
\end{cases}
}
\tag{6.1}
\]

Its multiplier is

\[
\widehat K_2(s)
=
\frac{(1-\sqrt2\,2^{-s})^2(1-2^{-s})^2(s+\frac32)}
{s(s-\frac12)}.
\tag{6.2}
\]

The five jumps at \(1,2,4,8,16\) are precisely the coefficients of

\[
\Delta_4=(I-S)^2(I-\sqrt2S)^2:
\]

\[
1,
-(2+2\sqrt2),
3+4\sqrt2,
-(4+2\sqrt2),
2.
\tag{6.3}
\]

---

## 7. Exact Hardy endpoint and jump filter

For any finite real coefficient sequence \((c_n)\), define

\[
H_2(X)=\sum_nc_nK_2(X/n).
\tag{7.1}
\]

Every breakpoint is an integer, so on \(m<X<m+1\),

\[
H_2(X)=A_m+B_m\sqrt X.
\tag{7.2}

Put

\[
P_c(x)=\sum_{n\le x}c_n,
\qquad
Q_c(x)=\sum_{n\le x}\frac{c_n}{\sqrt n},
\]

\[
W_c(x)=3P_c(x)-4\sqrt xQ_c(x).
\tag{7.3}
\]

Direct telescoping of the four active dyadic bands gives

\[
\boxed{H_2(m+)=-\Delta_4W_c(m).}
\tag{7.4}
\]

The square root in \(W_c(m/2^j)\) is taken at the real argument.

Let \(S_{\rm at}c(m)=\mathbf1_{2\mid m}c_{m/2}\).  The jump is

\[
\boxed{
H_2(m+)-H_2(m-)
=(I-S_{\rm at})^2(I-\sqrt2S_{\rm at})^2c(m).
}
\tag{7.5}

For \(c_n=\mu(n)/\sqrt n\), each shifted term contributes
\(O(M^{-1/2})\) to

\[
\sum_{M\le m\le2M}\frac{|\text{jump}(m)|}{m}.
\tag{7.6}

Thus the jump ledger is absolutely closed.

---

## 8. Exact signed area of one cell

Let

\[
u=H_2(m+),
\qquad
v=H_2((m+1)-),
\]

and set \(a=\sqrt m\), \(b=\sqrt{m+1}\).  On the cell,

\[
H_2(t^2)=A+Bt,
\]

where

\[
B=\frac{v-u}{b-a},
\qquad
A=\frac{bu-av}{b-a}.
\]

With \(F(t)=A\log t+Bt\), the negative logarithmic area is

\[
\mathfrak n_m(u,v)
=2\int_a^b\frac{(-A-Bt)_+}{t}\,dt.
\tag{8.1}
\]

If the signs agree, this is either zero or

\[
-2(F(b)-F(a)).
\]

If they differ, the root is

\[
r=\frac{av-bu}{v-u},
\]

and the integral is the corresponding negative-side primitive ending or
beginning at \(r\).  This proves the four-case formula in `L-105504`.

For

\[
c_n=\frac{\mu(n)}{\sqrt n},
\]

(7.4)--(7.5) give

\[
u_m=-\Delta_4W_\mu(m),
\]

\[
v_m=-\Delta_4W_\mu(m+1)-\Delta_{4,\rm at}c(m+1).
\tag{8.2}
\]

Hence, at integer \(Y\),

\[
\boxed{
\int_1^Y(G_2(X))_-\frac{dX}{X}
=
\sum_{m<Y}\mathfrak n_m(u_m,v_m).
}
\tag{8.3}
\]

---

## 9. Type-I removal for the derivative kernel

The kernel

\[
k_2(x)=x^{-1/2}K_2(1/x)
\]

is compactly supported and of bounded variation.  Equation (6.2) gives

\[
\int k_2(x)\,dx=\widehat K_2(1/2)=0.
\]

The bounded-variation Riemann-sum inequality therefore yields

\[
\sum_{m\ge1}\frac1{\sqrt m}K_2(Y/m)
=O(Y^{-1/2}).
\tag{9.1}
\]

Because \(K_2\) has jumps, no \(Y^{-3/2}\) bound is claimed.

On the dyadic block \(I_j=[2^j,2^{j+1})\), freeze

\[
U_j=\lfloor2^{j/6}\rfloor.
\]

Apply the exact Vaughan identity to the fixed scalar

\[
G_2(X)=\sum_n\frac{\mu(n)}{\sqrt n}K_2(X/n).
\]

For every sufficiently large block, \(U_j<X/16\), so compact support removes
the \(2\mu_{U_j}\) row.  The finitely many initial blocks contribute finite
logarithmic mass and are absorbed once into the initial ledger.  On each
cofinal block the Type-I row is

\[
T_{2,j}(X)
=-\sum_{a,b\le U_j}\frac{\mu(a)\mu(b)}{\sqrt{ab}}
\sum_m\frac1{\sqrt m}K_2(X/(abm)).
\]

Using (9.1) with \(Y=X/(ab)\), each pair contributes \(O(X^{-1/2})\), so

\[
\boxed{T_{2,j}(X)=O(U_j^2X^{-1/2})=O(X^{-1/6}).}
\tag{9.2}
\]

This has finite logarithmic \(L^1\) mass.  The balanced row is exactly the
source (1.3) and hence the Hodge mismatch (5.5).

---

## 10. RH equivalence

Define `NATIVECELL105504` by

\[
\sum_{m<Y}\mathfrak n_m(u_m,v_m)=Y^{o(1)}.
\tag{10.1}
\]

The Mellin transform of \(G_2\) is

\[
\frac{\widehat K_2(s)}{\zeta(s+1/2)}.
\]

The numerator is nonzero in \(0<\Re s<1/2\).  The fixed negative-mass
Mellin–Landau theorem gives

\[
\mathrm{NATIVECELL}_{105504}\Longrightarrow\mathrm{RH}.
\]

Conversely RH gives the standard subpower bound for the compact
ordinary-Möbius wavelet, hence (10.1).  Therefore

\[
\boxed{\mathrm{NATIVECELL}_{105504}\Longleftrightarrow\mathrm{RH}.}
\tag{10.2}
\]

Define `NATIVEF1XD105504` by

\[
\sum_j\int_{I_j\cap[1,Y]}
\bigl(L(D)\mathcal D_j(\log X)\bigr)_+\frac{dX}{X}
=Y^{o(1)}.
\tag{10.3}
\]

Equation (5.6) identifies this with one half of the balanced-row negative
mass.  Equation (9.2) permits addition or removal of the Type-I row in both
directions.  Hence

\[
\boxed{
\mathrm{NATIVEF1XD}_{105504}
\Longleftrightarrow
\mathrm{NATIVECELL}_{105504}
\Longleftrightarrow
\mathrm{RH}.
}
\tag{10.4}
\]

The equivalence is proved.  The estimate (10.3), and therefore RH, remains
open.

---

## 11. Replay boundary

The committed finite replay checks source identities, color covariance,
Vaughan compression, the explicit kernel, all endpoint and jump identities,
Hodge polarization, and the cell primitive.

```text
PASS_T105500_NATIVE_F1_TAIL_PAIR
e25255643bfd11e9fc931b4484189d0f6178bcf5537f39d734acb0b3da84a386
checks=161264
rh_established=false
```
