# L-100703 — Symmetric balanced squaring homotopy and its positive critical boundary layer

Claim ID: `L-100703`  
Status: **PROVED EXACT HOMOTOPY + UNCONDITIONAL ENDPOINTWISE POSITIVITY LAYER**  
Created: 2026-08-20  
Depends on: `L-100701`; centered-Bernstein critical owner inequality  
RH status: **not assumed**

For a finite active prime set put

\[
E_p=I-r_pU_p,
\quad
Q_p=I-r_p^2U_p^2,
\quad
R_p=r_pU_p(I-r_pU_p),
\]

and, for `0<=t<=1`, define

\[
\boxed{
H_{p,t}:=Q_p-tR_p
=I-tr_pU_p-(1-t)r_p^2U_p^2.
}
\tag{L-100703.1}
\]

Let

\[
H_t=\prod_pH_{p,t}.
\]

Then

\[
H_0=\prod_pQ_p,
\qquad
H_1=\prod_pE_p.
\tag{L-100703.2}
\]

## 1. Symmetric homotopy identity

Finite differentiation gives

\[
{d\over dt}H_t
=-\sum_pR_p\prod_{q\ne p}H_{q,t}.
\]

Therefore

\[
\boxed{
\prod_pE_p
=
\prod_pQ_p
-
\int_0^1
\sum_pR_p\prod_{q\ne p}H_{q,t}\,dt.
}
\tag{L-100703.3}
\]

This is the permutation-invariant counterpart of the ordered first-transition
identity `L-100701.2`. It retains the completed and transition carriers inside
one common parameterized source until their cancellation is taken.

## 2. Literal labelled source

For each prime, the local factor (L-100703.1) has three mutually exclusive
states:

```text
absent                     coefficient +1;
one ordinary p-label       coefficient -t r_p;
one squared p^2-label      coefficient -(1-t) r_p^2.
```

Thus `H_t` is an exact labelled Euler source. A local state never contains both
the ordinary and squared copy of the same prime.

At the final centered-Bernstein critical kernel, removing an ordinary label
costs at most `1/p`, while removing a squared label costs at most `1/p^2`.
Hence the complete adjacent-level owner budget at endpoint `X` is

\[
\boxed{
\Sigma_t(X)
\le
 t\sum_{p\le X}{1\over p}
 +(1-t)\sum_p{1\over p^2}
 +{1\over67^2},
}
\tag{L-100703.4}
\]

where the last term is the second labelled `67` occurrence.

## 3. Positive homotopy boundary layer

Put

\[
H_X:=\sum_{p\le X}{1\over p},
\qquad
 t_X:=\min\left(1,{1\over4H_X}\right).
\]

Using the elementary bound from PR #677,

\[
\sum_p{1\over p^2}< {95\over196},
\]

one obtains, for `0<=t<=t_X`,

\[
\Sigma_t(X)
< {1\over4}+{95\over196}+{1\over4489}< {3\over4}<1.
\tag{L-100703.5}
\]

The ordinary adjacent-level double-counting therefore gives

\[
kM_k(t,X)\le\Sigma_t(X)M_{k-1}(t,X),
\]

and every odd level is smaller than the preceding even level. Consequently:

\[
\boxed{
(H_tR_{m,m-1})(X)>0
\quad
(0\le t\le t_X,\ m\ge3),
}
\tag{L-100703.6}
\]

where `R_(m,m-1)` is any final centered-Bernstein critical remainder in the
canonical hierarchy.

Since `H_X=log log X+O(1)`, the proved positive layer has width
`asymp1/log log X`.

## 4. Correct remaining interval

The original critical state is `t=1`. Equations (L-100703.3) and
(L-100703.6) show that the open arithmetic is confined to the balanced
homotopy interval

\[
 t_X<t\le1,
\]

with the carrier cancellation of `L-100702` retained pointwise in the same
`t`-integral.

The missing statement is not positivity of the finite completion at `t=0` and
not positive inversion. It is a one-sided physical bound for the balanced
homotopy derivative after the explicitly positive boundary layer has been
removed.