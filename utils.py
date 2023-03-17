import openai

class OpenAi:
    MODEL_ENGINE_DEFUALT = "code-davinci-002" # You Can change Model Engine Name for see all Models read this document "https://platform.openai.com/docs/models/"

    def __init__(self,api_key, model_engine=MODEL_ENGINE_DEFUALT, max_tokens=300, temperature=0.5, count_response=1):
        self.openai = openai 
        self.api_key = api_key # Your Api Key
        self.model_engine = model_engine # Model ENgine
        self.max_tokens = max_tokens # max token For use
        self.temperature = temperature # The level of creativity
        self.n_response = count_response # Number Response For return

        self.openai.api_key = api_key

    def chat_io(self,text):
        completion = openai.Completion.create(
            engine=self.model_engine,
            prompt=text,
            max_tokens=self.max_tokens,
            n=self.n_response,
            stop=None,
            temperature=self.temperature,
        )

        response = completion.choices[0].text.strip() # Getting the raw answer

        return response
