# T-97680 standalone front door

Read:

1. `L-97680`
2. `R-97680`
3. `L-97681`
4. `L-97682`
5. `R-97681`
6. `T-97680`

Replay:

```bash
cd experiments/X-97680-critical-depth
./replay.sh
```

The replay checks exact finite source algebra, the asymptotic inequality
contracts, and hostile mutations. It does not prove NCBI67 or RH.
