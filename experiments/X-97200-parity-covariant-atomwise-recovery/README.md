# X-97200 packet replay

This is a content-integrity replay only. It verifies the frozen text packet and
does not authenticate PR #561's directed witness or prove `GPHT*`, `TFPE`,
`ACBI`, scalar positivity, or RH.

```bash
python3 experiments/X-97200-parity-covariant-atomwise-recovery/verify_packet.py
```

Expected output:

```text
PASS_T97200_PACKET_CONTENT
```
