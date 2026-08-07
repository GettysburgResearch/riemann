# Integration handoff — Issue #223

## Stack

Base:

```text
PR #222 / agent/gpt56-pro-18/221-signed-semiprime-dispersion
```

Add:

```text
T-22301  prime Hardy square and critical H1 criterion
L-22301  product-scale semiprime convolution
L-22302  semiprime Sobolev sufficient condition
R-22301  standard Dirichlet-Hardy embedding misses the critical orbit
M-22301  restricted critical semiprime H1 attack
X-22301  exact convolution-square regression
```

## Main connection

The two-prime signed ratio Gram of PR #222 and the one-dimensional semiprime
signal here are Fourier/Laplace dual presentations of the same analytic square.
The new coordinate removes the factor-ratio variable:

```text
Q(x)^2 energy in frequency
<->
(Q*Q)(x) on product scale.
```

## Dependencies

`T-22301` inherits the proof status of proposed `T-21502`. It does not repair or
independently verify that parent transfer.

Primary external interfaces:

```text
Brevig, arXiv:1606.03101          standard H2 embedding at Re s=1/2
Brevig--Perfekt, arXiv:1510.02019 weak products / multiplicative Hankel forms
Bayart--Brevig, arXiv:1602.03446  embedding/composition framework
```

## Scope corrections

Do not claim:

```text
mathscr H2 membership of the prime ray
=> the required identity-orbit bound;

weak-product membership of the square
=> its local H1 trace;

time-domain L1 of the semiprime signal
<=> the Fourier H1 norm.
```

`R-22301` refutes the first two universal implications.

## Exact remaining theorem

For every rational `sigma>0`, prove

```text
integral |Hhat(sigma+it)|^2
         |P1(1/2+sigma+it)|^2 dt < infinity.
```

A stronger sufficient interface is the pair of weighted semiprime `L2`
estimates in `L-22302`.

## Candidate registry

No candidate is added. No finite computation here advances RH status.
