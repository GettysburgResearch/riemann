# Research report — fixed-window CRT jet selectors

Date: 2026-08-23

Branch: codex/105100-residue-second-moment

Checkpoint base: 75bf12b76014da6ea983ac1dc8083aaac79132ce

## Outcome

Checkpoint 5 identified the right multiplicity-aware jet carriers but left
their global observability open. Checkpoint 6 supplies an exact identity on
every regular finite window once the complete denominator-event manifest is
known.

The construction uses the actual post-cancellation pole orders from
L-105103. A finite primary CRT selector moves only the leading target jet to
residue degree and vanishes to the full pole order everywhere else. Separate
selectors are necessary for the first and second quotients.

## Binding distinction

At a flat order-\(r\) turn, the leading \(Q\)-coefficient is \(\rho^2/r\).
The second selector therefore needs the factor \(r\). For \(x^4-1\), the
correct second charge is \(1/16\); omitting the factor three gives \(1/48\),
the ordinary \(Q\)-residue is \(-1/24\), and squaring the first weighted flux
has residue zero.

The simple cubic independently shows why all nontarget poles must be killed:
its unweighted \(Q\)-charge is \(2/9\), while the selected jet second moment
is \(5/18\). The reduced second selector \(x^2\) annihilates the
\(F''\)-only pole at zero.

The symmetric fixture \(F=z-z^5/5\) exercises partial cancellation rather
than the removable/raw extremes. At zero, \((m,r,s)=(1,0,3)\), so
\(d_1=0\) but \(d_2=1\); the real/even second selector kills the remaining
\(-1/4\) residue while preserving the targets at \(\pm1\).

## Polynomial corollary

Square-free multiplicity decomposition of \(f'\), modular inversion, and CRT
construct coefficient-level first and second carriers without finding roots.
Their logarithmic-derivative traces sum all odd-stratum algebraic embeddings.
Nonreal algebraic squares may make the total second trace negative, so this
corollary is not presented as an automatic real-window moment.

The nonlinear stratum \((x^2-1)^3\) makes the normalization
\((A_r')^r\) observable: replacing it by \(A_r'\) changes the carriers by a
factor four.

## Exact verification

    PASS_T105105_FIXED_WINDOW_CRT_JET_SELECTORS
    16/16 normal
    16/16 optimized
    3edde4fdb651ae0c3781e4f832884f0d7c81247edd3b5a151c6b2c54f051cf05

No heavy computation was run.

## Remaining frontier

For Xi derivatives the exact selector exists conditionally, but its inputs
and analytic cost are still open: event-manifest construction, selector
degree/coefficient/boundary norm, weighted edge estimates, multiplicity
defect, and cofinal-window stability. No RCMV104530 or RH conclusion is
claimed.
