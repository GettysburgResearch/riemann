# M-26201 — Green–dipole Skorokhod full RH proposal

Methodology ID: `M-26201`  
Title: Recombine the canonical Green equality and its signed constraint dipoles before taking parts, then prove a strict contact-cell descent  
Status: **FULL PROPOSAL — GREEN–DIPOLE SHARPNESS PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Issue: #260  
Imported live inputs: PR #240 at `fbc1dc1c75cdc8df01145c28a605f45415b5f5a6`, PR #248 at `5f2b25f89afbb90a3bc4ca6d40148f530303eb54`, and the signed-dipole/review stacks #254/#257 at their frozen heads  
Scope: elementary finite carry route; RH is not claimed proved

## 1. Strategic change

The carry programme previously exposed several equivalent open statements:

```text
Carry Sandwich,
Greedy Slack,
Discrete Carry-Resolvent Stability,
positive four-band renewal,
signed constraint-dipole transport.
```

The latest review identifies one missing operation common to all of them:
positive and negative errors were still being charged by different estimates.

This proposal starts from the exact endpoint-projected Green state, which solves
all prime-power constraints simultaneously, and imposes physical nonnegativity
only afterward. The negative excursion is decomposed into signed interval
dipoles. Every dipole endpoint is recombined with every sibling endpoint before
a positive or negative constraint part is taken.

The proposed proof is therefore not

```text
bound positive defect + bound negative slack.
```

It is

```text
solve the signed problem exactly
-> project once onto the physical obstacle
-> transport the net signed contact measure
-> charge only the surviving contact debt.
```

## 1.1 Relationship to the newest signed Green–balayage barrier

The newest PR #240 continuation supplies two exact operations which are imported
rather than duplicated:

1. `L-23820` removes the complete Green-orthogonal residual at zero logarithmic
   objective cost, leaving one scalar mode;
2. `L-23821` replaces an arbitrarily high-rank signed residual inside one
   logarithmic prime cell by two aggregate endpoint moments at zero objective
   cost.

Its open theorem `SGQB(K)` asks for a source-bound lower-scale recurrence for the
remaining aggregate boundary residual.

The present proposal gives a physical positive-cone realization of that
boundary residual. Starting from the same exact Green state, the layer-cake
decomposition of its negative excursion emits the concrete endpoint charges
which `SGQB(K)` otherwise denotes abstractly by `Gamma_(K,X)`.

Thus:

```text
PR #240:
    exact orthogonal purge + exact two-moment cell balayage;

this proposal:
    exact positive-cone obstacle + signed contact debt + explicit descent tree.
```

A successful `CCD` certificate is an explicit `SGQB` certificate with every
boundary contact and physical nonnegativity constraint declared. Conversely,
a reviewed `SGQB` identity may be used to prove the local cell inequality
(M-26201.3).

## 2. Canonical finite construction

For every `X`:

1. form the parabolic seed
   \[
   b_m^{(0)}
   =
   2\sqrt m\left[
    \log(X/m)-2(1-\sqrt{m/X})
   \right];
   \]
2. build the endpoint-projected divisor Gram `G_X`;
3. solve
   \[
   G_XT_X=v(b^{(0)})-w_X;
   \]
4. construct the exact equality state
   \[
   b_X^\star(m)
   =
   b_m^{(0)}+F_X(m-1)-F_X(m);
   \]
5. clip only once,
   \[
   b_X^\circ=(b_X^\star)_+;
   \]
6. compute the fully recombined signed residual
   \[
   \varepsilon_X(q)
   =
   v_q(b_X^\circ)-w_X(q);
   \]
7. output
   \[
   \mathcal L_X^{\rm GS}
   =
   J_X(b_X^\circ)
   -
   \sum_q\Lambda(q)(\varepsilon_X(q))_+.
   \]

`L-26202` proves exactly

\[
\mathcal L_X^{\rm GS}\le\mathcal P(X)
\]

and

\[
\mathcal P(X)-\mathcal L_X^{\rm GS}
=
\sum_q\Lambda(q)(-\varepsilon_X(q))_+.
\]

There is no hidden optimizer and no omitted prime-power row.

## 3. The load-bearing finite theorem

The proposed **Green–Dipole Sharpness theorem** is

