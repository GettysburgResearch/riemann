# Independent review of PR #473 — factor-67 SONTR with explicit compact reserve

## Freeze

```text
review cutoff UTC:          2026-08-14T20:19:52Z
main at review start:       9c7538559d7f56c2914b39aed5a1fb3fbf7ce131
proposal PR:                #473
proposal base SHA:          4ac821701177edb67a77fe43e89cc2a7a53af68a
reviewed proposal head:     71d6a859ea741fe035de709e8d10ed37301b778e
reviewed proposal tree:     036365630b50cde18929715fa9d9211434821a09
proposal branch:            research/gpt56-pro/91690-factor67-sontr
```

The proposal head remained fixed during the theorem reconstruction recorded here.

A materially relevant successor appeared during review:

```text
PR #476 head: 9f16ce483954d4233b68ee09cb6bec47400aa3cc
new claim:    L-91694 — positive direct integrals preserve subcritical target mass
```

That theorem is not silently imported into the verdict for PR #473. It is discussed below because it addresses the first open arrow found in the frozen target.

## Executive verdict

```text
L-91690 root-window Hall algebra                 VERIFIED WITH FROZEN INPUTS
L-91692 total-row Hall transparency              VERIFIED
factor-67 equality-density bound                 VERIFIED / DIRECTED
C_67 and interior reserve arithmetic             VERIFIED
terminal 4452 / 5033 / 581 reserve               VERIFIED WITH FROZEN L-91115
aggregate P_61/67 Schur-port inequality          VERIFIED WITH NARROW SCOPE
per-packet causal coefficient mass <1/8          VERIFIED
global direct-integral child-mass normalization  UNPROVEN / GAP
T-91660 / T-91661 full SONTR composition         UNPROVEN / GAP
endpoint-to-RH implication                       CONDITIONAL / NOT REACHED
Riemann Hypothesis                               UNPROVEN
```

The compact-reserve pass is a substantial advance. The identities behind Hall
transparency are exact, the equality density rather than the larger SHARP target
is the correct density for the B-spline bound, and the displayed interior and
terminal constants are mutually consistent.

The full proof proposal does not yet follow at the reviewed SHA. The first
load-bearing gap is the passage from fiberwise causal decompositions to one
mass-normalized hereditary child decomposition after positive endpoint
integration and grouping.

## 1. What the new packet closes

### 1.1 Strict root domain

With

\[
K_X=\left\lfloor X/67\right\rfloor+1
\]

and retained endpoint support beginning at `K_X+2`, every root quotient
satisfies

\[
X/s<67.
\]

Thus the root Hall graph contains only the `P_61` small-divisor source and does
not reintroduce the stopped-leaf Hall theorem refuted at
`p=67,y=13,py=871`.

Disposition: **VERIFIED**.

### 1.2 Exact target, score and row Hall ledger

For target flow `t_(o,e)` and residual target mass

\[
r_e=T_e-\sum_ot_{o,e},
\]

the identity

\[
\sum_eT_e\rho_j(e)-\sum_oT_o\rho_j(o)
=
\sum_er_e\rho_j(e)
+
\sum_{o,e}t_{o,e}
[\rho_j(e)-\rho_j(o)]
\]

is exact. Under the frozen monotonicity
`e<=o => rho_j(e)>=rho_j(o)`, the second term is a nonnegative current row
bonus.

The same Hall coefficients give exact target use and score superordination.
Applying the ordinary maps at `q` and `4q` separately preserves the row equality,
after which their radix-four difference may be formed.

Therefore the statement

\[
\varepsilon_{\rm Hall,row}=0
\]

is correct at the total physical-row scope. It does not assert that the finite
equality seed equals its continuum Volterra model; the separate
finite/continuum defect remains.

Disposition: **VERIFIED WITH FROZEN MONOTONICITY INPUT**.

### 1.3 Equality-density firewall

The endpoint quantizer is controlled by

\[
L(x)
=
2\sqrt{x}\sum_{n\le x}\frac{\mu(n)}n
-
\sum_{n\le x}\frac{\mu(n)}{\sqrt n},
\]

not by

\[
\Psi(x)
=
4\sqrt{x}\sum_{n\le x}\frac{\mu(n)}n
-
3\sum_{n\le x}\frac{\mu(n)}{\sqrt n}.
\]

