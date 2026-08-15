# L-93780 — Directed primitive enclosures for `zeta(1/2)` and `zeta'(1/2)`

Claim ID: `L-93780`  
Status: **PROVED DIRECTED ANALYTIC PRIMITIVE**  
Created: 2026-08-15  
Replay: `X-93780-target-lorenz-directed-tail/check_zeta.py`  
RH status: **unproved**

The tail formula of PR #497 uses the constants `zeta(1/2)` and
`zeta'(1/2)`. They are no longer inserted as unproved long-double literals.
The directed replay proves

\[
\boxed{-1.460355<\zeta(1/2)<-1.460354}
\tag{L-93780.1}
\]

and

\[
\boxed{-3.922647<\zeta'(1/2)<-3.922646.}
\tag{L-93780.2}
\]

## Proof

At `a=100000`, use the Hurwitz Euler--Maclaurin identity through `B_2`:

\[
\zeta(s)=\sum_{n<a}n^{-s}
 +\frac{a^{1-s}}{s-1}+\frac12a^{-s}
 +\frac{s}{12}a^{-s-1}+R(s,a).
\]

At `s=1/2`, the periodic Bernoulli bound `|B_2({t})|<=1/6` gives

\[
|R(1/2,a)|\le\frac1{24a^{3/2}},
\tag{L-93780.3}
\]

and differentiation under the absolutely convergent remainder integral gives

\[
|\partial_sR(1/2,a)|
\le
\frac1{a^{3/2}}
\left(\frac5{36}+\frac{\log a}{24}\right).
\tag{L-93780.4}
\]

Every finite inverse square root and logarithm is evaluated at 100 decimal
digits and widened by `10^-82` after every interval operation. The resulting
enclosures are

```text
zeta(1/2):
[-1.4603545101272025046..., -1.4603545074919711211...]

zeta'(1/2):
[-3.9226461587708152837..., -3.9226461196474881713...]
```

which lie strictly inside (L-93780.1)--(L-93780.2).

The proof-object digest is

```text
efc17650cab07edbff49adf1f321569ccbd2a731d85103568df9f9455923f81b
```

and no displayed decimal is used without its enclosing interval.
