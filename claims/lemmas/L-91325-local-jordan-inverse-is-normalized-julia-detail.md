# L-91325 — The signed global Jordan inverse is locally the normalized detail channel of a Julia node

Claim ID: `L-91325`  
Status: **EXACT LOCAL INVERSE/DETAIL IDENTIFICATION**  
Created: 2026-08-12  
Depends on: `L-91323`; `L-91311`  
RH status: **unproved**

## 1. Local Dirichlet inverse

For \(p\) prime and \(\omega>0\), the local factor of the Dirichlet inverse of

\[
\frac{\zeta(s-\omega)}{\zeta(s+\omega)}
\]

is

\[
\boxed{
D_{p,\omega}(s)
=
\frac{1-p^{-(s-\omega)}}
     {1-p^{-(s+\omega)}}.
}
\tag{L-91325.1}
\]

Its Dirichlet coefficients are

\[
D_{p,\omega}(s)
=
1-\left(p^{2\omega}-1\right)
\sum_{k\ge1}p^{-k\omega}p^{-ks},
\tag{L-91325.2}
\]

which is the local formula

\[
d_\omega(p^k)
=
-\left(p^{2\omega}-1\right)p^{-k\omega}.
\]

## 2. Exact Julia-detail coordinate

Put

\[
\beta_p=p^{-2\omega},
\qquad
\alpha_p=\beta_p^2=p^{-4\omega},
\qquad
z_p(s)=p^{-(s-\omega)}.
\tag{L-91325.3}
\]

Then

\[
p^{-(s+\omega)}=\beta_p z_p(s),
\]

and therefore

\[
\boxed{
D_{p,\omega}(s)
=
\frac{1-z_p(s)}
     {1-\beta_p z_p(s)}.
}
\tag{L-91325.4}
\]

The Julia detail of `L-91323` with parameters
\((\alpha_p,\beta_p)\) is

\[
d_{p,\omega}^{\rm J}(z)
=
\delta_{p,\omega}
\frac{1-z}{1-\beta_pz},
\tag{L-91325.5}
\]

where

\[
\boxed{
\delta_{p,\omega}^2
=
\frac{\beta_p(1+\beta_p+\beta_p^2)}
     {(1+\beta_p)^2}.
}
\tag{L-91325.6}
\]

Hence

\[
\boxed{
D_{p,\omega}(s)
=
\delta_{p,\omega}^{-1}
d_{p,\omega}^{\rm J}(z_p(s)).
}
\tag{L-91325.7}
\]

The signed inverse is not an unrelated Möbius correction. It is exactly the
normalized detail output of a lossless local Euler node.

## 3. Companion scalar channel

The companion scalar output is

\[
\boxed{
m_{p,\omega}^{\rm J}(z)
=
\frac1{1+\beta_p}
\frac{1-\beta_p^2z}
     {1-\beta_pz}.
}
\tag{L-91325.8}
\]

On \(|z|=1\),

\[
\boxed{
|m_{p,\omega}^{\rm J}(z)|^2
+
\delta_{p,\omega}^2|D_{p,\omega}(s)|^2
=1.
}
\tag{L-91325.9}
\]

Thus local inversion is active only after the canonical detail normalization
is removed.

## 4. Interpretation

The positive forward Jordan channel and the signed Dirichlet inverse are two
ports of the same local lossless geometry:

```text
scalar port: normalized finer shifted Jordan section;
detail port: signed inverse high-pass.
```

This is the exact transfer-level bridge between the safe Fock route and
Suzuki's all-prime deconvolution.
