# Block-gain continuation: exact parity arithmetic, with the coarse lift retained

**RH is not proved. The uniform gain for the original full dictionary is
not proved.** This is an author submission of proposed component proofs,
not an independent scientific acceptance of PR #805.

Parent: PR #805 at `032c92e540202d1c409974c0c7b43130d684bfed`, packet
`../2026-09-06-astra-dilation-observability/`. Its thirteen files are unchanged.
This sibling placement preserves the parent's exact checksum inventory.

## Results and exact boundaries

The original squared distance is `delta_N`, and its full doubling gain is
`Delta_N=delta_N-delta_2N`. The continuation proves:

- **BG26.1:** `Delta_N >= (2/3) I_N`, where `I_N` uses the whole even-dilation
  channel and every new odd generator. `I_N=0` exactly when the full gain is
  zero. The target-specific lower bound `I_N >= c delta_N^2` remains open.
- **BG26.2–4:** an exact weighted parity/Haar decomposition exposes a
  divisor-incidence Gram. Jordan-totient factorization solves its entire
  detail minimization, with explicit Mobius weights, `e_M <= 1/(2M)`,
  `e_M-e_2M > 1/(40M) >= e_M/20` for every `M>=64`, and an explicit
  `constant/M + O(M^-5/4)` asymptotic. These are theorems for a specified
  relaxation, not for `delta_M`.
- **BG26.5–7:** a lossless finite-matrix recursion restores the complete
  coarse coupling. Its actual `8 -> 16` fixture refutes both monotonicity
  of the lifting penalty and the direct lift of the detail optimizer. A
  nonsquarefree coefficient is needed by the full optimizer. No
  source-blind bounded lift can hold even on individual odd generators.

Start with [PROOF.md](PROOF.md) sections 1 and 5, then sections 2–4 and 6–8.
[VALIDATION.md](VALIDATION.md) specifies the bounded replay and analytic
remainder boundary. [SOURCES.md](SOURCES.md) credits the classical inputs.

## Replay

From this directory in a checkout containing the unchanged sibling parent:

```bash
python3 -I -S scripts/replay.py --check
python3 -I -S -O scripts/replay.py --check
python3 -I -S scripts/test_replay.py
python3 -I -S -O scripts/test_replay.py
```

The checker authenticates four literal parent sources before loading its
interval/Gram implementation. It reconstructs the infinite Gram entries
through index 16, not a finite prime or zero approximation. New exact and
directed checks cover only their specified finite domains. The prose
all-scale theorems are not established by extrapolating these domains.

The new manifest checker uses POSIX-relative names on every platform.
No Windows execution is claimed. The parent's separately documented Windows
manifest portability defect is preserved, not silently patched.

## Independent review request

Check the first-cell weight, exact orthogonal parity decomposition,
Jordan inverse on the complete divisor-closed odd inventory, squarefree
counting constants, and the restoration of the coarse Schur term. Check the
parent's full infinite-Gram remainder proof and the new interval linear
algebra independently. In particular do not transfer the detail gain to
the original source: the retained real-source counterfixture forbids that
inference. No new canonical claim ID, formal declaration or public theorem
status is allocated by this packet.
