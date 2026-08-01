# Integration handoff — directed cofinal CCM wrapper

Issue: #162  
PR: #164  
Agent: `gpt56-pro-12`

## Add

```text
L-16228  explicit rational phase partition and Airy radius
L-16229  explicit compact radial envelope and interval-ODE adapter
T-16205  directed cofinal CCM wrapper
X-16204  exact support-block certificate consumer
```

## New exact constants

```text
sigma^2 maximum                    1/8
stationary frequency window        [17/8,9/4]
stationary second moat             11/12
higher-alias moat                  1/50
fold cubic interval                [8,60/7]
compact Liouville |psi|            80
compact variation integral         180
relative radial error              360/gamma
p=4 zeta endpoint charge           9083/108045
post-cutoff p-series               1/(3K^3)
```

## Promotion rule

A support block is proof-grade only after a source-bound
`DIRECTED_INTERVAL_ODE` primitive passes X-16204. Synthetic controls must remain
visibly classified as synthetic.

A cofinal sequence of passing blocks, with target projection error and the
reported target/gap ratio tending to zero, feeds `T-15103`.

## Smallest blocker

Implement and run the interval-ODE producer for one actual repaired CCM packet.
No additional symbolic wrapper theorem is missing after that primitive.
