# Cross-review replay

Run `python3 verify_cross_review.py`.

The replay validates the delta schema, exact verdict vocabulary, 40-character source SHAs, the semicolon-versus-ampersand parser defect, strict dangling-node census, small exact RN/source/half-divisor fixtures, and a fail-closed no-proven-path result. It does not validate every theorem or rerun any heavy campaign.
