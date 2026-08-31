# Volterra Green-lift compression: an Euler--Lagrange firewall

Status: **PROVED ABSTRACT COUNTEREXAMPLE; THE SPECIAL RIEMANN-SOURCE INEQUALITY REMAINS OPEN.**

This note strengthens Section 9 of
[`XI_SOURCE_HERMITE_STIELTJES_CLOSURE.md`](XI_SOURCE_HERMITE_STIELTJES_CLOSURE.md).
It shows that the following data do not by themselves imply contraction
of a compressed multiplier:

1. a contraction `K` on a lifted Hilbert space;
2. a surjective compression `C` and right inverse `E`, with `C E=I`;
3. a nontrivial closed trace kernel;
4. nonnegativity of the difference form on that kernel;
5. the exact Euler--Lagrange orthogonality of the selected lift against the
   kernel.

Consequently a completed-domain or density argument cannot promote the
pointwise bound `|kappa|<=1` into `||C K E||<=1` without one additional
source-specific weighted inequality or intertwining identity.

## 1. Exact finite-dimensional model

Fix a real number `M>1`.  Let

\[
 {\cal D}=\mathbb R^3,\qquad X=\mathbb R^2,
\]

with their Euclidean inner products, and set

\[
 C=
 \begin{pmatrix}
 M&0&0\\
 0&1&0
 \end{pmatrix},
 \qquad
 E=
 \begin{pmatrix}
 M^{-1}&0\\
 0&1\\
 0&0
 \end{pmatrix},
 \tag{VG1}
\]

and

\[
 K=
 \begin{pmatrix}
 0&1&0\\
 1&0&0\\
 0&0&0
 \end{pmatrix}.
 \tag{VG2}
\]

Then

\[
 CE=I_X,\qquad \|K\|=1,
 \tag{VG3}
\]

and

\[
 N=\ker C=\operatorname{span}\{e_3\}
 \tag{VG4}
\]

is nontrivial.

Define the plus/minus observation maps and the difference form by

\[
 G_+f=Cf,\qquad G_-f=CKf,
\]

\[
 Q(f,h)=\langle G_+f,G_+h\rangle_X
        -\langle G_-f,G_-h\rangle_X.
 \tag{VG5}
\]

For every `h in N`, both `C h` and `C K h` vanish.  Therefore

\[
 Q(h,h)=0\ge0,
 \tag{VG6}
\]

and, for every `x in X`,

\[
 Q(Ex,h)=0.
 \tag{VG7}
\]

Thus `Ex` obeys the exact fibre Euler--Lagrange orthogonality.  Indeed for
every `h in N`,

\[
 Q(Ex+h,Ex+h)=Q(Ex,Ex)+Q(h,h)=Q(Ex,Ex).
 \tag{VG8}
\]

So the selected lift is a difference-form minimizer in its fibre; the
kernel form is nonnegative; and all finite-dimensional closure, density and
continuity requirements are automatic.

## 2. Compressed multiplier is not a contraction

Direct multiplication gives

\[
 CKE=
 \begin{pmatrix}
 0&M\\
 M^{-1}&0
 \end{pmatrix}.
 \tag{VG9}
\]

Hence

\[
 \boxed{\qquad \|CKE\|=M>1.\qquad}
 \tag{VG10}
\]

For example, the second unit vector is sent to `M` times the first unit
vector.

This model satisfies the abstract statements

\[
 CE=I,\quad \|K\|\le1,\quad Q|_{\ker C}\ge0,
 \quad Q(Ex,h)=0\ (h\in\ker C),
 \tag{VG11}
\]

but violates the desired output contraction.

## 3. Exact missing inequality

The desired conclusion is equivalent to

\[
 E^*K^*C^*CKE\le I_X
 =E^*C^*CE.
 \tag{VG12}
\]

Pointwise contraction gives only `K^*K<=I` in the lifted metric.  It does
not imply (VG12) because the positive weight `C^*C` need not commute with
`K` and the selected right inverse need not be isometric for that weight.
The model above has

\[
 C^*C=\operatorname{diag}(M^2,1,0),
\]

which is exactly where the amplification occurs.

For the Riemann-source multiplier

\[
 \kappa(r)=\frac{1-r}{1+r},
\]

the algebraic defect is

\[
 1-\kappa(r)\kappa(q)
 =\frac{2(r+q)}{(1+r)(1+q)}.
 \tag{VG13}
\]

After restoring the lifted plus factors `(1+r)(1+q)`, (VG13) becomes the
original signed source/Hermite factor `2(r+q)`.  Thus the concrete weighted
inequality (VG12), when expanded in the actual source variables, is the
positivity theorem to be proved rather than a consequence of the scalar
bound on `kappa`.

## 4. Precise scope

This counterexample does **not** prove that the concrete Hardy--Volterra map
for the Riemann theta source fails.  It proves that the displayed abstract
inputs are insufficient.  A successful Volterra proof must add and prove at
least one genuinely source-specific statement, for example:

- a weighted intertwining making `C^*C` commute with the multiplier on the
  Green-lift range;
- an isometric/coisometric realization of the selected lift in the plus
  metric;
- or the direct weighted inequality (VG12).

Any of these would be substantive.  None follows from Euler--Lagrange
orthogonality, nonnegativity on the trace kernel, pointwise `|kappa|<=1`, or
completion by density alone.
