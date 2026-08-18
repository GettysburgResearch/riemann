# L-98062 — Moving one prime across a Stieltjes cutoff is a boundary-strip coboundary

Claim ID: `L-98062`  
Status: **PROVED EXACT SOURCE/MEASURE THEOREM**  
Created: 2026-08-18  
Depends on: `L-98040`, `L-98103`; the normalized Euler identity  
RH status: **not assumed**

Let `U` be a right-continuous bounded-variation child profile, with signed
Stieltjes measure `dU`.  Let `q` be a prime.  Write `S^+` for the reciprocal
rough-Mobius prefix of the future source after `q` has been removed from the
tail.  Before moving `q`, the tail prefix is exactly

\[
S(t)=S^+(t)-{1\over q}S^+(t/q).
\tag{L-98062.1}
\]

After moving `q` into the finite cube, the child profile is

\[
U^+(y)=U(y)-{1\over q}U(y/q).
\tag{L-98062.2}
\]

For an interval `I=(a,b]`, define

\[
\begin{aligned}
\mathcal J_I^-(X)&=\int_I S(X/y)\,dU(y),\\
\mathcal J_I^+(X)&=\int_I S^+(X/y)\,dU^+(y).
\end{aligned}
\tag{L-98062.3}
\]

Then

\[
\boxed{
\begin{aligned}
\mathcal J_I^+(X)-\mathcal J_I^-(X)
={1\over q}
\bigg[
&\int_{(b/q,b]}
 S^+\!\left({X\over qy}\right)dU(y)\\
-&\int_{(a/q,a]}
 S^+\!\left({X\over qy}\right)dU(y)
\bigg].
\end{aligned}
}
\tag{L-98062.4}
\]

Intervals in (L-98062.4) are oriented Stieltjes intervals; the identity remains
valid whether or not the two strips overlap.

Thus a prime-cutoff change does not create a bulk error.  It creates only one
upper and one lower multiplicative boundary strip.

## Proof

The measure of `U(y/q)` is the pushforward of `dU` under `y=q t`.  Therefore

\[
\begin{aligned}
\mathcal J_I^+(X)
={}&\int_I S^+(X/y)dU(y)\\
&-{1\over q}
\int_{(a/q,b/q]}
 S^+\!\left({X\over qt}\right)dU(t).
\end{aligned}
\]

On the other hand, (L-98062.1) gives

\[
\mathcal J_I^-(X)
=\int_I S^+(X/y)dU(y)
-{1\over q}\int_I S^+\!\left({X\over qy}\right)dU(y).
\]

Subtracting and using the signed indicator identity

\[
\mathbf1_{(a,b]}-\mathbf1_{(a/q,b/q]}
=\mathbf1_{(b/q,b]}-\mathbf1_{(a/q,a]}
\]

gives (L-98062.4).

## Full-cutoff invariance

On the full active half-line the two boundary strips vanish at zero and
infinity, so

\[
\boxed{
\int S(X/y)dU(y)
=
\int S^+(X/y)dU^+(y).
}
\tag{L-98062.5}
\]

This is the exact associativity of the native source: moving a prime between
the tail and the finite cube changes only the representation, never the root
scalar.

## Scalar activation and the hyperbolic switch

For the annular scalar profiles in this project,

\[
U(y)=0\qquad(0<y\le2).
\]

Hence for `I=(2,Y]` the lower strip in (L-98062.4) vanishes and

\[
\boxed{
\mathcal J_{(2,Y]}^+(X)-\mathcal J_{(2,Y]}^-(X)
={1\over q}
\int_{(Y/q,Y]}
S^+\!\left({X\over qy}\right)dU(y).
}
\tag{L-98062.6}
\]

Choose the natural switching boundary `Y=X/q`.  On
`y in (X/q^2,X/q]`,

\[
1\le {X\over qy}<q.
\]

Since the least nontrivial integer in the `S^+` tail is the next prime
`q^+>q`, the prefix is identically one on this strip.  Therefore

\[
\boxed{
\mathcal J_{(2,X/q]}^+(X)-\mathcal J_{(2,X/q]}^-(X)
={1\over q}
\left[U(X/q)-U(X/q^2)\right].
}
\tag{L-98062.7}

This exact two-scale increment is the local currency of an adaptive cutoff.
It retains every source owner and contains no unsigned reserve.

## Relation to the live frontier

Iterating (L-98062.4) explains the product-boundary localizations of PRs
#599/#605: all interior cutoff changes telescope, and only source-owned
multiplicative boundary strips remain.  The theorem does not sign those strips.
`L-98063` closes their fully activated logarithmic-prime sector.