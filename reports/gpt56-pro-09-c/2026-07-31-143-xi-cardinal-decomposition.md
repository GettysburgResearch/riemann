# Xi-cardinal functions split the Weil form exactly

Agent: `gpt56-pro-09-c`  
Date: 2026-07-31  
Issue: #166  
Draft PR: #168

## Main identity

Let `Phi` be the standard Riemann Fourier kernel and let `gamma` be a certified
simple real zero of `Xi`.  Define

```text
psi_gamma(t)
 = i exp(i gamma t)
   integral_(-infinity)^t exp(-i gamma u) Phi(u) du.
```

Because `Xi(gamma)=0`, the same function also equals the negative right-tail
integral.  It is therefore rapidly decreasing at both ends and satisfies

```text
Fourier(psi_gamma)(z)=Xi(z)/(z-gamma).
```

After normalization by `Xi'(gamma)`, its transform is one at `gamma` and zero
at every other zeta zero, real or nonreal.

## Exact positive coordinates

For a finite set `Z` of certified simple critical-line zeros, let `C_Z` synthesize
the normalized cardinal functions and let `V_Z` evaluate at those zeros.  Then

```text
V_Z C_Z=I,
R_Z=I-C_Z V_Z,
V_Z R_Z=0.
```

The global Weil form splits exactly:

```text
Q_W(f,g)
 = Q_W(R_Z f,R_Z g)
   + sum_(gamma in Z) fhat(gamma) conjugate(ghat(gamma)).
```

The cardinal block is positive identity and Weil-orthogonal to the remainder.
Every unselected or hypothetical off-line zero is confined to the remainder.

This is stronger than a principal-angle approximation: it is exact spectral
interpolation.

## Localization

The unnormalized tail obeys

```text
|psi_gamma(t)|
 <= integral_(|u|>=|t|) |Phi(u)| du,
```

independently of `gamma`.  For each fixed finite zero set, the normalized
cardinal synthesis tails tend to zero in Schwartz/form topology as the support
expands.  The cofinal growing-set gate is the normalized tail-synthesis norm,
which includes the derivative-conditioning factor

```text
max_(gamma in Z) 1/|Xi'(gamma)|.
```

The Riemann kernel tail is double exponential, but no cofinal derivative lower
bound is asserted.

## Burnol connection

Burnol's complete/minimal systems built from `zeta(s)/(s-rho)^k` are the
Sonine/de Branges precursor of these completed centered cardinal coordinates.
The new ODE formula supplies the explicit two-sided logarithmic tail needed by
the repository's localized block method.

## Exact regression

`X-14314` uses

```text
P(z)=(z-1)(z-3)(z^2+1)
```

as a polynomial analogue.  For `h(z)=z`, the exact zero-sum form is

```text
global       8
positive    10
residual    -2.
```

The selected cardinal block is positive and orthogonal even though the
unselected nonreal pair makes the residual negative.  Eight tests and all six
checksum rows pass. Proof-object SHA-256:

```text
cd9872f6200fad83bad0a58df661558e471cf2dc2eb920d13c8d9e697f5e89c9
```

## Remaining theorem

No RH proof is claimed. The remaining cofinal problem is now a corrector-capacity
estimate for the normalized Xi-cardinal tails, together with a lower floor for
the exact selected-zero near-kernel remainder.
