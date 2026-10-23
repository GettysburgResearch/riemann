# Review of the quantitative global and finite heat consequences

23 October 2026. Reviewer: root, independently of the author. Exact objects:

* `QUANTITATIVE_QUADRATIC_NONNORMALITY.md`, SHA256
  `6c8b831d994496fe4313627d9f31d1b105c663aab23c2564316b6267652c6c1b`.
* `FINITE_ORDER_HEAT_TRACE_POSITIVITY.md`, SHA256
  `d94cc407dd9831a2794b878f3e94906ae0938ab2fe77e0b7b695de941a55d596`.

The quantitative non-normality proof is correct under its stated common
zero-free premise. Agreement of coefficients through y gives the tail bound
`2 y^(-v)/v`. At `v=3 log log y/log y` this is small compared with v, so the
two positive real values have ratio tending to 2. The disk centered at
`1+2delta` with radius `R-2delta` is inside the larger disk; applying Harnack
at distance delta gives exactly `(R-delta)/(R-3delta)`. Rearranging yields
the displayed lower bound on log M without a sign reversal. Its limiting
constant is `R log(3/2)/6`. Conductor-dependent growth is permitted, so this
does not contradict the initial zero-free premise or imply a better one.

For the heat proposition, symmetry pairs the nonreal lambda values; the
individual real contributions may be bounded with their multiplicities.
For `gamma>T`, the initial phase `-n theta` lies strictly between `-pi/2`
and zero. A negative real part can occur only after `t>pi/(2gamma)`.
The inequalities `a-q >= 3 gamma^2/4` and `3pi/8>1` then justify H7.
The decreasing function `log gamma/gamma`, together with H2, gives
`2n log gamma <= gamma/4` on the whole infinite tail. Thus the negative
part is bounded by `exp(-3gamma/4)` relative to the first retained positive
term. The zero-counting hypothesis controls the sum by H8. All orders in
the finite range and all t>0 are covered; no numerical time grid is used.

The numerical example follows from the exact integer inequality
`8^30 > 3^31 * 10^12` and `e>8/3`, whence `log(3*10^12)<30`.
The quoted height is independently confirmed by the abstract of
Platt--Trudgian, <https://arxiv.org/abs/2004.09765>, which explicitly covers
all nontrivial zeros with `0<gamma<=3*10^12`. The published zero census and
zero-counting theorem are analytic/computational imports, not rerun here.
The author's attribution to Sra is preserved; this review independently
checks the displayed proof and does not claim a full audit of Sra's PDF.

No mathematical defect was found. The heat statement is finite-order
derivative positivity, not complete monotonicity of every order, total
positivity of a density, an increased verified height, or RH. Both notes
keep these distinctions explicit.
