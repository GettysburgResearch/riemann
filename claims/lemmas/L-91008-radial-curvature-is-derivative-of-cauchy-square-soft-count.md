# L-91008 — Radial xi curvature is the derivative of a squared-Cauchy soft zero count

Claim ID: `L-91008`  
Status: **PROPOSED COMPLETE EXACT TRANSFORM LEMMA — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-11  
Depends on: PR #394, especially `L-91004/T-91002`  
RH status: **unproved**

## 1. Definition

Fix a real centre \(x\), put

\[
 s_x=\frac12+ix,
 \qquad
 L(s)=\frac{\xi'(s)}{\xi(s)},
\]

and, away from a zero of the sampled function, define

\[
 p_x(a)=\Re L(s_x+a),
 \qquad a>0.
\]

The radial curvature of PR #394 is

\[
 \mathcal C_x(a^2)
 =
 \frac{
 p_x(a)-a p_x'(a)-a^2p_x''(a)
 }{8a^3}.
 \tag{L-91008.1}
\]

Define the **Cauchy-square soft count**

\[
 \boxed{
 \mathcal N_x(a)
 =
 \frac12\left[
 a\,p_x(a)-a^2p_x'(a)
 \right].
 }
 \tag{L-91008.2}
\]

Then direct differentiation gives

\[
 \boxed{
 \mathcal N_x'(a)
 =
 4a^3\mathcal C_x(a^2).
 }
 \tag{L-91008.3}
\]

Equivalently,

\[
 \mathcal N_x(a)
 =
 -\frac{a^3}{2}
 \frac{d}{da}\left(\frac{p_x(a)}a\right).
 \tag{L-91008.4}
\]

Thus the conclusion-producing radial-concavity theorem of PR #394 is exactly
monotonicity of one soft local zero count.

## 2. Exact zero expansion

Write a critical-line zero as

\[
 \rho=\frac12+i\gamma,
 \qquad
 u=\gamma-x.
\]

Its contribution to \(p_x(a)\) is

\[
 \frac{a}{a^2+u^2},
\]

and its contribution to the soft count is

\[
 \boxed{
 n_{a,0}(u)
 =
 \frac{a^4}{(a^2+u^2)^2}
 =
 \left(
 \frac{a^2}{a^2+u^2}
 \right)^2.
 }
 \tag{L-91008.5}
\]

This lies in \([0,1]\), increases with \(a\), and tends from zero to one as the
resolution crosses the ordinate gap.

For a right-side reflected pair, write the centred coordinate as

\[
 z=d+iu,
 \qquad
 0<d<\frac12.
\]

The pair contribution to \(p_x(a)\) is

\[
 \Re\frac{2a}{a^2-z^2}
 =
 \frac{a-d}{(a-d)^2+u^2}
 +
 \frac{a+d}{(a+d)^2+u^2}.
 \tag{L-91008.6}
\]

Its contribution to the soft count is

\[
 \boxed{
 n_{a,d}(u)
 =
 2\Re\frac{a^4}{(a^2-z^2)^2}.
 }
 \tag{L-91008.7}
\]

Differentiating atomwise yields

\[
 \boxed{
 \frac{d}{da}n_{a,d}(u)
 =
 -8a^3
 \Re\frac{z^2}{(a^2-z^2)^3},
 }
 \tag{L-91008.8}
\]

which is \(4a^3\) times the reflected-pair curvature kernel of PR #394.

The standard zero count makes the complete sums absolutely convergent for
every fixed \(a>0\) away from a matched singularity. Hence

\[
 \boxed{
 \begin{aligned}
 \mathcal N_x(a)
 ={}&
 \sum_{\rho=1/2+i\gamma}
 m_\rho
 \frac{a^4}{[a^2+(\gamma-x)^2]^2}\\
 &+
 2\sum_{\Re\rho>1/2}
 m_\rho
 \Re
 \frac{a^4}
 {[a^2-(\rho-s_x)^2]^2}.
 \end{aligned}
 }
 \tag{L-91008.9}
\]

## 3. RH and common-width monotonicity

Under RH the second sum in (L-91008.9) is absent. Every remaining atom is
monotone:

\[
 \frac{d}{da}
 \frac{a^4}{(a^2+u^2)^2}
 =
 \frac{4a^3u^2}{(a^2+u^2)^3}
 \ge0.
 \tag{L-91008.10}
\]

Thus

\[
 \mathrm{RH}
 \Longrightarrow
 \mathcal N_x'(a)\ge0
 \qquad(x\in\mathbb R,\ a>0).
 \tag{L-91008.11}
\]

Conversely, if

\[
 \rho=\frac12+y+i\gamma
\]

is off the line, then at the matched centre \(x=\gamma\),

\[
 n_{a,y}(0)
 =
 \frac{2a^4}{(a^2-y^2)^2}
\]

and

\[
 \frac{d}{da}n_{a,y}(0)
 =
 -\frac{8a^3y^2}{(a^2-y^2)^3}<0
 \qquad(a>y).
 \tag{L-91008.12}
\]

The derivative tends to \(-\infty\) as \(a\downarrow y\) from the right, while
all distinct zero terms are less singular there. Hence every off-line zero
causes a strict local failure of monotonicity.

## 4. First-Hermite precursor

PR #394 proves

\[
 \mathcal C_x(t)
 =
 \frac12\int_0^\infty q^2e^{-tq}M(q,x)\,dq,
 \tag{L-91008.13}
\]

where \(M(q,x)\) is the first-Hermite zero-heat scalar. Integrating
(L-91008.3) from \(0\) to \(a\) gives, whenever the interchange is justified,

\[
 \boxed{
 \mathcal N_x(a)
 =
 \int_0^\infty
 \left[
 1-(1+qa^2)e^{-qa^2}
 \right]M(q,x)\,dq.
 }
 \tag{L-91008.14}
\]

The multiplier in square brackets is nonnegative. Thus the complete transform
chain has the additional primitive level

```text
first-Hermite zero heat
 -> Cauchy-square soft count
 -> radial curvature by differentiation
 -> safe-line jet / Hausdorff / Pick descriptions.
```

Equation (L-91008.14) is not an unconditional positivity proof because
\(M(q,x)\) is exactly the RH-bearing signed heat scalar.

## 5. Boundary

Established here:

```text
radial curvature = derivative of one soft count;
exact line and reflected-pair soft-count kernels;
line atoms are squared Cauchy/Poisson resolutions;
off-line matched pair forces a negative derivative;
first-Hermite-to-soft-count integral transform.
```

Not established here:

```text
prime-side monotonicity of the soft count;
radial curvature positivity;
RH.
```
