import torch
from fastapi import FastAPI

app = FastAPI()

@app.get("/speculative-decoding")
def speculative_decoding():
    return {"message": "Speculative Decoding Service"}
