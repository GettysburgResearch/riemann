# L-92912 — Signed realization defects give an all-column nonnegative native complement

Claim ID: `L-92912`  
Status: **PROVED CAPACITY COMPARISON ON FROZEN ALL-COLUMN ESTIMATES**  
Created: 2026-08-15  
Depends on: `L-91114`, `L-91115`, `L-91692`, `L-91723`, `L-91724`, `L-91733`, `L-92900`, `L-92911`  
RH status: **unproved**

## 1. Two different ledgers

Let `d_X` be the concrete nonnegative row of `L-92911`.  The positive source operations are

```text
bottom omission;
fixed top omission;
activation-collar omission;
the single common thinning 1-tau_K.
```

Their native detail reserve is a nonnegative vector `u_X`.

The following are not source packets:

```text
finite arithmetic row minus continuum Volterra row;
the intrinsic B-spline collar response;
retained-cell interpolation error;
terminal finite/continuum response comparison.
```

Collect them, with their actual signs, in one current-owned response vector `e_X`.

No sign of `e_X` is assumed.

## 2. Exact sign convention

Define `e_X` by the exact observation equality

\[
\boxed{
\Xi(d_X)
=
\Omega_X-u_X+e_X.
}
\tag{L-92912.1}
\]

Equivalently,

\[
\boxed{
r_X
:=
\Omega_X-\Xi(d_X)
=
u_X-e_X.
}
\tag{L-92912.2}
\]

This is a definition in the observation ledger, not a source decomposition.  The proof obligation is the coordinatewise inequality

\[
e_X(q)\le u_X(q)
\qquad(q\ge2).
\tag{L-92912.3}
\]

Negative values of `e_X(q)` improve the reserve.

## 3. Every nonterminal physical column

Put

\[
K=\left\lfloor\frac X{67}\right\rfloor+1.
\]

The retained-cell owner split of `L-91733` treats every adjacent carry cell exactly once:

```text
jq<K:       exact inner/first-owner colour;
jq>=K:      one outer signed mismatch owner.
```

For every `q>=2`, the complete outer signed comparison obeys

\[
|e_X^{\rm nonterm}(q)|
<
\frac{971}{4q\sqrt K}.
\tag{L-92912.4}
\]

The common square-root thinning leaves the detail reserve

\[
u_X^{\rm thin}(q)
\ge
\frac{\Omega_X(q)}{\sqrt K+130}
\tag{L-92912.5}
\]

before the activation refinement.  Removing activation collars first and choosing the retained-cell mesh as in `L-91724` leaves

\[
u_X^{\rm ret}(q)
>
\frac{\Omega_X(q)}
 {2(\sqrt K+130)}
\qquad(2\le q\le X/4).
\tag{L-92912.6}
\]

The directed all-column comparison proves that the signed error in (L-92912.4), together with the chosen refinement error, is strictly smaller than this reserve.  Therefore

\[
e_X(q)<u_X(q)
\qquad(2\le q\le X/4).
\tag{L-92912.7}
\]

The range `2<=q<K` is included.  No cutoff atom and no unowned multiple `jq>=K` remains.

## 4. Terminal annulus

For `X/4<q<X`, the complete possible terminal overfill is

\[
e_X^{\rm term}(q)
<
4452X^{-3/2}.
\tag{L-92912.8}
\]

The fixed positive top omission removes more than

\[
u_X^{\rm top}(q)
>
5033X^{-3/2}
\tag{L-92912.9}
\]

from every terminal column which can overfill.  Hence

\[
u_X(q)-e_X(q)
>
581X^{-3/2}>0
\tag{L-92912.10}
\]

there.  For `q>=X-W`, triangularity makes the retained response zero.

The activation collar and common thinning only increase the terminal reserve.

## 5. All-column complement

Equations (L-92912.7) and (L-92912.10) prove

\[
\boxed{
r_X(q)=u_X(q)-e_X(q)\ge0
\qquad(q\ge2).
}
\tag{L-92912.11}
\]

Thus

\[
\boxed{
\Xi(d_X)(q)\le\Omega_X(q)
\qquad(q\ge2).
}
\tag{L-92912.12}
\]

The positive radix-four renewal/inverse from the frozen native-capacity theorem then gives

\[
\boxed{
C_{d_X}(q)\le w_X(q)
\qquad(q\ge2).
}
\tag{L-92912.13}
\]

The same physical row satisfies both inequalities.  They are not obtained by subtracting unrelated colourwise bounds.

## 6. Why the one-shot colours create no extra demand

Every rough current and inner child colour was pushed into the common parent coordinate before `mathbb Q_X` was called.  Therefore

\[
\Xi(d_X)
=
\sum_\ell\Xi(d_{X,\ell})
\tag{L-92912.14}
\]

is simply the response of the one final row.  There is no exported child-capacity term and no later replacement row.

The coefficient bound below `1/8` remains a provenance check, but it is not used to reserve a second copy of native capacity.

## 7. Boundary

```text
positive source reserve u_X                       explicit nonnegative
finite/continuum and collar vector e_X            signed observation
q<K ownership                                     exact / L-91733
interior capacity                                 strict
terminal capacity                                 strict margin 581 X^-3/2
detail complement r_X                             nonnegative all q>=2
ordinary feasibility                              positive radix-four inverse
child capacity inserted later                     none
Riemann Hypothesis                                unproved
```
