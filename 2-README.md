# github-profile-tuner

An Agent Skill that audits and upgrades a GitHub profile: the profile README,
bio, links, pinned repos, and top-repo metadata. Built to be handed to any
agent that reads the open `SKILL.md` format.

Give it to your agent and say "ظبط بروفايلي على جيت هاب" or "level up my
GitHub profile" - it audits what exists, scores it against a checklist, picks
one coherent style, and rewrites substance-first.

## Install

Clone or copy this folder into your agent's skills directory:

- Claude Code: `~/.claude/skills/github-profile-tuner`
- Cursor: `~/.cursor/skills/github-profile-tuner`
- OpenAI Codex: `~/.codex/skills/github-profile-tuner`
- Any other agent that reads SKILL.md files: its documented skills directory

```bash
git clone https://github.com/mohamed-khairy-5i/github-profile-tuner \
  <skills-dir>/github-profile-tuner
```

No dependencies. The whole skill is `SKILL.md`.

## What it does

1. Verifies the profile-README mechanic (repo named exactly your username,
   public, README.md on the default branch).
2. Audits your README, bio, pinned repos, and top repos.
3. Scores against a checklist (first 15 lines, contact path, alt text, stale
   widgets, leftover placeholders).
4. Picks one archetype that matches your upkeep tolerance.
5. Rewrites substance-first, shows you the draft, then helps you ship it.
6. Verifies rendering in light and dark themes and on mobile.

## Credits

Approach grounded in public work, notably
[boffti/github-profile-readme](https://github.com/boffti/github-profile-readme)
(nine archetypes, 520-profile survey) and the open
[Agent Skills](https://agentskills.io) format.

## License

MIT
