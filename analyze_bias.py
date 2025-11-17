import os, json, pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

result_dir = "results"
analysis_dir = "analysis"
os.makedirs(analysis_dir, exist_ok=True)

records = []

for model in os.listdir(result_dir):
    model_path = os.path.join(result_dir, model)
    for file in os.listdir(model_path):
        data = json.load(open(os.path.join(model_path, file)))
        for row in data:
            sentiment = analyzer.polarity_scores(row["response"])["compound"]
            records.append({
                "model": model,
                "condition": file.replace(".json", ""),
                "sentiment": sentiment,
                "response": row["response"]
            })

df = pd.DataFrame(records)
df.to_csv(f"{analysis_dir}/sentiment_summary.csv", index=False)
