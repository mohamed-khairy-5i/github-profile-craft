# Adoption and demo plan

**Status: public repository; promotion remains a plan.** The owner approved
public visibility on 2026-11-21. This is not approval to contact people, submit
listings, post publicly elsewhere or run a campaign. No star-growth experiment
has been run.

## Positioning worth testing

"Turn the work in your repos into a profile someone understands. Finished
Markdown, checkable claims, no badge wall."

Target first: developers with one or two useful projects whose profiles explain
the stack but not the problem solved. This is a proposed audience, not measured
market demand. Evidence-first writing already has competitors, see RESEARCH.md.

## Try it without a long setup

Clone the public repository and put the complete repoproofloom folder in
your agent's documented skills directory. Start a fresh session if required by
that agent. No API key or dependency installation is required by the skill.
The optional lint command needs Python 3.

For a draft-only trial, provide a GitHub username or a small local evidence pack:
current profile text, one project README, and a short inspected implementation
excerpt. Do not provide private client code unless its use is authorized.

Ask:

> Use repoproofloom to produce PROFILE-README.md and PROFILE-PLAN.md.
> Use only the supplied evidence. Lead with the useful behavior of my strongest
> project. Separate source facts from unverified claims. Don't deploy anything.

Arabic trial prompt:

> استخدم repoproofloom وطلعلي README كامل وخطة للبايو والمشاريع المثبتة.
> اعتمد على الشغل الموجود بس، ووضح إيه المتأكد منه وإيه لسه مش متحقق.
> عايز اللي يفتح البروفايل يفهم المشروع بيحل إيه. متغيّرش حسابي دلوقتي.

## Demo storyboard, 25 seconds

A proposed recording, not a claim that a video was made:

- 0-4s: show the supplied generic profile, labeled "synthetic example".
- 4-8s: show the tiny evidence pack, including the unsupported marketing claim.
- 8-17s: show the actual generated README. Highlight one useful project behavior
  and a concrete next step, not a score or simulated star counter.
- 17-22s: open the evidence ledger and show that unverified metrics were omitted.
- 22-25s: show the draft-only boundary and one trial prompt.

Use the exact captured output, not a manually improved result presented as a
raw model run. Keep text large enough to read on a phone. Do not show private
sources, contact details or real account tokens. DEMO.svg is an illustrative
summary, not an execution recording or a GitHub UI screenshot.

## Launch gates, only after owner approval

1. Inspect the repository for private details and source/license obligations.
   Existing examples refer to the owner's real public projects. Confirm that
   they are intended for the proposed audience before widening access.
2. Confirm README, sample, optional script and installation files work from a
   clean local copy. Check actual target-agent discovery and output generation.
3. Record results on at least one additional real profile with consent and an
   Arabic request. Keep failures visible. Do not turn these gates into claimed
   completed tests.
4. If the owner chooses release, decide repository visibility explicitly. Verify
   installation from that actual state before sharing an install command.
5. If the owner wants a listing, verify the directory's current submission and
   private-repository rules. skills.sh documents its installer at
   https://skills.sh/docs . Do not claim a listing or support badge exists yet.

Do not paste an untested universal npx command into the README. A standard
SKILL.md file does not prove compatibility with every agent or installer.

## Small measurement plan

Before an approved release: save a baseline snapshot. After release: inspect
7 comparable days, then a second 7-day period. GitHub traffic retains visitors
and clones for 14 days, so save each snapshot in time. With low volume report
raw counts and avoid percentage hype. Repository traffic is not profile traffic.

Record separately:

- Discovery: repository visitors and referring sites, if available.
- Trial: installs or direct reports of successful installation, with source.
- Usefulness: how many consented testers get a usable draft and what they edit.
- Return use: whether anyone uses it again or recommends it without prompting.
- Stars: optional observed outcome, never the primary quality measure.

Do not estimate conversion across unrelated counters or time windows. Directory
install telemetry and GitHub visitors are not necessarily the same population.
No tracking widgets, bought engagement or unsolicited mass outreach.

A sensible decision rule: if people install but cannot get a complete useful
profile package, fix the output and setup before seeking more attention. If the
output is useful but few people try it, improve the demo and description. This
is a diagnosis framework, not a forecast or a guarantee of virality.

Source for traffic limits:
https://docs.github.com/en/repositories/viewing-activity-and-data-for-your-repository/viewing-traffic-to-a-repository
