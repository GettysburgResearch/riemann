# T-91007 — A coefficient-one Cauchy storage recurrence is equivalent to RH

Claim ID: `T-91007`  
Status: **PROPOSED COMPLETE RH-EQUIVALENT CRITERION — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-11  
Depends on: `T-91004`, `L-91020`, the standard zero count  
RH status: **unproved**

## 1. Normalized dyadic gate

Retain the Cauchy-square soft count

\[
 \mathcal N_x(a)
 =\frac12\left[
 a\Re\frac{\xi'}{\xi}(1/2+a+ix)
 -a^2\partial_a\Re\frac{\xi'}{\xi}(1/2+a+ix)
 \right].
\]

Define

\[
 \boxed{
 \mathcal E_x(a)
 =a^{-4}\bigl[\mathcal N_x(2a)-\mathcal N_x(a)\bigr].
 }
 \tag{T-91007.1}
\]

The theorem is

\[
 \boxed{
 \mathrm{RH}
 \Longleftrightarrow
 \mathcal E_x(a)\ge\mathcal E_x(2a)
 \quad(x\in\mathbb R,\ a>0).
 }
 \tag{T-91007.2}
\]

It is enough to use positive rational `a` and rational `x`.

## 2. Proof under RH

Under RH,

\[
 \mathcal N_x(a)
 =\sum_\gamma m_\gamma
 \frac{a^4}{[a^2+(\gamma-x)^2]^2}.
\]

Therefore

\[
 \mathcal E_x(a)-\mathcal E_x(2a)
 =a^{-4}\sum_\gamma m_\gamma
 \left[
 D_a^{(0)}(\gamma-x)
 -\frac1{16}D_{2a}^{(0)}(\gamma-x)
 \right].
\]

By `L-91020`, every summand is

\[
 a^{-4}|\Psi_a(i(\gamma-x))|^2>=0.
\]

The sum converges absolutely from the `O(|u|^-6)` decay of the stored residual and the Riemann--von Mangoldt zero count. Hence (T-91007.2) holds under RH.

## 3. Failure under false RH

Assume RH is false. Choose an ordinate `gamma` carrying a right-side zero and, among the finitely many zeros at that exact ordinate, choose one of maximal horizontal depth

\[
 y=\Re\rho-\frac12>0.
\]

At the matching centre `x=gamma`, the reflected pair contributes

\[
 2\Re\frac{a^4}{(a^2-y^2)^2}
 =\frac{2a^4}{(a^2-y^2)^2}
\]

to `N_gamma(a)`. Consequently

\[
 \mathcal N_\gamma(2a)-\mathcal N_\gamma(a)
 \longrightarrow-\infty
 \qquad(a\downarrow y,\ a>y).
\]

After the harmless factor `a^-4`, `E_gamma(a)` also tends to `-infinity`.

The quantity `E_gamma(2a)` stays bounded along a sequence `a downarrow y`: a real singularity there would require a zero at the same ordinate and depth `2y`, contradicting maximality; if `2y>=1/2`, such a nontrivial depth is impossible. Zeros at other ordinates do not create a real singularity at this centre.

Therefore

\[
 \mathcal E_\gamma(a)<\mathcal E_\gamma(2a)
\]

for all sufficiently close admissible `a>y`. The failure is strict and survives a rational perturbation of `a,x`.

## 4. Why the normalization matters

Without normalization, `L-91020` gives

\[
 D_a^{(0)}-\frac1{16}D_{2a}^{(0)}=|\Psi_a|^2.
\]

Multiplication by `a^-4` turns the inherited term into exactly

\[
 (2a)^{-4}D_{2a}^{(0)}.
\]

Thus the recurrence has coefficient one:

\[
 \boxed{
 \mathcal E_x(a)
 =\mathcal E_x(2a)+\mathfrak I_x(a),
 }
 \tag{T-91007.3}
\]

where, under RH,

\[
 \mathfrak I_x(a)
 =a^{-4}\sum_\gamma m_\gamma|\Psi_a(i(\gamma-x))|^2>=0.
 \tag{T-91007.4}
\]

The same construction continues to every order `m` of `L-91020`:

\[
 a^{-2(m+2)}D_a^{(m)}
 =(2a)^{-2(m+2)}D_{2a}^{(m)}
  +a^{-2(m+2)}D_a^{(m+1)}.
 \tag{T-91007.5}
\]

Thus the finite-scale geometry has a genuine no-loss return channel at every cancellation order.

## 5. Terminal behavior

The Riemann--von Mangoldt count and the Cauchy decay imply, for fixed `x`,

\[
 \mathcal E_x(A)\longrightarrow0
 \qquad(A\to\infty).
 \tag{T-91007.6}
\]

Hence an unconditional proof of the innovation sign in (T-91007.3) would iterate directly to

\[
 \mathcal E_x(a)>=0.
\]

By `T-91004`, this is the dyadic Cauchy-square gate and proves RH.

## 6. Exact production theorem

The remaining conclusion-producing statement may be formulated as follows.

> **Cauchy--Jordan boundary intertwiner.** Construct, from the explicit divisor isometry `V_(a,a)` of `L-91021` together with the completed gamma/pole factor of `xi`, a source-ordered Gram representation whose scalar output is the causal Hardy factor `Psi_a` of `L-91020`.

The representation must retain:

1. the coefficient-one returned state at scale `2a`;
2. every logarithmic cross term from the coproduct of `L-91021`;
3. the exact completed pole and gamma channels;
4. no additional signed same-scale output.

A source-only construction is insufficient by the control models of PR #398. The completed boundary coupling is load-bearing.

## 7. Boundary

```text
sharp sixteenfold line-kernel storage              EXACT
all-order positive storage hierarchy               EXACT
coefficient-one normalization                       EXACT
RH -> coefficient-one recurrence                   PROPOSED COMPLETE
false RH -> strict recurrence failure               PROPOSED COMPLETE
terminal normalized energy -> zero                  PROPOSED COMPLETE
completed Cauchy--Jordan boundary intertwiner        OPEN / RH-EQUIVALENT
Riemann Hypothesis                                   UNPROVED
```
