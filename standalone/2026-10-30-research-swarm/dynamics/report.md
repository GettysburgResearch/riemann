# Dynamics lane: an exact integration gate, hidden quartets, and a heat-bath law

Status: **PROVED MODEL LEMMAS / EXACT FINITE CHECKS / OPEN XI TRANSFER**.  
Scope: real entire functions, Jensen polynomials and polynomial heat flow. No new zero-free boundary for zeta is asserted.  
Exact dependencies: the elementary derivations below, standard real-rooted polynomial closure under differentiation, and the repository overlap noted in §8.  
What was run: standard-library rational Sturm computations, exact polynomial heat calculations, and separately labeled floating illustrations in [experiments.py](experiments.py), with output in [results.json](results.json).  
Smallest remaining gap: a source-specific inequality placing the actual xi integration constants inside every relevant critical-value interval. Forward heat smoothing and high-derivative entry do not supply it.

## 1. The attacks and their outcome

Two proposed mechanisms were pursued:

1. **Degree/shift transport:** enter a uniformly hyperbolic high-derivative regime, then reconstruct the original entire function through integration. This led to an exact, computable critical-value gate and a countermodel that retains the order, coefficient signs, an arbitrarily narrow zero strip, and any prescribed finite on-line zero list. Its high derivatives are all in the Laguerre–Pólya class, yet it has an off-axis quartet.
2. **Density-accelerated root flow:** exploit the attraction of a nonreal conjugate pair toward the real axis when many real roots are nearby. This led to a local contraction inequality and an exactly solvable model with collision time $a^2/(4m+2)$. It also demonstrates why forward smoothing is not an inverse theorem about the original zeros.

These are concrete investigations of mechanisms, rather than a new claim that familiar Jensen or heat ideas have never been considered. The strongest outcome is the explicit integration gate and its quantitative hidden-zero detection scale. It sharpens an already recognized qualitative obstruction in this repository.

## 2. An order-matched, positive-coefficient hidden quartet

For $C>0$, define the entire function

$$
G_C(w)=C+2\sqrt w\sinh\sqrt w-2\cosh\sqrt w+2
      =C+\sum_{n\ge1}\frac{w^n}{n(2n-2)!}.
$$

The displayed square-root expression is single-valued through its power series. It has order $1/2$, every Taylor coefficient is positive, and

$$G_C'(w)=\cosh\sqrt w.$$

The derivative has only the negative real zeros $-\pi^2(k+1/2)^2$, $k\ge0$, and belongs to the Laguerre–Pólya class (LP). Every further derivative is also LP: approximate its genus-zero product by real-rooted polynomials and apply Rolle's theorem and locally uniform convergence.

At $w_0=-\pi^2/4$,

$$G_C'(w_0)=0,\qquad G_C''(w_0)=1/\pi,\qquad G_C(w_0)=C+2-\pi.$$

Consequently, if $C>\pi-2$, the first Laguerre expression is negative:

$$G_C'(w_0)^2-G_C(w_0)G_C''(w_0)
   =-\frac{C+2-\pi}{\pi}<0.$$

It cannot be LP. In fact, §2.1 proves that when

$$\pi-2<C<5\pi-2,$$

$G_C$ has exactly one nonreal conjugate pair. Its even order-one counterpart

$$F_C(z)=G_C(-z^2)=C+2-2z\sin z-2\cos z$$

has exactly one off-axis quartet. Thus this is not just an example with a different entire-function order from xi.

### 2.1 Why there is exactly one quartet

Write $H_c(z)=z\sin z+\cos z-c$, where $c=1+C/2$; $F_C=-2H_c$.

At $c=1$,

$$H_1(z)=2\sin(z/2)\bigl(z\cos(z/2)-\sin(z/2)\bigr).$$

Both factors have only real zeros. For the second, put $u=z/2$. A nonzero root satisfies $u\cos u=\tfrac12\sin u$, hence gives an eigenfunction $v(x)=\sin(ux)$ of

$$-v''=u^2v,\quad v(0)=0,\quad v'(1)=\tfrac12v(1).$$

Integration against $\overline v$ gives a real positive eigenvalue, because

$$\int_0^1|v'|^2-\tfrac12|v(1)|^2
  \ge\tfrac12\int_0^1|v'|^2>0.$$

Here $|v(1)|^2\le\int_0^1|v'|^2$ follows from $v(0)=0$. Thus $u^2>0$ and $u$ is real. The zero $u=0$ is also real.

The critical points of $H_c$ are independent of $c$:

$$H_c'(z)=z\cos z.$$

