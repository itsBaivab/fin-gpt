from fastapi import FastAPI
from transformers import pipeline
app = FastAPI()

@app.get("/")
def greet_json():
    return {"status": "Its working built by Fayaz"}

# Initialize the text generation pipeline
pipe = pipeline("text2text-generation", model="google/flan-t5-small")
# checking for ofingpt
# ofintech/FinGPT_0.1.3
# pipe = pipeline("text2text-generation", model="MudassirFayaz/llama-2-7b_career_0.6.0", trust_remote_code=True)
# Initialize the text generation pipeline
# model = AutoModelForSeq2SeqLM.from_pretrained("ofintech/FinGPT_0.1.3")
# pipe = pipeline("text2text-generation", model="MudassirFayaz/llama-2-7b_career_0.6.0", tokenizer=tokenizer)


@app.get("/")
def home():
    return {"message":"Hello World"}

# Define a function to handle the GET request at `/generate`


@app.get("/generate")
def generate(text:str):
    ## use the pipeline to generate text from given input text
    output=pipe(text)

    ## return the generate text in Json reposne
    return {"output":output[0]['generated_text']}