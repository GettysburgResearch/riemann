# L-26702 — Boundary-charge minimax and the Green/dipole bridge

Claim ID: `L-26702`  
Title: The least affine lift has an exact monotone-additive dual and is bounded by the canonical Green slope  
Status: **PROPOSED COMPLETE FINITE CONVEX-DUALITY LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-08`  
Created: 2026-08-08  
Dependencies: `L-26701`; PR #248 `L-24509`; PR #254 adjacent constraint-dipole algebra  
Scope: finite minimax identity and proof-producing interfaces; no asymptotic estimate

## 1. The least boundary charge

Retain the parabolic benchmark \(b_X^{(0)}\), the target
\[
w_X(q)=q^{-1/2}\log(X/q),
\qquad q\in\mathcal Q_X,
\]
and the carry map
\[
(V_Xb)_q=v_q^{(X)}(b).
\]

Define the least uniform downward deformation needed to reach the feasible
carry half-space:
\[
\boxed{
\mathcal C_X
=
\inf\left\{
C\ge0:
\begin{array}{l}
\text{there exists }b\in\mathbb R^{X-1},\\
V_Xb\le w_X,\\
b_m\ge b_X^{(0)}(m)-C\quad(2\le m\le X)
\end{array}
\right\}.
}
\tag{L-26702.1}
\]

The infimum is attained because the programme is finite and has the canonical
Green feasible point described below.

Applying `L-26701` to a minimizer gives a nonnegative oversupported carry vector
and
\[
\boxed{
P_X
\ge
J_X(b_X^{(0)})-\mathcal C_X\log X.
}
\tag{L-26702.2}
\]

This is an actual finite construction at every endpoint. The only cofinal
question is the size of the one scalar \(\mathcal C_X\).

## 2. Exact dual

For a nonnegative vector
\[
y=(y_q)_{q\in\mathcal Q_X},
\]
define its prime-power divisor potential
\[
\boxed{
Y_y(n)=\sum_{\substack{q\in\mathcal Q_X\\q\mid n}}y_q,
\qquad Y_y(1)=0.
}
\tag{L-26702.3}
\]

The transpose of the carry map is
\[
\boxed{
(V_X^Ty)_m=Y_y(m)-Y_y(m-1),
\qquad 2\le m\le X.
}
\tag{L-26702.4}
\]

Finite linear-programming duality gives
\[
\boxed{
\mathcal C_X
=
\max_y
\sum_{q\in\mathcal Q_X}y_q
\left[v_q^{(X)}(b_X^{(0)})-w_X(q)\right],
}
\tag{L-26702.5}
\]
where the maximum is over
\[
\boxed{
y_q\ge0,\qquad
Y_y(1)\le Y_y(2)\le\cdots\le Y_y(X),
\qquad
Y_y(X)\le1.
}
\tag{L-26702.6}
\]

### Proof

Introduce nonnegative dual variables \(y_q\) for
\[
V_Xb-w_X\le0
\]
and \(z_m\) for
\[
b_X^{(0)}(m)-b_m-C\le0.
\]
The Lagrangian is
\[
C+y^T(V_Xb-w_X)+z^T(b_X^{(0)}-b-C\mathbf1).
\]
Its infimum over the free vector \(b\) is finite exactly when
\[
z=V_X^Ty.
\]
Its infimum over \(C\ge0\) is finite exactly when
\[
\mathbf1^Tz\le1.
\]
Now
\[
z_m=Y_y(m)-Y_y(m-1),
\]
so \(z\ge0\) is precisely monotonicity of \(Y_y\), while
\[
\mathbf1^Tz=Y_y(X).
\]
The remaining dual objective is the right side of (L-26702.5). Strong duality
applies because the primal is feasible and bounded below.

Thus every obstruction to a small affine lift is witnessed by a
**nonnegative monotone additive divisor potential**, not by an arbitrary
vector.

## 3. The logarithmic ray is the RH firewall

Take
\[
y_q=\frac{\Lambda(q)}{\log X}.
\]
Then
\[
Y_y(n)
=
\frac1{\log X}\sum_{q\mid n}\Lambda(q)
=
\frac{\log n}{\log X}.
\]
This is feasible in (L-26702.6) and has \(Y_y(X)=1\). Therefore
\[
\boxed{
\mathcal C_X
\ge
\left[
\frac{
J_X(b_X^{(0)})-P_X
}{\log X}
\right]_+.
}
\tag{L-26702.7}
\]

This mutation is load bearing. A claimed proof of a small boundary charge cannot
delete the logarithmic/von-Mangoldt ray: that ray is the prime-ramp discrepancy
itself.

Equation (L-26702.5) nevertheless narrows the search. One need not control all
dual vectors, only monotone additive prime-power potentials normalized at the
endpoint.

## 4. Canonical Green upper bound

Let
\[
r_X=V_Xb_X^{(0)}-w_X.
\]
Use the endpoint-projected Dirichlet Gram \(G_X\) of PR #248 and let
\[
T_X=G_X^{-1}r_X.
\]
Write
\[
F_X(j)
=
\sum_{q\in\mathcal Q_X}T_X(q)f_q(j),
\qquad
F_X(0)=F_X(X)=0,
\]
and define the canonical signed Green solution
\[
\boxed{
b_X^G(m)
=
b_X^{(0)}(m)+F_X(m-1)-F_X(m).
}
\tag{L-26702.8}
\]

The exact Gram identity gives
\[
V_Xb_X^G=w_X.
\tag{L-26702.9}
\]

Its affine boundary charge is
\[
\boxed{
C_X^G
=
\max_{2\le m\le X}
\bigl[F_X(m)-F_X(m-1)\bigr]_+.
}
\tag{L-26702.10}
\]

Therefore
\[
\boxed{\mathcal C_X\le C_X^G.}
\tag{L-26702.11}
\]

The Green energy is
\[
\mathcal G_X
=
r_X^TG_X^{-1}r_X
=
\sum_{j=0}^{X-1}
\bigl[F_X(j+1)-F_X(j)\bigr]^2.
\]
Consequently
\[
\boxed{
\mathcal C_X
\le C_X^G
\le\sqrt{\mathcal G_X}.
}
\tag{L-26702.12}
\]

The new scalar is therefore weaker than the full Green-energy theorem: it asks
only for the largest upward Green edge, not the sum of all squared edges.

## 5. Dipole-assisted deformation

Let \(H=(H_j)\) be any adjacent-flow potential and put
\[
b_X^H(m)
=
b_X^G(m)+H_{m-1}-H_m.
\tag{L-26702.13}
\]

Suppose
\[
V_Xb_X^H\le w_X.
\tag{L-26702.14}
\]

Define
\[
C_X(H)
=
\max_m
\left[
b_X^{(0)}(m)-b_X^H(m)
\right]_+.
\tag{L-26702.15}
\]

Then
\[
\mathcal C_X\le C_X(H),
\tag{L-26702.16}
\]
and the affine oversupport construction of `L-26701` closes every remaining
negative coordinate.

This is the exact interface to the constraint-dipole flow of PR #254:

```text
canonical Green solve
-> signed adjacent/divisor transport using actual slack
-> no requirement of pointwise positivity yet
-> one scalar maximum deficit
-> affine prime-boundary lift
-> nonnegative finite certificate.
```

The dipole flow no longer has to finish with \(b_X^H\ge0\), nor does it need a
separate objective-cost estimate. It only needs
\[
C_X(H)=X^{o(1)}.
\]
The boundary lift then pays the entire remaining defect at cost
\(C_X(H)\log X\).

## 6. Relation to the other carry coordinates

- **DCRS/Greedy Slack** controls the aggregate objective debt.
- **GET** controls the full squared Green gradient.
- **Constraint-dipole transport** searches for a feasible physical deformation.
- **Affine boundary charge** controls only the largest unresolved downward
  displacement from the sharp seed.

The exact implications supplied here are
\[
\mathrm{GET}\Longrightarrow
C_X^G\text{ small}
\Longrightarrow
\mathcal C_X\text{ small}
\Longrightarrow
\text{sharp prime ramp}.
\]

No converse is asserted. The affine charge is a new, strictly local proof
target and an actual positivity-preserving completion mechanism.

## 7. Proof boundary

Closed exactly:

1. the minimax definition;
2. the monotone-additive dual;
3. the logarithmic-ray mutation;
4. the canonical Green upper bound;
5. the dipole-assisted completion interface.

Open:

1. the cofinal subpower estimate
   \[
   \mathcal C_X=X^{o(1)};
   \]
2. an explicit symbolic dipole flow achieving that estimate;
3. RH.
