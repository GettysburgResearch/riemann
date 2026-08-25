# Genus-two inverse-designed integral-split filter

## Read this first

This packet asks a deliberately narrow question:

> Can a small exact linear combination of low-frequency, ambient-Haar-zero
> Frobenius interferometers learn the integral `+q` elliptic-form split locus
> at `q=3,5` and keep the same direction on an untouched `q=7` family?

The bounded answer is **no for the prescribed maximin design**.  The unique
training optimum is

\[
F_*=2I_{1,7}+4I_{1,9}-I_{2,4}+I_{2,8},
\qquad
I_{r,s}=\operatorname{Tr}(U^r)\operatorname{Tr}(U^s)
             -\operatorname{Tr}(U^{r+s}).
\]

Its split-minus-complement conditional mean is positive at both training
fields and negative at the held-out field:

| field role | `q` | split-minus-complement mean | squared point-biserial correlation |
|---|---:|---:|---:|
| training | 3 | `19588/3645` | `23980609/412784100` |
| training | 5 | `259254992/52728125` | `1050205482451876/18533359280570751` |
| held out | 7 | `-255883667/122859170` | `196429353112100667/22169754251970484480` |

Thus the learned direction reverses on `q=7`.  This is a useful negative
result: a fairly strong, exactly normalized two-field contrast did not
transport even one step along the available prime ladder.

Start with `GENUS2_INVERSE_DESIGNED_SPLIT_FILTER.md`, inspect
`genus2_inverse_designed_split_filter.json` for every exact conditional
moment/sign/tail table, then read
`genus2_inverse_designed_split_filter.py` for the source locks, design/holdout
separation, and root-free adapter.  Independent checks are in
`test_genus2_inverse_designed_split_filter.py`.

## 1. No new arithmetic enumeration

The sole arithmetic input is the already frozen, member-complete joint
`(a_D,b_D)` histogram for monic squarefree quintics at `q=3,5,7` in
`balanced_control_family_scan.json`.  Its 32, 81, and 138 signed atoms carry
162, 2,500, and 14,406 members respectively.  The replay reads those 251
atoms once.  It enumerates no field, polynomial, curve, root, or member.

Four primitive dependencies are locked by LF-normalized SHA-256 before JSON
parsing or dynamic module loading:

- the complete histogram fixture;
- its producer;
- the exact Frobenius-interferometer engine; and
- the exact integral `+q` elliptic-form split predicate.

The histogram's canonical payload hash and per-field member-ledger hashes are
also checked.  A self-consistent substituted fixture is therefore refused.

## 2. The complete low-frequency design space

The normalized reciprocal quartic is

\[
Z^4-e_1Z^3+e_2Z^2-e_1Z+1.
\]

The packet exhausts every raw `I_(r,s)` satisfying

\[
1\le r\le s,\qquad r+s\le10,\qquad r+s\equiv0\pmod2,
\]

and retains exactly those with zero ambient `USp(4)` Haar mean.  Even parity
is required so the finite-field adapter is rational in

\[
A=e_1^2=a_D^2/q,\qquad e=e_2=b_D/q.
\]

The resulting pool is complete under those declared conditions:

| pool coordinate | exact seven-context signature |
|---|---|
| `I_(1,7)` | `(0,0,0,0,0,0,0)` |
| `I_(1,9)` | `(0,0,0,0,0,0,0)` |
| `I_(2,4)` | `(0,-2,-4,-2,0,0,0)` |
| `I_(2,8)` | `(0,0,0,-1,0,0,0)` |

The contexts, in order, are ambient `USp(4)`, block `SU(2)xSU(2)`, doubled
standard `SU(2)`, `Sym^3 SU(2)`, and the three corresponding uniform-torus
checks.  A zero signature means zero constant-term projection in those exact
contexts; it is not pointwise vanishing.

The candidate lattice consists of primitive integer coefficient vectors in
this pool, modulo overall sign by requiring the first nonzero coefficient to
be positive, with

\[
\lVert c\rVert_1\le8.
\]