\[
\boxed{
\mathcal L_X^{\rm GS}
\ge
J_X(b_X^{(0)})-C\log^A(2X)
\qquad(X\ge2)
}
\tag{M-26201.1}
\]

for absolute constants `A,C`.

The subpower version is sufficient. The strongest finite form suggested by
reconnaissance is

\[
\boxed{
\mathcal L_X^{\rm GS}\ge J_X(b_X^{(0)}).
}
\tag{M-26201.2}
\]

The proposal does not promote (M-26201.2) from computation.

By `T-26201`, (M-26201.1) gives the critical prime-ramp lower bound and RH.

Unlike the old Carry Sandwich statement, (M-26201.1) names one canonical finite
certificate and one scalar comparison. A reviewer can reconstruct it at any
endpoint without selecting a packing or cover.

## 4. Exact contact geometry

Let

\[
a_X=(-b_X^\star)_+.
\]

Its layer-cake decomposition is

\[
a_X(m)
=
\sum_\alpha
t_\alpha\mathbf1_{A_\alpha<m\le B_\alpha}.
\]

Each block is the exact signed incidence dipole

\[
\Delta_\alpha v_q
=
t_\alpha
\left(
 \mathbf1_{q\mid B_\alpha}
 -\mathbf1_{q\mid A_\alpha}
\right).
\]

Thus the complete residual is a finite signed endpoint measure.

The objective change of the block is

\[
t_\alpha\log(B_\alpha/A_\alpha).
\]

The positive endpoint mass and negative endpoint slack of all blocks are summed
first. Only the net residual is split in `D_X^+` and `D_X^-`.

This is the finite counterpart of the macroscopic constraint dipole found in
`L-25301`.

## 5. Cellwise Möbius–Poisson state

Let

\[
s_m=b_X^\star(m)-b_X^{(0)}(m),
\qquad
\gamma_m=s_m-s_{m+1}.
\]

The all-integer constraint change

\[
h(q)=v_q(b_X^\star)-v_q(b_X^{(0)})
\]

satisfies

\[
\gamma_m
=
\sum_{k\le X/m}\mu(k)h(mk).
\]

On

\[
X/(R+1)<m\le X/R,
\]

only `mu(1),...,mu(R)` occur.

The proposed proof never takes total variation before these complete cells are
joined. Boundary values shared by the `R`-th and `(R+1)`-st cells are carried
as one symbol.

## 6. Contact-cell descent

The proof-facing refinement of (M-26201.1) is the following finite certificate.

> **Contact-Cell Descent `CCD(X)`.**
> The layer-cake dipoles can be grouped into signed quotient-cell packets such
> that:
>
> 1. every internal endpoint cancels with its sibling before a positive part;
> 2. every same-scale prime-power endpoint cluster is solved jointly by the
>    nonnegative path/exceptional M-matrix inverses of `L-25301`;
> 3. every surviving child endpoint is at most `(Y+1)/2` when its parent scale
>    is `Y`;
> 4. the complete contact potential satisfies
>    \[
>    \mathfrak C_X
>    \le
>    C\log^A(2X)
>    +
>    \sum_\beta \omega_\beta
>       (\mathfrak C_{Y_\beta})_+,
>    \]
>    with
>    \[
>    Y_\beta\le(X+1)/2,
>    \qquad
>    \sum_\beta\omega_\beta\le1;
>    \]
> 5. every endpoint and floor-transition term is included in the same ledger.

The nonexpansive charge condition and factor-two descent imply, by induction,

\[
(\mathfrak C_X)_+\ll\log^{A+1}(2X).
\]

Hence `CCD` proves `GDS`.

The weights `omega_beta` are not abstract analytic constants. A production
certificate records the exact rational charge inherited by every child packet.

## 7. Why the descent is plausible

The live repository already supplies the pieces separately.

### 7.1 Same-scale clusters are finite and positive

A prime-power endpoint can have same-scale children only through consecutive
prime powers. Above the exceptional cluster `{2,3,4,5}`, every cluster has
length at most three. Its path M-matrix inverse is entrywise nonnegative; the
exceptional inverse is explicitly nonnegative.

### 7.2 All other children descend by one half

After the joint cluster solve, every remaining positive child is a prime-power
divisor of `q-1` or `q+1` and is at most `(q+1)/2`.

