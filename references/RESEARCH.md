# Research and design decisions

Checked 2026-11-21. Recommendation: keep a small, portable skill with evidence-first
copy, a complete draft package, and an optional offline lint step. Do not add a
large framework or claim a new category. Evidence-backed profile writing already
exists. The adoption bet is lower friction, Arabic-aware requests, inspectable
claims and a convincing output example, not exclusive invention.

## Compared approaches

| Approach | What the fetched source actually offers | Implication for this skill |
|---|---|---|
| boffti/github-profile-readme | Archetype selection, templates, optional widget builder, supporting references | Good breadth and presentation options. We choose a narrower text-first default; neither approach is universally better. |
| VincentXU0304/github-profile-builder | Reads local work, prefers code over stale docs, rejects padded profiles, delivers README and manual setup guide | A close competitor. Evidence-first positioning is NOT unique to this project. Our package adds explicit evidence levels, review gates and an executable lint tool, not proven superior writing. |
| jdevalk/skills github-profile | Audit, generated README, metadata and widget recommendations, verification | Audit plus complete output is already available. A finished README alone is not a differentiator. |
| birdcar github-profile plugin | Actual account research, generated README/assets and optional dynamic workflows; requires gh | Better fit when a user explicitly wants automation and dynamic widgets. This skill avoids that maintenance by default. |
| rahuldkjain/github-profile-readme-generator | Form-driven README generation with icon, stats and feed options | A lower-friction visual form may beat an agent for quick decoration. Our intended value is interpreting project evidence and writing useful copy. |

These are feature comparisons from fetched project documentation, not execution
benchmarks. We did not run these competitors, verify their survey claims, or
measure their user satisfaction. Popularity does not identify which design caused
adoption. No claim of best-in-market or guaranteed reach is justified.

## Structure decisions

1. Keep name/description in YAML; name remains github-profile-craft.
2. Keep the main file below the standard's 500-line recommendation. Use direct
   references with explicit load conditions, rather than requiring every example
   and evaluation guide on every profile request.
3. Route narrow requests narrowly. A bio edit is not permission for a full profile
   redesign; debugging and general marketing are not profile-skill triggers.
4. Separate live-account evidence from offline snapshots. Never fabricate source
   URLs just to make an evidence ledger look complete.
5. Use deterministic code for repeatable lint, not taste or factual truth. A
   passing script does not mean the biography is accurate or the links resolve.
6. Keep drafts separate from deployment. Installation and platform compatibility
   remain distinct from adherence to the open document format.

## What counts as a useful test

The public authoring guides recommend representative tasks, captured artifacts
and a baseline. We therefore fix the input and scoring rubric before execution.
One thin synthetic profile with inflated marketing and private source material
checks several failure modes cheaply. It does not replace live accounts,
Arabic/bilingual cases, visual-overload cases or different commercial agents.

See ../tests/TEST-RESULTS.md for what actually ran. Fixture definitions are not test passes.

## Source ledger

All below were fetched on 2026-11-21. Sources have no publication date unless
stated on their page; retrieval date is not publication date.

### Primary standards and implementation guidance

- Agent Skills specification, open standard: https://agentskills.io/specification
  Used for required metadata, progressive disclosure and line/size recommendations.
- Agent Skills best practices: https://agentskills.io/skill-creation/best-practices
  Used for concise instructions, explicit reference routing and execution-led revision.
- Anthropic skill-authoring guide: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices
  Used for baseline-first evaluation and iterative tests. Product-specific guidance,
  not independent proof that this particular skill improves results.
- OpenAI evaluation guide: https://developers.openai.com/blog/eval-skills
  Used for captured artifacts, small test sets and deterministic checks. We did
  not execute its Codex harness or claim Codex compatibility testing.

### Product/project primary sources

- https://github.com/boffti/github-profile-readme
- https://github.com/VincentXU0304/github-profile-builder
- https://www.skills.sh/jdevalk/skills/github-profile
- https://github.com/birdcar/claude-plugins/tree/main/plugins/github-profile
- https://github.com/rahuldkjain/github-profile-readme-generator

These establish advertised scope, not independently verified quality.

### Distribution and measurement sources

- Skills directory documentation: https://skills.sh/docs
  The CLI is from vercel-labs/skills. The directory documents install-based
  telemetry; installs are not retained use, satisfaction or GitHub stars.
- GitHub traffic documentation: https://docs.github.com/en/repositories/viewing-activity-and-data-for-your-repository/viewing-traffic-to-a-repository
  Traffic access requires push access; visitors and clones cover the past 14 days.
  Use short comparable windows and preserve snapshots before data rolls off.

### Limits

No independent controlled profile-skill outcome study was found in the checked
sources. Most available sources are standards, vendor guidance and project
self-descriptions. This supports implementation choices, not superiority claims.
The tempting claim that a profile design causes viral adoption remains unproven.
