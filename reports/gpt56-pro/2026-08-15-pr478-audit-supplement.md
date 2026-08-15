# PR #478 audit supplement on the live PR #481 spine

# Audit of PR #478 and corrected factor-67 native repair

## Frozen graph

```text
reviewed proposal PR:        #473
reviewed proposal head:      71d6a859ea741fe035de709e8d10ed37301b778e
reviewed proposal tree:      036365630b50cde18929715fa9d9211434821a09
review PR:                    #478
review head:                  9d19a7a6ff132fa5a39347392cbeadf09c14a261
mass successor PR:           #476 at 9f16ce483954d4233b68ee09cb6bec47400aa3cc
native-normalization PR:     #477 at 5acd9007b4f4bb1792466f5013c39bf4eac33f9e
all-column successor PR:     #479 at 518b6a5ec2b49b7decbd4c2e349d0ee5b26bfc9b
independent review PR:       #480 at d6d9c051abb20a47f3ce7adb45de33bfc2b933b9
```

## Executive verdict

PR #478 is strong and correct on the compact arithmetic it reconstructs:

```text
Hall total-row transparency                         verified;
159/500 < L(x) < 183/100                            verified;
C_67 < 19                                           verified;
K <= q <= X/4 reserve arithmetic                    verified;
581 X^(-3/2) terminal arithmetic                    verified on frozen input;
narrow aggregate Schur summation                    verified at narrow scope;
one-packet causal coefficient sum <1/8              verified.
```

Its headline conclusion remains correct:

