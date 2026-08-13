# L-91307 — The rough-prime renewal is critical and a scalar positive branch allocation cannot close it

Claim ID: `L-91307`  
Status: **PROVED ASYMPTOTIC RENEWAL THEOREM / DESIGN FIREWALL**  
Created: 2026-08-12  
Depends on: `L-91108`, `L-91113`, `R-91101`  
RH status: **unproved**

## 1. Small-prime constants

Let

\[
 P_{53}=\prod_{p\le53}p,
\]

and define

\[
 \delta_{53}=\prod_{p\le53}\left(1-\frac1p\right)>0,
 \qquad
 \beta_{53}=\prod_{p\le53}\left(1-\frac1{\sqrt p}\right)>0.
\tag{L-91307.1}
\]

For `a in {1,2}`, write

\[
 U_a(x)=a\sqrt x\,B(x)-A(x),
\tag{L-91307.2}
\]

so that `U_1=R` and `U_2=L`.  The finite Boolean forcing of `L-91113` is

\[
 F_a^{(53)}(x)
 =\sum_{d\mid P_{53}}\mu(d)w_a(x,d),
 \qquad
 w_a(x,d)=\left(\frac{a\sqrt x}{d}-\frac1{\sqrt d}\right)1_{d\le x}.
\tag{L-91307.3}
\]

For every `x>=P_53`, all small-prime divisors are active, hence exactly

\[
 \boxed{
 F_a^{(53)}(x)=a\delta_{53}\sqrt x-\beta_{53}.
 }
\tag{L-91307.4}
\]

## 2. Harmonic mass of the rough monoid

Let

\[
 \mathcal M_{59}=\{m\ge1:(m,P_{53})=1\}
\]

and put

\[
 S_{59}(x)
 =\sum_{\substack{m\le x\\m\in\mathcal M_{59}}}\frac1{\sqrt m}.
\tag{L-91307.5}
\]

Inclusion--exclusion gives

\[
 S_{59}(x)
 =\sum_{d\mid P_{53}}
  \frac{\mu(d)}{\sqrt d}
  \sum_{n\le x/d}\frac1{\sqrt n}.
\tag{L-91307.6}
\]

The classical Euler expansion

\[
 \sum_{n\le y}n^{-1/2}
 =2\sqrt y+\zeta(1/2)+O(y^{-1/2})
\tag{L-91307.7}
\]

is uniform for `y>=1`.  Since `P_53` is fixed, substitution into
(L-91307.6) yields

\[
 \boxed{
 S_{59}(x)
 =2\delta_{53}\sqrt x
  +\zeta(1/2)\beta_{53}
  +O_{P_{53}}(x^{-1/2}).
 }
\tag{L-91307.8}
\]

Thus the delayed rough-prime reservoir has exactly the same square-root scale
as the forcing.  It is critical, not a small perturbation.

## 3. Centered renewal

The exact renewal of `L-91113` is

\[
 F_a^{(53)}(x)
 =\sum_{\substack{m\le x\\m\in\mathcal M_{59}}}
  m^{-1/2}U_a(x/m).
\tag{L-91307.9}
\]

Introduce the natural constant centers

\[
 c_a=\frac a2,
 \qquad
 E_a(x)=U_a(x)-c_a.
\tag{L-91307.10}
\]

Then

\[
 \boxed{
 G_a(x):=F_a^{(53)}(x)-\frac a2S_{59}(x)
 =\sum_{m\in\mathcal M_{59},\,m\le x}
  m^{-1/2}E_a(x/m).
 }
\tag{L-91307.11}
\]

Equations (L-91307.4) and (L-91307.8) give the exact limiting boundary forcing

\[
 \boxed{
 G_a(x)
 =\beta_{53}\left[-1-\frac a2\zeta(1/2)\right]
  +O_{P_{53}}(x^{-1/2}).
 }
\tag{L-91307.12}
\]

Since

\[
 \zeta(1/2)=-1.4603545088\ldots,
\]

one obtains

\[
 \boxed{
 G_1(\infty)
 =\beta_{53}\left[-1-\frac12\zeta(1/2)\right]<0,
 }
\tag{L-91307.13}
\]

\[
 \boxed{
 G_2(\infty)
 =\beta_{53}\left[-1-\zeta(1/2)\right]>0.
 }
\tag{L-91307.14}
\]

Thus the equality and reserve channels carry opposite centered boundary signs.

For the SHARP combination `Psi=L+2R`,

\[
 \boxed{
 G_2(x)+2G_1(x)
 =\beta_{53}[-3-2\zeta(1/2)]
  +O(x^{-1/2})<0.
 }
\tag{L-91307.15}
\]

The numerical constant is

\[
 -3-2\zeta(1/2)=-0.07929098238\ldots.
\]

## 4. Consequences for positive allocation

### 4.1 No small-kernel argument

Equation (L-91307.8) rules out every proof which treats the delayed rough-prime
copies as a norm-small tail relative to the `sqrt(x)` forcing.  Their leading
mass is exactly `2 delta_53 sqrt(x)`.

### 4.2 No scalar centered cone

Suppose one attempts to prove the renewal by placing every centered reserve
copy `E_1(x/m)` in a nonnegative scalar cone.  Then the right side of
(L-91307.11) is nonnegative, contradicting the negative limit
(L-91307.13).  The same failure persists for the centered SHARP output by
(L-91307.15).

Therefore a successful reset cannot preserve the independent cones

```text
R-1/2 >=0,
L-1 >=0,
Psi-2 >=0.
```

It must mix the two channels and/or include an explicit finite boundary port.

### 4.3 The deficit is bounded, not macroscopic

Although the rough reservoir is critical at scale `sqrt(x)`, the uncancelled
centered forcing in (L-91307.12) is only an `O(1)` constant.  This is compatible
with the bounded per-generation debt allowed by `T-91101`.

Thus the exact design target is a conservative two-state allocation whose
cross-channel boundary port pays the fixed constants in
(L-91307.13)--(L-91307.15), while the delayed bulk is transferred with
coefficient one.

## 5. Connection to the operator routes

The structure is the arithmetic analogue of a conservative colligation:

```text
critical positive reservoir      S_59;
observed signed state             (L,R);
finite boundary defect            G_a(infinity);
required proof                    cross-channel Schur allocation.
```

Taking absolute values destroys the `sqrt(x)` cancellation; scalar inversion
creates alternating signs.  The required map must retain the full two-state
cross term, just as the Suzuki and theta/Brownian routes require a fixed
multi-channel completion.

## 6. Proof boundary

```text
rough-monoid square-root asymptotic             EXACT
critical cancellation with Boolean forcing       EXACT
opposite L/R centered boundary signs              EXACT
negative centered SHARP boundary forcing          EXACT
scalar positive-centered allocation               REFUTED
mixed two-state boundary port                      OPEN
coefficient-one rough-prime reset                  OPEN / RH-BEARING
Riemann Hypothesis                                UNPROVED
```
