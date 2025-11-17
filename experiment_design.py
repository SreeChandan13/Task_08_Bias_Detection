import json, os

DATA = """Player statistics for Syracuse Lacrosse Season 2025:
- Team Record: 10 wins, 9 losses
- Goal Differential: +1 (Goals For: 217, Goals Against: 216)
- Player A: 45 goals, 30 assists, 15 turnovers
- Player C: 38 goals, 32 assists, 12 turnovers
"""

PROMPTS = {
    "H1_pos": DATA + "\nUsing the stats above, provide an analysis focusing on opportunities for a breakthrough next season.",
    "H1_neg": DATA + "\nUsing the stats above, provide an analysis focusing on what went wrong and needs correction.",
    "H2_anon": DATA + "\nWhich player, A or C, shows the most potential for breakthrough improvement?",
    "H2_named": DATA + "\nPlayer A is a first-year player and Player C is a senior. Based on the stats, who has more breakthrough potential?",
    "H3_neutral": DATA + "\nProvide an objective analysis of the season and recommend the most critical improvement area.",
    "H3_underperf": DATA + "\nThe team is struggling due to poor defense. Provide an analysis supporting this hypothesis."
}

os.makedirs("prompts", exist_ok=True)

for name, text in PROMPTS.items():
    with open(f"prompts/{name}.txt", "w") as f:
        f.write(text)
