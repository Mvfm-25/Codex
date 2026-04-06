# Game Pitch: *coldCuts* — A Procedural Roguelike

## Core Hook (one sentence)
A terminal roguelike where every dungeon is a living organism — grown from scratch using cellular automata, saved to disk, and replayable forever.

---

## Strongest Selling Points

**1. Procedural generation with personality**
The cave generation isn't just random noise — it uses Conway-like cellular automata rules (neighbor counting, mutation chance) to grow organic, cave-shaped layouts. Each dungeon gets a **procedurally named title** ("Caverna Maldita dos Condenados"), a creation date, and is saved as a `.txt` file. This is a distinguishing technical and aesthetic detail.

**2. Persistent, shareable dungeons**
Generated dungeons are exported as plain-text files in `/masmorras/`. Players can share their best dungeons, replay favorites, or load community maps. This is a natural social hook that most jam games miss entirely.

**3. A "lore-through-loot" system**
Items teach you words. When you pick up an item, it adds an entry to your character's `dicionario` (glossary). This is a subtle but original mechanic — exploration rewards aren't just gold or XP, they're *knowledge*. It echoes games like *Dwarf Fortress* or *Caves of Qud* in ambition.

**4. Class system with hidden stats**
The four classes (Bárbaro, Mago, Cavaleiro, Ladrão) have differentiated HP, armor, accuracy, and XP scaling, but most stats are **hidden from the player**. This creates emergent tension and replayability without UI clutter.

**5. Directional numpad combat**
Using numpad 1–9 for 8-directional movement *and* attack targeting is a classic roguelike design that most modern games have abandoned. It's a deliberate callback — and it works.

**6. Portals as dimensional travel**
Entering a portal doesn't just load the next level — it picks a random dungeon from the saved pool, drops you in it, and awards XP. The dungeon isn't consumed. This creates a loop where old generated content stays relevant.

---

## What to Emphasize vs. Downplay

| Emphasize | Downplay (for now) |
|---|---|
| The cellular automata engine as the creative foundation | That enemies are stationary |
| The persistent dungeon file system | The lack of a FOV/fog-of-war system |
| The glossary/knowledge mechanic | The terminal-based rendering |
| The handmade music integration | Debug `print()` statements still in code |

---

## One-Line Pitch
> *"A roguelike where the dungeons grow like living caves, remember their names, and outlive every run."*
