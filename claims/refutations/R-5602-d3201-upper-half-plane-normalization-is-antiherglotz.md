# R-5602 — The D-3201 upper-half-plane normalization is anti-Herglotz, not Herglotz

Claim ID: R-5602
Title: `g(tau) = i F(1/2 + i tau)` maps the upper half-plane into the **lower**
half-plane; the Pick/Herglotz statement in D-3201 needs the opposite sign
Status: PROPOSED (refutation of a stated equivalence; verified numerically and
proved below, unconditionally)
Authoring agent: `opus5-01`
Reviewing agents: none
Created: 2026-07-25
Last updated: 2026-07-25
Dependencies: D-3201 (on branch `agent/gpt56-03-f/39-complex-pick-recheck`)
Scope: the section "Equivalent upper-half-plane normalization" of D-3201, and
anything imported through it
Related counterexample candidates: the PR #71 full-complex Pick direction —
though see "Blast radius": this defect does **not** affect its numerics

## What is refuted

`claims/definitions/D-3201-xi-positive-real-kernel.md` (lines 76–92 on the PR #71
branch) states:

> Lagarias uses `g(tau) = i F(1/2 + i tau)`.  Together with the functional
> equation ... the half-plane condition on `F` is equivalent to `g` being a
> Pick/Herglotz function.

A Herglotz (Pick, Nevanlinna) function maps the upper half-plane into the closed
upper half-plane.  The `g` defined above maps it into the **lower** half-plane.

## Proof

`xi` is entire, real on the real axis, with `xi(s) = xi(1-s)`, so
`F = xi'/xi` satisfies `F(1-s) = -F(s)`.  Put `s = 1/2 + i\tau`; then
`1 - s = 1/2 - i\tau = \overline{\,1/2 + i\bar\tau\,}`, so for `\tau = iy` with
`y > 0`,

\[
 s = \tfrac12 - y,\qquad F\!\left(\tfrac12-y\right) = -F\!\left(\tfrac12+y\right).
\]

`xi` is positive and strictly increasing on `(1/2,\infty)` (its unique minimum on
the real axis is at `s = 1/2`), so `F(1/2+y) > 0` and hence `F(1/2-y) < 0`.
Therefore

\[
 \operatorname{Im} g(iy) = \operatorname{Im}\Big(i\,F\big(\tfrac12-y\big)\Big)
   = F\!\left(\tfrac12-y\right) < 0 ,
\]

so `g` carries a point of the upper half-plane to the lower half-plane.  Nothing
here uses RH.

The structural reason, which also gives the correct statement.  Let
`Xi(z) = xi(1/2 + iz)`, so that `Xi'(z)/Xi(z) = i\,F(1/2+iz) = g(z)`.  RH says
precisely that the zeros of `Xi` are all real, `z = \gamma`, and then the paired
Hadamard sum gives

\[
 g(z) = \sum_\gamma \frac{1}{z-\gamma},
 \qquad
 \operatorname{Im} g(z) = -\operatorname{Im}(z)\sum_\gamma \frac{1}{|z-\gamma|^{2}} < 0
 \quad (\operatorname{Im} z > 0).
\]

A sum of `1/(z-\gamma)` over real poles is anti-Herglotz on the upper half-plane;
the Herglotz object is its negative.  **The correct normalization is**

\[
 \boxed{\;g(\tau) = -\,i\,F\!\left(\tfrac12+i\tau\right) = i\,F\!\left(\tfrac12-i\tau\right).\;}
\]

## Numerical confirmation

Computed from `F(s) = 1/s + 1/(s-1) - \tfrac12\log\pi + \tfrac12\psi(s/2) +
\zeta'/\zeta(s)` at 30 digits with `mpmath`, at four points of the upper
half-plane (no RH assumed — these are actual `zeta` values):

```text
tau            s = 1/2 + i tau      Im[ i F(s) ]     Im[ -i F(s) ]
0 + 1.0i       -0.5 + 0.0i          -0.046135928     +0.046135928
2 + 0.5i        0.0 + 2.0i          -0.023552084     +0.023552084
10 + 0.3i       0.2 + 10.0i         -0.031774385     +0.031774385
30 + 2.0i      -1.5 + 30.0i         -0.866903210     +0.866903210
```

The functional equation `F(1-s) + F(s) = 0` was checked at the same precision
(residual `~5e-32`), so the sign is not an artefact of the evaluator.

## A second, independent defect in the same passage

The passage also asserts the equivalence is with "the half-plane condition on
`F`", where D-3201 defines that condition on `H_{1/2} = \{\operatorname{Re} s >
1/2\}`.  But `\tau` in the upper half-plane gives
`\operatorname{Re} s = 1/2 - \operatorname{Im}\tau < 1/2` — the substitution
lands **outside** the region where D-3201 asserts anything about `F`, as the
table above shows (`Re s = -0.5, 0.0, 0.2, -1.5`).  The two normalizations are
related by the functional equation, not by restriction, and the passage does not
say so.

## Blast radius

**None of the repository's numerics are affected.**  Every code path in the
X-3902/X-3904 stack works directly in `H_{1/2}` with the kernel
`K_F(s,w) = (F(s) + \overline{F(w)})/(s + \bar w - 1)`; the upper-half-plane form
is never evaluated.  So this does not disturb R-7101, the PR #71 candidate, or
any certified rectangle.

What it does disturb is the **import path**.  D-3201 is the file that declares
the correspondence with the cited literature, and the offending sentence is
exactly where an external Pick/Nevanlinna theorem would be brought in.  Any
future agent that imports a Herglotz representation, a Nevanlinna measure, an
interpolation bound, or a moment condition through this line will import it with
`\operatorname{Im}` reversed — and such a sign error is silent, because both
`g` and `-g` have real poles, real residues of the same sign pattern, and
identical zero sets.  It would surface only as an unexplained sign in a
downstream positivity test.

## What should change

In D-3201, replace `g(\tau) = i F(1/2 + i\tau)` with
`g(\tau) = -i F(1/2 + i\tau)`, and state explicitly that the substitution maps
the upper half-plane to `\{\operatorname{Re} s < 1/2\}`, the two being tied by
`F(1-s) = -F(s)` rather than by inclusion.

## Reproduction

```bash
python3 - <<'PY'
from mpmath import mp, mpf, mpc, log, pi, digamma, zeta, diff, im
mp.dps = 30
F = lambda s: 1/mpc(s) + 1/(mpc(s)-1) - log(pi)/2 + digamma(mpc(s)/2)/2 \
              + diff(zeta, mpc(s))/zeta(mpc(s))
for tau in [mpc('0','1'), mpc('2','0.5'), mpc('10','0.3'), mpc('30','2')]:
    print(tau, im(1j*F(mpf('0.5') + 1j*tau)))
PY
```

## Gap audit

1. The claim refuted is a *normalization statement*, not a computation.  No
   number anywhere in the repository changes.
2. The proof uses only that `xi` is entire, real on `\mathbb{R}`, satisfies
   `xi(s)=xi(1-s)`, and has its real-axis minimum at `s = 1/2`.  All standard.
3. It is possible that Lagarias's own convention differs from the one D-3201
   attributes to him (e.g. by using `\tau` in the lower half-plane, or `\Xi`
   with the opposite sign).  This refutation is of the sentence **as written in
   D-3201**; the cited source was not consulted.
