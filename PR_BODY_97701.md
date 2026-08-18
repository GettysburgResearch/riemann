## Publication recovery: T-97701 / C4MBI67 critical core

This is a corrective successor stacked on PR #590 at its exact live head
`4f1283c67f0d4a4b504badd4c4113ba227521162`.

The preceding PR comment announced T-97701 materials that were not actually
present on GitHub or in the published ZIP. This packet reconstructs and
publishes those materials under a fresh namespace and archive name.

**RH remains unproved.**

## Exact continuation

For the annular scalar

\[
\mathcal A_X=5[c_X(2)-c_{X/4}(2)]+3[c_X(3)-c_{X/4}(3)],
\]

let

\[
H_X(n)=\min\!\left(\log4,\log\frac Xn\right)_+
\]

and

\[
\kappa_X(n)=-6H_X(n)+\frac9{\sqrt2}H_{X/2}(n)-\frac32H_{X/4}(n).
\]

Then

\[
\mathcal A_X=6H_X(1)+\sum_{n\ge1}\frac{\mu(n)}{\sqrt n}\kappa_X(n).
\]

Writing

\[
B_{1/2}(t)=\sum_{n\le t}\frac{\mu(n)}{\sqrt n},
\]

the Möbius term is the exact four-band boundary

\[
\begin{aligned}
\mathfrak C_X={}&-\frac32\int_{X/16}^{X/8}B_{1/2}(t)\frac{dt}{t}
+\frac{9\sqrt2-3}{2}\int_{X/8}^{X/4}B_{1/2}(t)\frac{dt}{t}\\
&+\frac{9\sqrt2-12}{2}\int_{X/4}^{X/2}B_{1/2}(t)\frac{dt}{t}
-6\int_{X/2}^{X}B_{1/2}(t)\frac{dt}{t}.
\end{aligned}
\]

`C4MBI67(X)` is the exact inequality

\[
\mathfrak C_X\ge-6H_X(1).
\]

At the root endpoint the Bellman identity from T-97700 gives

```text
BLPTE67(X)
<=> U_full(X) >= 0
<=> A_X >= 0
<=> C4MBI67(X).
```

## Exact prime-Möbius owner form

For squarefree `n>1`,

\[
\mu(n)\log n=-\sum_{p\mid n}\mu(n/p)\log p.
\]

Hence

\[
\sum_{n>1}\frac{\mu(n)}{\sqrt n}\kappa_X(n)
=-\sum_{p\le X}\frac{\log p}{\sqrt p}
 \sum_{\substack{m\le X/p\\p\nmid m}}
 \frac{\mu(m)}{\sqrt m}\frac{\kappa_X(pm)}{\log(pm)}.
\]

Every squarefree source coefficient is spent exactly once through the owner
weights `log p/log n`.

## Proof boundary

```text
four-band Möbius identity                 PROVED EXACT
prime-Möbius logarithmic ownership        PROVED EXACT
BLPTE67(X) <=> C4MBI67(X) <=> A_X>=0      PROVED EXACT AT ROOT
source-blind unsigned Type-II closure      REFUTED AS A PROOF MECHANISM
C4MBI67 sign                               OPEN / RH-BEARING
Riemann Hypothesis                         UNPROVED
```

## Replay

```bash
cd experiments/X-97701-blpte-critical-core
./build_and_replay.sh
cd ../..
sha256sum -c T97701_CONTENT_SHA256SUMS
```

The fresh deterministic archive, compiled manuscript, complete TeX source and
checksum ledger are mirrored in the Riemann Research Packets Drive folder and
are named with `t97701-c4mbi67-publication-recovery`, not the old T-97700 ZIP.
