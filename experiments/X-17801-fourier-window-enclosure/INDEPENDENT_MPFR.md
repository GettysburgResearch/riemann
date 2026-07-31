# Independent all-MPFR replay

The deterministic source is stored as `replay_mpfr.c.gz` to keep the connector
payload small. Verify and unpack it with:

```bash
sha256sum replay_mpfr.c.gz
# f906732dbeb72fc4c38e7f6d566721959f9d755da151485f9d2a1fe338f0c30a
gzip -dc replay_mpfr.c.gz > replay_mpfr.c
sha256sum replay_mpfr.c
# ce8c72162bb751b8d6b2d7811cc763b2139d697d21065cf6971f58c9538a429a
```

With ordinary MPFR development headers:

```bash
cc -O3 -std=gnu11 replay_mpfr.c -lmpfr -lgmp -lm -o replay_mpfr
```

On systems exposing only the versioned shared object, use the retained minimal
header and link the exact library path:

```bash
cc -O3 -std=gnu11 replay_mpfr.c /lib/x86_64-linux-gnu/libmpfr.so.6 -lgmp -lm -o replay_mpfr
```

Then run `./replay_mpfr 16 4096`, `18`, and `20`. The program fails closed on
ambiguous interpolation cells or support boundaries.
