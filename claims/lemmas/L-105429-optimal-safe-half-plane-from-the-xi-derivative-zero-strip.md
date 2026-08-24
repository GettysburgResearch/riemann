# L-105429 — The Xi derivative zero strip gives the optimal positive safe half-plane

Claim ID: `L-105429`  
Status: **PROVED UNCONDITIONALLY**  
Created: 2026-08-24  
Depends on: the classical zero strip for `xi`; Gauss--Lucas and Hurwitz  
RH status: **not assumed**

## 1. Complete derivative zero strip

Use

\[
\Xi(z)=\xi\!\left({1\over2}+iz\right).
\]

Every zero `rho=beta+i gamma` of `xi` has `0<beta<1`. Its centered coordinate

\[
z={\rho-1/2\over i}
\]

therefore satisfies

\[
|\operatorname{Im}z|<1/2.
\]

For every fixed `r>=0`,

\[
\boxed{
Z(\Xi^{(r)})
\subset
\{z:|\operatorname{Im}z|\le1/2\}.
}
\tag{L-105429.1}

One proof starts from the symmetric canonical products of `Xi`. Their finite
partial products have all zeros in the closed convex strip. Gauss--Lucas puts
every derivative zero of every partial product in the same strip. Local
uniform convergence of each fixed derivative and Hurwitz pass this containment
to `Xi^(r)`. Multiplicities are retained.

## 2. Paired logarithmic derivative

Put

\[
F_r=\Xi^{(r)}.
\]

The function is real entire, of order one, and of definite parity. Pairing the
zeros under `tau -> -tau` gives

\[
\boxed{
F_r(z)=Cz^\varepsilon
\prod_{\tau\in\mathcal Z_r^+}
\left(1-{z^2\over\tau^2}\right),
}
\tag{L-105429.2
}

where one representative is chosen from each nonzero `+-` pair and

\[
\sum_{\tau\in\mathcal Z_r^+}|\tau|^{-2}<\infty.
\]

There is no nonconstant exponential factor: parity excludes a linear factor,
and order one excludes a quadratic factor.

Away from the zeros,

\[
\boxed{
{F_r'(z)\over F_r(z)}
={\varepsilon\over z}
+
\sum_{\tau\in\mathcal Z_r^+}
\left({1\over z-\tau}+{1\over z+\tau}\right).
}
\tag{L-105429.3}

The paired series converges locally uniformly.

## 3. Sign above the zero strip

Let

\[
z=x+iy,
\qquad y>1/2.
\]

For every zero `tau`,

\[
\operatorname{Im}{1\over z-\tau}
=-{y-\operatorname{Im}\tau\over|z-\tau|^2}<0.
\]

The same holds for `-tau`, and the origin term has negative imaginary part.
Consequently

\[
\boxed{
\operatorname{Im}{F_r'(z)\over F_r(z)}<0
\qquad(y>1/2).
}
\tag{L-105429.4}

In particular the logarithmic derivative does not vanish there. Taking its
reciprocal gives

\[
\boxed{
\operatorname{Im}{F_r(z)\over F_r'(z)}
=-{\operatorname{Im}(F_r'/F_r)
  \over|F_r'/F_r|^2}
>0
\qquad(y>1/2).
}
\tag{L-105429.5}

Thus every fixed Xi derivative ratio is Pick in the entire half-plane above
the classical zero strip.

## 4. Sharpness of the height

The line `Im z=1/2` is the natural unconditional boundary: a zeta zero with
real part arbitrarily close to zero or one maps arbitrarily close to one of
the two strip edges. No smaller universal zero-free height follows from the
classical critical strip alone.

The theorem does not assert a zero occurs on the boundary.

## 5. Relation to L-105430

`L-105430` proves a weaker existential safe height directly from Stirling and
the absolutely convergent zeta series. The present theorem strengthens that
endpoint to the exact height `1/2` and avoids all far-field asymptotics.

The Bell-polynomial theorem remains useful for quantitative coarse-scale
expansions such as `L-105436` and `L-105439`.

## 6. Scope

The theorem gives no information inside `0<Im z<=1/2`, where all RH-bearing
critical and zero defects live. It does not prove the fine-scale microscope
sign or RH.
