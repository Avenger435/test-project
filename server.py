
from fastapi import FastAPI
from typing import List
import uvicorn

app = FastAPI()


@app.get("/", summary="Root")
def read_root():
    return {"message": "FastAPI is running", "items": ["item1", "item2"]}


@app.get("/items", summary="List items")
def list_items() -> List[str]:
    return ["apple", "banana", "cherry"]


if __name__ == "__main__":
    # Default FastAPI port is 8000
    uvicorn.run("server:app", host="127.0.0.1", port=8000, log_level="info")
