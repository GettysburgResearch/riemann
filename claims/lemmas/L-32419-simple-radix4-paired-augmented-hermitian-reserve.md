# L-32419 — Simple radix-four pair has a source-complete Hermitian reserve

Claim ID: `L-32419`  
Title: The imaginary Jordan curvature of the simple radix-four plus/minus pair is positive cofinally on every quarter-balanced row, and every row through 4734 has a directed exact positive certificate  
Status: **PROPOSED COMPLETE COFINAL HERMITIAN THEOREM + EXACT FINITE REPLAY — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-09  
Dependencies: `L-32416/L-32417`; generalized Selberg identity; elementary absolute-mass estimates  
Scope: source-complete row curvature; global independent-frequency recurrence remains separate

## 1. Source/Jordan coordinates

For each sign retain the Dirichlet system of `L-32416`, with inverse coefficients `b_\pm`, generalized primes `Lambda_\pm`, and

\[
 C_\pm=\Lambda_\pm\log+\Lambda_\pm*\Lambda_\pm.
\]

Put

\[
 q_\pm=b_\pm*\Lambda_\pm,
 \qquad
 t_\pm=b_\pm*C_\pm.
\tag{L-32419.1}
\]

For one binary carry row `e=(n,j)`, write

\[
 Y_\pm=\mathcal L_e(b_\pm),
 \qquad
 Q_\pm=\mathcal L_e(q_\pm),
 \qquad
 T_\pm=\mathcal L_e(t_\pm).
\tag{L-32419.2}
\]

Let `R_pair` be the positive paired Kummer reserve of `L-32417`.

Define

