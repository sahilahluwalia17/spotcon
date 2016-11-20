from flask import Flask
app = Flask("j")

def increment(x):
  return x+1;

print(map(increment, [1,2,3]));


@app.route("/")
def hello():
    return app.send_static_file('index.html')

@app.route("/foo")
def yo():
    return "foobar"

if __name__ == "__main__":
    app.run()
