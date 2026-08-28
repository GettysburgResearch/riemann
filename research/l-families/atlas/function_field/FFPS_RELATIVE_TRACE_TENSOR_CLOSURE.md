# The centered native relative trace is a bounded signed tensor assembly

Status: **exact trace-level transport of the cyclic relative identity through
common linear cleanup; exact finite signed external-product formulas for the
coprime square, literal atomic diagonal, and Wick-centered difference; no
constructible one-place descent, uniform Betti/trace estimate, principal
binding, RH, or GRH**

Architecture: **Architecture B only**.

Bounded replay:
[`ffps_relative_trace_tensor_closure.py`](ffps_relative_trace_tensor_closure.py).
Canonical fixture:
[`ffps_relative_trace_tensor_closure.json`](ffps_relative_trace_tensor_closure.json).

Frozen inputs are the relative-first Adams and phase-externalization packets
at PR #760 head `680be76bd31acdd96925d0b73f1a469226a19c9f`, the all-`k` centered cyclic
identity at PR #757, and the native Mellin-polarized bilateral normal form
`L-106093/L-106120` at PR #751.

## 0. Outcome

The previous route left

```text
NATREL -> RELPARTFROB -> RELTRACE -> PRINCIPAL BINDING -> RH.
```

Two statements were hidden inside `NATREL`: finite trace algebra and geometric
descent.  The first is exact; the second remains open.

For every cyclic source fibre and arbitrary coefficients, the frozen theorem
proves

\[
 P^\circ={1\over k}\sum_{j=0}^{k-1}O_j^\circ
 -\sum_{r=1}^{k-1}|c_r|^2H_r^\circ.
\tag{0.1}
\]

Since (0.1) holds after any common restriction or common linear change of the
source coefficients, signed outer recombination preserves it.  Call this
finite trace-function theorem

\[
\boxed{\mathrm{TRACE\mbox{-}NATREL}.}
\tag{0.2}
\]

At fixed native labels the Mellin-polarized bilateral member has form

\[
 S(A,B)=\sum_{(c,d)=1}{A(c)B(d)\over cd},
\tag{0.3}
\]

where the one-sided amplitudes already carry the Boolean, owner, shell,
carrier, marked-prime, renewal, and endpoint labels.  The predecessor proves
phase externality and the first-order coprimality formula.  Here squaring and
normal ordering are externalized exactly:

\[
\boxed{
 |S(A,B)|^2=\sum_{m,n\ge1}{\mu(m)\mu(n)\over m^2n^2}
 L_{m,n}(A)R_{m,n}(B),}
\tag{0.4}
\]

where

\[
 L_{m,n}(A)=\sum_{u,v}{A(mu)\overline{A(nv)}\over uv},\qquad
 R_{m,n}(B)=\sum_{u,v}{B(mu)\overline{B(nv)}\over uv}.
\tag{0.5}
\]

The outer absolute mass is at most `zeta(2)^2`.

The literal atomic diagonal

\[
 D(A,B)=\sum_{(c,d)=1}{|A(c)|^2|B(d)|^2\over c^2d^2}
\tag{0.6}
\]

has the exact tensor expansion

\[
\boxed{
 D(A,B)=\sum_{q\ge1}{\mu(q)\over q^4}
 \left(\sum_u{|A(qu)|^2\over u^2}\right)
 \left(\sum_v{|B(qv)|^2\over v^2}\right),}
\tag{0.7}
\]

with outer absolute mass at most `zeta(4)`.  Hence

\[
 :|S|^2:=|S|^2-D
\tag{0.8}
\]

is a **finite signed tensor span** with horizon-independent projective outer
cost.  Call this `COPRIME-WICK-EXT`.  The common-square coefficient `g^-2`
adds only a further `zeta(2)` cost.

The route is therefore sharpened to

```text
TRACE-NATREL                 [PROVED]
PHASE-EXT                    [PROVED IN PREDECESSOR]
COPRIME-WICK-EXT             [PROVED]
ONEPLACEWEIL                 [OPEN]
ONEPLACETRACE / RELTRACE     [OPEN]
PRINCIPAL-BINDING            [OPEN]
-> RH.
```

