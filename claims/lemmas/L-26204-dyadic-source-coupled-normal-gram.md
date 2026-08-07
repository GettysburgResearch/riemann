# L-26204 — Exact coupled normal Gram of the fixed-`q_0=2` dyadic Möbius source

Claim ID: `L-26204`  
Title: The fixed-logarithm Möbius packet enters one physical block through a rank-one two-translate normal matrix with every cross term retained  
Status: **PROPOSED EXACT LEMMA — COMPLETE ALGEBRAIC SOURCE TRACE**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Dependencies: PR #241 `L-9518`; PR #158 `L-15159`; PR #236 `L-23010`; elementary translation/Fourier algebra  
Scope: exact trace into the corrected two-frequency physical block; no contraction estimate

## 1. Fixed-logarithm source

Let

\[
\alpha_\mu
=
\sum_{n\ge1}{\mu(n)\over\sqrt n}\,\delta_{\log n}.
\tag{L-26204.1}
\]

PR #158 proves that after fixing the Heath--Brown logarithmic coordinate at
`q_0=2`, the complete signed coefficient packet is a translated nonzero scalar
multiple of this source throughout every block whose compact support lies below
the finite coefficient endpoint.

The harmless scalar `log(2)/sqrt(2)` and the common translation by `log(2)` do
not affect an upper exponential block exponent. We therefore work directly
with `alpha_mu`.

Put

\[
L=\log2,
\qquad
(\tau_Lf)(x)=f(x-L).
\tag{L-26204.2}
\]

The Euler-aligned dyadic atomic source is

\[
\beta_2
=
\sum_{n\ge1}{b_2(n)\over\sqrt n}\,\delta_{\log n},
\qquad
b_2(n)=\mu(n)-\mathbf1_{2\mid n}\mu(n/2).
\tag{L-26204.3}
\]

Coefficient comparison gives the exact source identity

\[
\boxed{
\beta_2
=
D_2\alpha_\mu,
\qquad
D_2=I-2^{-1/2}\tau_L.
}
\tag{L-26204.4}
\]

## 2. Exact physical signals

Let `H` be any real compact window and define

\[
Q_\mu=H*\alpha_\mu,
\qquad
Q_2=H*\beta_2.
\tag{L-26204.5}
\]

Translations commute with convolution, so

\[
\boxed{
Q_2(x)
=
Q_\mu(x)-2^{-1/2}Q_\mu(x-L).
}
\tag{L-26204.6}
\]

For one logarithmic block, put

\[
E_{2,H}(J)
=
\int_J^{J+1}|Q_2(x)|^2dx.
\tag{L-26204.7}
\]

Then exactly

\[
\boxed{
\begin{aligned}
E_{2,H}(J)
={}&
\int_J^{J+1}|Q_\mu(x)|^2dx
+{1\over2}
\int_J^{J+1}|Q_\mu(x-L)|^2dx\\
&-\sqrt2\,
\operatorname{Re}
\int_J^{J+1}
Q_\mu(x)\overline{Q_\mu(x-L)}\,dx.
\end{aligned}}
\tag{L-26204.8}
\]

No mixed term may be omitted or estimated before the signed source is formed.

## 3. Rank-one coupled normal matrix

Define the two-component source signal

\[
\mathbf Q(x)
=
\begin{pmatrix}
Q_\mu(x)\\
Q_\mu(x-L)
\end{pmatrix}
\tag{L-26204.9}
\]

and

\[
\boxed{
M_2
=
\begin{pmatrix}
1&-2^{-1/2}\\
-2^{-1/2}&1/2
\end{pmatrix}
=
\begin{pmatrix}1\\-2^{-1/2}\end{pmatrix}
\begin{pmatrix}1&-2^{-1/2}\end{pmatrix}
\succeq0.
}
\tag{L-26204.10}
\]

Then

\[
\boxed{
E_{2,H}(J)
=
\int_J^{J+1}
\mathbf Q(x)^*M_2\mathbf Q(x)\,dx.
}
\tag{L-26204.11}
\]

This is the complete coupled packet matrix for the dyadic source. It is positive
semidefinite and rank one. Its orthogonal translate combination is a genuine
null direction; therefore the matrix itself does not supply a strict Schur
reserve relative to the two uncoupled Möbius blocks.

