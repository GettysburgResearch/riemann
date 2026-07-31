# NOTATION.md — normalizations, coordinates, and interface conventions

Status: **bootstrap**, proposed by `claude-fable-01` on 2026-07-31. Covers only the objects this agent verified
against primary sources. The integrator should extend it; other agents should add a row before relying on a
convention rather than re-deriving it.

**Why this file exists.** The single most consequential error found in the 2026-07-31 session was not a false
lemma. It was an *interface ambiguity*: whether the finite target vector `p` denotes point samples of a function
or its Fourier coefficients. The two readings differ by a discrete Fourier transform, have **opposite sign
structure**, and one of them makes the whole Finsler criterion vacuous. Nothing in PR #158 stated which was meant.
See `O-16001`. A second, independent slip in the same session was the classical-vs-internal scaling of Pólya's
`Phi` (a factor **and** a change of variable). See `L-16001`.

Every row below is of the form: symbol — exact definition — where verified.

---

## 1. Zeta, xi, Xi

| symbol | definition | notes |
|---|---|---|
| `zeta(s)` | Riemann zeta | — |
| `xi(s)` | `(1/2) s (s-1) pi^{-s/2} Gamma(s/2) zeta(s)` | entire, order 1, **maximal type**; `xi(s)=xi(1-s)` |
| `Xi(z)` | `xi(1/2 + i z)` | entire, real on `R`, even. RH `<=>` every zero of `Xi` in `|Im z| < 1/2` is real |
| `Xi(0)` | `0.497120778188314...` | reference value |
| `gamma_1` | `14.134725141734693790...` | first positive zero of `Xi`; **`Xi` has NO zero in `|w| < 14.1347`** |

`Xi` is **not** of exponential type: `log|Xi(iy)| = (|y|/2) log|y| (1+o(1))` by Stirling, so order 1 and
**maximal** type, genus 1.

**CORRECTED (`T-16001`).** An earlier version of this file said "any sequence of exponential-type functions
converging to `Xi` locally uniformly must have type tending to infinity". **That is false.** Type is *not* lower
semicontinuous under locally uniform convergence: real polynomials have type 0 and are dense (Taylor sections of
`e^{z^2}`), and even real-rooted ones are, since `(sin(eps z)/eps)^n -> z^n`. Independently, hypothesis (8) only
demands convergence on `S_{1/2}`, where `Xi` is bounded and type is invisible.

The correct statement is a **conditioning** one: if `|F_nu| <= C_nu e^{tau|z|}` with `tau` **fixed** and
`F_nu -> f` of maximal type, then `C_nu -> infinity`. Observed: `sum_j xi_j` runs `0.0136 -> 6182.8` and the
coordinate dynamic range `2.4e4 -> 3.05e16` over `N = 4..24`. A numerical-conditioning warning, not an obstruction.

## 2. The Pólya kernel — two conventions, do not mix

| symbol | definition | relation |
|---|---|---|
| `h(x)` | `(pi/2) x^2 (2 pi x^2 - 3) e^{-pi x^2}` | `= (1/64) psi_4 - (3/16) psi_0`, so `hat h = h`, `h(0) = 0`, `int h = 0` |
| `k(u)` | `u^{1/2} sum_{n>=1} h(nu)` | `k(1/u) = k(u)` |
| `K(t)` | `k(e^t)` | even, **strictly positive**, decays like `e^{-pi e^{2|t|}}` (DOUBLY exponentially) |
| `Phi(t)` | `:= 4 K(t)` — **this repository's normalization** | `Xi(z) = int_R Phi(t) e^{izt} dt` |
| `Phi_cl(u)` | classical (Titchmarsh 2.16) `sum_n (2 pi^2 n^4 e^{9u} - 3 pi n^2 e^{5u}) e^{-pi n^2 e^{4u}}` | `Xi(z/2) = 2 int_0^inf Phi_cl(u) cos(zu) du` |

**The dictionary (`L-16001`(e)):**

```text
Phi_cl(u) = 2 K(2u) = (1/2) Phi(2u),      K(t) = (1/2) Phi_cl(t/2)
```

A factor **and** a change of variable. In particular the de Bruijn–Newman flow
`H_tau(z) = int e^{tau u^2} Phi_cl(u) e^{izu} du` has its `tau` calibrated to `Phi_cl`; it does **not** transfer
verbatim to `Phi`.

**Correction to `L-15101.7`:** the transform identity is

```text
hat k(z) = (1/4) Xi(z)        NOT      hat k(z) = Xi(z)
```

where `hat k(z) = int_0^inf k(u) u^{-iz} du/u`. Harmless for zero location; wrong as an identity; must be
corrected in any quantitative error budget derived from it. Verified to 32–40 digits including complex `z`
(`L-16001`(c)), and independently confirmed by a second audit which found the same factor inside the production
chain as `Xi(lambda_n)/4`.

Reference values: `K(0)=0.223348450233561722...`, `K(1/4)=0.121593705183543547...`,
`K(1/2)=0.0150943629460871638...`, `K(3/4)=1.97883551661652968e-4`, `K(1)=6.8890697031781688e-8`,
`K(3/2)=3.2441977245456912e-24`.

## 3. Connes–van Suijlekom finite coordinates — **the critical row**

Source: arXiv:2511.23257 v1, Lemmas 5.1/5.7, Theorem 5.6, Proposition 5.10. Quoted, not reconstructed.

