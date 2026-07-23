# L-2802 — Universal high-carrier correction budget

Claim ID: L-2802  
Title: A rational high-carrier bound for all omitted D-0801 archimedean and pole corrections  
Status: PROPOSED  
Authoring agent: `gpt56-04-c`  
Reviewing agents: none  
Created: 2026-07-23  
Last updated: 2026-07-23  
Dependencies: L-2801; elementary Fourier and digamma estimates  
Scope: equal-cell D-0801 carriers with `c=10^n`  
Related counterexample candidates: any future fixed-vector carrier witness

## Statement

Let `n>=1`, `c=10^n`, `L=log(c)`, and let `g_{T,v}` be D-0801 with `K` equal
cells and

\[
 \sum_{j=0}^{K-1}|v_j|^2=1.
\]

Assume

\[
 T\ge10,\qquad 2K<nT.
\]

Set

\[
 \alpha(T)=\frac{\log(T/(2\pi))}{2\pi}.
\]

For a positive real `x`, let `bit(x)` mean the binary bit length of
`ceil(x)`. Define

\[
 b_0=\operatorname{bit}\!\left(\frac{3nT}{4K}\right),\qquad
 b_1=\operatorname{bit}(T),\qquad
 b_2=\operatorname{bit}(3T/2),
\]

and

\[
 s=\left\lceil\sqrt{10^n}\right\rceil.
\]

Put

\[
 M=\frac{K^2}{3n}(1+2b_0),
\]

\[
 E_{\rm central}=\frac{2M}{3T},
\]

\[
 E_{\rm tail}=\frac{2K^2}{9nT}
 \left(30+2b_2+2b_1\right),
\]

\[
 E_{\rm point}=\frac1T,
 \qquad
 E_{\rm pole}=\frac{2K^2s}{3nT^2},
\]

and

\[
 E=E_{\rm central}+E_{\rm tail}+E_{\rm point}+E_{\rm pole}.
\]

Then, conditional only on the source normalization stated in L-2801,

\[
 \boxed{
 \left|
 \frac{\mathcal A(g_{T,v})+\mathcal R(g_{T,v})}{h}
 -\alpha(T)
 \right|<E.}
\]

Every quantity defining `E` is rational once `T` is rational. No special
function, prime, phase, floating-point operation, or numerical quadrature is
needed to check it.

### PR #44 parameter corollary

For

\[
 n=11,\qquad K=1024,
 \qquad T=4709203636353.65=\frac{94184072727073}{20},
\]

X-2801 computes exactly

\[
 E=
 \frac{98759175269343099756340}
 {79835755999127184820324325961}
 <\frac1{750000}
 \approx1.33334\times10^{-6}.
\]

The exact decimal value of the rational bound is approximately

\[
 1.2370293741\times10^{-6}.
\]

Thus a directed prime-side leading-margin interval with lower endpoint greater
than `1/750000` would prove that the complete exact D-0801 value at these
parameters is positive. A leading interval with upper endpoint below
`-1/750000` would prove a complete negative exact value, subject to the broader
normalization audit.

PR #44's ordinary-floating leading margin is about
`2.6896626427e-4`, more than 217 times this correction budget, but that decimal
is not a directed interval and is therefore not promoted here.

## Proof

### 1. Probability representation

Let

\[
 W_v(u)=\int_Iw_v(x)e^{2\pi iux}\,dx.
\]

Parseval and the coefficient normalization give

\[
 \int_{\mathbb R}|W_v(u)|^2du=h.
\]

Hence

\[
 d\mu_v(u)=\frac{|W_v(u)|^2}{h}\,du
\]

is a probability measure. Because `H` is even and D-0801 symmetrizes the two
carrier lobes, L-2801 is equivalently

\[
 \frac{\mathcal A(g_{T,v})}{h}
 =\frac1{2\pi}\int_{\mathbb R}H(T+u)\,d\mu_v(u).
\]

### 2. Uniform Fourier bounds

The compactly supported step function `w_v` satisfies

\[
 \|w_v\|_1\le\sqrt{\Delta h}=\frac{\Delta}{\sqrt K}.
\]

Its distributional total variation, including the two support endpoints, is
bounded by

\[
 |v_0|+\sum_{j=1}^{K-1}|v_j-v_{j-1}|+|v_{K-1}|
 \le2\sum_j|v_j|\le2\sqrt K.
\]

Integration by parts in the Fourier transform therefore yields

\[
 |W_v(u)|\le
 \min\left\{\frac{\Delta}{\sqrt K},
             \frac{\sqrt K}{\pi|u|}\right\}.
\]

The two bounds meet at

\[
 u_0=\frac{K}{\pi\Delta}=\frac{2K}{L}.
\]

Since `log(10)>2`, one has `L>2n`; the hypothesis `2K<nT` implies
`u_0<T/2`.

It follows that

\[
 \int_{|u|\le T/2}|u|\,d\mu_v(u)
 \le\frac{2K^2}{\pi L}
 \left[1+2\log\left(\frac{TL}{4K}\right)\right].
\]

Using `pi>3`, `L>2n`, `L<3n`, and

\[
 \log x<\operatorname{bit}(x)\qquad(x\ge1),
\]

this is strictly below `M` in the statement. The logarithm/bit inequality
uses only `log(2)<1`.

### 3. Digamma derivative and point estimates

For `a=1/4`, `y=r/2`, the trigamma series gives

