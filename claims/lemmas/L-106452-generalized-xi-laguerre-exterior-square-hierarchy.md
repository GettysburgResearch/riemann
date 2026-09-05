# L-106452 — The even endpoint numerators are derivatives of a positive-definite Xi Laguerre hierarchy

Claim ID: `L-106452`  
Status: **PROVED UNCONDITIONALLY FROM THE POSITIVE XI FOURIER KERNEL**  
Created: 2026-08-25  
Depends on: `L-106440`; the classical positive even Fourier kernel of Xi  
RH status: **not assumed**

Let `m>=1` and define

\[
\boxed{
\begin{aligned}
\mathcal L_m[F]
={}&F F^{(2m)}
 +2\sum_{j=1}^{m-1}(-1)^j
   F^{(j)}F^{(2m-j)}\\
&+(-1)^m\bigl(F^{(m)}\bigr)^2.
\end{aligned}
}
\tag{L-106452.1
}

For `m=1,2,3` this is

\[
F F''-(F')^2,
\]

\[
F F^{(4)}-2F'F^{(3)}+(F'')^2,
\]

\[
F F^{(6)}-2F'F^{(5)}+2F''F^{(4)}-(F^{(3)})^2.
\]

## 1. Exact endpoint primitive

Termwise differentiation telescopes.  Every interior product cancels, while
the middle term has the required half coefficient.  Therefore

\[
\boxed{
{d\over dt}\mathcal L_m[F](t)
 =F(t)F^{(2m+1)}(t)
  -F'(t)F^{(2m)}(t).
}
\tag{L-106452.2
}

Thus the literal endpoint numerator of `L-106440` is one derivative, not an
unstructured Wronskian.

## 2. Positive exterior-square Fourier density for Xi

Use

\[
\Xi(t)=\int_{\mathbb R}\Phi(u)e^{itu}\,du,
\qquad \Phi(u)=\Phi(-u)\ge0.
\]

Let `v=xi-u`.  Symmetrizing the derivative products gives

\[
\boxed{
\widehat{(-1)^m\mathcal L_m[\Xi]}(\xi)
 ={1\over2}\int_{\mathbb R}
 (u-v)^2
 \left(\sum_{j=0}^{m-1}u^{2j}v^{2(m-1-j)}\right)
 \Phi(u)\Phi(v)\,du
 =\Lambda_m(\xi)\ge0.
}
\tag{L-106452.3
}

Hence

\[
\boxed{
(-1)^m\mathcal L_m[\Xi]
\text{ is a continuous positive-definite function on }\mathbb R.
}
\tag{L-106452.4
}

The endpoint numerator satisfies

\[
\boxed{
\widehat{\Xi\Xi^{(2m+1)}-\Xi'\Xi^{(2m)}}(\xi)
 =(-1)^m i\xi\Lambda_m(\xi).
}
\tag{L-106452.5
}

This recovers `L-106401` at `m=1` and the fourth-endpoint density at `m=2`.

## 3. Immediate unconditional consequences

Bochner positivity gives, for every finite real packet `(t_a)` and complex
coefficients `(c_a)`,

\[
\boxed{
\sum_{a,b}c_a\overline{c_b}
 (-1)^m\mathcal L_m[\Xi](t_a-t_b)\ge0.
}
\tag{L-106452.6
}

Moreover

\[
\left|\mathcal L_m[\Xi](t)\right|
 \le (-1)^m\mathcal L_m[\Xi](0)
\]

with the sign interpreted through (L-106452.4), and all Toeplitz matrices of
the kernel are positive semidefinite.

## 4. Boundary

Positive definiteness is a genuine actual-Xi source theorem, but it is not the
pointwise generalized Laguerre inequality required for membership in the
Laguerre--Pólya class.  More importantly, the conclusion-facing all-pass symbol
is

\[
{2i\lambda\,\mathcal L_m'[\Xi]\over D_{2m}},
\]

so the endpoint denominator resolvent and its residue weights remain.  The
hierarchy proves the numerator Gram at every even order; it does not prove
`RESGRAM106450`, `HBSIG106451`, ninety percent, density one, or RH.