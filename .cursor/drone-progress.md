# Drone From Scratch — Checkpoint

Any agent: read this first. Student writes all `.py` code. Coach reviews plans and diagrams, gives snippets in chat only when stuck.

**Updated:** 2026-08-31 (paused — Block 1 diagram done; Python next)

## Goal

Build a drone from humble software beginnings (move a few blocks, like turtle) up to assembling real hardware flown by the student's own Python. Ready-made modules only when there is no safe or realistic alternative.

## How we work

1. Coach names the next tiny block (what to achieve, not how).
2. Student explains the plan and draws a yes/no diagram if decisions exist.
3. Coach confirms or suggests a simpler path.
4. Student types the code. Coach reviews if asked.
5. This file is updated before the session ends.

## Current block

**Block 1 — A drone is just numbers (simulated, on a grid)**

The drone has a position. It can take off, move one block north/south/east/west, and land. It cannot move while on the ground. No hardware. Print `x, y, z` is enough.

Status: **diagram approved.** Picture saved. **No `.py` yet.** Next session is Python structure, then the student types the file.

### Project folder

`my-dream-drone/drone/`

- Diagram source: `my-dream-drone/drone/block-1-descissions.md` (filename typo: descissions; leave unless they rename)
- Rendered picture: `my-dream-drone/drone/block-1-descissions.png`

### Approved rules (implement these in Python)

1. Takeoff while already airborne → do nothing, tell user already in air.
2. Land while already on ground → refuse, tell user.
3. Move while on ground → do not move, tell user to take off first (diagram says “fly first”).
4. East: `x += 1`. West: `x -= 1`. North: `y += 1`. South: `y -= 1`. One command = one block.
5. Takeoff success: `z = 1`. Land success: `z = 0`.
6. `z` is only `0` (ground) or `1` (air). 1 unit = 1 block, not metres.

## Done this session

- Coaching rule + checkpoint so new chats can resume.
- Block 1 yes/no rules agreed.
- Student wrote the mermaid diagram; coach reviewed until it matched the rules.
- PNG render of that diagram saved beside the `.md`.

## Decisions

| Decision | Choice |
|----------|--------|
| Start in simulation, not hardware | yes |
| First model | discrete grid (blocks) |
| Graphics | print `x, y, z` first |
| Student types all code | yes |
| Move unit | 1 = 1 block |
| z for Block 1 | 0 grounded, 1 airborne |
| Diagrams | mermaid inside `.md`; PNG is a preview only |

## Resume here next session (Python)

Do **not** write the student's `.py` file.

1. Ask the student to propose a plan in their own words, then review it:
   - Starting values of `x`, `y`, `z` (suggest 0, 0, 0 if they have no preference).
   - How they will take **one** command (e.g. `input()`).
   - How that command follows the diagram (if/elif matching takeoff, land, move).
2. Keep Block 1 small: one command is enough at first; a loop of commands can be Block 2 unless they want the loop now.
3. After the plan is sound, they type the code. Coach reviews pasted code. Snippets in chat only if stuck.

## Next (only after Block 1 works)

Block 2 later: likely a command loop. Then continuous motion, physics, hardware. Do not jump.

## Open questions

None. Python plan is tomorrow's first message from the student.
