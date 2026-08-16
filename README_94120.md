# T-94120 projective native–Lorenz closure candidate

This packet is a research reset.  It treats the repository as a theorem library
and combines only the strongest surviving ingredients:

```text
PR #508 directed Target–Lorenz compact/tail theorem   4ae97dffd1f76ed3244b8f3028560ffa80663caf
PR #513 review-503-safe direct-row architecture       4275fe97aa5ba885210abb6296c7048386e5909d
PR #512/#514 oriented-child obstruction               625a9273696a1f017f32d37bf9052423ee8590c7 / 944dabba065271f08f3cade0215292dcfbab590f
prior live source registry and terminal-leaf objects  release c17db84944c4b2fbd783d22153c66cddb7653116ad2feeaed8c7731ae3169906
PR #352/#353 one-sided endpoint consumer              906b5a477a1ed7c88a40db7569924f15f3d54b72 / ed566f3198e236c54ba18049181016536f56d456
```

The new step is not another branchwise child realization.  It proves a
projective gluing theorem in the paired source category: unresolved rough
children remain source objects, terminal Target–Lorenz leaf transports are
summed with their exact path weights, and physical observation occurs only once
after the frontier has vanished.  The exact q=2 negative child coordinate is a
mandatory regression.

The proposal is intended as an unconditional full RH candidate for hostile
review.  Publication and replay do not by themselves establish RH.

Quick replay:

```bash
cd experiments/X-94120-projective-native-lorenz
python3 projective_gluing.py --output results/projective_certificate.json
python3 verify.py --mutations --output results/verification.json
python3 -m unittest discover -s tests -v
python3 -m py_compile projective_gluing.py verify.py tests/test_verify.py
cd ../..
sha256sum -c T94120_CONTENT_SHA256SUMS
```
