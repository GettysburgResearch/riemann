# L-26202 — Green–Skorokhod reflection and exact signed contact debts

Claim ID: `L-26202`  
Title: Clipping or one-sided Skorokhod reflection of an exact Green carry state yields explicit nonnegative lower and upper certificates whose errors are signed endpoint dipoles  
Status: **PROPOSED — COMPLETE EXACT FINITE LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Issue: #260  
Dependencies: `L-24501`, `L-24509`, `L-24520`, `L-26201`  
Scope: finite algebra; no asymptotic debt estimate

## 1. Exact equality state

Fix `X>=2` and let

\[
\mathcal Q_X=\{p^a:p^a\le X\}.
\]

Let `w(q)` be any target on `Q_X`, and let

\[
b^\star=(b^\star_2,\ldots,b^\star_X)
\]

satisfy

\[
\boxed{
v_q(b^\star)=w(q)
\qquad(q\in\mathcal Q_X).
}
\tag{L-26202.1}
\]

The canonical application is the endpoint-projected Green state of `L-24509`,
but the identities below hold for every exact equality state.

Put

\[
\mathcal P_w
=\sum_{q\in\mathcal Q_X}\Lambda(q)w(q)
\tag{L-26202.2}
\]

and

\[
J_X(b)
=\sum_{m=2}^{X}b_m\log\frac m{m-1}.
\tag{L-26202.3}
\]

The von Mangoldt divisor identity gives

\[
\boxed{
J_X(b)=\sum_{q\in\mathcal Q_X}\Lambda(q)v_q(b),
}
\tag{L-26202.4}
\]

so (L-26202.1) implies

\[
J_X(b^\star)=\mathcal P_w.
\tag{L-26202.5}
\]

The equality state may have negative coordinates.

## 2. Positive-part excursion and interval dipoles

Define the negative excursion

\[
a_m=(-b^\star_m)_+,
\tag{L-26202.6}
\]

and clip once, after the complete equality solve,

\[
\boxed{
b^\circ_m=b^\star_m+a_m=(b^\star_m)_+\ge0.
}
\tag{L-26202.7}
\]

Let

\[
\varepsilon_q
=v_q(b^\circ)-w(q)
=v_q(a).
\tag{L-26202.8}
\]

The sequence `a` has a canonical finite layer-cake decomposition. At every
distinct positive height, decompose the superlevel set into its connected
integer intervals. Thus

\[
a_m
=\sum_\alpha t_\alpha
 \mathbf1_{A_\alpha<m\le B_\alpha},
\qquad t_\alpha>0.
\tag{L-26202.9}
\]

By the exact incidence block identity `L-24520`, each interval contributes

\[
\boxed{
\Delta_\alpha v_q
=t_\alpha
 \bigl(
  \mathbf1_{q\mid B_\alpha}
  -\mathbf1_{q\mid A_\alpha}
 \bigr).
}
\tag{L-26202.10}
\]

Consequently

\[
\boxed{
\varepsilon_q
=\sum_\alpha t_\alpha
 \bigl(
  \mathbf1_{q\mid B_\alpha}
  -\mathbf1_{q\mid A_\alpha}
 \bigr).
}
\tag{L-26202.11}
\]

This is the requested signed constraint-dipole recombination. All interval
endpoints are summed before any positive or negative part of the constraint
error is taken.

## 3. One clipped state gives a two-sided scalar sandwich

Define the weighted net endpoint masses

\[
D_X^+
=\sum_{q\in\mathcal Q_X}\Lambda(q)(\varepsilon_q)_+,
\qquad
D_X^-
=\sum_{q\in\mathcal Q_X}\Lambda(q)(-\varepsilon_q)_+.
\tag{L-26202.12}
\]

Set

\[
\boxed{
\mathcal L_X^\circ
=J_X(b^\circ)-D_X^+,
\qquad
\mathcal U_X^\circ
=J_X(b^\circ)+D_X^-.
}
\tag{L-26202.13}
\]

Since

\[
J_X(b^\circ)-\mathcal P_w
=\sum_q\Lambda(q)\varepsilon_q
=D_X^+-D_X^-,
\]

one has the exact identities

\[
\boxed{
\mathcal P_w-\mathcal L_X^\circ=D_X^-,
\qquad
\mathcal U_X^\circ-\mathcal P_w=D_X^+.
}
\tag{L-26202.14}
\]

In particular,

\[
\boxed{
\mathcal L_X^\circ
\le\mathcal P_w
\le\mathcal U_X^\circ.
}
\tag{L-26202.15}
\]

This is not the old positive-part cover. The vector is clipped only after the
signed exact Green solve, and the full signed endpoint residual
\(\varepsilon\) is assembled before its two parts are charged.

## 4. Weighted-BV control of the dipole gap

Put

\[
\gamma_m=a_m-a_{m+1},
\qquad a_{X+1}=0.
\tag{L-26202.16}
\]

Then

\[
\varepsilon_q=\sum_{kq\le X}\gamma_{kq}.
\tag{L-26202.17}
\]

Therefore

\[
\begin{aligned}
D_X^++D_X^-
&=\sum_{q\in\mathcal Q_X}
 \Lambda(q)\left|\sum_{kq\le X}\gamma_{kq}\right|\\
&\le
\sum_{m=2}^{X}|\gamma_m|
 \sum_{\substack{q\in\mathcal Q_X\\q\mid m}}\Lambda(q).
\end{aligned}
\]

