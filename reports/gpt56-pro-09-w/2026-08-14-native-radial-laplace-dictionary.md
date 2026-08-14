# Native endpoint ramps are the Laplace coordinates of the prime radial source

Agent: `gpt56-pro-09-w`  
Date: 2026-08-14  
Status: exact new source-lock theorem and conditional completion packet; RH unproved

## Frozen scientific inputs

```text
PR #202  5656091917835721e6f08cfb4e0fece72aaa9828
PR #404  ab71aa1fe0b1fd192011bbf40f032d2f42889ea0
PR #427  e4cba612839efb7296c1664f173e924f9e252bbf
PR #430  cedf2f5b43c99d6e6f9a760236432b123dd91770
PR #435  42a6929df3b637a151a2612b977fcabd2e774599
PR #468  a41f81466f85d52597c97b41505756a8860698d0
PR #470  89af3206ea1894884613e1188b5ab9a6a4cd74f0
```

## Main identity

For

```text
w_X(q)=q^(-1/2) log(X/q) 1_(q<=X),
x=log X,
lambda=sigma+2r-1/2>0,
```

one has exactly

```text
lambda^2 int_0^infinity exp(-lambda x) w_(exp x)(q) dx
 =q^(-(sigma+2r)).
```

After multiplication by `2 Lambda(q)`, this is the coefficient of the prime
radial Clark innovation on PR #430.

Therefore any atomwise source-owned use of native capacity transforms into an
atomwise source-owned use of radial prime capacity, and every unused native
coefficient transforms into an explicitly nonnegative radial coefficient.

## Consequences

1. The prime native-to-radial source lock is explicit rather than an abstract
   common-column hypothesis.
2. Radial interval refinement and carrier polarization are automatic because
   every source occurrence uses the same prime-power column
   `1-exp(-it log q)`.
3. The radix-four slack of PR #470 produces ordinary slack through the positive
   inverse `R_4`, and hence positive radial slack.
4. The native entropy debt is the exact Laplace budget of the total prime radial
   slack.
5. The entire `Y_4=0` triangular repair cone is a radial null gauge: it can
   repair the physical native row without changing any prime radial coefficient.
6. Eta, bridge, gamma/pole, reflected and compressed-delay channels append by
   direct sum from the existing positive arithmetic source construction.

## Correct boundary

The theorem does not prove `SONTR`, and it does not allocate the complete model
measure into the resulting source columns. The remaining model theorem is one
radially decomposable contraction `NRMA_a`.

Accordingly this work is not presented as an unconditional full proposal. It is
an exact source-interface advance plus a conditional completion packet.
