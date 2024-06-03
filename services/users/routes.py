from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from config.database import get_db
from services.cases.schemas import UserWithCases

from .models import User
from .schemas import User as UserSchema
from .schemas import UserCreate

router = APIRouter()


@router.get("/", response_model=list[UserSchema])
def get_users(db: Session = Depends(get_db)):
    return db.execute(select(User)).scalars().all()


@router.post("/", response_model=UserSchema)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@router.get("/{user_id}", response_model=UserSchema)
def get_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.get(User, user_id)
    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {user_id} not found",
        )
    return db.get(User, user_id)


@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.get(User, user_id)
    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {user_id} not found",
        )
    db.delete(db_user)
    db.commit()
    return {"message": f"User with id {user_id} deleted successfully"}


@router.get("/{user_id}/cases/", response_model=UserWithCases)
def get_user_with_cases(user_id: int, db: Session = Depends(get_db)):
    db_user = db.get(User, user_id)
    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {user_id} not found",
        )
    return db_user
