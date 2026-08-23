# L-105218 — Critical-node Schur complementation splits residue and boundary inertia exactly

Claim ID: `L-105218`  
Status: **PROVED EXACT FINITE-PACKET INERTIA THEOREM**  
Created: 2026-08-23  
Depends on: `L-105214`, `L-105217`  
RH status: **not assumed**

Let `F`, `Omega`, the real simple critical points

\[
c_1,\ldots,c_R,
\]

and the entire-window decomposition be as in `L-105214`. Assume for the moment
that every real critical residue

\[
\rho_i={F(c_i)\over F''(c_i)}
\]

is nonzero. Let

\[
x_1,\ldots,x_N
\]

be additional distinct real nodes, none critical. Put

\[
h_i=F''(c_i),
\qquad
D=\operatorname{diag}(\rho_1,\ldots,\rho_R),
\qquad
H=\operatorname{diag}(h_1,\ldots,h_R),
\tag{L-105218.1}
\]

and define the feature matrix

\[
Q_{\alpha i}
={F'(x_\alpha)\over x_\alpha-c_i}.
\tag{L-105218.2}

Let

\[
R_{\alpha\beta}
=\mathscr R_{F,\Omega}(x_\alpha,x_\beta)
\]

be the boundary-remainder matrix.

## 1. Exact block matrix

Order the packet with the critical nodes first and the additional nodes
second. Since the boundary remainder contains the factor `F'(x)F'(y)`, it
vanishes on every critical-point row and column. Since the critical residue
features interpolate diagonally, `L-105214.5` gives

\[
\boxed{
\mathbb B
=
\begin{pmatrix}
-HDH&-HDQ^T\\
-QDH&R-QDQ^T
\end{pmatrix}.
}
\tag{L-105218.3
}

No approximation is used.

## 2. The exact Schur complement

The critical block is invertible and

\[
(-HDH)^{-1}
=-H^{-1}D^{-1}H^{-1}.
\]

Its Schur complement in (L-105218.3) is

\[
\boxed{
(R-QDQ^T)
-(-QDH)(-HDH)^{-1}(-HDQ^T)
=R.
}
\tag{L-105218.4
}

Equivalently, one explicit block-triangular congruence sends

\[
\boxed{
\mathbb B
\sim
(-HDH)\oplus R.
}
\tag{L-105218.5
}

Thus the boundary and residue defects are not merely separately visible; they
are exact complementary inertia summands.

## 3. Additive negative index

Sylvester's law of inertia gives

\[
\boxed{
\operatorname{ind}_-(\mathbb B)
=
\#\{i:\rho_i>0\}
+
\operatorname{ind}_-(R).
}
\tag{L-105218.6
}

Similarly,

\[
\operatorname{ind}_+(\mathbb B)
=
\#\{i:\rho_i<0\}
+
\operatorname{ind}_+(R).
\tag{L-105218.7}

Zero residues give zero critical pivots. They may be handled by deleting the
corresponding zero row/column after a confluent common-zero ledger, or by a
regular perturbation. They do not create a hidden negative square.

## 4. Exact meaning of the last-defect alternatives

At any finite packet containing all real critical points in the window,

```text
positive real critical residues   contribute exactly their count to ind_-;
boundary Cauchy-Loewner remainder contributes its own negative index;
there is no cancellation between the two contributions.
```

In particular:

- a positive residue cannot be repaired by a positive boundary reserve;
- a negative boundary square cannot be repaired by highly coherent negative
  residues;
- global first/second residue moments are not the natural inertia coordinate.

This algebraically validates the sharp two-gate shape of `T-105220`.

## 5. Nested windows

Combine (L-105218.6) with `L-105217`. When a window is enlarged across one
real nonpositive residue, a positive rank-one feature moves from the boundary
block into the explicit residue block and the total negative index is
unchanged. Crossing a positive residue transfers one negative pivot in the
same way. Crossing nonreal critical points requires the conjugate rank-two
ledger.

Thus the entire reverse–Rolle transport can be viewed as exact migration of
negative squares between the two complementary blocks.

## 6. Scope

The theorem is finite-packet linear algebra. It does not prove positivity of
`R`, the sign of the residues, absence of nonreal critical points, or passage
to the complete Xi exhaustion. Those are precisely the two open sign gates
and the stated convergence requirements of `T-105220`.