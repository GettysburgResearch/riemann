# T-102770 — The filtered Lorentz problem reduces to one-octave endpoint radial cost

Claim ID: `T-102770`  
Status: **MAJOR UNCONDITIONAL LOCALIZATION ADVANCE; RH UNPROVED**  
Created: 2026-08-23  
Base: PR #719  
RH status: **unproved**

`L-102729--L-102736` replace the former signed-filter and homotopy interfaces
by one endpoint, carrier-subtracted, sublinear matrix gauge.

## 1. Full filtered disk

For every completion tangent and every scale,

\[
 JP_2Q_{\tau,-1+w}(X)\ge0
 \qquad(|w|\le1/2).
\]

The complete disk has one S-lemma matrix and one reserve.  The Lorentz current
is the fixed support functional `4A-B`.

## 2. Exact compact centering

The common ray carrier is

\[
 cX\sum_n\Sigma_\tau(n)n^{-3/2},
 \qquad c=2(2-\sqrt2).
\]

After subtracting it once, every disk coefficient has support ratio eight.
The earlier `(X-1)` carrier display is superseded by this exact formula; the
barycentric current is unchanged.

## 3. One sublinear radial gauge

The centered radial cost `mathfrak R` is positively homogeneous and
subadditive.  It satisfies

\[
 (4A-B)_-\le\mathfrak R(A,B,P_0^\circ)
\]

and the deterministic bound

\[
 \mathfrak R(A,B,C)
 \le
 4|A|+\frac{65}{16}|B|+\frac{129}{8}|C|.
\]

Thus every source region already controlled in `L1` remains controlled after
the matrix reduction without duplicating the reserve.

## 4. Homotopy compression

Integrating the full disk in the completion parameter before applying the
S-lemma produces one endpoint defect matrix and one endpoint radial cost
`bar(mathfrak R)(X)`.  It is no larger than the integral of the time-resolved
costs.

The conclusion-facing estimate therefore needs no homotopy parameter.

## 5. Four-octave localization and improved determinant reserve

On a physical horizon `Y<=X<=2Y`, ratio-eight support restricts every source
product to

\[
 Y/8\le n\le2Y,
\]

which is exactly four source octaves.  Subadditivity gives

\[
 \bar{\mathfrak R}_{\rm full}
 \le
 \sum_{j=0}^3\bar{\mathfrak R}_j.
\]

For each one-octave packet, the centered output support has logarithmic length
`4 log 2`.  The exact CV/XD contraction is

\[
 \boxed{
 \|XD\|^2
 \le
 \left(
 \frac14+\frac{9(\log2)^2}{\pi^2}
 \right)\|CV\|^2
 <0.689\|CV\|^2.
 }
\]

The strict diagonal reserve is therefore greater than `0.311` on every local
packet.

## 6. Final localized theorem

Define

```text
OERSC102770:
  for each of the four exact source octaves on every dyadic physical horizon,
  the endpoint centered radial cost has subpower logarithmic integral.
```

Then

\[
 \boxed{
 \mathrm{OERSC}_{102770}
 \Longrightarrow
 \mathrm{ERSC}_{102736}
 \Longrightarrow
 \mathrm{TRF}_{102750}
 \Longrightarrow
 \mathrm{AR\!-\!DEFECT}_{102600}
 \Longrightarrow
 \mathrm{RH}.
 }
\]

The remaining arithmetic estimate is now local in all of the following senses:

```text
one fixed endpoint defect;
one fixed filtered disk;
one carrier subtraction;
one S-lemma reserve;
one source octave;
one ratio-eight physical shell.
```

A source-blind coefficient countermodel still prevents the deterministic
contraction from proving the one-sided arithmetic estimate automatically.

```text
full filtered disk                         PROVED
exact common carrier                       CORRECTED / PROVED
centered support ratio eight               PROVED
radial gauge sublinearity                  PROVED
endpoint homotopy compression              PROVED
four-octave source localization            PROVED
one-octave contraction <0.689              PROVED
OERSC102770                                OPEN / RH-BEARING
Riemann Hypothesis                         UNPROVED
```
