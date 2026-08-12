# X-91800 — Radial spectral-type lock replay

This retained experiment checks finite identities used by the radial
spectral-type proposal.

It verifies:

1. the exact prime Clark radial integral formula on a finite prime-power
   packet;
2. the exact paired-eta radial integral formula on a large finite interval
   packet;
3. a finite spectral-gap control showing that an exact module intertwiner
   cannot hit an atom absent from the source spectrum;
4. the shrinking-interval norm law for a diffuse source;
5. the firewall that a global positive total can still hide an arbitrary
   radial atom when interval locality is omitted.

Run:

```bash
python3 verify.py --json /tmp/verification.json
cmp /tmp/verification.json results/verification.json
sha256sum -c SHA256SUMS
```

Expected verdict:

```text
PASS_RADIAL_SPECTRAL_TYPE_LOCK
```

The replay does **not** prove the continuous gamma product-system refinement,
RLSL, the zeta source-to-model interval identity, or RH.
