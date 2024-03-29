import requests
import os
ASSEMBLY_API_KEY = os.environ.get("ASSEMBLY_API_KEY")
WEBHOOK_URL = os.environ.get("WEBHOOK_URL")

def uploadToAssemblyAI(filename = "/path/to/foo.wav"):
    def read_file(filename, chunk_size=5242880):
        with open(filename, 'rb') as _file:
            while True:
                data = _file.read(chunk_size)
                if not data:
                    break
                yield data

    headers = {'authorization': ASSEMBLY_API_KEY} 
    response = requests.post('https://api.assemblyai.com/v2/upload',
            headers=headers,
            data=read_file(filename))

    response_data = response.json()
    return response_data
        
def createNewTranscriptRequest(request_data):
    endpoint = "https://api.assemblyai.com/v2/transcript"
    
    headers = {
        "authorization": ASSEMBLY_API_KEY,
        "content-type": "application/json"
    }

    response = requests.post(endpoint, json=request_data, headers=headers)
    response_data = response.json()
    return response_data


def getFiles():
    return ["./example_data/example1.wav", "./example_data/example2.wav", "./example_data/example3.wav"]


def main():
    files = getFiles()
    for file in files:
        upload_response = uploadToAssemblyAI(file)
        request_data = {
            "audio_url": upload_response["upload_url"],
            "webhook_url": WEBHOOK_URL,
        }
        transcript_response = createNewTranscriptRequest(request_data)
        print('Uploaded: ' + transcript_response['id'])
        
     

if __name__ == '__main__':
    main()