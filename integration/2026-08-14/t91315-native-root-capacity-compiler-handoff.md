# T-91315 native-root capacity compiler handoff

## Freeze

```text
repository: gfreund123/riemann
base PR:    #468
base SHA:   a41f81466f85d52597c97b41505756a8860698d0
PR #464:    2eb70463f3d0ae791a9f140694d2ace7032ae864
PR #467:    d5e03a3a63bd05b43abf4b5e37905f86e9ec59d6
PR #454:    a0409d54250bc211d62718a1aedb6fa020d7f091
PR #463:    9e138832258d19c252fe60597e36d02bfb95fe39
```

## Read order

1. `R-91316` — exact PR #464/native separator.
2. `L-91386` — simultaneous optimizer theorem.
3. `L-91387` — finite activation-cell/Farkas campaign.
4. `L-91388` — direct native \(Y_4\)-slack LP.
5. `T-91315` — fail-closed compiler.
6. `X-91144` — exact replay.
7. `O-91390` — route order and stop rule.

## Immediate falsifiers

```text
canonical P61 capacity is called native;
rough reservoir is owned both current and recursively;
a stopped-leaf Hall theorem is invoked;
an LP basis other than the leftmost target fill is claimed superior despite the
monotone profile hypotheses;
a signed detail map is assumed positive without ordinary q/4q reconstruction;
a Y4-positive slack is called score-free;
a PASS_NATIVE_ROOT_CAPACITY_THEOREM verdict is issued without a full live
primal certificate.
```

## Exact status

```text
compiler result:
PASS_EXACT_NATIVE_ROOT_COMPILATION_SEPARATOR

NRCT:
unproved

RH:
unproved
```
