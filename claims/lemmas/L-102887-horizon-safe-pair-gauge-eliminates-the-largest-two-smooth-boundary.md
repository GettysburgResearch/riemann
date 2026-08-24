# L-102887 — A horizon-safe pair gauge eliminates the largest-two smooth boundary

Claim ID: `L-102887`  
Status: **PROVED EXACT OWNER/COMPLETION GAUGE THEOREM**  
Created: 2026-08-24  
Depends on: `L-102746--L-102749`; `L-102505`; `L-102706--L-102709`; `L-102886`  
RH status: **not assumed**

Fix one dyadic physical horizon

\[
Y\le X<2Y.
\]

The centered ratio-eight observation sees only source products `n<=16Y`.

After placing the joint two-label `67` occurrence in the already-closed repeated-prime diagonal, every retained squarefree occurrence has distinct physical-prime labels.

## 1. At most one uncompletable label

If two selected primes satisfied

\[
r_1>4\sqrt Y,
\qquad r_2>4\sqrt Y,
\]

then

\[
r_1r_2>16Y,
\]

contradicting activity on the horizon.  Hence every active occurrence contains at most one prime greater than `4 sqrt(Y)`.

## 2. Deterministic horizon-safe pair

For each occurrence of depth at least two choose one unordered pair as follows:

1. include the unique label `>4 sqrt(Y)` if it exists;
2. fill the remaining owner slot by a fixed deterministic label rule among the other distinct physical primes;
3. if no large label exists, use the first two labels in that same fixed rule.

The rule is frozen on the dyadic horizon before any phase or physical observation.  It need not choose the two largest primes.

Moving the canonical equal-pair allocation of `L-102746` to this one pair changes labelled energy by at most

\[
\binom{k}{2}\ll(\log(2Y))^2
\]

for a depth-`k` occurrence, exactly as in `L-102830`.  Physical realization is unchanged coefficientwise.

## 3. Every nonowner is completable

Every nonowner prime is at most `4 sqrt(Y)`.  Apply the exact positive completion/gauge transfer to all nonowner labels at that fixed cutoff.  The resulting physical product has the form

\[
\boxed{N=pq\,a^2,}
\tag{L-102887.1}

where `p,q` are the two selected distinct owner primes, `a` is squarefree, and

\[
(a,pq)=1.
\]

The squarefree kernel of `N` is exactly `pq`.  Therefore

\[
\boxed{
(p,q,a)\longmapsto pq\,a^2
}
\tag{L-102887.2}

is injective up to the fixed order of the two owners.

Unlike the largest-two gauge, there is no condition

\[
P^+(a)<q.
\]

All active nonowner primes beyond the two owners are simply squared; an inactive completed product contributes zero.

## 4. Static horizon and source scope

The owner rule and completion cutoff are constant on the entire dyadic block.  Resetting them on the next block changes only a proof-side source decomposition of the same fixed detector and occurs on a zero-measure boundary, as in `L-102886`.

Thus the largest-two stopped monoid `N_<q` and its smooth-boundary current are optional coordinates, not intrinsic source terms.  In the horizon-safe gauge the core source is the monoid

\[
\boxed{
\mathbb N^{(p,q)}=\{a\ge1:(a,pq)=1\},
}
\tag{L-102887.3
\]

with only two fixed Euler factors removed.

The exact Vaughan theorem for this source is `L-102888`.
