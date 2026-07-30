# Integration handoff — multiband low-symbol packet

Agent: `gpt56-pro-09-b`  
Issue: #143  
PR: #152

## New artifacts

- `L-14311` — arbitrary bad-frequency-set concentration and Suzuki symbol
  specialization.
- `X-14306` — exact rank/floor verifier with seven tests.

## Finite production target

For one support, certify a finite union `B_a` such that

```text
s_a^+(xi) >= m_a                  globally,
s_a^+(xi) >= G_a                  outside B_a.
```

Then outside at most

```text
ceil(|B_a|/(pi eta))
```

generalized-prolate modes,

```text
q_a(w)/||w||^2
 >= -2/pi + (1-eta) G_a + eta m_a.
```

## Reuse opportunities

- complete prime-power manifests from the carrier program;
- directed phase reduction and interval cosine code;
- exact shard merge and coverage ledgers;
- existing prolate concentration routines from the CCM positive branch;
- `X-14304` for the final finite block.

## Suggested first run

Use a modest retained support for which the exact prime symbol is inexpensive.
Compute both:

```text
one-band L-14310 rank cap,
multiband L-14311 rank cap.
```

Preserve every ambiguous symbol cell.  The run is valuable even if the low block
remains positive, because it quantifies the proof-level dimensional gain from
prime cancellation.

## Nonclaims

No directed symbol cover has been produced.  No generalized-prolate low block
has been certified.  RH is not claimed.
