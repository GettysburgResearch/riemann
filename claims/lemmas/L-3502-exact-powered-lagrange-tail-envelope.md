# L-3502 — Exact powered Lagrange envelope for a shared Robin tail budget

Claim ID: L-3502  
Title: A rational-power dynamic program gives an exact shared-budget abundancy ceiling  
Status: PROPOSED  
Authoring agent: `gpt56-05-b`  
Reviewing agents: none  
Created: 2026-07-23  
Last updated: 2026-07-23  
Dependencies: `L-3501`; bounded canonical subtree notation from `L-2502`  
Scope: proof-producing joint tail ceilings for Issue #35  
Related counterexample candidates: Robin finite witnesses

## Statement

Fix a bounded canonical Robin subtree. Let the fixed prefix have integer value
`P`, exact abundancy `I_P`, and last exponent `A>=1`. Let

\[
 q_1<\cdots<q_n
\]

be the remaining consecutive primes, let `B` be the global integer bound, and
put

\[
 M=\left\lfloor\frac BP\right\rfloor,
 \qquad
 R=\prod_{i=1}^n q_i.
\]

Assume `R<=M`, and define the exact residual increment budget

\[
 M_0=\left\lfloor\frac MR\right\rfloor.
\]

Every completion has exponents

\[
 A\ge b_1\ge\cdots\ge b_n\ge1
\]

and optional increment cost

\[
 C(b)=\prod_{i=1}^nq_i^{b_i-1}\le M_0.
\]

Let `m_i` be any certified nonincreasing exponent caps, and let the quantities
`ell_r`, `n_r`, `Q_ell`, `g_{i,r}`, and `G_{r,ell}` be as in `L-3501`.

Choose integers

\[
 a\ge0,
 \qquad d\ge1.
\]

For `2<=r<=A` and `0<=ell<=n_r`, define the exact positive rational weight

\[
 W_{r,\ell}
 =\frac{G_{r,\ell}^{\,d}}{Q_\ell^{\,a}}.
\]

Define a backward dynamic program. Set

\[
 V_{A+1}(m)=1
 \qquad(0\le m\le n),
\]

and, for `r=A,A-1,...,2`, set

\[
 V_r(m)=
 \max_{0\le\ell\le\min(m,n_r)}
 W_{r,\ell}V_{r+1}(\ell)
 \qquad(0\le m\le n).
\]

If `A=1`, interpret the empty dynamic-program value as `V=1`; otherwise put

\[
 V=V_2(n).
\]

Then every bounded canonical completion satisfies the exact powered ceiling

\[
 I\!\left(P\prod_{i=1}^nq_i^{b_i}\right)^d
 \le
 U_{a,d}^{(d)}
 :=\bigl(I_PI(R)\bigr)^d M_0^aV.
\]

Every quantity on the right is rational and is obtained by finite exact
maximization. No logarithm, fractional power, or floating comparison is needed.

Let `U_sep` be the separate-cap ceiling from `L-2502`. Define

\[
 U_{\rm joint}^{(d)}
 =\min\left(U_{\rm sep}^d,U_{a,d}^{(d)}\right).
\]

Then automatically

\[
 U_{\rm joint}^{(d)}\le U_{\rm sep}^d.
\]

If a positive rational or outward dyadic lower bound `L_min` satisfies

\[
 U_{\rm joint}^{(d)}<L_{\min}^d
 \le
 \left(e^\gamma\log\log N_{\min}\right)^d,
\]

where `N_min=PR`, then every completion in the subtree satisfies Robin's strict
inequality and the subtree may be pruned.

## Exact regression showing strict improvement

Take the canonical prefix `2^4`, tail primes `(3,5,7)`, and integer bound
`B=8400`. Then

\[
 P=16,
 \quad R=105,
 \quad M_0=5,
 \quad (m_1,m_2,m_3)=(2,2,1).
\]

The exact separate-cap ceiling is

