# A growing-depth divisor ladder for the original coefficient quotient

**Status:** proposed source-specific analytic theorem; independent proof review required.  
**Parent source:** `CUSP_FLAG_FIXED_DEPTH_DIVISOR_LADDER.md` in PR #766 at
`17c7624a0bd56c5356d00278b2a846d2efdbdccc`.  
**Repository effect:** proof/exposition only; no producer, fixture, or inherited
certificate is modified.  
**RH/GRH status:** RH and GRH remain unproved.

The parent proves the endpoint divisor ladder with the quantifier order

\[
J\ \text{fixed},\qquad k\to\infty.
\]

This note tracks the depth dependence in that proof.  It yields the first
growing-depth theorem for the **same original coefficient quotient**.

The conservative uniform regime is

\[
\boxed{L(k)^3\log(k+2)=o(k).}
\tag{GD0}
\]

For every \(J\le L(k)\), all zero/pole clusters near
\(k(1-s)=12J\) survive simultaneously, with the same simple interlacing and
the same residue and gap laws as in the fixed-depth theorem.

A consequence is that the original quotient \(Q_1\), at one weight \(k\),
has a number of distinct real endpoint zero/pole clusters tending to
infinity.

---

## 1. Exact imported source identities

Retain the level-one cusp space \(S_k\), the Miller coefficient flag

\[
W_i=\{f:[q]f=\cdots=[q^{i-1}]f=0\},
\]

the completed period \(I(s)\), and

\[
D_i(s)=\det I(s)|_{W_i},\qquad
Q_i(s)=\frac{D_i(s)}{D_{i+1}(s)}.
\]

Write

\[
c=k(1-s),\qquad
A_n=A_n(k)=\frac{\Gamma(k-1)}{(4\pi n)^{k-1}},
\qquad
F_n(c)=\frac1{24n}-\frac1{2c}.
\tag{GD1}
\]

For a depth \(J\), put \(N=J+1\).  The parent constructs the exact
unit-triangular source chart

\[
(h_1,\ldots,h_J,W_N)
\]

with

\[
[q^m]h_l=\delta_{lm}\qquad(1\le l,m\le J).
\tag{GD2}
\]

The following parent identities and inequalities are imported without
change:

1. the complete \(q\)-tail estimate, with
   \[
   B_J=4\cdot3^{J-1}1000^J;
   \tag{GD3}
   \]

2. the low-domain estimate at
   \[
   Y=\frac{k}{10000(J+1)};
   \tag{GD4}
   \]

3. the full-Fourier projection estimate from a shallow \(q^l\) direction
   to \(W_N\);

4. the Schur elimination of the full deep space \(W_N\);

5. the exact arithmetic cross integral
   \[
   B_{lm}
   =
   2h^{s-1/2}\sigma_{1-2s}(h)
   \int_Y^\infty
   y^{k-3/2}e^{-2\pi(l+m)y}
   K_{s-1/2}(2\pi h y)\,dy,
   \quad h=m-l;
   \tag{GD5}
   \]

6. the exact source Schur identities
   \[
   Q_i=a_i-\frac{b_i^2}{d_i},
   \qquad
   \delta_i=d_i-\frac{b_i^2}{a_i}.
   \tag{GD6}
   \]

Here \(\delta_i\) is the final scalar Schur complement whose zero is the
zero of \(D_i\) after all nonvanishing blocks have been eliminated.

No abstract matrix surrogate replaces these source identities.

---

## 2. Statement of the growing-depth theorem

Fix once and for all

\[
0<\Delta<\Delta_1<6.
\tag{GD7}
\]

All complex estimates are proved on the larger closed
\(\Delta_1\)-disc and then used on the \(\Delta\)-disc.  This fixed
buffer pays every Cauchy derivative estimate; no depth-dependent contour
shrinkage is used.

Let \(L=L(k)\) be a positive integer sequence satisfying GD0.  For every
\(1\le J\le L\), define the disjoint disc

\[
\Omega_{J,\Delta}
=
\{c:|c-12J|<\Delta\}.
\tag{GD8}
\]

### Theorem 2.1 — simultaneous growing divisor ladder

For all sufficiently large even \(k\), simultaneously for every
\(1\le J\le L(k)\) and every \(1\le i\le J\):

