## Purpose

Republish the missing clamped-Volterra successor on the actual remote, stacked
on PR #638 at exact head
`73ee57ccc684f4062769a6d1c0456b3ef6318db2`.

**RH remains unproved.**

## Exact repair

The generic PR #638 audit correctly finds a two-dimensional nullspace and
possible derivative-jump atoms. For the actual clamped arithmetic primitive

```text
Phi(y)=4y log y+2 sqrt(y) log y-12y+12sqrt(y),
```

however,

```text
V Phi = 2sqrt(y)-1,
Phi(1)=0,
Phi'(1+)=0.
```

The two homogeneous coefficients are uniquely forced by the clamps. Every
Möbius colour `mu(n) Phi(x/n)` therefore enters with zero value and zero first
derivative. All activation-knot atoms vanish, and the two lower-boundary
Volterra modes are zero.

Hence

```text
f_mu(X)
 = integral_1^X 2(X-sqrt(Xt))/t^(3/2) L(t) dt
```

with

```text
L(t)=2sqrt(t) sum_(n<=t) mu(n)/n
     -sum_(n<=t) mu(n)/sqrt(n),
```

and no hidden atomic or homogeneous correction.

The physical parabolic endpoint packet is independently shown to obey the same
double-clamping equations.

## Replay

```bash
python3 experiments/X-99550-clamped-volterra/verify.py
sha256sum -c T99550_CONTENT_SHA256SUMS
```

Expected:

```text
PASS_T99550_CLAMPED_VOLTERRA_EQUALITY_FRAME
c1a44d3bf130a535ee4d389c1a524075c8d812ca37b5c7497916d154befff64c
```

## Scope

```text
specific activation-knot ledger       CLOSED: IDENTICALLY ZERO
specific Volterra nullspace debt       CLOSED: IDENTICALLY ZERO
generic PR #638 firewall               RETAINED
inherited compact Hall/profile work    NOT REPLAYED
terminal theorem                       NOT REPLAYED
full RH conclusion                     UNPROVED
```

This is an exact local/interface packet, not a declaration that RH has been
established.