Their critical values are $1-c$ at zero and
$(k+1/2)\pi(-1)^k-c$ at the positive critical points, with the same values at their negatives. As $c$ increases from $1$ to $\pi/2$, the double root at zero first separates along the real axis; no subsequent real-root collision is possible before $c=\pi/2$. At that value the roots at $\pm\pi/2$ become double. Increasing $c$ further makes them a nonreal quartet. The next possible real collision is at $c=5\pi/2$.

For completeness, roots cannot enter from infinity in this continuation argument. Uniformly for $c$ in a compact real interval, every sufficiently large zero lies in a disk of radius $A/|n|$ about $n\pi$, for a fixed sufficiently large $A$, and each such disk contains exactly one root. Indeed, for $|\Im z|\ge1$, $|z\sin z|$ dominates $|\cos z-c|$ when $|z|$ is large. For $|\Im z|\le1$, if $n\pi$ is the nearest real sine zero, then

$$|\sin z|^2=\sin^2(\Re z)+\sinh^2(\Im z)
  \ge(2/\pi)^2|z-n\pi|^2.$$

The zero equation forces $|z-n\pi|=O(1/|z|)$. On the boundary of a slightly larger disk, Rouché's theorem compares $z\sin z$ with $\cos z-c$ and gives one zero. Conjugation symmetry makes that unique zero real. All potentially nonreal roots therefore remain in one bounded region throughout the continuation. The critical-point calculation now proves the asserted classification. At $C=\pi-2$ all zeros are real, including the double zero of $G_C$ at $w_0$.

### 2.2 Arbitrarily high and narrow defects, with prescribed finite real zeros

Put $C=\pi-2+\eta$, with $\eta>0$ small. Taylor expansion at $w_0$ and analytic square-root splitting give

$$w_\pm=-\pi^2/4\ \pm i\sqrt{2\pi\eta}+O(\eta).$$

The positive-real-part roots of $G_C(-z^2/K^2)$ have

$$T=K\bigl(\pi/2+O(\eta)\bigr),\qquad
\delta=K\bigl(\sqrt{2\eta/\pi}+O(\eta^{3/2})\bigr).$$

Given any finite height $T_0$ and any strip width $\varepsilon>0$, choose $K$ large, then choose $\eta$ small. The sole quartet lies above $T_0$ and inside $|\Im z|<\varepsilon$; all other zeros are real.

One can additionally prescribe any finite collection $\tau_j\in(0,T_0]$ of real zeros. Set

$$P(w)=\prod_{j=1}^m(w+\tau_j^2),\qquad
\widetilde G(w)=P(w)G_C(w/K^2),\qquad
\widetilde F(z)=\widetilde G(-z^2).$$

All Taylor coefficients of $\widetilde G$ are positive. Choosing, for example, $K\ge2T_0$ ensures that the added $G_C$ factor has no zeros for $|z|\le T_0$: there the scaled argument is $w=-z^2/K^2$, so $|w|\le1/4$ and

$$|G_C(w)-C|\le |w|\cosh\sqrt{|w|}\le\tfrac14\cosh(1/2)<C.$$

Hence the prescribed list is exactly the zero list in that disk. The quartet remains, and the whole zero set still lies in the arbitrarily narrow strip.

Even the following much stronger high-derivative property survives:

> **For every $n\ge m+1$, $\widetilde G^{(n)}$ is LP.**

To prove it, for any analytic $g$ and $P(w)=\prod_{j=1}^m(w-r_j)$, repeated Leibniz differentiation gives the operator identity

$$D^{m+1}(Pg)=
  \bigl((w-r_1)D+m+1\bigr)
  \bigl((w-r_2)D+m\bigr)\cdots
  \bigl((w-r_m)D+2\bigr)g'.$$

Each factor preserves LP when $r_j$ is real and its integer constant $k$ is positive, since

$$((w-r)D+k)h=(w-r)^{1-k}D\bigl((w-r)^kh\bigr).$$

Multiplication by a real-rooted polynomial, differentiation, and removal of the displayed real-root factor preserve LP. Apply this to $g(w)=G_C(w/K^2)$, whose derivative is LP. Further derivatives remain LP.

**Scope of the obstruction.** These functions have xi's even order-one geometry, positive coefficients after the square-root change, arbitrary finite real-zero agreement, an arbitrarily thin strip, and uniform-in-degree high-shift Jensen hyperbolicity. They do not have xi's arithmetic source, its positive integrable Fourier kernel and real-axis decay, or its precise large-height zero-counting asymptotic: this model is of finite exponential type. The example therefore identifies information an actual xi proof must use; it is not a counterexample to RH or to any source-specific xi identity.

