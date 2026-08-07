# L-26203 — The parabolic Green sharpness problem is one paired obstacle debt

Claim ID: `L-26203`  
Title: Canonical Green equality, positive-cone clipping, and the signed constraint dipole reduce carry sharpness to one source-specific contact debt  
Status: **PROPOSED — EXACT REDUCTION AND CERTIFICATE INTERFACE PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Issue: #260  
Dependencies: PR #240 `L-23820/L-23821`; `L-24502`, `L-24509`, `L-24510`, `L-25301`, `L-26201`, `L-26202`  
Scope: exact finite reduction; the cofinal debt estimate remains proposed

## 1. The parabolic reference point

For every integer `X>=2`, let

\[
\boxed{
b_m^{(0)}
=
2\sqrt m\left[
 \log\frac Xm
 -2\left(1-\sqrt{\frac mX}\right)
\right]
\qquad(2\le m\le X).
}
\tag{L-26203.1}
\]

The bracket is nonnegative, so `b^(0)>=0`. Put

\[
J_X(b)
=\sum_{m=2}^{X}b_m\log\frac m{m-1}.
\]

The elementary seed calculation of `L-24502` gives

\[
\boxed{
J_X(b^{(0)})
\ge4\sqrt X-C_0\log(2X)
}
\tag{L-26203.2}
\]

for one absolute constant.

For prime powers `q<=X`, put

\[
w_X(q)=q^{-1/2}\log(X/q)
\]

and

\[
r_X(q)=v_q(b^{(0)})-w_X(q).
\tag{L-26203.3}
\]

The signed residual has macroscopic positive and negative von-Mangoldt masses;
they may not be estimated separately.

## 2. Canonical exact Green equality

Use the endpoint-projected profiles `f_q` and Gram `G_X` of `L-24509`.
Solve

\[
G_XT_X=r_X
\tag{L-26203.4}
\]

and put

\[
F_X(j)=\sum_{q\in\mathcal Q_X}T_X(q)f_q(j),
\]

\[
\boxed{
b_X^\star(m)
=b_m^{(0)}+F_X(m-1)-F_X(m).
}
\tag{L-26203.5}
\]

Then

\[
\boxed{
v_q(b_X^\star)=w_X(q)
\qquad(q\in\mathcal Q_X).
}
\tag{L-26203.6}
\]

The vector `b_X^star` is completely source bound: it depends only on the
finite prime-power manifest, floors, logarithms, square roots, and one positive
definite rational Gram solve after the transcendental target values have been
enclosed.

It need not be nonnegative.

## 3. Green clipping and the paired debt

Define

\[
a_X(m)=(-b_X^\star(m))_+,
\qquad
b_X^\circ=(b_X^\star)_+,
\tag{L-26203.7}
\]

and

\[
\varepsilon_X(q)
=v_q(b_X^\circ)-w_X(q)
=v_q(a_X).
\tag{L-26203.8}
\]

Let

\[
D_X^+
=\sum_q\Lambda(q)(\varepsilon_X(q))_+,
\qquad
D_X^-
=\sum_q\Lambda(q)(-\varepsilon_X(q))_+.
\tag{L-26203.9}
\]

The exact clipped lower certificate is

\[
\boxed{
\mathcal L_X^{\rm GS}
=J_X(b_X^\circ)-D_X^+.
}
\tag{L-26203.10}
\]

By `L-26202`,

\[
\boxed{
\mathcal L_X^{\rm GS}
\le
\mathcal P(X)
:=
\sum_{q=p^a\le X}
 \frac{\Lambda(q)}{\sqrt q}\log\frac Xq,
}
\tag{L-26203.11}
\]

and

\[
\boxed{
\mathcal P(X)-\mathcal L_X^{\rm GS}=D_X^-.
}
\tag{L-26203.12}
\]

The Green correction itself changes the objective by

\[
J_X(b_X^\star)-J_X(b_X^{(0)})
=
\mathcal P(X)-J_X(b_X^{(0)}).
\tag{L-26203.13}
\]

Combining (L-26203.10)--(L-26203.13) gives the exact sharpness deficit

\[
\boxed{
\mathfrak C_X
:=
J_X(b_X^{(0)})-\mathcal L_X^{\rm GS}
=
\lambda^{\!T}r_X+D_X^-,
}
\tag{L-26203.14}
\]

where `lambda_q=Lambda(q)`.

