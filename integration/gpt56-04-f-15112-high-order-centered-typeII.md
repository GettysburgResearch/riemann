# Integration handoff — high-order centered packet infrastructure after the Möbius-core audit

Branch:

```text
agent/gpt56-04-f/151-finsler-target-completion
```

Frozen direct-attack input:

```text
PR #158 9ee33527aef3acbb281ebad367aeb1e51652d006
PR #216 b76eef1b769584aa9d66d082bfc6634126f986a2
```

Status:

```text
CP(K) NECESSARY FOR THIS CHAIN
CP(K) NOT PROVED
NOT READY AS A COMPLETE RH PROPOSAL
RH NOT PROVED
```

## Review order

1. `claims/lemmas/L-15159-exact-mobius-core-of-heath-brown-packet.md`
2. `claims/theorems/T-15123-mobius-safe-energy-rightmost-zero-criterion.md`
3. `claims/refutations/R-15114-cpk-is-rh-bearing-mobius-core.md`
4. `experiments/X-15126-heath-brown-mobius-core/`
5. `reports/gpt56-04-f/2026-08-07-cpk-direct-attack-and-mobius-core.md`
6. repaired `claims/methodology/M-15112-high-order-centered-typeII-full-rh-proposal.md`
7. `L-15154` through `L-15158`, `T-15121/T-15122`, and `X-15125`

## Exact new result

For

```text
A_(K,V)
 = sum_(j=1)^K (-1)^(j-1) C(K,j)
   mu_V^(*j) * 1^(*(j-1)),
```

one has

```text
A_(K,V)=mu             through V^K,
A_(K,V)*log=Lambda     through V^K.
```

Fixing the final logarithmic variable at `q0` leaves exactly

```text
mu(m) log(q0).
```

The `q0=2` signal is a translate and scalar multiple of a compact Möbius safe
signal with Laplace transform

```text
Hhat(z)/zeta(z+1/2).
```

Its positive energy exponent is the rightmost zeta-zero displacement.

If the slice is split into `R_K` destination packets, at least one self-energy
is at least `R_K^(-2)` times the Möbius energy. Finite packetization therefore
does not lower every packet exponent.

## Consequence

`CP(K)` is not optional inside `M-15112`. It may be replaced by a direct
subexponential Möbius-energy theorem, but that theorem is itself RH-equivalent.
The finite Heath–Brown, centering, partition, and composition files remain
reviewable infrastructure; they do not constitute a completed proof.

## Exact decoder regression

```text
K,V,X cases:                 (2,5,25), (3,4,64), (4,3,81)
A_(K,V)-mu mismatches:       none
A_(K,V)*log-Lambda:          none
q=2 slice mismatches:        none
tests:                       8/8 PASS
proof digest:
21a807fdd5b4fbd0fe4017816cb2660dc1bc645c52e0d8a8285eb84b72647eb1
```

## Review recommendation

Do not count this branch among active complete RH proposals until `CP(K)` or an
equally strong Möbius-energy theorem is actually proved.
