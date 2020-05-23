from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
import argparse
import os
import urllib


app = Flask(__name__)
CORS(app)

@app.route('/project', methods=['GET','POST'])
def index():
    if request.method == 'GET':
        result = []
        title_list = ["칸반보드 프로젝트", "딥러닝 프로젝트", "JS react 프로젝트"]
        user_id_list = ["minho0312", "jbk4860", "msg0116"]
        description_list = ["파이썬 django, JS react를 이용한 칸반보드 만들기 프로젝트입니다. 파이썬 개발 모임에서 공부한 내용을 직접 활용을 하여 개발을 해보자는 취지에서 시작한 프로젝트입니다. 추후 더 재미있는 프로젝트를 할 수 있었으면 좋겠습니다.",
                            "컴퓨팅의 발달로 인해 기존 추천 시스템 대비 딥러닝 기반의 추천 알고리즘이 높은 성능을 보이고 있습니다. 이에 따라 본 프로젝트에서는 다중 인공신경망을 이용한 추천 시스템 개발을 목표로합니다. 이를 통해 기존 시스템 대비 더 높은 품질의 추천시스템을 만들어서 더 많은 유저들을 유치할 수 있을 것으로 기대됩니다.",
                            "자바스크립트 라이브러리인 react를 이용한 프로젝트입니다. 본 프로젝트는 front-end: react, back-end: django를 활용한 프로젝트입니다. 이를 통해서 개발과정에서 front-end, back-end 사이의 이해관계를 보다 자세히 이해할 수 있을 것으로 기대됩니다."]
        for idx,(title, user_id, description) in enumerate(zip(title_list, user_id_list, description_list)):
            dic = {}
            dic["id"] = str(idx+1)
            dic["title"] = title
            dic["user_id"] = user_id
            dic["description"] = description
            result.append(dic)
        return jsonify(result)
    elif request.method == 'POST':
        ## Requset data from Front-end
        data = request.get_json(force=True)
        print(data)
        return "just for test"



@app.route('/task/1', methods=['GET'])
def index_task_1():
    result = []
    title_list = ["컴포넌트 구성하기", "rest-api로 랜더링하기", "back-end 서버 구축하기"]
    user_id_list = ["minho0312", "jbk4860", "jbk4860"]
    description_list = ["react로 컴포넌트를 구성합니다",
                        "axios를 통해 api 호출을 합니다",
                        "django를 이용하여 서버를 구축합니다"]
    for idx,(title, user_id, description) in enumerate(zip(title_list, user_id_list, description_list)):
        dic = {}
        dic["id"] = str(idx)
        dic["title"] = title
        dic["user_id"] = user_id
        dic["description"] = description
        result.append(dic)
    return jsonify(result)

@app.route('/task/2', methods=['GET'])
def index_task_2():
    result = []
    title_list = ["데이터 구축하기", "머신러닝 공부하기", "GPU로 학습하기"]
    user_id_list = ["minho0312", "konlpy123", "tensorRT4U"]
    description_list = ["웹사이트로부터 크롤링하여 데이터 베이스를 구축합니다",
                        "코세라 강의를 통해 머신러닝 개념을 공부합니다",
                        "GeForce 2080Ti로 딥러닝 모델을 학습합니다"]
    for idx,(title, user_id, description) in enumerate(zip(title_list, user_id_list, description_list)):
        dic = {}
        dic["id"] = str(idx)
        dic["title"] = title
        dic["user_id"] = user_id
        dic["description"] = description
        result.append(dic)
    return jsonify(result)

@app.route('/task/3', methods=['GET'])
def index_task_3():
    result = []
    title_list = ["routing 공부", "컴포넌트 설계", "JS 개념공부"]
    user_id_list = ["jaccobi14", "lcci0334", "lucy"]
    description_list = ["routing하여 다른 페이지로 이동하는 것을 구상합니다",
                        "react 컴포넌트를 디자인, 설계를 합니다",
                        "django를 이용하여 서버를 구축합니다"]
    for idx,(title, user_id, description) in enumerate(zip(title_list, user_id_list, description_list)):
        dic = {}
        dic["id"] = str(idx)
        dic["title"] = title
        dic["user_id"] = user_id
        dic["description"] = description
        result.append(dic)
    return jsonify(result)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", "-p", help="port number", required=True)
    args = parser.parse_args()
    ## Build model
    app.run(host='0.0.0.0', port=args.port, debug=True)
