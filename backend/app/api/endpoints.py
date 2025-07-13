from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from sqlalchemy.orm import Session
from database import get_db
from models.models import User, Journal, Context, Reminder
from events.producers.journal_producer import publish_journal_recorded

router = APIRouter()

# --- Pydantic Schemas ---
class UserCreate(BaseModel):
    email: str
    name: str

class UserRead(UserCreate):
    id: int
    created_at: Optional[datetime]
    class Config:
        orm_mode = True

class JournalCreate(BaseModel):
    user_id: int
    text: str

class JournalRead(JournalCreate):
    id: int
    date: Optional[datetime]
    class Config:
        orm_mode = True

class ContextCreate(BaseModel):
    user_id: int
    data: dict

class ContextRead(ContextCreate):
    id: int
    updated_at: Optional[datetime]
    class Config:
        orm_mode = True

class ReminderCreate(BaseModel):
    user_id: int
    text: str
    datetime: datetime

class ReminderRead(ReminderCreate):
    id: int
    class Config:
        orm_mode = True


@router.get("/health")
def health():
    return {"status": "ok"}

# --- User CRUD ---
@router.post('/api/v1/users', response_model=UserRead)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(email=user.email, name=user.name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.get('/api/v1/users', response_model=List[UserRead])
def list_users(db: Session = Depends(get_db)):
    return db.query(User).all()

@router.get('/api/v1/users/{user_id}', response_model=UserRead)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail='User not found')
    return user

@router.put('/api/v1/users/{user_id}', response_model=UserRead)
def update_user(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail='User not found')
    db_user.email = user.email
    db_user.name = user.name
    db.commit()
    db.refresh(db_user)
    return db_user

@router.delete('/api/v1/users/{user_id}')
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail='User not found')
    db.delete(db_user)
    db.commit()
    return {"message": "User deleted"}

# --- Journal CRUD ---
@router.post('/api/v1/journals', response_model=JournalRead)
def create_journal(journal: JournalCreate, db: Session = Depends(get_db)):
    db_journal = Journal(user_id=journal.user_id, text=journal.text)
    db.add(db_journal)
    db.commit()
    db.refresh(db_journal)
    # Event gönder
    publish_journal_recorded(journal.user_id, journal.text)
    return db_journal

@router.get('/api/v1/journals', response_model=List[JournalRead])
def list_journals(db: Session = Depends(get_db)):
    return db.query(Journal).all()

@router.get('/api/v1/journals/{journal_id}', response_model=JournalRead)
def get_journal(journal_id: int, db: Session = Depends(get_db)):
    journal = db.query(Journal).filter(Journal.id == journal_id).first()
    if not journal:
        raise HTTPException(status_code=404, detail='Journal not found')
    return journal

@router.put('/api/v1/journals/{journal_id}', response_model=JournalRead)
def update_journal(journal_id: int, journal: JournalCreate, db: Session = Depends(get_db)):
    db_journal = db.query(Journal).filter(Journal.id == journal_id).first()
    if not db_journal:
        raise HTTPException(status_code=404, detail='Journal not found')
    db_journal.user_id = journal.user_id
    db_journal.text = journal.text
    db.commit()
    db.refresh(db_journal)
    return db_journal

@router.delete('/api/v1/journals/{journal_id}')
def delete_journal(journal_id: int, db: Session = Depends(get_db)):
    db_journal = db.query(Journal).filter(Journal.id == journal_id).first()
    if not db_journal:
        raise HTTPException(status_code=404, detail='Journal not found')
    db.delete(db_journal)
    db.commit()
    return {"message": "Journal deleted"}

# --- Context CRUD ---
@router.post('/api/v1/contexts', response_model=ContextRead)
def create_context(context: ContextCreate, db: Session = Depends(get_db)):
    db_context = Context(user_id=context.user_id, data=context.data)
    db.add(db_context)
    db.commit()
    db.refresh(db_context)
    return db_context

@router.get('/api/v1/contexts', response_model=List[ContextRead])
def list_contexts(db: Session = Depends(get_db)):
    return db.query(Context).all()

@router.get('/api/v1/contexts/{context_id}', response_model=ContextRead)
def get_context(context_id: int, db: Session = Depends(get_db)):
    context = db.query(Context).filter(Context.id == context_id).first()
    if not context:
        raise HTTPException(status_code=404, detail='Context not found')
    return context

@router.put('/api/v1/contexts/{context_id}', response_model=ContextRead)
def update_context(context_id: int, context: ContextCreate, db: Session = Depends(get_db)):
    db_context = db.query(Context).filter(Context.id == context_id).first()
    if not db_context:
        raise HTTPException(status_code=404, detail='Context not found')
    db_context.user_id = context.user_id
    db_context.data = context.data
    db.commit()
    db.refresh(db_context)
    return db_context

@router.delete('/api/v1/contexts/{context_id}')
def delete_context(context_id: int, db: Session = Depends(get_db)):
    db_context = db.query(Context).filter(Context.id == context_id).first()
    if not db_context:
        raise HTTPException(status_code=404, detail='Context not found')
    db.delete(db_context)
    db.commit()
    return {"message": "Context deleted"}

# --- Reminder CRUD ---
@router.post('/api/v1/reminders', response_model=ReminderRead)
def create_reminder(reminder: ReminderCreate, db: Session = Depends(get_db)):
    db_reminder = Reminder(user_id=reminder.user_id, text=reminder.text, datetime=reminder.datetime)
    db.add(db_reminder)
    db.commit()
    db.refresh(db_reminder)
    return db_reminder

@router.get('/api/v1/reminders', response_model=List[ReminderRead])
def list_reminders(db: Session = Depends(get_db)):
    return db.query(Reminder).all()

@router.get('/api/v1/reminders/{reminder_id}', response_model=ReminderRead)
def get_reminder(reminder_id: int, db: Session = Depends(get_db)):
    reminder = db.query(Reminder).filter(Reminder.id == reminder_id).first()
    if not reminder:
        raise HTTPException(status_code=404, detail='Reminder not found')
    return reminder

@router.put('/api/v1/reminders/{reminder_id}', response_model=ReminderRead)
def update_reminder(reminder_id: int, reminder: ReminderCreate, db: Session = Depends(get_db)):
    db_reminder = db.query(Reminder).filter(Reminder.id == reminder_id).first()
    if not db_reminder:
        raise HTTPException(status_code=404, detail='Reminder not found')
    db_reminder.user_id = reminder.user_id
    db_reminder.text = reminder.text
    db_reminder.datetime = reminder.datetime
    db.commit()
    db.refresh(db_reminder)
    return db_reminder

@router.delete('/api/v1/reminders/{reminder_id}')
def delete_reminder(reminder_id: int, db: Session = Depends(get_db)):
    db_reminder = db.query(Reminder).filter(Reminder.id == reminder_id).first()
    if not db_reminder:
        raise HTTPException(status_code=404, detail='Reminder not found')
    db.delete(db_reminder)
    db.commit()
    return {"message": "Reminder deleted"}