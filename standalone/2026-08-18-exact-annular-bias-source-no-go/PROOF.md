# The exact parity-contractive annular bias and the failure of low-child source closure

**Frozen proposal:** PR #565 at `339e3367660f40c74795802a6f8170b15e19b13a`  
**Classification:** sharp corrected theorem plus substantial no-go theorem  
**Riemann Hypothesis:** **unproved**

## Abstract

We reconstruct the complete grouped `P_61` bias used in the parity-contractive
annular proposal. Every real activation cell is certified with directed MPFR
intervals, and an analytic divisor-event tail closes the infinite range. The
claimed lower bound `F/M>=1/40` is false, but the exact global infimum is attained
uniquely at `x=184` and remains strictly above `1/42`:

\[
\inf_{x\ge67}{F(x)\over M(x)}
={F(184)\over M(184)}
=0.0239842935587663046732731586531\ldots
>{1199\over50000}>{1\over42}.
\]

Reconstructing the induction reveals a prior compositional failure. The proposed
low-child recombination deletes six genuine rough Möbius contributions already
at `X=184`; the resulting packet observes `F_61(184)` instead of the native
annular scalar. We also prove that the direct source-complete l1 rough-child
repair cannot contract for any fixed finite cutoff and any positive annular
kernel with a nonzero square-root main term. Thus the scalar certificate is
fully repaired, but the RH proposal is not.

## 1. Exact scalar

Set

\[
q_\star(2)=15,
\quad q_\star(3)=6,
\quad q_\star(4)=3,
\quad q_\star(m)=6\ (m\ge5),
\]

\[
H_x(n)=\min(\log4,\log(x/n))_+,
\quad
A_\star(x)=\sum_{m\ge2}{q_\star(m)\over\sqrt m}H_x(m).
\]

For `P_B=prod_{p<=B}p`, define

\[
F_B(x)=\sum_{d\mid P_B}{\mu(d)\over\sqrt d}A_\star(x/d),
\qquad
M_B(x)=\sum_{d\mid P_B}{1\over\sqrt d}A_\star(x/d).
\]

The proposal uses `B=61`.

Expanding `n=dm` gives

\[
F_B(x)=\sum_n{a_B(n)\over\sqrt n}H_x(n),
\qquad
M_B(x)=\sum_n{b_B(n)\over\sqrt n}H_x(n),
\]

with

\[
a_B(n)=6\mathbf1_{(n,P_B)=1}-6\mu_B(n)+9\mu_B(n/2)-3\mu_B(n/4),
\]

\[
b_B(n)=6\,2^{\omega((n,P_B))}-6\mathbf1_{n\mid P_B}
       +9\mathbf1_{n/2\mid P_B}-3\mathbf1_{n/4\mid P_B}.
\]

These formulas are the arithmetic generator used by the certificate.

## 2. Complete real-cell reduction

The only changes in `H_x(n)` occur at `x=n` and `x=4n`, hence all event points
are integers. On `(N,N+1)`,

\[
F_B(x)=A_N\log x+B_N,
\qquad M_B(x)=C_N\log x+D_N.
\]

Therefore

\[
{d\over d\log x}{F_B(x)\over M_B(x)}
={A_ND_N-B_NC_N\over(C_N\log x+D_N)^2},
\]

and the ratio is monotone or constant on the entire cell. Checking both
one-sided directed endpoint states is sufficient for all real `x`.

The full `P_61` compact ledger covers the 21,933 cells from `67` to `22000`.
The unique minimum endpoint is `184`; the derivative numerator is negative on
`(183,184)` and positive on `(184,185)`. Every other compact endpoint exceeds
`2399/100000`.

## 3. Exact counterexample and true infimum

The directed enclosures are

```text
F(184) = 10.69357964877382995080531550498546444404894853387789461064349...
M(184) = 445.8576035426028363155780773011076426727748731027168181564606...
F/M    = 0.023984293558766304673273158653137477483677710807580463415955...
```

Thus

\[
F(184)-M(184)/40=-0.4528604397912409570841364275\ldots<0,
\]

while

\[
F(184)-M(184)/42=0.0779224215690005147201231882\ldots>0.
\]

The exact value is the ratio of the finite expressions

\[
\log4\sum_{n\le46}{a_{61}(n)\over\sqrt n}
+\sum_{47\le n\le184}{a_{61}(n)\over\sqrt n}\log{184\over n}
\]

