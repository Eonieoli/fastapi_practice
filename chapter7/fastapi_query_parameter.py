from fastapi import FastAPI

app = FastAPI()

@app.get("/hi")
def greet(who):
    return f"hello? {who}?"