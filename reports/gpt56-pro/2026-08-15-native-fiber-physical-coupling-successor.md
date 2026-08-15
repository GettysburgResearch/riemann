# Native-fibre physical-coupling successor

PR #500 correctly turns Hall/current/child bookkeeping into an abstract positive
coupling, but its factor-67 instantiation begins after the source marginal has
already been chosen. The successor supplies that marginal.

The main changes are:

1. the input is the exact hybrid native source: finite anchored Möbius occurrences plus retained-cell Volterra Möbius occurrences;
2. the canonical `P_61` rough lift is retained only as a separator;
3. the source is split into a rank-one Hall bulk and an exact stopping-line /
   Target-Lorenz anchored sector;
4. every Hall edge, residual, first owner, causal choice and placement is one
   label in one source partition;
5. the physical target is an anchored/bulk disjoint union with one
   block-diagonal label-blind quantizer;
6. the signed finite comparison remains a second ledger;
7. small columns, common `q/4q` detail, native `Y_4` price and endpoint
   orientation are audited in one chain.

The construction is candidate-complete on the frozen analytic inputs. RH remains
unproved pending reconstruction.
