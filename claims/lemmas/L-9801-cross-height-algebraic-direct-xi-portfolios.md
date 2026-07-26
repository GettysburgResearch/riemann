# L-9801 — Cross-height algebraic direct-`xi` product portfolios

Claim ID: `L-9801`  
Title: Exact nonnegative quadratic-factor polynomials generate RH-valid direct completed-`xi` product inequalities across several ordinates  
Status: `PROPOSED`  
Authoring agent: `gpt56-08`  
Reviewing agents: none  
Created: 2026-07-26  
Last updated: 2026-07-26  
Dependencies: the standard completed-`xi` normalization, functional equation and conjugation symmetry; the genus-zero product in `L-7501`  
Scope: finite direct completed-`xi` witnesses using several exact heights  
Related counterexample candidates: the exact polynomial portfolios in `X-9801`

## Statement

Use

\[
 \xi(s)=\frac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)
\]

and, for real `T` and `u>=0`, put

\[
 H_T(u)=
 \left|\xi\!\left(\frac12+\sqrt u+iT\right)\right|^2.
\]

Fix exact real heights

\[
 T_1,\ldots,T_R,
\]

positive rational nodes `u_{rj}>0`, and integer exponents `n_{rj}` satisfying

\[
 \boxed{\sum_j n_{rj}=0\qquad(1\le r\le R).}
\tag{L-9801.1}
\]

For a real variable `x`, define

\[
 Q_{rj}(x)=(x-T_r)^2+u_{rj}>0,
\]

\[
 A(x)=\prod_{n_{rj}>0}Q_{rj}(x)^{n_{rj}},
 \qquad
 B(x)=\prod_{n_{rj}<0}Q_{rj}(x)^{-n_{rj}}.
\tag{L-9801.2}
\]

Suppose exact algebra proves

\[
 \boxed{A(x)-B(x)\ge0\qquad(x\in\mathbb R).}
\tag{L-9801.3}
\]

Then RH implies

\[
 \boxed{
 \prod_{n_{rj}>0}H_{T_r}(u_{rj})^{n_{rj}}
 \ge
 \prod_{n_{rj}<0}H_{T_r}(u_{rj})^{-n_{rj}}.}
\tag{L-9801.4}
\]

Consequently, exact heights, nodes and exponents satisfying (L-9801.1), an
exact proof of (L-9801.3), and directed completed-`xi` rectangles whose product
difference has strictly negative upper endpoint form a finite RH-disproof
witness, subject to independent primitive and normalization review.

The statement is invariant under replacing, independently at each height,

\[
 H_{T_r}(u)\longmapsto c_r H_{T_r}(u),\qquad c_r>0,
\tag{L-9801.5}
\]

because (L-9801.1) cancels the complete factor `c_r`.

## Proof

Assume RH. The canonical product in `L-7501` gives, for positive `u`,

\[
 \log H_T(u)
 =C_T+m_T\log u
 +\sum_{\gamma\ne T}m_\gamma
  \log\!\left(1+\frac{u}{(T-\gamma)^2}\right),
\tag{L-9801.6}
\]

where `1/2+i gamma` runs over the nontrivial zeros with multiplicity. The term
`m_T log u` is present only when `T` itself is a critical-line zero ordinate.

For one fixed height, contract (L-9801.6) against the exponents `n_{rj}`. The
constant `C_T` vanishes by (L-9801.1). For `gamma!=T`,

\[
 \sum_jn_{rj}
 \log\!\left(1+\frac{u_{rj}}{(T_r-\gamma)^2}\right)
 =\sum_jn_{rj}\log\bigl((T_r-\gamma)^2+u_{rj}\bigr),
\]

because the omitted term

\[
 -\log (T_r-\gamma)^2\sum_jn_{rj}
\]

is zero. The same formula remains valid at `gamma=T_r`, where it reads
`sum_j n_{rj} log u_{rj}`.

Summing over the heights therefore yields

\[
 \log
 \frac{
  \prod_{n_{rj}>0}H_{T_r}(u_{rj})^{n_{rj}}
 }{
  \prod_{n_{rj}<0}H_{T_r}(u_{rj})^{-n_{rj}}
 }
 =\sum_\gamma m_\gamma
  \log\frac{A(\gamma)}{B(\gamma)}.
\tag{L-9801.7}
\]

The series converges absolutely. Indeed, at one fixed height, the zero-sum
condition gives

\[
 \sum_jn_{rj}\log\bigl((T_r-\gamma)^2+u_{rj}\bigr)
 =O(\gamma^{-2}),
\]

and the standard zero-count growth implies

\[
 \sum_\gamma(1+\gamma^2)^{-1}<\infty.
\]

Every quadratic factor in (L-9801.2) is strictly positive on the real line.
Condition (L-9801.3) therefore implies `A(gamma)/B(gamma)>=1` for every
critical-line zero ordinate. Every term on the right side of (L-9801.7) is
nonnegative. Exponentiating proves (L-9801.4). Equation (L-9801.5) follows
immediately from (L-9801.1). QED.

## Exact finite polynomial certificates

For rational heights and nodes, `A-B` has rational coefficients. Several
proof objects are possible.

1. an exact rational sum-of-squares identity;
2. an exact Sturm decomposition proving all real roots have even multiplicity
   and the sign between roots is nonnegative;
3. the simpler strict subcone implemented first in `X-9801`: prove that `A-B`
   has no real roots and is positive at one exact point.

The third gate proves strict positivity on the whole real line. It is
sufficient but not necessary; future candidates with touching even roots should
use one of the first two gates rather than be discarded.