This is **not a uniform Betti theorem**.  It removes the explicit bivariate
phase/coprimality/Wick obstruction and leaves one-place descent, one-place
uniformity, signed conductor recombination, and exact principal binding.

## 1. Trace-level relative transport

Apply (0.1) separately after every common source restriction and multiply the
resulting equality by the signed outer source coefficient.  Summing proves

\[
 \sum_\lambda w_\lambda P_\lambda^\circ
 ={1\over k}\sum_{\lambda,j}w_\lambda O_{\lambda,j}^\circ
 -\sum_{\lambda,r}w_\lambda|c_{\lambda,r}|^2H_{\lambda,r}^\circ.
\tag{1.1}
\]

No positivity or fibrewise absolute value is used.  This is the exact finite
trace realization that a future relative Weil object must carry.

## 2. Coprime square and diagonal

Insert

\[
 1_{(c,d)=1}=\sum_{m\mid c,\ m\mid d}\mu(m)
\tag{2.1}
\]

into (0.3), write `c=mu,d=mv`, and obtain the first-order external product.
Multiplying it by its conjugate gives (0.4).  Applying (2.1) instead to (0.6)
gives (0.7).  All rearrangements are finite on the native horizon.

Thus Wick subtraction preserves rather than destroys externality.  The
source diagonal is not ignored: it is transported with its exact coefficient
and subtracted after its own tensor expansion.

## 3. Updated geometric interface

The frozen source packages the named Boolean, owner, shell, carrier,
marked-prime, renewal, and endpoint labels inside the one-sided Mellin
amplitudes before the family square.  Therefore the remaining geometric gate
can be stated one-sidedly:

```text
ONEPLACEWEIL:
  Each complete one-sided amplitude, including its least-prime, owner,
  Boolean, shell, carrier, renewal, endpoint, and Adams data, is the trace of
  a compatible constructible class on one fixed closed-point space, with
  presentation and conductor bounds uniform in degree and horizon.
```

If `ONEPLACEWEIL` and a compatible uniform one-place trace estimate hold on
both sides, formulas (0.4) and (0.7), the phase externalization, and
closed-point Adams inversion may be applied termwise.  The `m,n,q,g` sums
have fixed zeta costs; the conductor and principal source sums must retain
their signs.

## 4. Scope firewall

- `TRACE-NATREL` is a trace-function theorem, not an isomorphism of complete
  native Weil complexes.
- `COPRIME-WICK-EXT` does not prove one-sided constructibility or uniform
  cohomological bounds.
- The zeta costs pay only the auxiliary `g,m,n,q` sums, not a
  conductor-sized direct sum of place labels.
- Equal-product and repeated-label terms remain at their inherited cleanup
  scope.
- A genuinely mixed residue phase would still trigger the predecessor's rank
  firewall.

**No ONEPLACEWEIL, ONEPLACETRACE, RELTRACE, PRINCIPAL-BINDING, RH, or GRH is
proved.  RH and GRH remain unproved.**

## 5. Proof ledger

| statement | grade |
|---|---|
| centered cyclic identity | **IMPORTED EXACT** |
| preservation by common restrictions/signed recombination | **PROVED EXACT** |
| squared coprimality formula | **PROVED EXACT** |
| literal diagonal formula | **PROVED EXACT** |
| fixed projective outer costs | **PROVED** |
| `TRACE-NATREL` | **PROVED AT FINITE TRACE-FUNCTION LEVEL** |
| `COPRIME-WICK-EXT` | **PROVED EXACT** |
| ONEPLACEWEIL / RELTRACE / principal binding | **NOT PROVED** |
| RH / GRH | **NOT PROVED** |

## 6. Bounded replay

```text
python -B research/l-families/atlas/function_field/ffps_relative_trace_tensor_closure.py --check
python -B -O research/l-families/atlas/function_field/ffps_relative_trace_tensor_closure.py --check
python -B -m unittest tests.test_ffps_relative_trace_tensor_closure
python -B -O -m unittest tests.test_ffps_relative_trace_tensor_closure
```
