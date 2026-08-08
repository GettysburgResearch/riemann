# L-32307 — Positive critical digital dual for the critical-null source

Claim ID: `L-32307`  
Title: A positive geometric dyadic lift of the binary-digit dual has nonnegative summatory values and collapses the critical-null source to the same three boundary atoms  
Status: **PROPOSED COMPLETE EXACT LEMMA — independent review requested**  
Authoring agent: `gpt56-pro-xhigh`  
Created: 2026-08-08  
Dependencies: PR #268 `L-26202`; `L-32302/L-32305`  
Scope: exact digital/source algebra; no coercivity or RH conclusion

## 1. Old binary-digit dual

PR #268 uses

\[
c_2(n)=1-v_2(n)
\]

with exact summatory identity

\[
\boxed{
C_2(N):=\sum_{n\le N}c_2(n)=s_2(N)\ge0,
}
\tag{L-32307.1}
\]

where `s_2(N)` is the binary digit sum. It satisfies

\[
\boxed{
 c_2*\omega_2
 =\varepsilon-{5\over2}\delta_2+\delta_4.
}
\tag{L-32307.2}
\]

## 2. Critical geometric lift

Define the positive dyadic geometric sequence

\[
\boxed{
 g_{1/2}=\sum_{j\ge0}2^{j/2}\delta_{2^j}.
}
\tag{L-32307.3}
\]

Coefficientwise every finite integer sees only finitely many terms, and

\[
\boxed{
 g_{1/2}*(\varepsilon-\sqrt2\,\delta_2)=\varepsilon.
}
\tag{L-32307.4}
\]

Define the critical digital dual

\[
\boxed{
 d_\dagger=c_2*g_{1/2}.
}
\tag{L-32307.5}
\]

Since

\[
\omega_\dagger
=(\varepsilon-\sqrt2\delta_2)*\omega_2,
\]

associativity and (L-32307.2)--(L-32307.4) give the exact finite-output identity

\[
\boxed{
 d_\dagger*\omega_\dagger
 =\varepsilon-{5\over2}\delta_2+\delta_4.
}
\tag{L-32307.6}
\]

Thus inserting the critical-null factor does not enlarge the digital forcing support at all.

## 3. Exact nonnegative summatory function

Let

\[
D_\dagger(N)=\sum_{n\le N}d_\dagger(n).
\]

Using (L-32307.5) and finite reindexing,

\[
\begin{aligned}
D_\dagger(N)
&=\sum_{j\ge0}2^{j/2}
  \sum_{m\le N/2^j}c_2(m)\\
&=\boxed{
\sum_{0\le j\le\lfloor\log_2N\rfloor}
2^{j/2}s_2\!\left(\left\lfloor{N\over2^j}\right\rfloor\right).
}
\end{aligned}
\tag{L-32307.7}
\]

Every summand is nonnegative. Hence

\[
\boxed{
D_\dagger(N)\ge0
\qquad(N\ge1).
}
\tag{L-32307.8}
\]

The coefficient sequence `d_dagger` itself need not be nonnegative; the exact positivity is at the summatory level required by the causal digital kernel.

## 4. Critical size bounds

Since

\[
1\le s_2(m)\le1+\log_2m
\qquad(m\ge1),
\]

one obtains the elementary upper bound

\[
\begin{aligned}
D_\dagger(N)
&\le
\sum_{j\le\log_2N}2^{j/2}
\left(1+\log_2N-j\right)\\
&\le C\sqrt N
\end{aligned}
\tag{L-32307.9}
\]

for one absolute constant `C`: set `J=floor(log_2 N)` and write `j=J-r`; the series becomes `sqrt(N)` times a convergent sum of `(1+r)2^{-r/2}`.

On the other hand the last term `j=J` has

\[
s_2(\lfloor N/2^J\rfloor)=1,
\]

and `2^J>N/2`. Therefore

\[
\boxed{
\sqrt{N/2}<D_\dagger(N)\le C\sqrt N.
}
\tag{L-32307.10}
\]

The digital dual is exactly critical-order rather than integrable-order. This is expected: it inverts the deliberately inserted square-root critical zero.

## 5. Positive causal kernel

Define

\[
\boxed{
S_\dagger(t)
=e^{-t/2}D_\dagger(\lfloor e^t\rfloor),
\qquad t\ge0.
}
\tag{L-32307.11}
\]

Then

\[
S_\dagger(t)\ge0
\]

and (L-32307.10) gives uniform two-sided boundedness away from zero and infinity for large `t`, up to absolute constants.

Between integer knots, `S_dagger'=-S_dagger/2`; its jump at `t=log n` is `d_dagger(n)/sqrt n`. Thus, in distributions,

\[
\boxed{
\left(\partial_t+{1\over2}\right)S_\dagger
=\sum_{n\ge1}{d_\dagger(n)\over\sqrt n}\delta_{\log n}.
}
\tag{L-32307.12}
\]

Let

\[
\beta_\dagger
=\sum_{n\ge1}{\omega_\dagger(n)\over\sqrt n}\delta_{\log n}.
\]

The normalized convolution of (L-32307.6) gives

\[
\boxed{
\left(\partial_t+{1\over2}\right)
(S_\dagger*\beta_\dagger)
=\delta_0-{5\over2\sqrt2}\delta_{\log2}+{1\over2}\delta_{2\log2}.
}
\tag{L-32307.13}
\]

The causal output is therefore the same explicit three-tap exponential profile as for the older `omega_2` source; only the positive kernel on the left has changed.

## 6. Interpretation

The critical-null source now has four mutually compatible exact faces:

```text
finite carry face: rows 2,...,7;
positive generalized Selberg forcing;
closed-strip inverse-zeta source;
positive critical digital kernel S_dagger.
```

The positive kernel is not `L^1`; its nondecaying critical size is the exact analytic footprint of the neutral square-root mode. Therefore (L-32307.13) is not by itself an invertible positive convolution theorem and does not prove the six-row sign criterion.

What it does close is the digital compatibility of the new source without reintroducing an unsigned approximation.

## 7. Proof boundary

Closed exactly:

- critical geometric inverse;
- finite three-atom digital forcing;
- explicit nonnegative summatory formula;
- critical `Theta(sqrt N)` size;
- positive causal kernel and distributional convolution.

Open:

- source-specific coercivity or one-sided inversion of this critical positive kernel;
- CNSB / eventual six-row sign;
- RH.
