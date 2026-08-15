# T-91870 publication handoff

```text
base PR:      #500
base SHA:     d73c1e7a1a482cac31581211a84db43cc34c824e
new branch:   research/gpt56-pro/91870-native-fiber-physical-coupling
PR title:     successor: native-Mobius physical-coupling compiler
```

Run `./publish.sh`. The script clones a clean repository, checks the exact base,
copies the additive payload, runs the lightweight replay, commits, pushes, opens
a draft PR and reads back the remote ref, PR head, tree, changed paths and key
Git blob IDs.
