from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.journal import Journal
from database import get_db
from events.producers.journal_producer import publish_journal_recorded

router = APIRouter()

@router.post('/journal')
def record_journal(user_id: int, journal_text: str, db: Session = Depends(get_db)):
    # Create a new journal entry
    journal = Journal(user_id=user_id, text=journal_text)
    db.add(journal)
    db.commit()
    db.refresh(journal)

    # Publish the event
    publish_journal_recorded(user_id, journal_text)

    return {'message': 'Journal recorded successfully', 'journal_id': journal.id}