There are exactly **1,640** candidates, below the fail-closed cap of 4,096.
No candidate list or cap was changed after examining `q=7`.

## 3. Exact training objective and genuine holdout

For a detector `F` in field `q`, let `Y` be the indicator of the integral
split coefficient locus, let `pi_q=E[Y]`, and put

\[
\Delta_q(F)=E[F\mid Y=1]-E[F\mid Y=0].
\]

The exact scale-free score is the squared point-biserial correlation

\[
\rho_q(F)^2
=\frac{\pi_q(1-\pi_q)\Delta_q(F)^2}{\operatorname{Var}_q(F)}.
\]

Only candidates with nonzero, agreeing signs for `Delta_3` and `Delta_5`
are eligible.  Among them the deterministic objective lexicographically
maximizes

\[
\left(
\min(\rho_3^2,\rho_5^2),
\rho_3^2+\rho_5^2
\right),
\]

then uses lower `L1`, support, maximum coefficient, and fixed lexicographic
ties.  Exactly 849 directions are training-eligible and 791 are rejected for
opposite or zero training directions.  The winning objective has one witness.

The implementation-level holdout firewall is stronger than a prose promise:
`design_on_q3_q5_only` refuses any summary mapping whose keys are not exactly
`(3,5)`.  Only after it returns the frozen coefficient vector does
`_post_design_audit` consult `q=7`.

## 4. Held-out failure is widespread in this lattice

Of the 849 training-eligible directions:

- 80 retain their training direction at `q=7`;
- 769 reverse or vanish at `q=7`.

The winner is in the second class.  This does **not** prove that no detector
can recognize a split locus, nor even that no member of this lattice has a
stable direction.  It proves that the declared two-field maximin inverse
design does not generalize to the one exact held-out field.

For scale, a retrospective audit asks which of the 80 survivors had the best
original training objective.  It is

\[
2I_{1,7}+3I_{1,9}-2I_{2,4}-I_{2,8}.
\]

Its held-out squared correlation is

\[
\frac{6468033126390889}{41692284297035565120}<\frac1{6000}.
\]

That direction uses the held-out label to enter the retrospective survivor
set and is explicitly **not** promoted as a replacement detector.

## 5. The old selectors are an important control

The exact comparison with the existing selectors is not uniformly flattering
to inverse design:

| detector | `Delta_3` | `Delta_5` | `Delta_7` | direction at `q=7` |
|---|---:|---:|---:|---|
| `P` | `2416/729` | `15859984/10545625` | `3845512/1755131` | survives |
| `D` | `-9032/3645` | `-13691824/10545625` | `-44130197/26326965` | survives |
| `S` | `-11968/10935` | `-167964576/52728125` | `23919580/12285917` | reverses |
| `F_*` | `19588/3645` | `259254992/52728125` | `-255883667/122859170` | reverses |

`P` and `D` transport their conditional-mean direction through all three
fields, although their training maximin score is lower than `F_*`'s.  `S`
fails in the same qualitative way as the learned winner.  Three fields are
far too few to promote the `P` or `D` pattern to an all-`q` conjecture, but
the control shows why maximizing a small training panel is not itself a
robust detector-design principle.

## 6. Exact compact projection of the winner

The winner's seven-context signature is

\[
(0,2,4,1,0,0,0).
\]

In the existing selector signature basis,

\[
F_*=P+2D+\frac12S+R_{\rm null},
\]

where the exact raw residual is

\[
\begin{aligned}
R_{\rm null}={}&2I_{1,1}-I_{2,2}-4I_{1,5}-I_{4,4}
 +2I_{1,7}+4I_{1,9}\\
&{}-I_{2,4}+2I_{2,8},
\end{aligned}
\]

and its signature is exactly zero in all seven locked contexts.  This is an
exact decomposition modulo those Haar constant-term functionals.  It is not
an equality asserting that the residual vanishes pointwise.

