# X-0202 — Exact finite barrier for the superabundant Robin reduction

Experiment ID: X-0202  
Status: CERTIFIED COMPUTATION PENDING INDEPENDENT REPRODUCTION  
Agent: gpt56-02  
Issue: #2  
Date: 2026-07-22  
Related claims: L-0201, T-0201  
Candidate IDs: none

## Research question

Can the finite exceptional gap in L-0201 be closed exactly, proving that every
Robin counterexample implies a superabundant Robin counterexample above 5040?

## Method

`verify.py` computes \(\sigma(n)\) for every \(1\le n\le5582\) using exact
integer divisor additions. Abundancy ratios are compared by integer cross
multiplication; no floating point is used in the finite maxima.

Two remaining transcendental comparisons are enclosed with the directed-decimal
engine from X-0201:

\[
e^\gamma\log\log 5041>\frac{224}{65},
\qquad
e^\gamma\log\log 5583>\frac{403}{105}.
\]

## Command

```bash
python verify.py --precision 60 --gamma-terms 100000 \
  --output results/certificate.json
python -m unittest discover -s tests -v
python -m compileall -q verify.py tests
```

## Exact results

The exhaustive exact enumeration gives:

\[
\max_{1\le n\le5040}\frac{\sigma(n)}n
=\frac{\sigma(5040)}{5040}
=\frac{19344}{5040}
=\frac{403}{105},
\]

and 5040 is the unique maximizer.

It also gives:

\[
\max_{5041\le n\le5582}\frac{\sigma(n)}n
=\frac{\sigma(5460)}{5460}
=\frac{18816}{5460}
=\frac{224}{65},
\]

and 5460 is the unique maximizer.

## Directed comparison results

At 60 decimal digits with 100,000 gamma terms, the certificate encloses

\[
e^\gamma\log\log 5041-\frac{224}{65}
\]

inside a strictly positive interval whose lower endpoint exceeds `0.3707648`.
It encloses

\[
e^\gamma\log\log 5583-\frac{403}{105}
\]

inside

```text
[3.14655904367e-5, 5.06562719319e-5].
```

Both signs remain positive in tests at lower and higher precision/gamma-term
settings.

## Consequence

The interval at 5041 excludes every integer in the finite window
5041–5582, because \(R(n)=e^\gamma\log\log n\) is increasing. For any
counterexample \(n\ge5583\), its least earlier maximizer of \(\sigma(k)/k\)
has value greater than `403/105`, so it must occur after 5040 and is itself a
superabundant Robin counterexample. This yields proposed theorem T-0201.

## Verification

Four tests pass:

- exact maximum on 1–5040;
- exact maximum on 5041–5582;
- both directed signs at a control precision;
- stability at two precision/gamma-term settings.

## Proof boundary

The finite divisor-sum maxima are exact. The two transcendental signs depend on
the X-0201 Decimal interval implementation and CPython's documented
correct-rounding contract. Independent Arb/MPFI reproduction is required before
T-0201 is promoted beyond PROPOSED.

## Limitations

- This proves completeness only for the superabundant class, not the smaller CA
  class used in X-0201.
- The superabundant sequence is infinite; this is a structural reduction, not a
  finite proof of RH or its negation.
- No counterexample candidate was found.
