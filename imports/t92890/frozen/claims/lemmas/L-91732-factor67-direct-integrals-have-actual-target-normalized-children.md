# L-91732 — Aggregate and variable factor-67 direct integrals satisfy the exact target-mass contraction

Claim ID: `L-91732`
Status: **PROVED EXACT POSITIVE-INTEGRAL / TARGET-MASS COMPILATION THEOREM**
Created: 2026-08-15
Depends on: `L-91650`, `L-91375.9`, `L-91658`, `L-91674`, positive homogeneity and Tonelli
Parallel measure-valued inputs: `L-91355.11`, `T-91305`
Audits: PR #478's normalization objection and PR #480's missing-premise objection
RH status: **unproved**

## 1. Direct reconstruction of the controlling aggregate-list construction

Let `(S,\mathcal B,\lambda)` be the finite positive endpoint-parameter space
of the retained factor-67 root packet, after any common positive restriction or
thinning.  Let

\[
 P=\int_SP_s\,d\lambda(s),
 \qquad
 M=m(P)=\int_Sm(P_s)\,d\lambda(s).
\tag{L-91732.1}
\]

Let

\[
 67\le p_1<\cdots<p_k
\]

be the finite union of all rough primes active on any retained source atom.
Put

\[
 r_i=p_i^{-1/2},
 \quad
 s_i=\prod_{h\le i}(1-r_h),
 \quad
 \lambda_i=r_is_{i-1},
 \quad
 \alpha_i=r_i\lambda_i.
\tag{L-91732.2}
\]

For each fiber and each global prime `p_i`, let `B_{i,s}P_s` be its canonical
same-index child when that prime is active, and zero otherwise.  Define the
aggregate child operator

\[
 B_iP=\int_SB_{i,s}P_s\,d\lambda(s).
\tag{L-91732.3}
\]

Causal zero extension makes this a positive typed packet at an ambient endpoint
at most `X/p_i`.  For active pairs, `L-91654` gives positivity of
`P_s-r_iB_{i,s}P_s`; for inactive pairs it equals `P_s`.  Hence

\[
 C_i(P):=P-r_iB_iP
 =\int_S[P_s-r_iB_{i,s}P_s]d\lambda(s)\ge0.
\tag{L-91732.4}
\]

Applying `L-91650` once to the aggregate packet gives

\[
 \boxed{
 P=s_kP+
   \sum_i\lambda_iC_i(P)+
   \sum_i\alpha_iB_iP.
 }
\tag{L-91732.5}
\]

This identity is exact in source labels after the retained realization map,
target, declared and literal score, component rows, ordinary responses,
radix-four responses and child-owned boundary coordinates.

## 2. The aggregate target-mass inequality

`L-91375.9` with inherited scalar one gives, fiber by fiber,

\[
 m(B_{i,s}P_s)\le m(P_s).
\]

Positive integration therefore gives

\[
 \boxed{m(B_iP)\le M.}
\tag{L-91732.6}
\]

The exact coefficient budget of `L-91650` gives

\[
 \sum_i\alpha_i<67^{-1/2}<\frac18.
\tag{L-91732.7}
\]

Consequently

\[
 \boxed{
 \sum_i\alpha_i m(B_iP)
 \le M\sum_i\alpha_i
 <\frac18M.
 }
\tag{L-91732.8}
\]

Equations (L-91732.5)--(L-91732.8) are already the hereditary target-mass
hypotheses of `T-91312`.  No unit-mass normalization of the aggregate children
is required by that consumer.

The global list may contain primes inactive on a given fiber.  Such a prime
assigns the corresponding `lambda_i` fraction of that fiber to the positive
current term and exports no child.  This only decreases recursive mass and does
not duplicate source.

## 3. Why the PR #478 toy counterexample does not apply

PR #478 considers two unit-mass fibers with independently selected
coefficients `1/9` and `1/100`.  Their normalized aggregate coefficient is
indeed `109/1800`.

That example tests a **variable-list** construction.  It does not test
(L-91732.5), where one common global list supplies the same `alpha_i` to the
aggregate operator `B_i`.  The final construction written in `L-91692.30--.31`
is therefore not refuted by the toy calculation.

The frozen proposal should nevertheless have defined (L-91732.3) and displayed
(L-91732.6)--(L-91732.8).  Its omission is a proof-compilation defect, now made
explicit.

## 4. General variable-list theorem

