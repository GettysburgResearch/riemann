# L-97101 — Exact low-child recombination and parity-covariant current bounds

**Status:** exact algebra conditional only on `L-97100`'s bias inequalities.  
**RH:** not assumed.

For a rough prime `p>=67`, put `r=p^{-1/2}` and `y=x/p`. Rough placement exchanges parity channels. The positive nondivisible current is

\[
C_{x,p}=P_x-rSA_pP_y.
\]

Its unsigned mass and signed scalar are

\[
m(C_{x,p})=M(x)-rM(y),
\qquad
f(C_{x,p})=F(x)+rF(y).
\]

When `x,y>=67`, write

\[
a=F(x)/M(x),\quad b=F(y)/M(y),\quad q=rM(y)/M(x).
\]

Then

\[
\frac{f(C_{x,p})}{m(C_{x,p})}=\frac{a+qb}{1-q}.
\]

Using `1/40<=a,b<=1/8` and `0<=q<1/8` gives

\[
\boxed{
\frac1{40}m(C_{x,p})\le f(C_{x,p})\le\frac9{56}m(C_{x,p})<\frac16m(C_{x,p}).
}
\]

For the causal coefficients

\[
\lambda_i=r_is_{i-1},\qquad\alpha_i=r_i\lambda_i,
\]

a child with scale below `67` is never observed separately. Its current and final child recombine before signed observation:

\[
\boxed{
\lambda_i(P_x-r_iSA_{p_i}P_{x/p_i})+
\alpha_iSA_{p_i}P_{x/p_i}=\lambda_iP_x.
}
\]

Thus outer parity never requires a reversed terminal Hall realization.
