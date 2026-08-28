# The native bilateral phase and coprimality layer externalize exactly

Status: **exact fixed-stratum phase factorization, exact finite Möbius
externalization of the reduced-core coprimality predicate, and exact
finite-Fourier rank firewall for genuinely mixed phases; no complete native
source gluing, partial-Frobenius theorem, uniform trace estimate, RH, or GRH**

Architecture: **Architecture B only**.

Bounded replay:
[`ffps_relative_phase_stratified_externalization.py`](ffps_relative_phase_stratified_externalization.py).
Canonical fixture:
[`ffps_relative_phase_stratified_externalization.json`](ffps_relative_phase_stratified_externalization.json).

Frozen inputs:

1. PR #760's relative-first Adams packet at
   `aaccfe767c3d36a353056c9a2483e3824d89949f`;
2. the exact native bilateral least-prime phase theorem `L-106120` at
   `86cac1d64364015ec2cc0f8fbb6fc75dc041c12b`.

## 0. Outcome

The first apparent partial-Frobenius obstruction in the displayed native
bilateral source is not the Artin--Schreier phase itself.

At fixed source labels
\[
(g,\ell,\rho,\sigma,\tau,h,k),
\]
the exact member of `L-106120` contains
\[
 e_\ell(-hQd^2)e_\rho(kPc^2).
\]
This factors literally into one function of the left variables `(P,c)` and
one function of the right variables `(Q,d)`:
\[
\boxed{
 e_\ell(-hQd^2)e_\rho(kPc^2)
 =
 \Phi_{\rho,k}(P,c)\,\Psi_{\ell,h}(Q,d),
}
\tag{0.1}
\]
where
\[
 \Phi_{\rho,k}(P,c)=e_\rho(kPc^2),\qquad
 \Psi_{\ell,h}(Q,d)=e_\ell(-hQd^2).
\tag{0.2}
\]

The fixed least-prime and owner-class conditions are one-sided on the same
stratum:
\[
 \ell=P^-(c),\quad \tau=\kappa_\rho(P),
 \qquad
 \rho=P^-(d),\quad \sigma=\kappa_\ell(Q).
\tag{0.3}
\]
Thus the phase and these label predicates are already external-product data.

The remaining displayed arithmetic coupling is `(c,d)=1`.  It also has an
exact signed externalization.  For arbitrary finitely supported functions
`A,B`,
\[
\boxed{
 \sum_{(c,d)=1}{A(c)B(d)\over cd}
 =
 \sum_{m\ge1}{\mu(m)\over m^2}
 \left(\sum_{u\ge1}{A(mu)\over u}\right)
 \left(\sum_{v\ge1}{B(mv)\over v}\right).
}
\tag{0.4}
\]
Every sum is finite at a finite source horizon.  Moreover
\[
 \sum_{m\ge1}{|\mu(m)|\over m^2}
 \le \zeta(2),
\tag{0.5}
\]
so this exact decomposition has a conductor-independent absolute outer cost.
The already displayed common-square weight `g^{-2}` has the same summable
shape.

Consequently the **fixed-label native phase/coprimality layer** belongs to the
finite signed external-product span.  The phase portion of `RELPARTFROB` is
therefore discharged on these strata.

This does not prove `RELPARTFROB` for the complete relative object.  The shell,
Boolean representation, marked-prime, carrier, renewal, equal-product, Wick,
and horizon predicates named in `L-106120` still have to be transported
through the relative projector and shown to be external, partially
Frobenius-compatible, or cancelled.

## 1. Proof of the phase factorization

Equation (0.1) is equality in the product of the two cyclotomic value groups.
The first character sees only `P,c` modulo `rho`; the second sees only `Q,d`
modulo `ell`.  No Fourier expansion, triangle inequality, or completion is
used.

The labels are essential.  If `ell,rho,h,k` are allowed to vary inside the
same object without retaining their indexing spaces, the statement is no
longer one fixed external product.  The correct geometric object is a finite
direct sum over the exact labels, or a labelled correspondence carrying them.

