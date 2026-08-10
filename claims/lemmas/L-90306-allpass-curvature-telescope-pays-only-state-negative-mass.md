# L-90306 — An all-pass block telescope pays only the negative curvature mass of its state

Claim ID: `L-90306`  
Title: Differentiating the exact two-frequency Euler–Blaschke block identity in the imaginary Jordan direction gives a coefficient-one curvature recurrence; positivity of the state is unnecessary, and only its negative spectral mass enters as forcing  
Status: **PROPOSED COMPLETE EXACT HILBERT/STATE-SPACE LEMMA — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-10  
Dependencies: PR #339 `L-33804`; `L-90301`, `L-90305`  
Scope: exact all-pass/delayed-state orientation and inertia-tolerant upper law; arithmetic identification of the state with the corrected zero-bare Q4 block is a separate interface

## 1. Imaginary Jordan curvature of a physical block

Let `I` be one logarithmic physical block and let

\[
\tau\longmapsto f_\tau
\]

be a twice differentiable analytic path in the corresponding physical Hilbert space.  Define

\[
\boxed{
\mathfrak C_I(f)
=\frac12\frac{d^2}{dy^2}
  \|f_{iy}\|_I^2\bigg|_{y=0}.
}
\tag{L-90306.1}
\]

Writing dots for derivatives in `tau` at zero,

\[
\boxed{
\mathfrak C_I(f)
=\|\dot f\|_I^2
 -\operatorname{Re}\langle f_0,\ddot f\rangle_I.
}
\tag{L-90306.2}
\]

Indeed

\[
f_{iy}=f_0+iy\dot f-rac{y^2}{2}\ddot f+O(y^3),
\]

and direct expansion gives (L-90306.2).

This is the physical-block version of the Jordan curvature used throughout the Q2/Q4 source ledger.

## 2. Exact polarized all-pass identity

Retain the notation of PR #339 `L-33804`:

\[
\phi(z)=\frac{a-e^{-Lz}}{1-ae^{-Lz}},
\qquad
R(z)=\frac{\sqrt{1-a^2}}{1-ae^{-Lz}},
\qquad 0<a<1.
\tag{L-90306.3}
\]

For every physical input `h`, that theorem proves in the complete independent-frequency normal orientation

\[
\boxed{
\|h\|_I^2-\|\phi(D)h\|_I^2
=\|R(D)h\|_I^2-\|R(D)h\|_{I-L}^2.
}
\tag{L-90306.4}
\]

The operators `phi(D)` and `R(D)` are independent of the Jordan parameter.

Apply (L-90306.4) to `h=f_(iy)` and differentiate twice at `y=0`.  Since the equality holds for every sufficiently small real `y`, one obtains exactly

