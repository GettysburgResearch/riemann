# L-102909 — The harmonic midpoint has a positive critical-renewal inverse

Claim ID: `L-102909`  
Status: **PROVED EXACT POSITIVE-INVERSE / RENEWAL THEOREM**  
Created: 2026-08-25  
Depends on: `L-102906--L-102908`; fixed derivative kernel `K_L`  
RH status: **not assumed**

At one labelled prime let

\[
M(x)=1-{x\over2}-{x^2\over2}=(1-x)(1+x/2).
\]

Then

\[
\boxed{
{1\over M(x)^2}
={1\over(1-x)^2(1+x/2)^2}
=\sum_{j\ge0}w_jx^j,
}
\tag{L-102909.1}
\]

where partial fractions give the exact formula

\[
\boxed{
w_j={12j+20+(3j+7)(-1/2)^j\over27}.}
\tag{L-102909.2}
\]

Hence

\[
\boxed{w_j>0\qquad(j\ge0).}
\tag{L-102909.3}
\]

## 1. Global positive inverse

Tensor the local inverses over all labelled primes, retaining the two labels at `67`, and then collapse equal physical integers. This defines a nonnegative arithmetic function `varpi` satisfying

\[
\boxed{
\varpi*\mathcal M^2=\delta_1,
}
\tag{L-102909.4}
\]

where `mathcal M^2` is the global arithmetic midpoint-square source.

Its Dirichlet series has the exact form

\[
\boxed{
V(z)=\sum_n{\varpi(n)\over n^z}
=\zeta(z)G_V(z),
}
\tag{L-102909.5}
\]

where `G_V` is analytic and nonzero for `Re(z)>1/2`. For an ordinary prime its local analytic factor is

\[
{1\over(1-x)(1+x/2)^2}=1+O(x^2),
\]

and the second labelled `67` changes only one finite factor.

In particular,

\[
\boxed{
\sum_{n\le Y}{\varpi(n)\over n}
=G_V(1)\log Y+O(1),
\qquad G_V(1)>0.
}
\tag{L-102909.6}
\]

The inverse is positive but exactly critical: its harmonic mass grows logarithmically rather than remaining bounded.

## 2. Exact positive renewal equation

Let

\[
H_{\rm harm}(X)
=
\sum_n{\mathcal M^2(n)\over\sqrt n}K_L(X/n).
\]

Finite convolution Fubini and (L-102909.4) give

\[
\boxed{
K_L(X)
=
\sum_d{\varpi(d)\over\sqrt d}
H_{\rm harm}(X/d).
}
\tag{L-102909.7}
\]

Since `K_L` is supported in `[1,8]`, for every `X>8` this becomes

\[
\boxed{
H_{\rm harm}(X)
=-
\sum_{2\le d\le X}
{\varpi(d)\over\sqrt d}
H_{\rm harm}(X/d).
}
\tag{L-102909.8}
\]

All renewal weights are nonnegative. The present value is the negative of one positive weighted average of its strict past scales.

## 3. Why this is not yet a contraction

After the exponential normalization

\[
h_\sigma(u)=e^{-\sigma u}H_{\rm harm}(e^u),
\]

the renewal mass is

\[
V(\sigma+1/2)-1.
\]

It is finite only for `sigma>1/2` and diverges as `sigma downarrow 1/2` because of the simple zeta pole in (L-102909.5). Thus the positive inverse gives an elementary contraction only far to the right of the conclusion-bearing half-plane.

The zero logarithmic moment of `K_L` centers the forcing, but a critical centered-renewal estimate is still required to reach subpower growth.

## Meaning

The unique harmonic obstruction has two equivalent exact descriptions:

```text
a positive prime-power logarithmic intensity (`L-102908`);
a positive, logarithmically critical renewal inverse (`L-102909`).
```

The remaining RH-bearing cancellation is the centered physical behavior of this critical renewal, not a missing sign in the inverse coefficients.
