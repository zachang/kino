# kino
A simple movie list from Studio Ghibli


## Project Setup

- Clone the repo.
- Have at least Python 3.6.x installed. 3.8 was used.
- Open project with your favorite editor
- Create a .env file in your root directory as described in .env.example file; Optional if `DEBUG=True`
- creates virtual environment and activate.
- Run `make install`, to install pre-existing dependencies
- Run `make start` to start app
- For Test, Run `make test` or `make test_coverage`
- Do a `Makefile` file look-up if `make` commands don't work as specified or just run the allowed django commands.
- Since we cache our page using `redis` backend, install redis;
    - for MacOs `brew intall redis`
    - on your terminal, Run `redis-server`
    - do check how to install for other operating systems
- Webpage links sample; host server might differ
    - `http://localhost:8000/`
    - `http://localhost:8000/movies/`
    - `http://localhost:8000/{movie_id}`

## Technologies Used

- [Django](https://www.djangoproject.com/) - Python web framework used
- [Bootstrap](https://getbootstrap.com/)
