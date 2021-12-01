import requests
import json
token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImUzODdiMDUyLTA3MTctNDUzNi05YjExLTBmNDUzZDY3ZjAxNiIsImlhdCI6MTYzODM2MDAxNSwic3ViIjoiZGV2ZWxvcGVyL2Q4ODYxNGIwLTVkOTMtYmEzYS0wNzZhLWE2NTZiMjMyNTE1YyIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyIxMzQuMjI2LjIxNC4yNTEiXSwidHlwZSI6ImNsaWVudCJ9XX0.Fvw06gVLRP4opOUVd7wd-qjKdTEKvUUXVjFtT5_NwlPF30tjsQyPF49ijCjJrzBSO4iVBGX30_ib5ZTWcFQQDQ"
r=requests.get("https://api.clashroyale.com/v1/locations/57000000/rankings/clans", headers={"Accept":"application/json", "authorization":"Bearer "+token}, params = {"limit":50})
data1 = r.json()
data2 = data1['items']
clanArray = []
playerArray = []
size = len(data2)
for d in range (size):
    data = data2[d]
    #print(data['members'],"\n")
    testData = data['members']
    if(testData > 45):
        clanArray.append(data['tag'])

size = len(clanArray)
for x in range (size):
    currentClan = clanArray[x]
    currentClanFormatted = currentClan.replace("#","%23")
    r = requests.get("https://api.clashroyale.com/v1/clans/"+currentClanFormatted+"/members", headers={"Accept":"application/json", "authorization":"Bearer "+token})
    data1 = r.json()
    data2 = data1['items']
    for y in range (len(data2)):
        data = data2[y]
        #print(data['tag'])
        playerArray.append(data['tag'])
print("")   #Added so I can use breakpoints to check variables
        

    
