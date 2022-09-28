from turtle import title
from urllib.request import Request
from fastapi import APIRouter, HTTPException, Path, Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import BookSchema, RequestBook, Response
import crud

router = APIRouter()

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@router.post('/create')
async def create(request:RequestBook, db:Session=Depends(get_db)):
    crud.create_book(db,request.parameter)
    return Response(code=200,status="OK",message="Book created successfully").dict(exclude_none=True)


@router.get('/')
async def get(db:Session=Depends(get_db)):
    _book = crud.get_book(db,0,100)
    return Response(code=200, status="OK", message="All data fetch", result=_book).dict(exclude_none=True)


@router.get("/{id}")
async def get_by_id(id: int, db:Session=Depends(get_db)):
    _book = crud.get_book_by_id(db, id)
    return Response(code=200, status="OK", message="Success get data", result=_book).dict(exclude_none=True)


@router.post("/update")
async def update_book(request: RequestBook, db: Session=Depends(get_db)):
    _book = crud.update_book(db, 
                             book_id=request.parameter.id,
                             title=request.parameter.title,
                             description=request.parameter.description
    )
    return Response(code=200, status="OK", message="update data", result=_book)



@router.delete("/delete")
async def delete_book(id:int, db: Session=Depends(get_db)):
    _book = crud.remove_book(db, book_id=id)
    return Response(code=200, status="OK", message="Item sucessefully delete").dict(exclude_none=True)