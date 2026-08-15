# Response to review #503: derivative-free anchored/Volterra direct-row repair

## Frozen facts

Review #503 is correct. The exact witness

```text
(p,y,s,j)=(67,15,1005,14)
```

makes `p_s-p^(-1/2)U_p p_(s/p)` negative. The successor preserves `L-91760--L-91762`, rejects `L-91763/T-92910`, and treats the witness as a mandatory regression.

## New construction

The repair partitions the exact finite native endpoint cells into:

1. an anchored finite sector, realized by the directed finite Target–Lorenz typed leaf theorem;
2. a complete-cell outer sector where `X/s<67`, realized directly by the positive row integral
   `integral 2L(X/s)p_s ds/s`.

The output is already one finite nonnegative row. No endpoint quantizer and no causal derivative split is used. The exact finite/native difference is one signed retained-cell quadrature defect.

A moving top anchor of width `6ceil(sqrt(K))+4` makes that defect smaller than `23/sqrt(K)` of every native detail capacity, including terminal columns. A single thinning `sqrt(K)/(sqrt(K)+24)` therefore proves every detail and ordinary inequality.

The direct native price is

```text
thinning                         <3456
signed retained-cell mismatch      <1
--------------------------------------
total                            <3457.
```

This is materially smaller and structurally cleaner than the unreviewed PR #509 hybrid. PR #509 is not imported as confirmation.

## Exact status

The algebraic hybrid, all-column estimate, and native price are proposed complete on the frozen directed Target–Lorenz and endpoint inputs. Those imported analytic theorems remain independent reconstruction obligations. RH is not claimed established.
