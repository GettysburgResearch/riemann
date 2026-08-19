# T99550 — Clamped Volterra equality-interface recovery

## Publication recovery

An earlier response advertised a `99550` branch and PR that did not exist on
the remote.  This is the actual publication, stacked on PR #641 at exact head

```text
19cd3939a54ccea73b055b3952b5dd7ed638c4fb
```

**RH remains unproved.**

## Exact result

The canonical continuum equality seed is assembled from the one-colour atom

```text
F(u)=4(1-sqrt(u))+2 sqrt(u) log(u),  0<u<=1.
```

It satisfies

```text
F(1)=0;
F'(1)=0;
V F(u)=2/sqrt(u)-1.
```

Consequently every reciprocal activation knot is `C^1`, every distributional
knot mass is zero, and the endpoint data at `theta=1` kill both homogeneous
Volterra modes.  The exact frame is

\[
\mathscr B^\star(\theta)
 =\int_\theta^1
 \frac{2(\sqrt{\theta t}-\theta)}{t^{3/2}}L(1/t)dt.
\]

Thus PR #638's generic two-anchor gate is vacuous for the canonical equality
frame.  PR #641's canonical-frame boundary contribution can be removed;
Hall-transformed fibres and the explicit anchored block remain separately typed.

## Important correction to the stale draft

The theorem is proved in the native proportional variable `theta`.  No
unproved reciprocal-variable profile and no `4sqrt(X)` score consequence is
claimed by this packet.

## Replay

```bash
python3 experiments/X-99550-clamped-volterra/verify.py \
  --output experiments/X-99550-clamped-volterra/results/verification.json
sha256sum -c T99550_CONTENT_SHA256SUMS
```

Expected:

```text
PASS_T99550_CLAMPED_VOLTERRA_EQUALITY_INTERFACE
```

## Exact boundary

```text
canonical activation values             zero exactly
canonical activation derivative jumps   zero exactly
Volterra homogeneous modes              zero exactly
reverse Green reconstruction            proved exactly
canonical-frame Volterra boundary debt    eliminated
Hall-transformed/anchored/finite ledger    still requires reconstruction
inherited heavy campaigns               not replayed here
Riemann Hypothesis                       unproved
```