I independently reconstructed the cell endpoint calculation. On the strict
window `1<=x<67`,

```text
minimum L = 0.3186174007676585... at x -> 33-
maximum L = 1.8284271247461903... at x -> 2-
```

so

\[
\frac{159}{500}<L(x)<\frac{183}{100}<2.
\]

Meanwhile `Psi(2-)>2`, confirming that the distinction is load-bearing.

Disposition: **VERIFIED**.

### 1.4 Interior reserve

The factor-67 quadrature constant is

\[
C_{67}
=
\sum_{k\le67}
\frac{|\mu(k)|}{\sqrt k}
\left(1+\frac12\log\frac{67}{k}\right)
=
18.4717269\ldots<19.
\]

The resulting bounds

\[
|v_q(E_X)|<\frac{57}{2}q^{-3/2},
\qquad
|\mathcal D_4v_q(E_X)|
<\frac{285}{8}q^{-3/2}
\]

combine with the collar estimate to give

\[
\frac{|\mathcal D_4v_q(C_X-E_X)|}{\Omega_X(q)}
<
\frac{5655}{32K}.
\]

For

\[
\sigma_K=\frac{K}{K+178},
\]

the exact remaining coefficient is

\[
178-\frac{5655}{32}
=
\frac{41}{32}>0.
\]

Hence the displayed interior reserve

\[
s_X(q)
\ge
\frac{41}{32(K+178)}\Omega_X(q)
\]

is correct.

Disposition: **VERIFIED**.

### 1.5 Terminal reserve

The factor-67 adaptations give

```text
collar contribution        < 4224 X^(-3/2)
finite mismatch            <  228 X^(-3/2)
complete possible overfill < 4452 X^(-3/2)
top omission response      > 5033 X^(-3/2)
remaining reserve          >  581 X^(-3/2)
```

The arithmetic is exact. The omitted top cell has positive equality density and
no odd Hall demand. Above the retained endpoint support, triangularity does give
zero response.

Disposition: **VERIFIED WITH FROZEN L-91115 INPUT**.

### 1.6 Narrow aggregate-port use

If each branch satisfies

\[
M_b\succeq\frac19\mathcal V_bI,
\qquad
\tau_{p_b}\mathcal V_b<\frac19\mathcal V_b,
\]

then positive summation proves that one aggregate Schur port covers the
aggregate correction. This use does not require the historical open
colored-to-physical conclusion of `L-91320`.

Disposition: **VERIFIED WITH FIXES**. The dependency lock should freeze the
exact Schur-reserve displays rather than cite the whole historical claim, which
also contains superseded physical conclusions.

## 2. First open load-bearing arrow

The fiberwise causal theorem and the global hereditary consumer use different
normalizations.

For one positive packet, `L-91650` supplies formal coefficients with

\[
\sum_i\alpha_i<\frac18.
\]

The root construction, however, is a positive direct integral of packets whose
target masses, active rough-prime lists and child fields can vary with the
endpoint fiber. The hereditary consumer `T-91312` requires the
**mass-weighted** inequality

\[
\sum_b\alpha_b\,m(P_b)
<
\frac18\,m(P),
\]

followed by normalization of each aggregate child packet.

The frozen proposal moves across this interface in three incompatible ways:

1. `L-91690` applies the causal identity to each positive residual packet.
2. `L-91691.2--3` integrates and immediately retains a scalar
   `sum alpha_b<1/8`.
3. `L-91692.30--31` says instead to apply one causal coefficient list to an
   aggregate packet and absorb all fiberwise children with the same prime into
   one child.

No theorem at the reviewed SHA defines the aggregate rough-prime placement
operator in the first-owner direct integral, proves that it reproduces the
fiberwise source-owned children, or performs the required target-mass
renormalization.

The distinction is not cosmetic. If fibers have coefficients `a_i(s)` and child
target masses `m_(s,i)`, the global quantity is

\[
M_{\rm ch}
=
\int\sum_i a_i(s)m_{s,i}\,d\lambda(s),
\]

not an unweighted repetition or suppression of the scalar coefficient list.
After grouping by provenance label `b`, the hereditary coefficient is the
actual grouped target mass divided by parent target mass.

The deposited `X-91692` grouping regression uses one toy set of hard-coded
coefficients common to every toy fiber. It does not test varying active lists,
target masses, first-owner labels or normalized grouped children.

