# L-100603 — Largest-prime ownership, finite cofactor squaring, and positive divisor renewal reduce the inverse interface to a signed divisor difference

Claim ID: `L-100603`
Status: **PROVED EXACT REDUCTION; TERMINAL ESTIMATE OPEN**
Depends on: `L-100600`; `L-100601`; `L-100602`; PR #671 `L-99961`
RH status: **not assumed**

The positive divisor-renewal theorem of PR #671 does not invert finite Euler squaring. Instead it gives the correct source-faithful way to compare unsquared and squared cofactor sectors.

For a squarefree cofactor divisor `d` with nonzero native coefficient, PR #671 gives

\[
B_d(z)=\beta(d)B(z)G_d(z),
\]
with all coefficients of `G_d` nonnegative and, for every fixed `sigma>1/2`,

\[
G_d(\sigma)\ll_{\sigma,\varepsilon}d^\varepsilon.
\]

Fix the largest-prime owner `p` and square cofactor primes `q<=sqrt(X)` before physical collapse as in `L-100600`. Expanding the finite completion produces a finite linear combination indexed by squarefree divisors `d` of the completed small-prime support. Each such `d` restricts the original cofactor source to `d|m`.

Apply `L-99961` **to each divisor-restricted term before summing over the owner p**. Every restricted term becomes

\[
\frac{\beta(d)}{\sqrt d}
\sum_{r\ge1}\frac{g_d(r)}{\sqrt r}
 f_{p,\psi}\!\left(\frac{X}{dr}\right),
\]
where `f_(p,psi)` is the same owner-frozen base wavelet packet and `g_d(r)>=0`.

Therefore the failure of positive desquaring is localized to the outer sign `beta(d)`: all dilation transport after the divisor restriction is positive. The exact comparison between the original and completed cofactor packets is a signed sum over divisor labels `d`, but each label carries only a **positive dilation renewal** of one common owner-frozen base packet.

## Subpower transport cost

At every fixed `sigma>1/2`, the positive renewal attached to a divisor label has total Mellin mass `d^epsilon`. Thus any estimate of the divisor-labelled signed coefficient packet that is subpower in `d` survives the renewal with only subpower loss.

## Exact remaining terminal object

The hybrid closure gate may therefore be written without an operator inverse:

`HDRB100603` — a divisor-labelled signed bilinear estimate for

\[
\sum_p p^{-1/2}
\sum_d \frac{\beta(d)}{\sqrt d}
\mathcal R_{p,d}(X),
\]

where every `R_(p,d)` is a positive dilation renewal of the same fixed ratio-eight owner packet and satisfies subpower renewal mass.

This is strictly narrower than the original rough largest-prime form:

- `p` is unique;
- the smooth sector is removed;
- cofactor primes are squared before collapse;
- all post-restriction dilation transport is positive;
- the only surviving sign is the explicit native divisor coefficient `beta(d)`.

A subpower logarithmic negative-mass bound for `HDRB100603` feeds the already-proved compact wavelet detector and yields RH. `HDRB100603` remains open.