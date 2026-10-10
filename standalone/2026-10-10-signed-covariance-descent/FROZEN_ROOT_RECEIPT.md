# Frozen-source receipt for the root independent reconstruction

**Reviewer:** root AI agent. **Frozen source:**
[8f2acaacddc10bd8fb053a66070a1d06d25aa922](https://github.com/GettysburgResearch/riemann/commit/8f2acaacddc10bd8fb053a66070a1d06d25aa922).

**Tree:** `94bf5570710b88d2bb254cc6d274b4654411510f`.
**Sole parent:** `2edc467ef4dea4aa685219ac6a558a158b88768d`.

The remote source commit was fetched and its entire tree compared with
the staged source before adopting that commit locally. I then read
its committed blobs with `git show`, checked their Git blob IDs and
SHA-256 hashes, and compared them byte for byte with the contents used
in ROOT_INDEPENDENT_REVIEW.md. All matched. Its reviewed mathematical
claims and finite-checker scope are therefore bound to this exact
published source, not to a moving branch tip.

| File | Git blob | SHA-256 |
|---|---|---|
| [FINITE_RAY_REUNION.md](FINITE_RAY_REUNION.md) | `616d3b9a146d7eba4a7f56467ef24197e0791d67` | `8897088fb7e89c66e18bf0652a913983c5120a61d854591f990cce2a6261f2e0` |
| [FINITE_CUBE_HOMOGENEITY.md](FINITE_CUBE_HOMOGENEITY.md) | `850f03d087d885a6befd080dac95b76eee609568` | `e4f7b3ff0817c4b6deaf2e608657425c06ac97c1a7f4f60f3762eba7eca7b0e1` |
| [ALL_CUSP_COEFFICIENT_ADAPTER.md](ALL_CUSP_COEFFICIENT_ADAPTER.md) | `1533314683a550ed9e59bac1c1734df346377458` | `bfabc37c5b16a32d6b29fe5767f58f5f5a8dc161aaa3d127ebf11236fa2d3ca1` |
| [SUPPORT_PRUNED_COVARIANCE.md](SUPPORT_PRUNED_COVARIANCE.md) | `3965862cab6c058e6f98524d8d71cf8facaf3800` | `83ba41487ce6e0d1e81e2efbecc21be5c364134b97639afa0b12680765f0c8e3` |
| [SECOND_REFLECTION_BOOTSTRAP.md](SECOND_REFLECTION_BOOTSTRAP.md) | `38a2594ee38b14abbb8c6217352c9047e869e0f1` | `e1db605878eb805a3d21f908ea1c73f5869d56c112a3c3e91e67d9b715b16fd0` |
| [checks/check_descent_algebra.py](checks/check_descent_algebra.py) | `a5846d8e275da569ad136472f6bed3af5560a0e1` | `675187430abcfa5433f7a749da594b6121bc3fc2d06c7febb63fafb027124280` |
| [results/descent_algebra_checks.json](results/descent_algebra_checks.json) | `952ad574cd47a87c123740b2ac17810e51627c37` | `9a78e9d8559d6130573826a03608e8f09001c7e78b1e7956a6f56fd32c07798a` |
| [ROOT_INDEPENDENT_REVIEW.md](ROOT_INDEPENDENT_REVIEW.md) | `6cc13c3b14dfa569dc231ae955088d315cebad32` | `f69f453e7235e624c02a34a6252e447c0628044a058ef39622ecdbe91410dc7f` |

**Disposition: PASS at the scopes in ROOT_INDEPENDENT_REVIEW.md.**
This includes the two actual finite-ray identities, all-cusp
coefficient table and its support-pruned covariance consequence,
bootstrap local algebra and new domain, and the exact finite checker.
The proof-file authored-by-other boundaries remain as recorded there.
The spectral and full-cusp-composition notes were authored by root;
this receipt does not independently approve those two notes. Their
separate agent reviews are bound by the other frozen-source receipts.

The checker was independently executed under normal and optimized
Python, with byte-identical retained reports; its authenticated scope
is finite algebra only. The imported analytic foundation was not
reproved, there was no new Lean build, and no full fourth moment,
generalized moment or RH theorem is accepted by this receipt.

This receipt and the other validation additions do not change the
frozen mathematical source. A changed proof needs a new affected-scope
review; later GitHub metadata alone cannot strengthen its claims.
