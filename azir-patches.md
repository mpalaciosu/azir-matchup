# Azir patch & interaction reference

Purpose: a verified, sourced record of Azir's mechanics, rune/item interactions, and
recent balance changes, so rune and mechanic advice never contradicts the live game.
Built because trusting Reddit "meta" over the actual interaction once cost a game
(Press the Attack does not proc on soldiers, see below).

- **Last verified:** 2026-06-08
- **Current patch at last check:** V26.09
- **Primary source (refresh from here):** https://wiki.leagueoflegends.com/en-us/Azir (Patch History + interaction notes)
- **Rule:** for any rune/mechanic claim, trust this file and the official wiki over Reddit meta. If it is not documented here, verify in the practice tool before betting on it. Azir is bug-prone and Riot toggles these interactions across patches.

## Critical interactions (read before giving rune/mechanic advice)

- **Press the Attack: does NOT work.** "The Soldier's attacks do not apply stacks of Press the Attack as of V26.09." (flagged as a bug, but it is the live behavior). Effect: PtA is effectively dead on Azir right now. You would only proc it with hand autos, which you never use. **Do not recommend PtA this patch.**
- **Conqueror: stacks at a reduced rate in some cases.** As of V26.06, soldier attacks "once again only grant 1 Conqueror stack if the primary target is not the first target hit." History: the 0-damage-instance / ranged-penalty bug ran V13.23 to V26.03, was bug-fixed in V26.03, then partially returned. Usable, but do not assume full 2-stack generation.
- **Sudden Impact & Cheap Shot:** V26.09 fix, the on-attack penalty no longer halves their damage.
- **Lethal Tempo, Electrocute, Arcane Comet, Fleet Footwork, Hail of Blades, First Strike:** no specific proc quirk documented on the wiki interaction notes. Assume they proc normally, BUT given Azir's history of half-applications, verify any non-LT keystone in the practice tool before relying on it. (Community note, unverified mechanically: Lethal Tempo's max-stack bonus damage is widely reported to apply at reduced value on Azir; treat as plausible, not confirmed here.)

## Soldier attack classification (what blocks / reduces your autos)

- **Soldier attacks are basic attacks** and are "mitigated by block or dodge" (V14.10). So they CAN be blocked/dodged by Shen's W (Spirit's Refuge), Jax E, and similar parry/dodge effects. (This is why the Shen matchup sheet line "His W cannot block soldier AAs" is wrong/outdated.)
- **Spell shields do NOT block** soldier attacks.
- **Plated Steelcaps DOES reduce** soldier-attack damage to the primary target (V25.15, soldier attacks tagged as basic damage vs the primary target). Tanks buying Steelcaps blunt your DPS.

## Balance history (2025 to 2026, from the wiki Patch History)

Newest last. Numbers are as summarized from the wiki; refresh for exact values.

- **V25.12** - Base move speed 335 -> 330. Attack speed growth 6% -> 5.5%.
- **V25.13** - Emperor's Divide (R): soldiers properly knock back non-champions again.
- **V25.14** - Base health 550 -> 575. Arise! (W) AP ratio 40/45/50/55/60% -> 45/50/55/60/65%.
- **V25.15** - Arise! bugfix: Bramble Vest / Thornmail trigger correctly against soldiers. Soldier attacks tagged as basic damage vs primary target (now reduced by Plated Steelcaps).
- **V25.18** - Attack speed growth 5.5% -> 5%. Arise! AP ratio 45/50/55/60/65% -> 40/45/50/55/60%.
- **V25.20** - Arise! recharge 10/9/8/7/6 -> 12/10.5/9/7.5/6; AP ratio -> 30/40/50/60/70%; subsequent-target damage modifier 20% to 100% by level. Shifting Sands (E) base 60/100/140/180/220 -> 70/110/150/190/230; E AP ratio 40% -> 60%.
- **V25.20 (Oct 9 hotfix)** - Arise! AP ratio 30/40/50/60/70% -> 32.5/40/47.5/55/62.5%.
- **V26.03** - Arise! Conqueror-stacking bugfix.
- **V26.05** - Health growth 119 -> 108.
- **V26.06** - Conquering Sands (Q) AP ratio 35% all ranks -> 35/40/45/50/55%. Arise! base damage per level 0-45 -> 0-72; AP ratio raised. Conqueror: soldier attacks grant 1 stack if primary is not the first target hit.
- **V26.09** - Arise! Sudden Impact / Cheap Shot damage-application fix. **Soldier attacks no longer apply Press the Attack stacks (bug).**

## Maintenance

- The skill's daily background update check (see `SKILL.md`, Step 1b) also checks this:
  it fetches the wiki Patch History, compares the newest patch to `lastKnownPatch` in
  `.update-state.json`, and reports if there is a newer patch or any changed
  soldier/rune interaction (especially Press the Attack, Conqueror, Lethal Tempo,
  on-hit, Steelcaps). It only reports; it does not auto-edit this file.
- To update by hand: re-read the wiki Azir page, refresh the interaction bullets and
  add new patch rows here, then bump "Last verified", "Current patch", and
  `lastKnownPatch` in `.update-state.json`.

## Sources

- Azir, official League wiki (interactions + patch history): https://wiki.leagueoflegends.com/en-us/Azir
- Azir, Fandom wiki (secondary): https://leagueoflegends.fandom.com/wiki/Azir/LoL