\[
 |H'(r)|
 \le\frac12\sum_{m=0}^\infty
 \frac1{(m+a)^2+y^2}
 \le\frac2{r^2}+\frac\pi{2r}.
\]

For `r>=T/2` and `T>=10`, the right side is less than `4/T`.
Consequently the contribution of `|u|<=T/2` to

\[
 \frac1{2\pi}\int|H(T+u)-H(T)|\,d\mu_v(u)
\]

is at most `E_central`.

Binet's formula in the half-plane `Re(z)>0` is

\[
 \psi(z)=\log z-\frac1{2z}
 -2\int_0^\infty
 \frac{t\,dt}{(t^2+z^2)(e^{2\pi t}-1)}.
\]

For `z=1/4+iT/2`,

\[
 |t^2+z^2|\ge2(1/4)(T/2).
\]

Together with

\[
 \int_0^\infty\frac{t}{e^{2\pi t}-1}\,dt=\frac1{24},
\]

this gives the deliberately coarse bound

\[
 \frac1{2\pi}
 \left|H(T)-\log(T/(2\pi))\right|<\frac1T=E_{\rm point}.
\]

### 4. Remote Fourier tail

The convergent digamma series gives the global estimate

\[
 |H(r)|\le14+2\log(1+|r|/2).
\]

For completeness, choose `N=ceil(max(1,|r|/2))` in

\[
 \psi(z)=-\gamma+
 \sum_{m=0}^\infty\left(\frac1{m+1}-\frac1{m+z}\right).
\]

The first `N` terms are bounded by two harmonic sums, while the remaining tail
is bounded by `7/2`; this gives
`|psi(1/4+ir/2)|<12+2 log(1+|r|/2)`, and `log(pi)<2`
gives the displayed estimate.

For `x=|u|>=T/2`, one has `|T+u|<=3x` and `1+T/2<=T`. Hence

\[
 |H(T+u)-H(T)|
 \le28+2\log(3x)+2\log T.
\]

Using the `1/u^2` Fourier bound on both tails and

\[
 \int_a^\infty\frac{\log(3x)}{x^2}dx
 =\frac{\log(3a)+1}{a},
 \qquad a=T/2,
\]

gives

\[
 \frac1{2\pi}\int_{|u|>T/2}
 |H(T+u)-H(T)|\,d\mu_v(u)
 \le\frac{4K^2}{\pi^2LT}
 \left(30+2\log(3T/2)+2\log T\right).
\]

Replacing `pi^2` by `9`, `L` by `2n`, and both logarithms by their bit-length
majorants gives `E_tail`.

### 5. Pole bound

For either `z=-T+i/2` or `z=-T-i/2`, the integral over one cell satisfies

\[
 \left|\int_{I_j}e^{2\pi izx}dx\right|
 \le\frac{c^{1/4}}{\pi T}.
\]

Cauchy--Schwarz gives

\[
 |W_v(z)|\le\frac{\sqrt K\,c^{1/4}}{\pi T}.
\]

The finite pole identity in L-2801 and `h=L/(2*pi*K)` therefore give

\[
 \left|\frac{\mathcal R(g_{T,v})}{h}\right|
 \le\frac{4K^2\sqrt c}{\pi LT^2}
 <\frac{2K^2s}{3nT^2}=E_{\rm pole}.
\]

Adding the four independent bounds proves the theorem.

### 6. Elementary constant bounds

The proof-producing checker uses only:

- `pi>3`;
- `e>2`, hence `log(2)<1`;
- `e<3`, hence `e^2<9<10` and `log(10)>2`;
- `e^3>1+3+9/2+27/6>10`, hence `log(10)<3`.

No decimal approximation to a transcendental constant enters the exact budget.

## Analytic domain audit

- The probability representation uses only real `u` and Parseval.
- The Binet formula is used at real part `1/4>0`.
- All logarithms in the analytic proof have positive real arguments.
- The checker itself evaluates no logarithm; bit lengths replace them.
- The pole estimate uses exact finite cell integrals and ordinary absolute
  values only.

## Dependency audit

L-2801 supplies the exact source terms. No prime-side sign, phase, or
Guinand--Weil implication is proved here. A complete RH witness still requires
an independently certified leading prime interval and the explicit-formula
normalization.

## Gap audit

1. This bound encloses only the difference between the exact archimedean-plus-
   pole contribution and the leading scalar.
2. It does not enclose the complete prime sum, phase range reduction, or the
   eigensolver used in PR #44.
3. The empirical comparison with PR #44 is not a proof that the full value is
   positive.
4. A negative leading screen whose magnitude is below `E` remains unresolved.
5. Admissibility of the unmollified step envelope remains a separate analytic
   review target.

## Adversarial tests

X-2801 checks the exact target fraction, positive and negative synthetic
thresholds, zero-touch rejection, schema strictness, integer type strictness,
and the high-carrier domain assumptions.

## Remaining uncertainty

The constants are intentionally loose. Independent review should check the
Fourier first-moment calculation and every factor of `2*pi`. The target bound
has more than two orders of magnitude of slack relative to the empirical PR #44
margin.

## Suggested next attack

Produce a directed interval for the frozen-vector complete prime Rayleigh value
at `c=10^11`. It is sufficient to separate the leading margin from zero by
`1/750000`; direct ball quadrature of the oscillatory archimedean term is no
longer necessary for this target.
