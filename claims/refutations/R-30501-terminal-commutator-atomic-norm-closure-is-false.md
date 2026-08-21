# R-30501 — Terminal commutator closure through the atomic norm is false

Claim ID: `R-30501`  
Title: The complete stopped critical boundary has linear square-root atomic norm, so `L-30403/T-30401` do not yield polylogarithmic Cycle Debt  
Status: **EXACT SCOPE-MATCHING REFUTATION OF THE LOAD-BEARING ATOMIC-NORM STEP**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-08  
Frozen target: PR #304 at `78b75fc17e27334a9950018528c1c6e083d74820`  
Primary targets: `L-30403.6`, `L-30403.8`, `T-30401.4`, `T-30401.8`  
Scope: the proposed polylogarithmic source norm and terminal-lift composition; the adjacent-commutator algebra itself is retained

## 1. The reviewed proof step

PR #304 defines the ordinary divisor-source atomic norm

\[
 \|\sigma\|_{\rm at}
 =\sum_m\sqrt m\,|\sigma_m|
\]

and proves the valid source-to-flow estimate

\[
 \mathcal N_\omega(\Phi(\sigma))
 \le24\|\sigma\|_{\rm at}.
\tag{R-30501.1}
\]

It then asserts that the complete finite Euler/Peano boundary source emitted by
the positive stopped-power critical target satisfies

\[
 \sum_a\|\sigma_a\|_{\rm at}
 =O((\log X)^B),
\tag{R-30501.2}
\]

and concludes polylogarithmic Cycle Debt.

The claim already fails at the initial boundary generation.

## 2. Exact counterfamily

`L-30501` considers exactly the stopped critical powers used in PR #301:

\[
 p_Y(n)=n^{-1/2}\mathbf1_{n\le Y},
 \qquad
 w_X=\sum_{Y<X}\log{Y+1\over Y}\,p_Y.
\]

Let `Sigma_X` be the unique ordinary divisor source of the complete initial
finite-cutoff boundary. For every `X>=192`, `L-30501` proves

\[
 \boxed{
 \|\Sigma_X\|_{\rm at}
 \ge {X\over750}.
 }
\tag{R-30501.3}

The proof is source-local. On every node

\[
 \lfloor X/3\rfloor+1
 \le m\le
 \lfloor2X/5\rfloor,
\]

no higher multiple lies in the strict half-scale source support, and

\[
 \sqrt m\,\Sigma_X(m)<-{1\over25}.
\tag{R-30501.4}

Thus no finite Euler order, Peano re-expression, or common-destination
recombination can alter these coordinates after the channels are summed.

## 3. The coefficient-normalization mismatch

The raw boundary in PR #286 is

\[
 \sum_{2kq-1>Y}(2kq-1)^{-s}
 -\sum_{(2k+1)q>Y}((2k+1)q)^{-s}.
\tag{R-30501.5}

By contrast, the logarithmic estimate in `L-30402.10` is proved for the
different source-weighted coefficients

\[
 A_k={ (2kq-1)^{-s}\over2k},
 \qquad
 B_k={ ((2k+1)q)^{-s}\over2k+1}.
\tag{R-30501.6}

The factors `1/(2k)` and `1/(2k+1)` are exactly what create the extra half-power
and the logarithmic `k`-sum. They are not present in the raw boundary
(R-30501.5). A proof may use (R-30501.6) only after supplying an exact identity
which converts the complete raw cutoff source to that weighted source while
retaining all remainder terms. PR #304 supplies no such identity.

The uniqueness statement in `L-30501` shows that an ordinary divisor-source
conversion cannot provide it with polylogarithmic absolute norm.

## 4. Disposition of the PR #304 chain

The following statements survive:

```text
E_h=T_(h+1)-T_h realizes one divisor atom        RETAINED
||E_h||_(omega,1)<=24 sqrt(h+1)                  RETAINED
Phi is a bounded map from atomic source norm      RETAINED
actual divided shifted fibers have logarithmic cost RETAINED AT THEIR TYPE
```

The load-bearing composition does not:

```text
complete raw boundary atomic norm is polylog      FALSE
sum over all depths is polylog by that norm        FALSE AS DERIVED
terminal atom-by-atom commutator closure            REJECTED
T-30401 as a complete proposed RH proof             REJECTED
Riemann Hypothesis                                  UNPROVED
```

This does not prove that optimized Cycle Debt is large. It proves that the
specific terminal strategy loses the complete transition-band cancellation
before Cycle Debt is optimized.

## 5. Corrected research boundary

A valid continuation must act before ordinary source atomization. Permitted
possibilities include:

1. preserve the shifted-even/odd quotient labels and construct a complete
   relative source-to-existing-flow manifest;
2. apply Pascal cycles to the recombined boundary before measuring negative
   capacity;
3. compress through the full reciprocal-eta/Mersenne source and retain its
   sparse exceptional ledger;
4. prove a direct structured Cycle-Debt estimate which is not bounded by
   `||Sigma_X||_at`.

It is not sufficient to relabel the raw boundary coefficients by the divided
fiber weights of (R-30501.6).

## 6. Exact replay

`experiments/X-30501-boundary-atomization/verify.py` checks the rational moats,
the top-band index geometry, the stopped-layer telescope, and the linear count.
Its proof object uses only integers and `fractions.Fraction`.

## 7. Verdict boundary

```text
adjacent commutator algebra                    PROPOSED COMPLETE / RETAINED
critical raw boundary top-band source          PROVED MACROSCOPIC
polylog absolute atomic norm                   REFUTED
optimized structured Cycle Debt                OPEN
Riemann Hypothesis                             UNPROVED
```