Since the inner sum equals `log m`,

\[
\boxed{
D_X^++D_X^-
\le
\sum_{m=2}^{X}
 |a_m-a_{m+1}|\log m.
}
\tag{L-26202.18}
\]

Thus a subpower logarithmically weighted variation theorem for the one negative
Green excursion is already a subpower-sharp carry sandwich.

## 5. Prefix and suffix Skorokhod reflections

The clipping construction is the most flexible signed-dipole form. Two
one-sided reflections give still more explicit contact ledgers.

Define

\[
\sigma_m=\max_{2\le k\le m}a_k,
\qquad \sigma_1=0,
\tag{L-26202.19}
\]

\[
\tau_m=\max_{m\le k\le X}a_k,
\qquad \tau_{X+1}=0.
\tag{L-26202.20}
\]

Put

\[
b_m^\downarrow=b^\star_m+\sigma_m,
\qquad
b_m^\uparrow=b^\star_m+\tau_m.
\tag{L-26202.21}
\]

Both vectors are nonnegative. Define the contact increments

\[
\lambda_j=\sigma_j-\sigma_{j-1}\ge0,
\qquad
\nu_j=\tau_j-\tau_{j+1}\ge0.
\tag{L-26202.22}
\]

The prefix regulator is a sum of endpoint incidence dipoles:

\[
\sigma_m
=\sum_{j=2}^{X}\lambda_j\mathbf1_{j\le m\le X}.
\]

Hence

\[
\boxed{
v_q(b^\downarrow)-w(q)
=
\sum_{j=2}^{X}\lambda_j
\bigl(
 \mathbf1_{q\mid X}
 -\mathbf1_{q\mid j-1}
\bigr).
}
\tag{L-26202.23}
\]

Therefore the prefix residual is nonpositive whenever `q` does not divide `X`;
all possible positive residual is concentrated on the finite prime-power tower
dividing the endpoint.

Let

\[
E_X^{\rm end}
=\sum_{\substack{q\in\mathcal Q_X\\q\mid X}}
 \Lambda(q)\bigl(v_q(b^\downarrow)-w(q)\bigr).
\tag{L-26202.24}
\]

The endpoint terms in (L-26202.23) are nonnegative, so no positive-part symbol is
needed. Define

\[
\mathcal L_X^\downarrow
=J_X(b^\downarrow)-E_X^{\rm end}.
\tag{L-26202.25}
\]

Then

\[
\boxed{
\mathcal L_X^\downarrow\le\mathcal P_w.
}
\tag{L-26202.26}
\]

More precisely,

\[
\boxed{
\mathcal P_w-\mathcal L_X^\downarrow
=
\sum_{j=2}^{X}
 \lambda_j
 \log\frac{j-1}{\gcd(j-1,X)}.
}
\tag{L-26202.27}
\]

Indeed, one contact dipole moves mass from `j-1` to `X`; the prime-power
weights common to both endpoints cancel, leaving exactly the logarithm of the
coprime quotient.

For the suffix reflection,

\[
\tau_m
=\sum_{j=2}^{X}\nu_j\mathbf1_{2\le m\le j},
\]

so

\[
\boxed{
v_q(b^\uparrow)-w(q)
=
\sum_{j=2}^{X}\nu_j\mathbf1_{q\mid j}
\ge0.
}
\tag{L-26202.28}
\]

Thus `b^up` is an exact nonnegative cover and

\[
\boxed{
J_X(b^\uparrow)-\mathcal P_w
=
\sum_{j=2}^{X}\nu_j\log j.
}
\tag{L-26202.29}
\]

The formulas (L-26202.27) and (L-26202.29) are exact contact-debt
certificates.

## 6. Minimality of the regulators

The prefix regulator is the pointwise smallest nonnegative nondecreasing
sequence `s_m` satisfying

\[
b^\star_m+s_m\ge0.
\]

The suffix regulator is the pointwise smallest nonnegative nonincreasing
sequence with the same property.

Thus the two contact ledgers are canonical one-sided Skorokhod deformations of
the exact Green state, not arbitrary repairs.

Writing

\[
A_X^\star=\max_{2\le m\le X}(-b^\star_m)_+,
\]

one obtains the immediate bounds

\[
\boxed{
0\le
\mathcal P_w-\mathcal L_X^\downarrow
\le A_X^\star\log X,
}
\tag{L-26202.30}
\]

\[
\boxed{
0\le
J_X(b^\uparrow)-\mathcal P_w
\le A_X^\star\log X.
}
\tag{L-26202.31}
\]

These inequalities are useful finite gates, although the full proposal uses the
more cancellation-preserving clipped dipole ledger.

## 7. Proof boundary

Closed exactly:

- layer-cake interval-dipole decomposition;
- clipped lower and upper scalar certificates;
- weighted-BV gap;
- prefix/suffix Skorokhod incidence formulas;
- exact contact-debt identities;
- regulator minimality.

Open:

- a subpower bound for the clipped or contact debt for the actual parabolic
  Green state;
- the sharp prime-ramp theorem;
- RH.
