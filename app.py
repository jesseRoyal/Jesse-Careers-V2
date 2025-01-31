from flask import Flask, jsonify, render_template

app = Flask(__name__)
JOBS =[{
    'id':1,
    'title':'Data Analyst',
    'location':'Kingston, Jamaica',
    'salary':'USD. $150,000'
},{
    'id':2,
    'title':'Data Scientist',
    'location':'London, UK',
    'salary':'USD. $200,000'
},{
    'id':3,
    'title':'Frontend Engineer',
    'location':'Remote'
},{
    'id':4,
    'title':'Backend Engineer',
    'location':'San Francisco, USA',
    'salary':'USD. $200,000'
}]


@app.route("/")
def hello_world():
    return render_template('home.html', jobs=JOBS, company_name='Jesse')

@app.route("/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
  app.run('0.0.0.0',debug=True)
  
  