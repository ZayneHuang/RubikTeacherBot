from flask import Flask
from flask import render_template
from flask import request, jsonify
from flask import url_for
import json
import types
app=Flask(__name__)
from CFOPsolver import CubeSolver
import ast

with open('interface/initState.json', 'r') as f:
    result = json.load(f)

@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'GET':
        return render_template('mofang.html')

@app.route('/initState', methods=['POST'])
def initState():
    if request.method=='POST':
        #rev=request.get_json()['city']
        #result=selcity(rev)
        #result['state']=
        print("initstate")
        print(result)
        return jsonify(result)

@app.route('/2', methods=['POST','GET'])
def index2():
    if request.method == 'GET':
        # rev = {"state":[47,12,20,19,4,52,11,5,44,24,34,26,37,13,30,35,7,0,8,3,33,1,22,41,17,16,15,29,10,45,39,31,23,9,50,18,38,46,42,43,40,48,27,25,6,53,28,2,32,49,21,36,14,51]}

        state = request.args.get('state')
        rev = {"state": eval(state)}

        #rev=request.form['state']
        return render_template('mofang2.html',revi = str(rev))
    # if request.method == 'POST':
    #     data = json.loads(request.get_data(as_text=True))
    #     rev = {"state": data["state"]}
    #     cnt = cnt+1
    #     states[cnt] = rev
    #     # return render_template('mofang2.html', revi = str(rev))
    #     return json.dumps({'data': rev, 'id': cnt}), 200, {'ContentType':'application/json'}

@app.route('/recog',methods=['GET'])
def recog():
    if request.method == 'GET':
        return render_template('recog_cube.html')



@app.route('/solve', methods=['POST'])
def solve():
    if request.method == 'POST':
        rev = request.form
        print(rev)
        print("computing...")
        data = rev.to_dict()
        print("data:", data)
        state = []
        data['state'] = ast.literal_eval(data['state'])
        for i in data['state']:
            state.append(int(i))
        #solver=CubeSolver('../formula/F2L.txt','../formula/OLL.txt','../formula/PLL.txt')
        print("input state:",state)
        result = CubeSolver.getResults(state)
        print("complete!")
        print("result form:", result)
        return jsonify(result)

if __name__=='__main__':
    app.run(debug=True, port=5050)