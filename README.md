# FastAPI template

### Description of this template

- FastAPI(https://fastapi.tiangolo.com/)
- Implement simple endpoints and test
- OpenAPI3.0 - auto generated
- setup.sh for setting vitual env
  run the script with `source setup.sh`
- logging configuration
- Simple unit test
- Apply formatter(black) and linter(flake8) with pre-commit

### How to use this template for a new project

1. Change project name and remove .git
2. `source setup.sh`
3. `git init`
4. `git checkout [your branch]`
5. Change app/routers/router.py to your business endpoint such as user.py
6. Change test/test_query.py to your test_case.py
7. Implement your code
8. Create pre-commit hook by running `pre-commit install`
9. `pytest test `
10. `pre-commit run --all-files`
11. `git add .`
12. `git commit -m "init commit"`
13. `git push origin [your branch]`

Now you have your project repository.