\[
 \boxed{\text{PR #473 does not establish RH.}}
\]

Its claimed first open arrow is overstated.  The final construction in
`L-91692` does not use independently chosen fiberwise coefficient lists.  It
applies `L-91650` once to the aggregate labelled packet.  Together with
`L-91674` and the target nonexpansivity of `L-91375.9`, that aggregate list
already implies the mass-weighted contraction needed by `T-91312`.  What is
missing is an explicit definition and display, not a new arithmetic theorem.

The review is also incomplete.  It does not identify:

1. the uncovered physical columns `2<=q<K`;
2. the impossible normalization `4sqrt(X)-H(d_X)=O(1)`;
3. the activation-knot relative-refinement issue later isolated in PR #480;
4. the distinction between PR #479's valid continuum `<4290` shortfall and the
   complete native root cost.

This packet compiles the child-mass proof, proves a uniform bound for the
actual retained target mass, and supplies conservative repairs for the other
interfaces.  It remains a conditional proof proposal; RH remains
unproved.

# Part I — Audit of the review's claimed mass gap

## 1. What the reviewer models

PR #478 studies fibers

\[
 P_s=P_s^{\rm cur}+
 \sum_i a_i(s)U_{s,i}Q_{s,i}
\]

with varying active lists and coefficients.  For that model, the correct child
quantity is indeed

\[
 M_{\rm ch}
 =\int\sum_i a_i(s)m(U_{s,i}Q_{s,i})d\lambda(s),
\]

and actual-mass normalization is a valid scalar wrapper.

The review's two-fiber example with coefficients `1/9` and `1/100` is
mathematically correct.  It shows that one may not simply choose either
fiberwise coefficient after grouping.

## 2. Why that example does not refute `L-91692`

The controlling final passage of PR #473 says to apply `L-91650` to the
**aggregate packet**.  Let `p_1<...<p_k` be the union of all active rough primes.
For a fiber on which `p_i` is inactive, use zero child.  Then one global list

\[
 r_i=p_i^{-1/2},
 \quad
 \lambda_i=r_i\prod_{h<i}(1-r_h),
 \quad
 \alpha_i=r_i\lambda_i
\]

acts on the aggregate packet.

Positive integration defines aggregate child operators `B_i`, and the exact
identity is

\[
 P=s_kP+
 \sum_i\lambda_i(P-r_iB_iP)+
 \sum_i\alpha_iB_iP.
\]

For inactive fiber/prime pairs, the current term is simply the positive parent
fiber.  This can only stop more source in the current generation and reduce
recursive mass.

`L-91375.9` gives

\[
 m(B_iP)\le m(P).
\]

Therefore

\[
 \sum_i\alpha_i m(B_iP)
 \le m(P)\sum_i\alpha_i
 <\frac18m(P).
\]

That is exactly the target-mass statement used by `T-91312`.  No unit-mass
renormalization is required.

The review is therefore wrong to classify the mass issue as an independent
load-bearing arithmetic gap.  It is right that the frozen proposal should have
defined the aggregate operators and written the target-mass inequality.
`L-91732` supplies the missing compilation.

## 3. Variable lists still have a clean theorem

PR #476's `L-91694` gives a useful general Tonelli theorem, but review PR #480
correctly observes that it assumes the pointwise weighted mass inequality
instead of deriving it.

For the factor-67 fibers, the derivation is immediate:

\[
 \sum_i a_i(s)m(U_{s,i}Q_{s,i})
 \le m(P_s)\sum_i a_i(s)
 <\frac18m(P_s),
\]

using `L-91650` and `L-91375.9`.  Tonelli gives the integrated inequality.
Grouping by a countable placement/provenance class and normalizing by actual
child masses then gives

\[
 P=P^{\rm cur}+\sum_b\beta_bU_b\widetilde P_b,
 \qquad
 m(\widetilde P_b)=m(P),
 \qquad
 \sum_b\beta_b<\frac18.
\]

This is included as the second half of `L-91732`.

## 3A. The actual retained target mass is uniformly bounded

The consumer `T-91305` also requires a uniform bound on the physical target
mass of the distinguished positive packet.  The historical number `54` is a
certificate-count bound, not that target mass.

On the frozen endpoint-measure interpretation,

\[
 d\nu(x)=\frac{2L(x)}x dx,
 \qquad 0<L(x)<\frac{183}{100}.
\]

Thus `nu([1,67))<183/10`.  One Hall fiber has target mass below the full
positive target supply, hence below

\[
 4\sqrt{67}H_{66}<165.
\]

Positive integration gives

\[
 \boxed{m(P_X)<3020.}
\]

This is `L-91737`.  It makes the actual child-envelope contribution uniformly
bounded and avoids substituting the count `54` for exact target mass.

# Part II — Gaps missed by PR #478

## 4. Physical columns below `K`

PR #473 proves its relative error estimate only when `q>=K`.  Support at seed
indices `n>=K` does not make a smaller physical response vanish, because the
ordinary carry samples `n=jq`.

The correct object is the retained-cell cumulative seed

\[
 E_X^I(n)=
 \sum_{\substack{m\in I_X\\m\ge n}}
 \varepsilon_X(m),
\]

where `I_X` is the actual set of cells sent through the continuum producer.
Then

\[
 E_X^I(n)-E_X^I(n+1)
 =1_{I_X}(n)\varepsilon_X(n)
\]

and

\[
 v_q(E_X^I)=
 \sum_{jq\in I_X}\varepsilon_X(jq)
\]

for every `q>=2`.  No cutoff delta is introduced.

The exact all-column bounds are

```text
ordinary mismatch                 <57/(2q sqrt(K));
detail mismatch                   <171/(4q sqrt(K));
collar plus mismatch              <971/(4q sqrt(K));
relative error                    <129/sqrt(K).
```

The one-use thinning

\[
 \tau_K=\frac{\sqrt K}{\sqrt K+130}
\]

leaves strict reserve

\[
 \frac{\Omega_X(q)}{\sqrt K+130}
\]

in every nonterminal physical column.  This is `L-91733`.

## 5. Native versus continuum normalization

The exact endpoint deficit is

\[
 \Delta_X=J_\Lambda(X)-\mathcal H(d_X)
 =\langle Y_4,s_X\rangle.
\]

The line

\[
 4\sqrt X-\mathcal H(d_X)=O(1)
\]

in `T-91660` cannot hold for the same native-feasible row if the claimed RH
conclusion is true, because under RH

\[
 J_\Lambda(X)=4\sqrt X-\kappa_0\log X+O(1),
 \qquad
 \kappa_0>0.
\]

PR #477 is correct to reject this line.  The controlling scalar must be native
slack.

## 6. The seed firewall is not editorial

`T-91660` prints

\[
 b_X^\star=\bar b_X^\star
\]

and immediately says this equality is never asserted.  The controlling formula
is

\[
 b_X^\star=\bar b_X^\star+E_X.
\]

The later compact arithmetic correctly retains `E_X`; nevertheless the
contradictory display occurs in the conclusion-producing theorem and must be
superseded, not merely described as editorial.

# Part III — Audit of the live descendants

## 7. PR #479's all-column constants

The all-column constants in PR #479 are correct.  Its phrase assigning
`jq<K` to an “exact inner recursive owner” is too terse for a physical
correction packet.  `L-91733` replaces it with the explicit retained-cell seed,
which realizes exactly the same all-column response and introduces no boundary
atom.

## 8. PR #479's `<4290` statement

Let `H_0(X)>=4sqrt(X)` be the unthinned positive Hall score.  Then

\[
 4\sqrt X-\tau_KH_0(X)
 \le4\sqrt X(1-\tau_K)<4290.
\]

Thus the constant is valid as a continuum-equality-shortfall bound.  It is not
the whole native deficit.  The frozen native benchmark bridge gives

\[
 J_\Lambda(X)-4\sqrt X<4\log X,
\]

and hence

\[
 J_\Lambda(X)-\tau_KH_0(X)
 <4\log X+4290.
\]

The complete native root cost is therefore logarithmic.  An elementary
fallback bounds the incremental safety slack by `4290 log(X)` without using the
sharper bridge.  `L-91735` records both statements and preserves the correct
scope of PR #479's constant.

## 9. Activation knots

PR #480 is correct that raw Lipschitz interpolation does not imply uniform
relative convergence near a vanishing capacity.  PR #479 removes finite knot
collars and interpolates only on compact retained cells.

The remaining pointwise score majorant in PR #479 is unnecessary.  The endpoint
measure is finite and atomless, and literal score is an integrable positive
coordinate.  Dominated convergence makes the removed collar score tend to
zero.  Same-cell uniform convergence makes the integrated interpolation score
tend to zero.  This is `L-91734`.

## 10. Narrow port scope

The review is right to accept only the matrix inequality

\[
 M_b\succeq\frac19\mathcal V_bI,
 \qquad
 \tau_{p_b}\mathcal V_b<\frac19\mathcal V_b
\]

and its positive aggregate summation.  The old colored affine lift and open
colored-to-physical projection are not imported into this route.  The packet
locks only the narrow uncolored displays and the statement that recursive
physical causal children have zero root-global port coordinate.

# Part IV — Corrected native composition

## 11. One-use root identity

After current construction, full-child reservation and finite correction, the
root must export

\[
 \Omega_X(P_X)
 =\Xi_X(d_X^{\rm cur})+r_X+
  \sum_b\beta_bU_b\Omega_{Y_b}(\widetilde P_b),
 \qquad r_X\ge0.
\]

This exact vector identity is the remaining load-bearing producer statement.
It is stronger and more precise than a scalar score recurrence.

## 12. Exact native cocycle

For feasible child rows,

\[
 \Delta_X
 =\delta_{\rm root}(X)+
  \sum_b\beta_b\Delta_{Y_b},
 \qquad
 \delta_{\rm root}(X)=\langle Y_4,r_X\rangle.
\]

`L-91735` gives

\[
 \delta_{\rm root}(X)\le4\log X+C_{\rm root}.
\]

The children lie in the positive typed causal cone.  They are consumed by the
existing subcritical causal envelope, with bounded deficit per unit target
mass.  The root endpoint quantizer, Euler mismatch, knot collar and common port
are not charged a second time to every child.

Since `L-91737` proves the actual retained target mass is below `3020` and
the actual child mass is below one eighth of it, the total child contribution
is `O(1)`.  Thus

\[
 \Delta_X=O(\log X)=o(\log^2X).
\]

This is the content of `L-91736/T-91725`, with the uniform mass input `L-91737`.

# Exact boundary

The packet proves new algebraic and measure-theoretic interfaces and checks the
finite constants.  It does not independently reconstruct:

```text
the factor-67 Hall prefix inequalities;
the complete component-row profile theorem;
the native source interpretation of the endpoint frame;
the analytic adjacent mismatch estimate;
the all-column B-spline collar theorem;
the terminal top-omission packet;
the narrow root correction demand inside the common port;
the exact full-child/current/root-slack vector identity;
the resident one-sided endpoint-to-RH consumer.
```

Therefore:

\[
 \boxed{\text{The reviewer is partly mistaken about the child-mass gap.}}
\]

\[
 \boxed{\text{The review is incomplete about small columns and native normalization.}}
\]

\[
 \boxed{\text{The corrected factor-67 chain is review-ready, not accepted.}}
\]

\[
 \boxed{\text{The Riemann Hypothesis remains unproved.}}
\]

## Live post-publication boundary

PR #482, frozen at PR #481 head `f41bbd7608cc70bc2a8002d43ef99b5e35977968`, independently requests changes. This packet supplies the actual-mass, retained-cell, score-scope, native-cocycle, and root-mass arguments described above. It does not by itself instantiate the complete corrected root packet, the full common-port demand, the exact terminal/base/port `Y_4` pairing, or the external endpoint/WSTS chain. RH remains unproved.
