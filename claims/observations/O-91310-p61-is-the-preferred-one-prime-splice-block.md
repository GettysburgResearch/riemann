# O-91310 — `P_61`, not `P_79`, is the preferred one-prime splice block

Claim ID: `O-91310`  
Status: **ROUTE OPTIMIZATION / CURRENT PREFERRED GATE**  
Created: 2026-08-12  
Depends on: `L-91342`–`L-91344`; `L-91320`  
RH status: **unproved**

## 1. The stronger terminal theorem contains a smaller useful corollary

`L-91342` proves the target-exact, score-superordinate, row-positive terminal
projection throughout

\[
 1\le x<83.
\]

Restricting to

\[
 1\le x<67
\]

gives the identical theorem after absorbing only the primes through `61`,
because no prime `67,71,73,79` can occur below the endpoint.  The next rough
prime is then `67`, still beyond the factor-54 reset scale.

The directed target-Hall margin on this smaller window is much larger:

\[
 \boxed{
 \mathcal H_{\Psi,t}(x)>0.3593
 \qquad(1\le x<67),
 }
\tag{O-91310.1}

with the least margin again at threshold `13` and the right endpoint.  The
`7/100` theorem of `L-91342` is more than sufficient; the decimal above is route
reconnaissance, not a separately promoted proof constant.

## 2. Preferred one-prime packet

Put

\[
 P_{61}=\prod_{q\le61}q.
\]

The preferred splice is now

\[
\boxed{
\begin{aligned}
 \mathscr R^{(61)}_{p,y}(j)={}&
 \sum_{d\mid P_{61}}
  \frac{\mu(d)}{\sqrt d}Q_{py/d}(j)\\
 &-p^{-1/2}
 \sum_{d\mid P_{61}}
  \frac{\mu(d)}{\sqrt d}Q_{y/d}(j),
\end{aligned}}
\tag{O-91310.2
}

with causal support, where

\[
 p\ge67,
 \qquad1\le y<67,
 \qquad2\le j\le y.
\]

The Green identity `L-91344` applies with `P=P_61`.

## 3. Complexity reduction

The change from `P_79` to `P_61` gives:

```text
terminal child window             83 -> 67;
inherited row indices             81 -> 65;
finite Boolean states          2^22 -> 2^18;
first rough prime                 83 -> 67;
rough Green inclusion error    4,194,304 -> 262,144.
```

The projective-port threshold of `L-91320` was already designed around absorbing
`59,61` and beginning the delayed renewal at `67`.  The smaller splice therefore
aligns every existing finite, Schur and scale-weighted estimate.

## 4. Exact preferred row inequality

Let `Delta_p R_(P_61)` and `Delta_p G_(P_61)` be as in `L-91344`.  The inherited
row theorem is precisely

\[
\boxed{
\begin{aligned}
0\le{}&
 \frac2{j(j-1)}\Delta_p\mathcal R_{P_{61}}(y)\\
&-\frac2{j(j-1)}
 \sum_{m=1}^{j-1}\frac1{\sqrt m}
 \Delta_p\mathcal G_{P_{61}}(y/m)\\
&+\frac{j+2}{j\sqrt j}
 \Delta_p\mathcal G_{P_{61}}(y/j)\\
&-\frac1{\sqrt{j+1}}
 \Delta_p\mathcal G_{P_{61}}(y/(j+1)),
\end{aligned}}
\tag{O-91310.3
}

for

\[
 2\le j\le y<67,
 \qquad p\ge67.
\]

The first term is positive and at least

\[
 \frac{2\log p}{j(j-1)}.
\]

All remaining row uncertainty is a finite `P_61` activation-spline packet.

## 5. Current recommendation

Use `P_61` for the proof-producing splice and retain `P_79` as an independent
stronger terminal theorem and robustness check.

```text
P_61 terminal source projection                   CLOSED BY L-91342
positive-kernel recursion after the splice         CLOSED BY L-91343
P_61 finite Green decomposition                    EXACT BY L-91344
P_61 one-prime finite-boundary inequality          OPEN / PREFERRED
P_61 one-prime target/score source splice          OPEN / RH-BEARING
Riemann Hypothesis                                 UNPROVEN
```