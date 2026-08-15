# Independent frozen-head review of PR #495 at `50f45b46cbe3c471d6e702c41c7ef178b530e1ab`

## Freeze

```text
repository:       gfreund123/riemann
review cutoff:    2026-08-15T18:55:44Z
proposal PR:      #495
proposal base:    research/gpt56-pro/92900-two-ledger-terminal-child-closure
base SHA:         37f14be7c8bd16b3096baf08f6ba2cbc550797ac
proposal branch:  research/gpt56-pro/91760-native-volterra-common-parent
reviewed head:    50f45b46cbe3c471d6e702c41c7ef178b530e1ab
review branch:    review/pr495-volterra-frozen-50f45b46-20260815
```

This review is confined to PR #495's Volterra construction. PR #497 is reviewed separately and is not used as confirmation or as a source of missing lemmas.

No large computation was rerun. The retained `X-91760` files were inspected, and a new small exact rational-interval certificate was produced for the first failed causal row.

## Executive verdict

```text
mathematical type:  proposed complete native-root composition
review verdict:     FALSE AT L-91763.2
first broken arrow: infinitesimal Volterra fibres are not hereditary
                    positive causal generators
RH status:          UNPROVEN
```

The route makes substantial genuine progress before the failure:

1. the Volterra antiderivative is exact;
2. the support restrictions make the sum/integral interchange finite;
3. the infinitesimal row `p_s` is coefficientwise nonnegative;
4. Möbius colours become one rank-one scalar source partition;
5. the rough lift and its Jacobian are exact;
6. first-owner source labels can be kept disjoint.

The failure occurs when `L-91763` applies the canonical causal-generator theorem `L-91654` to the new infinitesimal packet family `p_s`. `L-91654` proves positivity for the canonical endpoint rows `Q_s`; it does not prove positivity for their normalized endpoint derivatives. The analogous causal row difference is in fact negative at an explicit factor-67 witness.

Consequently the child-capacity interface, subcritical positive source ledger, and complete native ledger are not reached.

# Reconstruction

## 1. Volterra antiderivative

For

\[
g_s(m)=\left(\sqrt m-\frac{m}{\sqrt s}\right)\mathbf 1_{m\le s},
\qquad
p_s=\mathcal R g_s,
\]

the one-colour identity of `L-91760` is correct. With `Y=X/k`, direct integration gives

\[
\frac1{\sqrt k}\int_n^Y t^{-1/2}\log\frac Yt\,dt
=
\int_n^Y\frac2s\,\ell_{X/s}(k)g_s(n)\,ds,
\]

and both sides equal

\[
\frac1{\sqrt k}
\left[
4(\sqrt Y-\sqrt n)-2\sqrt n\log\frac Yn
\right].
\]

There is no hidden endpoint term. At the lower activation boundary `g_n(n)=0`; at the upper boundary the identity is an ordinary finite integral identity, not a differentiated moving-boundary assertion.

**Disposition:** `VERIFIED`.

## 2. Support and Fubini

For each fixed coordinate `n`, only

\[
k\le X/n,\qquad n\le s\le X/k
\]

occur. The Möbius sum is finite, and every row, ordinary column, or detail column sees only finitely many active seed coordinates. Thus the order swap is finite Fubini, not a conditional infinite rearrangement.

Applying the finite row map after the coordinatewise identity is legitimate. It yields

\[
\overline c_X
=
\int_1^X \frac{2L(X/s)}s\,p_s\,ds.
\]

The required factor-67 positivity of `L(x)` on `1\le x<67` is mathematically true, but the exact supporting `L-91692` file is not present at the frozen PR #495 head. The 66-cell statement should be pinned explicitly rather than cited through an absent sibling. This is a provenance repair, not the broken mathematical arrow.

**Disposition:** `VERIFIED WITH PROVENANCE FIX`.

## 3. Typed positivity of the infinitesimal row

The retained part of `L-91112` proves

\[
\partial_s d_s(j)\ge0.
\]

Since

\[
g_s=\frac s2\,\partial_s b_s
\]

and the row map is finite and linear,

\[
p_s(j)=\frac s2\,\partial_s d_s(j)\ge0.
\]

Equivalently, for every `j>=2`,

\[
p_s(j)
=(j+1)\left[
 \frac{g_s(j)}{j-1}
 -\frac{2g_s(j+1)}j
 +\frac{g_s(j+2)}{j+1}
\right].
\tag{R495.1}
\]

Thus `p_s` is a genuine nonnegative physical row. This does not imply that the family is monotone under the factor-67 causal subtraction.

**Disposition:** `VERIFIED`.

## 4. Rank-one source ownership

After the Volterra order swap, every squarefree Möbius colour `k` multiplies the same physical feature `p_s`; only the scalar

\[
\ell_{X/s}(k)>0
\]

depends on `k`. On the positive-density interval, the complete bipartite transport from negative to positive colour mass is an exact scalar matching. Exhausting all negative mass leaves a positive residual of total scalar weight `L(X/s)`.

This supplies a literal one-use small-divisor ledger. The small-divisor labels `k<67` are disjoint from rough first-owner labels `p>=67`, so the two ownership coordinates do not collide.

**Disposition:** `VERIFIED WITH THE SAME FACTOR-67 DENSITY PIN`.

## 5. Rough lift

Starting from

