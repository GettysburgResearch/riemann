# T-24506 — Central-Neumann dipole-descent proposal for RH

Claim ID: `T-24506`  
Status: **FULL ELEMENTARY PROPOSAL — ONE SOURCE-SPECIFIC DYADIC VARIATION THEOREM OPEN**  
Scope: full Riemann Hypothesis conditional on `CNVD`  
Issue: #245  
Date: 2026-08-08

## 1. Why this proposal replaces the monotone cover

The current repository contains two decisive corrections.

First, a nonnegative Divisibility Cover of the raw parabolic positive defect necessarily costs order `sqrt(X)`. Second, the ordinary-prime unweighted queue has a deterministic positive density drift of order `sqrt(X)/log^2(X)`. Hence a correct sharp construction must transport positive and negative arithmetic mass **before** taking positive parts, and it must retain the logarithmically weighted dyadic shell.

`L-24523` supplies an explicit signed transport with exactly those features. No optimization or unknown finite geometry remains.

## 2. The producer

For the central split

\[
n=\lfloor n/2\rfloor+\lceil n/2\rceil,
\]

let `P_X` be the exact carry one-pass operator and `T_X=I-P_X`. `L-24523` proves

\[
(T_Xf)(q)
=\sum_{k\ge0}
\left[f((2k+2)q-1)-f((2k+3)q)\right].
\tag{T-24506.1}
\]

If `f` is supported through `Y`, then `T_Xf` is supported through

\[
\left\lfloor{Y+1\over2}\right\rfloor.
\]

Thus `T_X` is nilpotent on every finite endpoint.

For

\[
w_X(q)=q^{-1/2}\log(X/q),
\]

define

\[
f_0=w_X,
\qquad f_{r+1}=T_Xf_r,
\]

and

\[
A_X(n)=\sum_r[f_r(n)-f_r(n+1)].
\tag{T-24506.2}
\]

The sum has only `O(log X)` nonzero stages. Exactly,

\[
\boxed{
\sum_{n=q}^{X}A_X(n)
\chi_{n,\lfloor n/2\rfloor}(q)
=w_X(q)
\qquad(2\le q\le X).
}
\tag{T-24506.3}
\]

Every integer carry column is saturated.

## 3. Prime-ramp identity

Let

\[
\ell_n=\log\binom n{\lfloor n/2\rfloor},
\qquad
c_n=\sum_{q=2}^{n}\chi_{n,\lfloor n/2\rfloor}(q).
\]

Then

\[
\boxed{
\mathcal P(X)
=\sum_{n=2}^{X}A_X(n)\ell_n,
}
\tag{T-24506.4}
\]

where

\[
\mathcal P(X)=
\sum_{p^a\le X}{\Lambda(p^a)\over\sqrt{p^a}}
\log{X\over p^a}.
\]

Also

\[
\boxed{
\mathcal C(X)
:=\sum_{q=2}^{X}{1\over\sqrt q}\log{X\over q}
=\sum_nA_X(n)c_n
=4\sqrt X+O(\log X).
}
\tag{T-24506.5}
\]

The elementary local comparison is

\[
|\ell_n-c_n|\ll\sqrt n.
\tag{T-24506.6}
\]

Hence

\[
|\mathcal P(X)-4\sqrt X|
\ll
\log X+\sum_n\sqrt n|A_X(n)|.
\tag{T-24506.7}
\]

## 4. Only negative variation is load-bearing

Put

\[
\mathcal V_X^-
=\sum_n\sqrt n(-A_X(n))_+.
\]

`L-24524` proves from the exact carry load that

\[
\boxed{
\sum_n\sqrt n|A_X(n)|
\ll(\log X)^2+\mathcal V_X^-.
}
\tag{T-24506.8}
\]

Thus the one source-specific theorem is

\[
\boxed{
\textbf{CNVD:}\qquad
\mathcal V_X^-=X^{o(1)}.
}
\tag{T-24506.9}
\]

Under CNVD,

\[
\boxed{
\mathcal P(X)=4\sqrt X+X^{o(1)}.
}
\tag{T-24506.10}
\]

This is strictly more constructive than an existential signed-dipole theorem: the complete candidate flow is already written down in (T-24506.1)--(T-24506.3).

## 5. Proposed factor-two proof of CNVD

The exact support descent suggests the following production theorem.

### Central-Neumann Shell Descent (CNSD)

After combining the upper endpoint shell and the lower half-scale target before taking signs, the completed Neumann negative ledger obeys

\[
\boxed{
\mathcal V_X^-
\le
\mathcal V_{\lfloor(X+1)/2\rfloor}^-
+C(1+\log X)^A.
}
\tag{T-24506.11}
\]

The intended proof has four finite steps.

1. Expand every central residual by the exact interval formula (T-24506.1).
2. Pair the `X` and `floor(X/2)` cascades before taking negative parts.
3. Cancel the continuum density drift by the logarithmically weighted dyadic shell identity already isolated in the WSTS programme.
4. Charge the remaining reciprocal-knot and endpoint terms to the exact central row load. Their complete weighted mass is polylogarithmic because every stage has half-scale support and there are only `O(log X)` stages.

