# L-90303 — The relative Q4 inertia defect is one square versus the radix-four reserve

Claim ID: `L-90303`  
Title: For the exact source-complete relative Q4 Jordan jet, the complete polarized determinant collapses to the deterministic reserve times one centered-current square minus one centered-second-current square  
Status: **PROPOSED COMPLETE EXACT ALGEBRAIC REDUCTION — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-10  
Dependencies: `L-90302`; PR #345 `L-34404`; PR #342 relative Q4 coordinates  
Scope: exact row/finite-state algebra; no sign or asymptotic estimate

## 1. Relative Q4 jet

Use the exact relative Q4 two-channel path of PR #345.  On one aligned source-complete row its first three jets have the form

\[
V=(1,Y),
\qquad
V'=(E,I),
\qquad
V''=(E^2-R,T),
\tag{L-90303.1}
\]

where

```text
R = Delta_4 R     deterministic radix-four log-curvature/reserve;
E                 relative first generalized-prime coordinate;
Y                 relative bare-source coordinate;
I                 true RH-sensitive current innovation;
T                 source second-current coordinate.
```

The scalar curvature is exactly

\[
\boxed{
\operatorname{tr}K
=R+I^2-YT.
}
\tag{L-90303.2}
\]

This is the source-complete augmented relative curvature already used on the Q4 branches.

## 2. Exact determinant collapse

`L-90302` gives for any row jets

\[
\det K
=(Q-YP)(PT-QS)-\frac14(T-YS)^2.
\]

Substitute

\[
P=E,\qquad Q=I,\qquad S=E^2-R.
\]

Define the centered first current

\[
\boxed{D=I-YE}
\tag{L-90303.3}
\]

and the centered second-current expression

\[
\boxed{
C=T-2EI+Y(E^2+R).
}
\tag{L-90303.4}
\]

Then a direct expansion gives

\[
\boxed{
\det K
=R D^2-\frac14 C^2.
}
\tag{L-90303.5}
\]

### Proof

The three Wronskians are

\[
V\wedge V'=I-YE=D,
\]

\[
V\wedge V''=T-Y(E^2-R),
\]

and

\[
V'\wedge V''=ET-I(E^2-R).
\]

Using `I=D+YE`, one checks

\[
[V\wedge V'']-2E[V\wedge V']
=T-2EI+Y(E^2+R)=C.
\]

Substitution in `L-90302.3` and completion of the square gives (L-90303.5).

Equivalently, apply the parameter-independent shear which sends the zeroth jet `(1,Y)` to `(1,0)`.  In those centered coordinates the curvature matrix is

\[
\begin{pmatrix}
R & ED-C/2\\
ED-C/2 & D^2
\end{pmatrix},
\]

whose determinant is immediately `RD^2-(ED-C/2)^2`; replacing the centered second coordinate by its definition yields exactly (L-90303.5).  The Wronskian derivation is coordinate-free and is the preferred proof.

## 3. Exact inertia defect

When the scalar curvature (L-90303.2) is positive, `L-90301` gives

\[
\delta(K)
\le\frac{(-\det K)_+}{\operatorname{tr}K}.
\]

Using (L-90303.5),

\[
\boxed{
\delta(K)
\le
\frac{[C^2/4-RD^2]_+}
     {R+I^2-YT}.
}
\tag{L-90303.6}
\]

Thus the former full polarized PSD theorem is replaced by one scalar **square-versus-reserve** comparison.

Full PSD would ask

\[
|C|\le2\sqrt R\,|D|.
\tag{L-90303.7}
\]

The inertia-tolerant recurrence can allow violations of (L-90303.7), provided their excess

\[
\boxed{
\mathfrak d
=\left[\frac{C^2}{4}-RD^2\right]_+
}
\tag{L-90303.8}
\]

is polynomially payable after division by the already-positive scalar curvature.

## 4. Why this is source-specific

The exact Q4 work already gives different structural information about the ingredients:

```text
R:   deterministic critical moat, Theta(n log n) on balanced cones;
E:   radix-four first-moment innovation, only logarithmic size;
Y:   fixed/explicit bare-source coordinate on the compact relative source;
T:   source second current with a separately derived lower-order prefix law;
I:   the sole RH-sensitive first current.
```

Equation (L-90303.5) keeps these roles intact.  In particular, when `|I|` is very large, both `D` and the positive term `R D^2` grow with the current instead of forcing the negative eigenvalue to grow like `I^2`.  The bad direction is governed by the **mismatch** `C` against the reserve-weighted centered current.

This is substantially more structured than an arbitrary `2 x 2` Hermitian matrix and is the natural next target for the corrected source order.

## 5. Review / mutation tests

A valid continuation must reject any proof which:

1. replaces `T` by the old incorrectly typed Selberg carry from the pre-repair odd-source branch;
2. drops the `Y(E^2+R)` term in `C`;
3. replaces the inertia defect by the stronger sign `det K>=0` without proving it;
4. takes absolute values before forming `D` and `C`;
5. treats the Q4 all-pass factor as shrinking functional-equation hyperbolic pairs (refuted by `R-90301`).

## 6. Proof boundary

Closed exactly:

1. the relative Q4 determinant collapse;
2. the centered-current / centered-second-current coordinates;
3. the exact scalar inertia-defect upper bound.

Open:

1. a source-specific estimate for `mathfrak d` in (L-90303.8);
2. QIDR;
3. RH.