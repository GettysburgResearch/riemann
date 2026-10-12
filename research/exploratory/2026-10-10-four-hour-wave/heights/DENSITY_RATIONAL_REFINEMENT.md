# Sharper reference density: global Pick order 900,000

**Status:** native compact quantitative corollary, submitted for independent
review. This preserves the independently reviewed full-source and arbitrary
node proof in [VOLTERRA_RATIONAL_REFINEMENT.md](VOLTERRA_RATIONAL_REFINEMENT.md).
The latter 888,000 packet remains frozen. RH is not proved.

**Scope and inputs:** the same classical strip, complete xi source, published
Trudgian argument bound and published critical-line census. No additional
external input is used. Normal/-O exact guards are in
`verify_density_refinement.py`; they do not rebuild the published inputs.

## D1. Uniform logarithmic and density constants

Put `H0=3000000000000`, `L0=28729/1000`. The exact elementary bounds

\[
 \log H_0>L_0,\quad \log L_0<3358/1000,\quad
 \frac{333}{106}<\pi<\frac{355}{113},\quad
 \log(2\pi)<1838/1000                                  \tag{D1}
\]

are certified by rational series, not floating approximations. For example
`log3+12log10` is bounded below by the positive atanh series with parameters
`1/2` and `9/11`; exponential Taylor lower sums bound `log L0` and
`log(2pi)` from above; alternating Machin series bound pi.

The function `logL/L` decreases for `L>e`, while `1/L` decreases. Therefore
for every `u>=H0`, the same native count identity as V1 gives

\[
 \frac{|N_+(u)-\mathcal M(u)|}{\log u}
 <\frac{112}{1000}+\frac{278}{1000}\frac{3358}{28729}
    +\frac{2510}{28729}+\frac1{84H_0}
 <\boxed{c_*=232/1000}.                               \tag{D2}
\]

The strict one-sided endpoint convention is unchanged. Also the exact main
density satisfies, at all such `u`,

\[
 \boxed{m_*\log u<2\mathcal M'(u)<U_*\log u,\quad
 m_*=\frac{113}{355}\left(1-\frac{1838}{28729}\right),
 \quad U_*=106/333.}                                  \tag{D3}
\]

The lower density improves as `u` increases, so checking it at `H0` proves
the all-height statement. The argument of the logarithm is `u/(2pi)` in
the actual Riemann–von Mangoldt main term.

## D2. Keep the complete variable-displacement proof

For every even `n>=850000`, retain exactly

`d=3191/5000`, `C1=6383/10000`, `C2=2037/5000`

and the weighted endpoint, Volterra dilation and complex derivative proofs
V2–V7. With `q=n^2/T`, the complete quadrature coefficient becomes

\[
 \ell_*=2c_*(1+2d)=165039/156250,
 \quad S_*(q)=U_*+\ell_*q.                            \tag{D4}
\]

When `q<=27/100`, the complete amplification exponent
`(d+2/n)q` is less than `173/1000`. The exponential Taylor upper bound gives

\[
 \exp(173/1000)<\boxed{\kappa_*=119/100}.              \tag{D5}
\]

Discrete Minkowski therefore applies to every independently chosen source
displacement and every Taylor depth, with the same denominator class. No
constant-shift replacement or truncated source is used.

## D3. Exact strict payment and theorem

The complete conjugate-group Taylor argument is V7 unchanged. Every
nonzero real quadratic vector of either moment block is bounded below by

\[
 \left[m_*-\ell_*q
   -\tfrac14(C_2+C_1^2)\kappa_*^2q^2(U_*+\ell_*q)\right]B.
                                                               \tag{D6}
\]

All subtracted coefficients are positive, so the endpoint `q=27/100` is
the worst case. Its exact rational gap is strictly positive, approximately
`0.0000665435`; the full fraction is bound in the normal/-O receipt.

Thus for `T>=H0`, each even `n>=850000` with

\[
 \boxed{100n^2\le27T}                                 \tag{D7}
\]

gives strict positive definiteness of the complete `K_{>T}` on every `n`
distinct positive nodes. Principal submatrices cover smaller sizes.
The maximal even order at `H0` is exactly **900,000**. Adding the published
verified critical-pair source below or at `H0` proves global Pick order
**900,000**, at that imported census scope.

The cofinal tail orders belong to changing tail kernels. This finite global
order is not all-order positivity and supplies no RH conclusion. Every
complete-summation and multiplicity condition is the one proved in V7–V8.
