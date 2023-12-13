# Verifies each line in dataset.txt with openai api
# Outputs 2 csv: 
#   - verified-dataset.csv: contains all lines where gpt agrees with label
#   - clashed-dataset.csv: contains all lines where gpt disagrees with label, and holds for manual inspection
# Outputs log file to data/verify-log.txt
#

import openai
import tiktoken
import logging
import asyncio

class OpenAIRequest:

    def __init__(self, api_key, verifytext):
        self.api_key = api_key
        self.verifytext = verifytext
        self.encoding = tiktoken.get_encoding("cl100k_base")
        self.prompt=self.verifytext.replace("y   ", "")
        self.prompt=self.prompt.replace("n   ", "")
        if self.verifytext.find("y   ") == -1:
            self.isSpam = True
        else:
            self.isSpam = False
        return 


    def getTokenLength(self, text):
        token_num = len(self.encoding.encode(text))
        return token_num
    
    def getResponse(self):
        self.applyTruncication()
        openai.api_key = self.api_key
        self.promptToken = self.getTokenLength(self.prompt)
        self.verifytextToken = self.getTokenLength(self.verifytext)
        self.response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": self.prompt + self.verifytext}],
            temperature=0.0
            )
        self.returnmsg = self.response.choices[0].message.content
        self.returnmsgToken = self.getTokenLength(self.returnmsg)
        self.tokenStats()
        return self.returnmsg

    def tokenStats(self):
        print("Prompt token length: " + str(self.promptToken) + "\nVerify text token length: " + str(self.verifytextToken) + "\nResponse token length: " + str(self.returnmsgToken)+"\nTotal token length: " + str(self.promptToken + self.verifytextToken + self.returnmsgToken) + "\nTotal cost: $" + str(float(self.promptToken + self.verifytextToken + self.returnmsgToken)*0.001*0.002))
        print("Token count from openai API:" + str(self.response.usage.total_tokens)) 
        return

    def writeData(self, judgement):
        match judgement:
            case "verified":
                with open ("data/verified-dataset.csv", "a") as f:
                    f.write(self.isSpam"," + self.prompt + "\n")
            case "clashed":
                with open ("data/clashed-dataset.csv", "a") as f:
                    f.write(self.isSpam"," + self.prompt + "\n")
            case "error":
                with open ("data/error-dataset.csv", "a") as f:
                    f.write(self.verifytext + ","+self.returnmsg+"\n")
            case _:
                print("heh?")
        return
        

        

    def judge(self):
        if self.returnmsg in ["y", "yes", "Y", "Yes", "YES", "1", "true", "True", "TRUE"]:
            if self.isSpam:
                with open ("data/verified-dataset.csv", "a") as f:
                    f.write("1," + self.verifytext + "\n")
            else:
                with open ("data/clashed-dataset.csv", "a") as f:
                    f.write("0," + self.verifytext + "\n")
        elif self.returnmsg in ["n", "no", "N"]:
            if not self.isSpam:
                with open ("data/verified-dataset.csv", "a") as f:
                    f.write("0," + self.verifytext + "\n")
            else:
                with open  ("data/clashed-dataset.csv", "a") as f:
                    f.write("0," + self.verifytext + "\n")
        else:
            with open("data/error-dataset.csv", "a") as f:
                f.write(self.prompt + ","+self.returnmsg+"\n")

            
                


    


def main():
    OpenAIkey = "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"
    r = OpenAIRequest(OpenAIkey, prompt)
    if os.path.exists("data/progress.txt"):
        with open("data/progress.txt", "r") as f:
            try:
                progress = int(f.read())
            except:
                logging.warn("Progress file corrupted, resetting to 0. Original content: " + f.read())
                progress = 0
    else:
        progress = 0
        with open("data/progress.txt", "w") as f:
            f.write(str(progress))
        


    with open("data/dataset.txt", "r") as df:
        lines = f.readlines()

    
    
    
if __name__ == "__main__":
    main()







