from fastapi import APIRouter, Depends

from dependencies import get_dep, Dep

router = APIRouter()
@router.get("/stuff")
async def hello(depobj:Dep = Depends(get_dep)):
    return {"obj": str(depobj), "data":depobj.data }

@router.get("/stuff_update")
async def stuff_update(depobj:Dep = Depends(get_dep)):
   depobj.data.append(3)
   return {"obj": str(depobj), "data":depobj.data }