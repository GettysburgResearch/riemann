# Prime-positive square-diagonal attack

Agent: `gpt56-03-w`  
Date: 2026-08-07  
Repository: `gfreund123/riemann`  
Branch: `agent/gpt56-03-r/207-directed-d0001-frame`  
PR: #208  
Classification: new one-scalar prime-positive RH criterion; RH not proved

## Executive result

The previous prime-prefix attack removed matrices and the real support
continuum, but its exact entropy/Fenchel margin still contained a delicate
signed cumulative transport problem. PR #218 then found an integer-dilation
criterion on a fixed interval below the first prime knot, where every prime
coefficient is favorable; its finite level nevertheless required the whole
compact interval, or every prime knot in an exponentially growing annulus.

This pass extracts a single adaptive point from that prime-free region at each
critical square cutoff.

Fix `0<a<log2` and put

\[
 r_n=\left\lceil{2\log n\over a}\right\rceil,
 \qquad
 t_n={2\log n\over r_n}.
\]

Then `t_n<=a<log2` and `r_nt_n=2log n`. Define

\[
 \mathcal J_a(n)=r_n^2\Psi(t_n)-\Psi(2\log n).
\]

`T-20804` proves

\[
 \boxed{
 RH
 \iff
 (-\mathcal J_a(n))_+=n^{o(1)}
 \iff
 \mathcal J_a(n)\ge0\text{ eventually}.}
\]

There is exactly one scalar per integer `n`.

## Upper-envelope Landau transfer

The converse needs the upper rather than lower square-sample envelope. The new
lemma `L-20814` mirrors `L-19801`.

If

\[
 (\Psi(2\log n))_+=n^{o(1)},
\]

then RH follows. More quantitatively, a positive-part exponent `2theta` excludes
zeros in

\[
 \operatorname{Re}s>{1\over2}+\theta.
\]

The proof applies Landau's one-sign theorem to

\[
 P(t)e^{\sigma t}-\Psi(t)\ge0,
\]

rather than to `Psi(t)+P(t)e^(sigma t)`. The screw transform changes sign, but
the absence of positive-real xi zeros on the Laplace axis and the pole-exclusion
argument are identical.

Since `t_n` remains in a fixed compact prime-free interval and
`r_n=O(log n)`, the condition

\[
 \mathcal J_a(n)\ge-n^{o(1)}
\]

gives

\[
 \Psi(2\log n)\le O_a(\log^2 n)+n^{o(1)},
\]

which is exactly the upper square-sample hypothesis.

## Exact positive-prime formula

Writing

\[
 \Psi(T)=A(T)-
 \sum_{\log q\le T}{\Lambda(q)\over\sqrt q}(T-\log q),
\]

the small-scale sum vanishes because `t_n<log2`. Therefore

\[
 \boxed{
\begin{aligned}
 \mathcal J_a(n)={}&r_n^2A(t_n)-A(2\log n)\\
 &+\sum_{q\le n^2}{\Lambda(q)\over\sqrt q}
   \log{n^2\over q}.
\end{aligned}}
\]

Every prime-power coefficient is nonnegative. The theorem has

- no adverse old-prime prefix;
- no signed prime accumulation;
- no zero data;
- no matrix;
- no Schur complement;
- no interval or prime-knot minimization.

The remaining difficulty is the order-one/subpolynomial cancellation of the
positive prime ramp against the explicit order-`n` archimedean term. Positivity
of the coefficients does not by itself supply that cancellation.

## Indicative computation

`X-20808` uses the simple exact base

\[
 a={1\over2}\log2.
\]

The complete prime-power manifest through `10^7` contains `665,134` rows, with
SHA-256

```text
ad1fe1520966ca5c41885166f4a28a0d543922f087881175c0c15e89425fc56a.
```

Every level

```text
n=2,...,3162
```

had positive ordinary margin. The maximum lower cutoff was below `sqrt(2)`, so
no lower-scale prime deposition occurred.

At `n=3162`, `r_n=47`, the 80-decimal-place replay gives

```text
positive prime ramp
12600.9672192272113120387039902564337193715062948042...

A(2 log n)
12601.0051209049633386503562836244225819959646732039...

r_n^2 A(t_n)
97.7098679914833611349042671095563156066610237285...

J_a(n)
97.6719663137313345232519737415674529822026453288...
```

This is not a directed result and not a cofinal argument. It checks the
normalization and demonstrates that the order-`n` cancellation is being retained
before the explicit `O(log^2 n)` reserve is added.

## Conditioning optimization

For fixed `a`,

\[
 r_n^2A(t_n)
 ={4A(a)\over a^2}\log^2n+O_a(\log n).
\]

Ordinary high-precision minimization gives

```text
a approximately      0.642223040599643581780592924640919...
exp(a) approximately 1.90070152288894619765819143025379...
A(a)/a^2             0.129941205778347651386582895442076...
```

from the stationary equation `a A'(a)=2A(a)`. This is only a production
conditioning nomination; the theorem works for every frozen `a<log2`.

## SERIOUS RESOLUTION PATH

The exact remaining theorem is now

\[
 \boxed{
 r_n^2A(t_n)
 +\sum_{q\le n^2}{\Lambda(q)\over\sqrt q}\log{n^2\over q}
 \ge A(2\log n)-n^{o(1)}.}
\]

A proof can proceed by one of three genuinely global mechanisms:

1. integrate Selberg's identity against the triangular square-cutoff kernel and
   preserve `Lambda*Lambda` as a positive prime-pair/semiprime Gram;
2. transport the positive finite-Euler flow of `L-20813` back to the square
   cutoff while retaining its exact cumulant defect;
3. prove a block majorization theorem in the prime-power polygon/Fenchel
   coordinates of `T-20802` and PR #219.

Any such proof, after the inherited normalization audit, proves RH. A finite
positive diagonal does not.

## Files

```text
claims/lemmas/L-20814-upper-square-sampling-landau-transfer.md
claims/theorems/T-20804-prime-positive-square-diagonal-rh-criterion.md
claims/observations/O-20807-prime-positive-square-diagonal-recon.md
claims/methodology/M-20804-prime-positive-square-diagonal-attack.md
experiments/X-20808-prime-positive-square-diagonal/recon.py
experiments/X-20808-prime-positive-square-diagonal/results/recon-1e7.json
experiments/X-20808-prime-positive-square-diagonal/README.md
```

## Honest conclusion

The adverse prime prefix and compact-cell continuum are both gone. The full
problem is now represented by one all-positive finite prime-power ramp at each
integer square cutoff. The cofinal cancellation theorem has not been proved in
this pass, so RH is not claimed solved.