# L-91010 — The completed shift ratio is a common-depth Clark family under RH

Claim ID: `L-91010`  
Status: **PROPOSED COMPLETE EXACT STRUCTURAL LEMMA — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-11  
Depends on: `L-91008`; the functional equation and reality of \(\xi\)  
RH status: **unproved**

## 1. Completed shift ratio

For \(a>0\), define

\[
 \boxed{
 \Theta_a(s)
 =
 \frac{\xi(s-a)}{\xi(s+a)}.
 }
 \tag{L-91010.1}
\]

On the critical boundary \(s_x=1/2+ix\), the functional equation and
conjugation give

\[
 \xi(s_x-a)
 =
 \overline{\xi(s_x+a)}.
\]

Hence, wherever the quotient is defined,

\[
 \boxed{|\Theta_a(s_x)|=1.}
 \tag{L-91010.2}
\]

Let

\[
 \phi_a(x)=\arg\Theta_a(s_x).
\]

With

\[
 p_x(a)=\Re\frac{\xi'}{\xi}(s_x+a),
\]

one has

\[
 \boxed{
 \partial_x\phi_a(x)=-2p_x(a).
 }
 \tag{L-91010.3}
\]

The Cauchy-square soft count of `L-91008` is therefore the mixed phase
curvature

\[
 \boxed{
 \mathcal N_x(a)
 =
 \frac{a^3}{4}
 \partial_a\left[
 \frac1a\partial_x\phi_a(x)
 \right].
 }
 \tag{L-91010.4}
\]

## 2. Common-depth Blaschke factors under RH

Assume RH. Pairing the centred zeros in the canonical product gives, up to an
\(a\)-dependent unimodular constant,

\[
 \Theta_a(s)
 =
 \prod_\gamma
 \frac{s-(1/2+a+i\gamma)}
      {s-(1/2-a+i\gamma)}.
 \tag{L-91010.5}
\]

Each factor is a half-plane Blaschke factor whose zero is at the same
horizontal distance \(a\) from the boundary. Thus \(\Theta_a\) is a
common-depth meromorphic inner function.

For one factor, at \(s=s_x\),

\[
 \partial_x\arg
 \frac{-a+i(x-\gamma)}
      {a+i(x-\gamma)}
 =
 -\frac{2a}{a^2+(x-\gamma)^2}.
\]

Therefore the boundary phase density is the common-width Poisson sum

\[
 p_x(a)
 =
 \sum_\gamma
 m_\gamma
 \frac{a}{a^2+(\gamma-x)^2},
 \tag{L-91010.6}
\]

and (L-91010.4) becomes

\[
 \boxed{
 \mathcal N_x(a)
 =
 \sum_\gamma
 m_\gamma
 \left[
 \frac{a^2}{a^2+(\gamma-x)^2}
 \right]^2.
 }
 \tag{L-91010.7}
\]

So the radial criterion is a rigidity statement for an inner family whose
Clark/Poisson atoms all have one common depth.

## 3. What an off-line pair changes

For a reflected pair at depth \(d\) and ordinate gap \(u\), the phase density
splits into two unequal widths:

\[
 \boxed{
 p_{d,u}(a)
 =
 \frac{a-d}{(a-d)^2+u^2}
 +
 \frac{a+d}{(a+d)^2+u^2}.
 }
 \tag{L-91010.8}
\]

The corresponding soft count is

\[
 2\Re\frac{a^4}{[a^2-(d+iu)^2]^2}.
\]

When \(a\) crosses \(d\), the first Poisson width changes sign and the matched
soft-count derivative develops the negative cubic singularity of
`T-91002`.

Thus an off-line pair is not merely a perturbation of the Clark density. It
breaks the common-depth geometry by splitting one width into \(a-d\) and
\(a+d\).

## 4. Scope

The quotient \(\Theta_a\) may have cancellations between numerator and
denominator zeros for a specially chosen fixed \(a\). No fixed-\(a\)
zero-free equivalence is asserted here. The robust conclusion-producing
statements are:

```text
all a / cofinal a -> 0 shift-ratio geometry;
or, equivalently, local soft-count monotonicity at every a.
```

The lemma supplies a canonical-system/Clark interpretation of the radial
criterion. It does not prove that the arithmetic shift ratio is inner or that
the soft count is monotone.
