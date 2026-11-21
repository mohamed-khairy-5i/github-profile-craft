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
