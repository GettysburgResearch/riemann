# L-99821 — Native box pair positivity and the correct half-order collar window

Claim ID: `L-99821`  
Status: **PROVED EXACT FINITE-SOURCE THEOREM**  
Created: 2026-08-20  
Depends on: `L-99820`; PR #658 `L-99703`  
RH status: **not assumed**

The normalized box potential `phi` is nonnegative and nondecreasing on
`[1,infinity)`, with zero extension below one.

For a labelled prime `p`, put

\[
\mathcal E_p=I-p^{-1}U_p.
\]

Then

\[
\boxed{
(\mathcal E_p\phi)(y)
=\phi(y)-p^{-1}\phi(y/p)\ge0.
}
\tag{L-99821.1}
\]

Indeed `phi(y)>=phi(y/p)>=0`. For two labels `p,q`,

\[
\begin{aligned}
\mathcal E_p\mathcal E_q\phi(y)
={}&\phi(y)-p^{-1}\phi(y/p)-q^{-1}\phi(y/q)
 +(pq)^{-1}\phi(y/(pq))\\
\ge{}&\left(1-p^{-1}-q^{-1}\right)\phi(y).
\end{aligned}
\]

Thus, for distinct primes—and in particular for rough primes—

\[
\boxed{\mathcal E_p\mathcal E_q\phi(y)>0\quad(y>1).}
\tag{L-99821.2}
\]

This is native pair positivity. It does not imply an all-prime composition.

## Correct collar coefficient

Let `P` be a finite multiset of labelled primes and put

\[
\mathcal E_P=\prod_{p\in P}(I-p^{-1}U_p).
\]

On a fixed activation cell write `u=log y`. A subset `A` has product `p_A` and
Euler coefficient `(-1)^{|A|}/p_A`. If

\[
0\le u-\log p_A<\log67,
\]

then its collar term is

\[
\frac{(-1)^{|A|}}{p_A}
\left[8+(-8-3(u-\log p_A))e^{-(u-\log p_A)/2}\right].
\]

The coefficient of `u e^{-u/2}` is therefore

\[
\boxed{
 c_P^{\rm nat}(u)
 =-3\sum_{A:\ e^u/67<p_A\le e^u}
   \frac{(-1)^{|A|}}{\sqrt{p_A}}.
}
\tag{L-99821.3}
\]

For the complete canonical label set—one copy of every prime and a second copy
of `67`—equal products combine to `beta(n)`. Hence

\[
\boxed{
 c^{\rm nat}(u)
 =-3\sum_{e^u/67<n\le e^u}\frac{\beta(n)}{\sqrt n}.
}
\tag{L-99821.4}
\]

Put

\[
B_{1/2}(x)=\sum_{n\le x}\frac{\mu(n)}{\sqrt n}.
\]

Since

\[
\sum_{n\le x}\frac{\beta(n)}{\sqrt n}
 =B_{1/2}(x)-67^{-1/2}B_{1/2}(x/67),
\]

the window in (L-99821.4) is

\[
\boxed{
D_{67}^{\beta}(x)
=B_{1/2}(x)-(1+67^{-1/2})B_{1/2}(x/67)
 +67^{-1/2}B_{1/2}(x/67^2).
}
\tag{L-99821.5}
\]

The plain unweighted Mertens window in PR #664 is therefore not the native
collar slope of the normalized box scalar.
