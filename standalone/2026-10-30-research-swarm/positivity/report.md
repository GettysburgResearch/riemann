# Reciprocal-density factor removal: a finite closure theorem and an exact obstruction

Status: **EXPLORATION / EXACT ELEMENTARY COUNTERMODEL / SOURCE-QUALIFIED FINITE COROLLARY**.  
Scope: a constructive attack through reciprocal-xi densities, with an explicit fourth-order condition for iterating real-zero removal. No new zero-free boundary or RH proof is obtained.  
Exact dependencies: Suvrit Sra, author-site v2 of 29 October 2026, especially Proposition 3.3 and Appendix C.2; classical self-decomposable-law unimodality and PF convolution facts used there. The countermodel and its algebraic estimates are derived below independently.  
What was actually run: primary-source screening, full Sra PDF extraction, exact rational checks, an ordinary binary64 Fourier probe of the actual reciprocal xi function, and an analytic countermodel construction.  
Smallest remaining gap: a source-specific, cofinal preservation theorem for the factor-removal inequality in §2. Existing verified-height arguments stop at a finite cutoff.

## 1. Candidate mechanisms and novelty screen

Two mechanisms were attacked.

1. **Infinite divisibility / Thorin factorization.** Constructing the reciprocal-xi law as an infinitely divisible law initially looked like a possible bridge to real zeros. This does not supply that bridge. Sra's paper already proves the relevant unconditional self-decomposability; Polson's 2026 papers explicitly distinguish it from the additional generalized-gamma-convolution/Thorin positivity requirement. This direction was rejected as a standalone route: replacing the missing positivity with its name would be circular.
2. **Real-zero factor removal with a preserved shape condition.** Instead of asking for every Toeplitz minor at once, remove one verified real-zero pair by a local differential operator and track a concrete fourth-order sign. This produces an exact iterative target, a substantial finite consequence of Sra's method, and a sharp obstruction to an automatic bootstrap.

The resulting formulas and countermodel are contributions of this pass, with no claim that their abstract ingredients are globally new. Sra already extracts finite PF factors; that operation is explicitly attributed rather than rediscovered here. The proposed research step is to establish an arithmetic invariant under repeated factor removal, beyond the currently verified-height argument.

**Objects:** write $\Xi(z)=\xi(1/2+iz)$ and normalize its reciprocal density $p$ by

$$
\int_{\mathbb R}e^{sx}p(x)\,dx=\frac{\Xi(0)}{\Xi(s)}.
$$

Thus its characteristic function is $\widehat p(u)=\xi(1/2)/\xi(1/2+u)$. This is the reciprocal density, not the original theta/Fourier kernel whose transform is $\Xi$.

## 2. The exact operator and the missing preservation inequality

The centered Laplace density $\ell_a(x)=a e^{-a|x|}/2$ has bilateral Laplace transform $a^2/(a^2-s^2)$. Removing a real-zero pair $\pm a$ from the reciprocal transform therefore corresponds to

$$
\mathcal D_a f=f-a^{-2}f''.
\tag{2.1}
$$

All derivatives may first be interpreted distributionally. In the smooth exponentially decaying setting below, they are ordinary functions and the integral of $\mathcal D_a f$ is one.

### Lemma 2.1: one removal preserves nonnegativity under log-concavity

Suppose $f$ is an even, positive, $C^2$ probability density, $\log f$ is concave, its logarithmic tail slope tends to $-a$ as $x\to+\infty$, and the derivatives have the decay needed to integrate (2.1). Then $\mathcal D_a f\ge0$ and has mass one.

**Proof.** Put $r=-(\log f)'$ for $x>0$. Evenness and log-concavity give $0\le r\le a$ and $r'\ge0$. Hence $f''/f=r^2-r'\le a^2$. Integrating (2.1), with vanishing boundary derivatives, gives mass one. □

The conclusion is positivity, not log-concavity of the new density. That distinction is exactly where iteration can fail.

For a positive $C^4$ density define

