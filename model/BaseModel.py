from connection import Connection

class BaseModel:
    base = Connection.get_base()

    def __init__(self, table_name):
        self._model = getattr(self.base.classes, table_name)  # ✅ Store model reference

    @classmethod
    def get_model(cls):
        """Return the automapped SQLAlchemy model for the table."""
        return getattr(cls.base.classes, cls.__table_name__)  # Uses table name defined in subclass


    @classmethod
    def get_all(cls):
        """Get all records from the table using a class method."""
        session = Connection.get_session()
        records = session.query(cls.get_model()).all()

        return QueryResultWrapper(records, cls)
    

    @classmethod
    def get_filter(cls, **kwargs):
        """Filter records based on conditions."""
        session = Connection.get_session()
        records = session.query(cls.get_model()).filter_by(**kwargs).all()
    
        return QueryResultWrapper(records, cls)

    @classmethod
    def get_or_create(cls, defaults=None, **kwargs):
        """Get one record if it exists, else create a new one."""
        session = Connection.get_session()
        instance = session.query(cls.get_model()).filter_by(**kwargs).first()
        if instance:
            session.close()
            return QueryResultWrapper(instance, cls)  # Found existing record
        
        params = {**kwargs, **(defaults or {})}
        instance = cls.get_model()(**params)
        session.add(instance)
        session.commit()
        instance = session.query(cls.get_model()).filter_by(**kwargs).first()
        session.close()
        return QueryResultWrapper(instance, cls)  # Created new record

    @classmethod
    def to_dict(cls, obj):
        """Convert a SQLAlchemy object to a dictionary."""
        return {column.name: getattr(obj, column.name) for column in cls.get_model().__table__.columns}
    
    
class QueryResultWrapper:
    """A wrapper around a list of results that adds a .to_dict() method."""
    def __init__(self, records, model_cls):
        self.records = records
        self.model_cls = model_cls

    def __iter__(self):
        return iter(self.records)

    def __getitem__(self, index):
        return self.records[index]

    def __len__(self):
        if (type(self.records) is list):
            return len(self.records)
        return self.records

    def to_dict(self):
        if (type(self.records) is list):
            return [self.model_cls.to_dict(record) for record in self.records]
        return self.model_cls.to_dict(self.records)