from model.BaseModel import BaseModel
from model.DimAge import DIM_AGE
from model.DimGender import DIM_GENDER
from model.DimDepression import DIM_DEPRESSION
from model.DimSuicidalThoughts import DIM_SUICIDAL_THOUGHTS
from model.DimDietaryHabits import DIM_DIETARY_HABITS
from model.DimFamilyMentalIllnessHistory import DIM_FAMILY_MENTAL_ILLNESS_HISTORY
from model.DimFinancialStress import DIM_FINANCIAL_STRESS
from model.DimSleepDuration import DIM_SLEEP_DURATION
from model.DimWorkHours import DIM_WORK_HOURS
from model.DimWorkPressure import DIM_WORK_PRESSURE
from model.DimWorkSatisfaction import DIM_WORK_SATISFACTION
from model.FormSouce import FROM_SOURCE
from connection import Connection
from tenacity import retry, stop_after_attempt, wait_exponential
from sqlalchemy.exc import OperationalError


class FACT_DEPRESSION(BaseModel):
    __table_name__ = "fact_depression"
    def __init__(self):
        super().__init__(self.__table_name__)
    @classmethod
    @retry(
        stop=stop_after_attempt(5),  # ✅ Retry up to 5 times
        wait=wait_exponential(multiplier=1, min=2, max=10),  # ✅ Exponential backoff (2s, 4s, 8s...)
        retry=(lambda e: isinstance(e, OperationalError))  # ✅ Retry only on DB errors
    )
    def add_record(cls, data: dict):
        session = Connection.get_session()  # ✅ Create session
    
        try:
            # ✅ Mapping of column names to their corresponding dimension models
            dimension_mapping = {
                "age": DIM_AGE,
                "gender": DIM_GENDER,
                "work_pressure": DIM_WORK_PRESSURE,
                "work_satisfaction": DIM_WORK_SATISFACTION,
                "sleep_duration": DIM_SLEEP_DURATION,
                "dietary_habits": DIM_DIETARY_HABITS,
                "suicidal_thoughts": DIM_SUICIDAL_THOUGHTS,
                "work_hours": DIM_WORK_HOURS,
                "financial_stress": DIM_FINANCIAL_STRESS,
                "family_mental_illness_history": DIM_FAMILY_MENTAL_ILLNESS_HISTORY,
                "depression": DIM_DEPRESSION,
                "from_source": FROM_SOURCE
            }

            record_ids = {}
            for key, model in dimension_mapping.items():
                if key in data:
                    record = model.get_or_create(**{key: data[key]}).to_dict()
                    if record:
                        record_ids[f"{key}_id"] = record['id']

            fact_record = cls.get_model()(**record_ids)
            session.add(fact_record)
            session.commit()  # ✅ Commit transaction
        
        except Exception as e:
            session.rollback()  # ✅ Rollback in case of error
            print(f"Error adding record: {e}")

        finally:
            session.close()  # ✅ Always close session


