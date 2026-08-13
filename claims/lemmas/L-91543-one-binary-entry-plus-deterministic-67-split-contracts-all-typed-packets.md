# L-91543 — One binary arithmetic entry followed by a deterministic 67-split contracts every surviving typed packet

Claim ID: `L-91543`  
Status: **PROVED EXACT POST-ENTRY CONTRACTION THEOREM**  
Created: 2026-08-13  
Depends on: `L-91540`; frozen one-prime target-exact producer of PR `#416`  
RH status: **unproved absent the one-prime producer audit**

## 1. The unnecessary ordered-prime loop

The binary-return branch was designed to process an ordered list of rough
primes:

```text
survival -> next arithmetic prime;
hazard   -> contracted child.
```

That is stronger than the factor-54 consumer requires.  After the first
arithmetic/Hall step, both outputs are already positive paired kernel types.
No later arithmetic Euler identity is needed.

## 2. Frozen one-step entry

Assume the frozen one-prime producer supplies positive packets

\[
 (\tau_s,\nu_s)\quad\text{at endpoint }X,
 \qquad
 (\tau_h,\nu_h)\quad\text{at endpoint }X/p,
 \tag{L-91543.1}
\]

with \(p\ge67\), satisfying

\[
 \boxed{
 \mathfrak T_{\tau_s,X}(\nu_s)
 +\mathfrak T_{\tau_h,X/p}(\nu_h)
 =\mathfrak T_X^{\rm parent},
 }
 \tag{L-91543.2}
\]

\[
 \boxed{
 \mathfrak S_{\tau_s,X}(\nu_s)
 +\mathfrak S_{\tau_h,X/p}(\nu_h)
 \ge\mathfrak S_X^{\rm parent},
 }
 \tag{L-91543.3}
\]

and with nonnegative exact finite rows.  These are precisely the target-exact,
score-superordinate conclusions claimed by the frozen target-Hall producer.

The hazard endpoint already satisfies

\[
 \boxed{
 X/p\le X/67<c_0X.
 }
 \tag{L-91543.4}
\]

## 3. Deterministic positive split of survival

Apply `L-91540` to the survival packet with one geometric branch:

\[
 p_s=67,
 \qquad
 \theta_s(n)=\mathbf 1_{n\le X/67}.
 \tag{L-91543.5}
\]

The child is the actual restricted packet

\[
 \nu_s^{\rm child}
 =\nu_s|_{\{n\le X/67\}}
 \tag{L-91543.6}
\]

of the same type \(\tau_s\), now evaluated at endpoint \(X/67\).  The complement
and the endpoint-monotonicity difference form positive current-generation
target, score and exact-row residuals.

Thus

\[
 \boxed{
 \mathfrak T_{\tau_s,X}(\nu_s)
 =
 \mathfrak T_{\tau_s,X/67}(\nu_s^{\rm child})
 +\mathfrak T_s^{\rm residual},
 \qquad
 \mathfrak T_s^{\rm residual}\ge0,
 }
 \tag{L-91543.7}
\]

with the identical positive decomposition for score and every finite row.

The survival child endpoint is

\[
 \boxed{
 X/67<c_0X.
 }
 \tag{L-91543.8}
\]

## 4. Final child target weights

Normalize the parent target in (L-91543.2) to one.  Let

\[
 \omega_s
 =\mathfrak T_{\tau_s,X/67}(\nu_s^{\rm child}),
 \qquad
 \omega_h
 =\mathfrak T_{\tau_h,X/p}(\nu_h).
 \tag{L-91543.9}
\]

Equations (L-91543.2) and (L-91543.7) give

\[
 \boxed{
 \omega_s\ge0,\qquad
 \omega_h\ge0,\qquad
 \omega_s+\omega_h\le1.
 }
 \tag{L-91543.10}
\]

Both actual child packets belong to the paired type class of `L-91540`, and
both endpoints are at most \(X/67\).

The entry step has no positive score debt by (L-91543.3).  The deterministic
survival split has local debt at most its residual target, hence at most one
after parent normalization, by (L-91540.15).

## 5. Consequence

After one target-exact arithmetic/Hall entry, the reset has the exact form
required by `T-91541`:

```text
positive current-generation residual;
survival typed child at X/67;
hazard typed child at X/p <= X/67;
child target weights summing <=1;
bounded local debt;
nonnegative exact finite rows.
```

The survival packet is **not** sent to the next ordered arithmetic prime.
Therefore no all-generation least-prime color transport, no repeated Hall
projection and no recursive return to the native common-kernel type is needed.

## 6. Boundary

This theorem begins after the one-prime target-exact positive producer.  It does
not prove that producer or its exact normalization against the live signed
`P_61`/`P_79` packet.

```text
hazard endpoint contraction                          EXACT
deterministic survival 67-split                      EXACT
survival target/score/row residual positivity        EXACT
two final child target weights sum <=1               EXACT
all post-entry children contract                     EXACT
ordered-prime recursive color stability              NOT NEEDED
one-prime signed arithmetic positive entry           AUDIT REQUIRED
Riemann Hypothesis                                   UNPROVEN
```
