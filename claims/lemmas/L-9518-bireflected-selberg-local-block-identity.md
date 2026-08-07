# L-9518 — Two-frequency reflected Selberg identity for a localized normal block

Claim ID: `L-9518`  
Title: Independent conjugate twists give an exact reflected Selberg representation of the physical unit-block normal Gram  
Status: **PROPOSED EXACT REPAIR LEMMA PENDING INDEPENDENT REVIEW**  
Authoring/review agent: `gpt56-pro`  
Created: 2026-08-07  
Dependencies: the generalized coefficient identity in `L-9516`; Fourier inversion for a compact safe window  
Scope: exact algebraic/localization adapter only; no Type-II or terminal estimate

## 1. Why a second frequency is necessary

Let `H` be real and compactly supported, and define

\[
Q_H(x)
=
\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}H(x-\log n).
\tag{L-9518.1}
\]

For `alpha>1/2`, put

\[
L_\alpha(t)
=
-\frac{\zeta'}{\zeta}
\left(\frac12+\alpha+it\right)
\tag{L-9518.2}
\]

and

\[
F_\alpha(t)
=
\widehat H(\alpha+it)L_\alpha(t).
\tag{L-9518.3}
\]

Then `F_alpha` is the Fourier transform of

\[
x\longmapsto e^{-\alpha x}Q_H(x).
\]

The diagonal integral

\[
\int|F_\alpha(t)|^2dt
\]

is the all-line exponentially weighted energy. A physical block

\[
\int_J^{J+1}|Q_H(x)|^2dx
\]

requires two independent Fourier variables.

## 2. General two-frequency reflected coefficient identity

For independent real `t,s`, define the twisted Dirichlet series

\[
A_t(w)=\zeta(w+it),
\qquad
A_{-s}(w)=\zeta(w-is).
\]

Their coefficient, inverse, and logarithmic-derivative sequences are

\[
a_t(n)=n^{-it},
\qquad
b_t(n)=\mu(n)n^{-it},
\qquad
\Lambda_t(n)=\Lambda(n)n^{-it},
\]

and

\[
a_{-s}(n)=n^{is},
\qquad
b_{-s}(n)=\mu(n)n^{is},
\qquad
\Lambda_{-s}(n)=\Lambda(n)n^{is}.
\]

For any invertible Dirichlet series `A`,

\[
b*(a\log^2)
=
\Lambda_A\log+\Lambda_A*\Lambda_A,
\qquad
\Lambda_A=b*(a\log).
\tag{L-9518.4}
\]

Apply (L-9518.4) to

\[
A_t,\qquad A_{-s},\qquad A_tA_{-s}.
\]

Let

\[
\mathcal C_t=b_t*(a_t\log^2),
\qquad
\mathcal C_{-s}=b_{-s}*(a_{-s}\log^2),
\]

and

\[
\mathcal C_{t,-s}
=
(b_t*b_{-s})*
((a_t*a_{-s})\log^2).
\]

The logarithmic-derivative sequence of the product is

\[
\Lambda_t+\Lambda_{-s}.
\]

The linear terms cancel on subtraction, and the quadratic terms give

\[
\boxed{
\mathcal C_{t,-s}
-\mathcal C_t
-\mathcal C_{-s}
=
2\Lambda_t*\Lambda_{-s}.
}
\tag{L-9518.5}
\]

This is an exact coefficient identity for independent frequencies.

The diagonal specialization `s=t` is `L-9516.2`.

## 3. Analytic identity on a real line

For real `sigma>1`, taking Dirichlet series in (L-9518.5) gives

\[
\boxed{
\begin{aligned}
&
\mathcal C_{t,-s}(\sigma)
-\mathcal C_t(\sigma)
-\mathcal C_{-s}(\sigma)
\\
&\qquad=
2
\left[-\frac{\zeta'}{\zeta}(\sigma+it)\right]
\left[-\frac{\zeta'}{\zeta}(\sigma-is)\right].
\end{aligned}
}
\tag{L-9518.6}
\]

When `s=t`, the right side is the Hermitian square.

For independent `t,s`, it is precisely the mixed product needed by a localized
normal Gram.

## 4. Exact physical-block formula

Fourier inversion gives

\[
e^{-\alpha x}Q_H(x)
=
\frac1{2\pi}
\int_{\mathbb R}F_\alpha(t)e^{itx}\,dt.
\tag{L-9518.7}
\]

Let

\[
I_J=[J,J+1]
\]

and define

\[
\Phi_{J,\alpha}(\omega)
=
\int_J^{J+1}e^{2\alpha x}e^{i\omega x}\,dx.
\tag{L-9518.8}
\]

Then

\[
\boxed{
\begin{aligned}
\mathcal B_J(H)
:={}&
\int_J^{J+1}|Q_H(x)|^2dx
\\
={}&
\frac1{(2\pi)^2}
\iint_{\mathbb R^2}
F_\alpha(t)\overline{F_\alpha(s)}
\Phi_{J,\alpha}(t-s)
\,dt\,ds.
\end{aligned}
}
\tag{L-9518.9}
\]

Since `H` is real,

\[
\overline{\widehat H(\alpha+is)}
=
\widehat H(\alpha-is),
\]

and

\[
\overline{L_\alpha(s)}
=
-\frac{\zeta'}{\zeta}
\left(\frac12+\alpha-is\right).
\]

Put

\[
\sigma=\frac12+\alpha.
\]

Substituting (L-9518.6) into (L-9518.9) yields

\[
\boxed{
\begin{aligned}
2\mathcal B_J(H)
=
\frac1{(2\pi)^2}
\iint_{\mathbb R^2}
&
\widehat H(\alpha+it)
\widehat H(\alpha-is)
\Phi_{J,\alpha}(t-s)
\\
&\times
[
\mathcal C_{t,-s}
-\mathcal C_t
-\mathcal C_{-s}
](\sigma)
\,dt\,ds.
\end{aligned}
}
\tag{L-9518.10}
\]

This is the exact reflected Selberg representation of the unit-block normal
energy.

## 5. Recovery of the finite arithmetic Gram

For `alpha>1/2`, all initial series and integrals are absolutely convergent.
Expanding the right side of (L-9518.9) and applying Fourier inversion gives

\[
\boxed{
\mathcal B_J(H)
=
\sum_{m,n\ge2}
\frac{\Lambda(m)\Lambda(n)}{\sqrt{mn}}
K_J^H(\log m,\log n),
}
\tag{L-9518.11}
\]

where

\[
K_J^H(u,v)
=
\int_J^{J+1}H(x-u)H(x-v)\,dx.
\tag{L-9518.12}
\]

Because `H` is compactly supported, only finitely many `m,n` occur for one
fixed `J`.

Equation (L-9518.11) is exactly the localized normal orientation

\[
\mathcal P_\Lambda^*\chi_J\mathcal P_\Lambda
\]

of `L-15154`. It is not the same-orientation product operator
`\mathcal P_\Lambda^2`.

The parameter `alpha` disappears from the final finite arithmetic identity.

## 6. What this repairs

The diagonal identity of `L-9516` remains useful for the global weighted Hardy
norm. Equation (L-9518.10) is the correct replacement when the consumer needs a
unit logarithmic block and a finite arithmetic endpoint.

It repairs the statement

```text
single t integral
= one physical block
```

to the correct statement

```text
double (t,s) integral with the block kernel Phi_J(t-s)
= one physical block.
```

It also provides the exact aggregate packet source map in the required normal
orientation.

## 7. What it does not repair

The identity is still an equality for the complete aggregate source. It does
not imply:

- an upper bound for the block;
- a balanced Type-II recurrence;
- control of packet self-energies after a signed packet decomposition;
- a strict Selberg coercivity coefficient;
- an endpoint-face bound;
- RH.

If the complete source is decomposed into packet fields, every cross term must
remain in a coupled matrix Gram or be controlled by an independently proved
frame inequality.

## 8. Exact regression

`X-9515` represents `t` and `s` by two independent Laurent-variable blocks and
verifies (L-9518.5) coefficientwise through `n=24`.

The retained digest is

```text
c194c7cdcc5a13cf69baaed6cdf798666656b925ddfd07f614106c7a1a591165
```

The same regression rejects the incorrect sign

```text
Lambda_A=-b*(a log).
```

## 9. Proof boundary

Closed exactly:

- independent two-frequency reflected coefficient algebra;
- the mixed analytic product on a real line;
- the double-Fourier unit-block formula;
- recovery of the finite factor-ratio normal Gram.

Open:

- every source-specific packet inequality;
- balanced Type-II contraction;
- terminal arithmetic boundary estimates beyond complete-lattice Euler rows;
- RH.
