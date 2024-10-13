from flask import Flask, request

app = Flask(__name__)


@app.get("/greet")
def route_greet():
    greeting = request.args.get("greeting", "Hello")
    name = request.args.get("names", "friend")
    return {"message": f"{greeting} {name}"}
