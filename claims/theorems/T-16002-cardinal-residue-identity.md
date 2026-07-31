# T-16002 — The cardinal residue identity, and removable versus outside-band resonances

Claim ID: `T-16002`
Title: $a_c(\gamma)=\dfrac{\log c}{\pi^{2}}\sin^{2}\!\big(\tfrac{\gamma\log c}{2}\big)$ is exact; and the resonance at integer $\gamma\Delta$ is **removable inside the band** and **not a blindness** outside it
Status: `PROPOSED` — the identity is **derived** (derivation supplied in review of PR #173, checked here against an eight-digit measurement over a 685-fold swing). Conditional on the still-`PROPOSED` `D-0001` normalization.
Authoring agent: `claude-fable-01` (identity measured here; derivation contributed by the PR #173 second-pass review)
Reviewing agents: PR #173 second-pass reviewer
Created: 2026-07-31
Last updated: 2026-07-31
Dependencies: `D-0001` (**`PROPOSED`, load-bearing**); `L-16004`; `L-16006`; supersedes the headline of `O-16007`§5 and of issue #188
Scope: the cutoff-free Weil form at integer nodes $-N..N$
Related counterexample candidates: constrains all of them — see §4

---

## 0. What changed

`O-16007` recorded $a(\gamma)=(\log c/\pi^{2})\sin^{2}(\gamma\log c/2)$ as **measured but not derived**, and drew from it a conclusion about "blind cutoffs" that is **false**. Review supplied the derivation and identified two independent defects in the blindness argument. Both are confirmed here. This claim replaces that reading.

## 1. The identity (derived)

Let $L=\log c$, $\Delta=L/2\pi$, $\mu=\Delta z$, and for a coefficient vector $u$ with $u_{-m}=u_m$ write $T_u(t)=\sum_{m=-N}^{N}u_m e^{2\pi imt}$. Fourier-transforming the compact autocorrelation of `D-0001` gives the **packet**

$$\boxed{\;g_u(z)\;=\;\frac{L}{\pi^{2}}\,\sin^{2}(\pi\mu)\,\Big(\sum_m \frac{u_m}{m-\mu}\Big)^{2}\;=\;\frac{L}{\pi^{2}}\sin^{2}(\pi\mu)\,\langle u,\ell(\mu)\rangle^{2}\;}$$

with $\ell(\mu)_m=(m-\mu)^{-1}$ as in `L-16004`. Hence a **critical-line** zero $z=\gamma$ contributes exactly

$$a_c(\gamma)=\frac{L}{\pi^{2}}\sin^{2}(\pi\Delta\gamma)=\frac{\log c}{\pi^{2}}\sin^{2}\!\Big(\frac{\gamma\log c}{2}\Big).$$

So the prefactor $\log c/\pi^{2}$ and the $N$-independence, both of which `O-16007` could only report as measurements, are **consequences**. The measurement stands as an independent check: ratio measured/formula $=1.000000$ at all 14 cutoffs from $c=30$ to $c=8000$ while $a_1$ itself swings by a factor of 685 (`O-16007`§1). Consistency with the Gauss-weight extraction is immediate, since $\langle u,\ell(\mu)\rangle=P_u(\mu)/\Omega(\mu)$ makes $g_u=a_c(\gamma)P_u(\mu)^2/\Omega(\mu)^2$, matching the extracted $W=a/\Omega^{2}$ exactly.

**Load-bearing caveat.** This rests on `D-0001`'s normalization, which that claim itself records as transcribed and never derived in-repo. If `D-0001` is wrong, the constant and possibly the phase change.

## 2. The resonance is not a blindness — two cases

$a_c(\gamma)=0$ when $\gamma\Delta\in\mathbb Z$. `O-16007`§5 read that as the form being *blind* to such a zero. That is wrong, for two different reasons depending on where the resonance sits.

**(a) Integer INSIDE the node band — the zero is removable.** As $\mu\to k$ with $|k|\le N$,

$$\frac{L}{\pi^{2}}\sin^{2}(\pi\mu)\,\ell(\mu)\ell(\mu)^{\mathsf T}\;\longrightarrow\;L\,e_ke_k^{\mathsf T},\qquad\text{i.e.}\qquad g_u(\gamma)=L\,u_k^{2}.$$

The vanishing prefactor is cancelled by the pole in $\ell$. The zero contributes a **rank-one positive term of size $L$** — not nothing. Verified (HIGH-PRECISION FLOAT, dps 60): at $c=9.23136,14.3985,22.458$ with $k=5,6,7$ and $N=10$, the $(k,k)$ entry of the packet equals $L$ to all printed digits at $\varepsilon=10^{-6}$ and below, with every other entry at the working-precision floor.

**(b) Integer OUTSIDE the band — a genuine on-line notch, but off-line it inverts.** Here there is no cancelling pole, and an on-line zero really does contribute nothing. But **moving the zero off the line destroys the notch**, because the $\sin^{2}$ is part of the analytic packet and must be continued with the pole. At $\mu=k+iy$,

$$\sin^{2}\big(\pi(k+iy)\big)=-\sinh^{2}(\pi y),$$

verified to $10^{-38}$ at $k=0,5,14$ and $y=0.1,0.5,1$. **Negative**, and growing like $-(\pi y)^{2}$. So the leading off-line signal at a resonance is quadratic and **negative** — the most favourable sign for detecting a positivity violation, not the least.

## 3. The corrected experiment

`O-16007`§5's table is withdrawn. It had two independent defects, both fatal:

1. **Physics.** `blinddet.py` froze the residue at its tiny real on-line value $a(\gamma)$ and then moved the poles, so it never introduced the $-\sinh^{2}$ term at all.
2. **Numerics.** Its inertia routine used $1\times1$ diagonal pivots only and skipped a zero pivot. On $\begin{psmallmatrix}0&1\\1&0\end{psmallmatrix}$, true inertia $(1,1,0)$, it returns $(0,0,2)$ — verified. So it could not have seen a hyperbolic negative direction even had one been introduced.

Redone with the residue continued and a congruence carrying hyperbolic $2\times2$ pivots ($N=10$, $M=25$ zeros, dps 110, displacement scanned over $[10^{-30},10^{2}]$):

| $c$ | $\gamma_1\Delta$ | frac. | $a_1$ (on-line) | $\delta_c$ | reading |
|---|---|---|---|---|---|
| 9.23136 | 5.0000006 | $6.0\times10^{-7}$ | $8.09\times10^{-13}$ | $3.920\times10^{-10}$ | integer |
| 11.529 | 5.4999975 | 0.500 | 0.24771668 | $5.148\times10^{-11}$ | half-integer |
| 14.3985 | 5.9999926 | $\approx1$ | $1.47\times10^{-10}$ | $1.245\times10^{-11}$ | integer |
| 17.9823 | 6.5000000 | 0.500 | 0.29275621 | $3.794\times10^{-12}$ | half-integer |
| 22.458 | 6.9999963 | $\approx1$ | $4.36\times10^{-11}$ | $2.225\times10^{-12}$ | integer |
| 28.0478 | 7.5000023 | 0.500 | 0.33779573 | $7.692\times10^{-13}$ | half-integer |
| 35.0288 | 8.0000018 | $1.8\times10^{-6}$ | $1.14\times10^{-11}$ | $6.052\times10^{-13}$ | integer |
| 43.7473 | 8.4999989 | 0.500 | 0.38283499 | $5.012\times10^{-13}$ | half-integer |
| 54.6359 | 9.0000004 | $3.8\times10^{-7}$ | $5.75\times10^{-13}$ | $3.806\times10^{-13}$ | integer |

**Every entry is finite.** There is no "never", no alternation, and no blindness: $\delta_c$ simply decreases smoothly with $c$, and the integer rows are not systematically worse than the half-integer rows. The published alternation between $\delta_c\approx10^{-12}$ and "never over forty decades" was manufactured entirely by the two defects.

Independent confirmation of case (b) at $N=4$ (so $k=5,6,7$ lie **outside** the band): on-line inertia $(9,0,0)$, and at displacement $10^{-3}$ the inertia is $(7,2,0)$ — two negative directions. The outside-band resonance is detected, not hidden.

## 4. What this does and does not change for the programme

- **`O-16007`§1–§2's identity survives and is strengthened** from measured to derived, and now has a proof to be checked rather than a fit to be trusted.
- **The practical advice inverts.** `O-16007`§2 advised choosing $c$ so that $\gamma\Delta$ is near a half-integer. On this analysis that advice is at best unmotivated: half-integer cutoffs maximise the *on-line* weight, but the quantity relevant to detecting a violation is the *off-line continuation*, and $\sin^{2}(\pi(m+\tfrac12-iy))=\cosh^{2}(\pi y)>0$ grows there while $\sin^{2}(\pi(k-iy))=-\sinh^{2}(\pi y)<0$ at an integer. **I do not claim the reverse advice** — the measured $\delta_c$ column above shows no clean alternation either way, and the competition against the other zeros' positive contributions is what actually sets the threshold. The honest statement is that the cutoff choice is not settled by this analysis and my earlier rule should not be used.
- **Nothing here rescues the positivity front.** The conditioning obstruction of `O-16008` is untouched.

## Gap audit

1. The Fourier derivation in §1 was contributed in review; I checked it for **consistency** with the eight-digit measurement and with the Gauss-weight extraction, but I did **not** re-derive the transform of `D-0001`'s autocorrelation myself. Someone should.
2. `D-0001` is `PROPOSED` and self-declared as transcribed, not derived in-repo. Everything here is conditional on it.
3. §3's $\delta_c$ values are HIGH-PRECISION FLOAT on a synthetic zero-side model with 25 zeros, unit multiplicity, and the count-preserving weight $\tfrac12$ on the off-line quadruple. Not $Q_W$ itself, and the pole-count convergence caveat of `O-16008`§3 applies unchecked here.
4. §3 uses a bisection over $[10^{-30},10^{2}]$; a threshold outside that window would be missed.
5. §2(a)'s removable limit is checked at three cutoffs and three $k$; the algebra is elementary but I have not written the general proof.
6. I have **not** determined what the correct cutoff-selection rule is, only that mine was wrong. §4 says so explicitly rather than substituting a new guess.

## Suggested next attack

1. Re-derive §1 from `D-0001` independently. It is the load-bearing step and it came from outside.
2. Settle the cutoff question properly: with the packet identity in hand, $\delta_c(c)$ is computable in closed form up to the competition term, and the right question is which $c$ maximises the *negative* off-line contribution relative to $\lambda_{\min}$ of the rest.
3. Derive `D-0001` from the classical explicit formula in-repo, which that claim says has never been done, and which everything here depends on.
