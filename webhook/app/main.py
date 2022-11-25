from fastapi import FastAPI, Response, Request
import json
import datetime

assembly_ip_address = ["44.238.19.20", "127.0.0.1"]

def getTranscript(transcript_id):
    # get transcript from AssemblyAI
    pass

def saveToDatabase(row):
    print(row)
    # save row to database
    pass



app = FastAPI()
#fast api post route to receive webhook
@app.post("/")
async def webhook(request: Request): 
    # ip = str(request.client.host)
    # if ip not in assembly_ip_address:
    #     return Response(status_code=401)
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
    saveToDatabase({transcript_id, status, timestamp, completed_transcript})
    #return response 2XX
    return Response(status_code=200)
    
    
