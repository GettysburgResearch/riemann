# R-91005 — A positive source/port identity does not force the zero ports to vanish

Claim ID: `R-91005`  
Status: **EXACT ONE-POLE FIREWALL**  
Created: 2026-08-12  
Depends on: `L-91034`  
RH status: **unproved**

## 1. Control model

Fix a point `p` in the right half-plane and put

\[
 b_p(z)=\frac{z-p}{z+\overline p},
 \qquad
 \Theta(z)=b_p(z)^{-1}.
 \tag{R-91005.1}
\]

The quotient `Theta` is boundary-unimodular and has one pole at `p`. Its pole-removing Blaschke factor is exactly `B=b_p`, and

\[
 B(z)\Theta(z)\equiv1.
 \tag{R-91005.2}
\]

Take no deterministic stable factor and take the scalar Cauchy multiplier to be one.

## 2. Exact decomposition

Since the pole-removed inner function is constant,

\[
 K_{B\Theta}=K_1=0.
\]

On the other hand,

\[
 \boxed{
 K_{\Theta}(z,w)
 =-
 \frac{K_{b_p}(z,w)}
 {b_p(z)\overline{b_p(w)}}.
 }
 \tag{R-91005.3}
\]

The port kernel is the nonzero positive rank-one square

\[
 \boxed{
 \frac{K_{b_p}(z,w)}
 {b_p(z)\overline{b_p(w)}}
 =\frac{2\Re p}
 {(z-p)(\overline w-\overline p)}.
 }
 \tag{R-91005.4}
\]

Thus the exact source/critical/port identity is

\[
 \boxed{
 0
 =K_\Theta
 +\frac{K_{b_p}}{b_p\overline{b_p}}.
 }
 \tag{R-91005.5}
\]

The source Gram is positive—indeed, it is identically zero—while the zero-port term is nonzero and exactly cancels the negative critical kernel.

## 3. Consequence

The following implication is false:

```text
positive safe source Gram
+ exact source = critical + stable + zero-port identity
=> zero-port term vanishes.
```

Neither positivity nor norm conservation can delete the pole port. One needs an additional **exhaustion/saturation theorem** proving that the explicitly arithmetic source norm is already completely used by the critical and deterministic outputs.

For the xi problem, that missing theorem can be phrased as either:

1. an arithmetic coisometry from the explicit Stinespring space of `L-91031` onto the pole-removed model-space source of `L-91034`, with no remaining output; or
2. a direct proof that the Blaschke pole factor `B_a` in `L-91034` is constant for every `a>0`.

The second statement is exactly RH. The first would imply the second only if the exhaustion identity is proved with the correct completed normalization.

## 4. Separate kernel warning

The scalar completely-monotone kernel of `L-91031` has the Hankel form

\[
 \mathcal S_a(z+\overline w).
\]

The pole-removed source kernel of `L-91034` has the de Branges--Rovnyak form

\[
 m_a(z)\overline{m_a(w)}
 \frac{1-I_a(z)\overline{I_a(w)}}{z+\overline w}.
\]

They are not equal merely because both are positive. An explicit intertwining operator or coisometry is required. Treating these two source Grams as identical would silently assume the remaining theorem.
