# Fifth strike on centered Cycle Debt and Q4: exact OPB separator, root-completed redesign, and positive scale-four source

Date: 2026-08-16  
Agent: GPT-5.6 Pro  
Repository: `gfreund123/riemann`  
Target PR: #474  
Frozen parent: `4f59985d9e453c1a1966c5476e1bfcaca3ce4b91`  
Discovery cutoff: `2026-08-16T00:05:49Z`

\[
\boxed{\text{The Riemann Hypothesis remains unproved.}}
\]

## 1. Mandate and method

This pass resumed the exact fourth-strike head and tested the two stated
frontiers:

1. prove One-sided Parity Borrowing (`OPB`), or produce an exact separator and
   redesign the flow;
2. upgrade the scale-four logarithmic-derivative dictionary to a positive,
   capacity-faithful transfer.

The pass deliberately did not import the active factor-67 proposal lineage.
The latest visible PR at cutoff was #509, head
`e01daee9cdfea35d2a7d2591f1df6c8080084119`; it is recorded only as an
excluded live branch.

The directly relevant source packets were frozen to:

```text
PR #272  fa787eed202aef67b2a4e23a64aeedfb05f93645
PR #326  f8030b7fab808956f6e7968d3699685d7fb2cf6c
PR #483  87bd7ad2127f98b6141b4c03355556f2b95f6404
```

Only lightweight work was used:

- exact rational carry matrices;
- exact finite primal/dual and Farkas fixtures;
- outward-rounded `Decimal` square-root/logarithm intervals;
- formal prime-log coefficient dictionaries;
- finite Dirichlet convolution;
- finite endpoint fibre identities.

No broad endpoint scan, zero computation, prime database, or large LP sweep was
retained as evidence.

## 2. Decisive Cycle-Debt finding: zero borrowing is false

The one-sided carry-discrepancy LP of `L-93017` suggested that the high-scale
witness might project to the lower polytope with no excess. Exact experiments
falsified this at the first nontrivial endpoint.

### 2.1 The universal root face

Define

\[
b_2=(\varepsilon-\delta_2)*\mu.
\]

Its floor potential satisfies

\[
\sum_{q=2}^{n}b_2(q)\lfloor n/q\rfloor=-n
\qquad(n\ge2).
\]

Therefore

\[
\psi_*(q)=\frac{\sqrt q}{2\sqrt2}\,b_2(q)
\]

represents the potential `H(1)=0`, `H(n)=-n/(2sqrt(2))` for `n>=2`.
Its defect is zero on every interior split and negative only on the three
quarter-balanced unit-child rows. The exact capacity inequalities hold on all
three rows, so this is a universal feasible discrepancy witness.

This is not a newly invented mode: it is exactly the irreducible dyadic root
source of PR #326 `L-32401`.

### 2.2 Exact finite primal/dual discovery

At `X=6`, with rational unit carry weights, `psi=b2/2` is the exact optimum for
the objective supported on columns `4,5,6`.

A matching dual uses:

```text
one lower multiplier on split (2,1,1);
one upper multiplier on split (6,3,3).
```

The incidence difference is exactly `e4+e5+e6`, and the primal and dual values
are both one. This identifies the root face algebraically.

### 2.3 Directed actual separator

The borrow objective at `X=40` omits the `q=2` term. The root witness gives

\[
0.0057402951203073452286897864721745518758912719224995554701268890
<
V_{40}
<
0.0057402951203073452286897864721745518758912719224995554701268891.
\]

A separate symbolic triangular carry flow realizes the complete `X=20` target
with eighteen strictly positive coefficients. The smallest directed lower
bound is

\[
0.0072746377822568561874828454158911005334\ldots
\]

at parent five. Thus `N_20=0`, and hence

\[
\boxed{\mathfrak B_{40}>1/200.}
\]

The stronger theorem `B_(2Y)=0` is false.

The polylogarithmic OPB statement is not refuted by one finite positive value.
However, every valid proof must now retain and pay the root face.

## 3. Root-completed redesign

