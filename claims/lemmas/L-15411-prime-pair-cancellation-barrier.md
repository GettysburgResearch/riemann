# L-15411 — A positive proof must cancel a quadratic diagonal prime energy

Claim ID: `L-15411`  
Title: Bounded mean square requires order-`X^2` off-diagonal cancellation in the triangular prime window  
Status: `PROPOSED`  
Authoring agent: `gpt56-05-l`  
Created: 2026-07-31  
Dependencies: `L-15409`; the prime number theorem with a classical remainder sufficient for weighted partial summation  
Scope: obstruction and exact target for prime-side mean-square proofs  
Related counterexample candidates: none

## Mean-square expansion

Let

\[
 Q_h(x)=\sum_n a_nG_h(x-\log n),
 \qquad
 a_n=\frac{\Lambda(n)}{\sqrt n},
 \tag{L-15411.1}
\]

where `G_h` is the triangular pole-free window and `h=log 4`. For fixed `x_0`
and `X>0`, write

\[
 M_h(X)=\int_{x_0}^{x_0+X}|Q_h(x)|^2dx.
 \tag{L-15411.2}
\]

Expanding the finite sum at each `x` gives

\[
\boxed{
 M_h(X)=
 \sum_{m,n\ge2}
 \frac{\Lambda(m)\Lambda(n)}{\sqrt{mn}}
 \mathcal K_X(\log m,\log n),}
 \tag{L-15411.3}
\]

where

\[
 \mathcal K_X(u,v)=
 \int_{x_0}^{x_0+X}G_h(x-u)G_h(x-v)dx.
 \tag{L-15411.4}
\]

Only pairs with

\[
 |\log(m/n)|\le3h
 \tag{L-15411.5}
\]

contribute. Thus the positive route is a fixed-ratio prime-power correlation
problem.

## Diagonal asymptotic

The diagonal part is

\[
 D_h(X)=
 \sum_n\frac{\Lambda(n)^2}{n}
 \int_{x_0}^{x_0+X}G_h(x-\log n)^2dx.
 \tag{L-15411.6}
\]

`L-15409` gives

\[
 \|G_h\|_2^2=\frac8{3h}.
 \tag{L-15411.7}
\]

Weighted partial summation and the prime number theorem give

\[
 \sum_{n\le e^Y}\frac{\Lambda(n)^2}{n}
 =\frac12Y^2+O(Y).
 \tag{L-15411.8}
\]

In fact the higher prime powers contribute `O(1)`, and the standard
zero-free-region PNT remainder gives a bounded error in the prime part after the
main integral; the displayed `O(Y)` is deliberately conservative.

All terms whose logarithms stay at least `3h` from the two integration
endpoints contribute their full `L2` norm. The two boundary layers have fixed
logarithmic width and contribute `O_h(X)`. Therefore

\[
\boxed{
 D_h(X)=\frac4{3h}X^2+O_{h,x_0}(X).}
 \tag{L-15411.9}
\]

## Required off-diagonal cancellation

Let

\[
 O_h(X)=M_h(X)-D_h(X)
 \tag{L-15411.10}
\]

be the sum over `m!=n`. If the positive target

\[
 M_h(X)=O(X)
 \tag{L-15411.11}
\]

holds, then necessarily

\[
\boxed{
 O_h(X)=-\frac4{3h}X^2+O(X).}
 \tag{L-15411.12}
\]

Thus the off-diagonal prime-power correlations must cancel the complete
quadratic diagonal energy to relative precision `O(1/X)`.

This is not a small technical correction. Any argument that:

- drops cross terms;
- applies absolute values term by term;
- replaces the signed window by its modulus;
- bounds prime powers independently;
- uses only an `L1` or total-variation estimate;

cannot establish the desired mean square.

## Autocorrelation form away from endpoints

Define

\[
 C_h(r)=\int_{\mathbb R}G_h(u)G_h(u+r)du.
 \tag{L-15411.13}
\]

For pairs whose two translated supports lie inside the integration interval,

\[
 \mathcal K_X(\log m,\log n)
 =C_h(\log(m/n)).
 \tag{L-15411.14}
\]

Hence, up to the two fixed-width boundary ledgers, the target is the signed
pair-correlation estimate

\[
\boxed{
 \sum_{
 \substack{m,n\text{ in the active range}\\
            |\log(m/n)|\le3h}}
 \frac{\Lambda(m)\Lambda(n)}{\sqrt{mn}}
 C_h(\log(m/n))=O(X).}
 \tag{L-15411.15}
\]

The kernel `C_h` is an explicit compact piecewise cubic function. It can be
integrated and range-certified exactly after scaling by `h`.

## Fourier interpretation

The autocorrelation transform is

\[
 \widehat C_h(t)=|\widehat G_{h,L}(it)|^2\ge0.
 \tag{L-15411.16}
\]

Under RH, the pair cancellation is reorganized by the explicit formula into the
finite Bohr variance

\[
 2\sum_{\gamma>0}m_\gamma^2
 |\widehat G_{h,L}(i\gamma)|^2.
 \tag{L-15411.17}
\]

Prime-side cancellation and zero-side positivity are therefore two spectral
representations of the same energy.

## Relation to known PNT mean squares

Classical critical mean-square bounds for `psi(x)-x` are proved under RH and
are known to become unbounded if RH is false. The present logarithmic,
fixed-ratio smoothed statistic has the same pole obstruction but a finite exact
window and a convergent boundary variance.

The diagonal calculation explains why ordinary probabilistic independence is
misleading: a diagonal or Poisson model predicts growth, while the true
RH-scale signal is produced by highly structured negative off-diagonal
correlation.

## Positive proof interface

A successful prime-side proof may certify (L-15411.15) through one of:

1. a new Selberg-symmetry identity retaining the signed autocorrelation kernel;
2. a Hilbert-space factorization whose norm is independent of the terminal
   support;
3. a matrix/system ground-state representation preserving the phase channels;
4. a direct Hardy/Carleson estimate equivalent to `T-15406.5`.

The cancellation must appear explicitly in the proof object. It cannot be
hidden inside an absolute error term of order larger than `X`.

## Gap audit

- Formula (L-15411.9) uses a standard weighted PNT asymptotic; an explicit
  version should cite and bind one concrete remainder theorem.
- The boundary ledger depends on `x_0` but not on the cofinal quadratic term.
- An empirical pair sum over finitely many supports is not a cofinal estimate.
- This lemma proves a necessity/barrier, not the required cancellation theorem.
