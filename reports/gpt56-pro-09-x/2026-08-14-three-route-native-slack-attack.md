# Three-route native-slack attack after the factor-67 proposal

Authoring agent: `gpt56-pro-09-x`  
Date: 2026-08-14  
Status: **new exact reductions plus one load-bearing correction; RH unproved**

## Executive verdict

The newest live input, PR #473 at
`13ad1fdbf06edc931dc0c524327b701c5c8f86a3`, materially improves the native
producer.  Its compact root claims reproduce correctly:

```text
minimum equality state L        0.3186174007676585... >159/500;
minimum reserve state R         sqrt(2)-1 >2/5;
minimum target-Hall prefix       0.3593176605985002... >7/20;
C_67 mismatch constant           18.471726914982252... <19;
interior constant                5655/32 =176.71875 <177;
recursive coefficient mass       <1/sqrt(67)<1/8.
```

The current packet nevertheless contains a false or misnormalized concluding
step.  A native-feasible row always satisfies

\[
 \mathcal H(d_X)\le J_\Lambda(X).
\]

But PR #473 states

\[
4\sqrt X-\mathcal H(d_X)=O(1).
\]

Since the proposal claims to imply RH, the RH explicit formula would then give

\[
J_\Lambda(X)=4\sqrt X-\kappa_0\log X+O(1),
\qquad\kappa_0>0,
\]

contradicting native feasibility.  This is recorded in `R-19882`.

The source-owned factor-67 construction can still be salvaged.  The correct
recursive quantity is the exact native slack

\[
\Delta_X=J_\Lambda(X)-\mathcal H(d_X)
       =\langle Y_4,s_X\rangle.
\]

I developed three simultaneous closure routes around that object.

## Route A — exact native slack cocycle

Suppose the finite root packet partitions the native detail capacity as

\[
 \Omega_X
 =\Xi(c_X)+r_X+
  \sum_b\alpha_bU_b\Omega_{Y_b},
 \qquad r_X\ge0.
\]

After inserting recursively feasible child rows, the parent slack is exactly

\[
 s_X=r_X+
 \sum_b\alpha_bU_bs_{Y_b}.
\]

Same-index covariance gives the scalar equality

\[
 \Delta_X
 =\delta_X+
  \sum_b\alpha_b\Delta_{Y_b},
 \qquad
 \delta_X=\langle Y_4,r_X\rangle.
\]

Thus a local bound

\[
 \delta_X\le A+B\log(2X)
\]

and `sum alpha_b<1/8` imply

\[
 \Delta_X=O(\log X)=o(\log^2X).
\]

This closes the resident endpoint consumer without comparing the physical row
to `4 sqrt(X)` and without normalizing by a growing target mass.

The exact PR #473 review target is now only:

```text
F67-NRS:
  reconstruct the common-parent vector identity;
  expose the literal nonnegative root slack r_X;
  prove its Y4 cost is O(log X);
  retain one-use ports and source labels.
```

The local root Hall, first-owner rough partition and compact constants are
strong evidence, but `F67-NRS` still requires independent reconstruction.

## Route B — depth graph-Gram completion

The radial route formerly asked for one measurable model contraction at almost
every depth or for every rational interval.  `L-19883` reduces that selection
problem to one graph-core theorem.

For source, model and auxiliary depth operators, prove the four blocks

\[
 K_{\rm src}^{ij}
 =K_{\rm model}^{ij}+K_{\rm aux}^{ij},
 \qquad i,j\in\{0,1\}.
\]

These are the Gram kernels of the feature vectors and their first depth
images.  They construct an isometry of operator graphs and force

\[
(D_{\rm model}\oplus D_{\rm aux})W=WD_{\rm source}.
\]

Resolvent covariance then gives all Borel spectral projections.  A diffuse
source cannot feed a positive-depth model eigenspace, so every crossed-zero
hyperbolic atom vanishes.

The new concrete target is `DGGC_a`, the `2 x 2` depth graph-kernel
factorization.  Its raw ingredients already exist:

```text
prime native/radial columns;
eta and bridge radial derivatives;
gamma Hellinger score;
completed Xi radial logarithmic derivative;
de Branges--Weyl model derivative bridge.
```

The load-bearing unknown is the positive `(1,1)` defect after the base and
mixed graph blocks are frozen.

## Route C — passive string carried by native slack

For any coherent native-feasible family, put

\[
\delta(x)=\Delta(e^x)\ge0.
\]

Then

\[
\widehat\Delta(a)=\int_0^\infty e^{-ax}\delta(x)dx
\]

is completely monotone, and every derivative Hankel matrix is PSD.  A second
Laplace transform gives

\[
 \mathscr S_a(q)
 =\int_0^\infty
   \frac{e^{-ax}\delta(x)}{q+x}dx,
\]

an explicit Stieltjes function.  Its measure is the primal certificate for all
finite passive-string moment cones and both truncated Hankel tests.

The native benchmark has the exact transform

\[
 \int_0^\infty e^{-ax}J_\Lambda(e^x)dx
 =-a^{-2}\frac{\zeta'}{\zeta}(a+1/2).
\]

Therefore the native producer already splits the safe prime logarithmic
derivative into a realized-row transform and a completely monotone unused
capacity transform.

The remaining theorem `PSI_a` is a coefficient-one completed identification:
attach the eta, gamma/pole and bridge strings and prove that their positive
parallel sum is the safe Xi admittance.  This replaces arbitrary all-order
Hankel guessing by one explicit positive measure identity.

## Why these are the three best routes

They cover the three strongest live architectures and fail independently:

```text
A. finite native arithmetic + endpoint/Landau consumer;
B. radial Clark/Jordan source + spectral-type exclusion;
C. complete-Bernstein/passive-string Xi impedance.
```

They are linked by one source-owned slack ledger, so progress on the factor-67
common-parent packet automatically supplies the arithmetic input to all three.

## Exact status

```text
PR #473 local factor-67 compact claims               REPRODUCED
PR #473 absolute 4sqrt(X) score conclusion           MISNORMALIZED / R-19882
native detail-slack cocycle                           EXACT / L-19882
depth graph-Gram locality theorem                     EXACT / L-19883
native-defect Stieltjes string                        EXACT / L-19884
F67-NRS common-parent root slack                      OPEN / CLOSEST
DGGC_a completed Xi depth graph                       OPEN / INDEPENDENT
PSI_a completed passive source identity               OPEN / INDEPENDENT
Riemann Hypothesis                                    UNPROVED
```

No artifact in this packet is labelled a full proposal.
