# Independent complete heat-derivative cone review

Status: full analytic/source/code ACCEPT; independent exact normal and
optimized replays PASS and match the owner's frozen receipt byte for byte.
Scope: all real `u>=1` and integer `0<=r<=u*5419^2/32`; the complete actual
source, including every unknown conjugate occurrence and multiplicity.
This is an infinite cone, with a restricted ratio of derivative order to
time. It does not establish complete monotonicity or a cofinal census.
Exact sources: [FINITE_CENSUS_HEAT_DERIVATIVE_CONE.md](../FINITE_CENSUS_HEAT_DERIVATIVE_CONE.md),
SHA256 `d0679c63b57ffe755ad22853bc5d2d98c007d00d4a1c4941e2383a91e184fcc7`;
[check_heat_derivative_cone.py](../check_heat_derivative_cone.py), SHA256
`784238e5caa98ec855a134fd5a077c949b8154c2844a63486c7323d23c556fd8`;
the reviewed complete heat formula `d48987c9143620d6b433163c080a89f3bc4966764d0880a83666a671fda3fb29`;
the exact old count-free census receipt
`964f49cc79a61b354cd77fe1f077637e54bb46f39a5643e1455e87f60fabc4d6`;
and old `heights/COARSE_ZERO_COUNT.md`, SHA256
`67725ad90c5caaad231c4e232b76f5c38c81a84efe5005fc8909342456afa726`.
What was actually run: both exact checker modes under `/tmp`, complete direct
source authentication, full written proof/code and inherited Z1–Z5 read.
No new native heat derivative, sign interval or zero-count evaluation.
Smallest remaining gap: every time/order pair outside the proved cone.

## Entire tail and strict head comparison

HD1 correctly uses one actual real root in `(14,15)` for a lower bound
`14^(2r)*exp(-225u)` on the whole real-head derivative. The count-free
census establishes that every head root is real; simplicity is unnecessary
for this lower bound. Every remaining occurrence has real coordinate
greater than 5419. The strip gives the exact absolute tail estimate
`exp(A^2u)*sum (gamma^2+A^2)^r exp(-gamma^2u)`.

For `gamma>=R`, the two elementary inequalities in HD2 yield
`(gamma^2+A^2)^r exp(-u gamma^2)` at most
`(R^2+A^2)^r exp(-r) exp(-(u-r/R^2)gamma^2)`.
The direction of the first ratio inequality is correct because
`gamma^2>=R^2`; the second is `log z<=z-1` at `z=gamma^2/R^2`.

Closed-head Stieltjes partial summation retains the negative endpoint
`-N(R) exp(-vR^2)`. Discarding it gives an upper bound. The complete count
bound `N(t)<=t^2` pays the whole Gaussian integral, which is exactly
`(R^2+1/v) exp(-vR^2)`. Substituting `v=u-r/R^2` cancels the exponential
`exp(-r)` and gives HD5 with the stated `exp(-u(R^2-A^2))` factor.
No finite heat list replaces this complement.

The cone `r<=uR^2/32` makes `v>=31u/32>0` and `1/v<2` for `u>=1`.
The rational comparisons against `(27/10)^12` and `(27/10)^18`, together
with the exact exponential series lower bound `65/24>27/10`, give both
logarithmic prices. Thus
`12r+18-u(R^2-1/4-225)` is bounded above by
`-u*(5R^2/8-973/4)`, using `18<=18u`. The exact positive margin is
`146825859/8`. A vanishing tail is handled without taking its logarithm.
These bounds prove strict positivity throughout the literal infinite cone.
At u=1 its integer slice is exactly `r<=917673`.

## Actual complete count source and scope

The inherited Z1–Z5 proof was independently read in full. Positive actual
theta bounds the centered maximum modulus by the positive real-axis value.
The Gamma integral gives its elementary real growth bound; the ordinary
zeta Dirichlet series is used only for real `s>=2`. Jensen counts every
upper-ordinate occurrence and multiplicity, together with its lower
conjugate, by the complete classical strip. Its exact elementary logarithmic
inequalities yield `N_+(T)<T log T` for all `T>=1024`, and hence `N(T)<=T^2`
in the present domain. Under `s=1/2+i rho`, the upper ordinate is the
positive real coordinate used by HD4, including off-real representatives.

This count bound is an analytic actual-source derivation and uses the
single primitive seed `xi(1/2)>=1/4`. It is not a historical all-height
zero-count routine. The accepted old count-free source packet supplies
the stronger critical-center seed and authenticates the real head. The
last sentence of the old coarse-count note discusses a separate imported
finite-height input for older compact Pick lemmas; that input is not used
by Z1–Z5 or by this heat cone. The two inherited premises remain distinct:
the real-head theorem locates the low source roots, and the Jensen count
bound pays all unknown high occurrences.

## Independent executed controls

Both [heat_derivative_cone_normal.json](heat_derivative_cone_normal.json)
and [heat_derivative_cone_optimized.json](heat_derivative_cone_optimized.json)
have SHA256
`1708abc0dd320a35d8f753aa20b1330d5fda60c364a6ad678acf3122226a3bcd`,
matching the owner's frozen `heat_derivative_cone.json`. The eight direct
source bindings and all inherited prior direct hashes are current.
The exact checker validates the prior census scope, the actual first-root
bracket, both logarithmic upper prices, the exponential lower price, the
strict cone margin and the u=1 integer derivative slice. Its acceptance
gates survive Python optimization. The infinite time and derivative
coverage is supplied by the complete proof, rather than numerical sampling.

Every fixed derivative order therefore has the required positive sign at
all sufficiently large times. Complete monotonicity requires every order
at each fixed positive time, so the finite ratio bound does not supply it.
The qualitative positive-Fourier countermodel is compatible with such
eventual signs while having later off-real zeros. Verdict: ACCEPT within
the stated cone and exact source/import boundaries; RH remains open.
