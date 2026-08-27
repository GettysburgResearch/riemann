# T-105360 — A cofinal terminal Stieltjes reserve is enough for the Xi boundary gate

Claim ID: `T-105360`  
Status: **MAJOR EXACT IMPLICATION REDUCTION — XI PRODUCER ESTIMATES OPEN**  
Created: 2026-08-23  
Depends on: `T-105220`, `T-105330`, `T-105350`, `L-105360`, `L-105361`  
RH status: **unproved**

## 1. Previous sharp gates

The sharp low-order theorem `T-105220` has the form

\[
\mathrm{PRES105220}
\wedge
\mathrm{BRP105220}
\Longrightarrow
\mathrm{RH}.
\tag{T-105360.1}
\]

The later moment coordinates identify:

```text
CRVH105330   complete critical-residue Vandermonde/Hankel positivity;
OASH105350   complete origin Stieltjes positivity of the boundary function.
```

Under the exact finite-window hypotheses,

\[
\mathrm{CRVH105330}\Longrightarrow\mathrm{PRES105220}
\]

and

\[
\mathrm{OASH105350}\Longleftrightarrow\mathrm{BRP105220},
\]

with the nonreal critical correction retained explicitly.

The apparent burden in `OASH105350` was positivity at every order in every
window. `L-105360--L-105361` remove the all-window part of that burden.

## 2. Terminal asymptotic inward reserve

Fix one parity-symmetric Xi derivative `F=Xi^(r)` occurring at the last
potentially defective level of the exact reverse-Rolle descent. Let

\[
\Omega_1\Subset\Omega_2\Subset\cdots
\]

be its canonical parity-symmetric regular exhaustion. Let

\[
\mathsf S_{k,N}^{(0)}
=[\beta_{a+b}(F;\Omega_N)]_{a,b=0}^{k-1},
\qquad
\mathsf S_{k,N}^{(1)}
=[\beta_{a+b+1}(F;\Omega_N)]_{a,b=0}^{k-1}.
\tag{T-105360.2}
\]

Define the terminal gate:

```text
TAIR105360 — terminal asymptotic inward reserve

There is a cofinal sequence N_j -> infinity such that, for every fixed
matrix order k>=1 and a in {0,1},

    liminf_j lambda_min(S_(k,N_j)^(a)) >= 0.

Equivalently, the negative part of each fixed-order terminal matrix tends to
zero along the cofinal sequence.
```

The quantifier order is load bearing:

\[
\forall k\ \exists\text{ a fixed-order limit},
\]

not a uniform estimate over all `k` at once.

## 3. Exact inward transport

Assume `CRVH105330` throughout the exhaustion. Then every critical point
crossed between `\Omega_N` and `\Omega_M` is real and has

\[
\rho_c={F(c)\over F''(c)}\le0.
\]

By `L-105361`, for `M>N`,

\[
\boxed{
\mathsf S_{k,N}^{(a)}
=
\mathsf S_{k,M}^{(a)}
+
\mathsf P_{k;N,M}^{(a)},
\qquad
\mathsf P_{k;N,M}^{(a)}\succeq0,
}
\tag{T-105360.3}
\]

for both `a=0,1`. Therefore

\[
\lambda_{\min}(\mathsf S_{k,N}^{(a)})
\ge
\lambda_{\min}(\mathsf S_{k,M}^{(a)}).
\tag{T-105360.4}
\]

Choose `M=N_j` and let `j\to\infty`. `TAIR105360` gives

\[
\boxed{
\mathsf S_{k,N}^{(0)}\succeq0,
\qquad
\mathsf S_{k,N}^{(1)}\succeq0
}
\tag{T-105360.5}
\]

for every fixed inner `N` and every finite `k`. Thus `OASH105350` holds in the
complete exhaustion.

## 4. Conclusion-facing implication

The exact implication chain is

\[
\boxed{
\mathrm{CRVH105330}
\wedge
\mathrm{TAIR105360}
\Longrightarrow
\mathrm{PRES105220}
\wedge
\mathrm{OASH105350}
\Longrightarrow
\mathrm{PRES105220}
\wedge
\mathrm{BRP105220}
\Longrightarrow
\mathrm{RH}.
}
\tag{T-105360.6}
\]

This is conditional on the same multiplicity, common-zero, canonical
exhaustion and Hermite--Biehler interface hypotheses frozen in `T-105220` and
its parent descent packet. No new limiting interchange is hidden here: each
finite matrix order and inner window is fixed before the outer limit.

Neither `CRVH105330` nor `TAIR105360` is proved for the required Xi level.

## 5. Concrete affine terminal subgate

Define the stronger but simpler source target:

```text
AATR105360 — asymptotically affine terminal remainder

Along one cofinal regular sequence,

    beta_0(F;Omega_(N_j)) -> a_F >= 0,
    beta_n(F;Omega_(N_j)) -> 0 for every fixed n>=1.
```

By `L-105361`,

\[
\boxed{
\mathrm{AATR105360}
\Longrightarrow
\mathrm{TAIR105360}.
}
\tag{T-105360.7}
\]

Hence

\[
\boxed{
\mathrm{CRVH105330}
\wedge
\mathrm{AATR105360}
\Longrightarrow
\mathrm{RH}.
}
\tag{T-105360.8}
\]

The affine target is directly calibrated by the polynomial outer window
`H(z)=z/n`. For Xi it asks for coefficientwise decay of the non-affine
boundary Cauchy tail, not positivity of arbitrary packet determinants.

## 6. Why this is a genuine reduction

The former boundary target required

```text
for every window N;
for every packet size k;
prove two PSD matrices exactly.
```

The new target requires only

```text
choose one cofinal terminal sequence;
for each fixed k, make its negative part tend to zero.
```

Positive residue atoms generated while moving inward then pay the complete
finite-window hierarchy automatically. Exact positivity at terminal windows,
uniformity in matrix order, and a separate proof at every inner height are all
unnecessary.

## 7. Binding firewalls

1. The transport direction is outer to inner. Inner positivity alone does not
   force outer positivity because positive atomic reserve is removed outward.
2. A positive residue changes the update sign and destroys monotonicity.
3. A nonreal critical pair produces an indefinite real rank-two update.
4. Safe-axis scalar positivity is not a substitute for the two complete
   Stieltjes Hankel families.
5. `AATR105360` is an open asymptotic theorem for Xi, not a consequence of
   finite order or formal growth.

## 8. Exact frontier

```text
nested-window atomic moment transport          PROVED EXACT
parity-symmetric Stieltjes atom transport       PROVED EXACT
cofinal vanishing negative part -> all windows PROVED EXACT
asymptotically affine terminal remainder       OPEN / SOURCE-SPECIFIC
CRVH105330 critical residue hierarchy           OPEN / SHARP
TAIR105360 terminal asymptotic reserve           OPEN / SHARP BOUNDARY PRODUCER
Riemann Hypothesis                              UNPROVEN
```
