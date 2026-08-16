# Cubic prime shell and balanced dispersion after PR #498

Frozen predecessor:

```text
PR:       #498
head:     6cc0da2fa5711017e260ebdcea4ba8c22e453288
branch:   research/gpt56-pro/93250-centered-q4-cubic-closure
```

## Executive result

The centered Bernoulli/cubic route survives hostile reconstruction at its
analytic interfaces:

```text
finite endpoint identity                    verified
centered normalization                      verified
integer-to-real interpolation               verified
Mellin multiplier                           verified
open-strip pole survival                    verified
centered-energy/RH equivalence               verified
mean-free major-arc localization            verified on frozen Fourier inputs
```

The open CPBD statement has not been renamed.  It has been decomposed.

The new unconditional chain proves

\[
 \mathcal A_\circ(N)
 =
 \mathcal B_N
 +O\!\left(\sqrt N(\log(2N))^3\right),
\]

where

\[
 \mathcal B_N
 =
 \sum_{\substack{
 N^{1/3}<m,\ell\le N^{2/3}\\
 N^{3/4}<m\ell\le N
 }}
 \left(
 \sum_{\substack{d\mid m\\d>N^{1/3}}}\mu(d)
 \right)
 \Lambda(\ell)F(m\ell/N)
\]

and

\[
 F(x)=
 \begin{cases}
 170x^3-63x^2+5x,&x\le1/4,\\
 (-2x^3+3x^2-x)/3,&1/4<x\le1.
 \end{cases}
\]

Everything outside this explicit balanced near-hyperbola covariance is already
at square-root scale.

The Riemann Hypothesis remains unproved because the final BCD estimate is
RH-equivalent.

## 1. Hostile reconstruction

The exact projection is

\[
 \mathcal A_\circ(N)
 =\sum_{m\le N}c_\circ(m)K(m/N),
 \qquad
 K(x)=\frac{x(1-x)(2x-1)}3.
\]

The normalization is

\[
 |\mathcal A_\circ(N)|^2
 \le\frac N{180}\mathscr V_\circ(N).
\]

The Mellin transform is

\[
 \frac{s-1}{3(s+1)(s+2)(s+3)}
 \left[
 (1-4^{1-s})\left(-\frac{\zeta'}{\zeta}(s)\right)
 +3(\log4)\frac{4^{-s}}{1-4^{-s}}
 \right].
\]

No multiplier vanishes at a nontrivial zero.  Integer bounds extend to real
endpoints with \(O(1)\) loss.  Hence the centered criterion is a genuine
RH-equivalent theorem, not merely a heuristic projection.

## 2. Exact prime-shell reduction

After reindexing the contracted source,

\[
 \mathcal A_\circ(N)
 =
 \sum_{n\le N}\Lambda(n)F(n/N)
 +3(\log4)\sum_{4^r\le N}K(4^r/N).
\]

Every prime base \(p\le\sqrt N\), including its complete tower, has total
absolute contribution at most \(\log N\).  There are at most \(\sqrt N\) such
bases.  The gauge is logarithmic.  Therefore

\[
 \mathcal A_\circ(N)
 =
 \sum_{\sqrt N<p\le N}(\log p)F(p/N)
 +O(\sqrt N\log N).
\]

The RH-bearing object is a single large-prime shell, not an arbitrary family
of complete prime towers.

## 3. Two moments and discrete cancellation

The scale-four Mellin transform is

\[
 \widehat F(s)
 =(1-4^{1-s})
 \frac{s-1}{3(s+1)(s+2)(s+3)}.
\]

Therefore

\[
 \int F=0,
 \qquad
 \int F\log x=0,
 \qquad
 \int F(\log x)^2dx=\frac{\log4}{36}.
\]

The integer grid also has an exact mod-four law.  In particular,

\[
 \sum_{n=1}^{4h}F(n/(4h))=0.
\]

For the other three residue classes the complete rational remainders are
listed in `L-93302` and are \(O(1/M)\).

This is stronger than a continuous moment calculation and gives the
quadrature gain used in the Type-I estimates.

## 4. Vaughan reduction

With \(U=V=N^{1/3}\), the exact identity

\[
 \Lambda
 =
 \Lambda_{\le V}
 +\mu_{\le U}*\log
 -\mu_{\le U}*\Lambda_{\le V}*1
 +\mu_{>U}*\Lambda_{>V}*1
\]

is applied to the fixed wavelet.

The two-moment quadrature gives:

```text
small Lambda term                    O(N^(-1/3) log N)
mu*log Type I                        O(N^(-1/3) log N)
mu*Lambda*1 Type I                   O(N^(1/3) log N)
Type II with product <=N^(3/4)       O(sqrt(N) log^3 N)
```

After grouping \(m=dr\), the remaining coefficient is

\[
 a_U(m)=\sum_{\substack{d\mid m\\d>U}}\mu(d).
\]

Both variables lie between \(N^{1/3}\) and \(N^{2/3}\).  This is the first
point at which genuine Möbius--prime covariance is required.

## 5. Dispersion coordinates

The same hard form has two exact transforms.

### Additive

\[
 \mathcal T_N
 =
 \sum_{h\ne0}\widehat F_{\mathbb T}(h)
 \sum_{m,\ell}a_U(m)\Lambda(\ell)e(hm\ell/N),
 \qquad
 \widehat F_{\mathbb T}(h)\ll h^{-2}.
\]

The zero additive mode is absent.

### Mellin

\[
 \mathcal T_N
 =
 \frac1{2\pi}\int
 \widehat F(c+it)N^{c+it}
 A_U(c+it)L_U(c+it)\,dt.
\]

On the line \(c=1\), the multiplier vanishes quadratically at the zero carrier
and decays quadratically at remote carriers.

Neither identity supplies the required covariance estimate by itself.

## 6. First-Hermite connection

For

\[
 h_q(u)=\left(1-\frac{u^2}{2q}\right)e^{-u^2/(4q)},
\]

\[
 \widehat h_q(t)
 =4\sqrt\pi q^{3/2}t^2e^{-qt^2}.
\]

Writing

\[
 G(u)=e^{-u}F(e^{-u})\mathbf1_{u\ge0},
\]

one obtains the exact Calderón formula

\[
 G=\int_0^\infty
 \frac{h_q}{4\sqrt\pi q^{3/2}}*G\,dq.
\]

Thus the Q4 cubic wavelet is an exact continuous superposition of
First-Hermite heat derivatives.  This creates a real carrier-phase interface,
but it does not import the open First-Hermite one-carrier exclusion.

## 7. Exact remaining theorem

The sole conclusion-producing estimate is

\[
 |\mathcal B_N|
 \ll\sqrt N(\log N)^B.
\]

It is now fixed in:

```text
coefficients:  a_U(m), Lambda(l);
ranges:        N^(1/3)<m,l<=N^(2/3);
support:       N^(3/4)<ml<=N;
kernel:        the displayed piecewise cubic F.
```

This is materially narrower than CPBD and is suitable for a source-specific
bilinear dispersion campaign.  It remains RH-equivalent and has not been
proved in this packet.

## 8. Status

```text
PR #498 analytic spine                     VERIFIED
complete same-prime geometry               CLOSED
small prime bases and prime powers         CLOSED
double Mellin moment                       PROVED
exact mod-four grid cancellation           PROVED
all Type-I ranges                          CLOSED
low-product Type-II                        CLOSED
First-Hermite heat-wavelet bridge          PROVED
balanced cubic dispersion                  OPEN / RH-BEARING
Riemann Hypothesis                         UNPROVED
```
