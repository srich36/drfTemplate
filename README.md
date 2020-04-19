# Usage

To use this template first fork the repository and copy `config.ini.example` to `config.ini`. Set database name and password in `docker-compose.yml` and update `config.ini` with those set values. Run `docker-compose up --build` to build and run, and `docker-compose up` to just run. Running `docker-compose down -v` will drop the database volume for restarting and can be useful if you have database configuration errors when setting up.
