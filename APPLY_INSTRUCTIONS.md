# Apply instructions

This packet is designed against:

```text
repository: gfreund123/riemann
base:       research/gpt56-pro/91540-paired-kernel-typed-closure
base SHA:   2bd4625bb2e3cf41318be5b22f6f8e8d0827fef1
```

Apply the sibling patch file from the repository root:

```bash
git apply riemann_root_entry_attack.patch
python3 experiments/X-91702-post-hall-current-ledger/verify.py
```

Suggested branch:

```text
research/gpt56-pro/91702-root-entry-blocker-attack
```

Suggested commit message:

```text
research: reduce native root feasibility to one literal Hall row identity
```

The packet must not be described as an unconditional proof of RH.
