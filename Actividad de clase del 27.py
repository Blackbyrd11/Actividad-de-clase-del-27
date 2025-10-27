import re
import heapq
from collections import defaultdict, deque

class AdaptivePredictor:
    def __init__(self, n=3):
        self.n = n
        self.model = defaultdict(lambda: defaultdict(int))

    def tokenize(self, text):
        return re.findall(r"\b\w+\b", text.lower())

    def train(self, text):
        tokens = self.tokenize(text)
        for i in range(len(tokens) - self.n):
            context = tuple(tokens[i:i+self.n-1])
            next_word = tokens[i+self.n-1]
            self.model[context][next_word] += 1

    def predict(self, context, k=3):
        tokens = self.tokenize(context)
        if len(tokens) < self.n - 1:
            return []
        context_tuple = tuple(tokens[-(self.n-1):])
        candidates = self.model.get(context_tuple, {})
        return heapq.nlargest(k, candidates, key=candidates.get)

    def interact(self):
        print("🧠 Predictor de texto adaptativo (escribe 'salir' para terminar)\n")
        buffer = deque(maxlen=self.n - 1)
        while True:
            context = " ".join(buffer)
            suggestions = self.predict(context)
            if suggestions:
                print(f"Sugerencias: {', '.join(suggestions)}")
            else:
                print("(Sin sugerencias todavía)")
            
            user_input = input("> ").strip()
            if user_input.lower() == "salir":
                break
            
            self.train(user_input)
            buffer.extend(self.tokenize(user_input))

        print("\n✅ Sesión terminada. El modelo ha aprendido de tu texto.")

if __name__ == "__main__":
    texto_inicial = """
    Los modelos de lenguaje predicen la siguiente palabra basándose en contexto.
    Cuanto más texto leen, mejor entienden los patrones.
    """
    predictor = AdaptivePredictor(n=3)
    predictor.train(texto_inicial)
    predictor.interact()