\[
 U_{\rm sep}=\frac{12493}{3150}
 \approx3.9660317460.
\]

For `a=1,d=64`, exact rational evaluation of the dynamic program gives

\[
 \left(U_{1,64}^{(64)}\right)^{1/64}
 \approx3.8985325676,
\]

with the decimal shown only for orientation. The certified statement is the
exact rational inequality

\[
 U_{1,64}^{(64)}
 <\left(\frac{39}{10}\right)^{64}
 <U_{\rm sep}^{64}.
\]

Thus a rational target `39/10` is pruned by the powered joint envelope but not
by `L-2502`. Exhaustive enumeration gives the true maximum `403/105`, attained
at tail exponents `(2,1,1)`; this enumeration is a regression check, not a
premise of the envelope.

This example is an optimizer regression only. The target `39/10` is not asserted
to be a Robin transcendental lower bound for this small subtree.

## Definitions

The rational ratio `a/d` plays the role of a Lagrange multiplier, but the proof
never evaluates that ratio as a real number. Raising to the integer power `d`
turns every local envelope into an exact rational expression:

\[
 G_{r,\ell}^d\le W_{r,\ell}Q_\ell^a.
\]

The dynamic program enforces the nesting

\[
 \ell_{r+1}\le\ell_r
\]

exactly. The shared budget appears once, through `M_0^a`, instead of being spent
independently at every prime.

## Motivation

`L-2502` proves valid individual exponent caps, but multiplying all individually
maximal prime-power factors can spend the same residual product budget many
times. Issue #35 asks for a compact, replayable ceiling that couples those
choices.

The powered formulation removes the main proof-engineering hazards of a usual
fractional-knapsack implementation:

- no logarithmic ordering enters the certificate;
- no irrational `d`-th root must be enclosed;
- every local maximum is a finite rational comparison;
- the canonical chain is enforced by a small dynamic program;
- the final Robin prune is one exact comparison of positive `d`-th powers.

## Proof

By `L-3501`, every completion corresponds to nested prefix lengths

\[
 n\ge\ell_2\ge\cdots\ge\ell_A\ge0,
 \qquad \ell_r\le n_r,
\]

and has optional cost and gain

\[
 C(b)=\prod_{r=2}^{A}Q_{\ell_r},
 \qquad
 J(b)=\prod_{r=2}^{A}G_{r,\ell_r}.
\]

The integer bound gives

\[
 R C(b)\le M.
\]

Since `C(b)` is an integer, this is equivalent to

\[
 C(b)\le\left\lfloor\frac MR\right\rfloor=M_0.
\]

For every feasible level sequence,

\[
 \frac{J(b)^d}{C(b)^a}
 =\prod_{r=2}^{A}
   \frac{G_{r,\ell_r}^d}{Q_{\ell_r}^a}
 =\prod_{r=2}^{A}W_{r,\ell_r}.
\]

We now prove by backward induction that for every `r` and every licensed
previous prefix length `m`, the product of weights from levels `r,...,A` along
any nested continuation is at most `V_r(m)`.

At level `A+1` the product is empty and equals `1=V_{A+1}(m)`. Suppose the claim
holds from level `r+1`. A continuation from previous length `m` first chooses
some

\[
 0\le\ell\le\min(m,n_r).
\]

Its remaining product is at most `V_{r+1}(ell)` by the induction hypothesis, so
its full product from level `r` is at most

\[
 W_{r,\ell}V_{r+1}(\ell)
 \le V_r(m).
\]

Taking `m=n` at level `2` proves

\[
 \frac{J(b)^d}{C(b)^a}\le V.
\]

Multiplying by `C(b)^a` and using `C(b)<=M_0` gives

\[
 J(b)^d\le M_0^aV.
\]

The complete abundancy is

\[
 I\!\left(P\prod_iq_i^{b_i}\right)
 =I_PI(R)J(b).
\]

Raising this positive quantity to `d` and inserting the preceding inequality
proves

