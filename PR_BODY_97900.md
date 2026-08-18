## Purpose

Continue PR #594 at exact head
`ef76157a516c520a0f829ea4ee346c62759743ed` from the minimal root zero-hinge
criterion. The goal is to remove every owner range that can be paid by positive
complete cubes, exact top completion, classical PNT cancellation, or an
upper-bound sieve, and to expose the first genuinely centered boundary sign.

**RH remains unproved.** This successor proves two new localization theorems and
leaves two explicit root-only arithmetic statements open.

## I. Complete native cube beyond `log^2 X`

For

```text
Z=(log X)^2 loglog X,
```

the complete native rough cube satisfies

```text
U_Z(X)
 = a_* product_(67<=p<=Z)(1-1/p)+o(1/log Z)
 >0.
```

The proof does not require the primorial to fit below `X`. It splits activated
divisors at `X/(log X)^10`; a half-weight Rankin estimate pays the unactivated
tail, the unsigned constant coordinate is `X^(-1/2+o(1))`, and the asymptotic
remainder is `O((log X)^-20)`.

## II. Exact top-history completion

For `E_q=I-q^-1 T_q`, the identity

```text
E_q + q^-1 T_q = I
```

gives, exactly,

```text
U_(Z,<p)(Y)
 = sum_(S subset primes>p) 1/q_S
   U^(hat({p} union S))(Y/q_S).
```

Every nonempty top-prime set appears once, with its least prime as owner. This
is a literal squarefree source partition. The separate inverse omitted-factor
series is used only to bound state values and is not misrepresented as source
ownership.

## III. Every sufficiently high owner is lower order

With

```text
H=exp((loglog X)^4),
L=exp((loglog X)^2),
```

top completion converts the complete owner range `p>=H` into squarefree
`H`-rough products. Interior endpoints are PNT-small. On the activation
boundary, the standard upper-bound sieve gives reciprocal mass

```text
O(log L/log H)=O((loglog X)^-2).
```

Hence

```text
sum_(H<=p<=X/2) p^-1 U_(Z,<p)(X/p)
 =O((loglog X)^-2),
```

against a positive cube of order `1/loglog X`.

The unfiltered root problem is therefore confined to

```text
(log X)^2 loglog X
  < p
  < exp((loglog X)^4).
```

The exact remaining statement is `QPCB67`, a one-sided source-faithful
prime-versus-Mobius correlation on that quasipolylogarithmic corridor.

## IV. Constant-killing filtered route

Define

```text
b^Delta(Y)=b(Y)-b(Y/4).
```

Then

```text
b^Delta(Y)=(a_*/2)sqrt(Y)+O(Y^-3/2):
```

the constant asymptotic coordinate cancels exactly. The added Mellin factor is
`1-4^-s`, zero-free in `Re s>0`.

For

```text
K=(loglog X)^2,
Z=X^(1/K),
L=exp(K),
```

Rankin's method proves the complete filtered cube positive:

```text
U_Z^Delta(X)
 =(a_*/2) product_(67<=p<=Z)(1-1/p)
 +o(1/log Z)>0.
```

Exact top completion and PNT close every remaining history whose terminal
endpoint is at least `L`. At the terminal boundary all omitted primes exceed
the endpoint and are literally inactive. Thus the only surviving term is

```text
A_X^Delta
 = sum_(X/L<n<=X/2, P^-(n)>Z)
   mu(n)^2/n * U_full^Delta(X/n).
```

The positive cube and this boundary cancel to leading order. Their centered
difference is `FABP67`; its sign is the sole remaining theorem in the filtered
route.

## Replay

```bash
python3 experiments/X-97900-log-cube-boundary/verify.py \
  --output experiments/X-97900-log-cube-boundary/results/verification.json
```

Expected:

```text
PASS_X_97900_LOG_CUBE_AND_BOUNDARY_ALGEBRA
171f49bf4688d0d54ac53e00e4aaef8d916f7e625beab82ebb47137d8dd1b352
```

The replay uses exact rational arithmetic for operator identities, source
ownership, scale-filter commutation, boundary collapse, and hostile mutation
rejection. The PNT, Rankin, and upper-bound-sieve theorems are analytic and are
explicitly not represented as replayed.

## Exact boundary

```text
complete cube through (log X)^2 loglog X       PROVED POSITIVE
top-history completion                         PROVED EXACT
owners above exp((loglog X)^4)                 PROVED LOWER ORDER
QPCB67 quasipolylogarithmic corridor            OPEN / RH-BEARING
constant-killing scale filter                   PROVED EXACT
complete filtered cube through X^(1/loglog^2 X) PROVED POSITIVE
filtered interior top histories                 CLOSED BY PNT
FABP67 centered activation boundary             OPEN / RH-BEARING
Riemann Hypothesis                              UNPROVEN
```

No state-wise Hall theorem, nonzero Lorenz hinge, rowwise absolute value, or
source-blind large sieve is imported into the root conclusion.