# T-105059 — The branch-energy tent reduction and the W-pinch program: E1 transformed

Claim ID: `T-105059`
Status: **(.1) AUDIT PASSED; (.2) PROVED (exact, unconditional); (.3) PROVED-STANDARD (RH-conditional Perron bookkeeping); (.4) REFUTATION OF THE ORIGINAL E1a MATCHING PLAN (finding); (.5) PROVED (exact, unconditional) — the Cauchy–Schwarz tent reduction; (.6) PROGRAM — one named open analytic lemma (W-PW pinch lemma); (.7) bootstrap logic AUDIT PASSED, contingent on (.6). RH never assumed globally, never claimed.**
Created: 2026-08-23. Agent: claude, lane E1.
Depends on: `L-105058`, `T-105051`, `L-105052`, `L-105053`, `O-105054` @ `claude/riemann-proof-review-8nz34i`; lane S data (`experiments/X-105057-sign-hunt/out_*.json`).
Replay: `experiments/X-105059-branch-energy/` (num_e1.py … num_e4.py, num1.json, pred_vs_O.json, NOTES.md).
Notation as in L-105058: `U=U_X=floor(X^{1/3})`, `N=N_X=floor(X/U_X)`, `h_U=(mu 1_{>U})*eta`,
`C_U(x)=sum_{n<=x}h_U(n)n^{-1/2}`, `m(u)=sum_{d<=u}mu(d)/d`, `E(L)=int_{2^L}^{2^{L+1}}Ht_{U_X}(X)dX/X`.

## (.1) Re-verification of L-105058.5 — VERDICT: PROOF SOUND

Checked step by step. (1) `F(s)=1/(s zeta(s+1))` on `Re s>0`: Abel summation with
`|m|<=1`, `T^{-s}m(T)->0`. (2) `J(h)<=A'/(2h)+O_{A',T_0}(1)`: partial integration of
`int u m^2 u^{-2h}du` against `Q(T)<=A' log T (T>=T_0)`; `int_1^inf (log T)T^{-2h-1}dT=(2h)^{-2}`.
(3) Cauchy–Schwarz gives `int|m(u)|u^{-sigma-1}du<inf` for every `sigma>h'-1/2` (any `h'>0`
with `J(h')<inf`), hence the Mellin integral converges ABSOLUTELY on every line
`Re s=-1/2+h` (use `h'=h/2`); so `hat(phi_h)=F` pointwise a.e. and Mellin–Plancherel
`J(h)=(1/2pi)int|F(-1/2+h+it)|^2 dt` is legitimate (no H^2 boundary-limit subtleties:
interior lines only). The en-route conclusion "hypothesis => zeta nonzero on Re>1/2" is
derived, not assumed. (4) Schwarz on `D(rho_1,1/2)` (pole at 1 outside: `|rho_1-1|=14.14`);
`C_1(r_0)->|zeta'(rho_1)|=0.79316` (simplicity rigorously known numerically; fallback
constant stated); `int_{|tau|<=r_0}dtau/(h^2+tau^2)->pi/h`. (5) `c_0=2/((1/4+gamma_1^2)
|zeta'(rho_1)|^2)=0.0158924` recomputed. Corollaries 1, 2 verified (Cor 2: if only finitely
many heavy blocks, `Q(2^J)<=C+(c_0-eps)J log2` contradicts the limsup). **One caveat:
Corollary 3 is correct as stated but covers u-side log-scale smoothing at scale
`delta(u)->0` ONLY — see (.4): it does not cover what E1 needs.**

## (.2) Edge-mechanism lemma (NEW, exact): closed form for the branch-energy constant

**Lemma.** Let `C(x)=kappa sqrt(x)` (any constant `kappa`) be inserted as the model for
`C_U` in the truncated field `G_-(Y)=sum_{U<n<=N}h_U(n)n^{-1/2}A_-(Y/n)`. Then:
(i) [bulk] for `Y in (4U, N]`: `G_- = kappa sqrt(Y)[(1-2^{-1/2}) - sqrt2(2^{-1/2}-2^{-1})] = 0`
EXACTLY — the kernel zero `hatA_-(1/2)=0` (O-105054.3) annihilates the `sqrt(Y)` mode pointwise.
(ii) [edge] for `Y in (N,2N]`: `G_- = kappa(sqrtN - sqrtY)`; for `Y in (2N,4N]`:
`G_- = kappa(sqrt(Y/2) - sqrt2 sqrtN)`; and
`int_N^{4N}|G_-|^2 dY/Y = kappa^2 N (3 log2 - 2)`.
(iii) With `kappa = -2K/sqrt(pi log N)` this equals `(4(3log2-2)/pi) K^2 N/log N`, and
matching lane P's gamma-side formula `(2/pi^2) I_w K^2 N/log N` forces the closed form

    I_w := int_R w(gamma)/(1+4gamma^2) dgamma = 2 pi (3 log 2 - 2) = 0.4991459274...

