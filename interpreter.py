import shutil

import pyttsx3
import datetime
import webbrowser


class Interpreter:
    def __init__(self):

        # SET ASSISTANT NAME
        self.assname = "Arty"

        # SET ENGINE PROPERTIES
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)
        voices = self.engine.getProperty("voice")

        print("Voices: ", voices)

        self.u_gender = 'Monsieur'

        # GREET USER
        self.greet()

        # ask user name
        # self.usrname()

    def speak(self, audio):
        self.engine.say(audio)
        self.engine.runAndWait()

    def greet(self):
        hour = int(datetime.datetime.now().hour)
        if hour >= 0 and hour < 12:
            self.speak(f"Bonjour {self.u_gender} !")

        elif hour >= 12 and hour < 18:
            self.speak(f"Bon après midi {self.u_gender} !")

        else:
            self.speak(f"Bonsoir à {self.u_gender} !")

        # PRESENTATION
        self.speak(f"Je m'appelle {self.assname}, je suis votre assistant.")
        # self.speak(self.assname)

    def usrname(self):
        self.speak("Comment puis-je vous appeler?")

        self.speak("Bienvenue venue à vous")

        self.speak("Que puis-je faire pour vous?")

    def interpret(self, query):

        if 'ouvrez youtube' in query:
            self.speak("Here you go to Youtube\n")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            self.speak("Here you go to Google\n")
            webbrowser.open("google.com")


        elif 'quelle heure' in query:
            strTime = datetime.datetime.now().strftime("% H:% M:% S")
            self.speak(f"Maintenant, il est {strTime}")


        elif 'écrit à' in query or 'envoie un message' in query or 'envoyez un message' in query:

            self.speak("Désolé, je me trouve dans l'incapacité d'envoyer un message pour le moment.")


        elif 'comment tu vas' in query or 'comment vous allez' in query or "vous allez bien" in query:
            self.speak("Je vais bien, Merci.")
            self.speak(f"Et vous {self.u_gender}?")

        elif 'je vais bien' in query or "Très bien" in query:
            self.speak("Je suis heureuse de l'entendre.")


        elif "comment on t'appele" in query or "c'est quoi ton nom" in query:
            self.speak("Mes amis m'appelent")
            self.speak(self.assname)


        elif 'te quitter' in query or 'te laisse':
            print(query)
            self.speak("Merci de m'avoir accordé votre temps.")

        elif "qui t'a créer" in query:
            self.speak("J'ai été créée par Monsieur Antaress.")

        elif 'recherche' in query:

            query = query.replace("cherche", "")
            webbrowser.open(query)

        elif "qui je suis" in query:
            self.speak("Vous êtes .")

        elif "pourquoi tu es venu au monde" in query:
            self.speak("Je remercie Antaress, c'est un secret.")


        elif "c'est quoi l'amour" in query or "l'amour c'est quoi":
            self.speak("C'est le septième sens qui détruit les autres sens.")

        elif "qui es-tu" in query or "tu es qui":
            self.speak("Je suis simplement votre assistant virtuel. Créée par Antaress.")

        elif "ta raison d'être" in query:
            self.speak("J'ai été créé pour un petit projet par Antares. ")

        elif 'les nouvelles' in query:
            self.speak("Pour l'instant ")


        elif "n'écoute plus" in query or "Arrête de m'écouter" in query:
            self.speak("D'accord.")

        elif "note quelque part" in query or "écrit une note" in query:
            self.speak("Malheureusement je n'ai pas de stylo sur moi")


        elif "Albatros" in query:

            wishMe()
            self.speak("Albatros ici point o in your service Mister")
            self.speak(assname)

        elif "meteo" in query:

            temperature = random.randraint(20, 26)
            self.speak(f"Maintenant il fait {temperature} dans la ville de Goma, ma ville natale")

        elif "être ma copine" in query or "tu peux être ma copine" in query:
            self.speak("Je ne suis pas sur, veullez me laisser un peu de temps pour que j'y refléchisse.")

        elif "comment ça va" in query:
            self.speak("ça va bien, ")

        elif "je t'aime" in query:
            self.speak("Je suis contente de l'entendre.")

        else:
            self.speak("Désolé mais je ne vous entend pas bien!S")


if __name__ == "__main__":
    run = Interpreter()