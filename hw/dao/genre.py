from hw.dao.model.genre import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, bid):
        return self.session.query(Genre).get(bid)

    def get_all(self):
        return self.session.query(Genre).all()

    def get_by_genre_id(self, vol):
        return self.session.query(Genre).filter(Genre.genre_id == vol).all()

    def create(self, genre_d):
        ent = Genre(**genre_d)
        self.session.add(ent)
        self.session.commit()
        return ent
