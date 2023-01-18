import re

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn
import utility
app = FastAPI()

import random
@app.get("/", response_class=HTMLResponse)
async def root():
    return """
    	<form action='sayilaribul'>
    	text
    	<input name='text'>
    	<input type='submit' value='sayilari bul'>
    	</form>
    """



@app.get("/sayilaribul")
async def sayilaribul(text):
	lst = re.findall("[0-9]+", text)
	lst = [int(i) for i in lst]
	return lst


@app.get("/topla")
async def benimtoplamaislemim352547357337539843054(birinci, ikinci):
    return {"result": int(birinci) + int(ikinci)}

# print( benimtoplamaislemim352547357337539843054( 3, 5 ) )
@app.get("/area")
async def rastgeleisim(r):
    return {"result": utility.alanHesapla( float(r) ) }


@app.get("/forecast")
async def fslfjdlfjfls():
    return {"result": random.randint(1000, 20000) }


"""
import socket
hostname=socket.gethostname()
IPAddr=socket.gethostbyname(hostname)
print("Your Computer Name is:"+hostname)
print("Your Computer IP Address is:"+IPAddr)

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
print(s.getsockname()[0])
s.close()
"""
uvicorn.run(app, host="0.0.0.0", port=5000)
"""
uvicorn.run(app, host="127.0.0.1", port=6000)
uvicorn.run(app, host="192.168.0.1", port=6000)
uvicorn.run(app, host="localhost", port=6000)
"""

# 172.16.0.126
