# A growing-depth divisor ladder — Part III: Rouché, interlacing, and the next scale

This file continues [Part II](GROWING_DEPTH_DIVISOR_LADDER_PART_II.md). Equation numbering is continuous.

## 8. One zero in every disc

For \(c\in\partial\Omega_{J,\Delta}\),

\[
|F_J(c)|
=
\frac{|c-12J|}{24J|c|}
\ge
\frac{\Delta}{24J(12J+\Delta)}
\ge \frac{c_\Delta}{J^2}.
\tag{GD45}
\]

By GD39--GD42 and the exact Schur identity GD6,

\[
\frac{\delta_i(c)}{kA_J}
=
F_J(c)
+
O_\Delta\!\left(\frac{\eta_{k,L}}{J^2}\right)
+
O_\Delta\!\left(
\frac{A_J}{k^2A_i|F_i(c)|}
(1+\log J)^2
\right).
\tag{GD46}
\]

The last term is uniformly negligible.  Indeed its worst case is
\(i=J-1\), and then

\[
\frac{A_J}{A_{J-1}}
=
\left(1-\frac1J\right)^{k-1}
\le e^{-c k/J}.
\tag{GD47}
\]

Thus, by GD20 and Rouché's theorem, \(\delta_i\) and \(F_J\) have the
same number of zeros in the disc: exactly one.

Every eliminated block is nonzero there, so this is exactly the zero count
of \(D_i\).  Schwarz symmetry makes the unique zero real.

On the real interval,

\[
F_J'(c)=\frac1{2c^2}\ge\frac{c_\Delta}{J^2}.
\tag{GD48}
\]

Equations GD42 and GD46, differentiated once, show that
\(\delta_i'(c)>0\) near the zero.  Hence the zero is simple.

The same estimates and the mean-value theorem give the uniform location

\[
c_{i,J}=12J+O_\Delta(\eta_{k,L}),
\tag{GD49}
\]

which proves GD9.

---

## 9. Exact interlacing, gap, and residue

For \(i<J\), the scalar \(d_i\) is \(\delta_{i+1}\).  The exact identities
GD6 give:

* at \(c=c_{i,J}\),
  \[
  d_i(c)=\frac{b_i(c)^2}{a_i(c)}>0;
  \tag{GD50}
  \]

* at \(c=c_{i+1,J}\),
  \[
  d_i(c)=0.
  \tag{GD51}
  \]

Equations GD39--GD42 imply

\[
a_i>0,\qquad b_i>0,\qquad d_i'>0
\]

throughout the tiny interval between the two roots.  Therefore

\[
c_{i,J}>c_{i+1,J}.
\]

Moreover, for some \(\xi_{i,J}\) between them,

\[
c_{i,J}-c_{i+1,J}
=
\frac{b_i(c_{i,J})^2}
     {a_i(c_{i,J})d_i'(\xi_{i,J})}.
\tag{GD52}
\]

Using GD39--GD42, GD49, and

\[
F_J'(12J)=\frac1{288J^2},
\]

in GD52 proves GD11 uniformly.

At the pole \(d_i=0\), the numerator in
\(Q_i=a_i-b_i^2/d_i\) is \(-b_i^2\ne0\); hence there is no cancellation.
The \(c\)-residue is \(-b_i^2/d_i'\).  Since \(dc/ds=-k\), the
\(s\)-residue is

\[
\frac{b_i^2}{k\,d_i'},
\]

and GD40--GD42 give GD12.

This completes the proof of Theorem 2.1.

---

## 10. What controls the next regime

After column scaling, the local finite matrix has the schematic form

\[
\frac1kHA^{-1}
=
\operatorname{diag}(F_1,\ldots,F_J)
+
\frac1k\bigl[S_{m-l}\mathbf1_{l<m}\bigr]
+\text{exponentially small lower part}
+\text{source tails}.
\tag{GD53}
\]

Near \(c=12J+x\), for \(m=J-r\),

\[
J^2F_{J-r}(12J+x)
=
\frac r{24}+\frac x{288}+o(1)
\qquad(r\ \text{fixed}).
\tag{GD54}
\]

Thus the first nontrivial finite-block coupling is governed by

\[
\frac{J^2}{k}.
\tag{GD55}
\]

This points to a natural square-root transition \(J\asymp\sqrt{k}\).
The present cube-root theorem does **not** show that the ladder fails beyond
GD0.  The extra factor \(J\) comes from using the complex-disc bound
\(|B_{lm}|\le(m-l)A_m\) in the unweighted infinity norm.

A sharper pass should:

1. build a weighted triangular norm adapted to the distance \(J-m\);
2. retain the divisor average in a complex neighborhood, rather than the
   coarse factor \(m-l\);
3. prove a uniform inverse with error \(O(J^2\log^Ck/k)\);
4. seek a limiting upper-triangular divisor operator or continued-fraction
   recursion when \(J^2/k\to\alpha\).

The current proof must stop if the complex finite-block Neumann quantity in
GD37 is not \(o(1)\).  Finite computations beyond that point are conjecture
input, not proof of uniform interlacing.

---

## 11. Imported versus new

### Imported from PR #766

* the exact coefficient flag and period normalization;
* the source echelon chart;
* the complete \(q\)-tail and low-domain bounds;
* the Fourier-projection lemma;
* the exact arithmetic cross integral;
* the source Schur identities;
* reflection and real symmetry.

### New in this note

* explicit depth envelopes GD15--GD20;
* the growing deep inverse GD25;
* uniform diagonal and cross estimates GD26--GD32;
* the simultaneous finite-block inverse GD37--GD38;
* the uniform two-by-two data GD39--GD42;
* the growing Rouché, simplicity, interlacing, gap, and residue theorem;
* the fixed-weight growing divisor census for \(Q_1\);
* identification of \(J^2/k\) as the next renormalized coupling scale.

### Not claimed

* optimality of the cube-root regime;
* a theorem at \(J\asymp\sqrt{k}\), \(J=o(k/\log k)\), or \(J/k\to\alpha\);
* a self-adjoint Jacobi realization;
* a zero census away from the endpoint clusters;
* critical-line purity, RH, or GRH.

### Priority review points

1. the exponential-in-\(J\), rather than \(C^{J^2}\), extraction in
   Lemma 3.1;
2. uniformity of the complex-power estimate GD23;
3. the complex finite-block estimate GD37;
4. the Schur correction bound GD44;
5. derivative uniformity in GD42 and the Rouché error GD46;
6. the uniform relative errors in GD11--GD12.
