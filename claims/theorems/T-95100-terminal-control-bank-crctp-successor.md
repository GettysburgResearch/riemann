# T-95100 — A source-specific terminal-control bank reduces the carry route to two explicit cofinal theorems

Claim ID: `T-95100`  
Status: **COMPLETE CONDITIONAL SUCCESSOR — TWO LOAD-BEARING THEOREMS OPEN; RH UNPROVED**  
Created: 2026-08-16  
Depends on: `L-95100`, `L-95101`; PR #474 `L-93021`; PR #538 `L-95040`

Define **Fixed-Bank Terminal Control (`FBTC`)** as follows. There is a finite
set of cutoff policies `B` such that, for every sufficiently large endpoint
`X`, two members of `B` have nonnegative root-completed occupations and their
terminal parameters bracket zero.

By `L-95101`,

\[
\boxed{\mathrm{FBTC}\Longrightarrow\mathrm{CRCTP}.}
\tag{T-95100.1}
\]

The exact root-completion theorem on PR #474 then localizes all optimized Cycle
Debt to the dyadic root scalar

\[
\mathcal R_2(X)
=\sum_{q\le X}{b_2(q)\over\sqrt q}\log{X\over q},
\tag{T-95100.2}
\]

namely

\[
\mathfrak N_X={1\over2\sqrt2}[\mathcal R_2(X)]_+.
\tag{T-95100.3}
\]

Thus FBTC plus the independent one-sided estimate

\[
[\mathcal R_2(X)]_+=X^{o(1)}
\tag{T-95100.4}
\]

would give Cycle Debt, the sharp prime ramp, and RH through the resident
Mellin–Landau consumer.

The successor is materially sharper than a generic adaptive-policy problem:

```text
transverse positivity -> finite terminal controller with exact mod-12 drops;
principal obstruction -> one explicit zero-safe dyadic scalar.
```

Neither FBTC nor (T-95100.4) is proved here. The finite replay proves the bank
through endpoint `1024`; it does not establish the unbounded quantifier.
