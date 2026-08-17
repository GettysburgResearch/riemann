# L-97203 — The smallest exact Markov repair is the future-prime quotient profile

Claim ID: `L-97203`  
Status: **PROVED EXACT FINITE-STATE RECURRENCE; ALL-SCALE INVARIANT OPEN**  
Created: 2026-08-18  
RH status: **unproved**

Fix a horizon `N`. For a finite odd-prime set `P`, put

\[
\mathcal B_P(x)=\sum_{n\le x}\frac{b_P(n)}{\sqrt n}.
\]

Adding a prime gives

\[
\boxed{
\mathcal B_{P\cup\{p\}}(x)
=\mathcal B_P(x)-p^{-1/2}\mathcal B_P(\lfloor x/p\rfloor).
}
\tag{L-97203.1}
\]

Thus one boundary value is not a closed state. The exact finite Markov closure is the quotient profile

\[
\boxed{
\mathbf B_P^{(N)}(m)
=\mathcal B_P(\lfloor N/m\rfloor).
}
\tag{L-97203.2}
\]

Only `O(sqrt N)` different values occur. Prime addition is an upper-triangular linear map on this finite quotient DAG.

Order the missing primes in descending order and let `P_{>p}` contain the already-installed primes larger than `p`. The one-step boundary slack is

\[
\boxed{
\mathcal S_p(x)
=1-\mathcal B_{P_{>p}}(x)
 +p^{-1/2}\mathcal B_{P_{>p}}(\lfloor x/p\rfloor).
}
\tag{L-97203.3}
\]

If

\[
\boxed{
\mathrm{FCBI}:\qquad \mathcal S_p(x)\ge0
}
\]

holds for every descending prime step and every quotient coordinate, then the full all-prime state satisfies RJTE.

`R-97200` proves that the child coordinate cannot be removed from the state. In this precise Markov sense, the future-prime child port is the smallest additional variable exposed by the exact recurrence.

The directed verifier proves FCBI for every descending prime stage and every `x<=8192`. Its smallest nontrivial certified slack is positive. This is an exact finite diagnostic, not an all-scale theorem.