## 2. Proof of coprimality externalization

Insert the finite Möbius identity
\[
 1_{(c,d)=1}=\sum_{m\mid c,\ m\mid d}\mu(m).
\tag{2.1}
\]
Then write `c=mu`, `d=mv`.  The normalization becomes
\[
 {1\over cd}={1\over m^2uv}.
\]
Finite rearrangement gives (0.4).

This is better suited to the closed-point architecture than replacing
coprimality by a positive sieve.  The Möbius sign remains outside the two
one-sided factors until after Adams extraction and trace recombination.

## 3. A sharp firewall for genuinely mixed phases

The favorable conclusion above uses the actual separated phase of
`L-106120`.  It must not be generalized to an arbitrary Artin--Schreier phase
on a product.

For a prime `p` and `lambda != 0 mod p`, let
\[
 T_{x,y}=e_p(\lambda xy),
 \qquad x,y\in\mathbf F_p^\times.
\tag{3.1}
\]
Its exact row Gram is
\[
\boxed{TT^*=pI-J.}
\tag{3.2}
\]
Indeed the diagonal row inner product is `p-1`, while every distinct-row
inner product is `-1`.  The eigenvalues are `1` on the constant line and `p`
on its orthogonal complement, so
\[
\boxed{\operatorname{rank}T=p-1.}
\tag{3.3}
\]

A sum of `R` external products has trace-matrix rank at most `R`.  Therefore
the mixed phase (3.1) needs at least `p-1` external summands.  There is no
bounded-rank external-product presentation as `p` grows.

This is a scope firewall, not an obstruction to the actual displayed native
phase: equation (0.1) has rank one at each fixed label.  If a later cleanup
creates a surviving bilinear residue phase after the relative projector, the
naive bounded-rank separable route fails and must be replaced by a
Fourier--Deligne transform, a genuine higher-rank partial-Frobenius object,
or an exact cancellation before estimation.

## 4. Updated Architecture B gate

The relative-first route may now be refined as
```text
NATREL
  transport the complete hard-selected identity through one common cleanup

PHASE-EXT
  fixed-label bilateral phases, owner classes, least-prime predicates, and
  reduced-core coprimality have the exact signed externalization (0.1)-(0.4)

REMAINING-GLUE
  externalize or cancel shell/carrier/renewal/Boolean/Wick/horizon couplings

RELPARTFROB
  equip the resulting relative object with partial Frobenii

CLOSED-POINT ADAMS -> RELTRACE -> PRINCIPAL BINDING -> RH.
```

`PHASE-EXT` is proved here.  Every later arrow remains open.

## 5. Proof ledger

| statement | grade |
|---|---|
| fixed-label phase factorization (0.1) | **PROVED EXACT** |
| one-sided label predicates (0.3) | **READ DIRECTLY FROM FROZEN SOURCE** |
| coprimality externalization (0.4) | **PROVED EXACT** |
| absolute outer cost (0.5) | **PROVED** |
| mixed Fourier Gram/rank firewall (3.2)--(3.3) | **PROVED EXACT** |
| complete native source is separable | **NOT PROVED** |
| NATREL / RELPARTFROB / RELTRACE | **NOT PROVED** |
| RH or GRH | **NOT PROVED** |

No external novelty or priority claim is made.

## 6. Bounded replay

```text
python -B research/l-families/atlas/function_field/ffps_relative_phase_stratified_externalization.py --check
python -B -O research/l-families/atlas/function_field/ffps_relative_phase_stratified_externalization.py --check
python -B -m unittest tests.test_ffps_relative_phase_stratified_externalization
python -B -O -m unittest tests.test_ffps_relative_phase_stratified_externalization
```

The replay uses exact rational and modular arithmetic.  It enumerates no
finite-field family, curve, conductor family, `L`-function, or zero.
