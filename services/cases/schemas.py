from typing import List, Optional

from pydantic import BaseModel

from services.users.schemas import User


class CaseBase(BaseModel):
    name: str


class CaseCreate(CaseBase):
    user_id: int
    pass


class Case(CaseBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True


class CaseUserRetrieve(CaseBase):
    id: int


class CaseWithUser(Case):
    creator: User


class UserWithCases(User):
    cases: Optional[List[CaseUserRetrieve]] = []
