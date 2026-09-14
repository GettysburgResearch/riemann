# R-105210 — The pressure term pays each interior gap six times

Claim ID: `R-105210`  
Status: **EXACT FIREWALL**

In a sliding family of consecutive seven-point windows, an interior gap
belongs to six windows. Therefore summing a local term
\[
c\sum_{i=1}^6g_i
\]
over all windows produces a global cost \(6c\) per interior gap, up to
endpoint terms.

Any global deduction that retains only \(c\) rather than \(6c\) is invalid.
This firewall rejects attractive strengthened constants obtained by optimizing
the local certificate while forgetting window overlap.
