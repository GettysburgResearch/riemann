# 92880 standalone Gates A/B review front door

Base: PR #488 current head at publication time.
Proposal: `T-92880`.
Status: candidate proposal; RH remains unproved pending independent review.

## Review order

1. `imports/t92880/IMPORT_MANIFEST.json`
2. `L-92880`
3. `L-92881`
4. `L-92882`
5. `L-92883`
6. `L-92884`
7. `T-92880`
8. `experiments/X-92880-standalone-gates-ab/verify.py`
9. `standalone/2026-08-15-92880-gates-ab/REVIEW_SPECIFICATION.md`

## First falsifiers

- a root Hall fiber outside `1<=x<67`;
- one flow failing target equality, score superordination or a declared row;
- any source occurrence with two owners;
- any physical column violating the current-plus-full-child capacity ledger;
- aggregate port demand not dominated by the one available port;
- any root slack component not arising from an explicit unused positive source packet;
- child target coefficient sum at least `1/8`;
- use of an upper bound for `J_Lambda-4sqrt(X)`;
- failure of the frozen endpoint-to-RH consumer.
