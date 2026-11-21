---
name: github-profile-tuner
description: >-
  Audit and upgrade a GitHub profile: the special profile README (the repo named
  exactly after the username), the bio and links, pinned repos, and the metadata
  of the top repositories. Use whenever someone wants to improve, fix, tune,
  redesign, or "level up" their GitHub profile or profile README, asks why their
  profile README is not showing, or wants their GitHub to look more professional
  to recruiters, clients, or collaborators. Arabic triggers: "ظبط بروفايل جيت
  هاب", "حسّن البروفايل", "بروفايلي على جيت هاب وحش". Works for creating a
  profile README from zero or upgrading an existing one.
license: MIT
---

# GitHub Profile Tuner

Turn "fix my GitHub profile" into a finished, coherent profile built from the
person's real work. Substance first, decoration last.

## The mechanic that makes or breaks everything

A GitHub profile README only renders when ALL of these hold:

- A repo named **exactly** the username exists (`github.com/<user>/<user>`,
  case included).
- It is **public**.
- It has a `README.md` in the root of the **default branch** (check whether it
  is `main` or `master`; image URLs hardcoding the wrong branch silently 404).

If the README "is not showing", check these before touching any content.

## Workflow

Do the human parts before writing any markdown.

### 1. Audit the current state

Collect, in this order, stopping when you have enough:

- The profile README content, if the special repo exists.
- The account bio, profile links, and avatar (visible on `github.com/<user>`).
- The pinned repositories and up to 3 highest-signal other repositories: their
  About description, topics, and the first screen of their README.
- What the person actually wants from the profile (jobs, freelance clients,
  open-source users) and how much upkeep they will tolerate. If they are vague,
  ask 2-3 sharp questions instead of guessing. Never fabricate roles,
  employers, metrics, or achievements; if a claim cannot be verified from
  their repos or their own words, leave it out.

Quick commands when `gh` is available and authorized:

```bash
gh api users/<user>                                  # bio, blog, location
gh repo view <user>/<user>                           # profile repo + README
gh api users/<user>/repos --jq '.[].name'            # repo list
```

### 2. Score against the checklist

Report only findings that change the next action, not the whole list:

- First 15 lines: do they say who this is, what they build, and where a
  visitor goes next? "Passionate developer" filler fails here.
- One clear contact or next step (site, LinkedIn/X, email).
- Tech stack pruned to what they actually use, one consistent badge style.
- Every image has meaningful `alt` text; intro is real text, not text baked
  into an image.
- No stale or broken widgets (dead stats services, "No activity" feeds).
- No leftover placeholders and no *other person's* username, feed URL, branch,
  or stats URL in copied snippets - the most common genre mistake.
- Pinned repos tell a story: each has a real description and topics.
- Repo names and About texts across the profile are consistent and specific.

### 3. Pick exactly one archetype

Choose by maintenance tolerance, personality, and what to lead with. Resist
mixing more than one accent.

| Archetype | Lead with | Upkeep | Best for |
|---|---|---|---|
| Minimalist / Prose-First | A few honest sentences | None | The safest default; signal over noise |
| Badge / Icon Card | Stack + socials at a glance | Low | People who'd rather not write much |
| Stats Dashboard | Live activity cards | Low | Daily contributors |
| Visual Showcase | Hero banner/GIF | Low | Design-minded, friendly first impression |
| Descriptive Resume | About/Skills/Experience | Low | Job hunters with real credentials |
| Code-as-Bio | About written as code | Low | A memorable coder flex |
| Self-Updating / Automated | Always-fresh injected content | Automated | People who ship or blog often |

Quick rule by time budget: none -> Minimalist. Low but visual -> Badge or
Visual. Some -> Stats, Resume, or Code-as-Bio. Ongoing automation appetite ->
Self-Updating. A clean Minimalist profile never looks bad; a kitchen-sink page
usually does.

### 4. Rewrite, substance first

1. Heading/greeting, then a 1-3 line identity statement in real prose.
2. The archetype body.
3. A tidy link row: one badge style (`flat-square` OR `for-the-badge`, never
   both) or plain text links, with real verified URLs.
4. Widgets only if the archetype calls for them; pass the same theme and
   `hide_border=true` to every stats card so they read as one system. Tuck
   streaks, trophies, and counters inside `<details>` or omit them.
5. Automation (blog feeds, WakaTime) only if they will maintain it; stale
   automation advertises neglect.

Show the draft and get the person's OK before committing anything to their
repositories. Keep their voice; write in the language they use on their
profile.

### 5. Verify before declaring done

- Confirm the commit landed on the default branch of the right repo.
- Open the profile page and confirm it renders; check light AND dark themes
  and a narrow/mobile width.
- Click every link and load every image.

## Principles

- Substance over decoration. Specific prose beats a pile of widgets.
- One coherent style, one theme. Consistency is the polish.
- Accessibility is quality: alt text everywhere, real text for the intro,
  restraint with motion and fancy Unicode.
- Only show what gets maintained. A simple page that stays true beats a
  dynamic one that rots.
- Scrub every copied snippet of other people's handles and URLs.
- Never invent credentials. An honest small profile beats an inflated one.

## Credits and further reading

This skill's approach is grounded in public work on GitHub profiles:

- `boffti/github-profile-readme` - nine-archetype model calibrated against a
  2026 survey of 520 public profile READMEs, plus a pitfalls checklist:
  https://github.com/boffti/github-profile-readme
- The open Agent Skills format (SKILL.md with name/description frontmatter):
  https://agentskills.io
