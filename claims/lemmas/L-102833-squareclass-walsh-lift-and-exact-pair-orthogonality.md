# L-102833 — Semiprime squareclasses have an exact quadratic Walsh lift

Claim ID: `L-102833`  
Status: **PROVED EXACT PHASE/ORTHOGONALITY THEOREM**  
Created: 2026-08-24  
Depends on: `L-102831--L-102832`  
RH status: **not assumed**

Give every labelled prime `ell` an independent sign

\[
\varepsilon_\ell\in\{-1,+1\}.
\]

For an integer product define its quadratic squareclass character

\[
\chi_\varepsilon(n)
=
\prod_\ell
\varepsilon_\ell^{v_\ell(n)\bmod2}.
\]

For a completed largest-two occurrence `n=pq a^2`,

\[
\boxed{
\chi_\varepsilon(n)=\varepsilon_p\varepsilon_q.
}
\tag{L-102833.1}
\]

The square core is invisible and the two labelled copies of `67` remain
separate coordinates.

## 1. Exact orthogonality of owner pairs

For unordered pairs `P={p,q}` and `Q={r,s}`, Haar averaging on the finite sign
cube gives

\[
\boxed{
\mathbb E_\varepsilon
[(\varepsilon_p\varepsilon_q)
 (\varepsilon_r\varepsilon_s)]
=
\mathbf1_{P=Q}.
}
\tag{L-102833.2}

Hence if

\[
\mathcal H_\varepsilon(u)
=
\sum_{p>q}
\varepsilon_p\varepsilon_q H_{p,q}(u),
\]

then

\[
\boxed{
\mathbb E_\varepsilon\|\mathcal H_\varepsilon\|_2^2
=
\sum_{p>q}\|H_{p,q}\|_2^2
\ll
\log(2Y)(\log\log(3Y))^2.
}
\tag{L-102833.3}

Thus the entire semiprime-squareclass lift is polylogarithmic in quadratic
Walsh average.

## 2. The physical restriction

The literal physical current is the single point evaluation

\[
\mathcal H_{\rm phys}=\mathcal H_{\varepsilon\equiv1}.
\]

Define

```text
L2SC102833:
  after exact carrier, region and gauge recombination, the identity-point
  evaluation of the semiprime-squareclass Walsh lift has subpower logarithmic
  negative mass at the fixed outer ray.
```

Then `L2SC102833` implies `DPWNC102749` and hence RH through the existing fixed
consumer.

Equation (L-102833.3) is an exact orthogonalization, not a bound for the
identity point. The source-blind obstruction is retained in `R-102830`.