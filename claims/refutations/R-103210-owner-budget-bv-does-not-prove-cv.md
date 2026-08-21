# R-103210 — Owner-budget bounded variation does not prove literal collar variation

Claim ID: `R-103210`  
Status: **PROVED SOURCE-TRANSFER FIREWALL**  
Created: 2026-08-20  
Depends on: `L-103210`  
RH status: **unproved**

At the activated-coefficient scope, the adaptive choice \(Z=X^{9/10}\) has the
event ledger

```text
X=p:          +1/p   (enter unsquared collar)
X=p^(10/9):   -1/p   (leave collar)
X=p^2:        +1/p^2 (enter squared active core).
```

Its total coefficient variation is \(O(\log\log X)\).

This does not control the physical scalar.  At a cutoff crossing the actual
source jump is

\[
p^{-1/2}S_p\mathscr A_{p^-}F.
\]

For the homogeneous critical carrier \(F(X)=\sqrt X\),

\[
p^{-1/2}S_pF(X)=\frac{\sqrt X}{p}.
\]

At \(X=p^{10/9}\), this equals \(p^{-4/9}\), whose prime sum is power-sized.

The centered critical packet removes this homogeneous carrier, but the example
proves the implication firewall:

\[
\boxed{
\text{coefficient budget BV}
\not\Longrightarrow
\text{literal source-transfer BV}.
}
\]

After carrier subtraction, the remaining transfer packet is exactly the
conclusion-bearing activation/collar channel.  Its one-sided variation still
requires an arithmetic estimate.