For a target specified on columns `q>=3`, define

\[
\rho_2^{>2}(t)=\sum_{q=3}^X b_2(q)t(q),
\qquad
\beta(t)=\frac12[\rho_2^{>2}(t)]_+.
\]

Set `t_tilde(2)=beta(t)` and leave all other columns unchanged. This is the
smallest nonnegative bottom completion satisfying the necessary root
inequality.

On the root face, every positive realization must avoid unit-child edges.
Therefore the correct producer is the interior positive cone

\[
A_X^\circ x=\widetilde t,\qquad x\ge0.
\]

This is finite and fail-closed:

- a feasible point is a positive flow certificate;
- an infeasible point has an exact Farkas separator;
- a feasible point can be chosen rank-sparse.

### 3.1 Generic root neutrality is not sufficient

At `X=6`, the target

\[
t(2)=t(6)=1,\qquad t(3)=t(4)=t(5)=0
\]

has zero `b2` pairing. Yet it is not in the positive interior cone. The exact
Farkas separator is

\[
y(2)=-1,\qquad y(4)=1.
\]

It pairs nonnegatively with every interior split row and negatively with the
target. Thus the critical shape of `w_X` remains load-bearing.

### 3.2 Conditional exact localization of all debt

If the root-completed critical target is positively realizable, the original
target differs only at the bottom split. The resulting optimized Cycle Debt is
then exactly

\[
\mathfrak N_X
=
\frac1{2\sqrt2}
\left[
\sum_{q\le X}\frac{b_2(q)}{\sqrt q}\log\frac Xq
\right]_+.
\]

The new explicit producer theorem is named `CRCTP`: positive realization of
the root-completed critical target in the interior cone.

`CRCTP` is not proved in this packet. Unlike another scalar criterion, it is a
concrete all-coordinate positive-flow theorem with an exact primal/Farkas
format. If proved, it would remove every transverse negative coefficient and
leave only the unavoidable root mode.

## 4. Decisive Q4 advance: genuinely positive scale-four source

The fourth strike gave

\[
A_4(s)=\frac{1-4^{1-s}}{(1-4^{-s})\zeta(s)}.
\]

The fifth strike studies its reciprocal

\[
G_4(s)=\frac1{A_4(s)}
=
\zeta(s)\frac{1-4^{-s}}{1-4^{1-s}}.
\]

Its coefficients are exactly

\[
\boxed{g_4(n)=4^{\lfloor v_2(n)/2\rfloor}>0.}
\]

The generalized von Mangoldt sequence of `G4` is nonnegative:

\[
\Lambda_4(p^k)=\log p\quad(p\text{ odd}),
\]

and

\[
\Lambda_4(2^r)
=
\begin{cases}
\log2,&r\text{ odd},\\
(2^{r+1}-1)\log2,&r\text{ even}.
\end{cases}
\]

Define the positive source

\[
\Lambda_+
=
(\varepsilon+2\delta_2)*\Lambda_4.
\]

Then the complete compact-Q4 source factors coefficientwise as

\[
\boxed{
c_\circ
=
(\varepsilon-2\delta_2)*\Lambda_+,
\qquad
\Lambda_+\ge0.
}
\]

This includes the full four-adic gauge. It is stronger than the former signed
logarithmic-derivative dictionary.

## 5. Positive source-owned physical transfer

Let

\[
h_m(x)=1_{m\le x}-2\,1_{2m\le x}
\]

and

\[
Z_{m,N}(j)
=
h_m(N)-h_m(j)-h_m(N-j-1).
\]

Then

\[
\boxed{
R_N(j)
=
\sum_{m\le N}\Lambda_+(m)Z_{m,N}(j).
}
\]

Every coefficient is nonnegative. Every source atom has one label, one
scale-two Haar fibre, and one endpoint placement. The source/provenance bridge
is now exact.

For each atom, split orthogonally:

\[
Z_{m,N}
=
\kappa_{m,N}\mathbf1+Z_{m,N}^\perp.
\]

The scalar is explicit:

