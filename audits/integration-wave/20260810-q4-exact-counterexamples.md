# Exact review counterexamples for the Q4 reflected–Jordan lineage

**Review cutoff:** `2026-08-10T22:00:51Z`  
**Purpose:** retain exact, lightweight review artifacts without editing
or rewriting the submitted theorem files.

## REV-Q4-01 — The #346 coefficient budget is not the #359 operator contraction

### Submitted use

PR #359 invokes the inertia-tolerant synthesis lemma with a hypothesis
of the form

\[
W^*W\le qI,\qquad q<\frac25,
\]

and cites the finite synthesis budget from PR #346. The #346 quantity
is a weighted sum of coefficient energies divided by the parity-frame
reserve \(45/4\). It is not the pointwise operator norm of the
frequency response.

### Exact witness

For the submitted finite filters \(W_+\) and \(W_-\), evaluate on the
critical-line radius at

\[
z=\frac1{\sqrt2}.
\]

Direct exact simplification gives

\[
\begin{aligned}
S
&=|W_+(z)|^2+|W_-(z)|^2\\
&=
\frac{751606691}{24000000}
-
\frac{277818163}{18000000}\sqrt2\\
&\approx 9.48948912565671182875.
\end{aligned}
\]

In particular,

\[
S-\frac25
=
\frac{2226020073-1111272652\sqrt2}{72000000}.
\]

Both integers are positive, and

\[
\begin{aligned}
2226020073^2-2(1111272652)^2
&=2485311551232699121\\
&>0.
\end{aligned}
\]

Therefore

\[
2226020073>1111272652\sqrt2
\]

and hence \(S>2/5\).

### Verdict

The claim that the retained #346 coefficient budget supplies the #359
hypothesis \(W^*W\le qI\), \(q<2/5\), is **FALSE**. This does not
refute the exact #346 Bézout identity or its true joint jet-frame
inequality. It refutes only the operator-norm promotion used in the
#359 full composition.

## REV-Q4-02 — A bounded nonconstant multiplier does not transfer integrated inertia masses

### Submitted use

PR #357 `L-90308.12` uses

\[
M(t)=\frac1{1-\frac12e^{-it\log4}}
\]

and \(\|M\|_\infty\le2\) to assert factor-four transfers for positive
and negative spectral masses of an integrated indefinite curvature.

A constant multiplier would preserve cancellation up to scale. A
nonconstant multiplier does not.

### Exact construction

Let

\[
T=\frac{\pi}{\log4}.
\]

Choose a nonzero real smooth bump \(a\) supported in a sufficiently
small interval about \(0\), and define its translate

\[
b(t)=a(t-T).
\]

Choose the support small enough that \(a\) and \(b\) are disjoint.
They have equal \(L^2\) norm.

Define the twice differentiable scalar path

\[
d_\tau(t)
=
a(t)+b(t)
+\frac{\tau^2}{2}\{-a(t)+b(t)\}.
\]

At \(\tau=0\),

\[
d_0=a+b,\qquad d'_0=0,\qquad d''_0=-a+b.
\]

For scalar Jordan curvature

\[
K(d)=|d'|^2-\operatorname{Re}(d\overline{d''}),
\]

disjointness gives

\[
K(d)_0=|a|^2-|b|^2.
\]

Consequently,

\[
\int_{\mathbb R}K(d)_0\,dt
=
\|a\|_2^2-\|b\|_2^2
=0.
\]

Now multiply the whole path by \(M\). Since \(M\) is independent of
\(\tau\),

\[
K(Md)_0=|M|^2K(d)_0.
\]

Moreover,

\[
|M(t)|^2
=
\frac1{5/4-\cos(t\log4)}.
\]

For \(t\) near zero,

\[
\begin{aligned}
|M(t+T)|^2
&=
\frac1{5/4-\cos(t\log4+\pi)}\\
&=
\frac1{5/4+\cos(t\log4)}\\
&<
\frac1{5/4-\cos(t\log4)}
=
|M(t)|^2.
\end{aligned}
\]

Because \(b\) is the exact translate of \(a\),

\[
\int |M|^2|a|^2\,dt
>
\int |M|^2|b|^2\,dt.
\]

Therefore

\[
\int K(Md)_0\,dt>0
\]

although the original integrated curvature is exactly zero. Replacing
\(-a+b\) by \(a-b\) reverses the sign and gives a strictly negative
weighted curvature from the same zero unweighted curvature.

The construction embeds diagonally in any two-state Hermitian path, so
it also refutes the corresponding matrix positive/negative mass
transfer.

### Verdict

The factor-four positive- and negative-mass transfers in
`L-90308.12` are **FALSE** under the stated bounded-multiplier
hypothesis. The exact source/filter dictionary around that statement
may survive. A replacement theorem must use additional source-specific
structure or compare pointwise positive/negative densities before
integration; an \(L^\infty\) norm bound alone is insufficient.

## Scope and computation statement

These are exact finite algebra / smooth-bump arguments. No heavy
experiment, endpoint scan, interval campaign, optimization sweep, or
formal build was run.
