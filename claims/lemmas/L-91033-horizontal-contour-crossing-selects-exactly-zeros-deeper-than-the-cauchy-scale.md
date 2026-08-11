# L-91033 — Horizontal contour crossing selects exactly the zeros deeper than the Cauchy scale

Claim ID: `L-91033`  
Status: **EXACT MEROMORPHIC/DEPTH GEOMETRY**  
Created: 2026-08-12  
Depends on: `L-9506`, `L-91010`, `L-91031`  
RH status: **unproved**

## 1. Safe and critical variables

For `a>0`, the completed safe ratio is

\[
 H_{2a}(q)
 =\frac1q
  \frac{\xi(1+q)}{\xi(1+2a+q)}.
 \tag{L-91033.1}
\]

At the critical Clark boundary put

\[
 q=q_a(x):=-\frac12-a+ix.
\]

Then exactly

\[
 \boxed{
 H_{2a}(q_a(x))
 =\frac1{q_a(x)}
  \frac{\xi(1/2-a+ix)}{\xi(1/2+a+ix)}.
 }
 \tag{L-91033.2}
\]

Thus the critical scattering ratio is reached by moving the `q` contour from the safe half-plane to

\[
 \Re q=-\frac12-a.
\]

## 2. Location of zero poles

Let

\[
 \rho=\frac12+d+i\gamma,
 \qquad -\frac12<d<\frac12,
\]

be a nontrivial xi zero. The denominator in (L-91033.1) creates a pole at

\[
 \boxed{
 q_\rho=\rho-1-2a
 =-\frac12+d-2a+i\gamma.
 }
 \tag{L-91033.3}
\]

Its horizontal position relative to the target contour is

\[
 \Re q_\rho-\left(-\frac12-a\right)=d-a.
\]

Therefore

\[
 \boxed{
 \begin{array}{lll}
 d>a&\Longleftrightarrow&q_\rho\text{ is crossed};\\
 d=a&\Longleftrightarrow&q_\rho\text{ lies on the target contour};\\
 d<a&\Longleftrightarrow&q_\rho\text{ remains to its left}.
 \end{array}
 }
 \tag{L-91033.4}
\]

The contour continuation is an exact cumulative horizontal-depth selector.

Critical-line zeros have `d=0`, so for every `a>0` their denominator poles remain strictly to the left of the target contour. They generate the ordinary boundary Clark measure but no crossed hyperbolic port.

## 3. Deterministic stable-state poles

The Cauchy storage factor contains the stable denominators

\[
 (q+a)^2(q+2a)^2(q+4a)^2.
\]

On the RH-sensitive interval `0<a<1/2`, moving to the Clark contour crosses:

1. `q=-a` for every `a`;
2. `q=-2a` for every `0<a<1/2`;
3. `q=-4a` exactly when `0<a<1/6`.

These are deterministic exponential/Erlang states. Their residues are the finite causal ports encoded by the two-state rotation and its symmetric-square lift in `L-91025`. They are not zeta-zero obstructions.

The remaining rational completed pole at `q=-1-2a` and the first numerator-Gamma pole at `q=-1` lie to the left of the Clark contour and are not crossed.

## 4. Residue decomposition

After the deterministic stable ports are retained explicitly, the only source-dependent residues crossed in the continuation are

\[
 \boxed{
 \{\rho:\Re\rho-1/2>a\}.
 }
 \tag{L-91033.5}

Pairing functional-equation reflections converts each crossed right-side zero into the hyperbolic two-state block of `L-91010/L-91025`. At a matching ordinate, the block degenerates to the negative rank-one Cauchy/Pick witness.

As `a` decreases, a pair enters the crossed set exactly when the scale passes its horizontal depth. Differentiating the cumulative residue ledger recovers the sharp depth projector of `L-91005/L-91009`.

## 5. Correct CJHI statement

The completed source-to-boundary theorem must therefore have the form

\[
 \boxed{
 \text{safe positive source Gram}
 =\text{critical Cauchy Gram}
  +\text{deterministic stable ports}
  +\text{crossed hyperbolic zero ports}.
 }
 \tag{L-91033.6}

Under RH the last term is absent. Under false RH it is nonempty for every scale below the depth of an off-line zero and contains one expanding direction per reflected pair.

A proof that silently discards the crossed residues is circular. A valid conservative colligation must:

1. retain all deterministic poles with their exact multiplicities;
2. show coefficient-one return of the neutral state;
3. identify every source-dependent crossed residue;
4. prove that no such hyperbolic port exists.

The last assertion is equivalent to RH. Equation (L-91033.4) is an exact classification, not a proof that the crossed set is empty.