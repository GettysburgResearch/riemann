# O-15105 — Central `xi` Stieltjes--Hankel reconnaissance

Claim ID: `O-15105`  
Status: **ORDINARY HIGH-PRECISION RECONNAISSANCE; NOT DIRECTED**  
Authoring agent: `gpt56-04-f`  
Created: 2026-08-01  
Dependencies: `T-15110`  
Scope: nominate the first proof-grade central-moment calculation  
Related counterexample candidates: none

## 1. Moments

Using 60-decimal `mpmath` differentiation at the center, with

\[
 \log\frac{\xi(1/2+w)}{\xi(1/2)}
 =\sum_{m\ge1}c_mw^{2m},
 \qquad
 s_{m-1}=(-1)^{m-1}m c_m,
\]

the first six midpoint values are

```text
s0 = 2.31049931154189707889338104303e-2
s1 = 3.71725992852696861648662624717e-5
s2 = 1.44173931400973279695381556095e-7
s3 = 6.63031680252990869873272081961e-10
s4 = 3.21366415061660121610211659983e-12
s5 = 1.58769345149101535189828388084e-14
```

The numerical imaginary residuals were between `1e-64` and `1e-68` and were
discarded as differentiation noise.

## 2. First Hankel determinants

The ordinary and shifted determinants are

```text
r=1:
  det H  = 2.31049931154189707889338104303e-2
  det H+ = 3.71725992852696861648662624717e-5

r=2:
  det H  = 1.94933555481914221473987821917e-9
  det H+ = 3.86048846787093841952413095008e-15

r=3:
  det H  = 2.17281051052624677495651744858e-22
  det H+ = 3.11996028999615295242929725598e-31
```

All are positive at the midpoint.  Their rapid shrinkage shows that a
proof-grade ladder should use interval `LDL^T`, scaling, and independent
precision nesting rather than raw determinants.

## 3. Interpretation

By `T-15110`, positivity at every order is equivalent to RH.  These six moments
therefore provide only a low-order control and no global evidence beyond the
already known finite tests.

They are nevertheless a compact production target for the existing Arb central
`xi` backend:

1. emit balls for `log xi` through order twelve;
2. reconstruct `s0,...,s5` independently;
3. certify the two `3 x 3` Hankel matrices by directed `LDL^T`;
4. extend the ladder until conditioning or a sign obstruction appears.

A finite positive ladder is not a proof. A strict negative Hankel direction is
an unconditional RH counterexample.
