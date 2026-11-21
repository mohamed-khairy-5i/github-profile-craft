# GitHub Profile Tuner

## Make the work memorable. Then make the profile look like it.

A portable Agent Skill for turning a scattered GitHub presence into a clear,
evidence-backed showcase. Not another wall of badges. Not a star generator.

**Input:** a GitHub username or supplied project evidence.

**Output:** a finished profile README, a concise bio, a reasoned pin order,
project descriptions/topics, an evidence ledger, and a verification checklist.
Nothing changes on the actual profile until the owner approves.

## Use it

Give the folder to an agent that supports the open `SKILL.md` format and say:

> Improve my GitHub profile. Lead with what makes my real work distinctive.
> Produce the finished files for review; do not change my live profile yet.

Or in Arabic:

> ظبط بروفايلي وخلي الشغل الحقيقي هو اللي يشد الناس. طلّعلي نسخة كاملة
> أراجعها، مش شوية نصايح وبادچات. متعدّلش البروفايل قبل ما أوافق.

### Install

Clone this repository, then place the **whole folder**, including `EXAMPLE.md`
and `EVALS.md`, in your agent's documented skills directory. Keep the folder
name `github-profile-tuner`. No package installation or API key is required by
the skill itself. Your agent needs its own GitHub reading capability.

This repository is private unless its owner changes that setting. Another
agent needs authorized repository access or a local copy. Do not paste access
tokens into prompts. Installation paths and support vary by agent version;
use that agent's current documentation, rather than assuming one universal path.

## What changed in v2

| Before | Now |
|---|---|
| An audit and a presentation archetype | Finished README plus profile package |
| Generic style choices | One angle derived from the builder's actual work |
| Repository marketing repeated as fact | Observed, owner-stated, unverified evidence separated |
| Optional polish | First-screen, mobile, accessibility and link checks |
| No test fixtures | Six acceptance scenarios and a worked dry run |

[Read the worked example](EXAMPLE.md) to see the level of specificity.
[Read the evaluation cases](EVALS.md) to test an agent's output.

## What it will not do

- Invent users, clients, titles, test results, benchmarks, or testimonials.
- Promise stars, reach, search ranking, or hiring outcomes.
- Publish private information or change your profile without approval.
- Install tracking widgets, buy engagement, or send unsolicited launch posts.

The output is a draft package. A profile preview is not a deployed profile.
Static checks and one worked dry run are not cross-agent certification.

## Files

- `SKILL.md`: the reusable workflow and output contract.
- `EXAMPLE.md`: evidence-backed example using public project descriptions and
  limited code inspection, with a clear verification boundary.
- `EVALS.md`: acceptance fixtures, scoring, and the test record.
- `LICENSE`: MIT.

## Sources and credit

Built against the [Agent Skills specification](https://agentskills.io/specification)
and [skill-authoring guidance](https://agentskills.io/skill-creation/best-practices).
Profile mechanics follow [GitHub's own documentation](https://docs.github.com/en/account-and-profile/how-tos/setting-up-and-managing-your-github-profile/customizing-your-profile/managing-your-profile-readme).
The earlier version drew presentation inspiration from
[boffti/github-profile-readme](https://github.com/boffti/github-profile-readme).
No third-party benchmark claims are implied by this skill.

## License

MIT
