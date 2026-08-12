# R-91610 — Positive log generators do not make the signed three-scale completion passive

Claim ID: `R-91610`  
Status: **EXACT SIGNED-COMBINATION AND DETERMINANT FIREWALL**  
Created: 2026-08-12  
Depends on: `L-91610/L-91611`; `L-91404`; `R-91404`  
RH status: **unproved**

## 1. The tempting shortcut

`L-91610` proves that every safe prime Euler channel has a positive-real
logarithmic generator and that the safe prime cascade is additive in this
coordinate.  It is tempting to insert these generators directly into the
three-scale Cauchy recurrence and conclude positivity.

That inference is false.

## 2. Signed positive-real generators can have either sign

The recurrence carries the scale coefficients

\[
 -1,
 \qquad
 \frac{17}{16},
 \qquad
 -\frac1{16}.
\]

Let `ell_1,ell_2,ell_4` be nonnegative real constants.  Each is the
positive-real logarithmic generator of the constant zero-free Schur multiplier

\[
 m_r=e^{-\ell_r}.
\]

Nevertheless

\[
 \mathscr L
 =-\ell_1+rac{17}{16}\ell_2-rac1{16}\ell_4
\]

can have either sign:

```text
(ell_1,ell_2,ell_4)=(1,0,0)  ->  mathscr L=-1;
(ell_1,ell_2,ell_4)=(0,1,0)  ->  mathscr L=17/16.
```

Therefore positivity of every one-scale Clark generator does not survive the
signed radial observation automatically.  The scales must be interconnected
before the recurrence signs are applied.

## 3. Determinant equality does not imply operator order

Let

\[
 A=\begin{pmatrix}4&0\\0&1/4\end{pmatrix},
 \qquad
 B=I.
\]

Then

\[
 \det A=\det B=1,
\]

so their logarithmic determinants agree, but

\[
 A-B=\begin{pmatrix}3&0\\0&-3/4\end{pmatrix}
\]

is indefinite.

Thus even exact equality of source and target entropy does not prove CPPD or
PDWT on a multi-vector packet.  A full conservative source map, or an exact
one-node specialization where the target is genuinely scalar, remains
necessary.

## 4. Correct interpretation of the logarithmic route

The additive Clark generator closes the nonlinear **prime** cascade and gives
a canonical positive entropy environment.  It does not delete:

```text
the active completed pole/long channel;
the negative middle radial scale;
the finite compensation connection;
compressed-delay cross terms;
the source-to-model identification.
```

The valid continuation is a completed Redheffer interconnection in the
logarithmic coordinate, not a termwise signed sum of positive generators.

## 5. Exact boundary

```text
one-scale prime log generator positive real        EXACT
safe prime log cascade additive                    EXACT
signed three-scale log combination positive        FALSE
log-determinant equality -> Loewner order           FALSE
completed connection-aware interconnection         OPEN / RH-BEARING
Riemann Hypothesis                                 UNPROVED
```
