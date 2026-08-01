# X-16209 — source-bound gamma=32768 block and cofinal wrapper emitter

This experiment instantiates the closed `L-16231` alias theorem at the next real
source packet without redoing its stationary-phase proof.

## Finite result

```text
gamma                              32768
source file SHA-256                8e3dc89a82a7381ebf930336ba635a6d7af168afdd8ba1a4f0dcc77054170281
cross-alias upper                  5019/23168
complete profile-Gram lower        2265729/2896000
good-support measure lower         29/32
relative epsilon upper             51/100
complete target/gap ratio          151/125439898
proof-object SHA-256               8a32bf65f752ee645c4b081f81fa639871c514035188a79366d0400c6d791be8
```

The source-tail contribution uses only the exact unit-energy ceilings already
present in the bound `DIRECTED_INTERVAL_ODE` primitive. It is intentionally
conservative; decay of the full wrapper ratio does not require those ceilings
to shrink because the scalarization denominator grows like `log gamma`.

## Cofinal rule

```text
gamma_j=4096*8^j,
cross_j<=18/floor(sqrt(gamma_j))
         +2/cuberoot(gamma_j)+1792/gamma_j,
epsilon_j=O(1/log gamma_j),
d4/d8<=1/(50000*4096^j),
wrapper_ratio_j=O(4096^-j)=O(gamma_j^-4).
```

`cofinal-schedule.json` displays the first eight exact instances. Later blocks
must still supply their own bound source primitive; the emitter never reuses a
prior source digest.

## Replay

```bash
python emit.py \
  --source source-gamma32768.json \
  --output-dir results

python verify.py \
  results/certificate-gamma32768.json \
  --source source-gamma32768.json \
  --output results/verification-gamma32768.json

python -m unittest discover -s tests -v
```

Ten mutation tests pass. No RH proof is claimed.
