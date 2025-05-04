from connection import Connection
from sqlalchemy import func,text
import pandas as pd

def fetchAll():
    session = Connection.get_session()
    result = session.execute(text("SELECT * FROM fetch_all()"))
    df = pd.DataFrame(result.fetchall(), columns=result.keys())
    return df

