from APIFunctions import changeTrack, getTrack
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel
from fastapi import FastAPI
from typing import Optional


app = FastAPI()

currentTrack = 0

origins = [
    "file:///C:/Users/aladdin/Desktop/ahlan-salati/FrontEnd/Testing.html"
    "http://192.168.50.189:8080",
    "http://127.0.0.1:8080",
    "https://ahlan-salati.surge.sh/",
    "https://ahlan-salati.surge.sh"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def read_item():
    return ("Sucsuess")


@app.get("/1")
async def text1():
    changeTrack(1)
    return ("Sucsuess")


@app.get("/2")
async def text2():
    changeTrack(2)

    return ("Sucsuess")


@app.get("/3")
async def text3():
    changeTrack(3)
    return ("Sucsuess")


@app.get("/4")
async def text4():
    changeTrack(4)

    return ("Sucsuess")


@app.get("/5")
async def text5():
    changeTrack(5)

    return ("Sucsuess")


@app.get("/6")
async def text6():
    changeTrack(6)

    return ("Sucsuess")


@app.get("/7")
async def text7():
    changeTrack(7)
    return ("Sucsuess")


@app.get("/8")
async def text7():
    changeTrack(8)
    return ("Sucsuess")


@app.get("/9")
async def text7():
    changeTrack(9)
    return ("Sucsuess")


@app.get("/10")
async def text7():
    changeTrack(10)
    return ("Sucsuess")


@app.get("/11")
async def text7():
    changeTrack(11)
    return ("Sucsuess")


@app.get("/12")
async def text7():
    changeTrack(12)
    return ("Sucsuess")


@app.get("/13")
async def text7():
    changeTrack(13)
    return ("Sucsuess")


@app.get("/currentTrack")
async def currentTrackNum():
    return(getTrack())


@app.get("/stop")
async def stopAudio():
    changeTrack(0)
    return ("Sucsuess")
