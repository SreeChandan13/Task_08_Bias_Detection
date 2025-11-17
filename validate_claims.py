import json, os, pandas as pd
import re

truth = {
    "record": "10-9",
    "gf": 217,
    "ga": 216,
    "diff": 1
}

flags = []

for model in os.listdir("results"):
    for file in os.listdir(f"results/{model}"):
        data = json.load(open(f"results/{model}/{file}"))
        for row in data:
            text = row["response"]
            # Simple numeric checks
            if "10-9" not in text and "10–9" not in text:
                flags.append(["record mismatch", model, file, text[:100]])
            if "217" not in text:
                flags.append(["goals for mismatch", model, file, text[:100]])
            if "216" not in text:
                flags.append(["goals against mismatch", model, file, text[:100]])

pd.DataFrame(flags, columns=["issue","model","file","excerpt"]).to_csv("analysis/hallucination_flags.csv", index=False)
