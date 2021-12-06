import requests


def run():
    counter=0
    with open("8000-9000.txt", "a") as myfile:  ##########################################
        x = requests.get("https://api.clashroyale.com/v1/locations/global/seasons", headers={"Accept": "application/json",
                                                                              "authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImZiYTAyMWY3LTllNDEtNDI4NS04MWFkLWI0YmUxNjU0N2E1ZiIsImlhdCI6MTYzNTM0ODY5MSwic3ViIjoiZGV2ZWxvcGVyLzc0ZWQzYzdiLTkzNmYtZmEzZi1lNzBlLTk5ZDVjNTQ1MzlhNyIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyI5NS40NS4xNzUuODciXSwidHlwZSI6ImNsaWVudCJ9XX0.nK6ANzWgu0X7uA9wzfPD4cBZ2bKryqH91gZ3EH85LFw6y09VUU4HhC3yfWE8mhM8YLq3QP1m8tWMF1uvmphcag"},
                         params={})
        lent=len(x.json()["items"])
        while(lent>=0):

            ider = str(x.json()["items"][lent-4]["id"])
            lent-=1
            y = requests.get("https://api.clashroyale.com/v1/locations/global/seasons/"+ider+"/rankings/players", headers={"Accept": "application/json",
                                                                                                 "authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImZiYTAyMWY3LTllNDEtNDI4NS04MWFkLWI0YmUxNjU0N2E1ZiIsImlhdCI6MTYzNTM0ODY5MSwic3ViIjoiZGV2ZWxvcGVyLzc0ZWQzYzdiLTkzNmYtZmEzZi1lNzBlLTk5ZDVjNTQ1MzlhNyIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyI5NS40NS4xNzUuODciXSwidHlwZSI6ImNsaWVudCJ9XX0.nK6ANzWgu0X7uA9wzfPD4cBZ2bKryqH91gZ3EH85LFw6y09VUU4HhC3yfWE8mhM8YLq3QP1m8tWMF1uvmphcag"},
                             params={})
            tempcount=0
            for j in y.json()["items"]:
                if tempcount>=20:
                    break
                tempcount+=1
                tag = j["tag"]
                tag2 = list(tag)
                tag2.remove('#')
                a = (''.join(tag2))
                newTag = "%23" + a
                z = requests.get("https://api.clashroyale.com/v1/players/" + newTag,
                                 headers={"Accept": "application/json",
                                          "authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImZiYTAyMWY3LTllNDEtNDI4NS04MWFkLWI0YmUxNjU0N2E1ZiIsImlhdCI6MTYzNTM0ODY5MSwic3ViIjoiZGV2ZWxvcGVyLzc0ZWQzYzdiLTkzNmYtZmEzZi1lNzBlLTk5ZDVjNTQ1MzlhNyIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyI5NS40NS4xNzUuODciXSwidHlwZSI6ImNsaWVudCJ9XX0.nK6ANzWgu0X7uA9wzfPD4cBZ2bKryqH91gZ3EH85LFw6y09VUU4HhC3yfWE8mhM8YLq3QP1m8tWMF1uvmphcag"})
                try:
                    if z.json()["bestTrophies"]>=8000 and z.json()["bestTrophies"]<9000:
                        counter += 1
                        tempcount=0
                        print("found one ", counter)
                        WinRatio = z.json()["wins"] / (z.json()["losses"] + z.json()["wins"])
                        twoDec = str(round(WinRatio, 2))

                        if (len(twoDec) == 3):
                            twoDec = twoDec + "0"

                        # write data to file
                        myfile.write(z.json()["currentFavouriteCard"]["name"] + " " + str(
                            z.json()["bestTrophies"]) + " " + twoDec + "\n")
                except Exception as e:
                    print(e)