## 3. Exact Jensen gate and the degree required to reveal the defect

Use the exponential Taylor convention

$$G_C(w)=\sum_{n\ge0}\gamma_n\frac{w^n}{n!},\quad
\gamma_0=C,\quad \gamma_n=\frac{(n-1)!}{(2n-2)!}\quad(n\ge1),$$

and $J_d^n(X)=\sum_{j=0}^d\binom dj\gamma_{n+j}X^j$.

### 3.1 Every positive shift passes every degree

For $n\ge1$,

$$J_d^n(X)=\gamma_n\,{}_1F_1(-d;n-1/2;-X/4)
 =\gamma_n\frac{d!}{(n-1/2)_d}L_d^{n-3/2}(-X/4).$$

The Laguerre parameter is greater than $-1$, so all roots are negative and real. This agrees with, and makes explicit, the LP derivative argument. Changing $C$ does not change any of these polynomials.

### 3.2 A complete finite-degree integration-constant criterion

For $d\ge2$,

$$J_d^0(X)=C+2-2\,{}_1F_1(-d;-1/2;-X/4).$$

Let $q(u)={}_1F_1(-d;-1/2;u/4)$, and let $u_1>0$ be its first critical point. Define

$$C_d=2q(u_1)-2.$$

Then, for $C\ge0$,

$$\boxed{J_d^0\text{ has only real nonpositive roots}\iff C\le C_d.}$$

Here is a proof that the *first* critical value is the controlling one. The derivative of $q$ is a positive multiple of $L_{d-1}^{-1/2}(u/4)$ and therefore has $d-1$ simple positive zeros. Its differential equation is

$$4u q''-(u+2)q'+dq=0.$$

The Sonin-type energy

$$E(u)=q(u)^2+\frac{4u}{d}q'(u)^2$$

satisfies the exact identity

$$E'(u)=\frac{2u+8}{d}q'(u)^2>0$$

away from isolated critical points. Thus the absolute values at successive critical points strictly increase. At a critical point the ODE gives $q''=-dq/(4u)$: maxima have positive value, minima have negative value, and these alternate. In $J_d^0(-u)=C+2-2q(u)$, every negative critical value of $q$ produces a positive local maximum. The positive critical values produce local minima, and the first is the smallest upper constraint on $C$. Requiring that minimum to be nonpositive gives $C\le C_d$. Together with $J_d^0(0)=C\ge0$ and the leading-end sign, the alternating extrema supply all $d$ real roots. Conversely a positive first local minimum forbids real-rootedness. Equality gives a double root.

This is an explicit acceptance gate for the missing integration constant. It is stronger information than saying merely that descent is not automatic.

### 3.3 Asymptotic size of that gate

Uniformly with derivatives on compact $w$-sets,

$$J_d^0(w/d)=G_C(w)-\frac{w^2}{2d}G_C''(w)+O(d^{-2}).$$

For justification, the coefficient multiplier is
$s_{d,j}=\prod_{k=0}^{j-1}(1-k/d)$ for $j\le d$ and zero otherwise. The first-order expansion is
$s_{d,j}=1-j(j-1)/(2d)+O(j^4/d^2)$, with a bound valid for all $j$ after extending by zero. Summation is uniform because the entire series and all polynomially weighted versions converge on compact sets.

The scaled first critical point tends to $w_0=-\pi^2/4$. In fact,

$$d(-u_1)=w_0-\frac{3\pi^2}{16d}+O(d^{-2}),$$

where $X=-u_1$ is the unscaled polynomial variable. Since $G_C'(w_0)=0$ and $G_C''(w_0)=1/\pi$, the critical value gives

$$\boxed{C_d=\pi-2+\frac{\pi^3}{32d}+O(d^{-2}).}$$

For $C=\pi-2+\eta$ tending down to the threshold, the degree at which the gate fails therefore has scale

$$d\sim\frac{\pi^3}{32\eta}\sim\frac{T^2}{4\delta^2}.$$

This is a quantitative statement for this countermodel, not a universal lower bound for every RH test. It shows why a high, near-axis quartet can require a very large unshifted Jensen degree even when **every positive shift, at every degree, already passes**.

All finite collections of degree tests can be made to pass while retaining the quartet. Indeed, $G_{\pi-2}$ is LP by §2.1, so $C_d\ge\pi-2$ by the polynomial differential-operator proof of Jensen preservation. The inequality is strict: $C_d$ is algebraic (it is a value of a rational polynomial at an algebraic critical point), whereas $\pi-2$ is transcendental. Choose $C$ strictly between $\pi-2$ and the minimum of finitely many $C_d$.

