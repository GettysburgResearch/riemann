# T-21904 — Mellin-zero route to RH

Claim ID: `T-21904`  
Title: Real-zero geometry of the canonical Riemann-kernel Mellin interpolant alone implies the Riemann Hypothesis  
Status: **PROPOSED EXACT CONDITIONAL THEOREM PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-02-p`  
Created: 2026-08-07  
Dependencies: `L-21910`; Konstantopoulos–Patie–Sarkar Theorem 16 and Theorem 3  
Scope: a weaker final condition than `T-21903`; no Bernstein or one-separation hypothesis

## 1. The positive density on the half-line

Let `Phi` be the positive even Riemann kernel and define, for `y>=0`,

\[
 f_\Xi(y)=\Phi(\sqrt y).
 \tag{T-21904.1}
\]

After division by its positive integral this is the density of a positive random
variable. The normalization has no effect on its Mellin zeros.

The function `f_Xi` has the hypotheses required in Theorem 16 of
Konstantopoulos–Patie–Sarkar:

1. it is analytic in a neighborhood of zero because `Phi` is even analytic;
2. it is positive on the positive half-line;
3. its decay is stronger than
   \[
    B\exp[-y^{1/2+\beta}]
   \]
   for some `B,beta>0`, by the classical theta-series expression for `Phi`.

## 2. Exact Mellin relation

The Mellin transform is

\[
\begin{aligned}
 M_{f_\Xi}(s)
 &=\int_0^\infty y^{s-1}\Phi(\sqrt y)\,dy\\
 &=2\int_0^\infty x^{2s-1}\Phi(x)\,dx.
\end{aligned}
 \tag{T-21904.2}
\]

Using the fractional moment transform of `L-21910`,

\[
 \mathcal M_\Xi(z)
 =\frac{2}{\xi(1/2)}
  \int_0^\infty x^{2z}\Phi(x)\,dx,
\]

one obtains

\[
 \boxed{
 M_{f_\Xi}(s)
 =\xi(1/2)\,\mathcal M_\Xi(s-1/2).}
 \tag{T-21904.3}
\]

Substitution in the definition of `C_Xi` gives

\[
 \boxed{
 M_{f_\Xi}(s)
 =\frac{\xi(1/2)}{\sqrt\pi}
   4^{s-1/2}\Gamma(s)
   C_\Xi(s-1/2).}
 \tag{T-21904.4}
\]

The gamma and exponential factors have no zeros. Their poles are exactly the
Mellin poles caused by the Taylor expansion of `f_Xi` at zero and are canceled
in `C_Xi` as proved in `L-21910`.

Thus every genuine zero of `M_(f_Xi)` is a zero of `C_Xi` shifted right by
`1/2`, and conversely every zero of `C_Xi` away from a removable Mellin point
gives a Mellin zero.

## 3. Weak final hypothesis

Assume

\[
 \boxed{
 C_\Xi\text{ has only real zeros}.}
 \tag{T-21904.5}
\]

Since `C_Xi(x)>0` for every real `x>-1/2`, all of its real zeros lie strictly to
the left of `-1/2`. Equation (T-21904.4) therefore shows that every zero of
`M_(f_Xi)` is real and negative.

No zero spacing, simplicity, Pick property, or Bernstein interpolation is
assumed.

## 4. Theorem 16 gives the Riemann function in the Lukacs class

Theorem 16 of Konstantopoulos–Patie–Sarkar states that if a positive analytic
half-line density has the declared tail and its Mellin transform has only
negative zeros, then, for every positive integer `n`, the normalized Fourier
transform of

\[
 x\longmapsto f(x^{2n})
\]

belongs to the Lukacs class `D_L`.

Take `n=1` and `f=f_Xi`. Then

\[
 f_\Xi(x^2)=\Phi(|x|)=\Phi(x),
 \tag{T-21904.6}
\]

because `Phi` is even. Its normalized Fourier transform is exactly

\[
 \frac{\xi(1/2+it)}{\xi(1/2)}=\Xi(t).
 \tag{T-21904.7}
\]

Consequently

\[
 \boxed{
 C_\Xi\text{ real-rooted}
 \Longrightarrow
 \Xi\in\mathds D_L.}
 \tag{T-21904.8}
\]

Theorem 3 of the same paper identifies

\[
 \Xi\in\mathds D_L
 \quad\Longleftrightarrow\quad
 \mathrm{RH}.
 \tag{T-21904.9}
\]

Therefore

\[
 \boxed{
 C_\Xi\text{ has only real zeros}
 \Longrightarrow
 \mathrm{RH}.}
 \tag{T-21904.10}
\]

## 5. Comparison with the Pick route

The earlier theorem `T-21903` assumes that

\[
 \phi_\Xi(z)=C_\Xi(z-1)/C_\Xi(z)
\]

is a nonnegative Pick function with the induced one-separation geometry. That
hypothesis implies real negative zeros of `C_Xi`, but is strictly stronger than
(T-21904.5).

The preferred review target is now simply

\[
 \boxed{C_\Xi\text{ is real-rooted}.}
 \tag{T-21904.11}
\]

The Pick route remains a structured sufficient mechanism for proving this
weaker statement.

## 6. Exact finite shadows

The following established or empirical facts are consistent with
(T-21904.11):

1. `L-21911` proves strict log-concavity of the positive integer values
   `C_Xi(n)`;
2. the first two located zeros in `O-21904` are real, negative, and simple to
   ordinary high precision;
3. the canonical quotient has positive imaginary part at the retained sample
   points.

None of these finite shadows proves real-rootedness.

## 7. Status boundary

Closed:

- exact Mellin relation (T-21904.4);
- verification of the hypotheses of the published Mellin theorem;
- the deduction from real zeros of `C_Xi` to `Xi in D_L` and RH;
- removal of the unnecessary one-separation hypothesis from the final target.

Open:

- real-rootedness of `C_Xi`;
- RH.

This is a complete conditional theorem, not a proof that the condition holds.