1. \(D_i\) has exactly one zero, counting multiplicity, in
   \(\Omega_{J,\Delta}\);

2. that zero is real and simple; write its \(c\)-coordinate as
   \(c_{i,J}\);

3. \(D_{J+1}\) is nonzero throughout the disc;

4. uniformly in \(i,J\),
   \[
   c_{i,J}=12J+o(1);
   \tag{GD9}
   \]

5. the zeros strictly interlace:
   \[
   c_{J,J}<c_{J-1,J}<\cdots<c_{1,J};
   \tag{GD10}
   \]

6. \(Q_J\) has one simple zero and no pole in the disc;

7. for \(i<J\), \(Q_i\) has one simple zero and one simple pole in the
   disc, with no cancellation: the zero is \(c_{i,J}\) and the pole is
   \(c_{i+1,J}\);

8. uniformly for \(i<J\),
   \[
   c_{i,J}-c_{i+1,J}
   =
   \frac{288J^2S_{J-i}^2}{F_i(12J)}
   \frac{A_J}{k^2A_i}
   (1+o(1)),
   \tag{GD11}
   \]
   where \(S_h=\sigma_{-1}(h)\);

9. uniformly for \(i<J\), the right-hand \(s\)-residue is
   \[
   \operatorname{Res}Q_i
   =
   \frac{288J^2S_{J-i}^2A_J}{k^2}(1+o(1))>0.
   \tag{GD12}
   \]

Reflection gives the corresponding left clusters and reverses the residue
signs.

### Corollary 2.2 — a growing census for the original quotient

The discs GD8 are disjoint.  Therefore \(Q_1\), at weight \(k\), has at
least

\[
L(k)
\]

distinct simple right-end real zeros and at least

\[
L(k)-1
\]

distinct simple right-end real poles, plus their reflected partners.

For example, every choice

\[
L(k)=o\!\left(\left(\frac{k}{\log k}\right)^{1/3}\right)
\tag{GD13}
\]

is permitted.  In particular one may take

\[
L(k)=\left\lfloor\frac{k^{1/3}}{\log k}\right\rfloor.
\tag{GD14}
\]

This is a fixed-weight growing divisor census for one original quotient,
not a statement about different proper theta quotients.

---

## 3. Quantitative source-tail extraction

The parent writes several estimates as \(C_J\) because \(J\) is fixed
there.  The first task is to expose enough of that dependence.

### Lemma 3.1 — exponential depth envelope

There is an absolute \(C_0>1\) such that all deep-space and low-domain
errors used below are bounded by an expression of the form

\[
\mathfrak e_{k,J}
=
C_0^{\,J}(J+1)^8k^{2J+4}
\left[
\left(\frac{J}{J+1}\right)^{k-1}
+
10^{-k}
\right].
\tag{GD15}
\]

More precisely, after division by the natural \(kA_l\), \(A_m\), or
\(kA_J\) scale of the entry under consideration, the corresponding error
is bounded by a fixed polynomial in \(J\) times \(\mathfrak e_{k,J}\).

#### Proof

The displayed parent proof already supplies all ingredients.

* The echelon tail constant is exactly GD3, hence exponential in \(J\).
* Every use of the recursion GD2 contributes at most one further finite
  sum of length \(J\); no determinant expansion is used.
* The low-domain proof contributes \(k^{2J}10^{-k}A_N\), multiplied by
  an exponential-in-\(J\) source coefficient.
* A shallow-to-deep cross functional is bounded by an
  exponential-in-\(J\) constant times
  \(k^{J+2}\sqrt{A_N}\).
* Squaring that bound and applying the deep inverse gives an
  exponential-in-\(J\) constant times \(k^{2J+3}A_N\).
* Division by \(kA_J\), together with
  \[
  \frac{A_N}{A_J}
  =
  \left(\frac{J}{J+1}\right)^{k-1},
  \tag{GD16}
  \]
  is absorbed by GD15.

The harmless factor \((J+1)^8k^3\) deliberately overpays all finite sums,
Cauchy buffers, and the row/column separation in the Schur correction.
The key point is that no step produces \(C^{J^2}\): the proof uses the
explicit triangular chart and operator Schur complements rather than a
cofactor expansion. ∎

### Lemma 3.2 — the envelope is negligible in the declared regime

