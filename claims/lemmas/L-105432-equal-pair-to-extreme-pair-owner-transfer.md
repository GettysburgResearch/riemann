# L-105432 — Equal Duhamel pair ownership and extreme-pair ownership are source-exact gauges

Claim ID: `L-105432`

Status: **PROVED EXACT OWNER-GAUGE TRANSFER WITH POLYLOGARITHMIC FREE COST**

PR #719 assigns a squarefree occurrence \(S\) of labelled depth \(k\ge2\)
equally to its \(\binom{k}{2}\) unordered pairs.  If its complete signed
physical vector is \(v_S\), each pair receives

\[
\binom{k}{2}^{-1}v_S.
\]

Fix a total order on labelled prime occurrences; the two copies of \(67\)
remain distinct under a tie-break.  Define the extreme owner

\[
P_{\rm ext}(S)=\{\min S,\max S\}.
\]

Transfer every equal-pair share of this occurrence to \(P_{\rm ext}(S)\).

## 1. Source and physical invariance

The transferred coefficient at the extreme pair is

\[
\sum_{P\subset S,\ |P|=2}
\binom{k}{2}^{-1}v_S
=
v_S.
\]

Therefore

\[
\boxed{
\text{equal-pair source sum}
=
\text{extreme-pair source sum}
}
\tag{L-105432.1}
\]

coefficient by coefficient and before physical collapse.  The integer product,
activation side, homotopy time, ray coordinate and source sign are unchanged.

## 2. Exact owner-space cost

For one occurrence, the equal-pair free norm is

\[
\sum_P
\left\|
\binom{k}{2}^{-1}v_S
\right\|^2
=
\binom{k}{2}^{-1}\|v_S\|^2,
\]

whereas the extreme-pair norm is \(\|v_S\|^2\).  The exact gauge cost is

\[
\boxed{\binom{k}{2}.}
\tag{L-105432.2}
\]

On the physical horizon \(n\le16Y\),

\[
k
\le
\frac{\log(16Y)}{\log2}+1,
\]

so the transfer costs at most \(O(\log^2Y)\), which is harmless relative to a
subpower target.

## 3. Interval geometry

After the repeated-label sector is charged to its already-closed ledger, an
extreme pair consists of two distinct numerical primes \(p<q\), and every
remaining prime label of the occurrence lies strictly between \(p\) and \(q\).
Thus the hard pair source is placed in the exact endpoint/interior geometry of
the double-owner interval and compensated-prefix programmes.

This theorem does not claim that a sign theorem for one detector automatically
transfers to the filtered outer-ray detector.  It supplies the missing
source-exact owner gauge needed to attempt that kernel comparison without
changing coefficients.
