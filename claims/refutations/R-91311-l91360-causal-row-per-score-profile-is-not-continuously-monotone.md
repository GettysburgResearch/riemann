# R-91311 — The causal row-per-score profile is not continuously monotone

Claim ID: `R-91311`  
Status: **EXACT COUNTEREXAMPLE / SCOPE CORRECTION**  
Created: 2026-08-13  
Refutes: `L-91360` as stated  
Retains: global single-endpoint monotonicity `L-91359`  
RH status: **unproved**

## 1. Claimed causal profile

For an integer row `j`, real `p>=67`, and real `z>=1`, put

\[
 S(Y)=5\sqrt Y-3,
 \qquad r=p^{-1/2},
\]

and

\[
 \mathcal R_{p,j}(z)
 =\frac{Q_{pz}(j)-rQ_z(j)}{S(pz)-rS(z)}.
\tag{R-91311.1}
\]

`L-91360` claims that this function is nondecreasing in `z` on the complete causal window.

## 2. Exact derivative numerator

On an activation cell write

\[
 C_Y(j)=\partial_{\log Y}Q_Y(j).
\]

The sign of the logarithmic derivative of (R-91311.1) is the sign of

\[
\boxed{
\begin{aligned}
\mathfrak N={}&
 [C_{pz}(j)-rC_z(j)]
 [S(pz)-rS(z)]\\
&-[Q_{pz}(j)-rQ_z(j)]
 \left[\frac52\sqrt{pz}-r\frac52\sqrt z\right].
\end{aligned}}
\tag{R-91311.2
}

Take

\[
\boxed{
 j=66,
 \qquad p=67,
 \qquad z=\frac{133}{2}.
}
\tag{R-91311.3
}

Then `pz=8911/2`, and neither endpoint lies at an activation knot.

## 3. Directed certificate

The companion standard-library replay uses:

- exact `Fraction` arithmetic;
- rational square-root enclosures of denominator `10^50`;
- rational atanh-series logarithm enclosures;
- the exact Green formula for `Q_Y(66)`;
- only the elementary lattice bounds
  \[
  4\sqrt Y-4-2\log Y
  \le
  \sum_{m\le Y}m^{-1/2}\log(Y/m),
  \]
  and
  \[
  \sum_{m\le N}m^{-1/2}\le2\sqrt N-1.
  \]

It proves the directed corridors

\[
 Q_{8911/2}(66)>0.0968219,
 \qquad
 C_{8911/2}(66)<0.0595545,
\]

and, most importantly,

\[
\boxed{
 \mathfrak N<-1.5293<0.
}
\tag{R-91311.4
}

Therefore

\[
\boxed{
 \frac{d}{d\log z}\mathcal R_{67,66}(z)<0
 \quad\text{at }z=133/2.
}
\tag{R-91311.5
}

The causal ratio decreases on a neighborhood of this point.

## 4. Consequences

The following claims are withdrawn:

```text
continuous causal row-per-score monotonicity;
the sufficient derivative gate in L-91360;
use of L-91358 with that continuous monotonicity as an input.
```

The checked-in historical `X-91136` verifier also fails; it must not be treated as a positive certificate.

The following remain unaffected:

```text
single-endpoint profile Q_Y(j)/(5 sqrt(Y)-3) increasing;  L-91359
frontier ordering when the child term is inactive;        L-91359
the abstract Lorenz bathtub theorem when its order input holds; L-91358
```

The source nodes in the arithmetic packet are discrete divisors of `P_61`. Numerical reconnaissance suggests that ordering may survive on that discrete set even though continuous ordering fails. No discrete theorem is claimed here.

## 5. Proof boundary

```text
L-91359 single-endpoint monotonicity              RETAINED
L-91360 continuous causal monotonicity             FALSE
historical X-91136 PASS claim                      FALSE / NO RESULT
finite discrete-divisor causal ordering            OPEN
direct Lorenz row subordination                     OPEN
Riemann Hypothesis                                  UNPROVEN
```
