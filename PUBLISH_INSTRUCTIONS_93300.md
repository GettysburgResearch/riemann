# Publication instructions — cubic-shell balanced-dispersion packet

The downloadable packet contains `publish.py`, a deterministic unified patch, all repository files, metadata, and SHA-256 ledgers.

From a clean checkout of `gfreund123/riemann`:

```bash
python3 publish.py /path/to/riemann
```

The publisher fails closed unless:

- the checkout has commit `6cc0da2fa5711017e260ebdcea4ba8c22e453288`;
- the worktree is clean;
- none of the packet paths already exists;
- all packet hashes validate;
- the exact replay succeeds.

It creates:

```text
branch: research/gpt56-pro/93300-cubic-shell-balanced-dispersion
base:   6cc0da2fa5711017e260ebdcea4ba8c22e453288
```

then applies the deterministic files, commits, pushes, and—when an authenticated `gh` is available—opens a draft PR against
`research/gpt56-pro/93250-centered-q4-cubic-closure`.

The publisher does not modify PR #498. The GitHub branch already published by this session is the canonical live successor; the downloadable publisher is an independently replayable fallback.
