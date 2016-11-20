from flask import Flask
app = Flask("j")

def increment(x):
  return x+1;

print(map(increment, [1,2,3]));


@app.route("/")
def hello():
    return "Hello World!"

@app.route("/foo")
def yo():
    return "foobar"

if __name__ == "__main__":
    app.run()
