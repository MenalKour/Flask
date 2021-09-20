from flask import Flask,jsonify,request
app=Flask(__name__)
##creating an array of task with each task as a different object
tasks=[{
    'id':1,
    'contact':u'9472659630',
    'name':u'Menal',
    'done':False
},
{
    'id':2,
    'contact':u'97442856396',
    'name':u'Olaf',
    'done':False
}
]
@app.route('/add-data',methods=['POST'])
def add_task():
    if not request.json:
        return jsonify({
            'status':'Error',
            'message':'Please Provide The data'
        },
        400
        )
    task={
        'id':tasks[-1]['id']+1,
        'contact':request.json['contact'],
        'name':request.json.get('name',''),
        'done':False
    }
    tasks.append(task)
    return jsonify({
        'status':'SUCCESS',
        'message':'Task Added Successfully'
    })

@app.route('/get-data')
def get_task():
    return jsonify({
        'data':tasks
    })    

if(__name__=='__main__'):
    app.run(debug=True)