and its `b_61` analogue.

## 4. Analytic tail

Write

\[
K(x)=\sum_{n\ge1}{H_x(n)\over\sqrt n}
=2\sqrt x+\zeta(1/2)\log4+e_4(x),
\quad |e_4(x)|\le{1\over6\sqrt x}.
\]

The exceptional weights give

\[
A_\star(x)=6K(x)-6H_x(1)+{9\over\sqrt2}H_x(2)-{3\over2}H_x(4).
\]

At every divisor event the proof object maintains the directed truncated sums
`A,B,C,D,N,D2,D4` and the complete finite correction

\[
\Phi_B(x)=\sum_{d\mid P_B}{\mu(d)\over\sqrt d}H_x(d).
\]

The `2^{18}`-colour `P_61` sweep proves

\[
-1.1462988517<\Phi_{61}(x)<1.4195858313,
\]

hence `|Phi_61|<3/2`. Both sides of all 522,245 tail event groups, as well as
the splice `x=22000`, satisfy the lower and upper rational margins. Between
events the certified lower bounds are increasing. This proves

\[
{1199\over50000}<{F_{61}(x)\over M_{61}(x)}<{9\over200}
\quad(x\ge22000),
\]

and completes the proof of the global infimum.

A 448-bit independent targeted reconstruction overlaps the 320-bit intervals.

## 5. Formal contraction arithmetic

If the source identity asserted in PR #565 were valid, the corrected bounds
would improve its formal current cap to

\[
{1+1/8\over1-1/8}{9\over200}={81\over1400},
\]

and its formal root margin to

\[
{7\over8}{1199\over50000}-{1\over8}{81\over1400}
={38501\over2800000}>0.
\]

This number is not an actual contraction margin: the required native source
equality fails before this estimate is applied.

## 6. Exact low-child source mismatch

The full native scalar factors by rough squarefree part:

\[
\mathcal A_X=
\sum_{r\ {\rm rough}}{\mu(r)\over\sqrt r}F_{61}(X/r).
\]

At `X=184`, only the six rough primes `67,71,73,79,83,89` occur. Hence

\[
\mathcal A_{184}=F_{61}(184)-{15\over\sqrt2}
\sum_p{1\over\sqrt p}\log{92\over p}.
\]

The deleted term is

\[
D_{184}=1.3631478826704517803995957899073789883230\ldots>0.
\]

PR #565 recombines every low child into the parent and therefore produces
`F_61(184)`, not `A_184`. This is an exact source-to-observation discrepancy,
not a weakness of the scalar bound.

## 7. Fixed-cutoff l1 no-go

For every fixed cutoff and every positive annular dictionary with
`M_B(x)=C_B sqrt(x)+O(1)`, direct source-complete child magnitudes satisfy

\[
\sum_{R\le p\le\sqrt x}{1\over\sqrt p}M_B(x/p)
\ge {C_B\sqrt x\over2}
\sum_{R\le p\le\sqrt x}{1\over p}.
\]

After division by `M_B(x)<=2C_B sqrt(x)`, the ratio diverges. Thus no proof that
handles arbitrary history parity by a fixed l1 child contraction can close this
source-complete recurrence. Global signed cancellation or a different producer
is necessary.

## 8. Optimization result

The nearby cutoff `B=37`, rough threshold `41`, has stronger certified local
bias:

\[
{17\over500}<{F_{37}(x)\over M_{37}(x)}<{8\over125},
\qquad x\ge41,
\]

with unique minimum at `x=104`. It does not evade the source mismatch or l1
no-go.

The weights `5:3` are unique up to scale among rows two and three if one requires
elimination of the `3^{-z}` Mellin frequency. Their numerator is

\[
-3(1-2^{-z})(2-2^{-z}),
\]

which is nonzero in `Re z>0`. A fixed dilation only multiplies the transform by
`1-D^{-s}` and cannot repair source ownership.

## 9. Verdict

\[
\boxed{
\inf_{x\ge67}{F(x)\over M(x)}={F(184)\over M(184)}>{1\over42}.
}
\]

\[
\boxed{
\text{The low-child parity-contractive induction of PR #565 is not source-complete.}
}
\]

The scalar theorem is unconditional. The RH proposal is not repaired by it.
The Riemann Hypothesis remains unproved.
