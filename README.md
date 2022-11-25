## [AssembylAI Webhooks](https://www.assemblyai.com/docs/walkthroughs#using-webhooks)



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
- [Create a webhook endpoint]()
- [Create a tunnel](https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/install-and-setup/tunnel-guide/remote/#1-create-a-tunnel)

### Deployment Example


#### ```Authentication & Security```
- [Whitelist AssemblyAI IP Address - Python]()
- [Whitelist AssemblyAI IP Address - Cloudflare](https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/install-and-setup/tunnel-guide/remote/#3-connect-a-network)
- [Additional Security with Cloudflare](https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/do-more-with-tunnels/secure-server/)
- [Add Authorization Header]()



#### ```Deployment```
- [Docker Build]()
- [Local Setup]()
- [Docker Compose]()










