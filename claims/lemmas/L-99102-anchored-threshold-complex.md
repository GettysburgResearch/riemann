# L-99102 — Anchored duplicate-67 threshold-complex formulation

Claim ID: `L-99102`  
Status: **PROVED EXACT**  
Depends on: `L-99001`, `L-99002`  
RH status: **unproved**

Let `F(t)=C(t)/6` be the expected Euler characteristic in L-99001.  Adjoin a
second labelled vertex `67*` of cost `67` and activity

\[
 r=67^{-1/2}.
\]

Let `F*(t)` denote the expected Euler characteristic of the resulting induced
multiplicative-threshold complex.  The exact add-one-label recurrence gives

\[
 F^*(t)=F(t)+r\bigl(\mathbf1_{t\ge67}-F(t/67)\bigr).
\]

Therefore

\[
\boxed{
 \frac{H_{67}(t)}6
 =F^*(t)-r\mathbf1_{t\ge67}.}
\]

Equivalently, the factor-67 Harnack target is an **anchored Euler-characteristic
inequality**: after duplicating the 67 vertex, the expected Euler characteristic
must cover the activity of one distinguished 67 anchor.

At the Dirichlet-series level this is exactly the squared local factor in
L-99101.  At the combinatorial level it identifies a concrete closure task:
construct a source-faithful weighted matching or relative-complex argument for
this anchored expectation.

No pointwise claim about the Euler characteristic of every random induced
complex is made.  Only the expectation identity is proved here.
