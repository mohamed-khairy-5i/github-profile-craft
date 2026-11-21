# Worked dry run: proof before polish

Date: 2026-11-21. This is a draft demonstration, not a deployed profile or a
claim that the skill was benchmarked across different agents.

The example uses only Mohamed's already-public repository information and a
limited inspection of two source/config files. It does not expose private
account data. It is deliberately narrower than a full profile audit: current
pins, every public repo, and live demos were not fully inspected.

## Positioning decision

Compare: generic full-stack developer, visual map builder, or builder of tools
that make hidden software behavior visible. Choose the last as a provisional
angle: it connects a wrong-account testing lab with a route/GPS interface
without inventing a job title or customers.

Chosen hook: **The tool call passed. The wrong account changed.**

Rejected hook: **Building the next generation of intelligent applications.**
It could describe almost anyone and offers no reason to open a project.

## Example PROFILE-README.md

The block below is complete proposed copy. It has not been applied.

```markdown
# Mohamed Khairy | محمد خيري

### The tool call passed. The wrong account changed.

I build tools that make software behavior easier to inspect, from AI agents
choosing between accounts to browser-based route and GPS interfaces.

## Start with Agent Account Lab

An agent can have permission to both accounts and still change the wrong one.
[Agent Account Lab](https://github.com/mohamed-khairy-5i/agent-account-lab)
explores that failure with synthetic accounts, mock file operations, and
trace-based evaluation.

The question is not only "did the call succeed?" It is "did the intended
account and file change?"

**For:** people building or evaluating tool-using agents.
**Open:** the repository for scenarios, evaluation rules, and setup.

## Also building: OpenTrack OS

[OpenTrack OS](https://github.com/mohamed-khairy-5i/opentrack-os) explores
browser-based mapping, routing, and GPS interfaces with Arabic and English UI.
Its local driver code uses browser geolocation and a BroadcastChannel for
same-origin browser messaging. It is a prototype, not a claim of a complete
cross-device fleet backend.

**For:** developers exploring a map or driver interface.
**Open:** the repository to inspect the implementation and setup.

## Inspect the work

Start with the synthetic account scenarios, or inspect the browser driver
implementation. Both repositories explain their setup and scope.

[Explore the testing lab](https://github.com/mohamed-khairy-5i/agent-account-lab)
```

## Example PROFILE-PLAN.md

### Bio proposal

> Building tools that make software behavior visible: AI-agent account testing,
> browser maps, and Arabic/English interfaces.

This is a draft. Check the current live bio field limit before applying.

### Pin and metadata proposals

1. **agent-account-lab** first, because it illustrates one clear failure in a
   memorable sentence. About: "Synthetic multi-account tests for tool-using
   agents: detect successful operations against the wrong account."
   Topics: `agent-testing`, `multi-account`, `tool-calling`, `synthetic-data`.
2. **opentrack-os** second, as a more visual supporting artifact. About:
   "Browser map and driver-interface prototype with routing, geolocation,
   and Arabic/English UI."
   Topics: `geolocation`, `leaflet`, `typescript`, `rtl`, `prototype`.

This is a two-project example, not a final recommendation over all public repos.
Do not unpin other work without auditing it and getting approval.

### Evidence ledger

| Claim | Evidence and level | Boundary |
|---|---|---|
| Account-selection testing is the lab's focus | Public repository README, owner-stated | Not an independent performance evaluation |
| The lab defines test and validation scripts | `package.json`, observed by file read | Commands were not run |
| Driver code uses geolocation and BroadcastChannel | `src/app/driver/page.tsx`, observed by file read | No cross-device backend or end-to-end behavior verified |
| Map project offers Arabic/English UI | README and inspected driver code | Full language coverage not tested |

Sources checked on 2026-11-21:

- https://github.com/mohamed-khairy-5i/agent-account-lab
- `package.json` retrieved from that repository through GitHub's file API.
- https://github.com/mohamed-khairy-5i/opentrack-os
- `src/app/driver/page.tsx` retrieved from that repository through GitHub's file API.

### Before/after improvements

- Replace broad identity copy with a precise wrong-account failure hook.
- Replace stack-first project labels with problem, behavior, and next action.
- Drop unverified numerical scores and zero-cost/production guarantees.

### Highest-value next evidence

- Capture one short, reproducible lab trace showing a wrong-account mutation
  and the evaluator flagging it. Label mock/synthetic data on the capture.
- Verify a documented map setup, then capture the actual working interface.
- Resolve the map's local-browser messaging boundary before suggesting a real
  fleet use case. A polished screen does not establish a fleet backend.

### Honest experiment

If the owner approves a profile update and has traffic access, compare traffic
and referring sources over comparable periods before/after, noting release or
posting changes. Do not attribute every star to the README. No traffic data was
read for this example.

### Checks

- Public source descriptions read: yes.
- Two code/config files read: yes.
- Profile changes: none.
- External metrics or real-model benchmarks reproduced: no.
- End-to-end map/demo tested: no.
- Full profile and pin audit: no, this is a limited example.
- Render and structural checks: see the creation test record in EVALS.md.

## Why this is more than a nicer adjective

The first line points to a specific failure. The featured project explains who
would use it. The second project is described without claims its inspected
transport cannot establish. The result still needs real demonstration assets,
but it gives an agent a concrete standard to meet rather than "make it pop."
