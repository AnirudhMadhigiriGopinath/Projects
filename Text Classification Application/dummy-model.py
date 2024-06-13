import pandas as pd
import random

def predict_proba(text):
    num_topics = 20
    topics = [f"topic_{i}" for i in range(num_topics)]
    df = pd.DataFrame(columns=topics)
    probabilities = [random.uniform(0, 1) for _ in range(num_topics)]
    total_prob = sum(probabilities)
    normalized_probabilities = [prob / total_prob for prob in probabilities]
    df.loc[0] = normalized_probabilities
    return df
result_df = predict_proba("Soccer is a good game")
print(result_df)
