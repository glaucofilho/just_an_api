pre-commint install
pre-commit migrate-config
pre-commit run --all-files
uvicorn main:app --reload
