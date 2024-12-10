build:
	docker build -t ollama .

run:
	mkdir -p ${PWD}/models
	docker run --rm --name ollama -p 11434:11434 -v ${PWD}/models/.ollama:/root/.ollama ollama

translate:
	docker cp translate.py ollama:/usr/src/app
	docker cp to_do.txt  ollama:/usr/src/app/to_do
	docker exec -ti ollama python3 translate.py to_do

