from flask import Flask

app = Flask(__name__) # __name__ default is __main__
@app.route("/")
def hello_world():
  return "Hello, world"

print(__name__)
if __name__ == "__main__":
  # print("I am inside the if now")
  app.run(host='0.0.0.0',debug=True)