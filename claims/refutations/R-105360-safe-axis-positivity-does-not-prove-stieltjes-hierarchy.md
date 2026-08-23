# R-105360 — Safe-axis positivity and finite terminal data do not prove the Stieltjes hierarchy

Claim ID: `R-105360`  
Status: **PROVED EXACT SCOPE REFUTATION**  
Created: 2026-08-23  
Depends on: `L-105351`, `L-105361`, `R-105350`  
RH status: **not assumed**

## 1. Positive safe-axis values can hide a negative moment pivot

Consider the odd entire function

\[
H(z)=z-z^3.
\tag{R-105360.1}
\]

Its origin coefficients are

\[
\beta_0=1,
\qquad
\beta_1=-1,
\qquad
\beta_n=0\quad(n\ge2).
\tag{R-105360.2}
\]

For every real `y`, however,

\[
\boxed{
{H(iy)\over iy}=1+y^2>0.
}
\tag{R-105360.3}
\]

Thus pointwise positivity on the complete imaginary axis does not imply a
positive Stieltjes representation. Indeed, the first shifted Stieltjes matrix
is already

\[
\boxed{
\mathsf S_1^{(1)}=[\beta_1]=[-1]\not\succeq0.
}
\tag{R-105360.4}
\]

The Loewner kernel also fails: its diagonal is

\[
H'(x)=1-3x^2,
\]

which is negative for `|x|>1/\sqrt3`.

Therefore a source argument proving only

\[
H(iy)/(iy)\ge0
\]

cannot establish `OASH105350`, `TAIR105360`, or `BRP105220`.

## 2. The transport theorem does not create terminal positivity

Under nonpositive annular residues,

\[
S_{\rm inner}=S_{\rm outer}+P,
\qquad P\succeq0.
\]

This proves that a terminal lower bound propagates inward. It does **not**
prove any lower bound for `S_outer`. A sufficiently negative terminal matrix
can remain negative after small positive atomic additions.

Accordingly,

```text
CRVH105330 alone -> BRP105220              FALSE / UNPROVED
atomic inward transport alone -> RH        FALSE
terminal reserve + CRVH -> BRP             VALID
```

## 3. Fixed finite order remains insufficient

For every prescribed ceiling `K`, the bounded-order separator of `R-105350`
can be placed beyond that ceiling: all confluent Stieltjes tests through order
`K` may be nonnegative while a higher Hankel determinant is negative. Thus the
phrase “for every fixed order” in `TAIR105360` means every finite order in the
mathematical quantifier, not a large but finite computed list.

## 4. Entrywise affine appearance needs the full fixed-order limit

The asymptotically affine gate `AATR105360` requires, along one cofinal
sequence,

\[
\beta_0\to a\ge0,
\qquad
\beta_n\to0
\quad\text{for every fixed }n\ge1.
\]

Observing this only for `n\le K`, or only numerically at a finite collection of
windows, does not imply `TAIR105360`. The fixed-order matrix limit is valid
only after all entries of that particular matrix have been controlled with a
rigorous error tending to zero.

## 5. Scope

The example `H(z)=z-z^3` is an abstract analytic separator, not an Xi boundary
function. It proves that no source-free implication from safe-axis value signs
to the complete Stieltjes hierarchy exists. Special Xi structure may prove the
hierarchy, but that is precisely the open producer theorem rather than a
formal consequence of scalar positivity.
