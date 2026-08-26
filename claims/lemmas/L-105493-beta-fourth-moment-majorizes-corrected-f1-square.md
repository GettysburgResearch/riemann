# L-105493 — A corrected normal-ordered Beta fourth moment majorizes the bounded F1 square

Claim ID: `L-105493`

Status: **PROVED EXACT SUFFICIENT REDUCTION; FOURTH-MOMENT ESTIMATE OPEN**

Created: 2026-08-26

Depends on: `L-105492`, `L-106132--L-106134`, corrected PR #719 head `426fe1c34a35d21b38a393456a7071c0902170f1`

RH status: **unproved**

Retain the corrected integrable weight \(\Omega_K\) of `L-105492`.

For each \(\theta\), put

\[
\mathscr W_{U,\theta}(t)
=
:\!S_{U,\theta}(t)^2\!:_B,
\tag{L-105493.1}
\]

where Boolean normal ordering deletes intersecting prime-label supports before
physical recombination. The exact Wick amplitude is

\[
\mathscr Q_U^\diamond(t)
=
\int_0^1(1-\theta)\mathscr W_{U,\theta}(t)\,d\theta.
\tag{L-105493.2}
\]

Cauchy in the Beta variable gives pointwise

\[
\boxed{
|\mathscr Q_U^\diamond(t)|^2
\le
\frac12\int_0^1(1-\theta)
|\mathscr W_{U,\theta}(t)|^2\,d\theta.
}
\tag{L-105493.3}
\]

Define the exact source-faithful fourth-order premise

```text
F1KFOURTH105493:
  M^(1/2) integral Omega_K(t)
    integral_0^1 (1-theta)
      | :S_(U,theta)(t)^2:_B |^2
    dtheta dt
  = M^(o(1))
```

on every frozen finite source packet. Then

\[
\boxed{
\mathrm{F1KFOURTH}_{105493}
\Longrightarrow
\mathrm{F1KASQ}_{105492}
\Longleftrightarrow
\mathrm{F1GRAM}_{105480}
\Longleftrightarrow
\mathrm{F1HCNC}_{105481}.
}
\tag{L-105493.4}
\]

Unlike the withdrawn `F1FOURTH105483`, the weight in this theorem decays like
\((1+t^2)^{-1}\), so the integral is finite for every finite packet.

## Ordinary fourth moment as a stronger optional premise

Write

\[
S_{U,\theta}(t)^2
=
\mathscr W_{U,\theta}(t)+\mathscr C_{U,\theta}(t),
\]

where \(\mathscr C\) is the shared-label contraction amplitude. If its
corrected \(\Omega_K\)-weighted square is paid by the inherited repeated-label
square ledger, then

\[
|\mathscr W_{U,\theta}|^2
\le
2|S_{U,\theta}|^4+2|\mathscr C_{U,\theta}|^2
\]

shows that the corresponding ordinary Beta-weighted fourth moment is a
stronger sufficient premise. This optional promotion is not used in the exact
definition above.

## Quarter-power coordinate

At PR #719 head

```text
426fe1c34a35d21b38a393456a7071c0902170f1
```

the corrected quarter-power theorem proves that the balanced source is empty,
but the coherent owner-dependent Type-I collapse

```text
QPTI103112
```

remains open and is equivalent to `BCI102990`.

This is compatible with (L-105493.4): the fourth-moment/Gram route is a
stronger Hilbert norm of the same bounded source, while `QPTI103112` is the
sharp one-sided physical restriction. No implication from the fixed-owner
quarter-power estimate to `F1KFOURTH105493` is asserted.
