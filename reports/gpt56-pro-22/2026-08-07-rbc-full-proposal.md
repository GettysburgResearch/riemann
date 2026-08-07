# Full proposal — reflected boundary-charge reserve contraction

Agent: `gpt56-pro-22`  
Date: 2026-08-07  
Issue: #249  
Base: PR #236 at `1c9a749a1648c4772509eb3b056598c7044f4393`  
Status: **FULL PROPOSAL; SOURCE-BOUND RBC RESERVE OPEN; RH UNPROVED**

## Executive conclusion

The reflected Selberg identity is valuable because it creates the correct
Hermitian square. It does not by itself estimate that square. The old terminal
face proposal made two logically distinct moves:

1. it counted endpoint coordinates;
2. it moved the Hermitian diagonal from the forcing to the energy side.

The first controlled only a terminal family. The second could be the tautology
`2E=2E`. The corrected route therefore requires a proof-producing **strict
reserve** in addition to a bounded boundary-charge count.

The new spine is

```text
reflected Hermitian Selberg identity
-> exact double finite Möbius resolvent
-> residual-depth expansion
-> superorder Euler purge of every non-top row
-> top-top all-truncated Möbius corner
-> source-additive oriented subdivision
-> exact cancellation of internal unmarked faces
-> strict reflected Schur reserve
-> bounded simultaneous paid-coordinate defect
-> rate C_ref/K at fixed scale reserve
-> rightmost-zero exponent zero
-> RH.
```

## New exact reduction: only the top-top row survives

For a one-sided row `mu_V*r_V^j`, expand every residual as `a_i b_i` with
`a_i<=V`. If `j<=K-2`, product geometry forces one residual factor to lie
exponentially far above `V`:

```text
(a_i b_i)/V >= exp((K-j-1)J/K^2-O_K(1)).
```

Its unrestricted quotient is therefore a complete active lattice, separated
from the residual cutoff. With Euler order `R_K=K^3`, the row has amplitude
exponent at most

```text
1/2-K(K-j-1)+o_K(1),
```

and is exponentially small. The same argument works Hilbert-valuedly in the
reflected packet.

Thus every reflected row except `(j_+,j_-)=(K-1,K-1)` is closed. This is a
strict strengthening of the fixed-positive-fraction Euler theorem: even a free
scale of order `J/K^2` is enough.

The surviving top-top row is not declared harmless. It is the exact Möbius
boundary tensor and retains the RH-bearing shell exponent.

## Boundary charge versus face count

An oriented source subdivision cancels all internal faces before norms. The
number of face families may grow with `K` without affecting the exponential
rate. One paid normalized coordinate costs `V^(1/2)` in amplitude and `V` in
energy, hence exactly `1/K` in the exponent.

Therefore the correct invariant is

```text
maximum number of coordinates simultaneously paid on one surviving row,
```

not the number of faces and not the raw dimension of a face.

## The indispensable reflected reserve

The reflected identity has the form

```text
2 E = reflected forcing.
```

If the forcing decomposition returns the same `2 E`, moving it left gives zero
and proves nothing. The full certificate must instead produce a block
factorization with Schur complement

```text
R = G-C*D^-1 C >= kappa_0 G,
kappa_0>0.
```

Only then does boundary control imply energy control.

This reserve is the genuine arithmetic hinge. It must be proved on the actual
top-corner source span and cannot be imported from an arbitrary-vector operator
estimate.

## `RBC(K)`

For every sufficiently large block at order `K`, emit:

1. the complete top-corner source manifest;
2. the oriented incidence cancellation;
3. every lower-scale route;
4. the reflected reserve;
5. every charged row and its paid-coordinate set;
6. an absolute charge bound `q_K<=C_ref`;
7. one fixed-ratio Möbius-shell projection.

Then

```text
E_K(J)
 <= exp((C_ref/K+o_K(1))J)
    [1+M_K((1-delta)J+O_K(1))].
```

A uniform sequence of such certificates gives

```text
2 Theta_zeta <= C_ref/(K delta) -> 0,
```

and RH.

## Candidate producer

The proposed top-corner producer uses one radial cumulative-log crossing near
`J/2`. The crossing coordinate has range at most `V`; all other fiber
coordinates remain inside the reflected Gram. A candidate physical token
vocabulary has at most eight token types. This nominates `C_ref<=8`, but the
number is not promoted until the source incidence and reserve are emitted for
`K=4,6,8` and then proved symbolically.

## Exact status

```text
reflected coefficient identity                 inherited proposed exact
finite inverse and shell-transfer algebra       inherited proposed exact
superorder residual-depth purge                 proposed complete
oriented internal-face cancellation             proposed complete abstractly
paid-coordinate exponent C/K                    proposed complete
reflected Schur-reserve adapter                 proposed complete abstractly
actual top-corner reserve                        OPEN
actual bounded charge injection                 OPEN
RBC(K) => BTP(K) => RH                           proposed complete conditional chain
Riemann Hypothesis                              UNPROVED
```

## Reviewer decision

The proposal is accepted only if the actual source-bound reserve and charge
objects are produced. It is rejected by any of:

- an unpaired internal face;
- an Euler row with a live cutoff;
- a same-scale target hidden on the reserve right side;
- a Schur floor tending to zero;
- a surviving row with unbounded simultaneous paid defect;
- loss of the fixed-ratio Möbius shell.
