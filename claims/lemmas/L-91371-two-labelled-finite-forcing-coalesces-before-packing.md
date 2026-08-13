# L-91371 — The two finite-forcing labels coalesce before physical packing

Status: **proved exact packet-algebra reduction; RH unproved**

Let `F_2(X)` and `F_1(X)` be the complete `P_61` finite-forcing packets for the two paired source labels. Their scalar source atoms are

\[
w_a(X,n)=\frac{a\sqrt X}{n}-\frac1{\sqrt n}.
\]

The RH-sensitive target and declared score are the two different positive observations

\[
\boxed{W_\Psi=w_2+2w_1}
\]

and

\[
\boxed{W_S=2w_2+w_1}.
\]

Thus the current finite block is naturally one **two-labelled packet**

\[
\mathbf F_{61}(X)=(F_2(X),F_1(X)),
\]

with target row `(1,2)` and score row `(2,1)`. It is not necessary, and in general is not correct, to assign one complete physical row independently to each label.

The exact component-row observation of this joint packet is

\[
\boxed{
D_{P,X}(j)=
\sum_{d\mid P_{61}}
\frac{\mu(d)}{\sqrt d}Q_{X/d}(j),
}
\]

by the retained finite row identity `L-91112.26`; its ordinary and radix-four capacities and literal entropy are exactly those of `L-91363`.

Apply the source-disjoint stopping-line identity `L-91362` separately to the two labels and then add the current pieces before any physical observation:

\[
(F_2,F_1)
=(F_2^{\rm fin},F_1^{\rm fin})
 +\sum_b(P_{2,b},P_{1,b}).
\]

The finite direct sum is packed once through `D_(P,X)`. Every rough child keeps its original label and is passed by the same-index functor `L-91361`. Source disjointness and packet mass additivity are unchanged.

Consequently the producer hypothesis in `T-91307` may be weakened from

```text
one CFFP realization for each label separately
```

to

```text
one joint CFFP realization for the complete two-labelled current block.
```

If

1. `D_(P,X)>=0` coefficientwise;
2. its exact ordinary/detail capacities are used;
3. its literal entropy is at least the joint declared score minus a uniform constant;

then the joint finite block satisfies CFFP. No labelwise duplication, scalar hazard normalization, or affine row lift occurs.

```text
joint target/score dictionary             EXACT
finite labels summed before packing       EXACT
rough children remain labelled            EXACT
joint CFFP suffices for packet reset       EXACT
canonical-row sign                        L-91364
literal entropy comparison                 PR #437 / dependency lock required
root endpoint criterion                    INDEPENDENT REVIEW REQUIRED
Riemann Hypothesis                         UNPROVEN
```
