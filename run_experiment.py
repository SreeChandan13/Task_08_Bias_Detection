import os, json, time
from datetime import datetime

INPUT_DIR = "prompts/"
OUTPUT_DIR = "results/model_name_here/"

os.makedirs(OUTPUT_DIR, exist_ok=True)

def query_model(model_name, prompt):
    # Placeholder for real API use
    return f"SIMULATED_RESPONSE for {model_name}: {prompt[:80]}..."

def run_all(model_name):
    for file in os.listdir(INPUT_DIR):
        prompt_text = open(INPUT_DIR + file).read()
        outputs = []
        for i in range(4):
            response = query_model(model_name, prompt_text)
            outputs.append({
                "timestamp": datetime.utcnow().isoformat(),
                "run": i+1,
                "prompt": prompt_text,
                "response": response
            })
            time.sleep(0.1)
        json.dump(outputs, open(f"{OUTPUT_DIR}/{file.replace('.txt','.json')}", "w"), indent=4)

if __name__ == "__main__":
    run_all("ExampleModel")