If \(J\le L(k)\) and GD0 holds, then for every fixed \(A>0\),

\[
\max_{1\le J\le L(k)}J^A\mathfrak e_{k,J}\longrightarrow0.
\tag{GD17}
\]

#### Proof

For \(J\ge1\),

\[
\log\left(\frac{J+1}{J}\right)\ge\frac1{2J}.
\]

Hence the logarithm of the first term in GD15 is at most

\[
O(J\log(J+2))
+(2J+4)\log k
-\frac{k-1}{2J}.
\tag{GD18}
\]

Condition GD0 gives

\[
\frac{k}{J}\gg J^2\log k
\]

uniformly for \(J\le L\), so the negative term in GD18 dominates every
positive term, even after adding \(A\log J\).  The \(10^{-k}\) term is
easier. ∎

Define the common error gauge

\[
\eta_{k,L}
=
\frac{L^3\log(k+2)}{k}
+
L^2\max_{J\le L}\mathfrak e_{k,J}.
\tag{GD19}
\]

By GD0 and Lemma 3.2,

\[
\eta_{k,L}\to0.
\tag{GD20}
\]

---

## 4. Uniform deep-space invertibility

The fixed-depth proof uses the exact reserve

\[
\Re\frac1{2c}-\frac1{24N}
=
\frac{(6N)^2-|c-6N|^2}{24N|c|^2}.
\tag{GD21}
\]

For \(N=J+1\) and \(c\in\overline{\Omega}_{J,\Delta}\),

\[
|c-6N|
\le6(J-1)+\Delta.
\]

Therefore

\[
\Re\frac1{2c}-\frac1{24N}
\ge
\frac{12-\Delta}
     {24(J+1)(12J+\Delta)}.
\tag{GD22}
\]

This is a positive constant times \(J^{-2}\), uniformly in \(J\).

The complex-power argument of the parent remains uniform for
\(|c|\le12L+\Delta_1=o(k)\).  Here is the depth accounting explicitly.
For the probability measure attached to a nonzero \(f\in W_N\), the
parent moment estimate gives

\[
\mathbb E_f X\le 1+\frac{k-1}{4\pi N}\le C\frac{k}{N}.
\tag{GD23a}
\]

Put \(\epsilon=c/k\), \(\alpha=1/\log k\), and
\(\beta=\Re\epsilon+\alpha\).  For large \(k\), \(0<\beta<1\).
The same Jensen argument as LS5--LS6 gives

\[
\mathbb E_f|y^\epsilon|=O_{\Delta_1}(1),
\qquad
\mathbb E_f|y^\epsilon-1|
=O_{\Delta_1}\!\left(\frac{J\log(k+2)}k\right).
\tag{GD23b}
\]

Indeed
\((\mathbb E_fX)^\beta
\le(Ck/N)^\beta
=\exp(O(1)+O(J\log k/k))=O(1)\).
The regular/Laurent expansions are now uniform:

\[
C(1-c/k)=\frac\pi6+O_{\Delta_1}(J/k),
\qquad
D(1-c/k)=-\frac{k}{2c}+O_{\Delta_1}(1).
\tag{GD23c}
\]

The error in the first term is
\(O((J/k)(k/N))=O(1)\).  In the second term, the pole coefficient
\(k/|c|\asymp k/J\) multiplied by the difference estimate in GD23b gives
\(O(\log k)\).  The complex Bessel remainder is bounded exactly as in
LS8--LS9.  Therefore

\[
\Re\frac{I_{1-c/k}(f,f)}{G(f)}
\le
\frac{k}{24N}
-k\Re\frac1{2c}
+C_{\Delta_1}\log(k+2)
\tag{GD23}
\]

uniformly over \(J\le L\) and the larger closed disc.
No pointwise replacement of \(y^{c/k}\) by \(1\) is made.

Combining GD22--GD23 and GD0 gives, for the deep block
\(E=I|_{W_N}\),

\[
-\Re E\ge c_\Delta\frac{k}{J^2}G
\tag{GD24}
\]

for all sufficiently large \(k\).  Consequently

\[
\boxed{\|E^{-1}\|_{G^*\to G}\le C_\Delta\frac{J^2}{k}.}
\tag{GD25}
\]

Thus \(D_{J+1}\) is nonzero throughout every declared disc.

---
