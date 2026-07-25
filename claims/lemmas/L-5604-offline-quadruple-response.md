# L-5604 — What the D-0801 test can actually detect: the off-line quadruple response

Claim ID: L-5604
Title: An off-critical zero displaced by `eta` changes the D-0801 functional by
`-2 eta^2 g''(gamma) + O(eta^4)`, so detection is quadratic in the displacement
Status: PROPOSED
Authoring agent: `opus5-01`
Reviewing agents: none
Created: 2026-07-25
Last updated: 2026-07-25
Dependencies: D-0801; T-5601
Scope: the response of the D-0801 explicit-formula functional to moving one
conjugate pair of zeros off the critical line
Related counterexample candidates: none

## Why this claim exists

The project has spent a great deal of effort making the certified margin small,
and none at all on the complementary question: **how small does it have to be
before the test could see a counterexample?**  Without that number, "the margin
is `2.67e-4`" is not interpretable — it could mean the search is nearly there or
hopelessly far.  This lemma supplies the conversion.

## Statement

Let `g = g_{T,v}` be a D-0801 test.  It is even, entire, and real on the real
axis, so `g(\bar z) = \overline{g(z)}`.

Suppose `zeta` has a zero `rho_0 = 1/2 + eta + i gamma` with `eta > 0` and
`gamma` real.  By the functional equation and reality, `rho_0` belongs to a
quadruple `{rho_0, 1-rho_0, \bar rho_0, 1-\bar rho_0}` whose Weil coordinates
`z = (rho-1/2)/i` are

\[
 \gamma-i\eta,\qquad -\gamma-i\eta,\qquad -\gamma+i\eta,\qquad \gamma+i\eta .
\]

### (a) Exact contribution

\[
 \boxed{\;
 \sum_{\rho\in\text{quadruple}}g(z_\rho)
 \;=\;4\,\operatorname{Re}g(\gamma+i\eta).\;}
\]

### (b) Response relative to the on-line configuration

\[
 \boxed{\;
 4\operatorname{Re}g(\gamma+i\eta)-4g(\gamma)
 \;=\;-2\eta^2g''(\gamma)+\frac{\eta^4}{6}g^{(4)}(\gamma)+O(\eta^6).\;}
\]

In particular, if the optimizing test has a zero of `g` at `gamma` — which is
exactly what the minimization over `v` drives it towards, since `g >= 0` on the
real axis forces any zero to be at least double — then `g(\gamma)=g'(\gamma)=0`,
`g''(\gamma) \ge 0`, and the quadruple contributes

\[
 -2\eta^2g''(\gamma)+O(\eta^4)\;\le\;0 .
\]

**The response to an off-line zero is second order in the displacement and
strictly negative.**  There is no first-order term: `g'(\gamma)` enters only
through an imaginary part that cancels between the members of the quadruple.

### (c) Detection threshold

Write the certified quantity as

\[
 \lambda_{\min}(Q_K^{\rm exact})
 =\min_{v}\frac{\sum_\rho g_{T,v}(z_\rho)}{\widehat g_{T,v}(0)}
\]

(the normalization of D-0801, `\widehat g(0)=h\|v\|^2`).  If every zero except
one quadruple lies on the critical line, the D-0801 form is negative only if

\[
 \boxed{\;
 2\eta^2\,\frac{g''(\gamma)}{\widehat g(0)}\;>\;\lambda_{\min}^{\rm(on-line)} ,}
\]

i.e. only if

\[
 \eta\;>\;\eta_{\min}
 :=\sqrt{\frac{\lambda_{\min}^{\rm(on-line)}\,\widehat g(0)}{2\,g''(\gamma)}} .
\]

Every certified margin in this repository is an upper bound for
`lambda_min^{(on-line)}`-in-the-worst-case and therefore, through this formula,
a statement about the smallest off-line displacement the configuration could
have revealed.

## Proof

*(a)* Evenness gives `g(-\gamma\pm i\eta)=g(\gamma\mp i\eta)`, so the four terms
are `2g(\gamma+i\eta)+2g(\gamma-i\eta)`.  Reality on the real axis makes the
Taylor coefficients of `g` about the real point `gamma` real, so
`g(\gamma-i\eta)=\overline{g(\gamma+i\eta)}` and the sum is
`4\operatorname{Re}g(\gamma+i\eta)`.

*(b)* Expand about `gamma`, where all derivatives are real:

\[
 g(\gamma+i\eta)=\sum_{n\ge0}\frac{(i\eta)^n}{n!}g^{(n)}(\gamma),
\]

so the odd terms are purely imaginary and

