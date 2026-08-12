# L-91315 — A cocycle-aligned node path returns one fixed Green state with coefficient one

Claim ID: `L-91315`  
Status: **EXACT COMPLETED-XI COCYCLE AND POSITIVE SAFE-FEATURE ALIGNMENT; BOUNDARY EXHAUSTION OPEN**  
Created: 2026-08-12  
Depends on: `L-91313`, main `L-9506/L-91014/L-91027`  
RH status: **unproved**

## 1. A fixed Green parameter

Fix once and for all

\[
 q_0>0.
 \tag{L-91315.1}
\]

For every `a>0`, choose the right-half-plane node

\[
 \boxed{
 \eta_a=\frac12+a+q_0.
 }
 \tag{L-91315.2}
\]

Then

\[
 \frac12-a+\eta_a=1+q_0,
 \qquad
 \frac12+a+\eta_a=1+q_0+2a,
 \tag{L-91315.3}
\]

so

\[
 \boxed{
 \Theta_a(\eta_a)
 =\frac{\xi(1+q_0)}{\xi(1+q_0+2a)}.
 }
 \tag{L-91315.4}
\]

Every value is on the absolutely convergent safe real axis.

## 2. Exact one-Green feature

The completed one-Green ratio is

\[
 \mathcal H_{2a}(q)
 =\frac1q\frac{\xi(1+q)}{\xi(1+2a+q)}
 =\int_0^\infty e^{-qt}\,d\mu_{2a}(t),
 \qquad \mu_{2a}\ge0.
 \tag{L-91315.5}
\]

Thus

\[
 \boxed{
 \Theta_a(\eta_a)
 =q_0\mathcal H_{2a}(q_0)
 =\left\|\sqrt{q_0}e^{-q_0t/2}\right\|_{L^2(\mu_{2a})}^2.
 }
 \tag{L-91315.6}
\]

The test function `sqrt(q_0)e^(-q_0t/2)` is independent of the scale `a`.
Only the positive source measure changes.

## 3. Exact horizontal cocycle

The completed quotient satisfies

\[
 \boxed{
 \Theta_{a+b}(z)
 =\Theta_a(z-b)\Theta_b(z+a).
 }
 \tag{L-91315.7}
\]

Indeed the intermediate Xi factors cancel directly. At `b=a` and
`z=eta_(2a)=1/2+2a+q_0`,

\[
 \boxed{
 \Theta_{2a}(\eta_{2a})
 =\Theta_a(\eta_a)
  \Theta_a(\eta_a+2a).
 }
 \tag{L-91315.8}
\]

The first factor is the returned state at the same fixed Green parameter
`q_0`. The second factor is

\[
 \boxed{
 \Theta_a(\eta_a+2a)
 =\frac{\xi(1+q_0+2a)}{\xi(1+q_0+4a)}
 =(q_0+2a)\mathcal H_{2a}(q_0+2a).
 }
 \tag{L-91315.9}
\]

Therefore

\[
 \boxed{
 q_0\mathcal H_{4a}(q_0)
 =\bigl[q_0\mathcal H_{2a}(q_0)\bigr]
  \bigl[(q_0+2a)\mathcal H_{2a}(q_0+2a)\bigr].
 }
 \tag{L-91315.10}
\]

This is the completed-xi version of the generalized-Jordan divisor cocycle.

## 4. Coefficient-one state interpretation

Let

\[
 \phi_{a,q}(t)=\sqrt q\,e^{-qt/2}
 \in L^2(\mu_{2a}).
 \tag{L-91315.11}
\]

Equation (L-91315.10) says that the coarse amplitude at scale `2a` factors
into

```text
one returned q_0 state at scale a
x one shifted q_0+2a detail state at scale a.
```

The returned scalar coefficient is exactly one. This is the one-node analogue
of the coefficient-one divisor isometry and of the coefficient-one Cauchy
storage recurrence.

A source-side tensor isometry realizing (L-91315.10) for the complete
rational/Beta/Jordan measures is the natural safe input to the final
one-node boundary map.

## 5. One-node zero-port detection along the path

At every scale,

\[
 \mathcal K_a^{\rm hyp}(\eta_a,\eta_a)
 =\frac{1-|B_a(\eta_a)|^2}
        {2\eta_a|B_a(\eta_a)|^2}.
 \tag{L-91315.12}
\]

Therefore exact arithmetic norm exhaustion at the cocycle-aligned node deletes
all crossed zeros deeper than `a`.

For any sequence `a_j downarrow0`, the same fixed Green test `q_0` may be used
at every generation. No moving test family or carrier interpolation is needed.

## 6. Two complementary alignments

`L-91314` chooses

\[
 \eta_a=\frac12+3a,
 \]

which lands exactly on the canonical Jordan anchor
`k_(a,1/2+a)`.

The present lemma chooses

\[
 \eta_a=\frac12+a+q_0,
 \]

which keeps the one-Green test vector fixed and makes dyadic scale propagation
coefficient-one.

The final construction may use the anchor alignment to identify the local
first-chaos source and the cocycle alignment to iterate the state without loss.

## 7. Exact remaining theorem

Construct the completed source-to-model one-node isometry on the vectors
(L-91315.11), compatible with the tensor factorization (L-91315.10), and prove
that after the critical and deterministic stable outputs no norm remains.

This is the cocycle-aligned form of `ONAE_a`; it remains open and RH-bearing.
