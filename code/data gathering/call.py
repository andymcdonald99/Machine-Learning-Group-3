import requests




def run():
        leagues = [0, 300, 600, 1000, 1300, 1600, 2000, 2300, 2600, 3000, 3400, 3800, 4200, 4600, 5000]
        names = {"goblin stadium", "bone pit", "barbarian bowl", "p.e.k.k.a's playhouse", "spell valley",
             "builder's workshop", "royal arena", "frozen peak", "jungle arena",
             "hog mountain", "electro valley", "spooky town", "rascal's hideout", "serenity peak", "legendary arena"}
        numberCards = [11, 17, 23, 30, 36, 42, 49, 55, 61, 68, 75, 82, 89, 96, 103, 106]
        finished = False
        afterer = None # used to start off where call left in previous iteration
        i = 0
        with open("6000-7000.txt", "a") as myfile:         ##########################################
            while(finished==False):

                    x = requests.get("https://api.clashroyale.com/v1/clans/?minMembers=20", headers={"Accept": "application/json",
                                                                                                     "authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImZiYTAyMWY3LTllNDEtNDI4NS04MWFkLWI0YmUxNjU0N2E1ZiIsImlhdCI6MTYzNTM0ODY5MSwic3ViIjoiZGV2ZWxvcGVyLzc0ZWQzYzdiLTkzNmYtZmEzZi1lNzBlLTk5ZDVjNTQ1MzlhNyIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyI5NS40NS4xNzUuODciXSwidHlwZSI6ImNsaWVudCJ9XX0.nK6ANzWgu0X7uA9wzfPD4cBZ2bKryqH91gZ3EH85LFw6y09VUU4HhC3yfWE8mhM8YLq3QP1m8tWMF1uvmphcag"},
                                     params={})

                    #afterer = x.json()["paging"]["cursors"]["after"] #get point to start off on next iteration
                    #print("after is ",afterer)
                    for clan in x.json()["items"]: #run through each clan
                         if clan["requiredTrophies"]>5000:
                             if(finished==True):
                                 break
                             #get clan tag
                             tag = clan["tag"]
                             # format tag for api call
                             tag2 = list(tag)
                             tag2.remove('#')
                             a = (''.join(tag2))
                             newTag = "%23" + a

                             #get members from clan using reformatted tag
                             y = requests.get("https://api.clashroyale.com/v1/clans/" + newTag + "/members",
                             headers={"Accept": "application/json",
                             "authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImZiYTAyMWY3LTllNDEtNDI4NS04MWFkLWI0YmUxNjU0N2E1ZiIsImlhdCI6MTYzNTM0ODY5MSwic3ViIjoiZGV2ZWxvcGVyLzc0ZWQzYzdiLTkzNmYtZmEzZi1lNzBlLTk5ZDVjNTQ1MzlhNyIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyI5NS40NS4xNzUuODciXSwidHlwZSI6ImNsaWVudCJ9XX0.nK6ANzWgu0X7uA9wzfPD4cBZ2bKryqH91gZ3EH85LFw6y09VUU4HhC3yfWE8mhM8YLq3QP1m8tWMF1uvmphcag"})

                             #run through players in clan
                             for player in y.json()["items"]:
                                 if i > (3000):  ###################
                                     finished = True
                                     print("finished now")
                                     break

                                 #reformat tag same as clan
                                 playerTag = player["tag"]
                                 playerTag2 = list(playerTag)
                                 playerTag2.remove('#')
                                 b = (''.join(playerTag2))
                                 newPlayerTag = "%23" + b

                                 #get player details
                                 z = requests.get("https://api.clashroyale.com/v1/players/" + newPlayerTag,
                                                  headers={"Accept": "application/json",
                                                           "authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImZiYTAyMWY3LTllNDEtNDI4NS04MWFkLWI0YmUxNjU0N2E1ZiIsImlhdCI6MTYzNTM0ODY5MSwic3ViIjoiZGV2ZWxvcGVyLzc0ZWQzYzdiLTkzNmYtZmEzZi1lNzBlLTk5ZDVjNTQ1MzlhNyIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyI5NS40NS4xNzUuODciXSwidHlwZSI6ImNsaWVudCJ9XX0.nK6ANzWgu0X7uA9wzfPD4cBZ2bKryqH91gZ3EH85LFw6y09VUU4HhC3yfWE8mhM8YLq3QP1m8tWMF1uvmphcag"})

                                 #check if in desired trophy range
                                 if z.json()["bestTrophies"]>=6000 and z.json()["bestTrophies"]<7000: #############################
                                     i += 1
                                     print("found one ", i)
                                     # calculate win ratio and round to 2 decimal places
                                     WinRatio = z.json()["wins"] / (z.json()["losses"] + z.json()["wins"])
                                     twoDec = str(round(WinRatio, 2))

                                     if (len(twoDec) == 3):
                                         twoDec = twoDec + "0"

                                     # write data to file
                                     myfile.write(z.json()["currentFavouriteCard"]["name"] + " " + str(
                                         z.json()["bestTrophies"]) + " " + twoDec + "\n")





        myfile.close()