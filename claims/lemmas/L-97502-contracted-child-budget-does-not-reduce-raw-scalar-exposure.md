# L-97502 — Contracting the recursive ledger does not reduce the raw scalar exposure

Claim ID: `L-97502`  
Status: **PROVED EXACT ACCOUNTING THEOREM**  
Created: 2026-08-18  
Depends on: `L-97501`; repaired P61 constants in PR #576  
RH status: **unproved**

Assume a local base packet has unsigned mass `M` and scalar at least `l M`.
For each raw child let its mass be `m_w`, its scalar be in `[0,u m_w]`, its raw
coefficient be `r_w`, and its contracted coefficient be `t_w` with
`0<=t_w<=r_w`.

The current of `L-97501` pays the leftover scalar exposure

\[
 \sum_w(r_w-t_w)f_w,
\]

after which the recursive ledger pays

\[
 \sum_wt_wf_w.
\]

Therefore

\[
 \boxed{
 \sum_w(r_w-t_w)f_w+
 \sum_wt_wf_w=
 \sum_wr_wf_w.
 } \tag{L-97502.1}
\]

The strongest lower bound obtainable from only the interval data is

\[
 \boxed{
 f_v\ge lM-u\sum_wr_wm_w,
 } \tag{L-97502.2}
\]

and is independent of the safe-child split `t`.

For the repaired P61 constants

\[
 l=\frac1{42},\qquad u=\frac18,
\]

the local interval method needs the **raw** child mass fraction to satisfy

\[
 \boxed{
 \frac{\sum_wr_wm_w}{M}\le\frac lu=\frac4{21}.
 } \tag{L-97502.3}
\]

A contracted recursive budget below `1/8` does not imply (L-97502.3). For
example, raw child fraction `1/4` and contracted fraction `1/10` satisfy the
safe recursive budget but give

\[
 \frac1{42}-\frac18\frac14=-\frac1{1344}<0.
\]

Thus the `<1/8` coefficient theorem is valuable source bookkeeping, but it
cannot replace the missing correlation between current and raw rough parity.
Any successful continuation must use a nonlocal Hall/Lorenz invariant, a
trace-free two-channel extraction, or another source-specific mechanism.
