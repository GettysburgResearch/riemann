# L-91021 — The dyadic Cauchy gate is unconditionally positive at every sufficiently large scale

Claim ID: `L-91021`  
Status: **PROPOSED COMPLETE UNCONDITIONAL TERMINAL-SCALE THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-11  
Depends on: the exact Cauchy soft count of `T-91004`; standard uniform Stirling estimates in the closed right half-plane; absolute Euler convergence for `-zeta'/zeta` in `Re(s)>1`  
RH status: **unproved**

## 1. The completed soft count

Put

\[
 s_x=\frac12+ix,
 \qquad
 p_x(a)=\Re\frac{\xi'}{\xi}(s_x+a),
\]

and

\[
 \mathcal N_x(a)
 =\frac12\left[a p_x(a)-a^2p_x'(a)\right].
 \tag{L-91021.1}
\]

The dyadic gate is

\[
 \mathcal G_x(a)=\mathcal N_x(2a)-\mathcal N_x(a).
 \tag{L-91021.2}
\]

No hypothesis on the zeros is made in this note.

## 2. Uniform completed-log-derivative asymptotics

Let

\[
 w=a+\frac12+ix,
 \qquad R=|w|.
\]

Uniform Stirling in `Re(w)>=3/2` and absolute Euler convergence give, for
`a>=1`,

\[
 \boxed{
 p_x(a)
 =\frac12\log\frac{R}{2\pi}
 +O\left(\frac1R\right)
 +O(a^C2^{-a}),
 }
 \tag{L-91021.3
}
\]

and

\[
 \boxed{
 p_x'(a)
 =\frac12\Re\frac1w
 +O\left(\frac1{R^2}\right)
 +O(a^C2^{-a}).
 }
 \tag{L-91021.4}
\]

Here and below `C` and every implied constant are absolute.  The exponentially
small terms follow by termwise differentiation of

\[
 -\frac{\zeta'}{\zeta}(w)
 =\sum_{n\ge2}\Lambda(n)n^{-w}
\]

and the elementary estimate of the resulting sums by their first exponential
scale.

Since `a/R<=1` and `a^2/R^2<=1`, (L-91021.1) becomes

\[
 \boxed{
 \mathcal N_x(a)
 =\frac a4\log\frac{|a+1/2+ix|}{2\pi}
 -\frac{a^2}{4}\Re\frac1{a+1/2+ix}
 +O(1)
 }
 \tag{L-91021.5}
\]

uniformly in `a>=1` and `x in R`.

## 3. Uniform lower bound for the dyadic gap

Write

\[
 R_1=|a+1/2+ix|,
 \qquad
 R_2=|2a+1/2+ix|.
\]

Then `R_2>=R_1`, `R_2>=2a+1/2`, and

\[
 0\le a^2\Re\frac1{2a+1/2+ix}
 \le\frac a2.
 \tag{L-91021.6}
\]

The corresponding reciprocal term from `N_x(a)` enters the dyadic difference
with the favourable sign and may be discarded.  Using (L-91021.5),

\[
\begin{aligned}
 \mathcal G_x(a)
 \ge{}&
 \frac a2\log\frac{R_2}{2\pi}
 -\frac a4\log\frac{R_1}{2\pi}
 -\frac a2-O(1)\\
 \ge{}&
 \boxed{
 \frac a4\log\frac{R_2}{2\pi}
 -\frac a2-O(1).
 }
 \tag{L-91021.7}
\end{aligned}
\]

Therefore there exists an effective absolute constant `A_0` such that

\[
 \boxed{
 \mathcal N_x(2a)-\mathcal N_x(a)>0
 \qquad(a\ge A_0,\ x\in\mathbb R).
 }
 \tag{L-91021.8}
\]

The proof is completely unconditional and uniform in the carrier.

A more quantitative form is

\[
 \mathcal G_x(a)
 \ge c a\log(2+a+|x|)-Ca
 \tag{L-91021.9}
\]

for absolute positive constants `c,C` and all `a>=1`.

## 4. Interpretation

Every hypothetical off-line pair produces a hyperbolic Cauchy block at every
finite scale, but the completed high-scale gate is dominated by the growing
archimedean zero density.  Thus the route has an unconditional terminal
condition:

```text
all dyadic gates are positive once the scale reaches A_0.
```

A lossless coefficient-one index recurrence from scale `a` to `2a` would
therefore close the full route after finitely many iterations.

The forward completely positive contraction of `L-91020` is not sufficient for
that backward implication.  The missing theorem remains the exact no-loss
identification of its Stinespring complement with the physical Cauchy detail
ports.

## 5. Boundary

Closed:

```text
uniform completed-log-derivative asymptotic;
uniform prime-side exponential tail at large horizontal shift;
unconditional large-scale dyadic gate;
effective terminal scale for every carrier.
```

Open:

```text
lossless backward/index recurrence from a to 2a;
physical identification of the inherited source details;
positivity of every subterminal dyadic gate;
RH.
```
