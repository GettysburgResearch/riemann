# Direct attack on `CP(K)` and exact Möbius-core decoder

Agent: `gpt56-04-f`  
Date: 2026-08-07  
Branch: `agent/gpt56-04-f/151-finsler-target-completion`  
Frozen input head: `9ee33527aef3acbb281ebad367aeb1e51652d006`  
Status: **CP(K) NOT PROVED; RH NOT PROVED**

## Executive conclusion

`CP(K)` is necessary for the high-order centered Type-II chain as currently
written. It may be replaced by a direct subexponential estimate for one exact
Möbius safe signal, but that replacement is itself RH-equivalent.

The direct attack found an exact decoder:

```text
signed truncated Heath-Brown packet before log = mu through V^K,
full packet after log                         = Lambda through V^K,
fixed log variable q=2                       = mu(m) log 2.
```

Thus high identity order does not dilute the arithmetic core. A finite packet
partition must leave at least one destination with the same upper exponential
energy exponent as the Möbius slice.

The packet construction remains useful infrastructure, but it is not ready for
scarce full-proof review while `CP(K)` is open.

## 1. Exact convolution proof

Define

\[
 A_{K,V}
 =\sum_{j=1}^{K}(-1)^{j-1}{K\choose j}
 \mu_V^{*j}*1^{*(j-1)}.
\]

With `B=mu_V*1` and `R=delta-B`,

\[
 A_{K,V}*1=\delta-R^{*K}.
\]

Because `R` is supported above `V`, `R^{*K}` is supported above `V^K`.
Therefore

\[
 A_{K,V}=\mu
 \quad(n\le V^K),
\]

and convolving with `log` gives the exact Heath–Brown identity.

## 2. Fixed logarithmic variable

Fixing the final `log` factor at `q0` leaves

\[
 \mu(m)\log q_0
\]

for every `q0 m<=V^K`. At `q0=2`, the normalized logarithmic signal is

\[
 {\log2\over\sqrt2}
 Q_{\mu,H}(x-\log2).
\]

Its Laplace transform is

\[
 {\widehat H(z)\over\zeta(z+1/2)}.
\]

A safe window has no transform zero in the open counterexample strip, so the
rightmost pole and positive energy exponent are exactly `Theta_zeta`.

## 3. Packet lower bound

If the fixed-`q0` slice is split into `R_K` destination vectors, then

\[
 \max_\tau E_{K,\tau}
 \ge E_{\mu,q_0}/R_K^2.
\]

For fixed `K`, the packet count contributes no block-scale exponent. Therefore
one packet retains the Möbius exponent.

## 4. What the direct Type-II attack did not prove

The following facts do not imply `CP(K)`:

- exact Heath–Brown coefficient reconstruction;
- fixed logarithmic scale reserve;
- zero combinatorial coefficient rate;
- null-mode centering of global polynomial companions;
- generic Cauchy, Young, Schur, or large-sieve inequalities after total
  variation.

A balanced factorization still has total logarithmic factor scale equal to the
output scale. Generic norm estimates either pay that full scale or reduce to a
critical local Möbius moment.

Current work on local moments of Möbius Fourier polynomials likewise identifies
arbitrarily high critical-scale moment bounds as equivalent formulations of RH,
not known unconditional estimates. This is consistent with the decoder above.

## 5. Correct status of the proposal

```text
L-15154 through L-15158:        proposed exact infrastructure
T-15121/T-15122:               proposed complete composition
L-15159/T-15123:               proposed exact Möbius decoder/transfer
CP(K):                         OPEN / RH-BEARING
M-15112 as a completed proof:  BLOCKED
RH:                            NOT PROVED
```

The next valid full proposal must either:

1. actually prove the Möbius-safe energy bound;
2. prove `CP(K)` with every signed packet and transition residual retained; or
3. supply an independent route not relying on this packet theorem.

## 6. Exact regression

`X-15126` checks three finite packet orders:

```text
K=2,V=5,X=25
K=3,V=4,X=64
K=4,V=3,X=81
```

In every case:

```text
A_(K,V)-mu mismatches       none
A_(K,V)*log-Lambda          none
q=2 slice mismatches        none
```

Proof digest:

```text
21a807fdd5b4fbd0fe4017816cb2660dc1bc645c52e0d8a8285eb84b72647eb1
```

Eight mutation and replay tests pass.
