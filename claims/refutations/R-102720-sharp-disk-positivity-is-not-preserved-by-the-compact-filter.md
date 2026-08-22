# R-102720 — SHARP-disk positivity is not preserved by the compact dyadic filter

Claim ID: `R-102720`  
Status: **PROVED EXACT COMPOSITION FIREWALL**  
Created: 2026-08-22  
Depends on: `L-102722--L-102724`  
RH status: **unproved**

The pointwise tangent theorem says that, before compact filtering,

\[
q_z(X)=q(X)+2\Re(z)h(X)+|z|^2a(X)\ge0
\]

throughout the complete SHARP disk.

This does not imply that the dyadically filtered family remains nonnegative.

Let

\[
P_2=(I-\sqrt2S_2)(I-S_2)^2
=
I-(2+\sqrt2)S_2+(1+2\sqrt2)S_2^2-\sqrt2S_2^3.
\]

Choose a nonnegative scalar fixture `f` on one dyadic orbit with

```text
f(X)=0,
f(X/2)=1,
f(X/4)=0,
f(X/8)=0.
```

Then

\[
\boxed{P_2f(X)=-(2+\sqrt2)<0.}
\tag{R-102720.1}
\]

Thus even a strictly nonnegative scale family can become negative under the exact compact filter used by the conclusion-facing wavelet.

The same obstruction applies to a positive semidefinite matrix-valued family entrywise: a signed linear combination of PSD matrices need not be PSD.

Consequently none of the following implications is valid without an additional arithmetic theorem:

```text
unfiltered SHARP-disk positivity
  -> filtered scalar positivity;

unfiltered S-lemma matrix PSD
  -> filtered matrix PSD;

strict local determinant reserve
  -> subpower negative mass of the compact detector.
```

The valid interface is the exact identity `L-102724.6`. A successor must preserve the source, carrier compensation and matrix slack through the signed filter and the distinct-product physical collapse. The remaining statement is named `FLC102730` in `T-102730`.