If CNSD is proved, iteration gives

\[
\mathcal V_X^-=O((\log X)^{A+1}),
\]

hence CNVD.

The third step is the load-bearing arithmetic step. It cannot be replaced by an absolute-value estimate of the two scales separately. The canonical `WSTS <=> RH` theorem shows why: the shell sampling remainder contains the full reciprocal-zeta obstruction.

Accordingly this proposal is deliberately falsifiable. A valid proof of CNSD must write the finite shell pairing of the **actual Neumann coefficients**, not invoke WSTS as an assumption.

## 6. Completion to RH

CNVD gives the sharp prime-power ramp (T-24506.10). At square endpoints `X=N^2`, the repository's square-screw identity then gives the required subpower upper envelope for the screw function. Critical square sampling propagates it to the half-line. The one-sided Laplace identity for `xi'/xi` and the upper-envelope Landau theorem exclude every zero with real part greater than `1/2`; functional-equation symmetry gives RH.

Thus

\[
\boxed{
\mathrm{CNSD}
\Longrightarrow
\mathrm{CNVD}
\Longrightarrow
\mathcal P(X)=4\sqrt X+X^{o(1)}
\Longrightarrow
\mathrm{RH}.
}
\tag{T-24506.12}
\]

## 7. Nonnegative-certificate interpretation

The theorem is formulated through a signed central producer because the repository now proves that taking positive parts too early incurs a `sqrt(X)` tax. Once CNVD gives the sharp scalar, the existing finite adapters recover a nonnegative proof certificate without losing the main term:

- proper prime powers have only `O(log^2 X)` total cost;
- ordinary-prime finite positivity geometry has zero additional geometric tax;
- alternatively, the signed flow can be cycle-repaired inside the atomized Pascal fragmentation space.

So the construction addresses the user's requested goal in the correct order:

```text
macroscopic positive/negative parabolic defect
-> exact signed factor-two transport
-> subpower negative ledger
-> sharp scalar
-> nonnegative finite certificate
-> RH.
```

The failed monotone cover attempted the last two transport steps in the opposite order.

## 8. Connections to other elementary equivalences

### Lagarias–Robin

The branch already imports

\[
\mathrm{RH}
\iff
\sigma(n)\le H_n+e^{H_n}\log H_n
\quad(n\ge1).
\]

`T-24504/T-24505` identify its scalar obstruction with the same critical prime-ramp deficit. The central-Neumann construction is therefore a proposed **producer** for the arithmetic inequality measured by the Lagarias criterion, not an independent assumption of it.

### WSTS

The newest canonical consolidation proves `WSTS <=> RH`. CNSD should be viewed as a constructive route to WSTS: the central residual is already organized into exact half-scale shells, while `L-24524` identifies the only signed variation that can survive them.

### Dyadic bottom charge

The opposite-parity/bottom-charge programme proves that the dyadic Mertens shell, its Riesz primitive, and the bottom carry charge are one source. The continuum multiplier of the central producer contains

\[
[(1-2^{1-s})\zeta(s)]^{-1},
\]

so the same dyadic source is visible here from the inverse side. This gives a mandatory mutation for any CNSD proof.

## 9. What this proposal deliberately does not use

It does not use:

- monotone Divisibility Cover;
- the refuted unweighted prime-tail queue;
- generic Green coercivity;
- pure carry-window physical transference;
- finite positivity extrapolation;
- a hidden assumption of WSTS or the Lagarias inequality.

## 10. Review protocol

A reviewer should reconstruct in this order:

1. `L-24523.1`: the exact central square-wave residues;
2. `L-24523.4`--`L-24523.8`: one-pass telescoping and nilpotence;
3. the exact saturation (T-24506.3);
4. the prime/all-integer ledgers;
5. `L-24524.3`--`L-24524.6`: why only negative variation matters;
6. the continuum eta/zeta firewall;
7. CNSD, with the `X` and half-scale shells recombined before signs;
8. the inherited square-screw/Landau consumer.

Reject the proposed completion if CNSD:

- estimates the two dyadic scales separately by total variation;
- deletes the endpoint `2q-1` shifts;
- loses the `2/3` or dyadic Mertens mutations;
- treats finite nilpotence as a uniform analytic contraction;
- uses numerical coefficient ranges as the cofinal theorem.

## Status boundary

Proved/proposed complete in the new packet:

```text
central carry square-wave algebra           exact
finite Neumann inverse                      exact
factor-two support descent                  exact
signed saturation of all integer columns    exact
prime/all-integer objective ledgers          exact
negative-part -> total-variation adapter    exact
CNVD -> sharp prime ramp -> RH               complete conditional chain
```

Open and load-bearing:

```text
CNSD / unconditional CNVD                   UNPROVEN / RH-BEARING
Riemann Hypothesis                          UNPROVEN
```

This is a complete explicit proof proposal with one source-specific dyadic variation theorem left for adversarial attack. It is not presented as an accepted proof of RH.
