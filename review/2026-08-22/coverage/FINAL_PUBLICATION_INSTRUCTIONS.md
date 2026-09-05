# Final publication instructions

## Immutable base

Apply the incremental patch only to draft PR #712 branch
`review/2026-08-22/coverage-genealogy-delta` at exact head:

```text
899d5efc37025b84a03f231fd6006a2b7a97e6e3
```

Do not rebase the patch onto another head without first regenerating and
revalidating the complete packet.

## Apply and validate

```bash
git switch review/2026-08-22/coverage-genealogy-delta
git reset --hard 899d5efc37025b84a03f231fd6006a2b7a97e6e3

git apply --check reviewer-c-final-pass-incremental.patch
git apply reviewer-c-final-pass-incremental.patch

python3 review/2026-08-22/coverage/replay/validate_packet.py
python3 review/2026-08-22/coverage/replay/light_fraction_fixtures.py
python3 review/2026-08-22/coverage/replay/cross_review_followup_fixtures.py
python3 review/2026-08-22/coverage/replay/validate_pass1.py
python3 review/2026-08-22/coverage/replay/validate_final.py

cd review/2026-08-22/coverage
sha256sum -c SHA256SUMS
cd ../../..

git add review/2026-08-22/coverage
git commit -m "review: complete Reviewer C final coverage and genealogy pass"
git push
```

Keep PR #712 in draft state and do not merge it as a proof claim. The packet is
review/provenance infrastructure. **The Riemann Hypothesis remains unproved.**
