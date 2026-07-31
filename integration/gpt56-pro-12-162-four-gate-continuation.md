# Integration handoff — Issue #162 four-gate continuation

## Add

```text
R-16202  raw prolate tails are not L2; use exact-radical two-packet
L-16210  fold-admissible local Weyl scalarization
T-16202  corrected repaired two-profile source transfer
T-16203  energy angle closes floor and coupling gates
L-16211  generic-support finite source surjectivity
L-16212  single-alias radial phase window and Gram separation
T-16204  growing tail frame closes all global gates
L-16213  quadratic-log Fourier cutoff for the Xi source
L-16214  consecutive-triple exact-radical frame
X-16202  exact repaired-packet, energy-angle, scalarization, and frame controls
```

## Replace the original gate 1

Do not search for ordinary L2 profiles of the four raw modes

```text
0,4,8,12.
```

Poisson summation leaves nonintegrable source-functional correction terms. Use
the two-dimensional kernel of

```text
q^T c=0,
ell^T c=0
```

inside these four modes. The repaired target and one repaired complement form
the production packet.

## Replace gates 2 and 4

Do not budget a global floor and an absolute cross norm independently. Whiten by
the production Gram and certify the relative factorization

```text
X=S^(1/2) C B^(1/2),
||C||<1.
```

This gives the global floor, target-floor excess, complete target-complement
gap, and target/background dual correction in one exact Schur certificate.

## Reinterpret gate 3

At generic circle length the projected exact arithmetic-source range equals
every finite Fourier space. There is no algebraically separate background.
Gate 3 is a quantitative growing source-frame theorem.

Use the consecutive-triple frame

```text
w_j=(1-r_j)e_j-e_(j+1)+r_je_(j+2),

r_j=(d_(j+1)-d_j)/(d_(j+2)-d_j).
```

It satisfies both source constraints exactly and is a small banded perturbation
of the first-difference frame. The remaining prolate input is uniform adjacent
defect separation and growing point-value control.

## Cutoff schedule

Use

```text
L=log lambda,
N_lambda=ceil(L^2),
tau_lambda->1/2.
```

The exact Xi source has exponentially decaying centered Fourier coefficients,
so this schedule closes the moving Hardy target tail. Its dimension is
`O((log lambda)^2)`, far below the radial scale `2pi lambda^2`.

## Remaining analytic theorem

Construct the polylog-dimensional exact-radical frame on a cofinal generic
support schedule and prove, in the complete omitted-tail metric,

```text
D-mu_DG>=c d_8 G on the target complement,

||D^-1/2(A-aD)D^-1/2||/a->0.
```

A sufficient radial package is:

```text
- CCM/Dunster leakage normalization;
- the single-alias profile lower bound;
- Airy-fold variation o(R);
- summable Poisson endpoint terms;
- operator-valued local Weyl error uniform over N=O(log^2 lambda).
```

These statements imply the old gates 2--4 automatically through `T-16204`.

## Candidate and proof status

No RH proof and no numerical candidate are added. The exact checkers are
synthetic regressions only. The new work narrows the positive route and prevents
computation on inadmissible raw tail profiles.
