# Compressed-delay repair and completed-source firewall — 2026-08-12

## Freeze

```text
review cutoff UTC: 2026-08-12T13:49:47Z
repository:        gfreund123/riemann
main:              b837c12199dd407116f604ce6c938039d1a76da4
parent PR:         #400
parent live head:  7dc9fec9eb5fab4ee9340ddbc5a52e36a6ab617e
continuation PR:   #404
continuation pre-session head:
                   3b0df831df7e1dbb4fce209fe1d55973b25e0459
RH status:         unproved
```

The parent branch moved during the continuation. Its two new files,
`L-91316` and `R-91011`, were merged forward into the continuation at merge
commit

```text
8c2fdc92df2df03000b7043eb195df09563f2730.
```

## I. Exact delay correction

The old statement

```text
raw positive delay preserves K_(Theta_a)
```

is false in general. The corrected conservative object is explicit. With

```text
P=projection onto K_Theta,
Q=I-P=M_Theta M_Theta*,
S_tau=positive Hardy delay,
```

put

```text
T_tau=P S_tau|_(K_Theta),
R_tau=M_Theta* S_tau|_(K_Theta).
```

Then

```text
S_tau g=T_tau g+M_Theta R_tau g,
T_tau* T_tau+R_tau* R_tau=I,
T_(tau+sigma)=T_tau T_sigma,
R_(tau+sigma)=R_tau T_sigma+S_tau R_sigma.
```

For arbitrary mixed delays,

```text
<S_tau_i g_i,S_tau_j g_j>
 =<T_tau_i g_i,T_tau_j g_j>
  +<R_tau_i g_i,R_tau_j g_j>.
```

Thus all cross-delay terms are retained exactly by one resident compressed
semigroup plus one positive Julia leakage. This is `L-91401`.

The same orthogonal decomposition places the two Hardy components of the
finite bridge into resident model-space and leakage coordinates. It does not
supply their arithmetic source norm.

## II. Exact completed-source correction

The completed Fisher characteristic function is

```text
varphi_a(t)
 =xi(1/2+a-it)/xi(1/2+a)
 =Xi_(1/2+a)(t).
```

Nakamura's published Theorem 1.4 proves that `Xi_sigma` is quasi-infinitely
divisible but not infinitely divisible for every `sigma>1`. Hence for every
unconditional Suzuki-safe scale `a>1/2`, the completed Fisher law is not a
positive Poisson/Levy law.

This does not weaken the positive Fisher Hilbert realization. It blocks the
shortcut

```text
ordinary-prime Poisson source
 = completed Fisher source.
```

The ordinary Euler zeta ratio remains compound Poisson with positive atomic
Levy measure. The completion to xi requires a genuine renormalized
Julia/Wick/Green map, not a relabeling of the same Levy first chaos. This is
`R-91402` and the accompanying primary-source lock.

## III. Corrected architecture

The exact resident chain is now

```text
ordinary-prime compound-Poisson score
 -> explicit tail-Hankel Julia dilation at a=4;

gamma/pole multiplier
 -> moving-unitary covariant connection;

completed xi probability law
 -> positive Fisher score source;

Fisher score
 -> completed model-space tangent through A_a and C_a;

raw physical delay
 -> compressed model-space delay T_tau
  + explicit Julia leakage R_tau.
```

These are compatible output constructions, but not yet one source-ordered
isometry.

## IV. Correct remaining theorem

Construct explicitly

```text
W_a:
 prime Poisson/Julia first chaos
 + gamma/pole/theta completion
 -> completed Fisher-Hankel source
  + positive renormalization environment
```

such that:

```text
visible output = A_a;
prime visible block = H_(beta_a);
gamma/pole visible block = covariant connection;
delays intertwine through (T_tau,R_tau);
two orientations and bridge are retained;
source-minus-output defect = corrected delayed zeta screw/Weil Gram
with coefficient one.
```

This is the actual remaining source theorem. The final screw-defect identity
cannot be posed until this renormalized common-source map is constructed.

## V. Replay

The finite replay now additionally verifies a unilateral-shift model of the
compressed-delay colligation:

```text
decomposition error       0
compressed semigroup error 0
leakage cocycle error      0
mixed-delay packet error   0
raw delayed resident norm  0
raw delayed leakage norm   1
```

Retained verdict:

```text
PASS_COVARIANT_TAIL_HANKEL_COMPLETION
```

The replay is finite algebra only.

## Exact boundary

```text
prime score first-chaos measure                         EXACT
prime tail-Hankel Julia dilation at a=4                 EXACT
gamma/pole covariant connection                         EXACT
completed Fisher/model-space factorization              EXACT
raw delay invariance of K_Theta                          REFUTED
compressed delay + Julia leakage                        EXACT
all mixed-delay cross terms                             EXACT
completed xi law = positive Poisson law                 REFUTED
renormalized Poisson/Julia -> Fisher-Hankel map          OPEN
bridge arithmetic source normalization                  OPEN
renormalized defect = delayed screw/Weil Gram            OPEN / RH-BEARING
Riemann Hypothesis                                       UNPROVED
```