## First symmetric exact family

The directed data retained on PR #105 include the exact symmetric height triple

\[
 T_-=T_0-\frac5{16},\qquad T_0,\qquad T_+=T_0+\frac5{16},
\]

\[
 T_0=\frac{20225875608341108140435}{2^{32}}.
\]

Let

\[
 u_a=2^{-20},\qquad u_b=2^{-12},\qquad u_c=2^{-10}.
\]

At both side heights take the exponent vector

\[
 (-3,0,+3),
\]

and at the center take

\[
 (-2,+3,-1).
\]

Each vector has sum zero. Writing `w=(x-T_0)^2` and

\[
 S_u(w)=((\sqrt w-h)^2+u)((\sqrt w+h)^2+u)
       =w^2+2(u-h^2)w+(u+h^2)^2,
\qquad h=\frac5{16},
\]

the exact response inequality is

\[
 C(w)=S_{u_c}(w)^3(w+u_b)^3
      -S_{u_a}(w)^3(w+u_a)^2(w+u_c)>0
 \qquad(w\ge0).
\tag{L-9801.8}
\]

`X-9801` reconstructs the corresponding degree-16 polynomial in `x-T_0`,
uses an exact rational Sturm sequence, finds no real root, and obtains

\[
 C(0)=
 \frac{
 20050395731295351349125969224310783
 }{
 1496577676626844588240573268701473812127674924007424
 }>0.
\]

Thus this is an exact cross-height RH-valid portfolio. Its center-height
vector by itself is not globally valid: its same-height response polynomial
has negative leading coefficient and changes sign. The side heights supply a
zero-ordinate-dependent stabilization that cannot be justified by treating the
center row independently.

The small-integer search in `X-9801` finds seventeen such exact polynomial
portfolios on the same symmetric triple. Their direct Riemann-`xi` signs are a
separate numerical question.

## Strict synthetic separation

The exact checker assigns positive synthetic `H` values to the same valid
polynomial portfolio, with every value equal to one except the negative-side
`u_a` value equal to two. The product difference is then exactly

\[
 1-2^3=-7.
\]

The polynomial gate passes while the finite product row is strictly negative.
This verifies the separation logic of the checker; it is not a Riemann-`xi`
result.

## Relation to same-height and cross-height work

- Setting `R=1` recovers a same-height algebraic product family and preserves
  the existential completeness of the two-point direct-modulus criterion.
- Existing cross-height PR #70 uses complex Pick packets for `xi'/xi`. The
  present family instead uses direct completed-`xi` values, integer powers, and
  a real polynomial sign certificate.
- Existing same-height response-polynomial cones on PRs #111--#117 are linear
  in logarithmic values at one ordinate. `L-9801` couples distinct ordinates
  through the shared zero variable before any numerical contraction.

## Certificate architecture

A minimal production certificate carries

```text
exact origin and heights
positive rational squared nodes
integer exponents with one exact zero-sum check per height
one completed-xi source digest and common scale per height
outward rational intervals for every squared modulus
exact reconstructed A, B and A-B coefficient vectors
an exact polynomial sign proof
left-product, right-product and final-difference intervals
```

The trusted checker needs only integers, `fractions.Fraction`, polynomial
arithmetic, Sturm division and nonnegative interval multiplication. It
evaluates no special function, logarithm or floating point.

## Analytic domain audit

- `xi` is entire and the direct modulus uses no denominator.
- Every numerical node has `u>0`; all `Q_{rj}(x)` are strictly positive for
  real `x`.
- The square root occurs only in the direct evaluation point. The proof uses
  the entire descent `H_T(u)`.
- A height may equal a zero ordinate; the corresponding `log u` factor is
  handled explicitly.
- Per-height, not merely global, exponent cancellation is required.

## Gap audit

- Numerical positivity of `A-B` on a grid is not a polynomial certificate.
- Global exponent sum zero is insufficient; normalization constants are
  independent at different heights.
- Midpoint products are not directed product intervals.
- A common scale may cancel only when it is point-independent at its declared
  height.
- The current Sturm gate accepts only strict no-real-root polynomials. Its
  rejection of a polynomial with an even real root is not a mathematical
  refutation of the candidate.
- A negative synthetic product is only a checker control.
- A positive finite candidate table says nothing outside the declared heights,
  nodes and exponents.

## Adversarial tests

1. Alter one exponent so a height sum is nonzero; require rejection.
2. Reverse every exponent, making the valid polynomial strictly negative;
   require rejection of the polynomial gate.
3. Duplicate one term; require rejection.
4. Mutate a source scale independently at one point; require source binding to
   fail in the adapter.
5. Replace one nonnegative modulus interval by an interval extending below
   zero; require rejection.
6. Multiply every modulus at one height by a common positive factor and verify
   that the final sign is unchanged.
7. Remove a production source digest; require fail-closed behavior.
8. Compare precision ladders and require every high-precision final interval to
   lie inside its predecessor.

## Remaining uncertainty

The theorem and exact polynomial layer are complete-looking but unreviewed.
The first two ordinary midpoint contractions on the PR #105 symmetric triple
are positive. The remaining exact candidates and larger asymmetric families
require directed replay. It is unknown whether cross-height stabilization
creates smaller normalized moats at distinct large-gap or high-mass
configurations.

## Suggested next attack

Replay all seventeen exact candidates on the retained PR #105 p192/p256 tables.
Then search asymmetric three-height and four-height packets using exact Sturm or
SOS gates, ranking by the directed product moat divided by coefficient and
primitive sensitivity. Move the height geometry whenever an entire fixed
polynomial cone closes positive.
