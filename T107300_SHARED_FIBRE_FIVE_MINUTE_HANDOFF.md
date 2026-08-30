# T-107300 shared-fibre primitive trace — five-minute handoff

Status: **exact native rank-one compression and Frobenius-stable primitive
object proved; uniform signed trace and principal binding open**

Base:

```text
PR #765
codex/riemann-structures-marked-descent-gate0
a30276a5be049749ebb2147f30f000dd5659298b
```

Read in order:

1. `claims/lemmas/L-107300-native-rectangular-shared-fibre-factorization.md`
2. `claims/lemmas/L-107301-augmentation-primitive-frobenius-object.md`
3. `claims/lemmas/L-107302-live-history-panel-has-explicit-primitive-energy.md`
4. `claims/theorems/T-107300-shared-fibre-relative-primitive-trace-frontier.md`
5. `claims/refutations/R-107300-residue-aggregate-alone-still-forgets-native-rank-one-energy.md`
6. `experiments/X-107300-shared-fibre-primitive/README.md`

## New exact compression

Inside one shared marked fibre, suppose the live arithmetic panel is a
rectangular family of left and right source atoms and the literal native
coefficient factors as

\[
z_{ij}=\overline{a_i}b_j.
\]

The physical residue map also factors:

\[
r(i,j)=(r_R(j),r_L(i)).
\]

If \(P_L,P_R\) are the one-sided residue aggregation maps and
\(H_\ell,H_\rho\) are the centered one-place kernels, then the complete
fixed-fibre Wick scalar is exactly

\[
\boxed{
\mathscr W(a,b)
=
\bigl(a^*P_L^*H_\rho P_La\bigr)
\bigl(b^*P_R^*H_\ell P_Rb\bigr)
-
d_{\ell,\rho}\|a\|^2\|b\|^2.
}
\]

Thus the native two-dimensional panel is controlled by two one-sided
quadratic forms and two one-sided norms. Arbitrary coefficient freedom and a
faithful rank-\(|\Omega|\) pushed module are unnecessary for this native
rank-one class.

## Canonical primitive object

Each one-sided source space has the Frobenius-stable augmentation splitting

\[
K^X=M_X\oplus P_X,
\qquad
P_X=\ker(\text{cell aggregation}).
\]

The bilateral tensor has four exact graded channels

\[
M_L\otimes M_R,\quad
P_L\otimes M_R,\quad
M_L\otimes P_R,\quad
P_L\otimes P_R.
\]

Physical residue pushforward sees only the mean–mean channel. Literal
diagonal energy is the sum of all four. Source-aware Adams extraction
commutes with this splitting because it is performed before pushforward and
the augmentation projections commute with total Frobenius.

## Live panel computation

The one-hundred-history native control already present on PR #765 has
one-sided coefficient pattern

```text
3,3,-1,-1,-1,-1,-1,-1,-1,-1.
```

Hence

\[
\sum a_i=-2,\qquad \|a\|^2=26,
\]

and for the bilateral rank-one panel

\[
|\sum_{ij}z_{ij}|^2=16,\qquad
\sum_{ij}|z_{ij}|^2=676.
\]

Its same-cell Wick value is therefore

\[
\boxed{-660\,d_{\ell,\rho}.}
\]

This proves that the actual native history vector has a large primitive
component; it is not merely an arbitrary-support counterexample.

## Remaining gates

```text
RECTGLUE107300:
  decompose the complete live fibre into source-authorized rectangular
  panels plus a signed boundary defect of acceptable total size;

PRIMTRACE107300:
  prove a uniform signed Adams/trace estimate for the three primitive
  channels after conductor recombination;

PRINBIND107300:
  identify the resulting trace with the frozen principal physical detector.
```

These gates remain open. RH and GRH remain unproved.
