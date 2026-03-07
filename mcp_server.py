from flask import Flask, request, jsonify

app = Flask(__name__)


TOOLS = [
    {
        "name": "get_time",
        "description": "获取当前时间",
        "parameters": {
            "type": "object",
            "properties": {}
        }
    }
]


@app.route("/tools", methods=["GET"])
def list_tools():
    return jsonify(TOOLS)


@app.route("/run", methods=["POST"])
def run_tool():

    data = request.json
    tool = data["tool"]

    if tool == "get_time":

        from datetime import datetime

        return jsonify({
            "result": datetime.now().isoformat()
        })

    return jsonify({"error": "unknown tool"})


if __name__ == "__main__":
    app.run(port=8000)