Therefore the arrow

```text
fiberwise causal split
    -> positive endpoint direct integral
    -> grouped unit-mass children with coefficient sum <1/8
```

is **UNPROVEN / GAP** in PR #473.

## 3. Material successor

PR #476 subsequently adds `L-91694`, whose statement is exactly the missing
mass-normalization theorem:

\[
\int\sum_i a_i(s)m(A_{s,i}Q_{s,i})d\lambda(s)
\le
\rho\int m(P_s)d\lambda(s),
\qquad
\rho<1/8,
\]

followed by normalization of aggregate children by their actual target masses.

That theorem appears to be the right repair. It was not present at
`71d6a859ea741fe035de709e8d10ed37301b778e` and has not been independently reconstructed in this review. The
next proposal should either stack it explicitly or incorporate its proof into
the SONTR lock.

## 4. Secondary corrections

### 4.1 Contradictory seed display

`T-91660` displays

\[
b_X^\star=\overline b_X^\star
\]

and immediately says that this equality is never asserted. The controlling
identity is

\[
b_X^\star=\overline b_X^\star+E_X.
\]

This is evidently an editorial error, but it occurs in a load-bearing theorem
and must be corrected.

### 4.2 Dependency lock scope

`t91661-factor67-reserve-closure-lock.json` freezes several commit SHAs and the
new proof object, but it is not a path/blob-complete transitive proof lock.
In particular, the exact retained scopes of `L-91110/L-91111/L-91114/L-91115`
and the narrow Schur-port displays are not individually frozen.

The lock is useful provenance infrastructure; it should not be described as a
complete immutable proof DAG.

### 4.3 Live movement

The proposal intentionally freezes older heads of several moving PRs. During
review, PR #476 supplied a material successor theorem. Those newer results do
not retroactively change the verdict at the reviewed SHA.

## 5. Exact reviewed DAG

```text
strict factor-67 root window
  -> fixed P61 target Hall                         VERIFIED

target Hall
  -> exact target residual
  -> score superordination
  -> nonnegative all-row bonus                     VERIFIED

positive endpoint integration
  -> one total equality row                        VERIFIED FORMALLY

finite/continuum mismatch + B-spline collar
  -> explicit interior reserve                     VERIFIED

top omission
  -> explicit terminal reserve                     VERIFIED ON FROZEN INPUT

branch Schur reserves
  -> one aggregate port                            VERIFIED WITH NARROW SCOPE

fiberwise causal packets
  -> per-packet child coefficient <1/8             VERIFIED

fiberwise split + endpoint integration
  -> mass-normalized grouped HTR children           UNPROVEN / GAP

HTR
  -> Lambda_eq=O(1)                                CONDITIONAL

native benchmark comparison
  -> Y4 weighted slack O(log X)                    CONDITIONAL

one-sided endpoint consumer
  -> RH                                             CONDITIONAL / NOT REACHED
```

## 6. Integration recommendation

Retain and consider integrating, after ordinary review:

```text
Hall total-row transparency;
the strict factor-67 equality-density bound;
C67<19 and the 5655/32 interior calculation;
the 581 X^(-3/2) terminal reserve;
the narrow aggregate Schur-port summation.
```

Do not promote `T-91660` or `T-91661` to a verified complete theorem at the
reviewed SHA.

The minimal repair is:

1. import or reconstruct `L-91694`;
2. define the actual grouped child packets and their target masses;
3. rewrite the HTR decomposition with those normalized coefficients;
4. regenerate the proof lock with exact path/blob scopes;
5. rerun the full endpoint-to-RH reconstruction.

## 7. Computation boundary

I inspected the retained `X-91690` and `X-91692` source and result claims but
did not rerun their full directed campaigns. I independently reconstructed the
66-cell equality-density extrema, `C67`, and all displayed reserve arithmetic.
No large scan or expensive formal build was launched.

## Final conclusion

\[
\boxed{\text{The compact factor-67 reserve calculation survives review.}}
\]

\[
\boxed{\text{The global mass-normalized hereditary child step does not yet.}}
\]

\[
\boxed{T\text{-}91660/T\text{-}91661\text{ do not establish RH at }71d6a859ea741fe035de709e8d10ed37301b778e.}
\]
