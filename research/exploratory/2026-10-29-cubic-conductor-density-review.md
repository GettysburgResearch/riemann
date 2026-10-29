# Review of cubic conductor ordering and current index-density comparisons

**Status:** Conditional source-to-consequence audit. The cited analytic estimates have not been independently proved here. This is not an exhaustive prior-art search or a new individual zero-free region.

Let `K` be a fixed field containing the cube roots of unity, `S` the fixed set from [de Faveri, arXiv:2610.04045v1](https://arxiv.org/abs/2610.04045v1), and `chi_g` that paper's chosen cubic character for a cube-free good ideal `g`. Write `g=a b^2` with `a,b` coprime and squarefree. Section 2.5.1 states that the conductor of its primitive inducing character is `c_g ab`, with `c_g` supported on the fixed exceptional set. Consequently `N(ab) <= N(cond chi_g)`.

Set `g'=b a^2`. For every good ideal coprime to `ab`, the multiplicativity in Section 2.5.1 gives `chi_(g')=conjugate(chi_g)`; the same identity holds at the zero masks. Thus their primitive inducing characters are complex conjugates. Conjugation reflects zeros in the real axis and preserves multiplicity and the symmetric height condition `|Im rho|<=T`. Finally

```text
min(Ng,Ng') <= sqrt(Ng Ng') = (N(ab))^(3/2).
```

Fix a deterministic tie-breaker and choose the smaller of `g,g'`. Each chosen index has at most two preimages. Applying de Faveri's Corollary 1.5 to those indices, and using that deleted Euler factors do not introduce zeros in `Re s>0`, gives, for `1/2<sigma<1`, `T>1`, and `epsilon>0`,

```text
sum_(g cube-free, N cond(chi_g)<=X) N(sigma,T; primitive chi_g)
  << X^((3/2)(1-delta_3(sigma))+epsilon)
       T^(1+d(1-sigma)/(3-2sigma)+epsilon),  d=[K:Q].
```

The constant can depend on the field, fixed source data and `epsilon`. For `sigma>=5/6`, de Faveri's formula simplifies to

```text
1-delta_3(sigma) = 2(10sigma-7)(1-sigma)/(24sigma-12sigma^2-11).
```

The conductor exponent is `1` at `5/6` and strictly less than `1` on `(5/6,1)`. This is an untwisted, fixed-presentation family consequence of the cited theorem; it is not a conductor-ordered theorem for arbitrary finite-order characters of `K`. It retains an explicit, arbitrary-height `T` power. Unitary deleted Euler factors have zeros only on `Re s=0`, so passing to primitive inducing L-functions does not change the counted positive-real-part zeros.

## Stronger small-height source over the Eisenstein field

The current [rStation Paper 52, version 5, Theorem 1](https://rstation.ai/problems/riemann_hypothesis/papers/52) is a more recent claim than the index-density comparator in earlier search snippets. It concerns cube-free dyadic indices over `Q(omega)`, primitive inducing L-functions, an arbitrary **fixed** finite-order twist of trivial infinite type with conductor supported on the fixed `S`, both cubic orientations, and multiplicity-counted zeros. At each fixed `sigma>=5/6` and `epsilon>0`, it asserts a sufficiently small positive height power `h`, dependent on the fixed data and epsilon. At `sigma=5/6`, it claims index exponent `3/5+epsilon`; older version 4 quoted the weaker `8/13`.

The pairing above, now using the paper's explicitly supplied conjugate orientation and keeping the fixed twist unchanged, gives the conductor-ordered exponent `9/10+epsilon` at `sigma=5/6` for heights `T<=X^h0`, with some sufficiently small `h0>0`. Outside `S`, a fixed twist does not change the local conductor `ab`; at `S`, its conductor can differ from that of `chi_g` but remains irrelevant to this lower bound. The result sums the source's indexed family with multiplicity and includes both swapped labels if the original family includes both.

One bookkeeping point is essential: the paper's admissible height for an index dyad `P` is `P^h`, not automatically `X^h`. Choose a small fixed `eta>0` and handle selected indices with `P<X^eta` by standard zero counting, using `O(P)` indices and at most `O(T log(X(2+T)))` zeros per primitive function. Their total is `O(X^(eta+h0+epsilon))`. For all remaining dyads, choose `h0<=eta h`; then `T<=X^h0<=P^h`. Summing the dyadic bounds through `P<=X^(3/2)` yields the asserted `X^(9/10+epsilon)` after choosing the small parameters. The same argument transports each fixed-sigma exponent `E_new(sigma)` to `(3/2)E_new(sigma)`, but no uniformity as `sigma` approaches 1 is asserted.

Paper 52 states explicitly that its family is ordered by cube-free index norm, not conductor norm. Its `3/5` estimate depends on its detector, Gram, smooth Burgess, inverse identities and fourth-moment inputs. This audit verifies only the pairing and height conversion; it does not independently verify that paper's estimates. Its scope is limited to the Eisenstein field and a sufficiently small height power, unlike the broader field and explicit height range in the de Faveri deduction. Conversely, its `9/10` conductor exponent at `5/6` is strictly stronger in that common small-height setting.

Targeted searches found no directly matching conductor-ordered zero-density statement for this full indexed Eisenstein family. De Faveri's Theorem 1.2 is already conductor-ordered but concerns **central second moments**, not zero density. Corrigan's fixed-order Dirichlet conductor results concern a different rational family. These observations are not a claim of exhaustive priority.
