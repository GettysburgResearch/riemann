# Dependency lock and source freeze report

Audit date: 2026-08-25 (Asia/Jerusalem)
Repository: `gfreund123/riemann`
Frozen base: `573eb6aa42c3d9469462c91c6b3ddfb8ab36d77f`

## Source objects

| Source | Ref | Commit | Tree | Parent(s) | Worktree status at freeze |
|---|---|---|---|---|---|
| bootstrap merge/base | `origin/main` | `573eb6aa42c3d9469462c91c6b3ddfb8ab36d77f` | `1140cfcf2b614ee372c5db18eaa90fbb04c20e8c` | `852d8aa05c701ea7818ce8a50543e68987fef5cc`, `b2c92374d42836b60210bc5700f04a83c965750e` | clean detached publication worktree |
| merged bootstrap topic | `origin/formal/000-bootstrap` | `b2c92374d42836b60210bc5700f04a83c965750e` | `1140cfcf2b614ee372c5db18eaa90fbb04c20e8c` | `49602c8abd8dfdf56fbeaa8fdbce1e84017ffbcc` | object-only; tree equals base tree |
| Reviewer A | `origin/formal/010-upstream-analysis` | `9ed8988218fd9c3e1da33bde81361262fc0aa747` | `2c6e967344eb373843a018a5415f7dce6ba39b94` | `7f9959088610efb7ee7cd01cfce1ad6cda397d61` | clean, detached |
| Reviewer B | `origin/formal/020-arithmetic-mellin` | `072b4dbd0e4e407728a59110eb4f7214e23f8f8d` | `1c32466dd7928a24e0115268a6a330216f26ed3b` | `9bb802ebd97a00e01ef14789417f4c2a53031af3` | clean, detached |
| Reviewer C | `origin/formal/030-xi-operator-qa` | `b20ee9b3678e5d8fa32b04b156bc02cec782a97b` | `ed817c346294758ae1db773edba78d4527bace54` | `4863c31dd497ffe69ea400fe29275decf4cb5d29` | clean, detached |
| C reviews A / PR 747 | `origin/formal/review/2026-08-24/c-cross-a` | `ebe287cc85b122cbe3efd57b7c30ce17d150d74c` | `3fc7ab62d64ec04674d649e32afc2a6ca86e3c40` | `c202d8f33315ca70093edc81361d5f8dca2c5f77` | object-only ref |
| A reviews B / PR 750 | `origin/formal/review/2026-08-24/a-cross-b` | `c2a439895f73ce2b6d03ea3405c5bbddef0fb014` | `4ef94784179890f9bf5799d890d6de62ec8633f5` | `81d201849514224d0a5899ac6b61dc66a71b8d1e` | object-only ref |
| B reviews C / PR 749 | `origin/formal/review/2026-08-24/b-cross-c` | `5e406679aae9a217eff290dfce81e0a0f301d6cc` | `dba66f8b2a27096a06f6ae42dc7af2c2a51dcc18` | `9b28d44b391290095e6669c4a64f1f5d0bcbf18b` | object-only ref |

Every named remote branch and PR head matched the supplied SHA after the full ref fetch. A final literal `git fetch --all --prune` also exited 0 and left every listed ref at the same SHA. Every repaired/review head has merge base `573eb6aa42c3d9469462c91c6b3ddfb8ab36d77f` with the frozen base.

## Toolchain and manifest

All source objects above commit the same files:

- `formal/lean-toolchain`: `leanprover/lean4:v4.33.0-rc2`
- Lean: `4.33.0-rc2`, commit `d8b18978322de05a8f3dba51ef03cf5461676c17`, `x86_64-w64-windows-gnu`
- Lake: `5.0.0-src+d8b1897`
- elan used by the auditor: `4.2.1 (3d5138e15 2026-03-18)`
- Python: `3.12.10` (a private temporary `python3.exe` hardlink exposed the installed interpreter to Bash/PowerShell)
- GNU bash: `5.2.15`
- committed `formal/lake-manifest.json` Git blob: `f9c02d809750cf37e2ae9e19ac635f017e9efe82`
- committed manifest content SHA-256: `6be307e0de2294f99ce68e80903cd4cc88e77b6797c853c67be5cd9f6a1db453`

`lake update` was never run. No manifest diff was produced.

The user's principal checkout was not used for builds or source edits. Its pre-existing branch and untracked experiment remained outside this audit. All exact-source commands ran in the three detached worktrees; B's advisory patch was tested only in an additional disposable diagnostic worktree. Review evidence was authored in a separate publication worktree based on the frozen main commit. No combined-rehearsal worktree was created.

## Locked package checkouts

All ten checkouts were inspected after resolution and matched the committed manifest exactly.

| Package | Revision |
|---|---|
| plausible | `123d15766ba49356c02ebad2a4462dfe12d79899` |
| LeanSearchClient | `f5c090429dff3cf66cb65562526c9ea6e8edfbcb` |
| importGraph | `bb3469a87774349fe01898d8bf2fc6a1ce6411ca` |
| proofwidgets | `222c58dad7706a6e7cae46c0edd65ea881d3ee27` |
| aesop | `7db8190085343afde2f5d2cdcc9bac719b6ec02c` |
| Qq | `ef42f8944eaf5b6cbfbe75d1917d824c7dd6cf33` |
| batteries | `76e1c118b0700b4ceafe99532e887d6431625e1a` |
| Cli | `1319485273bf87833fa472afbcefdedecb16b45f` |
| mathlib | `51e6992efd06126df61a496bebf8f49482a4e129` |
| Zeta23 | `cec57f919ccf34e5fa5372b4ba332f7c848bbb6e` |

The first concurrent A/C cache attempts hit Windows sharing violations while finalizing global Mathlib `.ltar.part` files. Those attempts are retained as environmental `DEPENDENCY_FAILURE` evidence. Cache fetches were then serialized; B and A completed successfully, and C's recovery cache stage completed with no downloads. These retries did not change any dependency revision or committed file.
