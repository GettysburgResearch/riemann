# Astra theta-count continuation: mixed inequalities and an all-order small-time theorem

**RH remains unproved.** This add-only continuation contains proposed complete
proofs of new positivity regions and an exact growth theorem for the remaining
mixed-sign debt. Independent mathematical review and external novelty review
are pending. The finite checker is not a proof of the infinite arguments.

Target: PR #790, branch research/astra/20260905-theta-bernstein-exterior-closure.
Exact parent: bc3c35d8f434949748a2185783bf831d3afd9126.
This packet was produced as an exact-base PATCH, not remotely published in
the authoring session. The session could read GitHub but had no write action
or authenticated Git client. No remote commit is invented or implied.

## The actual advance

Let S(t)=sum_(Im rho>0) exp(-rho(1-rho)t), retaining multiplicities, and
D_m=(-1)^m S^(m). For the parent's mixed differences H_(a,b)(v), this pass
proves the following, using established inputs explicitly listed in SOURCES.md.

| Result | Quantifiers | Additional boundary |
|---|---|---|
| 27 global layers | H_(a,b)(v)>(15/16)196^b v^(a+1)/(v+226)^(a+b+1), all a>=0, v>0, 0<=b<=27 | Only V100 and the parent's low-zero certificate |
| Order-uniform small-time sign | D_m(t)>0 for EVERY m>=0 and 0<t<=10^-8 | Complete count argument; no verified zeros above 100 |
| All-order late-time sign | D_m(t)>(15/16)196^m exp(-226t) for t>=T_m(H) | T_m(H) depends on m; assumes verified prefix V_H |
| Global finite-depth consequence | H_(a,b)(v)>0, all a>=0, v>0, 0<=b<=10^15 | Imports the full published verified height H=3*10^12 |
| Exact signed-row growth | lim V_n(v)^(1/n)=sup_A (v+|A|)/|v+A| | All n, one fixed v; independent of finite zero verification |

The strongest new mechanism is the all-order small-time proof. The phase
2m atan(eta/gamma)-2t gamma eta cancels to leading order at the real Gaussian
saddle gamma=sqrt(m/t). Complete window counts and explicit Gaussian tails
make this uniform in m. It is not an extrapolation from a derivative table.

The 10^15 corollary is a parameter theorem plus a published finite zero
verification, not 10^15 computations. Its large number is NOT proximity to
an unbounded theorem. It should not be compared directly with a Toeplitz
rank or a Widder order without proving the corresponding adapter.

## The requested inequality is not completely proved

The original RH-equivalent target is H_(a,b)(v)>=0 at ONE fixed v>0 for all
a,b>=0. Arbitrarily large b remains unproved here. At the heat level, the
remaining region is an intermediate interval between 10^-8 and T_m(H),
when that interval is nonempty. No induction, analytic continuation, or
limit that fills this gap is asserted.

There is now an exact alternative target. Define

    B_(n,k)=binom(n,k)H_(k,n-k)(v),    V_n=sum_k |B_(n,k)|.

The proof establishes

    RH <=> V_n=exp(o(n))  at one fixed v>0.

The SOURCE-SIDE subexponential bound is OPEN. One hypothetical off-line
zero forces a strictly larger exponential rate, even if all other zeros
are critical. This avoids dilution of a finite exceptional set. The proof
uses a finite Vandermonde block, not a hypothesis of independent zero phases.

## Reading and replay

Read MIXED_HEAT_STRIPS.md first, then SMALL_TIME_ALL_ORDERS.md, then
BERNSTEIN_GROWTH.md. ATTEMPT_LEDGER.md records the exact attempted closure
and why the final step remains unpaid. REVIEW.md lists the load-bearing
points for an independent reviewer. The local claim band is ASTRA-TC2-01..08.

From this directory:

    python verify_pass2.py --check exact_result.json
    python -O verify_pass2.py --check exact_result.json
    sha256sum -c SHA256SUMS

The new checker performed 4,104 finite exact rational/Q(i) checks in each
interpreter mode, with identical outputs. The parent 225-check replay and
the parent's interval low-zero sign certificate were also rerun in both
modes without changing their files. See VALIDATION.md for the boundaries.

## Source preservation

Every file in this continuation is new under pass2/. The original twelve
PR790 files, original SHA256SUMS, main, canonical registries, prior research
branches and the formal spine are unchanged. SOURCE_LOCK.json records the
parent blob identities and external input scopes. An integration must obtain
a new exact-head review; this packet does not grant itself canonical status.
