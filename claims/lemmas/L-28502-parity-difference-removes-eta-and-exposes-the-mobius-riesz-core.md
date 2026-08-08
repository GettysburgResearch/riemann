# L-28502 — The parity difference removes eta and exposes the Möbius Riesz core

Claim ID: `L-28502`  
Title: Canceling the dyadic obstruction in the MCF dual removes exactly the factor `1-2^{1-s}` and leaves a translated classical Möbius Riesz sum  
Status: **PROPOSED COMPLETE EXACT LEMMA — independent review requested**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Dependencies: `L-28501`; finite reindexing  
Scope: exact source identification and proof boundary; no RH claim

## 1. The dyadic dual source

Retain

\[
\mathfrak D(X)
=\sum_{q\le X}\frac{a(q)}{\sqrt q}\log(X/q),
\qquad
A(s)=\sum_{q\ge1}\frac{a(q)}{q^s}
=\frac{2^{-s}}{\eta(s)}.
\tag{L-28502.1}
\]

The nonreal poles used in `R-28501` come from the factor

\[
1-2^{1-s}
\]

inside `eta(s)`.

## 2. Exact parity difference

Define

\[
\boxed{
\mathfrak P(X)
=\mathfrak D(X)
-\sqrt2\,\mathfrak D(X/2),
}
\tag{L-28502.2}
\]

where the second term is zero for `X<2`.

Reindexing the second sum gives

\[
\begin{aligned}
\sqrt2\,\mathfrak D(X/2)
&=\sum_{2q\le X}
\frac{2a(q)}{\sqrt{2q}}
\log\frac{X}{2q}.
\end{aligned}
\tag{L-28502.3}
\]

Thus

\[
\mathfrak P(X)
=\sum_{n\le X}\frac{c(n)}{\sqrt n}\log(X/n),
\tag{L-28502.4}
\]

with

\[
\boxed{
c(n)=a(n)-2\mathbf1_{2\mid n}a(n/2).}
\tag{L-28502.5}
\]

Its Dirichlet series is

\[
\begin{aligned}
C(s)
&=(1-2^{1-s})A(s)\\
&=\boxed{\frac{2^{-s}}{\zeta(s)}}.
\end{aligned}
\tag{L-28502.6}

Therefore

\[
\boxed{
c(2m)=\mu(m),\qquad c(2m+1)=0.}
\tag{L-28502.7}
\]

Substitution into (L-28502.4) yields the exact identity

\[
\boxed{
\mathfrak P(X)
=\frac1{\sqrt2}
\sum_{m\le X/2}
\frac{\mu(m)}{\sqrt m}
\log\frac{X/2}{m}.
}
\tag{L-28502.8}

No limit or analytic continuation is used here.

## 3. Mellin transform

For `Re(z)>1/2`,

\[
\boxed{
\int_1^\infty
\mathfrak P(X)X^{-z-1}\,dX
=
\frac{2^{-(z+1/2)}}{z^2\zeta(z+1/2)}.
}
\tag{L-28502.9}

Equivalently, (L-28502.9) follows from (L-28501.19) by multiplying with

\[
1-\sqrt2\,2^{-z}=1-2^{1-(z+1/2)}.
\]

Hence the parity difference cancels every artificial eta-factor pole on
`Re(z)=1/2`. It does not cancel a single zeta zero.

## 4. Exact interpretation

The chain is now rigid:

```text
one-sided MCF edge menu
    -> dyadic dual source 2^-s/eta(s)
    -> artificial Re(s)=1 eta poles
    -> MCF is false;

source-complete parity difference
    -> cancellation of 1-2^(1-s)
    -> source 2^-s/zeta(s)
    -> translated Möbius Riesz sum.
```

Thus a parity repair is necessary to escape `R-28501`, but after it is performed the remaining scalar is not routine boundary bookkeeping. It is the classical RH-bearing Möbius source itself.

## 5. One-sign boundary

Let

\[
\mathcal R_\mu(Y)
=\sum_{m\le Y}\frac{\mu(m)}{\sqrt m}\log(Y/m).
\tag{L-28502.10}
\]

Then

\[
\mathfrak P(X)=2^{-1/2}\mathcal R_\mu(X/2).
\tag{L-28502.11}
\]

Any eventual bound

\[
\mathfrak P(X)\ge-C_\varepsilon X^\varepsilon
\quad\text{for every }\varepsilon>0
\tag{L-28502.12}
\]

would, by the standard one-sided Mellin-Landau argument, exclude every zero of zeta with real part greater than `1/2`. Conversely, an off-line zero remains an uncancelled pole of (L-28502.9).

The lemma does not assert (L-28502.12). It proves that any corrected MCF/parity architecture must establish a genuine Möbius estimate rather than merely pay a deterministic eta collar.

## 6. Consequences for current branches

1. A pure MCF support theorem is impossible by `R-28501`.
2. A parity lift can legitimately remove that obstruction only if its complete edge/cycle ledger realizes the difference (L-28502.2).
3. Once realized, the conclusion-producing source is exactly (L-28502.8).
4. A claimed proof which obtains a positive parity ledger but never controls the translated Möbius Riesz coordinate has not completed RH.
5. A proof which deletes the parity cross term recreates the artificial eta poles and fails `R-28501`.

## 7. Proof boundary

Established exactly:

- the finite parity difference;
- the coefficient formula;
- cancellation of the eta factor;
- identification with the translated Möbius Riesz sum;
- the Mellin transform and surviving zeta poles.

Open:

- a one-sided subpower bound for the Möbius Riesz sum;
- unrestricted positive carry saturation or another valid source mechanism;
- RH.