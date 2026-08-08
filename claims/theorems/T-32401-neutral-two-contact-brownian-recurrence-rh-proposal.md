# T-32401 — Neutral two-contact Brownian recurrence criterion for RH

Claim ID: `T-32401`  
Title: A coefficient-one fixed-delay recurrence for the exact Brownian tail charges of the two-contact source implies the Riemann Hypothesis  
Status: **SERIOUS GLOBAL CONDITIONAL PROPOSAL — RECURRENCE OPEN / RH UNPROVED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-08  
Base: PR #302 at `477b527fb489397eb9e58ed6631be04f5eae00d1`  
Dependencies: `L-32401`, `L-32402`, `O-32401`; PR #302 `L-28009`--`L-28015`

## 1. Canonical principal energy

Retain the exact tail charge of `L-32401`,

\[
 S_X(u)=
 \sum_{\substack{n\le X\\|n/X-1/2|>u}}
 \operatorname{sgn}(n/X-1/2)c_2(n),
 \qquad0\le u\le\frac12,
\]

with

\[
 c_2(2)=2\log2,
 \qquad
 c_2(p^a)=\log p,
 \qquad
 c_2(2p^a)=-\log p
\]

for odd primes `p`, and zero otherwise. Define

\[
 \boxed{
 \mathcal E_2(X)
 ={2\over X}
  \int_0^{1/2}|S_X(u)|^2du.
 }
\tag{T-32401.1}
\]

By `L-32401`, this is exactly the full carry-position energy

\[
 \mathcal E_2(X)
 =\int_0^1
 |\mathfrak P_{2,\theta}(\log X)|^2d\theta.
\tag{T-32401.2}
\]

There is no hidden finite-dimensional source map in the definition.

## 2. Pole criterion

PR #302 `L-28011` gives the transform of the vector-valued field. For every
fixed balanced carry-position interval, every hypothetical zero

\[
 \rho=\frac12+\delta+i\gamma,
 \qquad\delta>0,
\]

produces a nonzero vector residue and therefore an `e^(delta J)` mode in the
physical field. Consequently

\[
 \boxed{
 \mathcal E_2(e^J)=e^{o(J)}
 \quad\Longrightarrow\quad
 \mathrm{RH}.
 }
\tag{T-32401.3}
\]

The reverse implication follows from the classical square-root Chebyshev error,
so the energy is an RH-equivalent scalar. This theorem does not claim an
unconditional bound for it.

## 3. Proposed production theorem — NTBR

The **Neutral Two-contact Brownian Recurrence** (`NTBR`) is:

There are absolute constants `delta>0`, `A`, and `C` such that for every
sufficiently large logarithmic scale `J`, the complete source-bound two-contact
certificate gives

\[
 \boxed{
 \mathcal E_2(e^J)
 \le C(1+J)^A
   +\sup_{u\le J-\delta}\mathcal E_2(e^u).
 }
\tag{NTBR}
\]

The coefficient of the delayed principal energy is exactly one. This is
intentional and is the strongest recurrence compatible with the critical
neutral-mode firewall of PR #323.

A production proof of `NTBR` must emit, rather than cite abstractly:

1. the centered-interval/Brownian charge ledger of `L-32401`;
2. the complete two-contact generalized-prime source;
3. the source-bound dyadic-lift matching of `L-28010`;
4. the balanced interior Selberg reserve of `L-28009/L-28012`;
5. the endpoint-contact absorption of `L-28015`;
6. the source-convolved reflected identity of `L-28013`;
7. the bounded shifted-lattice dressing of `L-28014`;
8. every small-parent and cutoff row;
9. an explicit map sending the only unpaid principal term to scale at most
   `J-delta` with coefficient one;
10. no strict contraction asserted on the principal reciprocal-zeta mode.

## 4. NTBR implies a polynomial energy bound

Let

\[
 M(J)=\sup_{0\le v\le J}\mathcal E_2(e^v).
\]

From `NTBR`,

\[
 M(J)\le C(1+J)^A+M(J-\delta)
\]

for all large `J`, after increasing `C` to absorb the fixed initial interval.
Iterating at most `1+J/delta` times yields

\[
 \boxed{
 M(J)=O((1+J)^{A+1}).
 }
\tag{T-32401.4}
\]

Hence

\[
 \mathcal E_2(e^J)=e^{o(J)}.
\]

Equation (T-32401.3) then gives

\[
 \boxed{\mathrm{NTBR}\Longrightarrow\mathrm{RH}.}
\tag{T-32401.5}
\]

No moving packet order or vanishing contraction constant is required.

## 5. Why this proposal is narrower than the former recurrences

`NTBR` does not ask for:

- pointwise positivity of the pure central producer;
- polylogarithmic ordinary divisor-source atomic norm;
- strict contraction of the eta/reciprocal-zeta source;
- an odd-prime radix automaton;
- a generic physical-to-carry frame theorem;
- a balanced Type-II operator norm;
- suppression of critical-line oscillatory modes.

The only state allowed to return with coefficient one is the exact principal
Brownian tail energy (T-32401.1). Everything else must be paid by already
identified positive reserves or strict analytic dressing.

## 6. Automatic rejection tests

Reject an asserted `NTBR` proof if it:

1. takes absolute values before the source-convolved reflected identity;
2. uses a strict `<1` coefficient on the complete principal source without
   identifying a transverse projection;
3. omits the endpoint-neighbor null rows of `L-28009`;
4. applies `L-28015` to a cross-source matrix without first giving the required
   direct-sum/congruence ledger;
5. loses the odd-prime-power/double pairing of `L-32401.7`;
6. introduces a nonprincipal character channel via an odd prime radix;
7. promotes finite numerical energy decay to the cofinal recurrence;
8. leaves any current-scale unpaid term besides the single declared principal
   copy.

## 7. Exact status

```text
centered-interval physical normal form       PROPOSED COMPLETE EXACT
odd-prime-power/double source collapse       PROPOSED COMPLETE EXACT
Brownian/min Gram and adjacent precision     PROPOSED COMPLETE EXACT
local-Euler pole-preserving homotopy          PROPOSED COMPLETE EXACT
transverse two-contact Selberg reserves       IMPORTED PROPOSED COMPLETE
critical principal mode is neutral            IMPORTED / SCOPE FIREWALL
NTBR coefficient-one recurrence               OPEN / RH-BEARING
NTBR -> polynomial energy -> RH               COMPLETE CONDITIONAL
Riemann Hypothesis                            UNPROVED
```

This is a research proposal, not a completed proof.