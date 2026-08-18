# Publisher note

The deterministic ZIP carries `publish.sh` and `T98070_ADD_ONLY.patch` at its
outer root. They are intentionally not part of the add-only repository patch
itself, avoiding self-reference. Publication must be read back from GitHub
before any successor commit/PR is claimed.

Publication reconciliation: the legacy `10^8` scan was quarantined after the
current `10^6` scanner replay contradicted its semantics. A repository-relative
content ledger is added at publication so the advertised checksum command is
actually executable from the Git tree.
