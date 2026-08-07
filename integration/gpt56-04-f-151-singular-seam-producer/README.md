# Singular-seam producer artifact handoff

This directory preserves the exact prepared artifacts for `X-15120` while the
reviewable source files live at their normal repository paths.

The public-source result remains exactly:

```text
SOURCE_SPECIFICATION_INCOMPLETE
missing_count = 17
manifest_sha256 =
40a2cedeac541318f44a8aba9d7b1a00dc431ac8d271a3e0add5ca4f552dcf1a
```

No missing field has been filled and no surrogate row is included.

## Reconstruct the exact artifacts

From this directory run:

```bash
bash reconstruct.sh
```

The script creates:

```text
riemann-singular-seam-producer.patch
riemann-singular-seam-producer.tar.gz
```

and verifies them against `riemann-singular-seam-producer.SHA256SUMS`.

Then the patch is directly applicable from the repository root:

```bash
git apply integration/gpt56-04-f-151-singular-seam-producer/riemann-singular-seam-producer.patch
```

The patch and archive are split only because the GitHub connector used for this
push accepts UTF-8 repository files but not direct binary file uploads. The
reconstructed bytes and published SHA-256 values are identical to the prepared
artifacts.
