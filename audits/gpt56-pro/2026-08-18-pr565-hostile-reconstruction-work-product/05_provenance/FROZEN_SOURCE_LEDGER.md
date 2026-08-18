# Frozen-source ledger

## User-selected reconstruction base

```text
repository: gfreund123/riemann
PR:         #565
head:       339e3367660f40c74795802a6f8170b15e19b13a
```

## Mandatory adversarial firewalls

```text
PR #574: global Hall / local-to-global source feasibility firewall
PR #575: parity, scalar-lift, and completed-parity Lorenz firewall
```

The exact PR #574 and PR #575 head hashes fetched during the long pass were not written into the surviving local packet. This archive therefore does not invent them after the fact.

## Preserved recovery packet provenance

The exact recovered packet under `02_original_recovery_packet/` records:

```text
base PR #556: a4feca0457d310c72054f274040f93b0503f658b
PR #559:      88d97adef8a42c5baf2f52c2c259a4ef536bdfdd
PR #561:      db9bdc63c855c6ddf664b763d748f8155a6a2c67
original ZIP: 441b133b4b621afd96090f5f315e1adc942d6fa9b98a4f42d33a1a30dc7f81f3
```

Its verification JSON explicitly says:

```text
directed_certificate_replayed_here: false
scientific_status: candidate complete; P61 bias certificate requires independent reconstruction
rh_established: false
```
