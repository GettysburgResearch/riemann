# Genus-two Sym12 finite cusp-trace scout

Status: **FINITE EXACT MATCH AT `q=3,5,7` ONLY**

Scope: stored complete joint laws at three odd primes; no new family scan.

Exact sources: two committed, content-hash-locked JSON artifacts listed below.

What was actually run: 251 stored atoms, one reciprocal recurrence through
degree 12, and an eight-coefficient exact modular-form reconstruction.

Smallest remaining gap: an arithmetic or cohomological theorem identifying the
candidate trace for general odd prime powers; another finite row can falsify but
cannot prove that theorem

The replay is `genus2_sym12_finite_cusp_trace_scout.py`; its canonical,
self-hashed artifact is `genus2_sym12_finite_cusp_trace_scout.json`.

## 1. Exact finite calculation

For a stored genus-two numerator

\[
P_D(u)=1+a_Du+b_Du^2+qa_Du^3+q^2u^4,
\]

write

\[
\frac1{P_D(u)}=\sum_{n\geq 0}r_D(n)u^n.
\]

The producer uses the exact recurrence

\[
r_D(n)=-a_Dr_D(n-1)-b_Dr_D(n-2)
       -qa_Dr_D(n-3)-q^2r_D(n-4),
\]

with absent negative-index terms omitted. It evaluates this recurrence once
through degree 12 on each stored joint-law atom and accumulates degrees
`6,8,10,12` with the atom multiplicities.

The degree-twelve normalizations are

\[
T_{(12,0)}(q)=\frac{\sum_Dr_D(12)}{q(q-1)}
\]

and

\[
\widehat H_{12}
=T_{(12,0)}+2q+9+4\Theta_\Delta
 +\Theta_{(8,2)}+\Theta_{(10,2)}.
\]

The exact output is:

| `q` | atoms | `sum r_D(6)` | `sum r_D(8)` | `sum r_D(10)` | `sum r_D(12)` | `T_(12,0)` | `Hhat_12` | `H_12` |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 3 | 32 | -24 | -126 | 3,828 | -27,522 | -4,587 | -3,708 | -22,248 |
| 5 | 81 | -80 | 3,980 | 372,960 | 5,345,020 | 267,251 | 287,250 | 5,745,000 |
| 7 | 138 | -168 | -43,218 | -4,222,764 | -16,074,870 | -382,735 | -449,624 | -18,884,208 |

Every division by `q(q-1)` is exact.

## 2. Lower recurrence controls

The same recurrence pass reproduces three already closed normalizations:

\[
\sum_Dr_D(6)=-4q(q-1),
\]

\[
\sum_Dr_D(8)=q(q-1)(-\Theta_{(8,2)}(q)-q-6),
\]

and

\[
\sum_Dr_D(10)=q(q-1)\big((q-1)\Theta_\Delta(q)
-\Theta_{(8,2)}(q)-\Theta_{(10,2)}(q)-q-7\big).
\]

The `r_D(10)` totals also equal the committed held-out totals byte-for-byte.
These controls catch a reversed numerator sign, a missing reciprocal term, a
wrong family normalization, or a trace-row mismatch. They do not supply a
fourth degree-twelve value.

## 3. The explicit weight-14 target

No database orbit label is used. Define the comparison target by the explicit
Fricke-negative normalized expansion

\[
\begin{aligned}
f_-(Q)={}&Q+64Q^2+1236Q^3+4096Q^4-57450Q^5\\
         &+79104Q^6+64232Q^7+O(Q^8).
\end{aligned}
\]

The producer independently reconstructs these coefficients from the committed
modular rows using

\[
f_-(Q)=\frac{f_{(8,2)}(Q)E_6(Q)
                 +3g_{(10,2)}(Q)E_4(Q)}4,
\]

where the Eisenstein coefficients are generated exactly from divisor sums.
All eight numerator coefficients are checked to be divisible by four.

