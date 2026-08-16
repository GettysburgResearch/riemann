# R-94200 — The proof is arithmetic integer-sieving, not ordinary translation monotonicity

Claim ID: `R-94200`  
Status: **EXACT SCOPE FIREWALL + DETERMINISTIC COUNTERDIAGNOSTIC**  
Created: 2026-08-16  
Depends on: `L-94200` definitions  
RH status: **unproved**

## 1. What `L-94200` does not assert

After conjugation by \(\sqrt Y\), the prime operator becomes
\[
 f(x)\longmapsto f(x)-f(x-\log p).
\]
It is tempting to replace the prime logarithms by arbitrary positive shifts and
claim ordinary complete monotonicity. That strengthening is false.

Let
\[
 f_j(x)=G_j(e^x).
\]
At \(j=3\), take the noninteger dilation
\[
 a=\frac{21}{10},\qquad Y=11.
\]
The fourth repeated difference is
\[
 \sum_{\nu=0}^4(-1)^\nu\binom4\nu
 G_3(Y/a^\nu)
 <-0.18.
 \tag{R-94200.1}
\]
The retained high-precision diagnostic encloses it inside
\[
 -0.191<\text{left side of (R-94200.1)}<-0.190.
\]

Thus neither absolute monotonicity nor a generic real-shift theorem is the
mechanism of `L-94200`.

## 2. Why the prime theorem is different

Integer dilation maps every activation knot \(\log m\) to another activation
knot \(\log(am)\). For an initial prime segment, the alternating copies form
Boolean divisor cubes. Equal bulk vertices cancel exactly, and only the
finite row frontier survives.

A noninteger dilation destroys this divisor-cube ownership and the
sign-reversing cancellation.

## 3. Other forbidden readings

The following do not prove `L-94200`:

* a finite scan of \(c_X(j)\);
* local-uniform convergence of an approximant;
* positivity of ordinary responses without component-row positivity;
* positivity of each oriented Möbius child;
* the claim that the canonical \(P_{61}\) row fits native capacity;
* a benchmark estimate for \(J_\Lambda(X)-4\sqrt X\).

The theorem stands or falls on the exact frontier-chain transport.

## 4. Boundary

```text
initial segments of ordinary primes       claimed in L-94200
arbitrary real dilations                  false
finite numerical positivity               diagnostic only
branchwise child positivity               not used
full cancelled row positivity             conclusion-producing claim
Riemann Hypothesis                         not treated as established
```