\[
\kappa_{m,N}
=
\begin{cases}
1-6m/N,&m\le N/2,\\
2m/N-1,&N/2<m\le N.
\end{cases}
\]

The transverse fibre satisfies

\[
\|Z_{m,N}^\perp\|_2^2\le144m.
\]

For `N>=4m`, the sharper decomposition is `Z=1+E`, with

\[
|\operatorname{supp}E|\le4m,
\qquad
\|E\|_2^2\le64m.
\]

Thus the positive scale-four dictionary is locally capacity-faithful modulo one
principal scalar channel.

## 6. Exact Q4 no-go and retained Hardy boundary

One source atom already has

\[
Z_{m,N}(j)=1
\]

on `N-4m` interior positions when `N>=4m`. Hence

\[
\|Z_{m,N}\|_2^2\ge N-4m.
\]

No reserve depending only on the local atom can control the full row uniformly
in the endpoint. The principal channel cannot be absorbed into the transverse
capacity.

Aggregating the orthogonal splits gives

\[
R_N=M_\circ(N)\mathbf1+R_N^\perp.
\]

Therefore the principal coefficient is exactly the Q4 endpoint mean. Positivity
does not estimate it.

The backward Hardy inverse also still requires the boundary theorem

\[
C_\circ(N)=o(N).
\]

The positive primitive `Psi_+` has a linear main term; only its Haar difference
cancels. The unconditional PNT remains the correct boundary input.

## 7. Stress tests

The packet rejects the following overclaims:

```text
zero parity borrowing;
root neutrality is sufficient;
positive scale-four coefficients bound the Q4 mean;
atomwise transverse capacities add orthogonally;
the principal fibre can be hidden in a local port;
the Hardy boundary vanishes from source positivity;
finite LP trends prove a cofinal theorem.
```

The Mellin consumer remains zero-safe:

- the dyadic root numerator `1-2^(-z-1/2)` has no zero in `Re z>0`;
- the scale-four finite factor has zeros on `Re s=1` and poles on `Re s=0`;
- neither cancels an open-strip zeta zero.

## 8. Lightweight exact replay

Retained verdicts:

```text
PASS_X_93021_OPB_ROOT_SEPARATOR
PASS_X_93022_Q4_POSITIVE_SCALE_FOUR
```

`X-93021` records:

```text
255    all-scale root floor identities
8,320  root split-defect identities
9      exact rational primal/dual checks
5      root-neutral Farkas checks
36     symbolic X=20 flow checks
20     directed X=20 positivity checks
76     symbolic X=40 root-completed flow checks
39     directed X=40 root-completed positivity checks
6      directed X=40 separator checks
5      hostile mutations
```

`X-93022` records:

```text
768    Dirichlet inverse checks
2,304  positive generalized-prime checks
768    source factorization checks
4,743  prefix Haar checks
4,650  complete row-fibre checks
9,468  principal/transverse checks
96     principal-channel no-go checks
5      hostile mutations
```

## 9. Honest closure status

The fifth strike does not provide a complete unconditional proof.

It decisively changes both frontiers:

```text
Cycle Debt:
    zero borrowing is false;
    root mode isolated exactly;
    root-completed transverse cone is finite and fail-closed;
    the actual X=40 completion is strictly positive;
    CRCTP remains open cofinally.

Q4:
    source factorization is genuinely positive;
    source-owned atomwise physical capacity is explicit;
    one principal mean and one aggregate transverse Gram remain open.

Cross-route:
    the type signatures now match, but no conservative principal coupling or
    aggregate transverse map is proved.
```

The smallest credible synthesis is now:

\[
\begin{array}{c|c}
\text{Cycle Debt}&\text{Q4}\\ \hline
\text{dyadic root face}&\text{principal endpoint mean}\\
\text{positive transverse carry cone}&
\text{positive-source transverse boundary Gram}
\end{array}
\]

A closing theorem must pair the two principal outputs separately and map the
two transverse objects without duplicating source or capacity.

\[
\boxed{\text{RH remains unproved.}}
\]
