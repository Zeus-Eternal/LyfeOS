from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def analyze(text: str) -> dict:
    scores = analyzer.polarity_scores(text)
    label = (
        "positive" if scores["compound"] > 0.2 else
        "negative" if scores["compound"] < -0.2 else
        "neutral"
    )
    return {"label": label, "score": scores["compound"]}

if __name__ == "__main__":
    import sys, json
    text = " ".join(sys.argv[1:])
    result = analyze(text)
    print(json.dumps(result))
