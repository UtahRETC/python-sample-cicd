# Sample CI/CD Python project

This is an example Flask application with automated tests, linters, and
deployments.

## Useful commands

- `./scripts/install`, install dependencies
- `./scripts/lint`, run code formatters and linters
- `./scripts/test`, run automated tests
- `./scripts/run`, start the web server.

## Configuration

The following configuration values are managed with environment variables. For
example, run `PORT=9001 DEBUG=1 ./scripts/run` to run the application in debug
mode and listen to requests on port 9001.

- `DEBUG`, toggle debug mode
- `HOST`, the host to listen on
- `PORT`, the port to listen on
