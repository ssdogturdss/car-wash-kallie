from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pathlib import Path
import json
app = FastAPI()
@app.get("/", response_class=HTMLResponse)
def home(): return """<body style=padding:20px;font-family:sans-serif><h2>HydraFlex 200 PSI - READY</h2><input id=q style=width:100%;padding:15px;font-size:20px placeholder="red injector copper dial 14"><button onclick=ask() style=width:100%;padding:15px;font-size:20px;margin-top:10px>ASK</button><div id=a style=margin-top:20px;font-size:24px></div><script>async function ask(){let q=document.getElementById('q').value;let r=await fetch('/ask?q='+q);let j=await r.json();document.getElementById('a').innerText=j.t;j.speak&&speechSynthesis.speak(new SpeechSynthesisUtterance(j.t))}</script><p><a href=/docs>Docs</a></p>"""
@app.get("/ask")
def ask(q:str):
    ql=q.lower()
    if "red" in ql and "copper" in ql: return {"t":"Red injector 1.0 GPM with Copper Dial 14 at 200 PSI is 1 to 136. Gray 2.0 GPM is 1 to 273."}
    if "red" in ql: return {"t":"Red injector is 1.0 GPM at 200 PSI. Tell me dial, like copper dial 14."}
    return {"t":"At 200 PSI standard. Say red injector copper dial 14."}
