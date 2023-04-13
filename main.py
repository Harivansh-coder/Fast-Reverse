from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/reverse/{string_to_reverse}")
def read_item(string_to_reverse: str):
    return {"reverse string": string_to_reverse[::-1]}
