# How To Run

---

### Dockerized version

```bash
# Build docker image
$ docker build -t circadian .

# Run in normal mode
$ docker run --rm circadian

# Run tests with coverage
$ docker run --rm --entrypoint sh circadian -c "cd /app && coverage run -m pytest && coverage report -m"

# Image cleanup
$ docker rmi circadian

# Optional build artifacts cleanup
$ docker system prune
```

Optionally you can pass latitude/longtitude as environmental variables. And example of e2e test against default values and my coordinates in Kaunas :)
```bash
$ docker run --rm circadian                                                                                                                                                                                                                                                             
OFF                                                                                                                                                                                                                                                                                                                         

$ docker run --rm -e LAT='54.8985' -e LNG='23.9036' circadian
ON

$ date
Sat Feb 24 07:08:31 PM EET 2024
```

---

### Virtual environment

```bash
# Prepare and activate virtual environment
$ python3 -m venv .venv
$ source .venv/bin/activate

# Install dependencies
(.venv)$ pip install -r requirements.txt

# Check against flake8
(.venv)$ make lint

# Tests with coverage
(.venv)$ make test

# Regular execution
(.venv)$ python3 main.py
```
