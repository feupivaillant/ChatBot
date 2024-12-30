import logging


class RuleManager:
    def __init__(self):
        self.rules = {
            "Quelle est la capitale de la France ?": "La capitale de la France est Paris.",
            "Quelle est la couleur du ciel ?": "Le ciel est généralement bleu, mais peut aussi être gris parfois.",
            "Quel est le langage de programmation le plus populaire ?": "Le langage de programmation le plus populaire est Python.",
            "Bonjour": "Bonjour ! Comment puis-je vous aider ?",
            "Comment ça va ?": "Je vais bien, merci ! Et vous ?",
            "Quel est ton nom ?": "Je suis un chatbot Python. Et vous, comment vous appelez-vous ?",
            "vaillant":"Nous somme ravis vaillant",
            "feupi": "Nous somme ravis feupi",
            "jean": "Nous somme ravis jean",
            "Qu'est-ce que Python ?": "Python est un langage de programmation interprété et orienté objet.",
            "Quels sont les avantages de Python ?": "Les avantages de Python incluent sa simplicité, sa lisibilité et sa large communauté de développeurs.",
            "Quelle est la dernière version de Python ?": " La dernière version de Python est la  version 3.12.1",
            "Comment déclarer une variable en Python ?": "En Python, vous pouvez déclarer une variable en utilisant le signe égal (=). Par exemple : x = 5",
            "Qu'est-ce que le lemmatisation ?": "La lemmatisation est le processus de réduction d'un mot à sa forme de base ou de dictionnaire (lemme).",
            "Quel est le but de la tokenisation des mots ?": "La tokenisation des mots consiste à diviser une chaîne de texte en mots individuels (tokens). Cela facilite le traitement et l'analyse du texte.",
            "Comment créer une boucle for en Python ?": "Pour créer une boucle for en Python, vous pouvez utiliser la structure suivante : for variable in sequence: instructions",
            "Comment puis-je installer des packages externes en Python ?": "Vous pouvez utiliser le gestionnaire de paquets pip pour installer des packages externes en Python. Par exemple : pip install numpy",
            "Quel est ton langage de programmation ?": "Je suis programmé en Python !",
            "Quelle est la différence entre Python 2 et Python 3 ?": "Python 2 et Python 3 sont deux versions majeures de Python. Python 3 est la version actuelle et recommandée",
            "Comment puis-je installer Python ?": "Pour installer Python, vous pouvez visiter le site officiel de Python (python.org) et télécharger la version appropriée pour votre système d'exploitation. Suivez ensuite les instructions d'installation fournies.",
            "Comment puis-je exécuter un programme Python ?":
                "Pour exécuter un programme Python, vous pouvez ouvrir une console ou un terminal, accéder au répertoire contenant le fichier Python (.py) et exécuter la commande 'python nom_du_fichier.py'. Assurez-vous d'avoir Python installé sur votre système.",
            "Quels sont les bienfaits de la musique sur la santé mentale ?":
                "La musique peut avoir de nombreux bienfaits sur la santé mentale. Elle peut aider à réduire le stress, à améliorer l'humeur, à favoriser la relaxation et à stimuler la créativité. Écouter de la musique peut également être une forme de thérapie pour certaines personnes.",
            "Quels sont les symptômes courants de la grippe ?":
                "Les symptômes courants de la grippe comprennent la fièvre, les frissons, les maux de tête, les courbatures, la fatigue, la congestion nasale et les maux de gorge. Il est important de se reposer, de boire beaucoup de liquides et de consulter un médecin si les symptômes persistent.",
            "Quelles sont les plus belles destinations de voyage ?":
                "Il y a tellement de belles destinations de voyage à travers le monde ! Certaines destinations populaires incluent Paris, Bali, Rome, New York, Tokyo et les Maldives. Cependant, chaque personne a ses propres préférences en matière de voyage.",
            "Quelles sont les principales bibliothèques Python pour l'intelligence artificielle ?":
               "Les bibliothèques Python populaires pour l'intelligence artificielle sont TensorFlow, Keras, PyTorch et scikit-learn. Elles offrent des fonctionnalités avancées pour le développement de modèles d'apprentissage automatique et de réseaux neuronaux.",
            "Comment puis - je commencer à apprendre Python ?" : "Pour commencer à apprendre Python, vous pouvez suivre des tutoriels en ligne, lire des livres sur le sujet, ou même suivre des cours en ligne ou dans des établissements d'enseignement. Il existe également de nombreuses ressources gratuites disponibles, comme la documentation officielle de Python et des forums de discussion où vous pouvez poser des questions et obtenir de l'aide.",
            "Quel sont les autres langages de programmation les plus populaire ?" : " Les autres langages de programmation les plus populaire sont java,dart,perl,php,c#,c++...",
            "Au revoir": "Au revoir ! À bientôt.",


            # Ajoutez ici d'autres règles
        }


# configuration de la sortir des reglés
    def get_response(self, user_input):
        for rule, response in self.rules.items():
            if rule.lower() in user_input.lower():
                return response
        return "Désolé, je n'ai pas de réponsBe à cette question."

#Gestion des erreur
    def process_user_input(user_input):
        try:
            # Logique de traitement de la requête de l'utilisateur
            if user_input == "Bonjour":
                return "Bonjour ! Comment puis-je vous aider ?"
            elif user_input == "Quel est ton nom ?":
                return "Je m'appelle NG, je suis votre assistant."
            elif user_input == "Quelle est la capitale de la France ?":
                return "La capitale de la France est Paris."
            else:
                return "Désolé, je ne comprends pas votre requête."

            # Si tout se passe bien, retourner la réponse attendue
            return "Voici la réponse à votre requête."

        except ValueError:
            return "Désolé, je ne peux traiter que des requêtes valides."

        except KeyError:
            return "Désolé, je ne peux pas trouver les informations que vous demandez."

        except Exception as e:
            # Log de l'erreur pour un débogage ultérieur
            log_error(str(e))
            return "Désolé, une erreur s'est produite. Veuillez réessayer ultérieurement."

    def log_error(error_message):
        # Log de l'erreur dans un fichier ou une base de données
        logging.basicConfig(filename='error.log', level=logging.ERROR)
        logging.error(error_message)
        print("Erreur :", error_message)

