#! /usr/bin/env python3
# coding: utf-8

import os
from flask import Flask, request, redirect, jsonify, url_for, session, abort
from flask_cors import CORS

from openai.lib.azure import AzureOpenAI
from chatconfig import ToolBot

from dotenv import load_dotenv
load_dotenv()

# ########## INIT APP ##########

# --- API Flask app ---
app = Flask(__name__)
app.secret_key = "super secret key"
# app.config["MAX_CONTENT_LENGTH"] = 1024 * 1024 * 200

CORS(app)


# ########## Init Chat Client ##########

client = AzureOpenAI(
    azure_endpoint=os.environ.get("AZURE_OPENAI_ENDPOINT"),
    api_key=os.environ.get("AZURE_OPENAI_API_KEY"),
    api_version=os.environ.get("AZURE_OPENAI_API_VERSION"),
)
model = os.environ.get("AZURE_OPENAI_DEPLOYMENT_MODEL_NAME")
tool_bot = ToolBot(client, model)

# ########## API ENTRY POINTS (BACKEND) ##########

@app.route("/")
# @app.doc(hide=True)
def index():
    """Define the content of the main fontend page of the API server"""

    return f"""
    <h1>The Inference API server is up.</h1>
    """

@app.route("/inference", methods=['POST'])
def inference():
    """Infer using the ToolBot"""

    query = request.form.get("query")
    response = tool_bot.send_query(query)
    return jsonify(response)

# ########## START FLASK SERVER ##########

if __name__ == "__main__":

    current_port = int(os.environ.get("PORT") or 5000)
    app.run(debug=False, host="0.0.0.0", port=current_port, threaded=True)
