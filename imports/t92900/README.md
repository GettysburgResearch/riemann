# Frozen imports for T-92900

The successor is based on the exact PR #489 head
`0bb487c8a0782f601be0a3041743b357ad93726a`.

Dependencies inherited by that tree are pinned by Git blob SHA. The Chebyshev
thinning estimate is not present as a normal file on the base tree and is
therefore pinned honestly to its exact historical commit
`116d0ffb42602d5711abdba15aeb3ba9de076984`.

The PR #490 review head
`6f46c2cf4e84d51c744263f7e92a0e1743de5148` is a review input, not a proof
dependency. Reviewers should fail closed on any path, commit or blob mismatch.
