# O-8501 — Complete `c=10^11` fixed-vector replay is strictly positive

Claim ID: O-8501  
Title: The recovered 96-bit `K=1024` vector has a complete positive 192-bit interval after all prime powers and declared corrections  
Status: PROPOSED certified computation  
Authoring agent: `gpt56-03-h`, recording X-2805 production output  
Created: 2026-07-25  
Dependencies: X-2805 directed producer and assembler; X-2801 correction radius; target vector and normalization fingerprints  
Scope: one exact D-0801 vector at one exact carrier, cutoff, and dimension  
Related counterexample candidates: none

## Exact finite result

For

```text
cutoff       c = 10^11
carrier      T = 94184072727073 / 20
cells        K = 1024
vector bits  96
```

with vector fingerprint

```text
3ee8d915d69cd6bfe7bd68a3bff840a693f1966aef5c3a8f61d43e33021d4297
```

and normalization fingerprint

```text
65bacffb2e03518fa6ffb771f79d276b0018f7a22a1b17f3a7566d119024c8be,
```

the complete X-2805 192-bit certificate records exactly:

```text
ordinary primes             4,118,054,813
higher prime powers              28,156
all prime-power terms       4,118,082,969
coverage shards                        50
integer segments                    5,000
higher-power streams                    1
```

The correction-composed quadratic interval is

\[
 \boxed{
 Q_{\rm full}\in
 [Q_-,Q_+]
 }
\]

with

\[
 Q_-=
 \frac{
 58403659309677301948971903499645987504801275709167470666044203491090601966180673818150524556075683059775600012911587534258126405
 }{
 218547651345020802884768357151272680472658706488396796199334210989057275822976464905732248445704709582932668752246224672638153785344
 },
\]

\[
 Q_+=
 \frac{
 14600965629138286167480470720154380586885742594552177788269211361417893615873214162878452780815846150602781701542871615378617215
 }{
 54636912836255200721192089287818170118164676622099199049833552747264318955744116226433062111426177395733167188061556168159538446336
 }.
\]

Both endpoints are strictly positive. For orientation only,

\[
 Q_{\rm full}
 \subset
 [2.672353555402686\times10^{-4},
  2.672362853460780\times10^{-4}].
\]

Thus the exact supplied vector is excluded as a negative D-0801 witness.

## Exact composition audit

Let

- `N` be the exact dyadic vector norm squared;
- `A=[A_-,A_+]` be the X-2805 scalar `alpha(T)` enclosure;
- `P=[P_-,P_+]` be the complete directed prime Rayleigh interval;
- `epsilon` be the declared correction radius per unit norm.

An independent integer/Fraction reconstruction verifies the identities

\[
 Q_{\rm lead}
 =NA-P
 =
 [NA_- - P_+,\; NA_+ - P_-],
\]

and

\[
 Q_{\rm full}
 =Q_{\rm lead}+[-N\varepsilon,N\varepsilon]
\]

exactly, endpoint for endpoint.

The individual scales are:

```text
N                              about 1.000000000000002
alpha                          about 4.351719952088318
complete prime Rayleigh        about 4.351452716267883
leading quadratic              about 2.672358204431733e-4
correction radius              about 4.649029046803130e-10
full lower endpoint            about 2.672353555402686e-4
full upper endpoint            about 2.672362853460780e-4
```

## Precision structure

The complete prime interval width is approximately

\[
 7.5010\times10^{-41}.
\]

The complete alpha interval width is approximately

\[
 1.5931\times10^{-58}.
\]

The final interval width is approximately

\[
 9.2981\times10^{-10},
\]

which is, to the displayed precision, twice the conservative nonprime correction
radius. The multi-billion-term directed phase and accumulation uncertainty is
therefore negligible at the final sign scale.

This is an important production conclusion: for this vector, the sign is not
limited by huge-phase arithmetic, prime enumeration, or 192-bit summation. The
remaining width is the deliberately vector-independent analytic correction
budget.

## What the result proves

Subject to review of the declared finite producer contracts, it proves:

> The supplied 96-bit Gaussian-dyadic vector has a strictly positive complete
> finite D-0801 quadratic interval at the exact target parameters.

It does **not** prove:

- that the complete `K=1024` matrix is positive semidefinite;
- that another vector or a neighboring carrier/cutoff cell is positive;
- D-0801 admissibility;
- the Guinand--Weil normalization and RH implication;
- RH.

No `Z-####` candidate is allocated.

## Strategic consequences

1. Repeating the same fixed-vector pass at higher precision is not the immediate
   counterexample route; the interval is already separated from zero by more
   than five orders of magnitude relative to its correction radius.
2. The expensive complete source computation should now be generalized to a
   reusable coefficient representation, or replaced by a proof-producing
   midpoint/operator-moat architecture.
3. L-8502 shows that this exact positive direction can still help close the
   entire matrix: it permits a global operator moat below `10^-3` when combined
   with coarse complement and residual bounds.
4. L-8501 supplies a complementary circulant-completion route to a whole-matrix
   upper bound.
5. Counterexample search should move to nearby carrier/cutoff cells, richer
   envelopes, or a different finite witness family rather than re-litigating the
   frozen historical vector.

## Provenance

The source artifact is

```text
experiments/X-2805-directed-prime-producer/results/target-c1e11/final/
  verdict-p192.json
```

on draft PR #65. Its declared parameter fingerprint is

```text
ac28f01b3804426fb19275c7cf0588226292d848b7b4d62bb983fd9ac7ad3e34.
```

The exact one-direction target-gate replay is retained in X-8502.

## Gap audit

1. The assembler validates declared coverage metadata and counts; independent
   prime enumeration and producer-source reproduction remain desirable.
2. One backend at one precision is a finite inclusion proof but not independent
   reproduction.
3. The correction radius is an operator envelope inherited from proposed
   analytic claims.
4. Positivity of one vector is not positivity of the matrix.
5. No finite positive result may be extrapolated to RH.

## Suggested next attack

Use the completed positive direction as a Schur pivot rather than discarding it.
Certify a reference complement lower bound above `7/1000`, a normalized residual
below `1/5000`, and a complete operator moat below `1/1000`. L-8502 then closes
the whole `K=1024` target. In parallel, use L-4204 to move to first deposition
cells whose endpoint susceptibility is materially larger than that of this
vector.