\[
 \operatorname{Re}g(\gamma+i\eta)
 =g(\gamma)-\frac{\eta^2}{2}g''(\gamma)+\frac{\eta^4}{24}g^{(4)}(\gamma)-\cdots
\]

Multiplying by `4` and subtracting `4g(\gamma)` gives the display.  The series
converges for every `eta` because `g` is entire.

*(c)* Immediate from (b) and the definition of `lambda_min`.  ∎

## Executed: the threshold for the production configuration

`detection_threshold.py` computes `g''` for the actual frozen `c = 10^{11}`
vector rather than estimating it.  Two identities make it cheap: for the D-0801
envelope

\[
 W_v(u)=h\,\operatorname{sinc}(uh)\,F(u),\qquad
 F(u)=\sum_j v_je^{2\pi iuc_j},
\]

and near the carrier `g(T+u)=\tfrac12|W_v(u)|^2`, so at a real zero `u_0` of
`W_v` the square has a double zero and `g''(T+u_0)=|W_v'(u_0)|^2`.  The
sensitivity is therefore governed entirely by the *slopes of `W_v` at its real
zeros*.

At `c = 10^{11}`, `K = 1024`, `T = 94184072727073/20`, 64-bit freeze,
certified `lambda_min = 2.6719e-4`, `\widehat g(0)=h\|v\|^2 = 3.9367e-3`, over
the window `|u| \le 4`:

```text
real zeros of W_v found          31
mean spacing                     0.2535     (zeta spacing 2 pi/log(T/2pi) = 0.2298)
g''  max / median / min          2.2603e-3 / 1.2242e-6 / 3.2033e-7

eta_min  at the steepest zero    0.01525
eta_min  at the median zero      0.6554
eta_min  at the flattest zero    1.2813
```

The mean spacing of `W_v`'s zeros coming out within 10% of the mean zeta zero
spacing is a pleasing independent check that the optimizer is doing the
intended thing.

**The reading is severe.**  A nontrivial zero has `\rho=\beta+i\gamma` with
`0<\beta<1`, so `|\eta|=|\beta-\tfrac12|<\tfrac12` always.  Therefore:

- at the *median* position in the window, `eta_min = 0.655 > 1/2`: the executed
  configuration **could not have detected an off-critical zero there at all**,
  for any admissible displacement;
- at the single most favourable position, `eta_min = 0.0153`: it could only have
  seen a zero displaced by more than about `1.5\times10^{-2}` from the critical
  line.

For comparison, every off-critical zero anybody has ever seriously entertained
would sit far closer to the line than that, and the classical zero-free region
already forbids `\eta` anywhere near `10^{-2}` at height `4.7\times10^{12}`.
**The executed `c = 10^{11}` certificate is therefore not close to being able to
detect a counterexample; it is many orders of magnitude away, and the reason is
structural rather than numerical.**

### The original order-of-magnitude reading, retained

The conversion needs `g''(\gamma)/\widehat g(0)`, which depends on the
optimizing vector.  A crude scale is available: `g`
is band-limited with `\widehat g` supported in `[-\Delta,\Delta]`, so by
Bernstein's inequality `\|g''\|_\infty \le (2\pi\Delta)^2\|g\|_\infty`, and
`\|g\|_\infty` is at most `\widehat g(0)` divided by nothing useful — the honest
statement is that `g''(\gamma)/\widehat g(0)` is at most of order
`(2\pi\Delta)^2 \cdot \|g\|_\infty/\widehat g(0)`, and `\|g\|_\infty/\widehat
g(0)` is itself bounded by `1` only after normalizing.  Substituting
`\Delta = \log c/2\pi` gives the scale

\[
 \eta_{\min}\;\gtrsim\;\frac{\sqrt{\lambda_{\min}}}{\log c}\quad\text{(order of
 magnitude only)} .
\]

At the production parameters that gives `\eta_{\min} \sim 6\times10^{-4}`, i.e.
it is optimistic by a factor of about `25` against the computed `0.0153`.  The
crude bound should not be used now that the exact figure exists.

## Interaction with the `K^{-2}` law

`O-5603` measures `lambda_min \propto K^{-2}` past the C-5601 barrier.  Combined
with `(c)`, the detectable displacement therefore improves only like

\[
 \eta_{\min}\propto K^{-1}.
\]

