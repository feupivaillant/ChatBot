from rule_manager import RuleManager
from response_manager import ResponseManager

class ConversationManager:
    def __init__(self):
        self.rule_manager = RuleManager()
        self.response_manager = ResponseManager()
        self.process_user_input = ResponseManager()

    def start_conversation(self, false=None):
        print("Comment pouvons-nous vous aidé !")
        while True:
            user_input = input("Utilisateur: ")
            if user_input.lower() == "exit":
                print("Au revoir !")
                break
            response = self.rule_manager.get_response(user_input)
            print("Bot: " + response)

        while false:
            user_input = input("Posez votre question : ")
            response = self.rule_manager.process_user_input(user_input)
            print("Bot: " + response)