### 7.3 The Green state has already paid the signed scalar mode

The full Green energy cannot be bounded without controlling the RH scalar. The
proposal does not bound it. It retains the exact signed Green equality and
adds only the obstacle debt. The scalar contribution and the obstacle response
appear together in

\[
\mathfrak C_X
=
\lambda^{\!T}r_X+D_X^-.
\]

### 7.4 Incidence dipoles have exact logarithmic costs

For a contact interval `(A,B]`, the constraint vector and objective cost are

\[
\mathbf1_{q\mid B}-\mathbf1_{q\mid A},
\qquad
\log(B/A).
\]

No generic operator norm or continuum discretization is needed.

## 8. Concrete local inequality to prove

One review-efficient form of the cell step is as follows.

For one recombined quotient cell `C_R`, let

\[
\Gamma_R(m)
=
\sum_{k\le R}\mu(k)h_R(mk)
\]

be its exact Möbius charge, and let `a_R` be the obstacle excursion generated by
its Poisson tail.

The local theorem should prove

\[
\boxed{
\sum_{q}\Lambda(q)
 \left(
  -\sum_{\alpha\in C_R}
   t_\alpha[
    \mathbf1_{q\mid B_\alpha}
    -\mathbf1_{q\mid A_\alpha}
   ]
 \right)_+
\le
\mathcal R_R+\mathcal C_R,
}
\tag{M-26201.3}
\]

where:

- `R_R` is the exact signed Green reserve of that complete cell;
- `C_R` is a child contact ledger supported below half scale;
- the sum of all cell reserves is
  \[
  J_X(b_X^\star)-J_X(b_X^{(0)});
  \]
- neighboring-cell boundary terms cancel exactly.

Summing (M-26201.3) gives (M-26201.1).

This is the main symbolic target. It is substantially more specific than a
global claim that “dipole transport is cheap.”

## 9. Mandatory firewalls

A reviewer must reject a purported proof if it:

1. takes positive parts before all layer-cake intervals in a quotient cell are
   recombined;
2. sets the non-prime-power Green extension to zero;
3. charges the positive and negative seed residuals independently;
4. replaces the canonical equality solve by the arithmetic optimal solution;
5. drops prime powers dividing the endpoint;
6. invokes the generic Green-energy bound refuted in scope by `L-24510`;
7. uses the monotone positive cover refuted by `R-25301`;
8. allows a same-scale child after the declared cluster solve;
9. omits the fixed-ratio Mertens shell mutation;
10. promotes a finite reconnaissance ladder to the cofinal theorem.

## 10. Proof-producing schema

Every `CCD(X)` certificate exports:

```text
X and complete prime-power manifest
parabolic seed intervals
endpoint-projected profile matrix
Green Gram and solve enclosure
all-integer induced constraint state
Möbius charge on every quotient cell
exact Green equality vector
negative-excursion layer cake
signed incidence dipoles
same-scale cluster solves
strictly lower-scale child map
contact weights and nonexpansive charge check
D_plus, D_minus
Green reserve
final C_X upper endpoint
fixed-ratio Mertens mutation
```

The exact consumer checks all finite algebra. A separate symbolic theorem must
prove the uniform polylogarithmic envelope.

## 11. Full proposed chain

```text
parabolic entropy seed
-> exact endpoint-projected Green equality
-> Möbius–Poisson quotient-cell decoder
-> one positive-cone clipping
-> signed layer-cake constraint dipoles
-> source-complete cell recombination
-> bounded same-scale cluster solve
-> factor-two contact descent
-> polylog Green contact debt
-> explicit nonnegative prime-ramp minorant
-> prime ramp >= 4 sqrt(X)-X^o(1)
-> square-screw/Landau transfer
-> RH.
```

## 12. Status boundary

Proposed exact and finite:

- Möbius–Poisson factorization;
- Green equality state;
- clipping and signed dipole ledger;
- lower/upper scalar certificates;
- contact formulas;
- finite verifier.

Proposed load-bearing theorem:

\[
\boxed{\mathrm{CCD/GDS}.}
\]

Not claimed:

- a completed proof of `CCD/GDS`;
- the prime-ramp asymptotic;
- RH.
