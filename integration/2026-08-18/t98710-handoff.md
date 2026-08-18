# T98710 handoff

Base proposal: PR #613 at `f28aa51a6d6740067202611d8ebda4be2ef0a1c9`.

The successor must not attempt to repair the constant `96` in a
uniform-in-center estimate. That theorem is false by `R-98710`, and
`L-98713` proves the correct uniform exponential type is exactly `1/2`.
`R-98712` also forbids treating Weyl centering as parity-invariant.

Retain:

- fractional Euler algebra;
- Sibuya-decorated support source;
- exact Gaussian difference-kernel Gram;
- ordinary dominated cutoff exhaustion;
- fixed-center pole-growth implication.

First open theorem:

```text
PLFHE: fixed-center, phase-sensitive fractional Hermite energy.
```

Mandatory tests:

```text
Bohr twist chi(p)=-1;
p^2 fractional coefficient;
x=2 Tao atom transition;
difference versus total-log kernel;
center dependence visible in every claimed trace bound.
```

RH remains unproved.