$$
K_a[f]=(a^2f'-f''')^2-(a^2f-f'')(a^2f''-f'''').
\tag{2.2}
$$

Whenever $h=\mathcal D_a f>0$,

$$
- (\log h)''=\frac{K_a[f]}{(a^2f-f'')^2}.
\tag{2.3}
$$

This is an identity, obtained by substituting $h,h',h''$. The precise additional condition for a log-concavity-preserving step is **$K_a[f]\ge0$ at every real location**, together with $h>0$.

An equivalent score formulation makes the proposed invariant explicit. Set

$$
q=a^2-r^2+r',\qquad r_a=r-\frac{q'}q.
$$

Then $h=fq/a^2$, and $r_a$ is its negative logarithmic derivative. The step preserves log-concavity exactly when

$$
r' q^2-q q''+(q')^2\ge0.
\tag{2.4}
$$

This is a concrete fourth-order inequality to derive from the actual reciprocal-xi construction. It is not implied by the sign $r'\ge0$ alone; §4 gives a fully explicit counterexample.

### Why a cofinal version would reach the actual zeros

Let $P_T(s)$ be the product of all real-zero factors $1-s^2/a^2$ of $\Xi$ with $0<a\le T$, counted with multiplicity. If, for every $T$, the quotient $\Xi(0)P_T(s)/\Xi(s)$ were the bilateral Laplace transform near zero of an even positive probability measure, then all zeros of $\Xi$ would be real.

Here is the short reason. The Laplace power series has nonnegative even coefficients. A finite radius of convergence of a power series with nonnegative coefficients forces a singularity on the positive real boundary (the positive-series/Pringsheim argument). But every positive real pole through $T$ has been removed. Therefore the quotient has no pole in the disc $|s|<T$. Any fixed nonreal zero would survive every $P_T$ and eventually lie in one of these discs, a contradiction.

For completeness, the positive-series fact follows by expanding at a point just to the left of a putative regular positive boundary point. All Taylor coefficients there are nonnegative. Tonelli then converts convergence slightly beyond the boundary into convergence of the original nonnegative series beyond its radius.

Under RH the converse follows from the convergent convolution of the remaining centered Laplace factors. Thus cofinal positivity is as hard as the missing global input. Equations (2.2)–(2.4) expose a possible *local preservation theorem* that would supply it; merely declaring the cofinal condition is not progress toward proving that theorem.

## 3. A finite log-concavity closure theorem from Sra's method

Sra's Theorem C.3 extracts all verified real-zero factors up to $U$, except one retained real factor, with a positive self-decomposable residual. The proof of Proposition 3.3 uses a second retained ordinate to control exponential tilts. The same estimates give the following useful explicit extension.

### Proposition 3.1: deletion through one eighth of the verified height

Assume the verified-height and zero-count inputs used in Sra v2. Let $2000\le U\le T_*$ and $0\le V\le U/8$. Delete from the reciprocal-xi transform **every real-zero factor with ordinate at most $V$**, with multiplicity. The resulting normalized density is positive, analytic on the real line, and strictly log-concave.

In particular, using the source's $T_*=3\cdot10^{12}$, this preserves strict log-concavity after deleting all verified real-zero factors through height

$$
V=3.75\cdot10^{11}.
$$

This is a finite, source-qualified consequence. It does not verify any new zeros beyond the supplied height and does not improve an all-height zero-free strip.

**Proof.** The source's counting estimate ensures a real ordinate in $(U/8,U/6]$ and one in $(U/4,U/3]$. Let $a$ be the first ordinate surviving deletion and retain an ordinate $\eta\in(U/4,U/3]$. Thus

$$
a\le U/6,\qquad \eta-a\ge U/12.
$$

The first interval's existence is Corollary C.4's counting argument with $U$ replaced by $U/2$. By Theorem C.3, retaining $a$ and restoring the undeleted verified factors gives a positive analytic density $p_V$. Retaining $\eta$ instead also exhibits a positive residual after extracting $\ell_a$, so $|p'_V|<a p_V$.

Write an upper-half-plane zeta zero as $\rho=1/2+\delta_\rho+i\gamma$, with $|\delta_\rho|\le1/2$. After deletion, the bilateral Lévy numerator is the sum of the remaining verified exponentials and the tail

$$
A_{>U}(x)=\sum_{\gamma>U}e^{-\gamma x}\cos(\delta_\rho x),\qquad x>0.
$$

For every tilt $|s|<a$, the high-zero terms of $e^{sx}A_{>U}(x)$ and their negative derivatives are nonnegative for $x\le\pi$: both the cosine term and $\delta_\rho\sin(\delta_\rho x)$ have the required sign. A negative contribution therefore requires $x>\pi$.

For such $x$, compare with the retained term $e^{-(\eta-s)x}$. The absolute derivative factor is at most $2\gamma$, while $\eta-s\ge U/12$. The reciprocal-square tail estimate in Sra gives

$$
\sum_{\gamma>U}\gamma^{-2}\le\frac{2(\log U+1)}U.
$$

Since $y^3e^{-\pi(y-\eta)}$ is decreasing for $y\ge U$, the possible negative derivative tail divided by the retained derivative is at most

$$
\begin{aligned}
\varepsilon_U
&\le\frac{24}{U}\sum_{\gamma>U}\gamma e^{-\pi(\gamma-\eta)}\\
&\le48U(\log U+1)e^{-2\pi U/3}<1.
\end{aligned}
\tag{3.1}
$$

The numerator itself has the smaller bound $2U(\log U+1)e^{-2\pi U/3}$. The opposite tilt is identical. All remaining verified terms have positive rates and coefficients. Therefore every tilt with $|s|<a$ is self-decomposable and hence unimodal, using the same classical theorem as Proposition 3.3.

If $(\log p_V)''(x_0)>0$, the tilt $s=-p'_V(x_0)/p_V(x_0)$ lies in $(-a,a)$ and has a strict local minimum at $x_0$, contradicting unimodality. Hence $\log p_V$ is concave. Real analyticity excludes an affine interval unless the density is a global exponential, which is incompatible with an integrable positive density on $\mathbb R$. This gives strict log-concavity in the usual two-point sense. □

**Precision about strictness.** The last argument proves strict concavity as a function; analyticity by itself does not exclude an isolated point where the second derivative vanishes. No stronger pointwise negative-curvature claim is used here.

**Interpretation.** A very long finite factor-removal ladder is already accessible from the recent source. The unpaid statement is preservation beyond any supplied verified-height cutoff. Enlarging this finite ladder is not itself a route from finite to cofinal positivity.

## 4. An explicit obstruction in the correct reciprocal-transform class

The next construction blocks a tempting shortcut: use strict log-concavity and a tiny total-variation distance from a PF-infinity law to justify indefinite factor removal.

### 4.1 A positive residual whose second removal becomes negative

Define the even probability density

$$
h(x)=\frac{e^{-|x|}}{10}\bigl(4-\cos|x|+3\sin|x|\bigr).
\tag{4.1}
$$

It is positive because $4>\sqrt{10}$, and direct integration gives mass one. Its bilateral Laplace transform, initially for $|\Re s|<1$, is

$$
\mathcal Lh(s)=\frac4{(1-s^2)(s^4+4)}.
\tag{4.2}
$$

Its reciprocal is an even entire polynomial with real zeros $\pm1$ and a nonreal quartet $\pm1\pm i$.

For $x>0$ put $g=4-\cos x+3\sin x$. Then

$$
(\log h)''=\frac{6-4g}{g^2}.
$$

At $x=3\pi/2$, $g=1$, so this curvature is $2>0$: $h$ is not log-concave. Removing the real pair $\pm1$ gives

$$
\mathcal D_1h(x)=\frac12e^{-|x|}(\cos|x|+\sin|x|),
\tag{4.3}
$$

which is negative at $x=\pi$.

### 4.2 A preceding density is strictly log-concave

Let $0<a\le1/20$ and $f_a=\ell_a*h$. For $x\ge0$, write $10f_a(x)=F(x)=Ae^{-ax}+e^{-x}P(x)$, where

$$
\begin{gathered}
P=B+C\cos x+D\sin x,\\
A=\frac{20a}{(1-a^2)(a^4+4)},\qquad B=-\frac{4a^2}{1-a^2},\\
C=-\frac{a^2(a^2+6)}{a^4+4},\qquad
D=-\frac{a^2(2-3a^2)}{a^4+4}.
\end{gathered}
$$

These formulas follow from $(1-a^{-2}D^2)f_a=h$ and evenness. Put $d=1-a$ and $R_0=\sqrt{C^2+D^2}$. Direct differentiation yields

$$
FF''-(F')^2=Ae^{-(a+1)x}K(x)+e^{-2x}L(x),
$$

where

$$
K=P''-2dP'+d^2P,
\qquad L=PP''-(P')^2.
$$

The following elementary bounds hold throughout $0<a\le1/20$:

$$
A\ge5a,\quad 4a^2\le-B\le5a^2,\quad
R_0^2=\frac{10a^4}{a^4+4}\le\left(\frac85a^2\right)^2,
\quad d^2\ge\frac9{10}.
$$

Consequently

$$
K\le d^2B+(d^2+1)R_0\le-\frac25a^2,
\qquad L\le(-B)R_0\le8a^4.
$$

Therefore

$$
FF''-(F')^2
\le e^{-(a+1)x}(-2a^3+8a^4)
\le-\frac85a^3e^{-(a+1)x}<0.
\tag{4.4}
$$

Thus $f_a$ is strictly log-concave, but its first real-zero removal gives $h$, which is not log-concave; its next removal gives a signed function. Equations (2.2)–(2.4) cannot follow from initial log-concavity alone.

### 4.3 Arbitrarily close to PF-infinity, with an order-one entire reciprocal

The first absolute moment of $h$ is $11/10$. A translation of $\ell_a$ through $y$ has total-variation distance $1-e^{-a|y|/2}\le a|y|/2$. Hence

$$
d_{TV}(f_a,\ell_a)\le\frac{11a}{20}.
\tag{4.5}
$$

The comparison density $\ell_a$ is PF-infinity. The right-hand side can be arbitrarily small while the nonreal quartet remains fixed. For example, $a=10^{-9}$ gives a bound $5.5\cdot10^{-10}$.

One can preserve this obstruction even while requiring an **entire density and an order-one entire transform reciprocal**. Let $G_R$ be the law of the convergent sum of independent centered Laplace variables with rates

$$
b_n=\frac{Rn}{1+\log n},\qquad n\ge1.
$$

Its variance is at most $12/R^2$, because the decreasing function $(1+\log x)^2/x^2$ has integral $5$ on $[1,\infty)$. Its transform reciprocal is

$$
E_R(s)=\prod_{n\ge1}(1-s^2/b_n^2),
$$

an entire function of order one with only real zeros. Finite Laplace convolutions are PF-infinity, and the limit retains that property. Moreover its characteristic function decays faster than every exponential: the number of $b_n\le |u|$ grows proportionally to $|u|\log|u|$. Fourier inversion therefore gives an entire density.

Convolve both densities in (4.5) with $G_R$. Total variation contracts, both resulting densities are entire and log-concave, and real analyticity makes their log-concavity strict. The reciprocal transform of $f_a*G_R$ is

$$
(1-s^2/a^2)(1-s^2)(1+s^4/4)E_R(s),
$$

which is still entire of order one and still has the nonreal quartet.

The failures after removal survive smoothing. For $R=1000$, the global derivative bounds

$$
\|h''\|_\infty<11/10,\quad
\|h'''\|_\infty<13/10,\quad
\|h''''\|_\infty<17/10
$$

give errors in $h,h',h''$ after smoothing bounded respectively by $33/(5R^2),39/(5R^2),51/(5R^2)$. At $x=3\pi/2$, $h'= -2h$, $h''=6h$, and $h>1/1500$. These bounds imply

$$
(h*G_R)(h*G_R)''-((h*G_R)')^2
>\frac{46955291}{56250000000000}>0.
$$

For the second removal, (4.3) has second derivative bounded by $3/2$, so its value after smoothing at $\pi$ is at most

$$
-\frac1{110}+\frac9{R^2}
=-\frac{99901}{11000000}<0.
$$

The elementary bounds $e^5<150$ and $e^4<55$ suffice for these rational estimates.

**Exact conclusion:** arbitrarily accurate PF-infinity approximation, strict log-concavity, evenness, an entire density and an order-one entire reciprocal do not imply that the reciprocal has only real zeros. This is not a counterexample to Sra's source-specific PF256 theorem. The construction does not establish PF256 for the countermodel, and no such claim is made.

## 5. Actual-xi probe and the computational target

`xi_probe.py` evaluates the actual real-axis function $\xi(1/2)/\xi(1/2+u)$ and multiplies it by the first zero-removal factors. Fourier inversion supplies derivatives through order four and evaluates (2.2). The two zero centers are the centers printed in Sra C.6, rounded to binary64.

For removed-factor counts $n=0,1,2$ and $x=0,0.1,\ldots,0.4$, all sampled densities and log-concavity margins were positive; all sampled available removal determinants were positive. Selected values of $-(\log f_n)''$ are:

| Removed pairs | $x=0$ | $x=0.2$ | $x=0.4$ |
|---|---:|---:|---:|
| 0 | 23.65746 | 21.89205 | 17.14004 |
| 1 | 29.07203 | 27.46298 | 23.05923 |
| 2 | 32.83558 | 31.23660 | 26.81115 |

Changing the quadrature step/cutoff from $(0.25,128)$ to $(0.125,256)$ changed sampled densities by at most $2.23\cdot10^{-16}$. This is only an internal stability observation in ordinary floating point. There is no directed rounding or rigorous truncation enclosure, and the computation proves no global sign. The finite-source result in §3, not this grid, explains why these first steps should succeed.

A meaningful next computation would enclose $K_a[f]$ with a full Fourier truncation and derivative-error budget, then establish a spatial tail inequality. A total-variation error does not suffice: it bounds characteristic-function error only uniformly, whereas removing $N$ factors multiplies that error by $\prod_{j\le N}(1+u^2/a_j^2)$, an unbounded polynomial. To control (2.2), the source error must be integrable after this multiplier and the derivative weights through $u^4$.

## 6. What survives as a research direction

The promising target is a **source-specific invariant for (2.2)**, or an equivalent invariant for the score update in (2.4), obtained from the theta/arithmetic construction rather than from a verified zero list. The generic positivity, infinite-divisibility and approximation statements do not provide that invariant. The countermodel identifies the exact place they fail.

The finite theorem gives a large, explicit baseline against which an alleged invariant can be tested. Any proposed extension must explain how it controls the previously unverified tail without assuming real zeros there. A claimed iteration based only on log-concavity, small residual variance, or a small total-variation error fails the countermodel in §4.

### Reproduction

Run `python countermodel.py` for the exact rational checks and `python xi_probe.py` for the NumPy/SciPy numerical probe. The corresponding JSON files preserve their different evidence levels. No test here authenticates a Riemann proof or reruns Sra's interval certificate.

### Sources and provenance

- Suvrit Sra, *On some positivity properties of the Riemann Xi function*, author-site v2, 29 October 2026: [PDF](https://suvrit.github.io/papers/riem-xi/riem-xi-v2.pdf), [author repository](https://github.com/suvrit/preprints/blob/main/preprints/riem-xi/v2/riem-xi-v2.pdf), Git blob `f98e0bd0d2d1353245a482581ffa74580c644996`. Full text inspected, including Proposition 3.3 and C.2–C.4; external proofs/certificates not replayed.
- Nicholas G. Polson, *Thorin Measures and the Reciprocal Xi Function*, [SSRN 7320139](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7320139), and *Thorin Positivity, GGC Factorization and the Riemann Xi Function*, [SSRN 6930178](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6930178). Primary indexed abstracts inspected for novelty screening; full manuscripts not audited.
- Alexander Belton, Dominique Guillot, Apoorva Khare and Mihai Putinar, *Hirschman–Widder densities*, Applied and Computational Harmonic Analysis, [DOI 10.1016/j.acha.2022.04.002](https://doi.org/10.1016/j.acha.2022.04.002). Primary journal introduction screened for the classical PF reciprocal-transform characterization.
- Wojciech Michalowski, *On the Pólya Frequency Order of the de Bruijn–Newman Kernel: Certified Failure at Order Five*, [arXiv:2602.20313v2](https://arxiv.org/abs/2602.20313v2). Primary indexed abstract screened only. It concerns the original theta kernel, not the reciprocal density in this report.

The root literature packet and its repository map identify the overlap with PRs #1021 and #1023. This work does not modify their reviewed claims or treat a different positive kernel as the actual xi object.
