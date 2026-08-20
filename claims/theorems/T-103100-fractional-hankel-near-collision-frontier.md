# T-103100 — Fractional Hankel near-collision frontier

**Status:** PROVED REDUCTION; `HCNC103100` OPEN; RH UNPROVED.

PR #696 proves

\[
|\mathcal B_U(X)|\le5\mathcal H_U(X),
\]

where `mathcal H_U` is the full logarithmic `L^2` energy of the half-completed ratio-four field and `U=floor(X^(1/3))`. Its Type-I remainder is logarithmically integrable, so subpower dyadic mass of `mathcal H_U` implies RH.

By `L-103100--L-103102`,

\[
\mathcal H_U(X)=\mathcal D_{U,N_X}+\mathcal O_{U,N_X},
\]

with

\[
\mathcal D_{U,N_X}=X^{o(1)}
\]

unconditionally and with `mathcal O` supported exactly on `1/4<m/n<4`. Therefore

\[
\boxed{\mathrm{HCNC103100}\Longleftrightarrow\mathrm{HHFE102010}.}
\tag{T-103100.1}
\]

Combined with PR #696,

\[
\boxed{\mathrm{HCNC103100}\Longrightarrow RH.}
\tag{T-103100.2}
\]

Moreover, by `L-103103`, for every subpower refinement depth `M_L` it is enough to prove the corresponding signed off-diagonal estimate on the shrinking window

\[
2^{-2/M_L}<m/n<2^{2/M_L},
\]

with the allowed factor `O(M_L^4)`. By `L-103104`, every term in that window has one unique largest prime, one cofactor Möbius sign, a sign-free gcd core, and positive half-divisor renewal weights.

Thus the former balanced trilinear has been reduced to one explicit fractional-Hankel near-collision problem. The reduction closes:

```text
the second Vaughan wing;
the positive-renewal source split;
the plus-field norm;
the full coefficient diagonal;
all far multiplicative ratios;
and arbitrary fixed-width collision geometry.
```

The remaining signed near-collision estimate is not proved here. The Riemann Hypothesis remains unproved.
