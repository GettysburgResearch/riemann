# L-100602 — The large-owner wavelet sector has no unsquared cofactor prime

Claim ID: `L-100602`
Status: **PROVED EXACT GEOMETRIC REDUCTION**
Depends on: `L-100601`; fixed ratio-eight support of PR #674
RH status: **not assumed**

In the rough largest-prime representation, a contributing integer has

\[
n=pm,\qquad X/8\le pm\le X,
\]
with `p=P^+(n)`.

Use the cofactor cutoff `Z_X=sqrt(X)`. Suppose the outer owner satisfies

\[
p>\sqrt X.
\]

If the cofactor contained an unsquared prime `q>sqrt(X)`, then `q<p` by largest-prime ownership, but

\[
pq>X.
\]
Since the remaining squared core is at least one, this would force

\[
pm\ge pq>X,
\]
contradicting the upper support condition `pm<=X`.

Therefore:

\[
\boxed{
p>\sqrt X\quad\Longrightarrow\quad P^+(m)\le\sqrt X.
}
\]

After finite cofactor squaring through `sqrt(X)`, the entire cofactor in the large-owner sector consists only of squared labels. There is no residual ordinary `q^-1/2` cofactor label.

Hence the rough wavelet splits exactly into:

1. `p>sqrt(X)`: unique terminal owner `p` times a fully squared, strictly subcritical cofactor core;
2. `Y_X<p<=sqrt(X)`: at most one unsquared cofactor prime `q>sqrt(X)` is impossible, so all cofactor primes still lie below `sqrt(X)` as well; more generally, using an owner-relative cutoff below `p` is only needed if one chooses a smaller squaring threshold.

For the literal square-root cutoff, every cofactor prime satisfies `q<p<=sqrt(X)` in sector 2 and is therefore also squared.

Thus **with cutoff `Z_X=sqrt(X)`, every cofactor prime in the entire largest-prime wavelet decomposition is squared**. The only unsquared prime is the unique terminal owner `p` itself.

This collapses `HCFB100600` from a trilinear problem to a bilinear one:

\[
\text{unique unsquared owner }p
\times
\text{fully squared positive/subcritical cofactor core}.

The remaining difficulty is source-faithful comparison back to the original unsquared cofactor wavelet without applying the forbidden scalar inverse after collapse.