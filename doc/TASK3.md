### Thinking out loud

- I will use Python for this task and will name it `circadian`
- Without frameworks as they seem unnecessary - by definition it's a script, not an API, let's stick to KISS
- If I use `?formatted=0`, we get UTC timezones, and probably can ignore DST transition
- I will need several dependencies
  - `requests` library for making requests and parsing json response
  - `pytest` and `coverage` for convenient unit testing
  - `flake8` or `pylint` for codestyle linting
  - some validation like `pydantic` or `jsonschema`

### Development

TDD (test driven development) seems like a good idea here, I start with unit test. In python there's no convenient way of creating dataProviders as in junit or phpunit, but pytest parametrization works in the same fashion. So, I start with a simple unit test for essential decision making.

![img.png](img.png)

At first I thought I need two requests in order to cover the case of request overnight. But then I found out that whenever scipt is run, it always responds with "today's" data. Hence it can be limited in one request.

Usage of Coordinated Universal Time, allows to get rid of timezones' issues, unless we need to handle specific cases like human-readable date and time output, extended logging, and so on.

Usually we don't store `.env` files in VCS, as they might contain secrets and sensitive data. Now this is not the case and in order to keep installation and usage simplier, I'm keeping `.env` in git.

### Possible vectors of improvement

- Make it a console application with at least arguments' support (`-v`, `-e`, etc)
- Make it a standalone project, get rid of relative imports, add CI/CD for lints, tests and maybe build
- Handle edge cases like:
  - Broken data (validation is performed but it's not defined what behavior is expected)
  - Service unreachable (5xx, 4xx errors for example)
- Reduce or remove dependency on external service:
  - It can be standalone with libraries `astral` and `suntime`, it will help to mitigate:
    - Speed degradation due to network or 3rd party issues
    - Undefined behavior if service is unreacheable
    - Potential 429 (request limit)
- Write code that is agnostic to `now()`
- Make it compilable with `pyinstaller` - easier to pack and distribute
