# R-103010 — A positive kernel factor or modulus square does not orient BCI

Claim ID: `R-103010`  
Status: **EXACT SOURCE-BLIND FIREWALL**  
Created: 2026-08-26  
Depends on: `L-103070--L-103071`; corrected PR #751 `R-106150`  
RH status: **unproved**

`L-103070` proves that the critical-weighted half-kernel has a strictly
positive Fourier factor, and `L-103071` proves that the fixed differential
multiplier has positive real part with phase smaller than nine degrees. These
facts do not orient an analytic source square.

## 1. Analytic and modulus squares are different sources

Take the two-atom source polynomial

\[
 S_M(t)=1-Me^{-it\lambda},
 \qquad M>0.
\]

Its analytic square is

\[
\boxed{
 S_M(t)^2
 =1-2Me^{-it\lambda}+M^2e^{-2it\lambda}.
}
\tag{R-103010.1}
\]

By contrast,

\[
\boxed{
 |S_M(t)|^2
 =1+M^2-2M\cos(t\lambda).
}
\tag{R-103010.2}
\]

Equation (R-103010.1) lives on product/source-sum translates
`0,lambda,2lambda`; equation (R-103010.2) lives on difference translates
`0,+-lambda`. Replacing one by the other is exactly the forbidden passage from
Boolean/Wick analytic convolution to an autocorrelation or uncentered family
square.

## 2. Disjoint-translate sign countermodel

Let

\[
 k=P(D)(a*a)
\]

be the fixed logarithmic one-atom detector kernel from `L-103071`. It is
compactly supported and nonzero. Since `P(D)` contains `D`,

\[
 \int_{\mathbb R}k(x)\,dx=0.
\]

Thus `k` has both positive and negative parts. The same conclusion follows
directly from the explicit signed derivative-outer kernel of `L-102880`.

Choose `lambda` larger than the support diameter of `k`. The analytic square
(R-103010.1) gives the physical output

\[
\boxed{
 k(x)-2M k(x-\lambda)+M^2k(x-2\lambda).
}
\tag{R-103010.3}
\]

The three supports are disjoint. Hence its logarithmic negative mass is

\[
 \|k_-\|_1+2M\|k_+\|_1+M^2\|k_-\|_1,
\tag{R-103010.4}
\]

which grows quadratically in `M`.

The source in this countermodel is not the Boolean arithmetic source, so it
does not refute `BCI102990`. It proves the exact logical limitation:

\[
\boxed{
 \text{positive kernel amplitude}
 +\text{small detector phase}
 \not\Longrightarrow
 \text{one-sided analytic-square output}.
}
\tag{R-103010.5}
\]

## 3. Binding consequence

A proof of BCI must use the literal arithmetic phase/cancellation in
`mathscr Q_U(t)` or an exactly equivalent source identity. None of the
following suffices source-blindly:

```text
positivity of r_A(t);
positive real part of P(1/4+it);
a bound for |S_U(t)|^2;
an uncentered character-family modulus square;
separate positive estimates of the two half-fields.
```

The corrected exact frontier is `T-103080`.
