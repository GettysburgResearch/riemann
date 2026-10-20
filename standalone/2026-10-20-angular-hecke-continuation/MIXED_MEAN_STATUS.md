# What the complete mixed mean would still require

Date: 2026-10-20. This is a record of the exact remaining target, not a
new moment theorem or a lower bound showing that target false.

## Source pins

PR #1006 head: `0c838d130f275efb6e8ddb81dab42462b4ce9454` in
`GettysburgResearch/riemann`, packet
`standalone/2026-10-18-three-direction-sprint/`.
The pinned consumer and completion analyses are the files
`eisenstein/MIXED_CONSUMER.md` and
`eisenstein/CONTINUOUS_COMPLETION_ATTEMPT.md` within that packet.

The original proof source is `openai/math` commit
`1581d4cbdd69a0faf34b2089614fe2a814316a6a`, file
`preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex`.
Its byte-exact SHA-256 is
`42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3`.

## Actual coefficients and the absent cancellation

With every original finite ray twist, height, and zero extension retained,
the normalized product is

\[
 M_u(D)S_u(N)=\sum_A c_A\chi_A(u)^{\varsigma},\qquad
 c_A=(DN)^{-1/2}\nu(A)
      \sum_{dn=A}\mu_E(d)W_M(Nd/D)W_S(Nn/N).
\]

There is no coprimality restriction between \(d,n\). A selected pair
of annular factors has the displayed restricted divisor sum; the
complete \(\mu*1\) identity cannot be applied again after the detector
has selected those annuli.

Writing \(n=h^2s\), then \(g=(d,s)\), \(d=ga\), \(s=gb\), gives
squarefree pairwise coprime \(g,a,b\); \(h\) remains unrestricted,
including primes shared with the other variables. The exterior square
factor is \((gh)^2\). On the squarefree product \(ab\), the source
Gauss identities can move the long inverse sign to the short divisor,
leaving a coherent mark

\[
 \sum_{b\mid A}\mu_E(b)W_S(Nb/N)W_M(NA/(D\,Nb))
\]

on a canonical angular Gauss coefficient. The licensed unmarked
canonical mean does not supply a coherent arbitrary-divisor version.
The new angular Type-I estimate in [ANGULAR_TYPE_I.md](ANGULAR_TYPE_I.md) bounds an exact
cubic Gauss block with such a short mark, but the remaining quadratic
row component and its averaging still need a separate argument.

## The full polygon is harder than its popular corner

Put \(D=U^r\), \(N=U^m\),

\[
 1\le r\le3/2,\quad0\le m\le1/2,\quad3/2\le r+m\le2.
\]

The consumer asks for a complete \(U^{6/5+\varepsilon}\) mean over
this polygon, including fixed robust neighborhoods. With
\(\kappa=2\beta-1\), the existing pure inverse exponent is

\[
 e(r)=\max\{1,(1+5r)/6\}.
\]

Using the pure inverse second moment, the plain fourth moment, and the
two pointwise bounds gives the available upper-bound exponent

\[
 E_{\rm known}(r,m)=\min\{e(r)+\kappa m,
                      (1+e(r)+\kappa r)/2\}.
\]

At \(\beta=7/8\), the corner \((r,m)=(1,1/2)\) gives \(11/8\),
whose excess over \(6/5\) is \(7/40\). But the pure inverse edge
\((3/2,0)\) already gives \(17/12\), an excess of \(13/60\).
At \((3/2,1/2)\), the available bound is \(85/48\), with excess
\(137/240\). Replacing \(7/8\) by \(B_\flat\) only changes this
last exponent to approximately \(1.77066330389328\).
These are gaps in the available upper bounds, not lower bounds on the
true moments.

## A smaller, precisely located gain that could matter

In the relaxed consumer at \(B=437/500\), \(\ell=6/35\), balanced
lengths \(29/70\), amplitude parameter \(x=1/2\), and
\(\delta=0.469\), the source count is approximately
\(R=0.59066709\), while the target is \(0.57842138\).
The binding long inverse cutoff is \(t\approx1.16377060\).
An improvement of roughly \(0.01225\) in its native exponent
\((1+5t)/6\) would resolve that one binding count.
This numerical localization does not cover the continuous consumer
or prove any improved mean. It identifies a smaller source-level target
than demanding \(U^{6/5}\) uniformly on the whole polygon.
