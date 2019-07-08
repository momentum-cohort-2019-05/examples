.PHONY: library-01 library-02 movies-01 movies-02 movies-03

library-01:
	psql library < library/01/books-schema.sql
	pgloader library/01/books.load

library-02: library-01
	cat library/02/create-*.sql | psql library
	psql -q library < library/02/patrons.sql

movies:
	dropdb movies
	createdb movies
	psql movies < movies.sql

movies-schema-only:
	dropdb movies
	createdb movies
	psql movies < movies-schema-only.sql
