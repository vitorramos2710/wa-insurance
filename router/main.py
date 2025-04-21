from fastapi import FastAPI, Request
import json

app = FastAPI()

@app.get("/healthz")
def health():
    return "ok"

@app.post("/webhook")
async def webhook(req: Request):
    data = await req.json()
    print("Received:", json.dumps(data)[:300])
    return {"status": "received"}

