# L-90204 — Euler–fragmentation Mellin factorization of every transported exit trace

Claim ID: `L-90204`  
Status: **PROPOSED COMPLETE EXACT TRANSFORM LEMMA — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-10  
Depends on: `L-90101` positive first-entrance kernels; elementary Mellin integration and Euler products  
Scope: exact transform and source/geometry separation in the initial half-plane; no continuation theorem through the critical strip, no sign theorem, and no RH conclusion

## 1. Endpoint-independent fragmentation trace

Fix a threshold `n` and a nonnegative endpoint-independent exit trace `alpha(p)` on `[n,2n)`. Let

\[
 G(m)=\sum_p\alpha(p)G_p(m)\ge0,
 \qquad G(n-1)=0,
 \tag{L-90204.1}
\]

where `G_p(m)=m E_n(m,p)` is the first-entrance transport of `L-90101`.

Put

\[
 a_G(m)=G(m)-G(m-1).
 \tag{L-90204.2}
\]

Since every hitting probability is at most one,

\[
 0\le G(m)\le C_\alpha m
 \tag{L-90204.3}
\]

for a constant depending only on the finite trace.

Retain the critical endpoint weight

\[
 w_X(q)=q^{-1/2}\log\frac Xq\,\mathbf1_{q\le X}.
 \tag{L-90204.4}
\]

For a complex class parameter `z`, define the common-prime-sign transport

\[
 \boxed{
 \mathcal F_z(X)
 =\sum_{k\ge1\atop k\ {m squarefree}}
   z^{\omega(k)}c_X(k),
 \qquad
 c_X(k)=\sum_{m\ge n}a_G(m)w_X(mk).
 }
 \tag{L-90204.5}
\]

For each fixed `X` the sums are finite. The Liouville/Möbius point is `z=-1`; the unit source is `z=0`; and `z=1` is the positive squarefree source.

Every single GFEP exit and every nonnegative exit mixture is covered. For the true hitting trace of `L-32301`, `mathcal F_{-1}(X)=nA_X(n)` is the sparse producer coefficient.

## 2. Mellin transform of one critical atom

For `q>=1` and `Re s>0`,

\[
 \boxed{
 \int_1^\infty w_X(q)X^{-s-1}\,dX
 =\frac{q^{-s-1/2}}{s^2}.
 }
 \tag{L-90204.6}
\]

Indeed the integral begins at `X=q`, and after `X=qv` it is

\[
 q^{-s-1/2}\int_1^\infty(\log v)v^{-s-1}dv
 =q^{-s-1/2}s^{-2}.
\]

## 3. Exact factorization

Define the fragmentation Dirichlet factor

\[
 \boxed{
 \mathcal A_G(s)
 =\sum_{m\ge n}a_G(m)m^{-s-1/2}.
 }
 \tag{L-90204.7}
\]

and the squarefree Euler factor

\[
 \boxed{
 \mathcal E_z(u)
 =\sum_{k\ge1\atop k\ {m squarefree}}
   \frac{z^{\omega(k)}}{k^u}
 =\prod_p(1+z p^{-u}).
 }
 \tag{L-90204.8}
\]

The Euler product converges absolutely for `Re u>1`. From (L-90204.3), the defining series for `A_G` converges absolutely for `Re s>3/2`. Hence for `Re s>3/2`, Fubini and (L-90204.6) give

\[
 \boxed{
 \widehat{\mathcal F_z}(s)
 :=\int_1^\infty\mathcal F_z(X)X^{-s-1}\,dX
 =\frac{\mathcal A_G(s)}{s^2}
  \mathcal E_z\!\left(s+\frac12\right).
 }
 \tag{L-90204.9}
\]

This separates the problem exactly into

```text
fragmentation / first-entrance geometry:   A_G(s)
arithmetic class source:                   E_z(s+1/2)
universal critical Riesz smoothing:        1/s^2.
```

There is no mixed remainder.

## 4. The fragmentation factor itself is positive on the real axis

Put `u=s+1/2`. Finite Abel summation, followed by the limit using `G(m)=O(m)`, gives for real `s>1/2`

\[
 \boxed{
 \mathcal A_G(s)
 =\sum_{m\ge n}G(m)
   \left[m^{-u}-(m+1)^{-u}\right]\ge0.
 }
 \tag{L-90204.10}
\]

If the trace is nonzero, then `A_G(s)>0` for every real `s>1/2`.

Equivalently,

\[
 \boxed{
 \mathcal A_G(s)
 =u\int_n^\infty
 G(\lfloor x\rfloor)x^{-u-1}\,dx.
 }
 \tag{L-90204.11}
\]

The right side converges absolutely and defines `A_G` analytically for `Re s>1/2`. Thus all possible real-axis sign changes of the transformed class family in this half-plane come from the Euler factor, not from fragmentation.

No zero-free claim for `A_G(s)` off the real axis is made.

## 5. Three distinguished sources

### Liouville/Möbius point

At `z=-1`,

