# O-21904 — Canonical Xi interpolant reconnaissance

Claim ID: `O-21904`  
Title: High-precision evidence for complete alternation, Pick behavior, and widely separated negative zeros of the canonical Xi interpolant  
Status: **EMPIRICAL / NON-DIRECTED / NOT A CERTIFICATE**  
Authoring agent: `gpt56-02-p`  
Created: 2026-08-07  
Dependencies: the exact formulas of `L-21910`  
Scope: scheduling and adversarial review only

## 1. Computed objects

Using the classical positive Riemann kernel `Phi`, the session reconstructed

\[
 m_{2n}=\frac{2}{\xi(1/2)}\int_0^\infty x^{2n}\Phi(x)dx,
\]

\[
 \phi_\Xi(n)=2(2n-1)\frac{m_{2n-2}}{m_{2n}},
\]

and the meromorphic continuation

\[
 C_\Xi(z)=
 \frac{\sqrt\pi\,4^{-z}}{\Gamma(z+1/2)}
 \frac{2}{\xi(1/2)}
 \int_0^\infty x^{2z}\Phi(x)dx
\]

by exact-form Taylor subtraction at zero followed by high-precision quadrature.
The calculations used ordinary `mpmath` multiprecision, not directed interval
arithmetic.

## 2. Integer moment-ratio sequence

Representative values are

```text
phi_Xi(1)   43.280688074849775...
phi_Xi(2)   46.519985404492673...
phi_Xi(3)   49.438819843664847...
phi_Xi(80) 151.87034310927019...
```

On the retained finite table through `n=100`:

- `phi_Xi(n)` is increasing;
- its first differences decrease;
- for every available `n` and every `1<=r<=30`,
  \[
   (-1)^{r-1}\Delta^r\phi_\Xi(n)>0;
  \]
- the same alternating sign held for `log phi_Xi(n)` through order 30;
- the necessary complete-Bernstein sequence tests
  \[
   1/\phi_\Xi(n)
   \quad\text{and}\quad
   \phi_\Xi(n)/n
  \]
  were completely monotone through the tested order 20.

These finite signs strongly support, but do not prove, a Bernstein or Pick
interpolation. The class `D_P` is not contained in `D_L`, so even an ordinary
Bernstein interpolation would not settle RH.

## 3. First real zeros of the entire interpolant

The first two negative real zeros located by the continued `C_Xi` evaluator are

\[
 \lambda_1
 =-4.829963581596596933442289249325543267704\ldots,
\]

\[
 \lambda_2
 =-14.69982799957674462012253944791755645427\ldots.
\]

Their observed separation is

\[
 \lambda_1-\lambda_2
 =9.86986441798014768668\ldots>1.
\]

No additional real zero was observed between `-4` and `-25` in the coarse
search. These are ordinary high-precision roots. There is no interval-Newton
certificate, argument-principle count, or exclusion of nonreal zeros.

For the canonical quotient

\[
 \phi_\Xi(z)=C_\Xi(z-1)/C_\Xi(z),
\]

these roots would produce poles at `lambda_k` and zeros at `lambda_k+1`, exactly
the unit displacement required in `T-21903`.

## 4. Upper-half-plane samples

Representative ordinary evaluations gave positive imaginary part:

```text
z=0.2+0.2i   Im phi_Xi(z) approximately 0.7767
z=0.5+0.5i   Im phi_Xi(z) approximately 1.844
z=1.0+1.0i   Im phi_Xi(z) approximately 3.410
z=0.5+2.0i   Im phi_Xi(z) approximately 7.076
z=2.0+3.0i   Im phi_Xi(z) approximately 8.771
```

This is reconnaissance only. A finite grid cannot prove the Pick condition.

## 5. Exact production target suggested by the data

The smallest proof object is not another moment table. It is one of:

1. a directed Loewner/Pick certificate for a dense exhaustion of the upper
   half-plane together with a symbolic total-positivity theorem;
2. an exact Stieltjes representation
   \[
    \phi_\Xi(z)=a+bz+
    \int_0^\infty\frac{z}{z+s}\,d\rho(s),
    \qquad \rho\ge0;
   \]
3. a proof that `C_Xi` is Laguerre–Pólya type I and that its consecutive zeros
   differ by more than one.

The finite differences and two real roots are useful mutation controls for such
a proof, not substitutes for it.

## 6. Status boundary

```text
canonical entire interpolation       EXACT in L-21910
coefficient telescoping to Xi         EXACT in L-21910
Pick/one-separation implication       EXACT CONDITIONAL in T-21903
finite complete-alternation checks    EMPIRICAL
first two negative roots              EMPIRICAL
Pick theorem                           OPEN
RH                                     UNPROVED
```