\[
\boxed{
\mathfrak C_I(f)-\mathfrak C_I(\phi f)
=\mathfrak C_I(Rf)-\mathfrak C_{I-L}(Rf).
}
\tag{L-90306.5]

(The closing bracket in the tag is typographical only.)

Equivalently,

\[
\boxed{
\mathfrak C_I(\phi f)+\mathfrak C_I(Rf)
=\mathfrak C_I(f)+\mathfrak C_{I-L}(Rf).
}
\tag{L-90306.6}

This is the exact dissipative orientation which is invisible in a diagonal `|phi|=1` statement: the current-block state occurs with a minus sign and the predecessor state with a plus sign.

## 3. The state need not have positive curvature

Suppose the state path has a source-complete finite realization

\[
R(D)f_\tau=W V_\tau,
\tag{L-90306.7}
\]

where `V_tau` is an `r`-channel path and `W` is parameter-independent with

\[
W^*W\preceq qI.
\tag{L-90306.8}
\]

Let

\[
K_{V,I}
=\langle\dot V,\dot V\rangle_I
 -\frac12\left(
   \langle V_0,\ddot V\rangle_I
  +\langle\ddot V,V_0\rangle_I
 \right)
\tag{L-90306.9}
\]

be the channel curvature matrix and put

\[
\delta_I(V)=\operatorname{tr}(K_{V,I})_-.
\tag{L-90306.10}
\]

The lower half of `L-90301.7` gives

\[
\boxed{
\mathfrak C_I(Rf)
=\operatorname{tr}(W K_{V,I}W^*)
\ge-q\,\delta_I(V).
}
\tag{L-90306.11}
\]

Insert this in (L-90306.5):

\[
\boxed{
\mathfrak C_I(\phi f)
\le
\mathfrak C_I(f)
+\mathfrak C_{I-L}(Rf)
+q\,\delta_I(V).
}
\tag{L-90306.12}
\]

Thus full polarized positivity of the state is not required.  The exact all-pass telescope pays only the trace mass of its bad spectral directions.

## 4. Q=4 coefficient-one normalization

For `Q=4`, PR #339 has

\[
a=\frac12,
\qquad L=\log4,
\qquad
E_4(1/2+z)=2\phi(z).
\]

Curvature is quadratic under multiplication by the constant two, so (L-90306.12) becomes

\[
\boxed{
\frac14\mathfrak C_I(E_4 f)
\le
\mathfrak C_I(f)
+\mathfrak C_{I-\log4}(Rf)
+q\,\delta_I(V).
}
\tag{L-90306.13}
\]

The coefficient of the incoming principal curvature is exactly one.  This is the curvature counterpart of the square-root-normalized row recurrence

\[
U(4n)=\frac12U(n)+\text{innovation}/(2\sqrt n).
\]

No strict contraction of the principal zeta mode is asserted or needed.

## 5. Finite cascades

Suppose `m` parameter-independent all-pass stages are composed, with states `x_j`, delays `L_j`, and normalized gains `g_j`.  Apply (L-90306.6) at each stage and sum.  Every internal signal curvature cancels once with each sign.  The result is an exact conservation law

\[
\boxed{
\mathfrak C_I(\text{final output})
+\sum_{j=1}^m\mathfrak C_I(x_j)
=
\mathfrak C_I(\text{initial input})
+\sum_{j=1}^m\mathfrak C_{I-L_j}(x_j),
}
\tag{L-90306.14}
\]

in the corresponding normalized units.  If `x_j=W_jV_j` and `W_j^*W_j<=q_jI`, then

\[
\boxed{
\mathfrak C_I(\text{final output})
\le
\mathfrak C_I(\text{initial input})
+\sum_{j=1}^m\mathfrak C_{I-L_j}(x_j)
+\sum_{j=1}^m q_j\delta_I(V_j).
}
\tag{L-90306.15}
\]

This applies in particular to the exact two-stage Q2 realization of the Q4 colligation once its source paths are placed in one declared block metric.

## 6. Combination with the zero-bare Q4 defect theorem

`L-90304` proves on every fixed balanced cone that the corrected zero-bare relative Q4 state has rowwise negative mass

\[
\delta_{n,j}=O_\eta(n/\log n),
\]

and `L-90305` proves that positive carry-position integration, independent-frequency direct integration, finite Toeplitz compression and contractive synthesis preserve the critically normalized bound

\[
\delta_I=O_\eta(1/\log n).
\tag{L-90306.16}
\]

Consequently, once the exact Q2/Q4 state dictionary identifies each `V_j` in (L-90306.15) with the corresponding zero-bare corrected block, the total inertia forcing is lower order and the right side has the desired form

\[
\boxed{
\text{principal input at }I
+\text{finitely many predecessor states}
+O_\eta(1/\log n).
}
\tag{L-90306.17}
\]

The all-pass/dissipative **sign** is therefore closed.  The remaining production interface is source typing: one must write the corrected Q2/Q4 principal and state paths as the exact `f,x_j,V_j` appearing in this one metric, including the finite collars and strictly delayed derivative gauges.

## 7. What this rules out

A valid continuation may not:

1. replace (L-90306.4) by the diagonal identity `|phi|=1`;
2. drop the predecessor state in (L-90306.6);
3. demand `K_V>=0` after (L-90306.11);
4. estimate the current and predecessor state separately before the exact telescope;
5. use the Q4 all-pass factor as a source-blind contraction on functional-equation hyperbolic pairs (`R-90301`).

## 8. Proof boundary

Closed exactly here:

1. imaginary-Jordan differentiation of the independent-frequency all-pass block identity;
2. exact current/predecessor dissipative orientation;
3. inertia-tolerant upper recurrence;
4. coefficient-one Q4 normalization;
5. finite-cascade conservation and defect forcing;
6. compatibility with the `O(1/log n)` normalized defect from `L-90304/L-90305`.

Still open:

1. the explicit corrected Q2/Q4 source-to-state dictionary in one block Hilbert metric;
2. finite-collar and derivative-gauge insertion in that dictionary;
3. the resulting closed global recurrence;
4. RH.
