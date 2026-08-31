# First Architecture E acquisition contract

Declared before any new numerical acquisition or producer run.

Target: the theorem FOUR_NODE_HIGH_AXIS.md for all packet dimensions1..4,
all real nodes>=256, arbitrary separation and confluence. The finite replay
does not infer this theorem by checking sampled PSD matrices. The proof is
analytic; its explicit constants and finite source algebra are replayed.

Fixed constants: R256,c1/2,n4, exponential Taylor order16 at7/2, gamma bound
27/(R+c), resolvent norm majorant J4(R), weighted shift constant181,
prime majorant181[2^-127+2^-126/126], claimed final Re F margin>1/8.
No threshold search, adaptive node selection or numerical Xi root search.

Exact rational controls, fixed now:

- source matrices represented after diagonal square-root similarity, avoiding
  irrational arithmetic; nodes(256,257,300,1024), (256,256,256,256),
  (256,256,512,512), and (256,65536,16777216,4294967296);
- resolvents at shifts-1/2,0,1/2,1,17,4096, checked by both matrix products;
- independent triangular path expansion versus the resolvent product;
- Cauchy/Newton determinant identity for fixed distinct-node lists, and exact
  fully confluent jet Gram determinant ratios at x256 and x512;
- actual von Mangoldt support through integer32 from independent prime-power
  enumeration, retaining formal log-prime labels rather than floating logs;
- exact Taylor/geometric upper bound exp(7/2)<34, and polynomial division for
  the positive integral22/7-pi;
- adversarial changes to source identity, arithmetic types, signs, factor2,
  rational constants, coverage and the claimed scope must be refused.

Arithmetic: Python standard-library integers/Fractions only; no float or
ordinary high precision accepted. Exact JSON uses integer numerator/positive
denominator pairs and rejects duplicate keys, floats, nonfinite constants,
booleans masquerading as integers and noncanonical fractions.

Resource scope: at most4x4 matrices, at most32 prime labels, at most4096 bits
for accepted exact numbers, owned process expected below64MiB and hard lane
allowance200MiB. No new heavy job, broad scan or external high-zero computation.

Producer: four_node_replay.py. Artifact: four_node_verification.json.
Tests: tests/test_architecture_e_pass_four_node.py. The producer binds this
preregistration, the complete theorem, its own source and the tests, plus exact
Git blobs of the integrated statement and pinned PR765/783 mathematical source.
--write builds a fresh record; --check rebuilds it and compares canonical typed
JSON. A matched checksum without fresh exact reconstruction is not acceptance.

This is a new packet. No inherited fixture, source, claimed test count or
review verdict is changed. Failed acceptance and unknown external analytic
claims are not converted into positive scientific outcomes.
