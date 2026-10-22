# X-91672 — stopped-leaf Hall-prefix counterexample for PR #455

Frozen proposal head:

```text
1b502acbe511776178da3dc916e3cd3464cd5e77
```

Normative content commit:

```text
c696d2a356eeacb3097d4ea6cc727b84548d7a03
```

The replay uses exact `Fraction` arithmetic and outward rational enclosures of
square roots and logarithms.

## Main check

Take the stopped one-prime leaf

```text
p = 67
y = 13
X = p y = 871
t = 13
```

For the survival target of `L-91562`, put

\[
r=67^{-1/2},\qquad
\alpha_s=\frac{2(r+2)}{r+3}.
\]

The no-upward Hall prefix, before its positive branch prefactor, is

\[
\mathcal H_{s,13}(871)
=\alpha_s\sqrt{871}\sum_{n\le13}\frac{\mu(n)}n
 -\sum_{n\le13}\frac{\mu(n)}{\sqrt n}.
\]

The checker proves

\[
\boxed{\mathcal H_{s,13}(871)<-2.}
\]

It also proves a conservative bound showing the same failure for every prime
\(p\ge67\) at \(y=13\). Therefore no target-Hall transport supported on
`e<=o` exists on this admissible stopped-leaf family.

## Secondary check

`L-91670` promotes the finite-window bound `M_1>1/20` from `L-91322`
to all activation cells. At

```text
N = 71
j = 70
Y = 72
```

the checker proves

\[
0<M_1<\frac1{20}.
\]

This disproves the promoted numerical margin. It does not by itself disprove
global monotonicity of the normalized row profile.

## Replay

```bash
python3 experiments/X-91672-stopped-leaf-hall-prefix-counterexample/verify.py \
  --json experiments/X-91672-stopped-leaf-hall-prefix-counterexample/results/verification.json
```

Expected output:

```text
PASS_PR455_STOPPED_LEAF_HALL_PREFIX_COUNTEREXAMPLE
d010a2ec2e1efa95efa98c237958a25166ae486381c6ace5d633d5f2016bace1
```

## Scope

The replay does not refute

\[
w_\Psi=3w_{4/3},\qquad
w_\Psi\frac{Q_Y}{4\sqrt Y-3}=Q_Y.
\]

It refutes the load-bearing claim that the frozen finite-window Hall producer
can be applied to every stopped one-prime parent packet in the final conclusion
chain.