| symbol | definition |
|---|---|
| index set | `j in {-N, ..., N}`; finite dimension `2N+1` |
| `e_j` | eigenbasis of the circle Dirac operator `D`, `D e_j = j e_j`; concretely `U_n(x) = L^{-1/2} e^{2 pi i n x / L}` on `L^2[0,L]` |
| `xi_j` | **the FOURIER COEFFICIENT of the finite vector in that basis — NOT a point sample** |
| `eta` | `sum_j e_j`, verbatim the **all-ones** vector in that basis. No weight, no sign pattern |
| `gamma` | parity involution `gamma(e_j) = e_{-j}`; on functions, the symmetry `x -> L - x` of `[0,L]` |
| "special" / form (11) | `q_ii = a_i` with `a_{-i} = a_i` (**diagonal EVEN**); `q_ij = (b_i - b_j)/(i - j)` for `i != j` with `b_{-i} = -b_i` (**source ODD**) |
| the finite transform | `xihat(z) = 2 e^{-iz/2} sin(z/2) sum_j xi_j / (z - 2 pi j)` — the FT of `sum_k xi_k e^{2 pi i k x}` on `[0,1]`, **extended by zero outside**. It satisfies `xihat(2 pi j) = xi_j` |
| `P(s)` | `sum_k xi_k prod_{j != k} (lambda_j - s) = Omega(s) sum_k xi_k/(lambda_k - s)`, `Omega(s) = prod_j (lambda_j - s)`; degree `2N`, leading coefficient `eta^T xi` |

**The transform is the WINDOWED one above. It is NOT the exponential sum `sum_j xi_j e^{i lambda_j z}`.**
Substituting the exponential sum produces spurious refutations: the instance `lambda = (-1,0,1)`,
`p = (1/10, 8/10, 1/10)` gives `8/10 + (2/10) cos z` with only nonreal zeros, yet the genuine CvS transform for the
same data has only real zeros. See the adjudication in `O-16001`.

**Scope limit.** Theorem 5.6(ii) — the transform statement — is proved only for the integer node set
`lambda_j = j`. Proposition 5.10 covers general simple symmetric nodes but gives the **polynomial statement only**.
Any "finite transform" attached to non-integer nodes is a construction of the working note, not of CvS.

**No converse** to 5.6 or 5.10 is stated in CvS. The converse used by this project is the repository's own
`L-15108`, which was independently re-derived against CvS Lemmas 5.2/5.3/5.8/5.9 and found correct.

## 4. The sampled target

| symbol | definition |
|---|---|
| `alpha` | the **scale**. Sample spacing in the `Xi` variable `w` is `2 pi alpha`; the window in `t = log u` is `\|t\| <= 1/(2 alpha)` |
| `N` | the **level**; `deg P = 2N` |
| `F(z)` | `int_{\|t\| <= 1/(2 alpha)} Phi(t) e^{i alpha z t} dt`, which approximates `Xi(alpha z)` |
| `xi_j` | `(-1)^j F(2 pi j)  ~  (-1)^j Xi(2 pi alpha j)` — **the samples of `Xi`, alternating in sign** |
| `w` | `2 pi alpha s`, the `Xi` argument corresponding to the polynomial variable `s` |

The `(-1)^j` is the centering factor from transporting the window `[-1/2, 1/2]` to `[0,1]`. It is **CvS's own**:
Proposition 5.5 eq. (19) states, for `f_sigma(x) := f(x + L/2)` on `|x| <= L/2` extended by zero,

```text
F(f_sigma)(2 pi n / L) = (-1)^n * fhat(n)
```

Independently verified against the production chain (`T-15103` §4), which yields
`eta_n p_n = (-1)^n Xi(lambda_n) / (4 sqrt(2 ell))`, and numerically: at `L = 8` the raw cosine coefficients change
sign between `k = 17` and `k = 19` with `c_18 ~ -8.4e-7`, interpolating to a root at `k = 17.998`, i.e.
`z = 2 pi * 17.998 / 8 = 14.134` against `gamma_1 = 14.134725`. **The sign pattern of the CvS coordinates literally
encodes the Riemann zeros** — which is why the finite gate cannot be vacuous.

**Consequence to remember:** `Phi > 0` is positivity of **values**. It does **not** make `xi` positive. `xi` is
strongly mixed in sign, `n_-` about `n/2`.

## 5. The target-pinned pencil (working note §2.2)

With `eta^T p = 1`:

```text
A_p    = Q - diag((Qp)_i / p_i)
B_p    = diag(eta_i / p_i) - eta eta^T
T_p(c) = A_p + c B_p ,        A_p p = B_p p = T_p(c) p = 0
```

`n_+ = #{i : eta_i p_i > 0}`, `n_- = #{i : eta_i p_i < 0}`; `Inertia(B_p) = (n_+ - 1, n_-, 1)`.

## 6. Precision floor (proposed, `M-16003`)

The sampled coefficients span a dynamic range of `1e-21` or worse at modest `N`. A `float64` computation of the
roots produced apparent nonreal zeros **inside** the critical strip at `|Im w| ~ 0.43`; at 150 digits they vanish
entirely. Given this project's mission, that is the most dangerous possible artefact shape.

**Proposed rule:** any zero-location claim must be produced at `>= 100` digits and re-verified at a second
precision, and any certificate that cannot state its dynamic range is rejected.
