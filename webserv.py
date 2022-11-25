from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn
import utility
app = FastAPI()

import random
@app.get("/", response_class=HTMLResponse)
async def root():
    return """
    	<form action='topla'>
    	birinci number
    	<br>
    	<input name='birinci'>
    	<br>
    	ikinci number
    	<br>
    	<input name='ikinci'>
    	<br>
    	<input type='submit' value='topla'>
    	</form>
    """


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


uvicorn.run(app, host="localhost", port=5000)
"""
uvicorn.run(app, host="127.0.0.1", port=6000)
uvicorn.run(app, host="192.168.0.1", port=6000)
uvicorn.run(app, host="localhost", port=6000)
"""