For completeness, let a positive fiber have an exact source-disjoint identity

\[
 \boxed{
 P_s=P_s^{\rm cur}+
 \sum_{i\in I(s)}a_i(s)U_{s,i}Q_{s,i},
 }
\tag{L-91732.9}
\]

where the finite or countable list `I(s)` may vary measurably with `s`.  Assume

\[
 a_i(s)\ge0,
 \qquad
 \sum_{i\in I(s)}a_i(s)\le\rho<\frac18,
\tag{L-91732.10}
\]

and

\[
 m(U_{s,i}Q_{s,i})\le m(P_s).
\tag{L-91732.11}
\]

For the factor-67 fibers, (L-91732.10) is `L-91650` and
(L-91732.11) is `L-91375.9`.  Thus the premise left implicit in PR #476 is
derived:

\[
\begin{aligned}
 \sum_i a_i(s)m(U_{s,i}Q_{s,i})
 &\le m(P_s)\sum_i a_i(s)\\
 &\le\rho m(P_s).
\end{aligned}
\tag{L-91732.12}
\]

## 5. Common restrictions and thinning preserve the inequality

Let `h:S->[0,1]` be measurable and replace `d\lambda` by
`h(s)d\lambda(s)`.  This covers the retained endpoint window, bottom and top
omissions, activation-knot collars, and any one-use scalar safety thinning
performed before the current/child labels are forgotten.

Put

\[
 P=\int_Sh(s)P_s\,d\lambda(s),
 \qquad
 M=m(P).
\]

The actual recursive target mass is

\[
 M_{\rm ch}
 =\int_Sh(s)
   \sum_i a_i(s)m(U_{s,i}Q_{s,i})d\lambda(s).
\]

Tonelli and (L-91732.12) give

\[
 \boxed{
 M_{\rm ch}\le\rho M<\frac18M.
 }
\tag{L-91732.13}
\]

This is the variable-list mass-weighted statement requested by PR #478.

## 6. Actual-mass grouping and optional scalar normalization

Group the child field by a countable discrete placement/provenance class `b`,
which may contain the rough prime, causal channel, first-owner class, boundary
type and normalized same-index placement class.  The real child endpoint stays
inside the packet as a provenance coordinate; causal zero extension places the
aggregate at an ambient endpoint

\[
 Y_b\le X/67+C_0.
\]

Let `R_b` be the positive direct integral of the children in class `b` and

\[
 M_b=m(R_b).
\]

Then

\[
 \sum_bM_b=M_{\rm ch}.
\tag{L-91732.14}
\]

If `M>0` and `M_b>0`, define

\[
 \widehat P_b=M_b^{-1}R_b,
 \qquad
 \widetilde P_b=M\widehat P_b,
 \qquad
 \beta_b=\frac{M_b}{M}.
\tag{L-91732.15}
\]

Then

\[
 m(\widehat P_b)=1,
 \qquad
 m(\widetilde P_b)=M,
\]

and positive integration of (L-91732.9) gives

\[
 \boxed{
 P=P^{\rm cur}+
   \sum_b\beta_bU_b\widetilde P_b,
 \qquad
 \sum_b\beta_b
 =\frac{M_{\rm ch}}M
 \le\rho<\frac18.
 }
\tag{L-91732.16}
\]

If `M=0`, positivity makes the retained packet trivial.  If `M_b=0`, positivity
of the target coordinate on the canonical child cone makes `R_b=0`, so that
class may be discarded.

## 7. Source ownership and consumers

Every original source occurrence retains its endpoint, Hall, first-owner and
generation labels inside exactly one aggregate child.  Grouping changes only
the external packet index.  The exact source and typed identities are preserved
by `L-91658/L-91674`.

There are therefore two equivalent consumer interfaces:

```text
aggregate global list:
    use alpha_i, B_iP and (L-91732.8) directly in T-91312;

variable lists:
    use the actual restricted measures in T-91305, or the optional
    beta_b, tilde P_b scalar normalization in T-91312/T-91314.
```

```text
controlling aggregate-list contraction            EXACT
reviewer's varying-list toy counterexample         NOT CONTROLLING
variable-list weighted premise                     DERIVED
Tonelli mass contraction                           EXACT
actual grouped-child normalization                 EXACT / OPTIONAL
source ownership                                    PRESERVED
Riemann Hypothesis                                  UNPROVEN
```
