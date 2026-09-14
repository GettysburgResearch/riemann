# Binding correction: the endpoint numerator must retain its denominator resolvent

## Finding

The endpoint algebra and the actual Xi exterior-square numerator are valid, but
the first source-to-Hankel promotion was not.

For a reduced all-pass quotient

\[
U=N/D,
\]

and analytic `g` for which `Dg,Ng in H^2`,

\[
H_U(Dg)=P_-(Ng)=0.
\]

Thus a denominator-multiplied analytic source lies in `ker H_U`, not in the
Hankel initial space.  The assumption `D G subset (ker H_U)^perp` can hold only
trivially.

The minimal fixture is

\[
U=z^{-1},\quad N=1,\quad D=z,\quad g=1.
\]

Here `H_U(1)` is nonzero but `H_U(Dg)=H_U(z)=0`.

## What survives

The following results remain exact:

- every even derivative endpoint telescopes directly to Xi;
- `N-D=2 i lambda(F F^(K+1)-F'F^K)`;
- for Xi and even `K`, the numerator is the derivative of a nonnegative
  exterior-square Fourier density;
- the signed Fourier-tail and confluent residue-Gram formulas;
- the companion barycenter and half-plane count ledger;
- convex derivative-root compression.

## Correct conclusion-facing object

The actual Hankel symbol is

\[
\boxed{
U-1={N-D\over D}.
}
\]

The denominator derivative and every pole principal part are load bearing.  At
a simple pole,

\[
\operatorname{Res}U
 ={2i\lambda(F F^{(K+1)}-F'F^K)(z)\over D'(z)}.
\]

The former source-density ratios remain useful local algebra but do not by
themselves bound the all-pass Hankel charge.

## Correct fourth-endpoint target

Using the unconditional fixed-order input

\[
R_4/N>2487/2500-o(1),
\]

the literal sufficient theorem is

\[
\boxed{
\limsup {\|H_{U_4}\|_{S_2}^2\over N}< {237\over2500}
\quad\Longrightarrow\quad
\liminf {N_0\over N}>0.9.
}
\]

An equivalent source-qualified signed residue-Gram estimate may replace the
full norm.  This corrected gate is `RESGRAM106450` and remains open.

## Binding status

```text
endpoint winding/exterior-square source       RETAINED PROVED
Dg source -> nonzero initial-space leakage     REFUTED
visible <1/600 and <1/982 percentage payments WITHDRAWN
T-106430/T-106440 percentage compositions      SUPERSEDED
RESGRAM106450                                  OPEN / RECORD-BEARING
90% / density one / RH                         UNPROVED
```
