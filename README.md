## [AssembylAI Webhooks](https://www.assemblyai.com/docs/walkthroughs#using-webhooks)

### [Video Tutourial](https://www.loom.com/share/e046f0b2ad2f4a16b51f82d45295d58c)

### Cloudflare Tunnels
###### Note: Cloudflare is required to be DNS provider
- [How do they work](https://developers.cloudflare.com/cloudflare-one/connections/connect-apps)
- [Pricing](https://blog.cloudflare.com/tunnel-for-everyone/)
- [Setup & Installation](https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/install-and-setup/tunnel-guide/remote/)

### Code Example

#### ```upload.py```
```python
def main():
    files = getFiles()
    for file in files:
        upload_response = uploadToAssemblyAI(file)
        request_data = {
            "audio_url": upload_response["upload_url"],
            "webhook_url": WEBHOOK_URL,
        }
        transcript_response = createNewTranscriptRequest(request_data)
        print(transcript_response)
```

#### ```webhook.py```
```python
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
```
- [Create a tunnel](https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/install-and-setup/tunnel-guide/remote/#1-create-a-tunnel)

### Deployment Example

Prepare Linux Box (Ubuntu 22.04)

1. ```sudo apt update -y```
2. ```sudo apt install python3-pip```
3. ```cd /opt```
4. ```git clone https://github.com/GarvanD/assemblyai_webhook```
    ##### Note: When Authenticating Github CLI, you must use an [Access Token](https://github.com/settings/tokens) as your password

Start Upload Process

1. Chage directory to /upload
2. ```pip3 install -r requirements.txt```
3. ```ASSEMBLY_API_KEY=YourAPIKey WEBHOOK_URL=YourWebhookURL python3 upload.py``` 

Start Webhook Process

1. Change directory to /webhook
2. ```pip3 install -r requirements.txt```
3. ```ASSEMBLY_API_KEY=YourAPIKey uvicorn app.main:app --host 127.0.0.1 --port 8000```




#### ```Authentication & Security```
- [Whitelist AssemblyAI IP Address - Python](https://github.com/GarvanD/assemblyai_webhook/blob/main/webhook/app/main.py#L31)
- [Whitelist AssemblyAI IP Address - Cloudflare](https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/install-and-setup/tunnel-guide/remote/#3-connect-a-network)
- [Secure VM with OS & Cloud Firewall](https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/do-more-with-tunnels/secure-server/)
- [Add Authorization Header](https://www.assemblyai.com/docs/walkthroughs#using-webhooks)











