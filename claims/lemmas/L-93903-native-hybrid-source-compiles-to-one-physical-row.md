# L-93903 — The native hybrid occurrence table compiles to one source-owned physical row

Claim ID: `L-93903`  
Status: **CANDIDATE-COMPLETE LIVE SOURCE-TO-ROW COMPILER FOR INDEPENDENT RECONSTRUCTION**  
Created: 2026-08-16  
Inputs: `L-91870`, `L-91872`, `L-92930`, `L-93901`, `L-93902`  
RH status: **unproved pending review**

For every integer `X>=10^12`, put

\[
K=\lfloor X/67\rfloor+1,
\qquad
I_X=[K+2,X-10002].
\]

## 1. Exact native arithmetic input

Use the hybrid identity

\[
\boxed{c_X=c_{X,A}+\overline c_{X,I}+\mathcal R E_X^I.}
\tag{L-93903.1}
\]

The anchored input `c_(X,A)` is represented by the literal finite Möbius
occurrences in the complementary integer cells.  The bulk input
`bar c_(X,I)` is represented by the paired Volterra Möbius occurrences on the
complete retained cells.  The finite defect `R E_X^I` is signed observation
data and is not source.

No row-first `P_61` rough lift is used as the parent marginal.

## 2. One explicit certificate space

Every positive source incidence is stored in the common table

\[
\Gamma_X^{src}(\omega,a,t),
\]

where `omega` contains

```text
anchored/bulk sector;
integer endpoint-cell tag;
Möbius occurrence;
equality/reserve channel;
small-prime divisor;
rough history and least rough owner;
actual parent/child endpoints;
child coefficient and orientation;
Target-Lorenz edge/residual owner;
current/child class;
physical same-index placement.
```

On bulk cells use the exact two-channel couplings of `L-93901`.  On anchored
stopped leaves use the exact generator of `L-93902`.  The incidence equations
exhaust every negative source marginal and split every positive source marginal
between matched and residual uses exactly once.

## 3. Actual children

A stopping-line child is the actual oriented source-tree packet, not a full
native packet inferred from its endpoint scale and not a rough-lift reservoir
slice.  Its arithmetic coefficient and same-index placement occur once in the
incidence table.

The primary one-shot construction physically places every actual child before
quantization and keeps it as an internal label.  The exported recursive family
is empty.  The optional audit implementation may instead export the same actual
children and terminalize each against its own typed capacities; no promotion to
`Omega(Y)` is allowed without a separate theorem.

## 4. One physical operator

The physical target is the disjoint union

\[
\mathcal T_X^{anc}\dotplus\mathcal T_X^{bulk}.
\]

Apply the single block-diagonal Markov operator

\[
Q_X^{nat}=I_{anc}\oplus Q_{bulk}.
\]

It depends only on the physical target point, never on a source, channel,
rough-owner, or child label.  Then apply one common thinning factor and retain
an explicit discard incidence for each native input marginal.

The final uncorrected physical row is the output marginal

\[
\boxed{d_X^0(j)
=\int Q_X^{nat}(j\mid t)\,d\Gamma_X^{src}(\omega,a,t).}
\tag{L-93903.2}
\]

It is coefficientwise nonnegative.  The live certificate of `X-93900` is a
finite exact instance of this same occurrence schema; it is not an unrelated
vector fixture.

## 5. Typed marginal identities

Before the signed finite comparison, the certificate gives simultaneously

```text
native target marginal;
declared score with an explicit nonnegative surplus;
literal component-row score;
every component row;
ordinary response at every q;
ordinary response at every 4q;
boundary coordinates;
one owner for every source and actual child occurrence.
```

Ordinary responses are summed on the total row before radix-four detail is
formed.  This is one joint certificate, not separately optimized coordinate
vectors.

```text
native input marginal                  explicit hybrid identity
bulk target/score gap                  repaired by two channels
anchored leaf coefficients             explicit Target-Lorenz generator
actual child marginal                  explicit and one-use
row bonus                              current-only, zero source target
one physical quantizer                 exact
rough lift / full-child promotion      forbidden
Riemann Hypothesis                     unproved pending review
```
