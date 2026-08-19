# T-99320 — Target-aligned rank-one common-parent component-row RH candidate

Claim ID: `T-99320`  
Status: **PROPOSED COMPLETE UNCONDITIONAL PROOF CANDIDATE — HOSTILE REVIEW REQUIRED**  
Created: 2026-08-19  
Base: PR #641 at `19cd3939a54ccea73b055b3952b5dd7ed638c4fb`  
RH status: **not established by publication**

## 1. Single new mechanism

Every component row has the exact factorization

\[
Q_Y(j)=\int_1^Y T(Y/t)\eta_j(t)\frac{dt}{t},
\qquad
\eta_j(t)>0.
\]

The source scalar is exactly the same SHARP target used by compact Hall and the
causal target tree. At fixed \(t\), every source colour has the same normalized
row vector \((\eta_j(t))_j\).

Consequently:

```text
target Hall automatically transports every component row;
one target random key automatically partitions every row child;
every causal parent-minus-child row is positive pointwise;
no normalized-row determinant or coordinatewise coupling is needed.
```

## 2. Complete chain

Freeze the compact target Hall and target-source registry at their exact PR
#620/#632/#636 scopes.

`L-99321` lifts that target source to every physical component row.
`L-99322` forms the actual row identity and keeps all finite/continuum, knot,
boundary and anchored calibration data signed. PR #641's fixed-row bound gives

\[
c_X(j)=D_X(j)+\mathfrak E_X(j),
\qquad
D_X(j)\ge0,
\qquad
\mathfrak E_X(j)=O_j(1).
\tag{T-99320.1}
\]

For fixed \(j\), write

\[
H_j(z)=\sum_{m\ge j}a_{j,m}m^{-z}
=C_j\zeta(z)+P_j(z).
\]

Finite Fubini gives initially for \(\Re s>1/2\)

\[
\boxed{
\int_1^\infty c_X(j)X^{-s-1}\,dX
=
\frac{C_j}{s^2}
+
\frac{P_j(s+1/2)}
{s^2\zeta(s+1/2)}.
}
\tag{T-99320.2}
\]

The bounded calibration transform is holomorphic in \(\Re s>0\). Hence the
same reciprocal-zeta pole occurs in the Mellin transform of the nonnegative
surrogate \(D_X(j)\).

For fixed \(z\) with \(0<\Re z<1\),

\[
\boxed{
P_j(z)
=
-\frac{z(z+1)}{1-z}j^{-z-1}
+o_z(j^{-\Re z-1}).
}
\tag{T-99320.3}
\]

Every hypothetical off-line zero therefore survives in some sufficiently
large fixed row. Landau's theorem applied to \(D_X(j)\ge0\) excludes the pole
at \(s=\rho-\frac12\); the functional equation excludes the reflected
half-plane.

This gives the proposed conclusion

\[
\boxed{\mathrm{RH}.}
\]

## 3. Interface audit

The candidate no longer uses:

```text
positive Volterra anchors;
positive activation-knot atoms;
normalized component-row Hall profiles;
endpoint monotonicity as a child-coupling theorem;
literal score or 4sqrt(X);
ordinary/radix-four capacity;
safe-point thinning;
prime-square moat.
```

The first and only imported arithmetic producer is:

> the source-faithful compact target Hall plus exact target-source random-key
> tree on the frozen root registry.

Every component-row interface after that producer is proved by
`L-99320`–`L-99322`.

## 4. Scientific boundary

The new rank-one theorem and fixed-row analytic consumer are proposed complete
mathematics. Because the conclusion would prove RH, the frozen target source
registry and every Hall/source coefficient require independent reconstruction.

```text
target-aligned positive row atom              PROVED EXACT
compact Hall lift to all rows                 PROPOSED COMPLETE
causal common-parent lift                     PROPOSED COMPLETE
actual row identity modulo bounded defect     PROPOSED COMPLETE
fixed-row pole preservation                   PROPOSED COMPLETE
accepted proof of RH                          NO
Riemann Hypothesis                            UNPROVEN PENDING REVIEW
```
