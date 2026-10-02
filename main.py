from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


l={
    '1':'Apple',
    '2':'Banana',
    '3':'Cherry',
    '4':'Date'
}

@app.get("/getList")
def read_root():
    return l

# @app.get("/SirikiAnna")
# def read_root():
#     return {"Hello": "siriki anna namaste"}

@app.post("/postList/")
async def read_root(request: Request):
    item=await request.json()
    print(item)
    id=str(len(l)+1)
    l[id]=item['item']
    return l
    
    
    
    
    
    
    # body= await request.body()
    # print("Method:", request.method)
    # print("URL:", request.url)
    # print("Headers:", dict(request.headers))
    # print("Body:", body.decode("utf-8"))
    # return {"Hello":"siriki anna namaste"}




# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: str | None = None):
#     return {"item_id": item_id, "q": q}