# Brownian continuation: positive cutoff averaging and functional-equation symmetrization do not cure the Bohr instability

**Date:** 2026-08-11  
**Stack:** PR #376 on PR #343 / PR #296  
**Status:** RH remains unproved

## Result

The first phase of PR #376 refuted the raw one-sided cofinal stability target. The continuation now proves a wider no-go:

> Any positive Brownian cutoff mixture that retains at least `c/log N` mass on cutoffs `K in [N/2,N]` has one-sided Bohr zeros in every fixed half-strip `1/2<Re s<1` for all sufficiently large `N`. Functional-equation symmetrization preserves those zeros by a Stirling/Rouché argument.

Both repository mixtures satisfy the top-mass hypothesis:

```text
logarithmic Norlund weights       lambda_(N,K)=1/(K H_N);
central-binomial Green weights    lambda_(N,K)=omega_K/sum_(J<=N)omega_J.
```

Therefore the proposed BLNRZ and BGRRZ finite real-zero theorems are false on every unbounded sequence.

## One-sided mixture theorem

For a positive mixture,

```text
m_(lambda,N)(s)
 =pi^(-s/2)Gamma(1+s/2)D_(lambda,N)(s),
D_(lambda,N)(s)=s B_(lambda,N)(s)+A_(lambda,N)(s),
B_(lambda,N)(s)=sum_(n<=N)b_(N,n)n^(-s),
b_(N,n)=1/2 sum_(K=n)^N lambda_(N,K)C_(K,n)>0.
```

The selected-prime block `2sqrt(N)<=p<=3sqrt(N)` obeys

```text
b_(N,p) >> 1/log N,
b_(N,mp)/b_(N,p) <= exp[-5(m^2-1)],
0<b_(N,n)<=2.
```

At any fixed `1/2<beta<1`, random Steinhaus phases make the unselected residual bounded because

```text
sum b_(N,n)^2 n^(-2beta) <= 4 zeta(2beta).
```

The selected prime-phase mass grows like

```text
N^((1-beta)/2)/(log N)^2 -> infinity.
```

It therefore cancels the residual exactly. Kronecker and Hurwitz turn the torus zero into infinitely many actual zeros of the one-sided factor with real parts tending to `beta`.

## Symmetrization theorem

At a simple one-sided zero `s_j=w_j+it_j`,

```text
D_N'(s_j) asymp t_j.
```

For

```text
A(s)=pi^(-s/2)Gamma(1+s/2),
```

uniform Stirling gives, on `Re s=beta>1/2`,

```text
|A(1-s)|/|A(s)| << |t|^(1/2-beta).
```

On a circle of radius `r_j=t_j^(-(beta-1/2)/2)`, the one-sided term is larger than the reflected term by a power of `t_j`. Rouché gives an off-line zero of

```text
X_N(s)=m_N(s)+m_N(1-s)
```

near every sufficiently high one-sided zero.

Thus exact functional-equation symmetry does not rescue the finite approximants.

## Disposition

```text
raw cofinal stability                      FALSE;
logarithmic Norlund real-zero theorem       FALSE;
central-binomial Green-Robin real-zero      FALSE;
positive finite cutoff averaging as cure    FALSE;
functional-equation symmetrization as cure  FALSE;
finite identities and local convergence     RETAINED;
height-dependent finite theorem              OPEN;
infinite limiting canonical system           OPEN;
RH                                            UNPROVED.
```

The surviving Brownian question is no longer “find the missing canonical-system proof for these finite producers.” These particular finite producers have the wrong global zero geometry. A future route must be height-dependent, redesign the producer to eliminate all torus zeros, or construct the limiting operator directly without claiming finite global real-zero stability.

## Verification

`X-90602` gives exact-rational checks of both weight families, their top-half mass, the positive leading coefficients, and the finite multiple-ratio algebra:

```text
PASS_X_90602_BROWNIAN_MIXTURE_INSTABILITY
```

The computation is a regression only; the refutation is analytic.
