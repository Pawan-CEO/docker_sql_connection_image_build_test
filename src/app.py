from utils.utils import WorkUtils

from flask import Flask, Response, request
api=WorkUtils()
app=Flask(__name__)


@app.route('/test',methods=['GET','POST'])
def test():
    try:
        response=api.test_process()
        print("code working")
        return response
    except Exception as e:
        print(e)

if __name__ == '__main__':
    app.run()
# host='0.0.0.0', port=5000