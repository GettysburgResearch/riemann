# Hostile continuation of PR #498: minimal-switch cubic dispersion

## Executive verdict

PR #498 remains frozen and its centered cubic equivalence survives independent
reconstruction. One displayed large-modulus inequality requires the harmless
replacement `a -> min(a,N-a)`.

No unconditional RH proof is obtained. The pass nevertheless changes the
arithmetic frontier in four substantive ways:

1. all proper prime powers and the four-adic gauge are removed at
   `O(sqrt(N) log^2 N)`, leaving one ordinary-prime scalar;
2. the Q4 kernel is proved to have the minimum possible two sign changes among
   nontrivial scalar kernels with both required `s=1` moments zero;
3. the signed cubic is the second logarithmic derivative of one explicit
   positive compact Peano kernel, producing a nonnegative prime potential with
   unconditional PNT limit `log(4)/72`;
4. the exact `Lambda=mu*log` hyperbola split pays every Mobius divisor
   `d<=sqrt(N)` unconditionally, leaving only one large-divisor tail with an
   elementary forcing of size `O(log Y/Y)`.

A critical radix-four Abel transform gives a one-switch kernel, but the pass
proves why this does not close the problem: one switch necessarily spends the
second Mellin zero and restores a macroscopic forcing term.

## Frozen genealogy

```text
base PR:      #498
base SHA:     6cc0da2fa5711017e260ebdcea4ba8c22e453288
new branch:   research/gpt56-pro/93260-minimal-switch-cubic-dispersion
```

## Corrected analytic spine

The centered scalar is

\[
A_circ(N)=\sum c_circ(m)K(m/N),
\qquad
K(x)=x(1-x)(2x-1)/3.
\]

Its normalization, Mellin multiplier, interpolation, and pole survival all
replay. In the two-sided Fourier major arc, the reduced modulus must be written

\[
q=N/(d_N(a),N),\qquad d_N(a)=\min(a,N-a),
\]

not bounded using `N/a` when `a` is near `N`.

## Prime-only normal form

With

\[
W(x)=K(x)-4K(4x),
\]

one has

\[
A_circ(N)=\sum_{p<=N}(\log p)W(p/N)
+O(\sqrt N\log^2N).
\]

The kernel is positive, then negative, then positive, with sign changes at

\[
(63-\sqrt{569})/340
\quad\text{and}\quad 1/2.
\]

Its Mellin transform has an exact double zero at one. A general rearrangement
argument proves that a nontrivial one-switch kernel cannot have both zero
moments. Hence this two-switch geometry is scalar-minimal, not an arbitrary
choice of cubic.


## Positive potential normal form

Define

\[
\Phi(x)=
\begin{cases}
x^2(85x^2-56x+10)/8,&0\le x\le1/4,\\
(1-x)^3(3x+1)/72,&1/4\le x\le1,\\
0,&x\ge1.
\end{cases}
\]

Then `Phi>=0` and, with `D=x d/dx`,

\[
D^2\Phi=xW.
\]

Consequently

\[
\mathcal U_\Lambda(X)
=\sum_{n\le X}{\Lambda(n)\over n}\Phi(n/X)\ge0,
\qquad
X(X\partial_X)^2\mathcal U_\Lambda(X)=\mathcal L_W(X).
\]

The Mellin transform of `Phi` is

\[
{1-4^{-s}\over3s(s+2)(s+3)(s+4)},
\]

and PNT gives the unconditional limit

\[
\mathcal U_\Lambda(X)\to\log(4)/72.
\]

This is a genuinely new positive observable, but positivity alone supplies no
RH-scale convergence rate. An off-line zero remains a nonremovable pole in
the transform of the error.

## Critical Abel compression and its firewall

The critical future sum

\[
\sum_{j>=0}4^{-j}A_odd(4^jN)
\]

telescopes to the one-switch kernel

\[
J(x)=-4K(4x)
={16\over3}x(1-4x)(1-8x),
\qquad 0<=x<=1/4.
\]

Its cumulative is the positive square

\[
\int_0^xJ(u)du={8\over3}x^2(1-4x)^2.
\]

But `Jhat` has only a simple zero at one. The packet proves that every finite
one-sign scale filter is trivial and every convergence-compatible geometric
future filter stays sign-changing. This rules out a false positivity proof.

## Large-divisor localization

Define

\[
F_W(Y)=\sum_{m<=Y}(\log m)W(m/Y).
\]

The double Mellin zero gives

\[
F_W(Y)=O((1+\log Y)/Y).
\]

Since `Lambda=mu*log`, exactly

\[
\sum_{n<=X}\Lambda(n)W(n/X)
=
\sum_{d<=X}\mu(d)F_W(X/d).
\]

Every divisor `d<=sqrt(X)` contributes only `O(log X)` in total. Therefore the
complete RH burden is

\[
\sum_{\sqrt X<d<=X/2}\mu(d)F_W(X/d).
\]

This is a genuine producer reduction, not a restatement of prime-block
coherence. It exposes the exact cancellation that a future bilinear or
large-divisor dispersion argument must prove.

## Scientific boundary

```text
PR #498 analytic spine                     SURVIVES
large-modulus display                      CORRECTED
prime powers and four-adic gauge           PAID
minimal two-switch theorem                 PROVED
positive compact prime potential           PROVED / PNT LIMIT
one-switch/double-zero scalar shortcut     REFUTED
small Mobius divisors                       PAID
large-divisor Mobius cancellation          OPEN
First-Hermite one-carrier exclusion        OPEN
Riemann Hypothesis                         UNPROVED
```
