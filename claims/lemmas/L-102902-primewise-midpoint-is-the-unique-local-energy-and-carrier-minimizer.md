# L-102902 — The midpoint is the unique local energy and carrier minimizer at every prime

Claim ID: `L-102902`  
Status: **PROVED UNCONDITIONAL PRIMEWISE ENERGY THEOREM**  
Created: 2026-08-25  
Depends on: `L-102901`; `L-102899`  
RH status: **not assumed**

At one labelled prime write

\[
(1-x)(1+x)^t=\sum_{k\ge0}a_k(t)x^k.
\]

Then

\[
a_0(t)=1,
\qquad
a_1(t)=t-1.
\]

Uniformly for `t` in a fixed compact subset of the complex plane,

\[
\sum_{k\ge0}|a_k(t)|^2p^{-k}
=1+\frac{|1-t|^2}{p}+O_t(p^{-2}).
\tag{L-102902.1}
\]

For the complementary factor the corresponding first-order coefficient is
`-t`, so its local energy is

\[
1+\frac{|t|^2}{p}+O_t(p^{-2}).
\]

## 1. Pointwise minimization

The combined local exponent is

\[
\boxed{
|1-t|^2+|t|^2
=\frac12+2|t-\tfrac12|^2.
}
\tag{L-102902.2}

Therefore the unique minimizer, separately at every labelled prime, is

\[
\boxed{t_p=\frac12.}
\tag{L-102902.3}

This proves the midpoint optimality without requiring all prime temperatures
to be equal.

## 2. Exact carrier balance

The first-chaos coefficients of the complementary factors are

\[
t_p-1=-(1-t_p),
\qquad
-t_p.
\]

Their sum is fixed:

\[
\boxed{(t_p-1)-t_p=-1,}
\tag{L-102902.4}
\]

while their imbalance is

\[
\boxed{(t_p-1)-(-t_p)=2t_p-1.}
\tag{L-102902.5}

Thus `t_p=1/2` is also the unique local gauge which splits the deterministic
prime carrier equally between the two factors.

## 3. Sparse endpoint cost

Let `S` be a finite source-owned set of labels. Keep `t_p=1/2` outside `S`
and choose `t_p` in `{0,1}` on `S`. At an endpoint the combined local energy
coefficient is `1`, rather than the midpoint value `1/2`. Hence the tensor
energy changes by at most

\[
\boxed{
\exp\!\left(
O\!\left(\sum_{p\in S}\frac1p\right)
\right).
}
\tag{L-102902.6}

Even if `S` contains every active prime up to a horizon `Y`, Mertens' prime
sum gives only a power of `log Y`. Therefore sparse endpoint placement of
owners, discrepancy primes, or finite boundary labels is a subpower gauge
operation.

The second labelled copy of `67` changes the constant only.

## Meaning

The midpoint should remain the default gauge for the undistinguished core.
Endpoint temperatures may nevertheless be used on a source-owned sparse label
set to obtain exact placement, at only polylogarithmic energy cost. This
observation is used in `L-102903`.
