import openai
from gtts import gTTS
from audioplayer import AudioPlayer

openai.api_key = #put your api key here


class Utils:
    def __init__(self):
        self.output = ""
        self.path = "output.mp3"

    def speech(self, words, display=False):
        try:
            words = str(words)
        except ValueError:
            print("Ce n'ai pas une chaine de caractère")
        if words == "":
            raise ValueError("Je ne parle pas")
        else:
            if display is False:
                output = gTTS(text=words, lang="fr", slow=False)
                output.save("output.mp3")
                AudioPlayer(self.path).play(block=True)
            else:
                for word in (
                    words.replace(",", ",###")
                    .replace(".", ".###")
                    .replace("?", "?###")
                    .split("###")
                ):
                    print(word.strip())
                    if word.strip():
                        output = gTTS(text=word, lang="fr", slow=False)
                        output.save("output.mp3")
                        AudioPlayer(self.path).play(block=True)

class ChatGTP:
    def __init__(self):
        self.utils = Utils()
        self.input_user = ""

    def chat_with_IA(self):
        while self.input_user != "Q":
            self.input_user = self.utils.listen().capitilzed()
            # self.input_user = input("Tapez votre texte ici\n> ").capitalize()
            if not self.input_user:
                print("ce champ ne peut pas être vide")
            elif self.input_user == "Q":
                break
            else:
                # create a chat completion
                chat_completion = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": self.input_user}],
                )
                self.utils.speech(
                    chat_completion.choices[0].message.content, display=True
                )


chat = ChatGTP()
if __name__ == "__main__":
    chat.chat_with_IA()
