.PHONY: install kernel train evaluate test run docker-build docker-run clean

install:
	uv sync

kernel:
	uv run python -m ipykernel install --user --name=project-ai-nlp --display-name "Python (project-ai-nlp)"

train:
	uv run python scripts/train_pipeline.py

evaluate:
	uv run python scripts/evaluate_pipeline.py

test:
	uv run pytest tests/ -v --tb=short

run:
	uv run streamlit run src/api/app.py

docker-build:
	docker build -f docker/Dockerfile -t hate-speech-classifier .

docker-run:
	docker-compose -f docker/docker-compose.yml up

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name ".ipynb_checkpoints" -delete
