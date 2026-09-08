# Six separated windows: the signed interactions are controlled

**PROPOSED COMPLETE COMPONENT PROOFS; independent review required. RH and the
original all-degree subexponential bound remain unproved.**

This is an add-only continuation of PR #792 at
`2c3184545bafb4f5d873d2fa0ffc2c335a25d048`. It retains the actual full arithmetic
kernel, including all prime powers through the inherited safe scalar at s=2.
No predecessor file or other agent's branch is changed.

## Result

Let `ell=1/1000` and `U=union_(j=1)^6 [log j,log j+ell]`. For every nonzero
complex L2 function f supported in U, the actual operator satisfies

```
<f,Tf> >= (81/6400) sum_j |M_j|^2 + (69/40) sum_j ||G_j||_2^2 > 0,
h_j(s)=exp(-(3/4)(log j+s)) f(log j+s),
M_j=int_0^ell h_j(s)ds,
G_j(s)=int_0^s h_j(t)dt-M_j/2.
```

The statement includes every supported function, not only constants or six
test vectors. It includes the signed cross terms at separations log 2, log 3,
log 4 and log 5, where the arithmetic kernel's derivative jumps. A common
translation of all six intervals is allowed. The support consists of six
short intervals, not their whole convex hull of length log 6 + 1/1000.

## What makes the gluing proof work

Each local measure splits into two endpoint masses and the derivative of
its centered primitive. The full cross interaction then consists of a finite
signed mass matrix, mean-primitive terms, and primitive-primitive terms.
The last group retains each actual prime-shift delta as a translated overlap
integral. The parent's local curvature factorization controls the diagonal.

The actual certificate proves

```
C >= (1/100) I,  p>11/5,  d_star<5/4,  beta_star<9/4.
```

One completion of squares then bounds every infinite-dimensional direction.
The finite mass matrix is NOT absolutely diagonally dominant. The source
signs are used jointly; this is not a sum of isolated local-positive tests.

The general theorem also proves: every strictly positive finite sample
matrix of this W has an all-functions positive thickening at sufficiently
small widths. A negative sample matrix has negative tests at all sufficiently
small widths. No assertion about the singular semidefinite case is added.

## Where the attempted completion stops

All matrices `[W(log(i/j))]_(i,j<=N)` being PSD would imply RH by density of
integer ratios and the established full-source endpoint. This packet does
not prove that cofinal sign. Six windows do not tile an arbitrary interval,
and the gluing condition is not established uniformly over larger center
sets. No all-rank induction or new zero-free theorem is claimed.

Read PROOF.md, then VALIDATION.md and the exact result.json. The calculation
is elementary rational interval arithmetic and integration-by-parts algebra.
The relationship to classical Weil-window and Schur-complement methods is
explicit; there is no external novelty or record-length claim.

## Replay

With the unchanged `local-window-positivity/` sibling present:

```sh
python verify_gluing.py --check result.json
python -O verify_gluing.py --check result.json
sha256sum -c SHA256SUMS
```

The checker authenticates the parent code and proof before importing the
interval implementation. It recomputes source constants, knot coverage,
all six strict signed LDL pivots, derivative/cusp bounds, and independent
polynomial cross identities. A saved PASS label is not accepted as proof.