\[
\boxed{
 \mathcal A_{\rm pair}(e)
 =\mathcal R_{\rm pair}(e)
 +\frac12\sum_{\sigma\in\{-,+\}}
  \left[Q_\sigma(e)^2-Y_\sigma(e)T_\sigma(e)\right].
}
\tag{L-32419.3}

## 2. Exact Hermitian orientation

For each sign form the Jordan deformation

\[
 J_{\sigma,\tau}(s)
 =\frac{A_\sigma(s-\tau)}{A_\sigma(s)},
 \qquad
 K_{\sigma,\tau}=b_\sigma*J_{\sigma,\tau}.
\]

On the row define

\[
 f_\sigma(\tau)=1+\mathcal L_e(J_{\sigma,\tau}),
 \qquad
 g_\sigma(\tau)=\mathcal L_e(K_{\sigma,\tau}).
\]

At `tau=0`,

\[
 f_\sigma=1,
 \quad f_\sigma'=P_\sigma,
 \quad f_\sigma''=S_\sigma,
\]

\[
 g_\sigma=Y_\sigma,
 \quad g_\sigma'=Q_\sigma,
 \quad g_\sigma''=T_\sigma.
\]

Because the independent-frequency direction is imaginary, Taylor expansion gives

\[
\boxed{
 {1\over2}{d^2\over dt^2}
 \left(
 |f_\sigma(it)|^2+|g_\sigma(it)|^2
 \right)\bigg|_{t=0}
 =P_\sigma^2-S_\sigma+Q_\sigma^2-Y_\sigma T_\sigma.
}
\tag{L-32419.4}

Averaging the two signs and using `L-32416.15--16` yields exactly

\[
\boxed{
 {1\over4}{d^2\over dt^2}
 \sum_{\sigma=\pm}
 \left(
 |f_\sigma(it)|^2+|g_\sigma(it)|^2
 \right)\bigg|_{t=0}
 =\mathcal A_{\rm pair}(e).
}
\tag{L-32419.5}

Thus (L-32419.3) is the correctly oriented Hermitian second variation of the complete generalized-prime plus inverse-source pair. It is not an ad-hoc correction to a Kummer inequality.

## 3. Bare source charges are bounded constants

Since

\[
 \mathbf1*b_- =\varepsilon-4\delta_4,
 \qquad
 \mathbf1*b_+ =\varepsilon+4\delta_4,
\]

their floor potentials stabilize at `-3` and `5`, respectively. Therefore once parent and both children are at least four,

\[
\boxed{Y_-=3,\qquad Y_+=-5.}
\tag{L-32419.6}
\]

For every row, including the finite endpoint collar,

\[
\boxed{|Y_\pm|\le5.}
\tag{L-32419.7}
\]

## 4. Cofinal second-current bound

The generalized-prime coefficients of either sign have absolute mass bounded by the positive finite main-pole source of `L-32415`:

\[
 \sum_{m\le x}|\Lambda_\pm(m)|
 <\frac{10}{3}x
\]

for the declared cofinal range. The same partial-summation argument as `L-32415` gives

\[
\boxed{
 \sum_{m\le x}|C_\pm(m)|<15x\log x
}
\tag{L-32419.8}
\]

once `x>=4735`.

Moreover

\[
 \mathbf1*t_\pm
 =(\varepsilon\pm4\delta_4)*C_\pm.
\]

Hence its prefix is one current-scale prefix plus one quarter-scale prefix. On a quarter-balanced row with `n>=4*4735`, all three relevant arguments are in the cofinal range and

\[
\boxed{|T_\pm(n,j)|\le60n\log n.}
\tag{L-32419.9}
\]

The constant is deliberately crude: each of the parent/child prefix terms is bounded by `30x log x`, and `j+k=n`.

Consequently

\[
\boxed{
 {1\over2}
 \left|Y_-T_-+Y_+T_+\right|
 \le300n\log n.
}
\tag{L-32419.10}

## 5. Cofinal positivity

`L-32417` gives for every sufficiently large quarter-balanced row

\[
 \mathcal R_{\rm pair}(n,j)
 \ge\frac{n^2\log^22}{320}.
\tag{L-32419.11}
\]

Since the current squares in (L-32419.3) are nonnegative, (L-32419.10)--(L-32419.11) imply

\[
 \mathcal A_{\rm pair}(n,j)
 \ge {n^2\log^22\over320}-300n\log n.
\tag{L-32419.12}
\]

The right side is positive for all sufficiently large `n`; for example `n>=10^7` is more than sufficient using the elementary bounds `log2>69/100` and `log n<17` at the initial endpoint together with monotonicity of `log n/n` thereafter.

Thus

\[
\boxed{
 \mathcal A_{\rm pair}(n,j)>0
}
\tag{L-32419.13}
\]

uniformly on the quarter-balanced cone cofinally.

No PNT, zero-free region, or RH-scale cancellation is used in this cofinal proof.

## 6. Directed finite theorem through 4734

`X-32419-simple-radix4-paired-augmented` constructs rigorous fixed-point intervals for all logarithms, both signed generalized-prime systems, their complete Selberg sequences, `q_\pm`, and `t_\pm`.

It then evaluates the lower endpoint of twice (L-32419.3) on every quarter-balanced row through parent 4734. The result is

```text
classification
PASS_EXACT_SIMPLE_Q4_PAIRED_AUGMENTED_HERMITIAN_RESERVE

balanced rows
2,803,709

finite endpoint
4734

minimum row
(6,2)

minimum augmented reserve lower bound
6.485722622277412...
```

The decimal is orientation only; the exact scaled integer lower margin is retained in the result payload.

Digest:

```text
62ff333cdad2997f8840eaa71327f5a8b3c4a917d044d4f138b799f2435805ea
```

The finite interval `4735<n<10^7` is not needed for a cofinal RH consumer and is not claimed checked here. It is an ordinary finite base region.

## 7. What this closes

The local source-complete Hermitian orientation is no longer an open sign question for the simple pair:

```text
paired generalized-prime Kummer reserve   positive;
source currents                            retained;
bare inverse-source terms                  retained;
second source currents                     retained;
imaginary/Hermitian sign                   explicit;
cofinal augmented reserve                  positive.
```

Together with the exact carry-position row placement `L-32412` on PR #326, this removes both the row-coordinate ambiguity and the local Hermitian sign ambiguity.

It still does not give a global RH proof. The remaining step is to derive from the complete independent-frequency reflected identities a block-energy inequality in which this positive curvature appears as **dissipation**, rather than merely as a positive comparison quantity.

## 8. Proof boundary

Closed here:

1. exact imaginary-Jordan orientation;
2. bounded two-tap source charges;
3. elementary cofinal second-current bound;
4. uniform cofinal positivity;
5. directed finite positivity through parent 4734.

Still open:

1. global source-convolved reflected dissipation/no-double-spend identity;
2. the resulting coefficient-one or subexponential pole-current recurrence;
3. RH.