### 3.4 Exact computational example

Take the rational constant $C=6/5$. The executable computes integer/Fraction Sturm chains, preserving their signs when removing content. It proves the following finite root counts:

| Unshifted degree | Distinct real roots | Consequence |
|---|---:|---|
| Every $1\le d\le17$ | $d$ | Every one of these tests passes |
| $d=18$ | $16$ | One nonreal pair in the Jensen polynomial |
| Every $19\le d\le24$ | $d-2$ | The defect persists in these checked degrees |

All these polynomials are squarefree. Sample positive-shift polynomials were also checked exactly; the infinite positive-shift statement is proved in §3.1 and does not depend on samples.

The illustrative floating root of $F_{6/5}$ is approximately
$1.5785411256+0.1917472036i$. The value is not an interval certificate; the existence and classification of the quartet follow analytically.

## 4. The reusable integration gate

The previous model suggests a practical replacement for an unqualified downward-hyperbolicity assertion. Assume $J_N^n$ has degree exactly $N$ with positive leading coefficient $\gamma_{n+N}>0$, and $J_{N-1}^{n+1}$ has simple negative roots $r_1<\cdots<r_{N-1}$. Write

$$Q(x)=N\int_0^xJ_{N-1}^{n+1}(t)\,dt,\qquad J_N^n(x)=\gamma_n+Q(x).$$

All roots of $J_N^n$ are real nonpositive exactly when its integration constant lies in

$$\max\left(0,\max_{N-i\ {
m even}}[-Q(r_i)]\right)
\ \le\gamma_n\le\
\min_{N-i\ {
m odd}}[-Q(r_i)].$$

This follows from the necessary and sufficient alternating critical-value signs
$(-1)^{N-i}J_N^n(r_i)\ge0$, together with the leading-end sign and $J_N^n(0)\ge0$. Empty constraint sets are omitted. Repeated derivative roots require the corresponding multiplicity conditions; the displayed simple-root version is the one used here.

For actual xi work, the integration constant is fixed by the exact theta-source coefficients. A useful next theorem would compare those constants with these extrema uniformly in a degree/shift range covering every missing polynomial. The countermodel's coefficients show that positivity, LP high derivatives, finite verification, and a narrow strip cannot substitute for that comparison.

This does not by itself complete the repository's descent programme. It supplies an explicit inequality to prove or disprove, and the test family measures how badly a truncated computation can underestimate the necessary degree.

## 5. A density-sensitive contraction inequality for root flow

Let a real polynomial $p_t$ solve $\partial_t p_t=-p_t''$. Away from collisions its simple roots obey

$$z_j'=2\sum_{k\ne j}\frac1{z_j-z_k}.$$

Suppose $z_j=x+iy$, $y>0$, has maximal imaginary part. Conjugation implies every other pair is $a\pm ib$ with $0\le b\le y$. Write $r=x-a$. Its inward imaginary contribution is

$$-2\left(\frac{y-b}{r^2+(y-b)^2}+\frac{y+b}{r^2+(y+b)^2}\right)
\le-\frac{4y}{r^2+4y^2}.$$

The inequality is exact algebra: after removing positive denominators, its difference has numerator

$$2y(y^2-b^2)(3r^2+3y^2+b^2)\ge0.$$

The root's own conjugate contributes $-1/y$. A real root contributes $-2y/(r^2+y^2)$, which is at most $-2y/(r^2+4y^2)$. If at least $M$ other roots, excluding the root and its conjugate and counting both members of other pairs, remain horizontally within $R$, then

$$y'\le-\frac1y-\frac{2My}{R^2+4y^2},\qquad
(y^2)'\le-2-\frac{4M y^2}{R^2+4y^2}.$$

If this density condition holds throughout the contraction interval for every maximizing root, integration gives an extinction-time bound from initial squared height $u_0$:

$$t_*\le\frac{u_0}{M+2}
 +\frac{R^2M}{4(M+2)^2}
 \log\left(1+\frac{2(M+2)u_0}{R^2}\right).$$

The case $M=0$ is $u_0/2$. The displayed logarithmic formula is for $R>0$, with its continuous limit when appropriate. Polynomial envelope switching is handled by the upper Dini derivative; collisions can be approached by simple-root perturbation.

**The time qualification is essential.** An initial local density count is not a bound maintained along the flow. For the actual xi heat family, one would also have to justify the normal convergence of the root sums, the relevant envelope, and a density estimate along the evolving source. Those statements have not been supplied by this lane.

