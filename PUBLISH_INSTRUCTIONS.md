# Publish T-107020 to PR #759

Target repository: `gfreund123/riemann`  
Target branch: `research/gpt56-pro/107000-beta-nyquist-compression`  
Required exact head: `d1b8aa57b08db1ba9f2edf3b68238c2a129b7c33`

From the unzipped packet:

```bash
./publish.sh /path/to/riemann
```

The script fails closed unless the checkout is clean and exactly at the frozen
head. It validates every packet hash, reproduces the retained replay, applies
the add-only patch, commits, pushes to the existing PR branch, and updates PR
#759 when `gh` is authenticated.