This decomposition offers a mechanism-level reading of the failed
generalization: the training optimum mixed the known product, doubled, and
`Sym^3` subgroup-sensitive projections with a large signature-null residual.
The finite arithmetic response of that residual is unconstrained by its
compact constant terms.

## 7. Root-free reciprocal-quartic adapter

No Frobenius angles or numerical roots are constructed.  If `p_n=Tr(U^n)`,
the order-four recurrence is

\[
p_n=e_1p_{n-1}-e_2p_{n-2}+e_1p_{n-3}-p_{n-4}.
\]

Parity permits the exact representation

\[
p_n=e_1^{n\bmod2}Q_n(A,e),
\]

so every pool coordinate, and hence `F_*`, is a polynomial in `A,e`.  The
expanded winner adapter is

\[
\begin{aligned}
F_*={}&4A^4e-6A^4-31A^3e^2+74A^3e-37A^3\\
&+74A^2e^3-208A^2e^2+116A^2e+32A^2\\
&-55Ae^4+134Ae^3+42Ae^2-204Ae+34A\\
&+6e^5-4e^4-32e^3+16e^2+40e-8.
\end{aligned}
\]

The producer constructs this polynomial from the recurrence, checks its
coefficient dictionary against a frozen sentinel, and evaluates it against
the raw linear combination on every one of the 251 source atoms.

## 8. Conditional means, covariances, signs, and tails

The JSON retains, for each of `q=3,5,7` and each of `F_*,P,D,S`:

- exact unconditional and split/complement conditional means and variances;
- covariance with the split indicator and squared point-biserial correlation;
- negative/zero/positive member counts overall and within each class; and
- a tied outer absolute one-percent tail with its exact split enrichment.

It also retains the full `4 x 4` covariance matrix of `(F_*,P,D,S)` under
the all-member, split-conditional, and complement-conditional measures.

Two tail facts help prevent an overly simple reading.  At `q=3` and `q=5`,
the extreme absolute tail of `F_*` contains no split member even though its
split conditional mean exceeds its complement mean.  At held-out `q=7`, 42
of 210 tied-tail members are split, giving split enrichment `343/425`, below
one.  Mean separation and extreme-tail enrichment are therefore distinct
diagnostics in this packet.

## 9. What is and is not established

Established exactly:

1. completeness of the declared low-frequency even ambient-zero raw pool;
2. completeness of the 1,640-candidate primitive lattice under `L1<=8`;
3. the unique q=3,5 maximin winner and all exact training scores;
4. the untouched q=7 direction reversal;
5. the 80/769 held-out direction-survival ledger;
6. the winner's compact signatures, selector-basis decomposition, and
   root-free polynomial adapter; and
7. every reported finite conditional moment, covariance, sign, and tail law.

Not established:

- an all-`q` trend or a limiting detector law;
- that the integral coefficient factorization is a polarized Jacobian split;
- that any large detector value diagnoses a compact subgroup, endomorphism,
  correspondence, motive, or monodromy group;
- a function-field zero theorem; or
- any RH or GRH consequence.

The clean next mathematical target is not another wider coefficient search.
It is an all-`q` moment calculation for the low-frequency raw pool, separated
by the integral split predicate if that conditioning can be made geometric.
Without that structure, adding more training fields risks producing a more
elaborate interpolant rather than a transportable detector.

## 10. Replay

The committed payload hash is

`d3fb13ea244790bfcdf65a65b94397117f8c931ca6ecdd0c13fd8eb4896a2dda`.

From the repository root:

```text
python research/l-families/atlas/function_field/genus2_inverse_designed_split_filter.py --check
python -O research/l-families/atlas/function_field/genus2_inverse_designed_split_filter.py --check
python -m unittest tests.test_genus2_inverse_designed_split_filter
python -O -m unittest tests.test_genus2_inverse_designed_split_filter
```

The producer refuses source drift, more than 4,096 source atoms or
candidates, the locked 50,000-contraction ceiling, malformed mass ledgers,
nonintegral compact signatures, an altered design winner, and any floating
value in the claim payload.
