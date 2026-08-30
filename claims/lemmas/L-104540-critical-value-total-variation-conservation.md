# L-104540 — Critical-value total-variation conservation

Claim ID: `L-104540`  
Status: **PROVED EXACT / UNCONDITIONAL XI SPECIALIZATION**  
Created: 2026-08-23  
RH status: **not assumed**

Let `f` be real `C^2` on `[a,b]`, with nonzero endpoint derivatives and only
simple critical points

\[
a<c_1<\cdots<c_R<b.
\]

Put

\[
\epsilon_- =\operatorname{sgn}f'(a),
\qquad
\epsilon_+ =\operatorname{sgn}f'(b).
\]

At a critical point write

\[
s_j=\operatorname{sgn}f''(c_j),
\]

so `s_j=+1` at a minimum and `s_j=-1` at a maximum.

## 1. Exact finite-interval identity

The derivative has constant sign on each interval cut out by the critical
points.  Summing the exact monotone variations gives

\[
\boxed{
\int_a^b|f'(t)|dt
=2\sum_{j=1}^{R}-f(c_j)s_j
 -\epsilon_-f(a)+\epsilon_+f(b).
}
\tag{L-104540.1}

Equivalently,

\[
\boxed{
\sum_{j=1}^{R}-f(c_j)\operatorname{sgn}f''(c_j)
={1\over2}
\left[
\int_a^b|f'(t)|dt
+\epsilon_-f(a)-\epsilon_+f(b)
\right].
}
\tag{L-104540.2}

No zero count, Fourier representation or entire-function hypothesis is used.

## 2. Good-versus-wrong critical-value mass

Call a critical point **good** when

\[
f(c_j)f''(c_j)<0
\]

and **wrong** when the product is positive.  Then

\[
-f(c_j)s_j
=
\begin{cases}
 |f(c_j)|,&c_j\text{ good},\\
-|f(c_j)|,&c_j\text{ wrong}.
\end{cases}
\]

Hence (L-104540.2) is the exact amplitude-weighted reverse-Rolle law

\[
\boxed{
\sum_{c\in G}|f(c)|-
\sum_{c\in W}|f(c)|
={1\over2}
\left[
\int_a^b|f'|
+\epsilon_-f(a)-\epsilon_+f(b)
\right].
}
\tag{L-104540.3}

## 3. Xi specialization

Take

\[
f(t)=\Xi''(t).
\]

Stirling's formula gives exponential decay of `Xi''` and `Xi'''` on the real
axis, so `Xi'''` is integrable and the critical-value sums converge absolutely.
Passing through regular symmetric truncations gives

\[
\boxed{
\sum_{\Xi'''(c)=0}^{\rm good}|\Xi''(c)|
-
\sum_{\Xi'''(c)=0}^{\rm wrong}|\Xi''(c)|
={1\over2}\int_{\mathbb R}|\Xi'''(t)|dt
>0.
}
\tag{L-104540.4}

Thus the Rolle-generating critical points of `Xi''` carry strictly more than
half of the total **critical-value amplitude mass** of all real `Xi'''` zeros.
This is an unconditional weighted converse to Rolle for the actual Xi
function.

Writing

\[
A_G=\sum_G|\Xi''(c)|,
\qquad
A_W=\sum_W|\Xi''(c)|,
\]

one has

\[
\boxed{
{A_G\over A_G+A_W}
={1\over2}
+{\int_{\mathbb R}|\Xi'''(t)|dt
  \over4(A_G+A_W)}
>{1\over2}.
}
\tag{L-104540.5}

## 4. Layer-cake count consequence

For `y>0`, let `G(y)` and `W(y)` count good and wrong critical points satisfying

\[
|\Xi''(c)|>y.
\]

The layer-cake identity gives

\[
\boxed{
\int_0^\infty [G(y)-W(y)]dy
={1\over2}\int_{\mathbb R}|\Xi'''(t)|dt>0.
}
\tag{L-104540.6}

Consequently there exists at least one amplitude threshold `y>0` for which

\[
\boxed{G(y)>W(y).}
\tag{L-104540.7}
\]

So a strict majority of the sufficiently large critical values is
Rolle-generating at some source-determined amplitude level.

## 5. Scope

The weight `|Xi''(c)|` cannot be discarded without a comparison theorem for
the critical-value distribution.  Equation (L-104540.4) is therefore not yet
a positive **unweighted density** statement.  Its conclusion-facing successor
is an amplitude-uniformity or critical-value moment theorem which converts the
proved weighted majority into a counting majority on a positive-density subset
of Conrey's real `Xi'''` zeros.
