# R-32404 — Powers of the Q=4 inner source destroy the balanced reserve already at row (8,4)

Claim ID: `R-32404`  
Title: Raising the Q=4 Euler–Blaschke local factor to higher powers preserves positive inverse/generalized-prime data but does not strengthen the Selberg–Kummer route; the balanced reserve is already negative at power two  
Status: **EXACT FINITE REFUTATION OF THE HIGH-POWER SHORTCUT**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-09  
Scope: scalar powers of the Q=4 local Euler factor; does not refute multichannel/root-of-unity source frames

## 1. Powered systems

For an integer `K>=1`, put

\[
 B_K(s)=\frac{E_4(s)^K}{\zeta(s)},
 \qquad
 A_K=B_K^{-1}.
\]

The local inverse factor is a positive power of

\[
 {1-4^{-s}\over1-4^{1-s}},
\]

so the Dirichlet inverse coefficients remain nonnegative. Its generalized-prime sequence is

\[
\boxed{
 \Lambda_K=\Lambda+K D,
}
\tag{R-32404.1}
\]

where

\[
 D(4^r)=(4^r-1)\log4,
 \qquad D(n)=0\text{ otherwise}.
\]

Thus positivity of the inverse and generalized primes survives every fixed power.

## 2. The row (8,4)

On the central row

\[
(n,j)=(8,4),
\]

the `4`-column has no carry:

\[
\chi_{8,4}(4)=2-1-1=0.
\]

There is no higher active four-adic level. Hence the generalized-prime first moment is independent of `K`:

\[
\boxed{
 P_K(8,4)=\log\binom84=\log70.
}
\tag{R-32404.2}

However, in the complete Selberg forcing

\[
 C_K=\Lambda_K\log+\Lambda_K*\Lambda_K,
\]

the mixed ordinary/local convolution at destination `8=2\cdot4` survives. Since

\[
 D(4)=3\log4=6\log2,
 \qquad
 \Lambda(2)=\log2,
\]

and the two convolution orders both occur, its row contribution is exactly

\[
\boxed{
 2K\Lambda(2)D(4)
 =12K(\log2)^2.
}
\tag{R-32404.3}

All other `K`-dependent local terms are absent at this row. Therefore

\[
\boxed{
 \mathcal R_K(8,4)
 =\mathcal R_1(8,4)
  -12(K-1)(\log2)^2.
}
\tag{R-32404.4]

(The closing bracket in the tag is typographical only.)

PR #325 `L-32405/X-32402` gives the rigorous value

\[
0<\mathcal R_1(8,4)<2.
\]

On the other hand

\[
12(\log2)^2>12(69/100)^2>5.
\]

Consequently

\[
\boxed{
 \mathcal R_2(8,4)<0.
}
\tag{R-32404.5}

and therefore every `K>=2` fails the desired all-row balanced reserve at the same row.

## 3. Consequence

The tempting strategy

```text
raise the critical all-pass Euler factor to a large power;
attenuate every off-line pole more strongly;
let the enlarged positive reserve absorb the boundary
```

is invalid. The first-moment local correction is invisible at `(8,4)`, while its mixed ordinary/local Selberg forcing grows linearly in the power. More source power makes this row worse rather than better.

This also explains why the root-of-unity channel separation of `L-32421` is structurally different: it **separates** active local levels before the Hermitian square instead of stacking them in one scalar generalized-prime sequence.

## 4. Disposition

```text
positive inverse for B_K                    RETAINED
nonnegative generalized primes for B_K       RETAINED
critical all-pass attenuation per factor     RETAINED
all-row Selberg reserve for K>=2              REFUTED at (8,4)
high-power scalar source as RH shortcut       REJECTED
multichannel Fourier separation               UNAFFECTED
Riemann Hypothesis                            UNPROVED
```
