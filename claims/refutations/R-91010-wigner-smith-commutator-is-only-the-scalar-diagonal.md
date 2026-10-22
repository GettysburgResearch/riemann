# R-91010 — The Wigner–Smith commutator is only the scalar diagonal

Claim ID: `R-91010`  
Status: **EXACT POLARIZATION REFUTATION OF `L-91038` AS A FULL-KERNEL REDUCTION**  
Created: 2026-08-12  
Refutes: the claim in `L-91038` that the complete delayed screw kernel is equivalent to one multiplication-operator commutator  
RH status: **unproved**

## 1. Scalar identity retained

Use Suzuki's boundary multiplier

\[
 \Theta_a(x)
 =\frac{\xi(1/2-a-ix)}{\xi(1/2+a-ix)}
\]

and put

\[
 q_a(x)=-i\Theta_a(x)^{-1}\partial_x\Theta_a(x),
 \qquad
 B_a(x)=-i\partial_a[a^{-1}\log\Theta_a(x)].
\]

Then

\[
 \partial_xB_a(x)=\partial_a[q_a(x)/a]
\]

and the scalar Cauchy soft count satisfies

\[
 \boxed{
 \mathcal N_x(a)
 =-\frac{a^3}{4}\,B_a'(x).
 }
 \tag{R-91010.1}
\]

With `P=-i partial_x`,

\[
 \boxed{
 M_{\mathcal N(a)}
 =-\frac{a^3}{4}i[P,M_{B_a}].
 }
 \tag{R-91010.2}
\]

This scalar multiplication-operator identity is exact.

## 2. The full screw kernel is an integral operator

For the causal Cauchy analyzer at fixed scale, the fully polarized RH-side
kernel is

\[
 \boxed{
 \mathbb K_a(x,y)
 =\sum_\gamma m_\gamma
  \Psi_a(\gamma-x)
  \overline{\Psi_a(\gamma-y)}.
 }
 \tag{R-91010.3}
\]

It is the kernel of an integral operator in the carrier variable.  Its
diagonal is the scalar residual:

\[
 \mathbb K_a(x,x)=a^4\mathcal R_x(a).
 \tag{R-91010.4}
\]

By contrast, `(R-91010.2)` has distribution kernel

\[
 \delta(x-y)\mathcal N_x(a).
 \tag{R-91010.5}
\]

These are different operators.

## 3. One-atom exact counterexample

Take one synthetic real zero ordinate `gamma` and suppress multiplicity.  The
wavelet Gram is the rank-one kernel

\[
 \boxed{
 K_\gamma(x,y)
 =\Psi_a(\gamma-x)
  \overline{\Psi_a(\gamma-y)}.
 }
 \tag{R-91010.6}
\]

For generic distinct `x,y`, this is nonzero.  The multiplication operator with
the same diagonal has off-diagonal kernel zero:

\[
 \delta(x-y)|\Psi_a(\gamma-x)|^2.
 \tag{R-91010.7}
\]

Therefore no identity between the two polarized operators can hold, even in a
one-atom RH-side model.

Equivalently, for coefficients `c_1,c_2`, the true quadratic form is

\[
 \left|
  c_1\Psi_a(\gamma-x_1)
  +c_2\Psi_a(\gamma-x_2)
 \right|^2,
 \tag{R-91010.8}
\]

whereas the diagonal multiplication surrogate is

\[
 |c_1|^2|\Psi_a(\gamma-x_1)|^2
 +|c_2|^2|\Psi_a(\gamma-x_2)|^2.
 \tag{R-91010.9}
\]

The missing interference term is load bearing.

## 4. Delay and orientation make the distinction stronger

The corrected form core of `L-91034` is indexed by

\[
 (\epsilon,x,\tau)
 \in\{+,-\}\times\mathbb R\times[0,\infty).
\]

Its full kernel contains:

```text
cross-carrier interference;
cross-delay phases;
causal/anti-causal cross terms;
bridge cross terms.
```

None is encoded in the pointwise scalar `N_x(a)` or its multiplication
operator.  Positive scalar soft counts do not imply positivity of this matrix
kernel; `R-91007` already gives a two-by-two finite firewall.

## 5. Correct operator target

Let

\[
 \mathcal A_a^{\rm del}:
 \ell^2_{\rm fin}(\mathfrak I_a^{\rm del})
 \longrightarrow
 \mathcal H_{\rm screw}
\]

be the synthesis map sending a finite coefficient vector to the corresponding
linear combination of delayed Hardy tests.  The exact target is

\[
 \boxed{
 (\mathcal A_a^{\rm del})^*
 \mathfrak Q_\zeta
 \mathcal A_a^{\rm del}
 \succeq0.
 }
 \tag{R-91010.10}
\]

A source-ordered completion must factor this entire operator as `C^*C`.

The Wigner--Smith commutator `(R-91010.2)` is a useful scalar shadow and may
help estimate diagonal entries.  It is not an equivalent full polarization.

## 6. Consequences

- `L-91038` is corrected to retain only the scalar commutator identity.
- `T-91008` remains the normative full-kernel proposal but must not cite a
  positive multiplication commutator as an equivalent endpoint.
- Suzuki's amplitude embedding still closes the amplitude-level component.
- The full delayed first-chaos Douglas factorization remains open and
  RH-equivalent.

## 7. Exact boundary

```text
scalar Wigner--Smith commutator identity           EXACT
commutator = complete delayed screw kernel          FALSE
one-atom off-diagonal counterexample                EXACT
full synthesis/compression operator target          EXACT FORMULATION
source-ordered full Gram factorization               OPEN / RH-EQUIVALENT
Riemann Hypothesis                                   UNPROVED
```
