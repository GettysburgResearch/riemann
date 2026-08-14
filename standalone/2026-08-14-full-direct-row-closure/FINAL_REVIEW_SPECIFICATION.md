# Final review specification for `T-91656`

## Freeze target

The reviewer must freeze the final PR head and read the final dependency manifest
and final lock before inspecting mathematics. Historical files `L-91668`,
`L-91669`, and `T-91655` are rejected or superseded and are not alternate
proofs.

## The theorem to reconstruct

For every sufficiently large real `X`, reconstruct a finite nonnegative row
`d_X` satisfying

\[
\Gamma(d_X;q)\le w_X(q),
\qquad
\Xi(d_X;q)\le\Omega_X(q)
\qquad(q\ge2),
\]

and

\[
\mathcal S(d_X)\ge4\sqrt X-C_1\log X-C_2.
\]

Then verify the finite dual and the frozen endpoint chain.

## Type table

| Symbol | Type | May recurse? | Physical row? |
|---|---|---:|---:|
| `L_*` on the first 54.2 cells | positive endpoint density | no | no, before realization |
| `P^Psi=3P^(4/3)` | positive labelled source measure | through stopping tree | no |
| `R_parent` | complete finite parent component row | no | yes |
| `R_child` | canonical fixed-67 child row | yes | yes |
| `d_child` | arbitrary feasible child replacement | yes | yes |
| `d_X=R_parent-R_child+d_child` | sole parent packing | no | yes |
| collar/mismatch/top/port | current ownership certificates | no | already included in `R_parent` |

## Mandatory normalization check

The historical balanced/reserve row claim is false:

\[
(1+\kappa_*)+(2-\kappa_*)=3.
\]

The only accepted root normalization is

\[
w_\Psi=3w_{4/3},
\qquad
\mathcal H_{\Psi,j}=\frac{Q_Y(j)}{4\sqrt Y-3},
\]

so

\[
w_\Psi\mathcal H_{\Psi,j}
=\frac1{\sqrt n}Q_Y(j).
\]

Any proof using the two separately normalized balanced/reserve row profiles must
be rejected.

## Exact dependency order

1. `R-91659`: reproduce the factor-three counterexample.
2. `L-91670`: verify one-copy single-SHARP target/score/row normalization and
   the exact least-prime source recursion.
3. `L-91107`, `L-91110`, `L-91111`, `L-91114`, `L-91115`: reconstruct the
   finite-window endpoint realization.
4. `L-91671.2--10`: verify the exact finite-seed/continuum-seed bridge and that
   current certificates are used once.
5. `L-91556`, `L-91560`, `L-91550`, `L-91562`: reconstruct the one-prime
   target/score/row cocycle and Hall certificate.
6. `L-91621` with `L-91670`: verify source ownership, stopped-leaf form,
   leafwise Hall, and measurable Fubini.
7. `L-91559`, `L-91663`: verify same-index arbitrary-child replacement in every
   ordinary and radix-four column.
8. `L-91666`: rerun all 402 finite cells and the analytic tail.
9. `L-91671.19--20`: verify the exact coefficient-one loss identity and the
   `X`-independent current constant.
10. `L-91557`, `L-91660`, and the frozen endpoint chain: verify the score front
    door, benchmark, finite dual, prime-square coefficient, Mellin pole, Landau
    sign, and functional equation.

## Exhaustive column partition

The proof must account for every physical integer `q>=2`:

```text
q<K                inherited inner capacity and same-index child identity
K<=q<=X/4          one safety-scaled mismatch/collar inequality
X/4<q<X            one top/terminal inequality
q>=X               triangular zero
```

No current row may be counted in two ranges.

## Exact one-row rule

The physical packing is exactly

\[
d_X=R_X^{\rm par}-R_X^{\rm ch}+d_K.
\]

The endpoint producer, quantizer, collar, mismatch, safety factor, top packet,
port, and Hall bonuses are ownership stages of `R_X^{par}`. They are not
additional summands after this formula.

## Exact loss rule

The reviewer must derive

\[
\operatorname{Loss}_X(d_X)
=
[J_X-J_K-\mathcal S(R_X^{\rm par}-R_X^{\rm ch})]
+
\operatorname{Loss}_K(d_K)
\]

before applying inequalities. The recursive coefficient must be one.

## Required computations

```text
X-91666  fixed-67 theorem
X-91670  factor-three refutation and single-SHARP normalization
frozen Hall-prefix and normalized-row certificate
frozen endpoint mismatch/collar/top certificate
final manifest/lock validator
```

A PASS result proves only its declared finite statements.

## Immediate falsifiers

```text
old balanced/reserve row normalization used;
source atom duplicated;
finite and continuum seeds misidentified;
global positivity of reciprocal-zeta equality weight assumed;
one current packet counted twice;
root-only packet copied to child;
ordinary/detail overdraw;
fixed-67 inequality failure;
current constant grows with X or leaf count;
loss coefficient differs from one;
endpoint sign or pole cancellation wrong.
```

## Status terminology

`Complete proof proposal` means every arrow is written and frozen. It does not
mean the mathematics has been independently accepted. RH remains unproved until
this reconstruction passes.
