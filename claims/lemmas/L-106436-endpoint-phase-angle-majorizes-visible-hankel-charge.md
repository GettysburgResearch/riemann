# L-106436 — The endpoint phase-angle statistic majorizes the visible Hankel charge

Claim ID: `L-106436`  
Status: **PROVED EXACT FINITE OPERATOR INEQUALITY**  
Created: 2026-08-25  
Depends on: `L-106435`  
RH status: **not assumed**

Retain the endpoint notation

\[
N=(F-i\lambda F')(F''+i\lambda F'''),
\qquad
D=(F+i\lambda F')(F''-i\lambda F'''),
\qquad
U=N/D.
\]

Let `D=B_-O_-` be the upper-half-plane inner--outer factorization and

\[
g_-={N-D\over O_-}.
\]

## 1. Exact boundary angle

On the real line, `N=bar D`, so

\[
|g_-|={|N-D|\over|D|}=|U-1|.
\]

Since

\[
N-D=2i\lambda(FF'''-F'F''),
\]

and

\[
|D|^2
 =(F^2+\lambda^2F'^2)
  (F''^2+\lambda^2F'''^2),
\]

one has the exact identity

\[
\boxed{
|g_-(t)|^2
 =4\lambda^2
 {\bigl(F(t)F'''(t)-F'(t)F''(t)\bigr)^2
  \over
  \bigl(F(t)^2+\lambda^2F'(t)^2\bigr)
  \bigl(F''(t)^2+\lambda^2F'''(t)^2\bigr)}.
}
\tag{L-106436.1}
\]

The determinant inequality for the two vectors

\[
(F,\lambda F'),
\qquad
(F'',\lambda F''')
\]

gives

\[
0\le |g_-|^2\le4.
\]

Away from zeros of `F F''`, put

\[
a=\lambda F'/F,
\qquad
b=\lambda F'''/F''.
\]

Then

\[
\boxed{
|g_-|^2
 ={4(a-b)^2\over(1+a^2)(1+b^2)}
 =4\sin^2\bigl(\arctan a-\arctan b\bigr).
}
\tag{L-106436.2}
\]

Thus the normalized Turán determinant is exactly the squared angle between the
two endpoint companion vectors.

## 2. Arbitrary finite source projection

For any finite-rank orthogonal projection `P` in `H^2`, `L-106435` gives

\[
\|H_UP\|_{\mathcal S_2}^2
 =\|P_{K_{B_-}}T_{g_-}P\|_{\mathcal S_2}^2
 \le\|T_{g_-}P\|_{\mathcal S_2}^2.
\]

If `(s_l)_(l=1)^d` is an orthonormal basis of `ran P`, define its diagonal
source density

\[
\rho_P(t)=\sum_{l=1}^d|s_l(t)|^2.
\]

Then

\[
\boxed{
\|H_UP\|_{\mathcal S_2}^2
 \le {1\over2\pi}
 \int_{\mathbb R}|g_-(t)|^2\rho_P(t)dt.
}
\tag{L-106436.3}
\]

The Fourier normalization determines the displayed `2 pi`; the statement is
otherwise basis independent.

## 3. Hard Paley--Wiener band

For the complete one-sided band `P_[0,H]`, the reproducing-kernel diagonal is
constant, `rho_H=H`.  Whenever `U-1` is square integrable,

\[
\boxed{
V_H^-(U)
 \le {H\over2\pi}
 \int_{\mathbb R}|U(t)-1|^2dt.
}
\tag{L-106436.4}
\]

For the endpoint quotient this becomes

\[
\boxed{
V_H^-(U)
 \le {2H\lambda^2\over\pi}
 \int_{\mathbb R}
 {\bigl(FF'''-F'F''\bigr)^2
  \over
  (F^2+\lambda^2F'^2)
  (F''^2+\lambda^2F'''^2)}dt.
}
\tag{L-106436.5}
\]

Therefore the actual visible `1/600` row follows from the concrete normalized
phase-angle estimate

\[
{2H_T\lambda_T^2\over\pi N(T,2T)}
 \int
 {\bigl(\Xi\Xi'''-\Xi'\Xi''\bigr)^2
  \over
  (\Xi^2+\lambda_T^2\Xi'^2)
  (\Xi''^2+\lambda_T^2\Xi'''^2)}dt
 <{1\over600}-o(1),
\]

with the window and endpoint ledger retained.

## 4. Scope

The inequality discards the favorable model-space projection and is therefore
stronger than necessary, but it is a valid scalar sufficient condition.  The
four-channel Fourier-density ratio does not prove this physical boundary
integral.  Estimating the endpoint phase-angle statistic for Xi is the exact
remaining analytic content of this route.
