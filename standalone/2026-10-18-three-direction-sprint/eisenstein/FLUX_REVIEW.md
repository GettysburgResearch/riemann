# Independent reconstruction of the BV flux compression

Reviewer: Eisenstein-probes sprint track, independent of the rational
track's construction. This is a component review, not repository acceptance.

Read the complete current `../rational/FLUX_COMPRESSION.md` and its
`DIAGONAL_COMPRESSION.md` source/geometry/projection details. Hashes measured
after this read:

* FLUX_COMPRESSION.md:
  `66cc82b317f6666f5c63c6f47d5c4c273a545be5c63cbb5824bacd33eae141e1`;
* DIAGONAL_COMPRESSION.md:
  `04dccc9b6ffe20b205ccf72ce502ffa2c2295d1f86ffb68ee78feae472ba0a5f`.

**Finding:** no blocking error found in the compression theorem or its
stated limitation. The exact remaining balanced-source contraction is open.

The Mellin identity was independently reconstructed, including its sign:
for `R(x)=H_floor(x)-log x-gamma`, the transform on 0<Re s<1 is
`-zeta(1-s)/s`. The compact signed transport measure has total mass zero,
and integration by parts supplies `-s integral F(u)u^(s-1)du` with no
endpoint term. These two factors cancel. On Re s=1/2, the remaining
transform is exactly zeta(1/2-it) times the Fourier transform of
`f(v)=exp(v/2)F(exp v)`. Hence the full dx norm has the asserted weighted
Fourier identity; no physical horizon or harmonic jump has been omitted.

The BV resources are consistent under this change of variables:
`||f||_2^2=integral |F(u)|^2du`, `||f||_infinity<<AG/sqrt D`, and
`TV(f)<<A sqrt D`. The L1 translation inequality times twice the supremum,
together with the L2 triangle bound, gives exactly
`A^2 min(G|h|,G^2/D)`. Splitting the fractional seminorm at h=G/D yields
`A^2 D^(-1+2theta)G^(2-2theta)` for 0<theta<1/2. The upper restriction
is necessary for the literal jump functions and is retained.

The primary [Hiary--Patel--Yang v1 paper]
(https://arxiv.org/pdf/2207.02366v1), Theorem 1.1 on its second PDF page,
really gives the corrected bound `0.618 t^(1/6)log t` for every t>=3.
The paper explicitly repairs the older Kusmin--Landau constant. Absorbing
the logarithm at any fixed theta>1/6 supplies the exact growth assumption
needed here. This does not use a zero-free theorem or RH.

For a native block D=X^2 and gap X^(7/10+eta), the exponent is
`-2+4theta+(2-2theta)(7/10+eta)`. At eta=1/100,theta=9/50 it equals
`-289/2500`, as stated. Because the smallest transported X tends to
infinity at least like a constant times Y^(1/4), summing the logarithmic
number of blocks preserves a decaying global error after small divisor
losses.

The refined reference coefficient resource was also checked independently.
The maximum coefficient X^(-3/2+epsilon) times its complete absolute mass
X^epsilon gives squared mass X^(-3/2+epsilon). Cauchy over multiples of q
and the divisor bound yield `X^(1/2+epsilon)Q`. Taking the minimum with
`X^epsilon(Q+Q^2/X)` and splitting at X=Q^(2/3) gives Q^(4/3), uniformly
over the whole source support. Applying the full fixed-coefficient
Abel/Gram bound produces the two powers
`K^((4/3)rho-1)` and `K^((10/3)rho-2)`. Both decay for 1/2<rho<3/5;
rho=13/24 gives the stated exponent -7/36.

The transport geometry and every native projection remain paid as in the
preceding review. Shared square primes satisfy r<=|a-b| in the reference
strip. The complete small-core resource is therefore subpower on the
declared schedule. The low-product source has EXACTLY zero large-
denominator projection. The top corner is handled by a full R norm plus
its explicit q=1, low-denominator and small-core projections, rather
than assuming a rough projection is contractive.

Finally, the actual balanced weights cancel their apparent reference
Mobius signs: their coefficients are local signed averages of z_Y(d)/d.
The proposed proof explicitly recognizes this. The transported positive
top-prime-pair source has the original large energy up to the subpower
error, so geometry alone cannot give the missing contraction. Neither
an arbitrary-coefficient bilinear theorem nor fictitious fresh Mobius
randomness has been used to claim the remaining bound.
