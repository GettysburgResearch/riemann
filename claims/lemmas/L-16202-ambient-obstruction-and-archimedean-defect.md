# L-16202 — The ambient bounded sandwich is impossible; the archimedean trace form has a different exact defect operator

Claim ID: `L-16202`  
Status: **PROVED SCOPE OBSTRUCTION AND SOURCE-LEVEL IDENTITY**  
Authoring agent: `gpt56-pro-12`  
Created: 2026-07-31  
Primary sources: Connes--Consani arXiv:2106.01715, Proposition 2.1; Connes--Consani arXiv:2006.13771, Proposition 5.5

## 1. The ambiguity that must be removed

The proposed bridge

```text
A_lambda=sigma_lambda G_lambda
         +a_lambda(I-K_lambda)+R_lambda                 (L-16202.1)
```

has two possible meanings.

1. `A_lambda` is the full self-adjoint operator associated with the localized
   Weil form on `L2([lambda^-1,lambda],d*u)`.
2. `A_lambda` is a finite compression or a transported low-dimensional source
   block.

Under the first interpretation, (L-16202.1) is impossible if `G_lambda`,
`I-K_lambda`, and `R_lambda` are bounded operators and the coefficients are
finite. Under the second interpretation it is meaningful, but the compression,
source map, Gram, constraints, and cutoff must be part of the theorem statement.

## 2. The localized Weil operator is unbounded above

Let

```text
H_lambda=L2([lambda^-1,lambda],d*u),
lambda>1.
```

Connes--Consani write the localized Weil form as

```text
QW_lambda(f)
 = integral_R |fhat(t)|^2 m_infinity(t) dt
   + bounded rank-two term
   - sum_(1<n<=lambda^2) Lambda(n)<f,V(n)f>,              (L-16202.2)
```

where

```text
m_infinity(t)=2 theta'(t)/(2pi)                           (L-16202.3)
```

and every `V(n)` is bounded. The prime sum is finite at fixed `lambda`.
Moreover

```text
m_infinity(t)->+infinity
```

logarithmically as `|t|->infinity`.

Choose a nonzero smooth logarithmic-window function `phi` supported strictly
inside `[-log lambda,log lambda]`, and put

```text
f_N(exp x)=phi(x) exp(iNx).                               (L-16202.4)
```

Its norm is independent of `N`, while its Mellin transform is a translate of
that of `phi`. Therefore

```text
integral |fhat_N(t)|^2 m_infinity(t)dt ->+infinity.       (L-16202.5)
```

All remaining terms in (L-16202.2) are uniformly bounded by a constant times
`||f_N||^2`. Hence

```text
QW_lambda(f_N)/||f_N||^2 ->+infinity.                    (L-16202.6)
```

The self-adjoint operator associated to `QW_lambda` is thus unbounded above.

## 3. Ambient obstruction

The ordinary time--frequency prolate concentration operator is a positive
contraction. Thus

```text
D_lambda=I-K_lambda
```

is bounded. If `G_lambda` and `R_lambda` are bounded and
`sigma_lambda,a_lambda` are finite, then the right side of (L-16202.1) is
bounded. It cannot equal the unbounded localized-Weil operator.

Consequently:

```text
boxed:
The requested affine-prolate identity cannot hold as a bounded-operator
identity on the full ambient localized Hilbert space.                   (L-16202.7)
```

The only coherent versions are:

- a finite Fourier compression with explicit dependence on `N`;
- a transported finite prolate-source block;
- or an equality of unbounded quadratic forms in a common graph domain, with a
  graph-relative remainder norm rather than (L-15109)'s bounded Gram norm.

## 4. Proof of unboundedness

In logarithmic coordinates the multiplicative Fourier transform is the ordinary
Fourier transform. If `Phi` denotes the transform of `phi`, then

```text
fhat_N(t)=Phi(t-N).                                       (L-16202.8)
```

After the change of variables `s=t-N`, the first term is