## 4. Direct arithmetic normal Gram

Let

\[
K_J^H(u,v)
=
\int_J^{J+1}H(x-u)H(x-v)dx.
\tag{L-26204.12}
\]

Expanding the atomic source gives

\[
\boxed{
E_{2,H}(J)
=
\sum_{m,n\ge1}
{b_2(m)b_2(n)\over\sqrt{mn}}
K_J^H(\log m,\log n).
}
\tag{L-26204.13}
\]

Equivalently, in the original Möbius coordinates the four coupled channels are

\[
\boxed{
\begin{aligned}
E_{2,H}(J)
={}&
\sum_{m,n}{\mu(m)\mu(n)\over\sqrt{mn}}
K_J^H(\log m,\log n)\\
&-{1\over\sqrt2}
\sum_{m,n}{\mu(m)\mu(n)\over\sqrt{mn}}
K_J^H(\log(2m),\log n)\\
&-{1\over\sqrt2}
\sum_{m,n}{\mu(m)\mu(n)\over\sqrt{mn}}
K_J^H(\log m,\log(2n))\\
&+{1\over2}
\sum_{m,n}{\mu(m)\mu(n)\over\sqrt{mn}}
K_J^H(\log(2m),\log(2n)).
\end{aligned}}
\tag{L-26204.14}
\]

Compact support makes every sum finite on one block. Formula (L-26204.14) is
the exact fixed-`q_0=2` coupled normal Gram requested by the corrected
reflected programme.

## 5. Two-frequency representation

Let

\[
F_{\mu,\alpha}(t)
=
\widehat H(\alpha+it)
{1\over\zeta(1/2+\alpha+it)}.
\tag{L-26204.15}
\]

The dyadic multiplier is

\[
\boxed{
D_2(\alpha+it)
=
1-2^{-1/2-\alpha-it}.
}
\tag{L-26204.16}
\]

With

\[
\Phi_{J,\alpha}(\omega)
=
\int_J^{J+1}e^{2\alpha x}e^{i\omega x}dx,
\]

PR #241's double-Fourier inversion gives

\[
\boxed{
\begin{aligned}
E_{2,H}(J)
={1\over(2\pi)^2}
\iint
&D_2(\alpha+it)F_{\mu,\alpha}(t)\\
&\times
\overline{D_2(\alpha+is)F_{\mu,\alpha}(s)}
\Phi_{J,\alpha}(t-s)\,dt\,ds.
\end{aligned}}
\tag{L-26204.17}
\]

This is the exact two-frequency realization of the same normal Gram.

## 6. Stable source equivalence

For `Re z>=0`,

\[
\left|2^{-1/2-z}\right|\le2^{-1/2}<1.
\]

Therefore

\[
\boxed{
D_2(z)^{-1}
=
\sum_{k\ge0}2^{-k/2}\,2^{-kz}
}
\tag{L-26204.18}
\]

is a causal `ell^1` translation filter. In physical coordinates,

\[
\boxed{
\alpha_\mu
=
\sum_{k\ge0}2^{-k/2}\tau_{kL}\beta_2.
}
\tag{L-26204.19}
\]

Thus the fixed-`q_0=2` Möbius block and the dyadic `b_2` block have the same
upper exponential energy status. The dyadic differencing does not delete or
attenuate an off-line zeta pole.

## 7. Structural conclusion

The corrected source trace is now exact:

```text
fixed-q0=2 signed Heath--Brown packet
-> Möbius atomic source
-> zero-safe dyadic difference
-> rank-one 2x2 coupled physical normal Gram
-> dyadic two-contact carry source.
```

The fixed translation `L=log2` is bounded and its inverse filter is stable. It
does not create a strict fractional logarithmic destination. Therefore a
lower-scale contraction cannot come from the two-by-two source matrix alone.
The arithmetic step must use the special two-contact carry or bottom-charge
structure of `L-26201`--`L-26203`.

## 8. Proof boundary

Closed exactly:

- the fixed-logarithm-to-dyadic source map;
- every coupled translate cross term;
- the rank-one positive normal matrix;
- the direct arithmetic and two-frequency forms;
- the zero-safe causal inverse.

Open:

- a source-specific lower-scale estimate for the coupled block;
- DSS/PBD;
- RH.
