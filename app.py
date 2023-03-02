from flask import Flask, render_template, jsonify

app = Flask(__name__)  # __name__ default is __main__

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': 'Rs, 10,00,000'
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Delhi, India',
    'salary': 'Rs, 15,00,000'
  },
  {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'Remote',
  },
  {
    'id': 3,
    'title': 'Backend Engineer',
    'location': 'San Fransicso, USA',
    'salary': '$ 120,000'
  },
]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name='Bear Fruit')


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


print(__name__)
if __name__ == "__main__":
  # print("I am inside the if now")
  app.run(host='0.0.0.0', debug=True)