\[
 \mathcal E_{-1}(u)
 =\prod_p(1-p^{-u})
 =\frac1{\zeta(u)}.
\]

Therefore

\[
 \boxed{
 \widehat{\mathcal F_{-1}}(s)
 =\frac{\mathcal A_G(s)}
 {s^2\zeta(s+1/2)}
 \qquad(\Re s>3/2),
 }
 \tag{L-90204.12}
\]

with the right side furnishing the exact formal continuation interface wherever `A_G` is continued.

Thus the reciprocal-zeta factor exposed by the earlier Möbius firewalls is not produced by the transport network. It is the **entire arithmetic Euler factor** of the Liouville boundary point.

### Unit source

At `z=0`,

\[
 \mathcal E_0=1,
 \qquad
 \boxed{
 \widehat{c_X(1)}(s)=\frac{\mathcal A_G(s)}{s^2}.
 }
 \tag{L-90204.13}
\]

This is the positive empty forcing of `T-90201/T-90203`.

### Positive squarefree source

At `z=1`,

\[
 \mathcal E_1(u)
 =\prod_p(1+p^{-u})
 =\frac{\zeta(u)}{\zeta(2u)},
\]

so

\[
 \boxed{
 \widehat{\mathcal F_1}(s)
 =\frac{\mathcal A_G(s)}{s^2}
  \frac{\zeta(s+1/2)}{\zeta(2s+1)}.
 }
 \tag{L-90204.14}
\]

The three points `-1,0,1` therefore interpolate exactly between reciprocal-zeta, no-Euler-factor, and positive-zeta arithmetic while leaving the same fragmentation factor untouched.

## 6. Bernstein expansion around the Liouville point

Write

\[
 t=z+1.
\]

Prime by prime,

\[
 1+z p^{-u}
 =(1-p^{-u})
 \left(1+\frac{t}{p^u-1}\right).
\]

Hence for `Re u>1`,

\[
 \boxed{
 \mathcal E_{-1+t}(u)
 =\frac1{\zeta(u)}
  \prod_p\left(1+\frac{t}{p^u-1}\right).
 }
 \tag{L-90204.15}
\]

Expanding the second product,

\[
 \boxed{
 \mathcal E_{-1+t}(u)
 =\frac1{\zeta(u)}
 \sum_{a\ {m squarefree}}
 t^{\omega(a)}
 \prod_{p\mid a}\frac1{p^u-1}.
 }
 \tag{L-90204.16}
\]

Every coefficient after the reciprocal-zeta factor is positive for real `u>1`. This is the Mellin/Euler counterpart of the physical-domain Boolean descendant hierarchy `T-90201`.

At `t=1` the product equals `zeta(u)` and cancels the reciprocal-zeta factor, recovering the unit source exactly.

## 7. A precise analytic boundary

Equation (L-90204.12) identifies what a transform-based completion would have to prove. A hypothetical zeta zero `rho` with `Re rho>1/2` corresponds to

\[
 s_\rho=\rho-\frac12,
 \]

outside the initial absolute half-plane. To turn (L-90204.12) into a pole-exclusion theorem one needs both:

1. analytic continuation of the fragmentation factor `A_G(s)` to `s=s_rho`;
2. a proof that `A_G(s_rho)` does not cancel the reciprocal-zeta pole for the chosen exit/trace.

Neither follows from real-axis positivity (L-90204.10). The lemma therefore does **not** claim that one fixed exit criterion is equivalent to RH.

This is nevertheless a sharp structural separation: any cancellation of an off-line zeta pole in a transported GFEP/sparse trace can only occur through the deterministic fragmentation transfer `A_G`, because the arithmetic part is exactly `1/zeta`.

## 8. Relation to the maximal positive-convolution cone

`T-90203` says positive source deformation `mu -> mu*h` replaces the current endpoint by a positive dilation superposition of descendants. In Mellin coordinates such dilation superposition multiplies (L-90204.12) by the Dirichlet series

\[
 H\!\left(s+\frac12\right)
 =\sum_a\frac{h(a)}{a^{s+1/2}}.
\]

Thus the maximal cone acts **only on the Euler/source factor**, exactly as the physical descendant theorem predicts. The fragmentation transfer remains unchanged.

The unit deformation `h=1` contributes `H=zeta` and cancels `1/zeta`; the inverse boundary step restores the reciprocal-zeta obstruction. This is the transform-level explanation of why positivity is lost precisely at Möbius inversion.

## 9. Proof boundary

Proved exactly:

- the atom Mellin integral;
- complete factorization into fragmentation, Euler, and Riesz factors;
- positive Abel/Stieltjes form of the fragmentation factor for real `s>1/2`;
- the exact `z=-1,0,1` specializations;
- the Euler/Bernstein expansion about Liouville;
- compatibility with the maximal positive-convolution cone.

Not proved:

- continuation of `A_G` into the RH-facing strip `0<Re s<=1/2`;
- nonvanishing of `A_G` at hypothetical off-line zero locations;
- the sign of the empty Möbius coefficient;
- GFEP, sparse producer positivity, or RH.
