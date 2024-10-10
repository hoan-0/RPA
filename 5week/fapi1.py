from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/") # HTTP GET 요청을 처리할 경로("/")를 설정. 즉, 루트 경로로 접근 시 이 함수가 실행됨
def read_root(): # 루트 경로로 GET 요청이 들어왔을 때 실행될 함수 정의
    return {"Hello": "World"} # 요청이 성공적으로 처리되면 {"Hello": "World"}라는 JSON 형식의 응답을 반환

@app.get("/item")
def read_item(item_id: int, name: str = None, age: int = 0):
     return JSONResponse(content={"item_id": item_id, "name": name, "age": age}, media_type="application/json; charset=utf-8")
    #return {"item_id": item_id, "name": name, "age": age}
