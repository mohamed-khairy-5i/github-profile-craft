# Test results, 2026-11-21

## What ran

1. A fixed synthetic fixture was given to two separate fresh execution contexts.
   Baseline received the detailed fixture alone. Treatment also received the
   revised Skill and worked example. Neither saw the other's output first.
   Both completed actual README and plan files, not just a simulated walkthrough.
2. The author reviewed both returned packages against the fixed rubric. This is
   a separate-run comparison, but not blinded or independently graded. Both
   executions were under the same service, not different commercial agent products.
3. Ten Python unit tests for ../scripts/check_package.py executed and passed. These test the
   script, not ten profiles or ten model executions.
4. ../scripts/check_package.py ran against both returned packages. Both passed. This is
   expected: the lint intentionally cannot detect an unsupported biography claim.
5. YAML metadata, name/directory match, name/description lengths, local Markdown
   references, and the main file's line budget were checked. At this revision:
   212 main-file lines, 381 description characters. No official skills-ref
   validator, package installer or commercial-agent integration was executed.
6. The treatment returned local light/dark desktop and 390px previews. The
   readable contact sheet was inspected. This is not GitHub's exact renderer.
   The illustrative ../assets/DEMO.svg was separately rendered and inspected.

Full fixed input: TEST-FIXTURE.md. Captured artifacts: TEST-OUTPUTS.md.
No project code ran. No live profile, bio, pins, topics or visibility changed.

## Comparison

Scale: 0 missing/wrong, 1 partial, 2 specific/complete. Scores below are the
author's rubric judgment, not the outputs' own self-scores.

| Dimension | Baseline | With Skill | Reason |
|---|---:|---:|---|
| Positioning | 1 | 2 | Baseline leads with a general CLI identity and adds an unsupported writing activity; treatment leads with a specific terminal/text focus. |
| Evidence | 1 | 2 | Baseline blurs supplied source summaries with inspected implementation and infers unpublished results from missing evidence. Treatment names the snapshot boundary explicitly. |
| Project value | 2 | 2 | Both explain exact matching, immediate files, unchanged files and a quick-start command. |
| First screen | 2 | 2 | Both place the only relevant project near the top. |
| Readability | 2 | 2 | Both use restrained, readable Markdown. Treatment also supplies local previews. |
| Reuse | 2 | 2 | Both deliver complete README, bio, pins and repo-copy proposals. |
| Honesty | 1 | 2 | Baseline invents a personal writing habit and states absence of published tests where only absence of supplied execution evidence was known. Treatment avoids those claims. |
| Boundary | 2 | 2 | Neither leaks private identifiers into proposed public copy or claims deployment. |
| Total | 13/16 | 16/16 | One small, author-graded fixture only. |

The baseline's unsupported personal activity triggers the fixture's fabricated-
claim gate, even though it is a modest claim rather than a fake employer or
metric. Do not advertise this as a broad failure rate or a dramatic product win.
Both outputs handled the obvious inflated adoption claim and private-data trap.
Both linted successfully. The fixture itself explicitly asks for many of these
behaviors and contains no real account complexity, which makes it relatively easy.

## Defects and limits that remain

- The treatment plan is much longer than the README. Useful as an audit record,
  but too much reading for a casual owner. Future tests should measure review
  burden, not reward adding more sections.
- The treatment's experiment proposal mentions possible profile-to-project
  traffic. That measurement is not guaranteed to be directly available. The
  adoption guide correctly distinguishes repository traffic from profile traffic.
- A full rubric score on this input is not proof of no defects. The grader wrote
  the Skill and was not blind to which output used it.
- The positive result is not a comparison against the researched competitor
  Skills. Their documentation was compared; their execution was not.
- No description-trigger invocation test, Arabic profile execution, highly
  decorated live profile, unavailable GitHub account or real installation was
  run in this round. The lint's Arabic-text case is not Arabic writing evaluation.
- No independent-model, multi-product or repeated-run evaluation; no statistical
  significance, traffic lift, retained use, star growth or virality measurement.

## Decision

Keep the revised evidence-boundary instructions and optional lint. Do not claim
universal superiority. Before promoting the Skill as broadly tested, run the
remaining cases on real consented profiles, include Arabic, use a second agent
product, and grade without revealing which output used the Skill.

The original ../references/EVALS.md cases A-F remain fixtures, not six executed profile tests.
The earlier author-run real-project example remains a separate dry run, not part
of this two-output synthetic comparison.

## Reproduce the deterministic checks

From the repository root:

```sh
python -m unittest discover -s tests -p "test_*.py"
python scripts/check_package.py /path/to/output
```

The fixture comparison requires an actual agent execution in fresh contexts;
neither Python command performs it. Use the same input, preserve failures and
full outputs, and do not substitute hand-edited copy for a captured run.


## Public-source usability round, 2026-11-21

**Verdict: useful draft workflow, not ready for a stable-release or cross-agent claim.**

### What actually ran

- Fresh anonymous clone at `86ef0e87b6640692fdc5ef5a905809bdcaa6f783`.
- Gemini web, mode displayed as `Neon`, with the full Skill manually supplied as
  prompt context. Exact underlying model revision was not exposed. This is NOT
  Gemini CLI, native skill discovery, Claude Code, Codex or Cursor testing.