```text
integral |Phi(s)|^2 m_infinity(s+N)ds.                   (L-16202.9)
```

On every fixed compact set in `s`, the multiplier tends uniformly to infinity.
Choose a compact set carrying positive `|Phi|^2` mass; the integral over that
set tends to infinity. The complement is irrelevant for a lower bound because
the multiplier is lower bounded. The finite rank-two term and every finite
prime operator are bounded by Proposition 2.1, proving (L-16202.6). QED.

## 5. What the archimedean trace formula proves exactly

There is nevertheless a genuine exact affine-defect identity in the primary
literature. Connes--Consani consider the archimedean correction functional
`E_+ o Q_+` on an interval

```text
I subset [-log 2,log 2],
length(I)<=log 2.
```

Their Proposition 5.5 defines its bounded representing operator `N_I` and
proves

```text
boxed:
N_I=-2 epsilon'(1+) (Id-K_I),                            (L-16202.10)
```

where `K_I` is a specific compact Hilbert--Schmidt integral operator whose
kernel is formed from `(Q epsilon)(exp(|v|))`.

Thus the trace-form literature does supply an exact `scalar times (I-K)`
architecture. It does so for:

- one archimedean correction operator;
- a fixed small support interval;
- its own compact kernel `K_I`.

It does **not** prove (L-16202.1) for the complete semilocal Weil operator.

## 6. `K_I` is not the prolate concentration operator

The kernel in Proposition 5.5 has zero diagonal value because

```text
(Q epsilon)(1)=0;
```

the authors explicitly note that the integral of its diagonal values is zero
independently of `I`.

By contrast, the standard nontrivial time--band concentration operator has a
strictly positive constant diagonal kernel and positive trace. Therefore the
operator `K_I` in (L-16202.10) is not the standard prolate concentration
operator whose eigenvalue defects are `d_0,d_4,d_8,...`.

This prevents the substitution

```text
K_I = K_lambda                                            (L-16202.11)
```

that would otherwise make the desired theorem immediate.

The same paper approximates its trace-remainder operator using prolate-derived
finite-rank data, but that approximation is neither an identification with the
concentration operator nor an `o(d_8)` semilocal estimate.

## 7. Semilocal prime terms are load-bearing

For larger support, the full localized form contains the finite sum

```text
-sum_(1<n<=lambda^2) Lambda(n)V(n).                       (L-16202.12)
```

The 2021 paper demonstrates that the archimedean part alone loses positivity
near the first prime threshold and that the prime-2 term restores it. Thus the
prime operators cannot be discarded as a routine small remainder in any
semilocal proof.

Any successful relative theorem must retain the correlation between:

- the archimedean multiplier;
- every active prime-power operator;
- the map `E`;
- and the prolate corrector.

Taking absolute norms term by term before combining them is not expected to
preserve the superexponential `d_8` scale.

## 8. Corrected proof target

The well-typed target is the sector comparison in `L-16201`. Let `S_lambda` be
the transported constrained prolate source sector containing the `0/4` target
and the first mode-8 complement. Prove

```text
P_S A_lambda P_S
 =sigma_lambda G_S+a_lambda D_S+R_S,                     (L-16202.13)

lambda^(2tau_lambda)||R_S||_(G_S)
 /(a_lambda d_8(lambda))->0,                             (L-16202.14)
```

plus:

```text
an independent global spectral floor,
a background complement gap,
a source/background cross-block estimate.               (L-16202.15)
```

By `L-16201` and `T-15103`, these statements are sufficient for the positive RH
route. They avoid the impossible ambient bounded-operator identity and ask only
for the low spectral information that the proof actually consumes.

## 9. Proof boundary

This lemma proves a scope obstruction, not RH. It does not prove the compressed
relative estimate (L-16202.14). It shows precisely which primary trace identity
is available, why it cannot be identified with the standard prolate defect, and
why the next theorem must be sectorial or graph-form relative.
