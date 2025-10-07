# Highlights

This is an API serving highlighted quotes from books I've read. Too often, important excerpts from books are highlighted and then hidden a book on my bookshelf, only to be forgotten or never read again. This API serves as a means for me to quickly refresh my memory of those highlights.

## Data

The data backing this API is maintained within the project's [src/data](src/data) directory. The models are simple enough and the overhead of running a database is unnecessary, presently.

## Getting started

Run the following command to setup the project. This command installs [uv](https://docs.astral.sh/uv/) and the required Python version.

```sh
make setup
```

Run the following command to run the API server on port 3000.

```sh
make dev
```

Alternatively, the server can be ran in a Docker container on port 3000 by running the following command.

```sh
make drun
```

To stop (and remove) the running container, run the following command.

```sh
make dstop
```

Running `make` (or `make help`) will also output a list of all available `make` targets that can be ran.

## Running tests

To run tests on the project, run the following command.

```sh
make test
```
