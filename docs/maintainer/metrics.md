# Metrics Baseline

Pre-rebrand baseline, recorded 2026-08-13 (before the Oraclebone rename resets platform counters).

| Metric | Value | Source |
|---|---|---|
| GitHub stars | 5 | gh api |
| GitHub forks | 0 | gh api |
| GitHub open issues | 1 | gh api |
| PyPI latest version | 0.7.1 | pypi.org JSON API |
| PyPI downloads, last week | 34 | pypistats.org |
| PyPI downloads, last month | 149 | pypistats.org |
| MCP Registry | published (`io.github.sapuyou45-bit/oraclebone`) | registry workflow |
| Glama / mcp.so | listed | manual check |

## Validation gate (review 4–6 weeks after V8.0.0 release)

Pass = majority of these met, measured against this baseline:

- PyPI weekly downloads ≥ 3x baseline (≥ ~100/week under the new name)
- Registry / Smithery installs show non-zero organic growth
- GitHub stars ≥ 30
- Playground shows organic visits/shares

If the gate fails: freeze growth investments (hosted endpoint, QRNG, long-form posts),
switch to boutique-maintenance mode (bugfixes, protocol tracking, issue response).
