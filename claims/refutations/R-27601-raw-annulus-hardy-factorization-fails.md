# R-27601 — The raw annulus multiplier is not a Hardy square or a positive Laplace kernel

Claim ID: `R-27601`  
Title: The exact top-quarter annulus Mellin factor contains an omitted dyadic zero and is negative at the reflection-fixed point  
Status: **EXACT SCOPE REFUTATION / CORRECTION**  
Authoring agent: `gpt56-08`  
Created: 2026-08-08  
Dependencies: `L-27602`, `L-27603`, `T-27601`  
Scope: refutes only the unpushed raw-kernel Hardy-factorization and complete-monotonicity shortcut; the prime-annulus criterion remains valid

## 1. Exact annulus window

Let

\[
W(u)=
\begin{cases}
2u-1,&\frac12<u\le1,\\[1mm]
\frac12-4u,&\frac14<u\le\frac12,\\[1mm]
0,&\text{otherwise}.
\end{cases}
\tag{R-27601.1}
\]

For complex `s`, initially away from `0,-1`, define

\[
A(s)=\int_{1/4}^{1}W(u)u^{s-1}\,du.
\tag{R-27601.2}
\]

Direct integration of the two bands gives

\[
\begin{aligned}
A(s)
={}&
\left[\frac{2u^{s+1}}{s+1}-\frac{u^s}{s}\right]_{1/2}^{1}
+
\left[\frac{u^s}{2s}-\frac{4u^{s+1}}{s+1}\right]_{1/4}^{1/2}.
\end{aligned}
\]

After collecting the dyadic powers,

\[
\boxed{
A(s)=
\frac{(1-2^{-s})(1-2^{-s-1})(s-1)}{s(s+1)}.
}
\tag{R-27601.3}
\]

The apparent singularities at `s=0,-1` have the values supplied by the original integral. In particular, the factor `1-2^{-s}` is load bearing. The speculative continuation which wrote only

\[
2^{-s}(1-2^{-s-1})\frac{s-1}{s(s+1)}
\]

was algebraically incorrect.

## 2. Sign at the reflection-fixed point

At the fixed point `s=1/2`,

\[
\boxed{
A(1/2)
=-\frac23
(1-2^{-1/2})(1-2^{-3/2})<0.
}
\tag{R-27601.4}
\]

Consequently `A` is not completely monotone on the positive real axis: a completely monotone function must in particular be nonnegative.

The same value rules out a single reflected Hardy square. If a function `B` satisfied

\[
A(s)=B(s)\overline{B(1-\overline s)}
\tag{R-27601.5}
\]

on a domain containing `s=1/2`, then

\[
A(1/2)=|B(1/2)|^2\ge0,
\]

contradicting (R-27601.4).

Thus neither of the following is available for the raw annulus multiplier:

```text
A is the Laplace transform of a positive measure;
A is one reflected Hardy square.
```

## 3. No invented boundary completion

The exact continuum/discrete boundary in `L-27604` is an arithmetic scalar

\[
\frac{2}{X(X+1)}
\left[B(X)-3B(X/2)+2B(X/4)-\log2\right].
\]

It does not license adding an arbitrary Mellin term to force positivity. Any completed kernel must be derived from the full independent-frequency identity, with every endpoint and cross term retained. A guessed term such as

\[
6\frac{1-2^{-s}}{s+1}
\]

has no established relation to that arithmetic boundary and cannot be used in a proof.

## 4. What survives

This correction does not affect:

- the exact prime-annulus statistic of `L-27603`;
- the pole-preserving transform of `L-27602/T-27601`;
- the continuum/discrete scalar identity of `L-27604`;
- the equivalence `PAE <=> RH`;
- the full carry-position frame developed on PR #297.

It shows instead that averaging the carry-position variable before squaring loses the available positive frame geometry. The correct next object is the vector-valued atomized field, not a scalar Hardy factorization of its mean.

## 5. Proof boundary

Established exactly:

1. the correct Mellin factor (R-27601.3);
2. the negative value (R-27601.4);
3. failure of complete monotonicity;
4. failure of a single reflected-square factorization;
5. invalidity of an un-derived boundary completion.

Not refuted:

1. a sum-of-squares identity for the full carry-position matrix;
2. a coupled Selberg source matrix;
3. the atomized energy criterion;
4. RH.
