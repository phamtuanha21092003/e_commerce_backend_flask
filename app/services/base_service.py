from db import session


class BaseService:
    session = session
    model = None

    def find_all_by_id(self, model_id: int):
        return self.model.get(model_id)

    def create(self, flush=True, **data):
        object = self.model(**data)
        self.session.add(object)

        if flush:
            self.session.flush()

        return object

    def find_first(self, **data):
        return self.model.query.filter_by(**data).first()
