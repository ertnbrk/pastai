from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.user import User
from database import get_db

router = APIRouter()

@router.post('/user')
def create_user(email: str, name: str, db: Session = Depends(get_db)):
    # Check if user already exists
    existing_user = db.query(User).filter(User.email == email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail='User already exists')

    # Create a new user
    user = User(email=email, name=name)
    db.add(user)
    db.commit()
    db.refresh(user)

    return {'message': 'User created successfully', 'user_id': user.id}