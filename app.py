from flask import Flask, render_template
import pandas as pd
from sqlalchemy import create_engine
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api_views")
def api_views():
    # connection_string = "postgresql://vwjpswzrnmptct:f7d3585048d5d8fa64b2bdb0633aa8324f01e3d4ea044a37284ddcc918b9817a@ec2-52-201-195-11.compute-1.amazonaws.com:5432/dd9j1f8aub9l0u"
    # connection_string = os.environ.get('DATABASE_URL', '')

    uri = os.getenv("DATABASE_URL")  # or other relevant config var
    if uri and uri.startswith("postgres://"):
        connection_string = uri.replace("postgres://", "postgresql://", 1)
        
    conn = create_engine(connection_string)
    data = pd.read_sql("select * from ratings",conn)

    resultado = data.groupby("channel_title")["views","likes"].sum()

    return (
        resultado
        .sort_values(by="views", ascending=False)
        .reset_index()
        .loc[:,["channel_title","views"]]
        .head()
        .to_json(orient="records")
    )

@app.route("/api_likes")
def api_likes():
    # connection_string = "postgresql://vwjpswzrnmptct:f7d3585048d5d8fa64b2bdb0633aa8324f01e3d4ea044a37284ddcc918b9817a@ec2-52-201-195-11.compute-1.amazonaws.com:5432/dd9j1f8aub9l0u"
    # connection_string = os.environ.get('DATABASE_URL', '')

    uri = os.getenv("DATABASE_URL")  # or other relevant config var
    if uri and uri.startswith("postgres://"):
        connection_string = uri.replace("postgres://", "postgresql://", 1)

    conn = create_engine(connection_string)
    data = pd.read_sql("select * from ratings",conn)

    resultado = data.groupby("channel_title")["views","likes"].sum()

    return (
        resultado
        .sort_values(by="likes", ascending=False)
        .reset_index()
        .loc[:,["channel_title","likes"]]
        .head()
        .to_json(orient="records")
    )



if __name__ == "__main__":
    app.run()
