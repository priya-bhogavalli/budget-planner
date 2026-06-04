# Budget Planner

Money-aware planning repo for Priya's personal intelligence, content, and venture ecosystem.

The rule is simple:

```text
earn first -> spend carefully -> upgrade only when revenue justifies it
```

This repo controls when we are allowed to add paid tools, hosting, APIs, rendering, or subscriptions.

## Monthly Spend Policy

Current cap: **25 EUR/month**

Default allocation:

| Category | Cap | Notes |
| --- | ---: | --- |
| LLM APIs | 15 EUR | Summaries, research, scripts, classification |
| Tooling / hosting | 5 EUR | Only if needed; prefer local and GitHub Actions |
| Buffer | 5 EUR | Experiments, occasional overage |

Hard rule: no new recurring subscription unless it maps to a revenue experiment or removes a clear bottleneck.

## Repo Roles

| Repo | Budget Role |
| --- | --- |
| `personal-hub` | Strategy and priorities |
| `de-ai-newsletter` | Low-cost signal intake |
| `research-analyser` | Research output; API spend only for high-value topics |
| `ai-video-studio` | Content production; local render first |
| `priya` | Command center; should stay lightweight |
| `priya-ventures` | Revenue experiments and business validation |

## Phases

See [roadmap/phased-budget-roadmap.md](roadmap/phased-budget-roadmap.md).

## Monthly Workflow

1. Set this month's planned spend in `budgets/YYYY-MM.md`.
2. Track actual API/tool/hosting costs.
3. Track revenue attempts in `revenue/revenue-experiments.md`.
4. Review gates before buying anything new.
5. Only increase spend after income or strong validation.

## CLI

```bash
PYTHONPATH=src python3 -m budget_planner.cli new-month 2026-06
PYTHONPATH=src python3 -m budget_planner.cli check 2026-06
```

