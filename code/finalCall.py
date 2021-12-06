import requests

def run():
    lister=[110,249,94,248,38]
    finished=False
    i=0
    counter=0
    x = requests.get("https://api.clashroyale.com/v1/locations", headers={"Accept": "application/json",
                                                                          "authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImZiYTAyMWY3LTllNDEtNDI4NS04MWFkLWI0YmUxNjU0N2E1ZiIsImlhdCI6MTYzNTM0ODY5MSwic3ViIjoiZGV2ZWxvcGVyLzc0ZWQzYzdiLTkzNmYtZmEzZi1lNzBlLTk5ZDVjNTQ1MzlhNyIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyI5NS40NS4xNzUuODciXSwidHlwZSI6ImNsaWVudCJ9XX0.nK6ANzWgu0X7uA9wzfPD4cBZ2bKryqH91gZ3EH85LFw6y09VUU4HhC3yfWE8mhM8YLq3QP1m8tWMF1uvmphcag"},
                     params={})
    with open("8000-9000.txt", "a") as myfile:  ##########################################
        while(finished==False):

            id = str(x.json()["items"][lister[i]]["id"])
            y = requests.get("https://api.clashroyale.com/v1/locations/"+id+"/rankings/players", headers={"Accept": "application/json",
                                                                                                             "authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImZiYTAyMWY3LTllNDEtNDI4NS04MWFkLWI0YmUxNjU0N2E1ZiIsImlhdCI6MTYzNTM0ODY5MSwic3ViIjoiZGV2ZWxvcGVyLzc0ZWQzYzdiLTkzNmYtZmEzZi1lNzBlLTk5ZDVjNTQ1MzlhNyIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyI5NS40NS4xNzUuODciXSwidHlwZSI6ImNsaWVudCJ9XX0.nK6ANzWgu0X7uA9wzfPD4cBZ2bKryqH91gZ3EH85LFw6y09VUU4HhC3yfWE8mhM8YLq3QP1m8tWMF1uvmphcag"},
                                             params={})
            for j in y.json()["items"]:
                if counter>3000:
                    finished=True
                    break

                tag = j["tag"]
                tag2 = list(tag)
                tag2.remove('#')
                a = (''.join(tag2))
                newTag = "%23" + a
                z = requests.get("https://api.clashroyale.com/v1/players/" + newTag,
                                 headers={"Accept": "application/json",
                                          "authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImZiYTAyMWY3LTllNDEtNDI4NS04MWFkLWI0YmUxNjU0N2E1ZiIsImlhdCI6MTYzNTM0ODY5MSwic3ViIjoiZGV2ZWxvcGVyLzc0ZWQzYzdiLTkzNmYtZmEzZi1lNzBlLTk5ZDVjNTQ1MzlhNyIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyI5NS40NS4xNzUuODciXSwidHlwZSI6ImNsaWVudCJ9XX0.nK6ANzWgu0X7uA9wzfPD4cBZ2bKryqH91gZ3EH85LFw6y09VUU4HhC3yfWE8mhM8YLq3QP1m8tWMF1uvmphcag"})
                if z.json()["bestTrophies"] >= 8000 and z.json()["bestTrophies"] < 9000:  #############################
                    counter+=1
                    print("found one ", counter)
                    WinRatio = z.json()["wins"] / (z.json()["losses"] + z.json()["wins"])
                    twoDec = str(round(WinRatio, 2))

                    if (len(twoDec) == 3):
                        twoDec = twoDec + "0"

                    # write data to file
                    myfile.write(z.json()["currentFavouriteCard"]["name"] + " " + str(
                        z.json()["bestTrophies"]) + " " + twoDec + "\n")

            i+=1