**verified by high-precision quadrature to 7e-9** (lane P's 0.49906 was coarse-grid error).
Proof of (ii): elementary integrals `int_1^2(1-sqrt y)^2 dy/y = log2+5-4sqrt2`,
`int_2^4(sqrt(y/2)-sqrt2)^2 dy/y = 4sqrt2+2log2-7`. QED.
This CONFIRMS, by an independent Y-side computation, lane P's claim (gamma): the branch
energy lives entirely on the truncation edge `Y in (N,4N]`; the bulk is killed by the
kernel zero. The gamma-side and Y-side computations agree exactly.

## (.3) E1b — the remainder under RH: CLOSED at strength O(N^eps) (PROOF-STANDARD)

**Theorem (RH).** Uniformly for `gamma in [1,2]`:
`Sigma_N(gamma) = HankelLoop_N(gamma) + E_N(gamma)`, `|E_N| <<_eps N^eps`,
where `HankelLoop_N(gamma)` is the exact cut-hugging loop integral of
`R_U(w) zeta^{1/2}(w) N^{w-s_0} dw/(w-s_0)` around the segment `[1/2+eps, 1]`
(`s_0=1/2+i gamma`; under RH `b(w):=((w-1)zeta(w))^{1/2}` is single-valued analytic on
`Re w>1/2`, and `zeta^{1/2}=b(w)/(w-1)^{1/2}` with cut `(1/2,1]`).
Proof (standard ingredients, constants not written line-by-line): truncated Perron at
`Re z=1/2+1/log N`, height `T=N`; Perron truncation error `<< N^{1/2+eps}/sqrt(T) = N^eps`
(`|h_U|<=(1*eta)(n)<<n^eps`); shift to `Re w=1/2+eps` with the cut detour; on the vertical
line, RH gives `1/zeta(w) << |t|^eps` and the Möbius partial-sum bound
`M_U(w)-1/zeta(w) << U^{1/2-sigma+eps}(1+|t|)^eps` (Titchmarsh 14.25-type), hence
`R_U(w) << N^eps` POINTWISE (crucially: not the trivial `|w| U^{1/2-sigma}` from Abel
summation), so the line contributes `<< N^{2eps} log N`; horizontals `<< N^{-1/2+2eps}`;
the `z=0` pole is never crossed. QED.
**This settles the E1b half beyond its target**: the requested `theta<1/2` holds with
`theta=eps`; `|E_N|` is `o` of the branch scale `N^{1/4}/sqrt(log N)` by a power.

## (.4) E1a as originally planned is REFUTED (finding), and measured

The loop's leading coefficient is NOT `-m(U)(1+o(1))`. Collapsing the loop:
`HankelLoop_N(gamma) = -2 K_N N^{1/2-i gamma}/((1-2i gamma) sqrt(pi log N)) + (expansion tail)`,
`K_N := (1/sqrt pi) int_0^{v_max} R_U(1-v/log N) b(1-v/log N) e^{-v} v^{-1/2} dv`
(UNCONDITIONALLY defined: real-sigma cut, `zeta(sigma)<0` on `(1/2,1)`). The sigma-side
smoothing at scale `1/log N` is, on the u-side, a MACROSCOPIC tail reweighting: formally
`K_N ~ -sum_{d>U}(mu(d)/d)(1-log d/log N)^{-1/2}` — weight `sqrt2` at `d ~ U`, not an
approximate identity. Hence: (a) L-105058.5 Cor 3 does NOT apply to it; (b) pointwise
matching `K_N = -m(U)(1+o(1))` is unreachable by current technology even under RH (the
cut-scale variation of `R_U` is `>> |m(U)|` by `exp((log U)^{1/2+o(1)})/log N`, by the best
known RH bound for `M(x)`); (c) any scheme absorbing the mismatch via upper bounds on
mu-mean-square block masses needs negative-moment inputs (Gonek-type) — the SAME wall
recorded in T-105051's obstruction paragraph.
**Numerical confirmation (numeric duty, 212 lane-S points, U in [1000,10800], X up to 1e12):**
with `pred := (2/pi^2) I_w m(U)^2 N/log N`: Pearson corr(pred, O) = **0.9975**; fit
`O = -3.716 + 2.023 pred` (residual sd 0.166, max 0.43); slope `2.023 ~= |sqrt2|^2` is the
predicted signature of the sqrt2-reweighted coefficient (`|K_N|^2 ~ 2 m(U)^2`); intercept
-3.72 = lane S's background. Sign classification at the model zero-crossing pred>1.84:
TP/FP/FN/TN = 32/1/0/179. Onset: U=2780 (pred 1.58) O=-0.44; U=2800 (pred 2.51) O=+1.56 —
the first positive O sits exactly at the crossing. Every measured positive-O window
(U~2800-3450, 8400-10800) is a predicted heavy window; no positive with pred<1. All dyadic
blocks j=7..19 of `u m(u)^2` carry mass 0.013-0.027 >= c_0 log2 = 0.011. Direct tent-sum
check: `|Lambda_meas/Lambda_pred| -> ~1` (0.60,0.64,0.75,1.04 at N=1e5..2e6) with
K-proxy `sqrt2 m(U)` (one overall sign in the convention chain still to be fixed; irrelevant
for the quadratic energy). **The branch-mass mechanism, with the sqrt2-corrected
coefficient, quantitatively explains lane S's entire positive-O phenomenology.**

## (.5) The Cauchy–Schwarz tent reduction (NEW, exact, unconditional): gap g2 dissolved

**Lemma.** For every X>=64, with `Lambda(X) := sum_{N/2<n<=N} h_U(n) n^{-1/2} log(2n/N)/log2`
(tent-weighted h-sum; `U=U_X`, `N=N_X`):

    Ht_U(X) >= int_{2N}^{4N}|G_-|^2 dY/Y >= (1/log2)|int_{2N}^{4N}G_- dY/Y|^2 = 2 log2 * Lambda(X)^2,

hence `E(L) >= 2 log2 int_{2^L}^{2^{L+1}} Lambda(X)^2 dX/X` EXACTLY.
Proof: on `(2N,4N]` only the `-sqrt2` band survives with `n in (Y/4, N]`, so
`G_-(Y) = -sqrt2 (C_U(N)-C_U(Y/4))`; `int_{2N}^{4N}(C(N)-C(Y/4))dY/Y = log2*C(N) -
int_{N/2}^{N}C(x)dx/x = log2*Lambda(X)` after swapping the order of summation (the tent
weight `log(2n/N)/log2` is the exact overlap measure); then Cauchy–Schwarz on `dY/Y`
(total mass log2). QED.
Consequences: (i) the branch-dominance question no longer requires ANY extraction — no
K_N, no window-variation error, no RH: the gate directly upper-bounds, and is lower-bounded
by, the log-mean square of the single arithmetic functional `Lambda`; (ii) the U-cell
bookkeeping closes trivially: `log U=(1/3)log X` maps each u-octave onto 3 X-octaves; if
`sum_{u-block j} W_u^2 >= c` with `W_u := Lambda sqrt(log N_u)/u` (scale `u^{-1/2}`), then
`E >= c' 2^j/j` summed over those 3 octaves, so at least one octave L has
`E(L) >= (c'/3) 2^{L/3}/L`; io heavy blocks give io heavy octaves. (Within a U-cell, N
sweeps only ~3u = O(sqrt N) integers; no freezing is needed anyway since (.5) is exact.)

## (.6) The single remaining gap (g1'): the W-pinch lemma — PROGRAM

**Target lemma (open).** `limsup_T (1/log T) int_1^T u W_u^2 du/u >= c_0' > 0` for the
tent field `W_u = Lambda sqrt(log N_u)/u`, by the L-105058.5 machinery.
What is proved about its shape: the u-Mellin transform of the tent field factors through

    (1/2pi i) int dz/z 2^{-z} zeta(w-z)^{1/2} / zeta(w+z),   w = 1/2 + s/2,

(ratio-cut `d>=2e` Perron in an auxiliary variable). Its continuation has singularities
where the moving branch point `w-z=1` PINCHES a zero `w+z=rho` of zeta: at `s=rho`,
`Re s=1/2` — exactly where the H^2-line `Re s=1/2-h` probes as `h->0`. The RAW singularity
type is `(s-rho)^{-1/2}` (a pole integrated against a half-power): its `|.|^2`-blowup is
only `log(1/h)` — **the eta-partner half-singularity wall**: the half-divisor structure
softens every zeta-zero from a pole to a half-pole, so the raw-field Paley–Wiener argument
stops a full power of `h` short of contradiction. This is the precise function-theoretic
form of T-105051's negative-moment obstruction and O-105054.1's bounded-frequency wall.
The DESIGNED ESCAPE (why W, not Lambda/u, is the right object): the deterministic weight
`sqrt(log N_u)` performs a half-derivative on the Mellin side and restores the full pole
(model: `F=(s-a)^{-1/2} <-> density u^a/sqrt(pi log u)`; weighting by `sqrt(log u)` gives
`(1/sqrt pi)(s-a)^{-1}`), with `1/h`-blowup constant computable from the pinch coefficient
at `rho_1` (expected `~ c_0` up to the explicit `2^{-z_*}/z_*` factors, `z_* = (rho_1-1)/2`).
REMAINING WORK, honestly: (w1) rigorous continuation of the two-variable representation to
a neighborhood of `s=rho_1` on the H^2-line, with the floor(U)-cell corrections; (w2) the
half-derivative singularity-transfer as a lemma (weighted-Mellin Tauberian, standard-shaped);
(w3) the hypothesis-side steps (2)-(3) of L-105058.5 for W (verbatim transfer; `|W_u|<<u^eps`
suffices and holds unconditionally); (w4) nonvanishing of the pinch coefficient (it is a
nonzero multiple of `2^{-z_*}/(z_* Gamma(1/2))` times `1/zeta'(rho_1)` — same simplicity
input as L-105058.5, same fallback). None of these needs RH. **Until (w1)-(w4) are written,
E1 is NOT closed.**

## (.7) Assembly and bootstrap audit (contingent on (.6))

If (.6) closes, the chain is: [(.5) exact] + [(.6)] give **unconditionally**
`E(L) >= c 2^{L/3}/L` for infinitely many L — note RH would no longer be needed at all,
strengthening L-105058.6's plan: (i) `Theta_gate >= 1/3` unconditionally; GATE_theta is
FALSE for every `theta<1/3`; GATE_{o(1)} (= HHFE102010 in the corrected Ht reading,
T-105051's audit) is FALSE unconditionally. (ii) With T-105051(III) (RH => GATE_theta for
all theta>1/3): under RH, `Theta_gate = 1/3` exactly. (iii) The dial T-105051(I) is
untouched: GATE_theta for theta in [1/3, 1/2) remains the honest open target, each level
still paying an unproved zero-free half-plane.
Bootstrap logic audit (as tasked): (i) the deposited chain does give GATE_{o(1)} => RH for
the Ht reading: T-105051(I) is stated for Ht (Step 0 repairs Hardy to `|B_U|<=3Ht`), and
GATE_{o(1)} means all theta>0, forcing zeta nonzero on Re s>1/2+theta for every theta —
i.e. RH. CITED EXACTLY: T-105051 Statement (I) + Step 0. (ii) No circularity: the reductio
"GATE => RH; GATE and RH => E large io => not GATE" is valid (any RH-conditional step may
be used inside the reductio since RH is derived from the assumed GATE — and in the (.5)/(.6)
route even this is moot, as no step uses RH). (iii) Quantifiers: GATE_theta is an
all-large-L statement; an io-sequence of L with `E(L)>=c2^{L/3}/L > C 2^{theta L}`
(theta<1/3, L large) negates it. VERIFIED. The failure mode lane P flagged (E_N-phase
conspiracy) is retired by (.3) (`|E_N|<<N^eps`) and made irrelevant by (.5).

## Falsifiers

(.2): any error in the two elementary integrals or the quadrature identity for I_w.
(.3): a gamma in [1,2] with measured `|Sigma_N - HankelLoop_N|` growing like a power of N
(would contradict RH via the theorem, hence merit maximal scrutiny). (.4): future data with
positive O and pred<1, or slope drifting from 2 at larger X (would falsify the sqrt2
interpretation, not the mechanism). (.5): a numerical X with `Ht < 2 log2 Lambda^2`
(exact inequality — any violation is a bug). (.6): a proof that the pinch coefficient at
rho_1 vanishes (would break the program and be a striking identity in its own right).
