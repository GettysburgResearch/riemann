# L-92900 — Positive source ownership and signed observation correction form two separate exact ledgers

Claim ID: `L-92900`
Status: **PROVED EXACT ABSTRACT COMPOSITION THEOREM**
Created: 2026-08-15
Primary purpose: repair the source/observation type conflation isolated by `R-92900`
RH status: **unproved**

## 1. Typed data

Let \(\mathscr S\) be a positive labelled source cone. A packet in
\(\mathscr S\) carries source ownership, target, benchmark, literal score,
component row, ordinary responses, radix-four responses and descendant boundary
coordinates. Let

\[
\mathcal A:\mathscr S\longrightarrow V
\]

be the positive linear observation map into the finite native-capacity space
\(V\).

A root-global finite/continuum comparison is not required to lie in
\(\mathscr S\). It is allowed to be a signed vector in \(V\).

## 2. Positive source ledger

Assume the exact source operations give

\[
\boxed{
P_X^{\rm src}
=
C_X^{\rm src}
+\sum_b\beta_bU_bP_b^{\rm src}
+U_X^{\rm src}.
}
\tag{L-92900.1}
\]

All terms are positive and source-disjoint, with

\[
\beta_b\ge0,
\qquad
\sum_b\beta_b<\frac18,
\tag{L-92900.2}
\]

and \(U_X^{\rm src}\) is literal unused source from positive restriction,
omission or thinning.

Applying \(\mathcal A\) gives the ideal physical identity

\[
\mathcal A(P_X^{\rm src})
=
\mathcal A(C_X^{\rm src})
+\sum_b\beta_bU_b\mathcal A(P_b^{\rm src})
+u_X,
\qquad
u_X:=\mathcal A(U_X^{\rm src})\ge0.
\tag{L-92900.3}
\]

Every original source occurrence has exactly one owner in (L-92900.1).

## 3. Signed observation ledger

Let \(e_X\in V\) be the signed change in physical use caused by all
decomposition-blind finite realization operations after the positive source
sum, including the finite/continuum comparison and any signed response
correction. Thus the actual current use is

\[
\mathcal A(C_X^{\rm src})+e_X.
\tag{L-92900.4}
\]

The datum \(e_X\) has one declared **correction owner**, but it is not asserted
to be source-positive.

Assume the explicit all-column estimates prove

\[
\boxed{
e_X(q)\le u_X(q)
\qquad(q\ge2).
}
\tag{L-92900.5}
\]

The stronger sufficient condition \(|e_X(q)|\le u_X(q)\) is often what the
directed estimates establish.

Define

\[
\boxed{
r_X=u_X-e_X.
}
\tag{L-92900.6}
\]

Then (L-92900.5) gives \(r_X\ge0\), and substituting
(L-92900.4)--(L-92900.6) into (L-92900.3) yields the exact realized capacity
identity

\[
\boxed{
\mathcal A(P_X^{\rm src})
=
\bigl[\mathcal A(C_X^{\rm src})+e_X\bigr]
+r_X
+\sum_b\beta_bU_b\mathcal A(P_b^{\rm src}).
}
\tag{L-92900.7}
\]

The equality and the positivity of \(r_X\) are proved by distinct facts:

```text
equality:     linear source identity plus the declared signed correction;
positivity:   explicit native-capacity domination e_X <= u_X.
```

No signed correction is relabelled as unused positive source.

## 4. Native-detail specialization

Take \(\mathcal A=\Xi\) and
\(\mathcal A(P_X^{\rm src})=\Omega_X\). Then

\[
\boxed{
\Omega_X
=
\Xi(d_X^{\rm cur})
+r_X
+\sum_b\beta_bU_b\Omega(P_b),
\qquad
r_X\ge0.
}
\tag{L-92900.8}
\]

If \(d_b\) is feasible for \(P_b\), then

\[
d_X=d_X^{\rm cur}+\sum_b\beta_bU_bd_b
\]

satisfies

\[
\Xi(d_X)\le\Omega_X.
\tag{L-92900.9}
\]

Positive radix-four inversion gives the simultaneous ordinary inequality.

## 5. Direct \(Y_4\) cost

Let \(Y_4\ge0\) be the exact native dual. If
\(|e_X|\le \bar e_X\) and \(u_X\le\bar u_X\), then

\[
\begin{aligned}
\langle Y_4,r_X\rangle
&=\langle Y_4,u_X-e_X\rangle\\
&\le
\langle Y_4,\bar u_X\rangle
+\langle Y_4,\bar e_X\rangle.
\end{aligned}
\tag{L-92900.10}
\]

This is the correct place to use the sparse \(Y_4\) estimates. A target-mass
bound for positive source may pay \(\bar u_X\), but a signed comparison must be
paid through \(\bar e_X\), not through source mass.

## 6. Source ownership versus correction ownership

The ledgers answer different questions:

```text
source ledger:
    Which positive arithmetic occurrence is current, child, stopped or unused?

observation ledger:
    How far does the finite physical realization move each native column?
```

A correction may be current-owned without being positive source. This does not
duplicate arithmetic provenance and does not make it eligible for a
positive-source mass theorem.

## 7. Boundary

```text
positive source telescope                         exact
signed correction ownership                      exact
native identity after correction                  exact
root slack positivity                             from explicit capacity domination
signed defect as positive source                  forbidden
Y4 cost of signed defect                          direct absolute pairing
recursive or terminal child insertion             both compatible
Riemann Hypothesis                                unproved
```