\[
\overline D_{P,X}
=
\sum_{m\in\mathcal R_{67}}
m^{-1/2}U_m\overline c_{X/m},
\]

substitution of the Volterra identity and `S=ms` gives

\[
\overline D_{P,X}
=
\int_1^X \frac{2L(X/S)}S
\left[
 \sum_{\substack{m\in\mathcal R_{67}\\m\le S}}
 m^{-1/2}U_mp_{S/m}
\right]dS.
\]

The load-bearing Jacobian is

\[
m^{-1/2}\frac2s\,ds
=
m^{-1/2}\frac2S\,dS.
\]

There is no extra factor of `m`. Every sum is finite in each physical coordinate, and first-owner labels may be transported through the same-index map without duplication.

**Disposition:** `VERIFIED`.

# First broken arrow: `L-91763.2`

`L-91763` next asserts that every positive labelled Volterra fibre admits the canonical causal decomposition with current terms

\[
p_s-p^{-1/2}U_pp_{s/p}
\]

inside the positive typed source cone, citing `L-91654`.

That citation changes packet families. `L-91654` establishes

\[
Q_s(j)-p^{-1/2}Q_{s/p}(j)\ge0
\]

for the canonical endpoint packet. It does not establish the same inequality for

\[
p_s=\frac s2\,\partial_s Q_s.
\]

The latter inequality is false.

## Exact factor-67 counterexample

Take

```text
rough prime:       p=67
child endpoint:    y=15
parent endpoint:   s=py=1005
component row:     j=14
```

Using (R495.1),

\[
\begin{aligned}
D
&:=p_{1005}(14)-67^{-1/2}p_{15}(14)\\
&=
4+\frac{15\sqrt{14}}{13}
-\frac{15\sqrt{15}}7
-\frac1{91\sqrt{1005}}
-\frac{15\sqrt{14}-14\sqrt{15}}{13\sqrt{67}}.
\end{aligned}
\tag{R495.2}
\]

Exact rational enclosures for the four square roots, with denominator `10^24`, give

\[
\boxed{
-\frac{184291}{10^9}
<
D
<
-\frac{184290}{10^9}
<0.
}
\tag{R495.3}
\]

Numerically,

\[
D=-0.00018429045170977335006\ldots.
\]

Therefore the proposed causal current has a negative row-14 coordinate. It is not an atom of the positive typed cone.

The review branch includes a short exact verifier and its retained result:

```text
experiments/reviews/X-PR495-volterra-causal-counterexample/verify.py
experiments/reviews/X-PR495-volterra-causal-counterexample/results/verification.json
```

The retained classification is

```text
FAIL_L91763_INFINITESIMAL_CAUSAL_GENERATOR_POSITIVITY
proof object:
e68063f61782dce2ffe7b513b04e7a852cd442db6a686f2c0f24f992427f5258
```

## Consequence for the child-capacity interface

The failure is local and precedes integration. Positive Tonelli and actual-target-mass normalization cannot repair a negative fibrewise current atom. In particular, `L-91694` can preserve a valid positive decomposition under integration, but it cannot manufacture positivity for a decomposition whose current packet has already left the cone.

A different grouped decomposition might conceivably avoid the negative atom. PR #495 does not provide one. The written atomwise causal source ledger is false.

# Complete native ledger

Everything after `L-91763.2` is conditional on the failed positive source decomposition:

```text
integrated current/child source identity      blocked
actual child target-mass coefficients <1/8   not established for this fibre family
signed observation versus positive source    formally well typed, but downstream
all-column capacity insertion                 not reached
terminal-child composition                    not reached
native Y4 deficit bound                       not reached
endpoint consumer                             not reached
```

The separation between positive source operations and signed mismatch/collar/terminal observations is conceptually correct. It does not rescue the missing positive current/child partition.

# Certificate audit

The retained `X-91760` verifier checks:

- sample Volterra antiderivatives;
- finite rank-one scalar transport;
- toy source-owner uniqueness;
- sample rough change-of-variable algebra;
- an arbitrary child coefficient list whose sum is below `1/8`;
- abstract two-ledger type labels.

It never instantiates the actual row

\[
p_s-p^{-1/2}U_pp_{s/p}.
\]

Its child fixture is supplied as already nonnegative data. Hence the retained `PASS_NATIVE_VOLTERRA_COMMON_PARENT_SOURCE_PACKET` result is a regression test for the intended formal architecture, not a certificate of the failed causal-generator theorem.

# Claim status

```text
L-91760  VERIFIED WITH PROVENANCE FIX
L-91761  VERIFIED WITH PROVENANCE FIX
L-91762  VERIFIED
L-91763  FALSE AT SECTION 2
T-92910  REJECTED AS A COMPLETE PROPOSAL
X-91760  REGRESSION ONLY AT THE BROKEN INTERFACE
RH        UNPROVEN
```

# Required successor

A repair must avoid claiming hereditary causal positivity for `p_s`. It must do one of the following:

1. prove a positive **grouped** current/child decomposition for the full rough fibre
   \[
   P_S^{\rm rough}
   =
   \sum_m m^{-1/2}U_mp_{S/m}
   \]
   without requiring each individual difference to be nonnegative; or
2. replace the causal split by another source-owned packetization and prove every component-row, ordinary, detail, score, and child-boundary coordinate directly.

The exact witness (R495.2) must be included as a mandatory fail-closed regression in any successor.

No result from PR #497 was used to obtain this verdict.
