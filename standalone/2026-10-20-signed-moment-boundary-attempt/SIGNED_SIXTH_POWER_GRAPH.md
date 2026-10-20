# Exact sixth-power amplification with the coprimality signs retained

Research audit, 2026-10-20. This identifies the exact graph that a proposed
signed M3 recursion must estimate; it is not a no-go theorem for sixth
moments or a numerical quasi-Riemann improvement.

Source: Liu, arXiv:2610.26835v1, equations (12.2), (12.4)–(12.7),
§§12.7.1–12.7.3, PDF SHA-256
`5d0fd10274c8444c789b0b7925a1cd3419017fe760be3219b6be51d7fbed9bd5`.

## 1. The diagonal before and after positivity

In the simplest genuine first-transform sector take `C=D=r=e=1`.
The full coefficients on the two residual columns still satisfy
`(a,b)=1`. Equivalently they retain the complete signed projector

```
1_{(a,b)=1} = sum_{s|a,b} mu_F(s).
```

If a second finite correlation is evaluated before factorwise Cauchy,
its zero frequency forces `a=b` by Lemma 12.10. The projector on that
diagonal is `sum_{s|a} mu_F(s)=1_{a=1}`. Thus the long diagonal really
does cancel in this signed expression. This cancellation is exact, and
does not need an asymptotic estimate for a fixed-character mean.

After source Cauchy, each divisor label instead supplies its own positive
Gauss norm. The second origin is

```
sum_u |B_s(u)|^2 phi_F(u)/Nu,
```

times the exact Poisson prefactor. Here `B_s` is the allocated whole
convolution and still contains the full centered stencil. Its positivity
does not disappear when the sum of that stencil over a fixed character
has a main-term cancellation. The source exponent is explicitly

```
A-M-d-(K0-K)-wo-Bc+g-ell <= A-M+O(sigma).
```

For three central factors of length `M/2`, `A=3M/2`; this terminal term
therefore costs `M/2`, irrespective of the stronger exceptional-row
centering calculation. The original dual origin causes no analogous
problem: the powerful-ideal count and divisor-bounded allocations used
in §12.7.1 extend to any fixed number of factors.

## 2. The exact graph retains all Fourier aliases

Let `m=ab` with `(a,b)=1`, and choose a pool prime `p` coprime to `m`.
For fixed columns, write

```
f(h)=G(a,h) conjugate(G(b,h)).
```

The sign convention at `-h` can be retained throughout; it changes none
of the following argument because -1 is a sixth power in the source.
The function is periodic modulo `m`. Source Lemma 12.9 gives the exact
invariance `f(p^6 h)=f(h)` when `p` is coprime to the columns.

For a smooth row weight `W`, the substitution `k=p^6 h` is therefore
the exact identity

```
sum_h f(h) W(Nh/H)
 = sum_{k in p^6} f(k) W(Nk/(H (Np)^6)).                 (1)
```

The right side is supported on the sublattice `p^6`. Its periodic
coefficient has modulus `m p^6`, not merely `m`. Consistent additive
characters give the following complete finite Fourier transform:

```
sum_{k mod m p^6, p^6|k} f(k) e(-jk/(m p^6))
 = sum_{x mod m} f(p^6 x) e(-jx/m)
 = fhat_m(j).                                         (2)
```

The first equality is the residue-ring substitution `k=p^6 x`; CRT
applies since `(p,m)=1`. The second is the actual sixth-power
invariance. This identity is valid for full imprimitive Gauss sums,
not only primitive moduli or squarefree columns.

Applying lattice Poisson to (1), its row scale is `H (Np)^6` and the
periodic modulus norm is `(Nm)(Np)^6`. Their quotient is exactly
`H/Nm`. Consequently both the Poisson prefactor and the dual norm
argument equal those of the unamplified expression:

```
prefactor = H/Nm,
dual argument = H Nj/Nm.                              (3)
```

Equivalently, expanding the sublattice indicator by its `(Np)^6`
additive characters introduces all the fractional-frequency aliases.
Keeping just the trivial additive character would give a shorter dual
range, but would delete the other terms of an exact identity. Thus a
direct second Poisson on the retained graph does not itself decrease
width, even in the no-common-support sector where the Möbius diagonal
cancellation is simplest.

The exact identity also keeps the source's row-dependent admissible
pool. For nonnegative fixed pool weights `w_p`, let `a_p(h)` be its
admissibility masks and `A(h)=sum_p w_p a_p(h)>0`. On a branch where
`F(p^6 h)=F(h)` for each admissible prime, normalized averaging and the
same substitution give

```
sum_h F(h) W(Nh/H)
 = sum_p w_p sum_k 1_{p^6|k}
       a_p(k/p^6)/A(k/p^6) F(k)
       W(Nk/(H (Np)^6)).                              (4)
```

No constant pool cardinality replaces `A(h)`. For the single fixed-prime
coefficient `F(h)1_{p not dividing h}`, considered on its own without
the general pool normalizer, the transformed graph has `v_p(k)=6`.
Its periodic modulus is `m p^7`, while the original masked coefficient
has modulus `m p`; the enlarged row scale again cancels the additional
six powers. General varying pool weights must remain inside (4),
rather than being assigned an unsupported periodic modulus.

## 3. What source amplification changes

In §12.7.2, Jensen first creates a nonnegative norm on the genuine
admissible prime graph. The proof then enlarges that positive graph to
an unrestricted row ball and uses the bounded representation count for
`h p^6`. After this enlargement the sublattice indicator has been
discarded, so the second Poisson has the enlarged smooth row scale
without the compensating enlarged periodic modulus. That is the source
of the strict width decrease.

The exact coprime bilinear form is not pointwise nonnegative in `h`.
For example, on two distinct coprime moduli its column kernel has the
principal block `[[0,1],[1,0]]`, whose quadratic form takes both signs.
Thus the source graph-enlargement inequality is not available for the
signed form simply because the original pre-Poisson moment was
nonnegative. Positivity before Poisson does not make each restricted
dual sector a nonnegative quadratic form.

Averaging (1) over a pool while retaining every graph exactly remains
an average of exact identities. Formula (2) holds prime by prime; the
aliases have not disappeared. A successful new argument could prove
additional cancellation between the alias terms, or produce a signed
graph estimate that is stronger than the separate positive norms.
Neither follows from the source Jensen/representation argument or from
the zero-frequency cancellation alone.

## 4. Scope of the higher-centering algebra

With one common character, coprimality indicator and norm twist,
an equal-product triple stencil having zero one-coordinate marginals
annihilates its all-main term and every term with exactly one mean
error. Its remaining raw fixed-character bound is controlled by the
largest surviving scale. The proposed exceptional-row improvement is
therefore credible as a component, subject to exact stencil allocation
and comparison-rank closure.

It is separate from the quadratic energy of the allocated convolution
in §1. The exact signed graph formulas (1)–(3) explain why keeping its
Möbius cancellation through a second transform does not automatically
supply the width decrease needed to turn that component into a sixth
moment `U^(1+epsilon)`.
