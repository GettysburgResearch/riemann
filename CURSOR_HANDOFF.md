# Cursor handoff — integrate X-15120 into PR #158

Target repository: `gfreund123/riemann`  
Target branch: `agent/gpt56-04-f/151-finsler-target-completion`

## Apply

From the repository root:

```bash
git apply /path/to/riemann-singular-seam-producer.patch
python -m unittest discover \
  -s experiments/X-15120-singular-seam-source-producer/tests -v
```

Expected: 12/12 tests pass.

## Scope

Add only the files in the patch.  They implement a source-bound exact quartic
row assembler and a machine-readable audit of the public Shimizu v8/v6 source
package.  The public-source certificate must remain
`SOURCE_SPECIFICATION_INCOMPLETE`; do not fill the 17 missing fields with
surrogate choices.

## Suggested commit

```text
experiment: add source-bound singular-seam quartic producer
```

## Issue handoff

Post to issue #176:

```text
X-15120 now assembles c4, A, K, Tr(A^4), Tr(K^4), the jet S4 value, and the
quartic target verdict from one source-bound finite package. The public v8/v6
manifest fails closed with 17 missing fields (digest
40a2cedeac541318f44a8aba9d7b1a00dc431ac8d271a3e0add5ca4f552dcf1a),
so no actual first-window row can yet be emitted without extra source data.
```
