from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

class evennumber(BaseModel):
    num:int


    
def even(num):
    if num % 2 == 0:
       return "it is an even number"
    else:
        return "it is not an even number"

# number=int(input("enter a number:"))
# result=even(number)
# print(result)
@app.post("/check")
async def final(data:evennumber):
    result=even(data.num)
    return result


@app.post("/welcome")
async def Hello():
    return {'message':"welcome the world of emotions"}