# L-106003 — Function-field mirror of the completed family and squareclass collision geometry

Claim ID: `L-106003`  
Programme aliases: `LFAM2.COMPLETED_FAMILY_MIRROR`, `LFAM2.SQUARECLASS_COLLISION_GEOMETRY`  
Status: **PROVED EXACT FINITE-FIELD/FUNCTION-FIELD DICTIONARY**  
Created: 2026-08-24  
Depends on: `L-106000--L-106002`  
Programme issue: #737  
RH status: **not assumed**

This theorem ports the exact family algebra to `A=F_q[T]`. It deliberately
separates the finite identity from any use of geometric RH or monodromy.

## 1. Polynomial Möbius and Dirichlet characters

Let `q` be odd and put

\[
A=\mathbf F_q[T].
\]

For monic `f`, let `mu_A(f)` be the polynomial Möbius function. Let
`\mathfrak l` be a monic irreducible polynomial of degree `d`, with norm

\[
|\mathfrak l|=q^d.
\]

A Dirichlet character modulo `\mathfrak l` is a character of

\[
(A/\mathfrak l)^*,
\]

extended by zero to nonunits.

For a formal variable `u`,

\[
\boxed{
\sum_{f\ {\rm monic}}
\mu_A(f)\chi(f)u^{\deg f}
=
{1\over L(u,\chi)}.
}
\tag{L-106003.1}
\]

This is the exact polynomial analogue of the reciprocal-`L` source.

## 2. Ramified completion

For the principal character,

\[
L(u,\chi_0)
=
Z_A(u)(1-u^d),
\qquad
Z_A(u)={1\over1-qu}.
\tag{L-106003.2}
\]

Hence the common ramified completion gives

\[
\boxed{
{1-u^d\over L(u,\chi_0)}
=
{1\over Z_A(u)}.
}
\tag{L-106003.3}
\]

At coefficient level, if

\[
b_{\mathfrak l}(f)
=
\mu_A(f)\mathbf1_{\mathfrak l\nmid f},
\]

then

\[
c_{\mathfrak l}(f)
=
b_{\mathfrak l}(f)
-
\mathbf1_{\mathfrak l\mid f}
b_{\mathfrak l}(f/\mathfrak l)
\]

satisfies

\[
\boxed{c_{\mathfrak l}(f)=\mu_A(f).}
\tag{L-106003.4}
\]

The proof is the same three-case valuation split as in `L-106000`.

A marked-prime analogue of the repository's distinguished `67` may be included
by choosing one fixed monic irreducible `\mathfrak p_*` and inserting

\[
1-\chi(\mathfrak p_*)u^{\deg\mathfrak p_*}.
\tag{L-106003.5}
\]

No specific degree or norm is declared canonical merely to imitate the integer
label `67`.

## 3. Exact character moment

Let `k_{\mathfrak l}=A/\mathfrak l`, a finite field of cardinality `q^d`.
For a finite coefficient packet `a(f)` supported on units,

\[
F_\chi=\sum_f a(f)\chi(f).
\]

Character orthogonality gives

\[
\boxed{
{1\over q^d-1}
\sum_{\chi\;(\mathrm{mod}\ \mathfrak l)}
|F_\chi|^2
=
\sum_{\substack{f\equiv g\;(\mathrm{mod}\ \mathfrak l)\\
                 \mathfrak l\nmid fg}}
a(f)\overline{a(g)}.
}
\tag{L-106003.6}
\]

The two-scale ramified completion is again one positive `2 x 2` moment form.

## 4. Pair-owner squareclass collision

Let

\[
f=P c^2,
\qquad
g=Qd^2,
\]

with `P,Q,c,d` nonzero modulo `\mathfrak l`. In the residue field,

\[
P c^2=Qd^2.
\tag{L-106003.7}
\]

Put `u=QP^{-1}`.

- If `u` is a nonsquare in `k_{\mathfrak l}`, there is no collision.
- If `u` is a square, choose `tau^2=u`; because the characteristic is odd,

\[
\boxed{
P c^2=Qd^2
\iff
c=\tau d
\quad\text{or}\quad
c=-\tau d.
}
\tag{L-106003.8}
\]

Thus the number-field collision-line reduction is literally the same finite
algebra over `F_q[T]`.

## 5. Exact finite-field phase mechanism

Every multiplicative character satisfies

\[
\chi(Pc^2)=\chi(P)\chi^2(c).
\tag{L-106003.9}
\]

All but the principal and quadratic characters retain the square core.
Combining with any nontrivial additive character of
`k_{\mathfrak l}` gives the Gauss norm

\[
\left|
\sum_{c\in k_{\mathfrak l}^*}
\chi^2(c)\psi(ac)
\right|
=
q^{d/2}
\tag{L-106003.10}
\]

whenever `chi^2` is nontrivial.

On a complete collision line, a nonresonant additive phase sums to `-1`
exactly, while a resonant line contributes `q^d-1`.

## 6. What geometric input would add

Equations (L-106003.1)--(L-106003.10) are finite algebra. They do not use
Deligne, purity, monodromy or equidistribution.

The programme-specific geometric theorem would have to control the actual
incomplete Möbius/Vaughan-weighted line sums, uniformly in conductor degree and
owner strata. A satisfactory result should identify:

```text
the trace sheaf or Frobenius representation;
the exact exceptional/resonant strata;
the weight and conductor of the sheaf;
memberwise versus family-averaged scope;
the number-field exponential-sum statement suggested by the proof.
```

Call this open theorem `FFHCLM106003`. Its proof would be a genuine discovery
mechanism for the number-field programme, but it would not by itself imply RH
over the integers.
