# X-95600 — five-million-endpoint annular cross-sign reconnaissance

Compile and reproduce:

```bash
g++ -O3 -std=c++17 -o /tmp/scan_cross scan_cross.cpp
/tmp/scan_cross 5000000 /tmp/scan_5000000.json
cmp /tmp/scan_5000000.json results/scan_5000000.json
sha256sum -c SHA256SUMS
```

The scan evaluates the exact ten-band formulas in long-double arithmetic. It is
floating discovery only and proves no cofinal sign, UOSACF estimate, or RH.
