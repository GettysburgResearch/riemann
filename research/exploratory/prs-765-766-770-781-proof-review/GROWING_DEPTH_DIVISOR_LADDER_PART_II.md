# A growing-depth divisor ladder — Part II: shallow matrix and finite-block inversion

This file continues [Part I](GROWING_DEPTH_DIVISOR_LADDER_PART_I.md). Equation numbering is continuous.

## 5. The uniform shallow matrix after deep elimination

Eliminate \(W_N\) and denote the remaining \(J\times J\) analytic matrix
by \(H(c)\).

### Lemma 5.1 — diagonal entries

Uniformly for \(J\le L\), \(1\le l\le J\), and
\(c\in\overline{\Omega}_{J,\Delta}\),

\[
\frac{H_{ll}(c)}{kA_l}
=
F_l(c)
+
O_\Delta\!\left(
\frac{J\log(k+2)}{kl}
+\mathfrak e_{k,J}
\right).
\tag{GD26}
\]

For the deepest entry,

\[
\frac{H_{JJ}(c)}{kA_J}
=
F_J(c)
+
O_\Delta\!\left(
\frac{\log(k+2)}{k}
+\mathfrak e_{k,J}
\right),
\tag{GD27}
\]

and

\[
\frac{\partial_cH_{JJ}(c)}{kA_J}
=
F_J'(c)
+
O_\Delta\!\left(
\frac{\log(k+2)}{kJ}
+\mathfrak e_{k,J}
\right).
\tag{GD28}
\]

#### Proof

The parent gives the exact diagonal model

\[
T_l(c)
=
C(s)\frac{\Gamma(k-1+s)}{(4\pi l)^{k-1+s}}
+
D(s)\frac{\Gamma(k-s)}{(4\pi l)^{k-s}},
\qquad s=1-c/k.
\tag{GD29}
\]

Uniform Stirling/digamma estimates for
\(|c|\le12L+\Delta=o(k)\) give

\[
\frac{T_l(c)}{kA_l}
=
\frac1{24l}-\frac1{2c}
+
O_\Delta\!\left(\frac{J\log(k+2)}{kl}\right).
\tag{GD30}
\]

At \(l=J\), the factor \(J/l\) disappears and gives GD27.
Differentiating GD29 gives the asserted derivative estimate for the
model.  The complete deep correction is analytic on the larger
\(\Delta_1\)-disc; Cauchy's estimate across the fixed buffer
\(\Delta_1-\Delta\) pays its derivative with the same depth envelope.
This proves GD28. ∎

### Lemma 5.2 — arithmetic crosses

For real \(c\in[12J-\Delta,12J+\Delta]\) and \(l<m\le J\),

\[
\frac{H_{lm}(c)}{A_m}
=
S_{m-l}
\left[
1+
O_\Delta\!\left(
\frac{J\log(J+2)}{k}
+\mathfrak e_{k,J}
\right)
\right].
\tag{GD31}
\]

In particular these crosses are positive.

On the full complex disc,

\[
|H_{lm}(c)|
\le C_\Delta(m-l)A_m
+C_\Delta\mathfrak e_{k,J}A_m.
\tag{GD32}
\]

#### Proof

In GD5, replacing \(K_{s-1/2}\) by \(K_{1/2}\) gives the exact arithmetic
factor

\[
h^{s-1}\sigma_{1-2s}(h),
\qquad h=m-l.
\]

For \(h\le J\) and \(c=12J+O(1)\),

\[
h^{s-1}\sigma_{1-2s}(h)
=
S_h
\left(1+O\!\left(\frac{J\log(J+2)}k\right)\right).
\tag{GD33}
\]

The \(K\)-Bessel comparison contributes \(O(J/k)\), because
\(y\ge Y=k/(10000(J+1))\).  The omitted low integral and all source-tail
terms are absorbed by Lemma 3.1.  This proves GD31.

The parent complex-order estimate gives the deliberately coarser
\(|B_{lm}|\le hA_m\), which gives GD32 after the same source corrections. ∎

The complex bound GD32, rather than the sharper real divisor average, is
the reason the present full-ladder theorem stops at a cube-root scale.

---

## 6. Uniform inversion of every earlier finite block

Let \(M\subset\{1,\ldots,J-1\}\) be an interval.  Put

\[
A_M=\operatorname{diag}(A_m:m\in M),
\qquad
\mathcal C_M=\frac1kH_{MM}A_M^{-1},
\]

and

\[
\mathcal D_M=\operatorname{diag}(F_m(c):m\in M).
\]

For \(m<J\), the exact identity

\[
F_m(c)
=
\frac{12(J-m)+(c-12J)}{24m\,c}
\tag{GD34}
\]

gives on the closed disc

\[
|F_m(c)|
\ge
c_\Delta\frac{J-m}{J^2}.
\tag{GD35}
\]