Equation (L-26203.14) is the central new interface. The signed scalar
\(\lambda^Tr_X\) and the negative dipole debt `D_X^-` are added before a
positive part is taken. The two macroscopic defect ledgers of `L-25301` are not
charged separately.

## 4. Variational meaning

The Green coefficient `T_X` is the unique minimizer of

\[
\frac12T^{\!T}G_XT-r_X^{\!T}T.
\tag{L-26203.15}
\]

Thus `b_X^star` is the canonical least-Dirichlet-energy exact correction of the
parabolic seed in the endpoint-projected divisor frame.

The passage

\[
b_X^\star\longmapsto b_X^\circ=(b_X^\star)_+
\]

is the pointwise obstacle projection in the physical `b` coordinate. Its
constraint error is not widened row by row; the complete negative excursion is
first decomposed into signed interval dipoles as in `L-26202`.

Consequently `mathfrak C_X` is a primal-dual obstacle debt:

```text
signed exact Green correction
+ positive-cone obstacle projection
+ net endpoint dipole charge
- parabolic seed objective.
```

The equality state solves the constraints. The obstacle state supplies
nonnegativity. The only unproved issue is the cost of imposing both
simultaneously on this source.

## 5. Equivalent proof-facing forms

Any one of the following estimates is sufficient for the proposal:

### Direct Green–Skorokhod sharpness

\[
\boxed{
(\mathfrak C_X)_+
\le X^{o(1)}.
}
\tag{L-26203.16}
\]

### Explicit lower certificate

\[
\boxed{
\mathcal L_X^{\rm GS}
\ge
J_X(b_X^{(0)})-X^{o(1)}.
}
\tag{L-26203.17}
\]

### Weighted negative-excursion form

It is enough to prove (L-26203.17) together with a source-bound estimate of

\[
\sum_{m=2}^{X}
 |a_X(m)-a_X(m+1)|\log m,
\tag{L-26203.18}
\]

because `L-26202` bounds the complete clipped dipole gap by this variation.

### Prefix contact form

With the prefix Skorokhod contacts `lambda_j` of `L-26202`, define

\[
\mathfrak C_X^\downarrow
=
\lambda^{\!T}r_X
+
\sum_{j=2}^{X}
 \lambda_j\log\frac{j-1}{\gcd(j-1,X)}.
\tag{L-26203.19}
\]

Then

\[
\mathfrak C_X^\downarrow
=
J_X(b_X^{(0)})-\mathcal L_X^\downarrow.
\tag{L-26203.20}
\]

A subpower upper bound for the positive part of (L-26203.19) is another complete
closing theorem.

## 6. Why this is strictly sharper than old Green-energy targets

The generic energy

\[
r_X^{\!T}G_X^{-1}r_X
\]

contains the scalar mode

\[
\frac{(\lambda^{\!T}r_X)^2}{\lambda^{\!T}G_X\lambda},
\]

as shown by `L-24510`. Bounding the whole Green energy by a polylogarithm
therefore assumes control of the RH-bearing scalar before using the positive
and negative residual cancellation.

The contact debt (L-26203.14) does not do that. It pairs the scalar mode with
the signed obstacle response generated by the same Green solution. Only their
net positive remainder is estimated.

Likewise, `R-25301` rules out replacing the dipole by a nonnegative monotone
cover. The present construction uses a signed exact equality state and clips it
only once, after all Green and Möbius recombination.

## 7. Finite proof object

A production certificate for one endpoint `X` contains:

```text
complete prime-power manifest
directed target intervals w_X(q)
directed seed coordinates b_X^(0)
exact endpoint-projected profiles f_q
directed/exact Green Gram G_X
a verified solve enclosure for T_X
the complete b_X^star vector
the clipped excursion and layer-cake intervals
the net signed residual epsilon_X(q)
D_X^+, D_X^-
the lower certificate L_X^GS
the seed comparison C_X
the Möbius–Poisson all-integer charge ledger
the fixed-ratio Mertens mutation
```

A finite certificate proves only its own level. The cofinal theorem is
(L-26203.16) or one of its equivalent forms.

## 8. Proof boundary

Closed exactly:

- canonical exact equality;
- obstacle clipping;
- paired signed debt;
- direct, variation, and contact formulations;
- finite proof-object schema.

Open:

- a source-specific subpower bound for `mathfrak C_X`;
- the sharp prime-ramp lower bound;
- RH.
