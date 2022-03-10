
from flask import request
from flask_restx import Resource, Namespace
from hw.dao.model.movie import MovieSchema, Movie
from implemented import movie_service

movie_ns = Namespace('movies')


@movie_ns.route("/")
class MoviesView(Resource):
    def get(self):
        res = MovieSchema(many=True)
        director_id = request.args.get('director_id')
        genre_id = request.args.get('genre_id')
        year = request.args.get('year')
        if director_id and genre_id and year:
            movies = Movie.query.filter_by(director_id=director_id, genre_id=genre_id).all()
        elif director_id:
            movies = Movie.query.filter_by(director_id=director_id).all()
        elif genre_id:
            movies = Movie.query.filter_by(genre_id=genre_id).all()
        elif year:
            movies = Movie.query.filter_by(year=year).all()
        else:
            movies = Movie.query.all()
        if movies:
            return res.dump(movies), 208
        else:
            return 404


    def post(self):
        req_json = request.json
        movie = movie_service.create(req_json)
        return "", 201, {"location": f"/movies/{movie.id}"}


@movie_ns.route("/<int:bid>")
class MovieView(Resource):
    def get(self, bid):
        b = movie_service.get_one(bid)
        sm_d = MovieSchema().dump(b)
        return sm_d, 200

    def put(self, bid):
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = bid
        movie_service.update(req_json)
        return "", 204

    def delete(self, bid):
        movie_service.delta(bid)
        return "", 204
