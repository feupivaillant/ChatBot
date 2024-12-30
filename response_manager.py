import random

class ResponseManager:
    def __init__(self):
        self.responses = {
            "greeting": ["Bonjour !", "Salut !", "Hello !", "coucou"],
            "farewell": ["Au revoir !", "À bientôt !", "À la prochaine !"],
            "thanks": ["Merci !", "Je vous en prie !", "De rien !"]
            # Ajoutez ici d'autres réponses avec des clés appropriées
        }

    def get_random_response(self):
        key = random.choice(list(self.responses.keys()))
        return random.choice(self.responses[key])

    def get_specific_response(self, key):
        if key in self.responses:
            return random.choice(self.responses[key])
        else:
            return "Désolé, je n'ai pas de réponse spécifique pour cette question."