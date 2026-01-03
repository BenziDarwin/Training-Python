from time import sleep

print("Hello World!")

arr = [1,2,3,4,5]
tup = (1,2,3,4,5)

dictionary = {"id":1, "name":"Benjamin", "description":"Scanners are down."}
 
 # FIFO
que = [{"id":1, "name":"Benjamin", "description":"Scanners are down."},
       {"id":2, "name":"Adrian", "description":"System of off."},
       {"id":3, "name":"Alvin", "description":"Support."}]


for i in range(len(que)):
    print(f"Working on item in queue: client: {que[i]['name']}")
    sleep(2)
    que[i]["status"] = "completed"
    print(que[i])
    que.pop()
