import requests

def uploadToAssemblyAI(filename = "/path/to/foo.wav"):
    def read_file(filename, chunk_size=5242880):
        with open(filename, 'rb') as _file:
            while True:
                data = _file.read(chunk_size)
                if not data:
                    break
                yield data

    headers = {'authorization': "YOUR-API-TOKEN"} 
    response = requests.post('https://api.assemblyai.com/v2/upload',
            headers=headers,
            data=read_file(filename))

    response_data = response.json()
    return response_data
        
def createNewTranscriptRequest(request_data):
    endpoint = "https://api.assemblyai.com/v2/transcript"
    
    headers = {
        "authorization": "YOUR-API-TOKEN",
        "content-type": "application/json"
    }

    response = requests.post(endpoint, headers=headers)
    response_data = response.json()
    return response_data


# def main():
    # get files from ftp server
    # files = get_files_from_ftp()
    # for file in files:
        #calculate optimal duration of each chunk
        #chunk_duration = file.duration / AssemblyAI Concurrency Limit
        #split file into chunks
        #for each chunk
            #upload chunk to AssemblyAI
            #get response from AssemblyAI
            #save response to database
                #UUID | transcript_id | status | timestamp
        

     

# if __name__ == '__main__':
#     main()