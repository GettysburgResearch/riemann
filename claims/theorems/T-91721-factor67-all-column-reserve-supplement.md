# T-91721 — The all-column reserve repairs the factor-67 SONTR finite realization

Claim ID: `T-91721`  
Status: **PROVED CONDITIONAL SUPPLEMENT TO PR #473 / FULL DEPENDENCY REVIEW STILL REQUIRED**  
Created: 2026-08-14  
Depends on: `L-91723`; frozen PR #473 stack `L-91688/L-91690/L-91691/L-91692/T-91660/T-91661`; direct-integral normalization `L-91694` if used  
RH status: **unproved pending reconstruction**

## 1. Scope of the supplement

The factor-67 proposal separates physical columns into:

```text
K<=q<=X/4        compact interior reserve;
q>X/4            terminal omission reserve;
q above support  exact zero response.
```

The global endpoint collar and finite mismatch can nevertheless feed the
remaining columns `2<=q<K`. The original displayed `177/K` reserve is not a
proof for that range.

`L-91723` closes the missing range with one source-owned global thinning

\[
 \tau_K=\frac{\sqrt K}{\sqrt K+130}.
\tag{T-91721.1}
\]

It proves, simultaneously for every nonterminal physical detail column,

\[
 \boxed{
 \Xi_{\rm realized}(q)
 \le
 \Omega_X(q)-s_X(q),
 \qquad
 s_X(q)>
 \frac{\Omega_X(q)}{\sqrt K+130}.
 }
\tag{T-91721.2}
\]

Ordinary feasibility follows through the positive radix-four inverse.

## 2. Compatibility with the frozen terminal and ownership clauses

For `K>=2`, `tau_K` is no larger than the original `K/(K+178)` factor.
Therefore the terminal omission, taper and above-support arguments of the
frozen factor-67 packet are unchanged or improved.

The factor is applied once to the complete labelled parent measure. Hence:

\[
 \sum_b\alpha_b<\frac18
\tag{T-91721.3}
\]

is unchanged, and every source atom, correction, omission and common-port
coordinate retains one owner.

If the aggregate target-mass normalization is formulated through positive
direct integrals, use the exact mass-weighted theorem `L-91694`; no
unweighted count of endpoint fibers is permitted.

## 3. Deficit consequence

The equality-score cost of (T-91721.1) is below `4290`. All other finite
correction costs remain the frozen absolute constants. Thus the completed
finite realization has

\[
 J_\Lambda(X)-\operatorname{Score}(d_X)
 \le4\log X+C_{\rm all}
 =o(\log^2X)
\tag{T-91721.4}
\]

for one absolute `C_all`, subject to reconstruction of the frozen Hall,
first-owner, port and endpoint-consumer inputs.

The stronger thinning therefore repairs finite realization without weakening
the endpoint asymptotic required by `T-91313`.

## 4. Conditional conclusion

On a frozen stack where the following have been independently reconstructed:

```text
factor-67 root Hall source identity;
rough first-owner partition;
positive causal current/child identity;
mass-weighted recursive target coefficient <1/8;
one common endpoint quantizer and one common port;
terminal omission and finite base correction;
positive radix-four dual and one-sided endpoint consumer;
```

`L-91723` supplies the previously missing all-column capacity clause. The
resulting packet satisfies the Native-Root Capacity interface with
`Y_4`-weighted slack `O(log X)`.

This is a complete **conditional supplement**, not an independent declaration
that SONTR, NRCT or RH is accepted.

## 5. Exact boundary

```text
small physical columns 2<=q<K                 CLOSED / L-91723
all nonterminal ordinary/detail feasibility    CLOSED ON FROZEN INPUTS
terminal and above-support feasibility         IMPORTED / IMPROVED BY THINNING
recursive target mass <1/8                     IMPORT L-91694 / RECONSTRUCT
common port and endpoint frame                  IMPORTED / RECONSTRUCT
SONTR / NRCT                                    CONDITIONAL PROPOSAL
Riemann Hypothesis                              UNPROVEN
```