## 6. Exact heat-bath collision law

There is a completely solvable test of the mechanism. Start with

$$p_0(z)=z^{2m}(z^2+a^2),\qquad a>0.$$

It contains one nonreal pair and $2m$ real roots at the origin. For $t>0$, with $x=z/(2\sqrt t)$ and physicists' Hermite polynomials,

$$p_t(z)=t^m\bigl(tH_{2m+2}(x)+a^2H_{2m}(x)\bigr).$$

The exact collision time is

$$\boxed{t_*=\frac{a^2}{4m+2}.}$$

Proof: let $n=2m$, $c=a^2/t$, and $h_j=2^{-j}H_j$ be monic Hermite polynomials. The relevant monic polynomial is

$$h_{n+2}+(c/4)h_n=xh_{n+1}
 -\left(\frac{n+1}{2}-\frac c4\right)h_n.$$

If $c\le2(n+1)$, this is the characteristic polynomial of the Hermite Jacobi matrix with a nonnegative squared last coupling. It has only real roots. At equality it is $xh_{n+1}$ and has a double root at zero.

If $c>2(n+1)$, evaluation at the $n+1$ zeros of $H_{n+1}$ gives $n$ interlacing real roots. On the imaginary axis, the sign at zero is opposite the eventual sign as $iy\to i\infty$, so there is an imaginary conjugate pair. These account for all $n+2$ roots. Converting $c=a^2/t$ proves the formula.

The script checks, with exact Sturm arithmetic, $m=0,1,2,4,8$ immediately before and after the predicted collision, and verifies the double zero at the collision. The times for $a=1$ are $1/2,1/6,1/10,1/18,1/34$.

This is a real acceleration effect: adding nearby real-root mass makes the off-axis pair disappear faster. It is also a rigorous warning against a proposed shortcut. Multiplying by a real-rooted factor and applying forward heat can erase a genuine off-axis zero. A zero-free transformed object gives no backward conclusion without an additional exact source identity or inverse inequality.

## 7. What would make this a productive xi attack?

The next experiment should be small and decisive:

1. Fix the actual xi coefficient normalization and select one unpaid degree/shift region from the integrated descent programme.
2. Compute the primitive critical-value interval using exact or directed bounds, retaining the actual integration constant. This distinguishes a genuine downward inequality from an entry estimate for derivatives.
3. Seek a source identity for its gap: an integral against the actual theta kernel, with the sign-changing polynomial displayed. Positivity of the kernel alone is not enough; the signed polynomial is the object to control.
4. Compare the quantitative gap against the model's $T^2/(4\delta^2)$ detection scale. A finite ladder cannot close the all-height claim without a uniform tail theorem.

The heat route requires a different additional input: an arithmetic identity that returns the smoothed function to the original source while retaining the relevant zero implication. Without that identity, the exact heat-bath example is a reason to stop treating faster forward contraction as a proof of RH at time zero.

## 8. Overlap, source screening and reproducibility

The current repository already identifies derivative entry versus downward descent as distinct. This lane therefore does not claim discovery of that distinction. The relevant integrated context is [PROGRAMMES.md, xi programme](https://github.com/GettysburgResearch/riemann/blob/f99d9e3908dde4865377c75d9ca051c1f545bf4f/PROGRAMMES.md), [OPEN_CUTS.md, xi cuts](https://github.com/GettysburgResearch/riemann/blob/f99d9e3908dde4865377c75d9ca051c1f545bf4f/OPEN_CUTS.md), and [CURRENT_RESULTS.md](https://github.com/GettysburgResearch/riemann/blob/f99d9e3908dde4865377c75d9ca051c1f545bf4f/research/integrated/CURRENT_RESULTS.md). Root review supplied these exact overlap locations. The new content here is the explicit same-order construction, the exact critical-value interval and degree scale, and the density/heat-bath calculations.

Public web search and direct primary-page retrieval returned service errors during this lane. GitHub retrieval remained available. Consequently no global novelty claim is made for these elementary constructions or identities. Laguerre and Hermite identities, Jensen theory, root dynamics and LP closure are classical frameworks; the proofs here are included rather than imported on an unverified citation. A dedicated primary-literature novelty check remains necessary before presenting any lemma as a publication novelty.

Run:

```sh
python experiments.py --output results.json
```

The script uses only the Python standard library. Exact finite claims use rational arithmetic and Sturm's theorem; root locations and threshold decimal tables are explicitly separated as floating illustrations. No external proof checker or zeta zero computation was run. The mathematical statements depend on the displayed proofs, not on fitting the numerical tables.
