image = flask-demo:latest

PHONY: build
build: ##@development build docker image
	docker build -t $(image) .

PHONY: run
run: ##@development run the tests
	docker run -p 5000:5000 $(image)
