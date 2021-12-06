import requests

def run():
    x = requests.get("https://api.clashroyale.com/v1/cards", headers={"Accept": "application/json",
                                                                                     "authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImZiYTAyMWY3LTllNDEtNDI4NS04MWFkLWI0YmUxNjU0N2E1ZiIsImlhdCI6MTYzNTM0ODY5MSwic3ViIjoiZGV2ZWxvcGVyLzc0ZWQzYzdiLTkzNmYtZmEzZi1lNzBlLTk5ZDVjNTQ1MzlhNyIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyI5NS40NS4xNzUuODciXSwidHlwZSI6ImNsaWVudCJ9XX0.nK6ANzWgu0X7uA9wzfPD4cBZ2bKryqH91gZ3EH85LFw6y09VUU4HhC3yfWE8mhM8YLq3QP1m8tWMF1uvmphcag"}
                     )
    names=[]
    id=[]
    actualid = []
    listcounter=1
    for i in x.json()["items"]:
        id.append(i["id"])
        names.append(i["name"])
        actualid.append(listcounter)
        listcounter+=1


    lines=[]
    file = open("5000-6000.txt")
    for line in file:
        lines.append(line)
    file.close
    count=0

    with open("5000-6000Converted.txt", "a") as myfile:
        for x in lines:
            x=1
            splitter = lines[count].split(" ")
            if len(splitter)==4:
                temp = splitter[0] + " " + splitter[1]
                x+=1
            else:
                temp = splitter[0]

            index = names.index(temp)
            newID = actualid[index]
            myfile.write(str(newID) + " " + splitter[x] + " " + splitter[x+1])
            count+=1
    
    myfile.close()

run()