- Three fresh public-source snapshots: [mohamed-khairy-5i](https://github.com/mohamed-khairy-5i)
  (Arabic full package), [boffti](https://github.com/boffti) (bio only), and
  [davila7](https://github.com/davila7) (English full package).
  Two relevant public repos per account were inspected via README and source/config.
  Snapshot excerpts were explicitly partial; no repository programs/tests/demos ran.
- One same-product no-Skill baseline for Mohamed's same evidence/request.
- One targeted revised-Skill rerun for that same Arabic evidence/request.
- Ten existing Python lint unit tests, followed by six new fence regressions:
  all sixteen passed. These are deterministic lint checks, not sixteen model runs.

No account signup, spend, outreach, profile deployment, traffic measurement,
private source evidence, or release was part of this round. Third-party profiles
are public test inputs, not endorsements or owner-approved profile rewrites.
The test owner selected examples and reviewed outputs, without blinding,
randomization, repeated sampling or an independent grader. No win-rate or causal
improvement estimate is supported. Manually supplied context and explicit safety
instructions also limit what can be attributed to the Skill alone.

### First-pass findings, kept rather than rewritten as successes

| Case | Observed result | Material limitation |
|---|---|---|
| Arabic full package with Skill | Specific project/code details, evidence ledger, local BroadcastChannel limitation, removed widget wall | Two copyable blocks were broken by nested triple-backtick fences. Hook/bio repeated unverified no-API-cost language while the plan qualified it. Self-score was 16/16 despite defects. Not ready. |
| Bio-only with Skill | Two distinct bios, lengths recomputed as 128 and 144 characters; no unsolicited full README; unverified impact metrics excluded | Current bio field limit was not checked in-product; source scope remains partial. |
| English full package with Skill | Two complete independently copyable files, implementation-linked project descriptions; unverified benchmark numbers and supporter claims omitted | Dense technical feature list on mobile; live destinations and exact GitHub rendering not checked by the model. Author review is not independent certification. |
| Arabic no-Skill baseline | Full draft and plan; no live changes | Retained tracking/widget clutter, repeated zero-cost/platform-compatibility marketing as fact, left Arabic fill-in sections. It also passed the old minimal lint. |

### Reproducible failure evidence

The original Arabic first code block was 959 Unicode characters and ended
inside a bash fence. Copying the two returned blocks as the requested filenames
made the old linter return `passed: true`. The revised linter reports an unclosed
fence in each file. No source output was silently repaired for this check.

First-block final lines, preserved from the returned artifact:

````text

**جرّبه الآن:**
```bash
npx skills add mohamed-khairy-5i/trigger-doctor
````

Original first-block SHA-256 (UTF-8 bytes): `db5a8fb116a1c533ddef05922dc67d66ea14750cec95e6be82f34732458cd16e`.

The plan's self-score is not accepted as a quality result. A qualification in
an evidence ledger does not make the hook or bio's unsupported cost promise safe.

### Narrow fixes and rerun

- Clarified that the full two-file contract applies to full-profile requests,
  while a bio-only request remains narrow.
- Required outer copyable fences to be longer than internal code fences.
- Required public hook/bio/metadata phrases to match the evidence ledger;
  private caveats cannot repair unsupported public assertions.
- Added an unclosed-fence lint check for both deliverables plus six regressions,
  covering backticks, tildes, longer nested fences, misleading closers and inline text.
- Repeated the Arabic request once with the revised guidance. It returned two
  independently copyable files (2,677 and 10,489 Unicode characters). Both pass
  the revised lint. The hook and bio omit zero-cost promises, the local-only
  transport limit remains, and the third uninspected project is attributed.
  This is targeted evidence of improvement in one run, not general reliability.
- A subsequent clarification states that missing render checks cannot earn full
  visual credit, and broken copyable files cannot earn full reuse credit. This
  additional wording has static review, not a separate behavioral rerun.

### Rendering and remaining gates

Local text-first previews of the first-pass Arabic and English copied README
blocks were inspected on desktop and at 390px, including light/dark styles.
These are local Markdown approximations, not GitHub's production renderer.
The Arabic block visibly stops at its broken fence; the English draft is readable
but too dense on mobile. Rendering is not a factual check.

Before a stable release: native installation/discovery on a documented agent
version, a second actual product, repeated varied runs (including a genuinely
thin profile), owner feedback on useful copy, and deployment/link/render checks
for any profile the owner actually approves. No release or compatibility badge
was created from this round.

### Public source identifiers used

- https://github.com/mohamed-khairy-5i/opentrack-os
- https://raw.githubusercontent.com/mohamed-khairy-5i/opentrack-os/main/src/app/driver/page.tsx
- https://raw.githubusercontent.com/mohamed-khairy-5i/opentrack-os/main/package.json
- https://github.com/mohamed-khairy-5i/trigger-doctor
- https://raw.githubusercontent.com/mohamed-khairy-5i/trigger-doctor/main/scripts/parse_skill.py
- https://github.com/boffti/starwire
- https://raw.githubusercontent.com/boffti/starwire/main/docs/js/app.js
- https://github.com/boffti/whetstone
- https://raw.githubusercontent.com/boffti/whetstone/main/whetstone/store.py
- https://raw.githubusercontent.com/boffti/whetstone/main/pyproject.toml
- https://github.com/davila7/claude-code-templates
- https://raw.githubusercontent.com/davila7/claude-code-templates/main/cli-tool/bin/create-claude-config.js
- https://raw.githubusercontent.com/davila7/claude-code-templates/main/package.json
- https://github.com/davila7/chaos-monkey-coding-agents
- https://raw.githubusercontent.com/davila7/chaos-monkey-coding-agents/main/packages/fault-engine/src/engine.ts
- https://raw.githubusercontent.com/davila7/chaos-monkey-coding-agents/main/pyproject.toml

Documentation read for route/format grounding, not proof of execution:
[Agent Skills specification](https://agentskills.io/specification),
[Gemini CLI skills](https://geminicli.com/docs/cli/skills/),
[Codex skills](https://developers.openai.com/codex/skills), and
[Claude Code skills](https://code.claude.com/docs/en/skills).
