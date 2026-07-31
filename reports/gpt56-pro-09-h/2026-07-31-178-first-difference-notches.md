# First-difference notch continuation

The first five-notch prime candidate on PR #184 closed at the selected-zero plus
trivial-zero scale; its old discrepancy was numerical. The next search should
not simply add more box-square notches. Those filters suppress a selected line
zero quadratically but also insert a high-frequency denominator squared and cost
`2r` in support.

The normalized first difference

```text
(G(u)-G(u-r))/2
```

is the unique maximal two-tap notch whose coefficient `l1` norm is one. It keeps
all shell and derivative tail budgets unchanged, costs only `r` in support, and
responds linearly to a horizontal zero displacement. At the published verified
height, replacing all five old notches improves the guaranteed transform response
by more than `4.5e115`; one conservative replacement already gains about `1e23`.

Ordinary first-100-zero reconnaissance recommends the zero-4 hybrid for minimum
RMS and zero-3 hybrid for slightly better guaranteed sensitivity. These are
scheduling observations only. The proof-grade next step is the same finite
phase-band comparator already implemented in PR #181.
