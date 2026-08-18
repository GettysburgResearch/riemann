# Identifier migration

The attached author packet used the `97400` claim namespace. That namespace is
already occupied on the live PR #577 line, so this recovery mechanically maps
its repository-facing claim, experiment and schema identifiers to `97600`.

The mathematical prose and formulas are unchanged apart from those identifiers.
The publication branch is stacked on PR #577 at
`ae85922195c12a29944e624337bae2167091929b`; the mathematical inputs remain
frozen at the PR #566, #574 and #575 heads recorded in the source lock.

The included PDF is the exact author-rendered binary from the attached packet
and therefore displays the original `97400` identifiers. `main.tex` is the
repository `97600` edition. The exact verifier was replayed after migration and
the retained result and proof-object hash were regenerated.
