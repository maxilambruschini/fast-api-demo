from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from config.database import get_db

from .models import Case
from .schemas import Case as CaseSchema
from .schemas import CaseCreate, CaseWithUser

router = APIRouter()


@router.get("/", response_model=list[CaseSchema])
def get_cases(db: Session = Depends(get_db)):
    return db.execute(select(Case)).scalars().all()


@router.post("/", response_model=CaseCreate)
def create_case(case: CaseCreate, db: Session = Depends(get_db)):
    from services.users.models import User

    db_user = db.get(User, case.user_id)
    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {case.user_id} not found",
        )

    db_case = Case(**case.model_dump())
    db.add(db_case)
    db.commit()
    db.refresh(db_case)
    return db_case


@router.get("/{case_id}", response_model=CaseSchema)
def get_case(case_id: int, db: Session = Depends(get_db)):
    db_case = db.get(Case, case_id)
    if db_case is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Case with id {case_id} not found",
        )
    return db.get(Case, case_id)


@router.delete("/{case_id}")
def delete_case(case_id: int, db: Session = Depends(get_db)):
    db_case = db.get(Case, case_id)
    if db_case is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Case with id {case_id} not found",
        )
    db.delete(db_case)
    db.commit()
    return {"message": f"Case with id {case_id} deleted successfully"}


@router.get("/{case_id}/user", response_model=CaseWithUser)
def get_case_with_user(case_id: int, db: Session = Depends(get_db)):
    db_case = db.get(Case, case_id)
    if db_case is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Case with id {case_id} not found",
        )
    return db_case
