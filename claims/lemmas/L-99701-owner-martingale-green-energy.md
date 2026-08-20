# L-99701 — The local-square reciprocal source has an exact owner martingale and logarithmic Green energy

Claim ID: `L-99701`  
Status: **PROVED EXACT SOURCE/ENERGY THEOREM**  
Created: 2026-08-20  
Depends on: `L-99271`  
RH status: **not assumed**

Let

\[
G(z)=\frac{\zeta(z)}{1-67^{-z}}
=\sum_{n\ge1}\frac{g(n)}{n^z},
\qquad g(n)=v_{67}(n)+1,
\]

and let `beta` be the convolution inverse of `g` from `L-99271`. Put

\[
f(n)=\frac{\beta(n)}{g(n)}\in[-1,1].
\tag{L-99701.1}
\]

For `n>1`, define

\[
\mathbb P_n(q)
=\frac{\Lambda_g(q)g(n/q)}{g(n)\log n},
\qquad q\mid n,
\tag{L-99701.2}
\]

where `q` ranges over prime powers and

\[
\Lambda_g(p^a)=\log p\quad(p\ne67),
\qquad
\Lambda_g(67^a)=2\log67.
\]

The coefficient identities for `G` and `1/G` give

\[
\sum_q\mathbb P_n(q)=1,
\qquad
\boxed{f(n)=-\sum_q\mathbb P_n(q)f(n/q).}
\tag{L-99701.3}
\]

Let `N_(t+1)=N_t/Q_(t+1)` under these probabilities and stop at `N_tau=1`. Then

\[
\boxed{M_t=(-1)^t f(N_t)}
\tag{L-99701.4}
\]

is a bounded martingale. Define its one-step conditional energy

\[
D(n)=\sum_q\mathbb P_n(q)
\bigl(f(n/q)+f(n)\bigr)^2.
\tag{L-99701.5}
\]

Doob orthogonality gives the exact finite Green identity

\[
\boxed{
1-f(n)^2
=\mathbb E_n\sum_{t<\tau}D(N_t).
}
\tag{L-99701.6}
\]

Thus the local completion diagonal `1-f^2` is not an arbitrary Schur reserve: it is exactly the quadratic variation of the source-owned alternating divisor martingale.

There is also a uniform logarithmic aggregate bound. Since `D(n)<=4` and

\[
g(n)=\sum_{a\ge0}\mathbf1_{67^a\mid n},
\]

one has, for `X>=2`,

\[
\begin{aligned}
\sum_{n\le X}\frac{g(n)\log n}{n}D(n)
&\le4\sum_{a\ge0}\frac1{67^a}
 \sum_{m\le X/67^a}\frac{\log(67^am)}m\\
&\le\boxed{\frac{134}{33}(1+\log X)^2}.
\end{aligned}
\tag{L-99701.7}
\]

No absolute Möbius mass, zero-density estimate, or RH-strength input enters (L-99701.6)--(L-99701.7).

The theorem supplies a real logarithmic-energy object. It does **not** by itself orient the squarefree parity channel; the exact obstruction is recorded separately in `R-99700`.