# T-91725 — PR #478 audit supplement compiles target-mass, retained-cell, and native-slack interfaces

Claim ID: `T-91725`
Status: **PROVED CONDITIONAL AUDIT SUPPLEMENT TO PR #481 — INDEPENDENT REVIEW REQUIRED**
Created: 2026-08-15
New inputs: `R-91727`, `L-91732`--`L-91737`
Stacked finite-root inputs: PR #479 at `518b6a5ec2b49b7decbd4c2e349d0ee5b26bfc9b`
Frozen local inputs: PR #473 at `71d6a859ea741fe035de709e8d10ed37301b778e`; PR #464 endpoint-frame formalism; narrow `P_61/67` Schur displays; `T-91312/T-91313`
Supersedes as controlling composition: `T-91660.8`, `T-91661`, and the uncompiled small-column and child-mass passages
RH status: **unproved pending independent reconstruction of the frozen producer and consumer stack**

Live scope note: PR #482 reviews PR #481 at `f41bbd7608cc70bc2a8002d43ef99b5e35977968` and identifies four further reconstruction obligations: one concrete post-Hall/post-quantization packet equality, instantiation of the complete port demand, an explicit `Y_4` pairing for terminal/base/port corrections, and the frozen endpoint/WSTS consumer. This supplement does not silently claim those obligations are closed.

## 1. Audit verdict incorporated into the theorem

PR #478 is correct on the compact-reserve arithmetic and correct that PR #473
does not establish RH.  Its first-gap diagnosis is too strong:

```text
the varying-list mass-normalization theorem was not written;
the final L-91692 construction instead uses one aggregate global prime list;
that aggregate list already satisfies the weighted target-mass inequality once
L-91375.9 and L-91674 are inserted.
```

The theorem below makes that compilation explicit and also repairs the two
earlier breaks missed by PR #478:

\[
 2\le q<K
\]

and

\[
 4\sqrt X-\mathcal H(d_X)=O(1).
\]

## 2. One labelled positive root packet

For every sufficiently large endpoint `X`, put

\[
 K=\left\lfloor\frac X{67}\right\rfloor+1.
\]

Retain the endpoint, small-divisor Hall, rough first-owner and generation labels
until all positive sums are formed.  Bottom cells, the fixed top interval and
activation-knot collars are common positive restrictions of this one endpoint
measure.  The square-root safety factor and same-cell positive refinement are
also applied to the common labelled measure, not independently to children.

On every retained root fiber,

\[
 X/s<67.
\]

The frozen target-Hall theorem therefore uses only the squarefree `P_61`
source.  It is target-exact and score-superordinate, and its total physical row
is transparent when the nonnegative Hall bonus is retained.  Rough primes
begin at `67` and retain their exact first-owner labels.

The finite equality seed is never identified with its continuum model.  The
controlling identity is

\[
 \boxed{b_X^\star=\bar b_X^\star+E_X.}
\tag{T-91725.1}
\]

## 3. Exact aggregate child-mass contraction

Let `p_1<...<p_k` be the union of all active rough primes in the retained
aggregate packet.  Use zero child on fibers where a global prime is inactive.
`L-91732` defines the positive aggregate child operators `B_i` and proves

\[
 \boxed{
 P=P^{\rm cur}+\sum_i\alpha_iB_iP,
 \qquad
 \sum_i\alpha_i m(B_iP)<\frac18m(P),
 \qquad
 Y_i\le X/67+1.
 }
\tag{T-91725.2}
\]

The first equality abbreviates the exact current terms of `L-91650`; it holds
in source labels, target, score, component rows, ordinary responses,
radix-four responses and child-owned boundary coordinates.

This already feeds `T-91312`.  If a variable fiberwise list is preferred,
`L-91732` derives the missing pointwise target-mass premise, applies Tonelli,
groups by actual provenance/placement class and supplies the optional scalar
normalization

\[
 \sum_b\beta_b<\frac18,
 \qquad
 m(\widetilde P_b)=m(P).
\tag{T-91725.3}
\]

Thus PR #478's requested mass-weighted interface is explicit, but no new
arithmetic contraction theorem was needed.

The exact retained root target mass is also uniformly bounded.  `L-91737` uses
the actual endpoint measure `2L(x)dx/x`, the factor-67 target atoms and positive
integration to prove

\[
 \boxed{m(P_X)<3020.}
\tag{T-91725.4}
\]

This supplies the uniform native-mass premise of `T-91305`; the certificate
count `54` is not used as a substitute for physical target mass.

## 4. Every physical column is covered

Let `I_X` be the actual retained set of endpoint cells.  `L-91733` constructs

\[
 E_X^I(n)=
 \sum_{\substack{m\in I_X\\m\ge n}}
 \varepsilon_X(m),
\]

so that

\[
 E_X^I(n)-E_X^I(n+1)
 =\mathbf1_{I_X}(n)\varepsilon_X(n)
\]

with no cutoff atom.  For every physical `q>=2`,

\[
 v_q(E_X^I)=
 \sum_{jq\in I_X}\varepsilon_X(jq).
\]

The frozen adjacent-error and collar bounds give

