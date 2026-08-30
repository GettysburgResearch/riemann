# T-104510 — Hermite–Biehler last-defect frontier for Xi

Claim ID: `T-104510`  
Status: **UNCONDITIONAL STRUCTURAL THEOREMS + TWO-GATE RH REDUCTION**  
Created: 2026-08-22  
Base: PR #716 at `a1d2387c4a1416c3f220a16fae849e6eab620545`  
RH status: **unproved**

## Unconditional results

1. For every real polynomial `p`,
   \[
   N_-(p-i\lambda p')=N_{\rm nr}(p)/2.
   \]
2. A real-rooted derivative has a real-rooted antiderivative exactly when the
   native integration constant lies in one explicit critical-value interval.
3. The Laguerre defect is the boundary phase velocity of the
   Hermite–Biehler companion.
4. Every derivative of Xi remains inside the classical horizontal strip
   `|Im z|<=1/2`.
5. High Xi derivatives have a zero-free Hermite–Biehler companion on every
   growing box satisfying
   \[
   T_n=o(\sqrt{n/\log n}).
   \]
6. The cumulative `RPCH104501` charge is exactly the off-real zero count and is
   therefore not an independent producer.
7. A single nonnegative Laguerre inequality is not enough; `R-104511` gives an
   exact cubic counterexample.

## Correct frontier

For each fixed height, start from the high derivative companion of
`L-104514` and descend until the last derivative carrying a lower-half-plane
zero. At that level, `L-104515` proves that exactly one of two explicit events
must occur:

```text
PRES104515  positive derivative-ratio residue / wrong extremum;
VFLUX104515 inward vertical Hermite–Biehler index flux.
```

Hence

\[
\boxed{
\mathrm{PRES104515}
\ \wedge\
\mathrm{VFLUX104515}
\Longrightarrow
\mathrm{RH}.
}
\tag{T-104510.1}
\]

Neither exclusion theorem is proved here.

## Why this is a stronger research reduction

The old route asked for a cumulative integer charge below two, which was the
desired zero count itself. The new route asks for the exclusion of one *last
event* at one derivative level. It is compatible with:

- Pick-kernel negative-index estimates;
- the exact antiderivative interval;
- high-derivative saddle asymptotics;
- verified-height or zero-density information;
- direct vertical-side asymptotics.

No charge is spent at several derivative levels, and no global zero percentage
is treated as a local theorem.

```text
PRES104515     OPEN / RH-BEARING
VFLUX104515    OPEN / RH-BEARING
RH             UNPROVED
```