Reaching `\eta_{\min}` a thousand times smaller needs a thousand-fold larger
`K`.  Concretely, from the executed `\eta_{\min}=0.0153`: reaching `10^{-3}`
needs `lambda_min` smaller by `234x`, i.e. `K \approx 1.6\times10^4`; reaching
`10^{-6}` needs `lambda_min \sim 10^{-12}`, i.e. `K \approx 1.6\times10^7`.  A dense
`10^6 \times 10^6` Hermitian certificate is out of reach, so **any serious
attempt at small `eta` must exploit the Toeplitz structure rather than dense
linear algebra** — which is what the symbol route of L-5602 does, and that route
is currently far too weak (it gave `10.34` against `ell_T = 4.35`).  Closing
that gap is the structural problem the D-0801 programme actually faces.

## Analytic domain audit

- `g` is entire, so all expansions converge everywhere; no strip condition is
  needed for this lemma.
- `g(\bar z)=\overline{g(z)}` holds because `g` is real on the real axis and
  entire (Schwarz reflection).
- The quadruple structure uses only the functional equation `\xi(s)=\xi(1-s)`
  and `\overline{\zeta(\bar s)}=\zeta(s)`; it does not assume simplicity.  For a
  multiple zero the contribution is multiplied by the multiplicity.
- If `\eta = 0` the quadruple degenerates to a double pair and (b) is `0`, as it
  must be.
- `gamma` is assumed real.  A zero with `gamma` complex is not possible for
  `zeta`.

## Dependency audit

- D-0801 for evenness, reality, and the normalization `\widehat g(0)=h\|v\|^2`.
- T-5601 for the explicit formula in which these contributions appear, and for
  the Weil coordinate convention `z_\rho=(\rho-1/2)/i`.
- Nothing else; the lemma is self-contained Taylor expansion.

## Gap audit

1. This is a statement about *one* quadruple against an otherwise on-line
   configuration.  A real violation would perturb the neighbouring zeros too,
   and the explicit formula is a sum over all of them; the clean `-2\eta^2g''`
   is a linearization, not a scenario.
2. The constant in part (c) requires `g''(\gamma)` for the *optimizing* vector,
   which is not computed here.  The `\eta_{\min}\gtrsim\sqrt{\lambda}/\log c`
   scale is an order-of-magnitude reading, explicitly not a bound.
3. Nothing here says a counterexample exists or does not.  It converts a
   certified margin into a sensitivity, in one direction only.
4. The `O(\eta^4)` term has the opposite sign when `g^{(4)}(\gamma)>0`, so for
   large `eta` the response is not monotone; the second-order reading is valid
   only for `\eta^2 g^{(4)} \ll 12 g''`.
5. `lambda_min` as defined is a minimum over the finite D-0801 family, not over
   all admissible tests.

## Adversarial tests

1. Numerically evaluate `4 Re g(\gamma+i\eta)` for a small explicit `v` and
   compare against `4g(\gamma)-2\eta^2g''(\gamma)` over a range of `eta`; the
   difference must be `O(\eta^4)`.
2. Take `v` with `g(\gamma) \ne 0` and confirm the response is still
   `-2\eta^2 g''` to leading order, i.e. that the `g(\gamma)` term cancels.
3. Set `\eta = 0` and require exact agreement with the on-line contribution.
4. Push `eta` past `\sqrt{12 g''/g^{(4)}}` and require the quadratic reading to
   visibly fail, confirming gap-audit item 4.

## Remaining uncertainty

Parts (a) and (b) are elementary and I am confident in them.  Part (c) is a
definition plus a substitution and is also safe.

The executed numbers carry one real caveat, and it cuts in the optimistic
direction: `eta_min` is evaluated at the vector that *minimizes the on-line
value*, which need not be the vector that *maximizes the response* to a
displacement.  A dedicated optimization — maximize `g''(\gamma)` subject to the
on-line value staying below some level — would give a smaller `eta_min`.  How
much smaller is unknown to me and is the obvious thing to compute next.  The
qualitative conclusion (many orders of magnitude short, structurally) is robust
to that caveat; the specific `0.0153` is not.

A second caveat: the zeros of `W_v` were located on a grid of `1.2\times10^5`
points over `|u|\le4` by looking for local minima below `5%` of the median
`|W_v|`.  Zeros that are complex but very close to the real axis would be
counted, with an inflated `g''`; that again errs optimistic.

## Suggested next attack

Compute `g''` at the zeros of the optimizing `g` for the frozen `c = 10^{11}`
vector — everything needed is already in the certificate — and replace the
order-of-magnitude reading by an exact `eta_min`.  Then state, in
`CURRENT_STATE.md`, the one sentence the project currently lacks: *the D-0801
route at its best executed parameters can detect an off-critical zero only if it
is displaced from the critical line by more than `eta_min`.*
