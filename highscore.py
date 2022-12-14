class HighScore:

    def get_high_score():
        # Le score de base est 0
        high_score = 0

        # On essaie de lire le fichier
        try:
            high_score_file = open("high_score.txt", "r")
            high_score = int(high_score_file.read())
            high_score_file.close()
        except IOError:
            # Le fichier n'existe pas, on ne peut pas le lire
            print("There is no high score yet.")
        except ValueError:
            # Erreur de conversion, on ne peut pas convertir le contenu du fichier en entier
            print("Starting with no high score.")
        return high_score

    def save_high_score(new_high_score):
        try:
            # On essaie d'écrire dans le fichier
            high_score_file = open("high_score.txt", "w")
            high_score_file.write(str(new_high_score))
            high_score_file.close()
        except IOError:
            # Quelque chose s'est mal passé lors de l'écriture du fichier
            print("Unable to save.")
    


    