import joblib


class IntentTypes:
    GREETINGS = "Saudações"
    DAILY_FORTUNE = "Sorte do dia"
    PRAYER = "Oração"
    WORKOUT_MOTIVATION = "Motivação para treinar"
    OTHER = "Outros"


class IntentClassifier:
    def __init__(self):
        self.clf = joblib.load("./pretrained_models/intent_classifier_embed.pkl")
        self.le = joblib.load("./pretrained_models/intent_label_encoder.pkl")
        self.embedder = joblib.load("./pretrained_models/embedder.pkl")

    def get_label(self, text):
        embedding = self.embedder.encode([text])
        pred = self.clf.predict(embedding)
        label = self.le.inverse_transform(pred)[0]
        return {"intent": label}


if __name__ == "__main__":
    llm = IntentClassifier()
    print(f"Oi Charlie: {llm.get_label('Oi Charlie')}")
    print(f"Sorte: {llm.get_label('Sorte do dia')}")
    print(f"Sujeito de sorte: {llm.get_label('Você é um sujeito de sorte')}")
