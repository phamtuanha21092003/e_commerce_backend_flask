from contextlib import contextmanager
from db import session


@contextmanager
def session_scope(scope=session, auto_commit=True, auto_close=True):
    session = scope
    try:
        yield session
        if auto_commit:
            session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        if auto_close:
            session.close()
