from db import session


class BaseService:
    session = session
    model = None

    def find_by_id(self, model_id: int, *select_columns):
        query = self.model.query
        if select_columns:
            columns = [getattr(self.model, col) for col in select_columns]
            query = query.with_entities(*columns)
        return query.filter_by(id=model_id).first()

    def create(self, flush=True, **data):
        object = self.model(**data)
        self.session.add(object)

        if flush:
            self.session.flush()

        return object

    def find_first(self, **data):
        return self.model.query.filter_by(**data).first()

    def find(self, sort_by_id=None, *select_columns, **data):
        query = self.model.query
        if select_columns:
            columns = [getattr(self.model, col) for col in select_columns]
            query = query.with_entities(*columns)

        if data:
            query = query.filter_by(**data)

        if sort_by_id and sort_by_id in ["asc", "desc"]:
            q = self.model.id.desc() if sort_by_id == "desc" else self.model.id.asc()
            query = query.order_by(q)

        return query.all()
