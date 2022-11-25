from fastapi import FastAPI, Response, Request
import json
from datetime import datetime
import requests

ASSEMBLY_API_KEY = ""

assembly_ip_address = ["44.238.19.20"]

def getTranscript(transcript_id):
    endpoint = "https://api.assemblyai.com/v2/transcript/"  + transcript_id 
    headers = {
        "authorization": ASSEMBLY_API_KEY,
    }
    response = requests.get(endpoint, headers=headers)
    response_json = response.json()
    return response_json

def saveToDatabase(transcript_id, status, created_at, json_data):
    print(transcript_id, status, created_at)



app = FastAPI()

#fast api post route to receive webhook
@app.post("/")
async def webhook(request: Request): 
    ip = str(request.client.host)
    if ip not in assembly_ip_address:
        print("Unauthorized IP Address")
        print(ip)
        return Response(status_code=401)
    #get request body
    body = await request.body()
    #convert request body to json
    body_json = body.decode('utf-8')
    #load json into dictionary
    body_dict = json.loads(body_json)
    #get transcript id from dictionary
    transcript_id = body_dict['transcript_id']
    #get status from dictionary
    status = body_dict['status']
    #get timestamp
    timestamp = datetime.now()
    #get completed transcript from assemblyai
    completed_transcript = getTranscript(transcript_id)
    #save to database
    #UUID | transcript_id | status | timestamp | assemblyai_response
    saveToDatabase(transcript_id, status, timestamp, completed_transcript)
    #return response 2XX
    return Response(status_code=200)
    
    
