# Independent heat-trace audit and a local-monotonicity countermodel

Reviewer: dynamics lane. Date: 30 October 2026.  
Reviewed object: `swarm/heat_trace/report.md`, including the uniform small-time assertion for every integer n≥400.  
Outcome: **no blocking mathematical error found, conditional on the stated counting and finite-verification inputs.** The review independently checked the phase cancellation, the all-order uniformity, the infinite-tail estimate, and the logical distinction between local and global complete monotonicity.

## 1. Why the small-time estimate is genuinely uniform in n

Write y=gamma sqrt(t), u=delta sqrt(t), r=sqrt(n). The exact phase is

$$\psi=2yu-2n\arctan(u/y).$$

Near the saddle y=r, the potentially large terms cancel. This is an algebraic cancellation inside each summand, not an assumption about cancellation among zeros. When |y−r|≤10 and n≥400, y≥r/2≥10, so

$$|2u(y-n/y)|
 =2|u|\,|y-r|(1+r/y)\le6|u|\,|y-r|.$$

The remaining arctangent error is at most 2n|u|³/(3y³), uniformly bounded because n/y³≤8/sqrt(n). With |u|≤1/2000, both bounds are much smaller than 1/2. There is no hidden factor growing with n in this phase estimate.

The central-window lower bound also checks: putting y=r+h, |h|≤1/2, the inequality log(1+h/r)≥h/r−h²/r² gives

$$y^{2n}e^{-y^2}\ge n^ne^{-n}e^{-3h^2}.$$

The complex modulus is larger than this real-axis modulus. The counting-law lower bound supplies at least L log(X)/20 central zeros, with L=t^(−1/2) and X=sqrt(n/t). The stated endpoint errors are safely smaller than the main term because L≥1000.

For the full tail, the identity v²=y²+u² and log(v/r)≤v/r−1 imply

$$v^{2n}e^{-v^2}\le n^ne^{-n}e^{-(v-r)^2}.$$

This is uniform in n and uses no asymptotic expansion in n. The possible complex modulus correction is only e^(2u²). The complete shell sum is bounded by

$$4n^ne^{-n}t^{-n}L\log X
 \sum_{k\ge10}(k+1)e^{-(k-1)^2}.$$

The claimed bound 3/2^78 on the last sum is correct: (k−1)²≥k+71 for k≥10, and the resulting geometric sum equals 3/2^78 after replacing e by 2. The central positive mass has a large margin over this tail.

Thus the proof is not merely a fixed-order small-time asymptotic. Its positivity range at sufficiently small time is genuinely simultaneous in all n≥400. The separate retained-zero estimate covers the finitely many lower orders, given the stated verified-height input.

## 2. Checks of the other regimes

- In the low-order argument, b and phi have the same sign, so bounding both |b|t and n|phi| by pi/2 bounds their difference by pi/2. The necessary condition for a negative term, t>pi/(2 gamma), follows from |b|≤gamma. The reciprocal-square tail comparison and its exponential margin have the correct signs.
- In the large-time argument, log(17x)≤3x for x≥1 and n≤10^(−6)U²/8 produce an exponent at most −10^(−6)gamma²/2. The comparison with the retained real zero is uniform in n throughout the claimed finite hierarchy.
- The numerical endpoint U=3·10^12 gives U²/(8·10^6)=1.125·10^18. It is a consequence of the inequalities, not a claimed count of evaluated derivatives.
- Normal convergence for fixed derivatives at positive time follows from the strip bound and the stated counting estimate. Functional-equation symmetry supplies reality. These ingredients do not themselves assert positivity of higher Hankel minors.

This review did not independently reverify the published zero census or reconstruct the cited explicit counting theorem. Those remain attributed external inputs, as the report states.

## 3. Local all-order complete monotonicity does not propagate globally

The following explicit countermodel answers the possible logical concern. Define

$$f(t)=\frac1t+e^{-t}\cos t
 =\int_0^\infty e^{-t\lambda}\,d\lambda
   +\frac12e^{-(1-i)t}+\frac12e^{-(1+i)t},\qquad t>0.$$

It is analytic on the right half-plane and tends to zero as real t tends to infinity. It is a real positive-spectrum background with one conjugate complex exponential pair. It is not the zeta heat trace and is not asserted to satisfy zeta's counting input.

### All derivative signs hold on one fixed small-time interval

For every integer n≥0,

$$(-1)^nf^{(n)}(t)
 =\frac{n!}{t^{n+1}}
 +e^{-t}\Re\bigl((1-i)^ne^{it}\bigr).$$

The ratio of the possible negative perturbation to the first term is bounded by

$$t e^{-t}\frac{(\sqrt2t)^n}{n!}
 \le t e^{(\sqrt2-1)t}.$$

For every 0<t≤1/10 this is less than 1/5, using sqrt(2)−1<1 and e^(1/10)<2. Hence

$$\boxed{(-1)^nf^{(n)}(t)>\frac45\frac{n!}{t^{n+1}}>0
\quad(n\ge0,\ 0<t\le1/10).}$$

All orders are covered by one common interval.

### The first two signs even hold for every positive time

Since t e^(−t)≤1/e<1,

$$f(t)\ge1/t-e^{-t}>0.$$

Also,

$$-f'(t)=t^{-2}+e^{-t}(\cos t+\sin t)
 \ge t^{-2}-\sqrt2e^{-t}>0.$$

For the last inequality, max t²e^(−t)=4/e², and
4sqrt(2)/e²<24/25<1 follows from sqrt(2)<3/2 and e>5/2. Thus the example retains global positivity of both f and its first alternating derivative.

### A higher sign fails at a larger time

At t=7pi/2,

$$(-1)^{10}f^{(10)}(t)=\frac{10!}{t^{11}}-32e^{-t}<0.$$

Indeed 10<t<11, e<3, and the exact integer comparison

$$10!\,3^{11}<32\,10^{11}$$

gives
10!/t^11<10!/10^11<32/3^11<32e^(−t).

Therefore even local complete monotonicity of **all orders**, analytic continuation throughout Re t>0, decay at positive infinity, and global positivity of f and −f' do not imply global complete monotonicity. The root report's small-time assertion is logically compatible with failure in the unresolved higher-order/larger-time regime.

The parent suggested the unit-amplitude version used here; this reviewer checked its exact derivative phase and added the global −f' inequality. An earlier larger-amplitude example also worked but lost global positivity of f, so this version tests the report's scope more closely.

## 4. Suggested exposition clarification

The report can explicitly say that it proves **all-order positivity on a fixed small-time interval**, as well as a **finite, height-dependent order range for all positive times**. These are different quantifier statements. The countermodel above explains why the former does not silently settle the missing latter statement at arbitrarily high orders. No correction to the theorem or its constants is required by this audit.
