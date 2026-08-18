# O-98070 — p=67 profile-ratio reconnaissance

Status: **FINITE FLOATING RECONNAISSANCE; NONPROBATIVE**

For
\[
Q_{67}(Y)=U_{71}(Y/67)/U_{71}(Y)
=\sqrt{67}\,F_{71}(Y/67)/F_{71}(Y),
\]
the current scanner, replayed through `Y=1,000,000`, reports

```text
maximum Q67 = 2.55967670964739158
argmax Y    = 536
child U71   = 4.85958016951216099
parent U71  = 1.89851325802061655
child F71   = 13.7449683663268853
parent F71  = 43.9537596652631066
nonpositive denominators = 0
```

The included C++ scanner reconstructs `U_71` from the exact identity
`U_67(Y)=U_71(Y)-67^-1 U_71(Y/67)`, so
\[
U_{71}(Y)=\sum_{k\ge0}67^{-k}U_{67}(Y/67^k),
\]
with `U_67` evaluated from the exact annular Möbius coefficient dictionary.

The bundled legacy `10^8` record is retained only for provenance. It reports a
different quantity at `Y=584`: the current scanner gives
`Q67=2.4976323499783275`, `child_F71=13.517866899960671`, and
`parent_F71=44.301359765922335`, whereas the legacy record reports
`Q67=10.154323446727647` and `parent_F71=10.896689462364304`. The legacy
semantics are therefore unreconciled and incompatible with the current T98070
scanner. Neither scan supplies proof evidence.
