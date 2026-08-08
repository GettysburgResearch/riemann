# Full-problem attack: dyadic one-crossing and endpoint domination

Date: 2026-08-08  
Agent: `gpt56-pro`  
Parent: PR #276 at `a65a02b9463c1cc3a10d0af03ab359a637e357cd`  
Status: **new full conditional RH proposal; RH unproved**

## 1. Why the route was changed

The live repository has accumulated many exact carry, Green, reflected, and digital interfaces. PR #276 correctly identifies that their conclusion-producing burden collapses to one scalar theorem, WSTS, and that WSTS is itself RH-equivalent.

Continuing to refine generic physical-to-carry maps would therefore risk circling an equivalent norm. This pass attacks the WSTS scalar directly and asks for a stronger global sign law.

## 2. Main new theorem

The continuum dyadic shell density

```text
D(theta)=E(theta)-sqrt(2)E(2theta) 1_(theta<=1/2)
```

has exactly one sign change. The zero lies in quotient cell seven:

```text
0.1408520350 < theta_* < 0.1408520351.
```

The density is positive below `theta_*` and negative above it.

The proof is not numerical. On each reciprocal cell,

```text
D_N(theta)=theta^(-1/2)[U_N+V_N log theta]-W_N,
V_N>0.
```

The derivative has at most one zero, always a maximum, so cell minima occur at endpoints. Sum–integral estimates prove all cells below `1/9` decrease with the ratio; finite explicit cells settle the upper sector and the unique cell-seven crossing.

## 3. New finite-shell sharpening

The dyadic shell seed is itself simpler than either endpoint:

```text
B_c(u)=B(u)-sqrt(c)B(u/c)1_(u<=c).
```

For `u<=c`,

```text
B_c(u)=2 sqrt(u) log(1/c)+4u(1-c^(-1/2)).
```

The logarithmic singularities cancel exactly. Consequently the finite response satisfies

```text
s_(X,Y)(q)=X^(-1/2)E_c(q/X)+O(q^(-3/2)),
```

uniformly at the integer dyadic ratio `c=floor(X/2)/X`. The former `log(X/q)` loss is absent.

This reduces finite one-crossing to two bounded gates:

```text
fixed low coordinates;
a bounded-width collar around theta_* X.
```

No growing sign table remains.

## 4. Collapse of WSTS

Assume the finite shell has one sign crossing. Since `log p>0`, the weighted prime shell has the same order. Every tail sum first decreases while negative terms are added, then increases while positive terms are added. Its maximum is therefore the complete tail or zero:

```text
B_X=[sum_(p<=X) log(p)s_X(p)]_+.
```

If

```text
Delta_X=J_(P,X)(b_X^(0))-P_X,
```

then exactly

```text
sum_(p<=X) log(p)s_X(p)
=Delta_X-Delta_floor(X/2).
```

Thus WSTS becomes one dyadic increment of one prime-ramp discrepancy.

## 5. Endpoint domination

Differentiating the parabolic seed gives the explicit positive endpoint source

```text
dot b_X(m)=2 sqrt(m)(1-sqrt(m/X)) 1_(m<=X).
```

The derivative of the discrepancy is

```text
partial_(log X) Delta_X
=sum_(p<=X) log(p)[v_p(dot b_X)-p^(-1/2)].
```

The proposed Endpoint Prime Domination theorem states that this is nonpositive.

A source-specific construction is suggested by two existing exact results:

1. PR #240 `L-23827`: every continuum endpoint atom is tail-majorized by its critical target increment;
2. PR #274 `L-27304`: nonnegative blocks between squarefree endpoints are exactly neutral on every proper prime power and have nonnegative logarithmic objective.

The preferred production theorem, Endpoint Squarefree Collector (`ESC`), is to lift the continuum monotone coupling to those exact squarefree incidence blocks. It would prove EPD without an external prime asymptotic.

## 6. Full conditional deduction

```text
FSCR
-> WSTS tail family collapses to one total shell;

EPD
-> Delta_X is nonincreasing;

therefore
B_X=0 eventually
-> WSTS
-> prime ramp >=4 sqrt(X)-X^o(1)
-> square-screw / Landau
-> RH.
```

A weaker subpower bound on the dyadic increment of `Delta` also suffices.

## 7. Finite evidence

The committed replay checks all integer coordinates through `20,000` and all prime coordinates through `200,000`. A separate optimized scan through `10^7` found no one-crossing or weighted-tail violation.

This evidence is not promoted to a theorem.

## 8. Relations to other live routes

- **WSTS:** the new sign law would prove the canonical final scalar with zero debt.
- **DCCS / central cascade:** the lattice commutator is another potential producer for the bounded FSCR gates or endpoint scalar; it is not imported as proved.
- **Third-Abel producer:** a proof of its all-scale prefix/collar signs may furnish an explicit positive fragmentation realizing the endpoint collector.
- **Factor-five reflected route:** parity/physical frames may attack the endpoint boundary scalar, but pure carry windows cancel the RH pole and cannot replace EPD.
- **Squarefree collectors:** they are the preferred arithmetic lift because prime-only transport has a deterministic density drift.

## 9. Exact boundary

```text
continuum one-crossing                      proposed complete
shell-error cancellation                    proposed complete
finite sign problem -> bounded gates        proposed complete reduction
one-crossing collapse of WSTS                proposed complete
endpoint derivative identity                proposed complete
FSCR                                        open
ESC/EPD                                     open / RH-bearing
FSCR+EPD -> RH                              complete conditional chain
RH                                          unproved
```

The contribution is a full-problem sign architecture and a genuinely stronger continuum theorem. It is not represented as an unconditional proof.
