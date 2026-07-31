# Integration handoff — exact capacity saturation

This stack continues PR #161 and composes with the corrected zero-evaluation and
radical-packet interfaces on PR #159, together with the symbol/complement
artifacts of PR #152 / PR #155.

## New logical correction

Do not attempt to prove a loose symbol count `D` is smaller than a radical
capacity `C`.  For `epsilon<t<Gamma`, min--max already proves `C<=D`.
The reverse inequality is valid only through exact low-index saturation.

## Required packet at one support

Provide:

```text
L  exact repaired radical packet
U  complete symbol-selected packet
W  = L+U
V  = W intersect L^perp
E  = W^perp
```

and certify:

```text
A|L < t I
A|E >= Gamma I + h M
Y-Gamma I-h^-1 R* M^-1 R >= 0 on V.
```

This proves

```text
N_A(t)=N_A(Gamma)=dim L.
```

Then run the inverse-Ritz checker from PR #161 or the scalar envelope of
`L-15602`.

## Exact control

```bash
cd experiments/X-15602-capacity-saturation
python verify.py certificates/synthetic-saturation.json \
  --output /tmp/saturation.json
python -m unittest discover -s tests -v
```

## Cofinal promotion gate

A proof of RH requires one symbolic sequence with

```text
alpha_j -> 0
alpha_j/t_j -> 0
beta_j^2/t_j -> 0
delta_j -> 0
```

and a saturation certificate at every cofinal level.  Fixed-rank convergence,
matching asymptotic dimensions, or a finite computation list is insufficient.

## Suggested next computation

At the first support where PR #155's scalar bathtub floor is insufficient:

1. reuse its directed symbol cells to build `U`;
2. build the largest uniformly controlled exact source packet and repair the
   source constraints;
3. use the PR #159 certified-zero evaluation split to decompose the mismatch
   into near-kernel and visible directions;
4. enlarge `L` by every repairable near-kernel direction;
5. assemble and certify the finite visible Schur complement;
6. in parallel, test the scalar leverage-deficit and weighted trace-tail gates
   of `L-15607/L-15608`.
