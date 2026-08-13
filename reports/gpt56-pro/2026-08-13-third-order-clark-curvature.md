# Third-order Clark curvature: the first open matrix level is one scalar inequality

Date: 2026-08-13  
Branch: `research/gpt56-pro/92000-third-order-clark-curvature`  
Parent: PR #438 at `bb7327d21c47410820cda2671f45dbe709a72eea`  
Live main observed during the pass: `9c7538559d7f56c2914b39aed5a1fb3fbf7ce131`  
Status: **research deposit; RH unproved**

## Executive result

PR #438 reduced RH to positivity of the finite safe-real Caratheodory matrices

\[
 \mathcal H_{ij}
 =\frac{F(x_i)+F(x_j)}{x_i+x_j},
 \qquad
 F(x)=\frac{\xi'}{\xi}\left(\frac12+x\right),
 \qquad x_i>\frac12,
\]

and proposed that all one- and two-node packets are positive unconditionally.
It also supplied an exact off-line control whose first negative packet has
three nodes.

The present pass solves the algebra of that first open level.

Put

\[
 p(t)=\frac{F(\sqrt t)}{\sqrt t}.
\]

For three nodes, the determinant is exactly

\[
\det\mathcal H
=\frac{p_1p_2p_3\Delta(t)^2}
       {\prod_{i<j}(x_i+x_j)^2}
 [t_1,t_2,t_3](1/p)
 [t_1,t_2,t_3](tp).
\]

The matrix sign has therefore become a product of two scalar curvatures.

The second curvature is proposed closed unconditionally:

\[
 (tp)''<0
 \qquad(t>1/4).
\]

The proof is orbitwise and uses only the very weak fact that nontrivial zeta
zeros have ordinate larger than `sqrt(3)` in modulus.

Hence every actual-Xi three-node packet is positive if and only if

\[
 \left(\frac1p\right)''\le0.
\]

Equivalently, the complete order-three gate is

\[
\boxed{
 x^2F F''-2x^2(F')^2+xFF'+F^2\ge0
 \qquad(x>1/2).
}
\]

This is a one-dimensional safe-Euler inequality.

## 1. Why this is structurally different from another determinant calculation

The determinant factorization is not a numerical convenience.  It identifies
the finite-order Stieltjes geometry behind the safe Pick hierarchy.

At orders one and two the required scalar data are:

```text
p>0;
p decreasing;
tp increasing.
```

At order three the only new datum is:

```text
1/p concave.
```

The companion `tp` concavity is automatic for the actual Xi zero geometry.
This pattern suggests that higher orders should be expressed through the
continued-fraction or finite-string coefficients of `p`, not through raw
`N x N` determinants.

## 2. Exact determinant algebra

For `t_i=x_i^2` and `p_i=p(t_i)`,

\[
 H_{ij}=\frac{x_ip_i+x_jp_j}{x_i+x_j}.
\]

The two-node determinant is

\[
 \det H_{ij}
 =-\frac{(p_i-p_j)(t_ip_i-t_jp_j)}{(x_i+x_j)^2}.
\]

The three-node determinant factors into the second divided differences of
`1/p` and `tp`.  The verifier reconstructs this identity over exact rational
arithmetic and reproduces the exact negative control determinant

\[
 -\frac{201516024836691562500}
 {1055839030806150723363641645963}.
\]

## 3. Why `tp` is concave orbit by orbit

A critical-line orbit of ordinate `b` contributes

\[
 p_{0,b}(t)=\frac{2m}{t+b^2}
\]

and

\[
 (tp_{0,b})''=-\frac{4mb^2}{(t+b^2)^3}<0.
\]

For an off-line orbit `a+ib`, put

\[
 c=b^2-a^2,
 \qquad B=2ab,
 \qquad U=t+c.
\]

Its complete quadruple contributes

\[
 p_{a,b}(t)=\frac{4mU}{U^2+B^2}.
\]

The curvature numerator reduces to

\[
 U^4\left[q(1-3r^2)+r^2(3-r^2)\right],
 \qquad q=c/U,\quad r^2=B^2/U^2.
\]

On the safe axis, `U>b^2`; hence `|r|<1/|b|`.  At actual zeta heights
`r^2<1/3`, making the bracket strictly positive and `(tp)''` strictly
negative.

## 4. Why the reciprocal curvature is genuinely collective

For one off-line orbit,

\[
 \frac1{p_{a,b}(t)}
 =\frac1{4m}\left(U+\frac{B^2}{U}\right),
\]

so

\[
 \left(\frac1{p_{a,b}}\right)''
 =\frac{B^2}{2mU^3}>0.
\]

Thus the hard curvature has the wrong sign on every off-line orbit by itself.
The actual Xi inequality, if true, must arise only after the complete zero or
prime/gamma system has been combined.

This is consonant with Claude's successful finite-compression mechanism: the
indefinite geometry must be read at the level of the complete Hermitian object,
not by assigning signs to individual off-line contributions.

## 5. Safe arithmetic form

For `s=1/2+x>1`, write

\[
 P_k(s)=\sum_{n\ge2}\Lambda(n)(\log n)^k n^{-s}.
\]

Then

\[
\begin{aligned}
 F={}&\frac1s+\frac1{s-1}-\frac12\log\pi
     +\frac12\psi(s/2)-P_0(s),\\
 F'={}&-\frac1{s^2}-\frac1{(s-1)^2}
      +\frac14\psi_1(s/2)+P_1(s),\\
 F''={}&\frac2{s^3}+\frac2{(s-1)^3}
       +\frac18\psi_2(s/2)-P_2(s).
\end{aligned}
\]

Every series is absolutely convergent.  The remaining order-three sign is
therefore available to a directed computation using no zero data.

## 6. Large-axis closure

Stirling and the safe Euler series give

\[
 F=\frac12\log\frac{x}{2\pi}+O(x^{-1}),
 \quad
 F'=\frac1{2x}+O(x^{-2}),
 \quad
 F''=-\frac1{2x^2}+O(x^{-3}).
\]

Therefore

\[
 x^2F''+xF'=O(x^{-1}),
\]

and

\[
 2x^2(F')^2=\frac12+O(x^{-1}).
\]

The hard curvature is

\[
 F^2-\frac12+O((F+1)/x),
\]

which is positive eventually.  Only a compact safe interval remains.

## 7. Retained diagnostics

The actual-Xi diagnostic samples the curvature at

```text
0.5001, 0.55, 0.75, 1, 2, 5, 10, 20, 50, 100.
```

The minimum sampled hard curvature is

```text
9.72106636403149e-10 > 0
```

and the largest sampled companion numerator is

```text
-7.41738343333236e-5 < 0.
```

These are high-precision floating-point values, not interval certificates.

## 8. Immediate completion plan

### Near `s=1`

Avoid the zeta pole by using

\[
 (s-1)\zeta(s)
 =\eta_D(s)\frac{s-1}{1-2^{1-s}}.
\]

The two factors on the right are analytic and positive near one.  Differentiate
their logarithms with directed enclosures.

### Middle compact interval

Use interval Euler--Maclaurin or a rigorously bounded eta acceleration for
`F,F',F''`.  Evaluate the scalar numerator directly, retaining correlations
between the three derivatives rather than bounding every term independently.

### Tail

Choose an explicit threshold and use Stirling with Bernoulli remainder plus an
all-integer majorant for the prime-power tails.

## 9. Exact boundary

```text
three-node determinant factorization                  EXACT
off-line reciprocal-curvature firewall                EXACT
actual-Xi companion curvature                          PROPOSED UNCONDITIONAL
large-axis hard curvature                              PROPOSED COMPLETE
compact safe-axis hard curvature                       OPEN / DIRECTED
all actual-Xi packets of size <=3                      CONDITIONAL ON COMPACT SIGN
all packet sizes                                       OPEN / RH-EQUIVALENT
Riemann Hypothesis                                     UNPROVED
```
