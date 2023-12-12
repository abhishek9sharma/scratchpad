from fastapi import FastAPI, Depends
from simple import router
from dependencies import get_dep, Dep


app = FastAPI()
app.include_router(router, prefix="/stuff",tags=['stuff'])


class Hello(str):
    @app.get("/hello")
    def hello(self, depobj:Dep = Depends(get_dep)):
        return {"obj": str(depobj), "data":depobj.data }
    
    @app.get("/update")
    def update(self, depobj:Dep = Depends(get_dep)):
        depobj.data.append(2)
        return {"obj": str(depobj), "data":depobj.data }