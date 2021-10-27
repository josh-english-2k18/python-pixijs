# python-pixijs
An experiment to see if Python code can work with PixiJS in the browser via a transpiler.

Setup:
```
$ pip3 install transcrypt
$ npm install http-server
$ http-server . --port 8080 -a 0.0.0.0 --ext html --no-dotfiles -c-1
```

Compile (transpile) Python into Javascript:
```
$ python3 -m transcrypt -b -m -n python-experiment.py
```

After starting the `http-server` instance, simply navigate to: http://0.0.0.0:8080/index.html

### Note that this project utilizes the following:
- Transcrypt (TM) Python to JavaScript Small Sane Subset Transpiler Version 3.9.0
- Found here: https://www.transcrypt.org