\[
 |\mathcal D_4v_q(C_X-E_X^I)|
 <\frac{971}{4q\sqrt K},
\tag{T-91725.5}
\]

and therefore

\[
 \frac{|\mathcal D_4v_q(C_X-E_X^I)|}
      {\Omega_X(q)}
 <\frac{129}{\sqrt K}
 \qquad(2\le q\le X/4).
\tag{T-91725.6}
\]

Use

\[
 \tau_K=\frac{\sqrt K}{\sqrt K+130}.
\]

Before finite relative refinement, every nonterminal physical column has the
strict reserve

\[
 s_X(q)>
 \frac{\Omega_X(q)}{\sqrt K+130}.
\]

`L-91734` removes finite activation-knot collars by absolute continuity and
chooses a positive same-cell mesh which consumes less than half this reserve.
Hence

\[
 \boxed{
 s_X^{\rm final}(q)>
 \frac{\Omega_X(q)}{2(\sqrt K+130)}>0
 \qquad(2\le q\le X/4).
 }
\tag{T-91725.7}
\]

Positive radix-four inversion gives ordinary feasibility.  Since
`tau_K<=K/(K+178)` for `K>=2`, the frozen terminal omission margin is preserved;
above retained support the response is zero.

## 5. One narrow aggregate port

Only the uncolored Schur-reserve displays are imported:

\[
 M_b\succeq\frac19\mathcal V_bI,
 \qquad
 \tau_{p_b}\mathcal V_b<\frac19\mathcal V_b.
\]

Positive summation before port observation gives one aggregate current-owned
port.  The physical causal children have zero root-global port coordinate.
No colored affine lift or colored-to-physical projection is imported.  The
analytic construction of the frozen correction demand remains a separate
review input.

## 6. Correct native root cost

Let `H_0(X)` be the unthinned positive root-Hall score.  The frozen score
superordination gives `H_0(X)>=4sqrt(X)`.  Therefore

\[
 4\sqrt X-\tau_KH_0(X)<4290.
\]

This constant is valid at the continuum-shortfall scope.  The exact native
benchmark bridge gives

\[
 J_\Lambda(X)-4\sqrt X<4\log X,
\]

so, after the bounded top/base/port corrections and the `o(1)` knot and
localized-error terms of `L-91734/L-91735`, the one-time root slack satisfies

\[
 \boxed{
 \delta_{\rm root}(X)
 :=\langle Y_4,r_X\rangle
 \le4\log X+C_{\rm root}.
 }
\tag{T-91725.8}
\]

An independent elementary fallback bounds the incremental safety slack by
`4290 log(X)`; either estimate is `o(log^2 X)`.  The theorem does not use or
assert

\[
 4\sqrt X-\mathcal H(d_X)=O(1).
\]

## 7. Exact native root-to-causal composition

Reserve every complete child capacity once.  The root identity is

\[
 \Omega_X(P_X)
 =\Xi_X(d_X^{\rm cur})+r_X+
  \sum_b\beta_bU_b
  \Omega_{Y_b}(\widetilde P_b).
\tag{T-91725.9}
\]

After inserting feasible child rows, `L-91736` gives

\[
 \boxed{
 \Delta_X
 =\delta_{\rm root}(X)+
  \sum_b\beta_b\Delta_{Y_b},
 \qquad
 \Delta_X=J_\Lambda(X)-\mathcal H(d_X).
 }
\tag{T-91725.10}
\]

The children are now in the positive typed causal cone.  They are consumed by
the existing subcritical causal envelope `T-91312/T-91305`; the root endpoint
quantizer, knot collar, Euler mismatch and common port are not charged again to
every child.  With `m(P_X)<3020` from `L-91737` and `sum beta_b<1/8`, the
complete child contribution is `O(1)`.  Hence

\[
 \boxed{
 \Delta_X=O(\log X)=o(\log^2X).
 }
\tag{T-91725.11}
\]

## 8. Conditional endpoint consequence

If the exact frozen Hall/profile theorem, endpoint-frame source realization,
retained-cell correction, terminal packet, narrow port, full-child identity
(T-91725.9), positive causal envelope and one-sided endpoint consumer are
independently reconstructed at their locked blobs, (T-91725.11) is precisely
the producer input of `T-91313`.  The resident implication then yields the
proposed implication to RH.

This is a conditional **audit supplement** to the corrected proposal, not an accepted proof.  The new
algebra and constants do not independently reconstruct every frozen analytic
input.

## 9. Exact audit disposition

```text
Hall total-row transparency                         reviewed / retained
factor-67 density and C67 constants                 reviewed / retained
aggregate target-mass contraction                   compiled / L-91732
uniform retained physical target mass               <3020 / L-91737
variable-list actual-mass wrapper                   L-91732 / optional
small columns 2<=q<K                                closed / L-91733
activation-knot score and relative refinement       L-91734
continuum thinning shortfall                        <4290 / retained
native root cost                                    <=4 log(X)+C / L-91735
native root-to-causal cocycle                       L-91736
contradictory b*=bar b* display                     replaced by b*=bar b*+E
T-91660.8 continuum normalization                   rejected
path/blob/scope lock                                included in packet
corrected SONTR/NRCT composition                    review-ready conditional
Riemann Hypothesis                                  unproved
```
