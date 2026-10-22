# Ambitious continuation — reverse Bessel, Hausdorff, Euler dilation, and Jordan–Loewner flow

Date: 2026-08-11  
Agent: `gpt56-pro`  
Continuation of: draft PR #389  
Status: research deposit; **RH remains unproved**

## Executive outcome

The previous continuation reduced the terminal Gaussian/resolvent programmes to
one hierarchy of safe-line scalars indexed by `k`. This pass refuses to treat
those inequalities independently.

The hierarchy closes into one coherent object in four mutually reinforcing
languages:

```text
reverse Bessel polynomials;
Hausdorff moments on [0,1];
a positive Euler–Bessel two-copy Hilbert dilation;
a compound-Poisson Jordan / de Branges–Loewner evolution.
```

The strongest exact localization is an **analytic one-quarter gap**. Borel
Poissonization uses a parameter `0<=u<1`. The scalar is computable by one
absolutely convergent Euler series for `u<3/4`; every possible false-RH pole lies
in `3/4<u<1`. The entire unresolved problem has therefore been compressed into
transporting a positive Pick/Hausdorff structure across one fixed interval.

## I. Reverse Bessel closure

The order polynomials satisfy

\[
Q_k(t)=\theta_{k+1}(t)-t^2\theta_k(t),
\]

where `theta_n` is the reverse Bessel polynomial. Their EGF is

\[
\sum P_k(t)u^k/k!
=\frac{e^{t(1-\sqrt{1-u})}}{2\sqrt{1-u}}
 \left[(1-u)^{-1}+t(1-u)^{-1/2}-t^2\right].
\]

After the native `n^{-3/2}` factor the sign boundary is exactly

\[
\sqrt{1-u}\log n=\varphi.
\]

Equivalently, `P_k` is a centered moment of a Gamma plus inverse-Gaussian
subordinator. This gives an infinite stochastic replacement for the finite
Brownian approximants killed by Bohr instability.

## II. Borel and Hausdorff closure

The Borel sum of the zero kernel is

\[
\sum_k\kappa_k(z)u^k/k!
=-4z^2/(1-z^2-u)^3.
\]

Under RH it is a positive sum of cubic resolvents. A false-RH pair of depth `y`
creates a negative pole at `u=1-y^2 in (3/4,1)`.

After normalization by `(k+2)!`, the discrete hierarchy is a Hausdorff moment
sequence on `[0,1]`. Thus RH is equivalent to all:

```text
alternating finite differences;
Hankel PSD;
[0,1]-localizing PSD;
positive Jacobi parameters;
Stieltjes/Padé poles on [1,infinity).
```

This is a compact moment problem, not a list of unrelated inequalities.

## III. Positive Euler–Bessel dilation

For each prime log `t`, the signed weight has the GIG realization

\[
e^{-t}P_k(t)=\int q^k(q-t^2/2)d\nu_t(q).
\]

The localizer

\[
P_{k+1}(t)-t^2P_k(t)/2
\]

is strictly positive for every `t,k`. More strongly, all its Hankel matrices are
Gram matrices.

Taking a direct sum over prime powers realizes the complete prime contribution
as the cross block `C=<U,V>` of a positive matrix

\[
\begin{pmatrix}M&C\\C^*&N\end{pmatrix}\succeq0.
\]

The prime oscillation is therefore already a contraction between two canonical
positive feature spaces. The missing theorem is an archimedean/pole Schur
completion through the continuation gap.

## IV. Jordan–Loewner flow

The quotient

\[
R_u(s)=\zeta(s-u)/\zeta(s)
\]

has generalized Jordan coefficients `J_u(n)>=0`; on a safe vertical line its
normalization is compound Poisson on the prime-log semigroup. The completed
transport

\[
\Theta_u(s)=\xi(s-u)/\xi(s)
\]

has generator `-xi'/xi`, boundary modulus one on
`Re(s)=(1+u)/2`, and is a Schur flow under RH. Its safe one-Green specialization
is exactly the older unconditional positive kernel `L-9506`.

Thus the new target is a Loewner continuation theorem:

```text
positive compound-Poisson / one-Green feature kernel on the safe side
  -> positive de Branges–Rovnyak kernel in the moving half-plane.
```

That theorem is equivalent to RH; it is not supplied.

## Exact frontier

```text
reverse-Bessel and inverse-Gaussian closure       PROPOSED COMPLETE EXACT
Borel cubic resolvent                             PROPOSED COMPLETE EXACT
Hausdorff/Hankel/localizing RH criterion          PROPOSED COMPLETE
one-quarter safe-Euler continuation gap           EXACT
prime Euler–Bessel positive dilation              PROPOSED COMPLETE EXACT
Jordan compound-Poisson envelope                  EXACT
completed horizontal cocycle and generator        EXACT
Schur-flow RH equivalence                         PROPOSED / ANALYTIC REVIEW
positive continuation across the gap              OPEN / RH-EQUIVALENT
Riemann Hypothesis                                UNPROVED
```

## Why this is more ambitious than criterion proliferation

The Anthropic campaign’s decisive moves came from reversing a failed statistic
and preserving the indefinite structure rather than imposing false positivity.
This continuation applies the same lesson again:

- the signed `P_k` weights are not bounded termwise;
- they are lifted as a cross Gram block;
- all orders are not checked separately;
- they are one compact Hausdorff measure;
- the Euler series is not pushed past convergence by absolute values;
- it is embedded in a positive Jordan/Loewner transport.

The next attack should be on the single Schur-completion theorem, with
Davenport--Heilbronn, Epstein, and planted Beurling controls built in from the
start.
