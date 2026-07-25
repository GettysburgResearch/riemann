# NOTATION.md

Maintained by: claude-01 (bootstrap).  Amend by pull request; do not silently
change a normalisation that existing claims depend on.

## Core objects (D-0001)

| symbol | definition | notes |
|---|---|---|
| `s = sigma + i t` | complex variable | `sigma = Re s`, `t = Im s` |
| `zeta(s)` | analytic continuation of `sum_{n>=1} n^{-s}` | simple pole at `s=1`, residue `1` |
| `eta(s)` | `(s - 1) zeta(s)` | **entire**; `eta(1) = 1`. Preferred computational object |
| `xi(s)` | `(1/2) s (s-1) pi^{-s/2} Gamma(s/2) zeta(s)` = `pi^{-s/2} Gamma(s/2 + 1) eta(s)` | entire, `xi(s) = xi(1-s)`, `xi(0)=xi(1)=1/2` |
| `rho = beta + i gamma` | a nontrivial zero | |
| trivial zeros | `s = -2, -4, -6, ...` | zeros of `zeta`, not of `xi` |
| critical strip | `0 < sigma < 1` | |
| critical line | `sigma = 1/2` | |
| `Theta` | `sup { Re rho }` | RH `<=>` `Theta = 1/2` |
| `N(T)` | number of zeros with `0 < gamma <= T` | counted with multiplicity |
| `theta(t)` | `Im log Gamma(1/4 + i t/2) - (t/2) log pi` | Riemann-Siegel theta, continuous branch, `theta(0) = 0` |
| `Z(t)` | `e^{i theta(t)} zeta(1/2 + i t)` | real-valued for real `t`; `|Z(t)| = |zeta(1/2+it)|` |
| `theta(x)` (arith.) | `sum_{p <= x} log p` | **name collision** with Riemann-Siegel theta; always disambiguated in context. Arithmetic `theta` appears only in X-0003 / O-0001 |
| `gamma` (constant) | Euler-Mascheroni constant `0.5772...` | **name collision** with zero ordinates; ordinates are always subscripted `gamma_n` |
| `H_n` | `sum_{k<=n} 1/k` | |
| `sigma(n)` | sum of divisors | **name collision** with `Re s`; arithmetic `sigma` always takes an integer argument |

The three name collisions above are inherited from the literature and are not
worth renaming; every claim file must make the intended reading explicit.

## Powers, logarithms, branches (D-0002)

* `n^{-s} := exp(-s log n)` with the **real** logarithm of the positive integer
  `n`.  Single-valued; no branch choice.
* `pi^{-s/2} := exp(-(s/2) log pi)`, real `log pi`.
* `log Gamma` is the continuous branch used by Arb's `lgamma` on the ray
  `{1/4 + i t/2 : t >= 0}`, normalised by `theta(0) = 0`.
* No claim in this repository may use `log zeta` or `zeta'/zeta` without
  stating the branch or restricting to a region where the quotient is
  single-valued.  `eta'/eta` under a contour integral is fine: it is a
  meromorphic function, not a branch of a logarithm.

## Certified computation vocabulary (D-0003)

| term | meaning |
|---|---|
| **ball / enclosure** | a set (Arb `arb`/`acb`, a real interval or a complex rectangle) guaranteed to contain the true value |
| **certified** | every step is an enclosure; the stated conclusion follows from enclosures alone |
| **high precision** | many digits, *no* guarantee. Never call this certified |
| **abstain** | the routine returns "unknown" rather than a possibly wrong answer. All certified routines here abstain instead of guessing |
| **witness** | a finite object whose certified property implies RH is false |

Working precision is given in bits (Arb `ctx.prec`).  Precision is not rigour:
see rule 11 of the README.

## Claim identifiers in use

See `CLAIMS.md`.  Prefixes are as in README section 7.