Clery and van der Geer give the two rational weight-14 level-2 expansions,
including this `f_-` and its Fricke sign, on pp. 1139--1140 of
[their 2018 paper](https://ems.press/content/serial-article-files/26421). The
explicit series above, rather than a potentially confusing orbit label, is the
identity of the comparison target in this packet.

At the three tested primes the match is exact:

| `p` | `a_p(f_-)` | `-p a_p(f_-)` | `Hhat_12(p)` |
|---:|---:|---:|---:|
| 3 | 1,236 | -3,708 | -3,708 |
| 5 | -57,450 | 287,250 | 287,250 |
| 7 | 64,232 | -449,624 | -449,624 |

Thus the finite statement is

\[
\boxed{\widehat H_{12}(p)=-p\,a_p(f_-),\qquad p=3,5,7.}
\]

Equivalently, on these three rows only,

\[
T_{(12,0)}(p)=-p a_p(f_-)-2p-9-4\tau(p)
-a_p(f_{(8,2)})-a_p(g_{(10,2)}).
\]

## 4. Source and resource locks

The producer reads exactly these committed artifacts:

1. `balanced_control_family_scan.json`, commit
   `955ea1e25160075fb4b498018319c80f7e4db9d5`, git blob
   `377c8c03d6a9ccf5a505a9b1a19acc360c59ff44`, LF-normalized SHA-256
   `c3494ae852fda4e754b3b0da7cb30a26e3e38ec1c87e2619cd6fee6cdc68b68e`,
   payload SHA-256
   `50fd136eb0483387246766c5f2426c3e727c69cd9a89943f9268368db0f9d39c`.
   Only its complete stored joint `(a_D,b_D)` laws and coverage metadata are
   consumed.

2. `genus2_sym10_marked_trace_average.json`, commit
   `42910253be8173c6cd0de19a7a7403d0c31b5c22`, git blob
   `561caa7dc504dfb158908aef9229e91af0707a1e`, LF-normalized SHA-256
   `4f91ac00193805207088e9fc6aea2b464645267b17dc54f71165a1ae3b9d45ce`,
   payload SHA-256
   `0fbf48768fdea477b2bee4f53c8f1e547a167155c665b5e97bc201961971ec77`.
   Only its committed modular trace and coefficient rows are consumed.

The source files total 180,674 bytes. The historical balanced artifact covers
20,175 monic quintic candidates and 17,068 squarefree members, but none is
reenumerated here. The replay performs exactly:

- 251 joint-law atom visits;
- 3,012 reciprocal updates (`251 x 12`), containing 10,542 explicit recurrence
  terms;
- 1,004 weighted accumulations (`251 x 4`);
- 56 Eisenstein divisor tests, of which 32 contribute divisor-power terms;
- 72 truncated q-series convolution terms and 8 linear combinations;
- 3 final finite-row checks.

The producer caps itself at exactly those operation counts, two source files,
200,000 aggregate source bytes, 32,768 output bytes, and four wall-clock
seconds. Arithmetic is entirely integral. It imports no enumerator and uses no
floating-point fit or external computer algebra.

The JSON contains LF-normalized hashes of this note, the producer, and its
test. Its `payload_sha256` is the canonical SHA-256 of the complete JSON object
with only that self-hash field removed.

## 5. Firewalls

### Finite-interpolation firewall

The three equalities above are not an all-`q` formula. A correction containing
`(q-3)(q-5)(q-7)` is invisible on every tested row, as are more structured
trace channels that vanish at those primes. Three exact values do not identify
a motive, compatible system, endoscopic/Yoshida summand, or cohomology class.

### Prime-power firewall

For `q=p^r`, the relevant Frobenius-power trace would be
`alpha_p^r+beta_p^r`. It is not, in general, the q-expansion coefficient
`a_(p^r)`. This packet tests only the primes `3,5,7`; it does not enumerate or
evaluate `q=9`, and it makes no prime-power continuation.

### Computation firewall

The replay authenticates a calculation from committed aggregate atoms. It is
not an authenticated replay of the primitive quintic enumeration, and it does
not claim to be one. The complete family enumeration remains provenance of the
locked balanced artifact.

No RH, GRH, number-field transfer, memberwise sign, or global Euler-product
claim is made.
