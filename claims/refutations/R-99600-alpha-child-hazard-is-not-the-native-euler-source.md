# R-99600 — The contracted alpha-child hazard does not reproduce a native rough Euler factor

Claim ID: `R-99600`  
Status: **PROVED EXACT SOURCE/COEFFICIENT SEPARATOR**  
Created: 2026-08-20  
Compared inputs: `L-99021`, `L-99211`, PR #647's corrected RN child map, and
the literal native source ledger of PR #598  
RH status: **not assumed**

## 1. One-prime audit

Let

\[
r=p^{-1/2}.
\]

For one active rough prime the contracted causal identity used by the
common-parent candidate is

\[
P=(1-r)P+r(P-rUP)+r^2UP.
\tag{R-99600.1}
\]

This identity is correct, but it is an identity for the parent packet \(P\).
The shifted coefficient on the right is

\[
-r^2+r^2=0.
\tag{R-99600.2}
\]

The native rough Euler factor is instead

\[
(I-rU)P,
\tag{R-99600.3}
\]

whose shifted coefficient is

\[
-r.
\tag{R-99600.4}
\]

Therefore (R-99600.1) cannot, by itself, be the source identity that adjoins
one native rough prime.

## 2. Parity-labelled audit

In a positive two-channel source, adjoining a native rough prime sends the
child to the opposite parity channel with magnitude \(r\). If both contracted
shifted copies in (R-99600.1) are interpreted in that odd channel, their total
signed magnitude is

\[
2r^2,
\]

not \(r\). The missing native source is

\[
\boxed{r-2r^2=r(1-2r)>0}
\qquad(p\ge67).
\tag{R-99600.5}
\]

This is the one-prime form of the source-faithfulness defect previously exposed
by the exact native occurrence ledger.

PR #647's Radon--Nikodym correction repairs **where** a child lives inside the
parent endpoint source. It does not change the scalar coefficient from
\(\alpha=r^2\) to the native coefficient \(r\).

## 3. Coboundary firewall

The calibration identity

\[
E=P+A,\qquad P=J+PT
\]

implies algebraically

\[
E=J+ET+(A-AT).
\]

That telescope is exact only after the same operator \(T\) has been proved to
act on the exact native source. If \(T\) is the contracted alpha-child
operator, the coboundary preserves the coefficient dictionary of
(R-99600.1); it cannot manufacture the missing coefficient (R-99600.5).

Thus a calibration coboundary is not an independent repair of a wrong
root/source operator.

## 4. Disposition

```text
alpha-child causal algebra                 exact for P
alpha-child net shifted coefficient        0
native Euler shifted coefficient           -r
parity-exported contracted magnitude        2r^2
native parity magnitude                     r
RN endpoint child map                       retained exact
native common-parent promotion              refuted without another theorem
```

The correct coefficient-one replacement is `L-99601`.