Hence

\[
\|\mathcal D_M^{-1}\|_\infty\le C_\Delta J^2.
\tag{GD36}
\]

### Lemma 6.1 — finite-block inverse

Uniformly over all such intervals \(M\),

\[
\left\|
\mathcal D_M^{-1}
(\mathcal C_M-\mathcal D_M)
\right\|_\infty
\le C_\Delta\eta_{k,L}.
\tag{GD37}
\]

Consequently, for sufficiently large \(k\),

\[
H_{MM}^{-1}
=
A_M^{-1}\frac1k\mathcal C_M^{-1},
\qquad
\|\mathcal C_M^{-1}\|_\infty\le C_\Delta J^2.
\tag{GD38}
\]

#### Proof

There are three contributions.

1. **Diagonal error.**  GD26 and GD35 give
   \(O(J^2\log k/k)+O(J^2\mathfrak e_{k,J})\).

2. **Strictly upper entries.**  For a row indexed by \(m\), put
   \(r=J-m\).  The complex estimate GD32 gives
   \[
   \sum_{n>m}\frac{|H_{mn}|}{kA_n}
   \le
   \frac{C_\Delta}{k}\sum_{h=1}^{r}h
   \le C_\Delta\frac{r^2}{k}.
   \]
   Multiplication by \(1/|F_m|\le C_\Delta J^2/r\) gives
   \(O(J^2r/k)\le O(J^3/k)\).

3. **Strictly lower entries.**  Real symmetry of the source matrix and
   column scaling produce the factor
   \[
   \frac{A_l}{A_m}
   =
   \left(\frac{m}{l}\right)^{k-1},
   \qquad l>m,
   \]
   which is bounded by \(e^{-c k/J}\) even for adjacent indices and is
   absorbed by Lemma 3.2.

These estimates give GD37.  Neumann inversion gives GD38. ∎

No exponentially ill-conditioned Petersson whitening is introduced.
Column scaling by the exact \(A_m\) remains load-bearing.

---

## 7. Uniform two-by-two Schur data

Fix \(i<J\), and eliminate the interval

\[
M=\{i+1,\ldots,J-1\}.
\]

After the already completed deep elimination, write the remaining block on
\((h_i,h_J)\) as

\[
\begin{pmatrix}
a_i&b_i\\
\widetilde b_i&d_i
\end{pmatrix}.
\]

On the real interval, the matrix is real symmetric and
\(\widetilde b_i=b_i\).

### Lemma 7.1

Uniformly for \(i<J\), \(J\le L\), and real
\(|c-12J|\le\Delta\),

\[
\frac{a_i(c)}{kA_i}
=
F_i(c)(1+O_\Delta(\eta_{k,L})),
\tag{GD39}
\]

\[
\frac{b_i(c)}{A_J}
=
S_{J-i}(1+O_\Delta(\eta_{k,L})),
\tag{GD40}
\]

\[
\frac{d_i(c)}{kA_J}
=
F_J(c)+O_\Delta\!\left(\frac{\eta_{k,L}}{J^2}\right),
\tag{GD41}
\]

and

\[
\frac{d_i'(c)}{kA_J}
=
F_J'(c)(1+O_\Delta(\eta_{k,L})).
\tag{GD42}
\]

The same deepest estimates hold for \(i=J\), with no earlier block.

#### Proof

The diagonal statements follow from Lemma 5.1 and the fact that every
Schur correction involving unequal \(A_m\) scales contains an exponentially
small ratio \(A_{m+1}/A_m\le e^{-c k/J}\).

For the cross, the direct entry is
\(A_JS_{J-i}(1+o(1))\) by GD31.  The correction is

\[
H_{iM}H_{MM}^{-1}H_{MJ}.
\]

Using GD38, the elementary sums

\[
\sum_{h\le J}S_h
=
\sum_{d\le J}\frac1d\left\lfloor\frac Jd\right\rfloor
\le\zeta(2)J,
\tag{GD43}
\]

and \(S_h\le1+\log h\), gives the deliberately coarse bound

\[
|H_{iM}H_{MM}^{-1}H_{MJ}|
\le
C_\Delta A_J\frac{J^3\log(J+2)}{k}
+
C_\Delta A_JJ^2\mathfrak e_{k,J}.
\tag{GD44}
\]

Since \(S_{J-i}\ge1\), this is the relative error in GD40.

For \(d_i\), both cross vectors carry an \(A_J\) factor while the inverse
carries \(A_m^{-1}\); hence every correction contains
\(A_J/A_m\le e^{-c k/J}\).  The same is true after one \(c\)-derivative.
This proves GD41--GD42. ∎

The cube-root condition pays the full complex block inversion and the
coarse real Schur correction simultaneously.  A weighted triangular norm
should reduce the \(J^3\) loss; that optimization is not silently assumed.

---
