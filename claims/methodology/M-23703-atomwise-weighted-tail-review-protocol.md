# M-23703 — Atomwise weighted-tail adversarial review protocol

Claim ID: `M-23703`  
Status: **FAIL-CLOSED REVIEW PROTOCOL**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-08  
Target: `L-23717`, `T-23706`

## 1. Freeze and scope

Freeze the reviewed commit before beginning.  The proposal has three distinct layers:

```text
A. exact endpoint/shell algebra;
B. proved upper-half negativity;
C. atomwise weighted prime-tail order AWTO.
```

A defect in layer C does not retroactively invalidate a passing identity in A or B.  Conversely, finite scans or the upper-half theorem do not verify AWTO.

## 2. Mandatory independent reconstruction

### 2.1 Endpoint difference

Starting from the two parabolic seeds, independently derive

\[
b_T(m)-b_{T-1}(m)
=2\ell_T\sqrt m
+4m\left(T^{-1/2}-(T-1)^{-1/2}\right)
\]

for `m<T`, and check that the entering endpoint is zero rather than the analytic continuation of this expression.

### 2.2 Column response

For each small endpoint, compare:

```text
direct response v_q(b_T)-v_q(b_(T-1));
endpoint-profile sum of L-23717.11;
positive row-atom response from PR #265.
```

The three values must agree.

### 2.3 Shell telescope

Test unequal endpoints, including odd dyadic endpoints, and verify that target activation at `q=T` contributes zero.  No endpoint atom may be counted twice.

### 2.4 Radical ledger

Construct `L_z(m)` from ordinary prime divisors only and verify

\[
\sum_p(\log p)\Gamma_T(p)
=
\sum_mF_T(m)[L_z(m)-L_z(m-1)].
\]

Replacing ordinary primes by all prime powers is a deliberate mutation and must change the result.

### 2.5 Upper-half inequalities

Check separately:

```text
(T-1)/2 < q < T-1;
q = T-1;
T-1 composite;
T-1 prime;
small endpoints T=3,4,5.
```

Every logarithmic inequality must retain its orientation.

## 3. Automatic rejection conditions for AWTO

Reject `T-23706` as a proof upon any one of:

1. one finite pair `(T,z)` with `A_T(z)>0`;
2. an omitted quotient boundary;
3. replacement of `log rad(m)` by `log m` without the complete squarefull reserve;
4. entrywise absolute values before neighboring radical increments are combined;
5. a one-frequency Selberg square in place of the physical two-frequency block;
6. an uncharged same-scale residue after the proposed lower-scale route;
7. use of PNT or finite scans as a substitute for a cofinal signed identity;
8. failure of the dyadic or `2/3` Mertens mutation.

## 4. Recommended symbolic production object

For each endpoint `T`, emit:

```text
F_T(m) at every integer m;
every quotient layer floor((T-1)/p);
every ordinary-prime radical increment;
every proper-power/digital reserve;
the upper-half negative ledger;
the lower-scale destination of every remaining term;
the two-frequency reflected matrix and cross terms;
the final weighted tail at every prime cutoff.
```

A valid symbolic theorem must prove the sign uniformly in `T`; a list of successful endpoints is reconnaissance only.

## 5. Status vocabulary

```text
endpoint/shell formulas       VERIFIED or REJECTED independently;
upper-half theorem            VERIFIED or REJECTED independently;
AWTO                          VERIFIED only after a cofinal proof;
AWTO -> WSTS -> RH            conditional until AWTO passes;
RH                            unproved unless every dependency passes.
```
