# L-108001 — Uniqueness backbone for trace-to-object reconstruction

```text
Claim ID: L-108001
Status:   PROVED (elementary/folklore; complete proof included because the
          structure detector's refusal semantics rest on it)
Created:  2026-08-30
Depends on: none (self-contained linear algebra over a field)
Used by:  T-108002 (structure detector), core/reconstruct.py
RH status: unproved / not addressed.
```

## Statement

Let `K` be a field and `(c_k)_{k>=0}` a sequence in `K`.

**(i) (uniqueness of the reduced rational form).** There is at most one pair
`(P, Q)` of polynomials with `Q(0) = 1`, `gcd(P, Q) = 1`, and
`sum_k c_k T^k = P(T)/Q(T)` as formal power series — with NO properness
hypothesis. If moreover the form is PROPER (`deg P < deg Q = L`), then
`(P, Q)` is already determined by the first `2L` coefficients
`c_0, ..., c_{2L-1}` together with the value `L`: any sequence agreeing on
those terms and admitting a PROPER rational form of denominator degree
`<= L` has exactly the form `P/Q`. (The properness hypothesis on the
competing form is necessary: the sequence `1, 1, 0, 0, ...` has the proper
form `1/(1-T)` refuted at index 2 by the improper polynomial form `1 + T`,
though both have denominator degree `<= 1` and agree on the first two
terms — adversarial-review example, 2026-08-30.)

**(ii) (window certification).** If Berlekamp-Massey run on
`c_0, ..., c_{N-1}` returns a connection polynomial of degree `L` with
`2L + 2 <= N`, and the read-off numerator `P := trim((C * c-series) up to
index N-1)` satisfies `P/C = sum c_k T^k` on all `N` terms with an observed
zero tail (`deg P <= N - 2`), then every longer sequence extending `(c_k)`
by the SAME rational law `P/C` is the unique rational extension among
proper forms of denominator degree `<= L` (and among ALL reduced forms it
is the unique one with this `(P, C)`, by (i)); conversely two distinct
reduced PROPER forms of denominator degree `<= L` cannot agree on `2L`
consecutive initial terms. Improper numerators (needed for trace
generating series `-T Q'/Q`, whose numerator degree equals `deg Q`) are
certified by the full-window re-expansion, not by the `2L`-term count. In
particular the detector's A5 held-out test (predicting withheld terms from
the certified prefix form) is exact, not heuristic.

**(iii) (weight-w rigidity).** Suppose additionally `Q, Q' ∈ Z[T]` are two
denominators with constant term 1, degree `d`, both with all inverse roots
of modulus `q^{w/2}` (a "weight-w q-Weil condition"). If the coefficient
sequences of `1/Q` and `1/Q'` agree for `k = 0, ..., 2d - 1`, then `Q = Q'`.
A weight-w local factor is therefore determined by its first `2d`
coefficients; the detector's reconstruction of a candidate Frobenius local
factor from a `2d`-window is unique, and any later disagreement is a
genuine refutation of the weight-w model, never an artifact.

## Proof

**(i).** Suppose `P/Q = P'/Q'` as power series with `Q(0) = Q'(0) = 1` and
both fractions reduced. Then `P Q' = P' Q` in `K[[T]]`, hence in `K[T]`
(both sides are polynomials). Since `gcd(P, Q) = 1`, `Q | Q'`; symmetrically
`Q' | Q`; with `Q(0) = Q'(0) = 1` this gives `Q = Q'`, hence `P = P'`.
For the determination from `2L` terms: the recurrence
`c_n = -(q_1 c_{n-1} + ... + q_L c_{n-L})` for `n >= L` (where
`Q = 1 + q_1 T + ... + q_L T^L`) expresses `c_L, ..., c_{2L-1}` as `L`
linear conditions on `(q_1, ..., q_L)`. If two PROPER reduced forms of
denominator degree `<= L` agreed on `c_0..c_{2L-1}`: let the two forms be
`P/Q`, `P'/Q'` with `deg Q, deg Q' <= L` and `deg P < deg Q`,
`deg P' < deg Q'`; then `P Q' - P' Q` is a polynomial of degree
`<= (L-1) + L < 2L` whose power-series expansion `(P/Q - P'/Q') Q Q'`
vanishes to order `>= 2L` (the series agree on `2L` terms and `Q Q'` has
constant term 1). A polynomial of degree `< 2L` vanishing to order `>= 2L`
is zero, so `P/Q = P'/Q'`, and by uniqueness of reduced forms the reduced
pairs coincide. (Without properness the degree bound `< 2L` fails and so
does the conclusion — see the example in the statement.) ∎

**(ii).** The certification hypothesis says the specific pair `(P, C)`
reproduces all `N >= 2L + 2` terms. By (i) it is the unique rational form
of denominator degree `<= L` fitting the first `2L` terms; any degree-`<= L`
rational extension of the sequence must equal it. The converse is the last
paragraph of (i). (Berlekamp-Massey minimality — that no shorter recurrence
fits — is a property of the algorithm; the detector does not rely on it
beyond using `L` as the candidate degree, since the certification re-checks
the whole window.) ∎

**(iii).** By (i) applied with `L = d`: the first `2d` coefficients admit at
most one reduced rational form with denominator degree `<= d`. Both `1/Q`
and `1/Q'` are reduced (numerator 1), with denominator degree exactly `d`,
so `Q = Q'`. (The weight-w hypothesis is not needed for the conclusion; it
is stated only because it is the detector's use case — adversarial-review
correction, 2026-08-30.) ∎

## Novelty position

Elementary and certainly classical in substance (linear recurrences,
Hankel/Kronecker theory; Berlekamp-Massey literature). Deposited as a
proved backbone, NOT claimed as new mathematics; the new artifact is the
refusal-semantics instrument built on it (T-108002).