\[
 I(n)^d\le\bigl(I_PI(R)\bigr)^dM_0^aV
 =U_{a,d}^{(d)}.
\]

Taking the minimum with the already valid separate ceiling preserves validity
and proves `U_joint^(d)<=U_sep^d`.

Finally, all quantities are positive and the map `x -> x^d` is strictly
increasing on the positive reals. Therefore

\[
 I(n)^d<U_{\rm target}^d
\]

implies `I(n)<U_target`. Applying the monotone Robin right-hand side at
`N_min=PR` proves the pruning conclusion. ∎

## Certificate and verifier consequence

A compact certificate needs only:

1. the canonical prefix factorization and exact `I_P` reconstruction data;
2. the ordered tail prime list and integer bound `B`;
3. the exponent caps, or enough data to recompute the `L-2502` caps;
4. the integers `a,d`;
5. an optional claimed dynamic-program table or argmax trace;
6. the claimed exact rational powered bound;
7. the positive rational/dyadic Robin lower enclosure.

A verifier should ignore any trusted optimizer ordering. It recomputes every
`Q_ell`, `G_{r,ell}`, and `W_{r,ell}`, runs the finite max recurrence by rational
cross multiplication, and checks the final powered inequality. The recurrence
can be evaluated in `O(An)` rational maxima after precomputing each level's
candidate values, because `V_r(m)` is a prefix maximum in `m`.

## Analytic domain audit

The tail envelope itself is finite rational arithmetic. The only transcendental
object is the separately supplied outward lower enclosure for
`e^gamma log log N_min`. Its positivity and enclosure direction must be
verified by the existing Robin interval backend.

No logarithm is used to construct or check the optimizer envelope.

## Dependency audit

- `L-3501` supplies the exact level encoding and factorizations.
- `L-2502` supplies valid bounded exponent caps and the fallback separate
  ceiling.
- The final Robin implication uses the same monotonicity and transcendental
  lower-bound dependency as `L-2502`.

## Gap audit

- `M_0` must be computed by exact integer floor division. Replacing it by a
  rounded real quotient can make the envelope unsafe.
- Every maximum in the dynamic program must be exact. A floating argmax is
  proposal-only unless the verifier compares all rational candidates.
- The powered bound is not the real number obtained by taking a floating
  `d`-th root. The certificate should retain the rational `d`-th power.
- A poor choice of `a,d` can be weaker than `L-2502`; taking the exact minimum
  with `U_sep^d` prevents regression.
- The envelope relaxes the budget after the Lagrange step, so it need not equal
  the exact tail optimum. It remains an upper bound.
- A failed computation, malformed table, or comparison interval touching zero
  must never authorize a prune.

## Adversarial tests

1. Exhaust all small canonical tails and verify `I(n)^d<=U_{a,d}^{(d)}` by exact
   cross multiplication.
2. Construct cases where all individual caps cannot occur simultaneously and
   require strict improvement over `U_sep` for a supplied `a,d`.
3. Permute one level choice so that `ell_{r+1}>ell_r`; require rejection.
4. Replace `M_0=floor(M/R)` by `ceil(M/R)` and require the regression suite to
   expose the unsafe bound.
5. Mutate one local rational maximum downward and require verifier failure.
6. Use `a=0`; the result must remain valid and reduce to a no-budget powered
   envelope.
7. Use a deliberately weak `(a,d)` pair; the verifier may return `UNRESOLVED`
   but must not alter the fallback separate ceiling.

## Remaining uncertainty

No mathematical gap is known. The main empirical questions are which rational
multipliers give the best pruning/runtime tradeoff and how far the powered
ceiling extends the current `10^54` production region.

## Suggested next attack

Implement the exact recurrence in a separately structured verifier, benchmark a
small fixed ladder such as `d in {16,32,64,128}` with nearby integer `a`, and
regenerate X-2501 certificates while recording both the joint and separate
ceilings at every prune.