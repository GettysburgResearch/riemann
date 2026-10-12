# Companion columns using the published verified height

Status: proposed imported-height corollaries and source audit, pending
independent review. This is separate from the native 8,049-bracket packet.
Scope: actual `Xi(z)=xi(1/2+iz)`, a finite real-part column of unbounded
lower depth, all positive lambda, and each fixed derivative order with
positive displayed width. No published large computation is rerun here.
Exact sources: [CENSUS_FULL_COLUMN_SECTOR.md](CENSUS_FULL_COLUMN_SECTOR.md),
its complete-product and localization dependencies, and the published
Platt--Trudgian verification specified below.
What was actually run: fetched and read the arXiv v1 paper; no large-height
primitive zero evaluation, Turing computation or sign list was replayed.
Smallest remaining gap: independent audit of the stronger published-method
contract required to include the real boundary. The open-lower-column
corollary needs only the paper's stated RH-through-height theorem.

## 1. Bind the published source and distinguish its two contracts

Dave Platt and Tim Trudgian, *The Riemann hypothesis is true up to
3*10^12*, Bull. London Math. Soc. **53** (2021), 792--797,
DOI [10.1112/blms.12460](https://doi.org/10.1112/blms.12460).
The text read here is [arXiv:2004.09765v1](https://arxiv.org/pdf/2004.09765v1),
21 April 2020, dated 22 April 2020 in the manuscript. The downloaded PDF
SHA256 is `3362f66af9fa9373977eee70e2282ec33989d5d8b97e0852df9e32cc25b52885`.
The extraction with `pdftotext -layout` had SHA256
`eae9298a2482d36719f37aa8d0b66a1e1c5c8f6c10fcc9988b2632f07a99551e`.
These hashes identify the source read; they are not correctness certificates
for its seven-million-core-hour computation.

Theorem 1 on manuscript page 2 states:

> The Riemann hypothesis is true up to height 3 000 175 332 800. That is, the
> lowest 12 363 153 437 138 non-trivial zeroes rho have Re rho = 1/2.

Call this the **published location contract**. We use only the weaker
conservative height

\[
H=3\cdot10^{12}<3\,000\,175\,332\,800.
\tag{PV1}
\]

This theorem wording alone does not state simplicity. It suffices for the
open-lower-column result in Section 2, because the interior arguments
retain every positive integer multiplicity.

Section 2 on manuscript pages 2--3 describes a stronger computational
contract. It says the algorithm computes values of the completed zeta
function on the half line and counts sign changes; then:

> Using a variation of Turing's method ... we can confirm that all the
> expected zeroes have been accounted for, so none lie off the half line
> and the Riemann hypothesis holds in the given range.

It also says that once a sign change was found, they "merely counted it and
moved on". The default lattice did not isolate every zero; the remaining
treatment belongs to the imported algorithm and is not separately described
in this short Section 2 account.
This is the **published sign-change/complete-count contract**: a count of
distinct sign-change intervals saturates the complete Turing zero count,
which counts analytic multiplicity. The computation uses Arb interval
arithmetic and rigorous truncation bounds. This stronger imported contract,
not the RH-only theorem wording, is what can supply simplicity for Section 3.

## 2. The open column needs only the location contract

Suppose every zero of a source satisfying THEOREM.md in `|Re z|<=R` is
real, with arbitrary positive integer multiplicities. The proof of
CENSUS_LOCALIZATION.md Sections 1--2, through (L10), uses no simplicity:
complete polynomial approximants have no nonreal zeros in that range;
repeated conjugate-pair localization and Gauss--Lucas give (L5)--(L8),
and the positive source moments make the signs strict. Thus, for fixed `r`
with `R-(r+2)A>0`, both `H_r,H_(r+1)` are nonzero in the corresponding
open lower column, with the two strict signs in (FC3).

The derivative product (FC4)--(FC5) has no omitted exponential, and
(FC6)--(FC13) keeps arbitrary real-zero multiplicities explicitly. Therefore
its strict sector proof applies for `y>0` without simple real zeros.
The real boundary is the only place where a multiple zero could make a
companion vanish; it is deliberately excluded here.

Import the published location contract, apply the actual zero correspondence
and conjugation symmetry, and use the classical complete strip `A=1/2`.
For every integer `0<=r<=5,999,999,999,997` and every real `lambda>0`,

\[
\boxed{E_{r,\lambda}(z)\ne0,\quad E_{r,\lambda}'(z)\ne0,\quad
\operatorname{Re}\frac{iE_{r,\lambda}(z)}{E_{r,\lambda}'(z)}>0
\quad(z=T-iy,\ |T|<3\cdot10^{12}-(r+2)/2,\ y>0).}
\tag{PV2}
\]

Here `E_(r,lambda)=Xi^(r)-i lambda Xi^(r+1)`. The displayed order upper
bound is exactly the positive-width condition; every order is fixed before
taking the complete polynomial limit. This is not a uniform numerical
calculation at trillions of derivative orders.

## 3. Simplicity follows from the stronger count saturation contract

Let the distinct intervals counted by the published method be `I_1,...,I_M`.
Each strict real sign change contains a real zero of odd analytic
multiplicity, in particular at least one unit of the complete multiplicity
count. If the complete count is exactly `M`, there is room for precisely
one multiplicity unit per interval and none elsewhere. Hence every interval
contains one simple zero, and no additional real multiple or nonreal zero
is omitted. In particular an odd multiplicity at least three would spend
at least two extra units; an even-multiplicity zero without a sign change
would also spend extra units. Both contradict saturation.

Thus importing the described published sign-change/complete-count contract
supplies a complete **simple** real census through the conservative `H`.
This logical consequence is not inferred from the RH-only theorem wording,
and the sign-change list, complete Turing count and implementation have
not been independently replayed here.

Under this explicitly stronger imported contract, (FC2) gives the closed
version of (PV2):

\[
\boxed{E_{r,\lambda}(z)\ne0,\quad E_{r,\lambda}'(z)\ne0,\quad
\operatorname{Re}\frac{iE_{r,\lambda}(z)}{E_{r,\lambda}'(z)}>0
\quad(|T|<3\cdot10^{12}-(r+2)/2,\ y\ge0,\ \lambda>0),}
\tag{PV3}
\]

for the same fixed-order range. This includes the real boundary using
(L11)--(L12) and the simple-zero induction. A reader importing only the
stated location theorem should retain (PV2), not silently include `y=0`.

The native 8192-height packet has stronger session-level primitive replay
provenance and stays separate. Both forms of this published-height corollary
have finite real-part range, retain all unknown tail zeros beyond `H`, and
supply no RH conclusion.
