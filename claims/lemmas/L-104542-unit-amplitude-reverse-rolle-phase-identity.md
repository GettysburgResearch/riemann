# L-104542 — Unit-amplitude reverse-Rolle phase identity

Claim ID: `L-104542`  
Status: **PROVED EXACT**  
Created: 2026-08-23  
RH status: **not assumed**

Let `f` be real `C^2` on a regular compact interval `[a,b]`. Assume:

1. `f` and `f'` have no common zero on `[a,b]`;
2. every zero of `f'` in `(a,b)` is simple;
3. `f'(a)f'(b) != 0`.

Write the critical points as

\[
a<c_1<\cdots<c_R<b.
\]

A critical point is **good** when `f(c_j)f''(c_j)<0` and **wrong** when
`f(c_j)f''(c_j)>0`. Put

\[
G=\#\{c_j:\text{good}\},\qquad
W=\#\{c_j:\text{wrong}\}.
\]

Fix an arbitrary parameter `lambda>0` and define

\[
r_\lambda(t)=\sqrt{f(t)^2+\lambda^2f'(t)^2},
\qquad
w_\lambda(t)=r_\lambda(t)^{-1}.
\tag{L-104542.1}
\]

At every critical point,

\[
-w_\lambda(c_j)f(c_j)\operatorname{sgn}f''(c_j)
=
\begin{cases}
+1,&c_j\text{ good},\\
-1,&c_j\text{ wrong}.
\end{cases}
\tag{L-104542.2}
\]

Thus this source-chosen weight removes the critical-value amplitude exactly.

## 1. Exact unit-weight integral

The weighted total-variation identity gives

\[
\begin{aligned}
2(G-W)
={}&\int_a^b w_\lambda(t)|f'(t)|\,dt\\
&+\int_a^b w_\lambda'(t)f(t)\operatorname{sgn}f'(t)\,dt\\
&+\operatorname{sgn}f'(a)\frac{f(a)}{r_\lambda(a)}
-\operatorname{sgn}f'(b)\frac{f(b)}{r_\lambda(b)}.
\end{aligned}
\tag{L-104542.3}
\]

Since

\[
w_\lambda'
=
-\frac{f'(f+\lambda^2f'')}
       {(f^2+\lambda^2f'^2)^{3/2}},
\]

the two bulk terms combine by the exact numerator identity

\[
(f^2+\lambda^2f'^2)-f(f+\lambda^2f'')
=
\lambda^2(f'^2-ff'').
\tag{L-104542.4}
\]

Therefore

\[
\boxed{
\begin{aligned}
2(G-W)
={}&
\int_a^b
\frac{
\lambda^2|f'(t)|
\bigl[f'(t)^2-f(t)f''(t)\bigr]
}{
\bigl[f(t)^2+\lambda^2f'(t)^2\bigr]^{3/2}
}\,dt\\
&+
\operatorname{sgn}f'(a)\frac{f(a)}{r_\lambda(a)}
-\operatorname{sgn}f'(b)\frac{f(b)}{r_\lambda(b)}.
\end{aligned}
}
\tag{L-104542.5}
\]

This is an exact **unweighted** reverse-Rolle identity. No amplitude-regularity
hypothesis appears.

## 2. Hermite-Biehler phase lift

Define the nonvanishing real-axis companion

\[
E_\lambda(t)=f(t)-i\lambda f'(t)
\tag{L-104542.6}
\]

and choose a continuous unwrapped phase

\[
\theta_\lambda(t)=\arg E_\lambda(t).
\]

Then

\[
\theta_\lambda'(t)
=
\lambda\frac{f'(t)^2-f(t)f''(t)}
              {f(t)^2+\lambda^2f'(t)^2},
\tag{L-104542.7}
\]

and

\[
|\sin\theta_\lambda(t)|
=
\frac{\lambda|f'(t)|}
     {\sqrt{f(t)^2+\lambda^2f'(t)^2}}.
\tag{L-104542.8}
\]

Hence the integrand in (L-104542.5) is

\[
|\sin\theta_\lambda|\,\theta_\lambda'.
\tag{L-104542.9}
\]

Let `H` be the unwrapped primitive

\[
H'(\theta)=|\sin\theta|,
\qquad
H(0)=0.
\]

If `theta=k pi+r` with `k in Z` and `0<=r<pi`, then

\[
H(\theta)=2k+1-\cos r.
\tag{L-104542.10}
\]

Thus

\[
\boxed{
2(G-W)
=
H(\theta_\lambda(b))-H(\theta_\lambda(a))
+\mathfrak b_\lambda(a,b),
}
\tag{L-104542.11}
\]

where the explicit endpoint term is the last line of (L-104542.5).

Since

\[
H(\theta)=\frac{2}{\pi}\theta+P(\theta),
\]

with `P` bounded and `pi`-periodic, one obtains the uniform phase law

\[
\boxed{
\left|
G-W
-\frac{\theta_\lambda(b)-\theta_\lambda(a)}{\pi}
\right|
\le 2.
}
\tag{L-104542.12}
\]

The constant is independent of `lambda`, `f`, and the number of critical
points.

## 3. Meaning

Equation (L-104542.12) is the sharp analytic form of Levinson's reverse-Rolle
intuition:

```text
good critical points minus wrong critical points
  = Hermite-Biehler phase drift / pi + bounded endpoints.
```

The parameter `lambda` is free. It may be chosen at the natural microscopic
scale `lambda=a/log T` required by a mollifier without changing the asymptotic
count.

The theorem does not prove that the phase drift is positive. It removes the
critical-value amplitudes completely and turns the fixed-order descent into one
ordinary adjacent-derivative argument problem.
