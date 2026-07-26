# Run X-9306 on the committed PR #103 atomized minimum

This marker triggers `.github/workflows/x9306-real-log-portfolio.yml` from a
base branch that already contains the workflow and search implementation.

The workflow searches the exact monomial-positive L-9308 portfolio cone on the
committed 512-bit direct-xi table at shift `483/1024`, then exactly replays every
retained rational direction against PR #103's atomized count shells.

No counterexample or sign is asserted by this marker.
