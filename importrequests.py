import requests
import json
r=requests.get("https://api.clashroyale.com/v1/locations/57000000/rankings/clans", headers={"Accept":"application/json", "authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjAzNWIzMTA3LWI3YzctNDIwMy04ZjNiLTllYmFhY2E3NTA0ZCIsImlhdCI6MTYzNzU3OTk1OCwic3ViIjoiZGV2ZWxvcGVyL2Q4ODYxNGIwLTVkOTMtYmEzYS0wNzZhLWE2NTZiMjMyNTE1YyIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyIxMzQuMjI2LjIxNC4yNDkiXSwidHlwZSI6ImNsaWVudCJ9XX0._SWpDy0w-3PYL2_oZqFksR7QQO0AWeXHU00qoVT5ddXs8YJa4OawLQmIGHp8t5Lo73nm2JgaPUiSFsLruCyUcw"}, params = {"limit":50})
data1 = r.json()
data2 = data1['items']
clanArray = []
size = len(data2)
for d in range (size):
    data = data2[d]
    print(data['members'],"\n")
    testData = data['members']
    if (testData > 35):
        

    
