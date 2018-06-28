
from flask import Flask, request, jsonify, make_response

app = Flask(__name__)

from service import userservice, blockchainservice
import traceback


@app.route("/")
def hello():
    return "Hello World!"

@app.route("/app/login", methods=['post', 'get'])
def login():
    try:
        username = request.values.get("username")
        password = request.values.get("password")
        res, account = userservice.login(username, password)
        if res:
            return finalMakeResponse(0, {'account': account}, 200)
            # return make_response(jsonify({'code': 0, 'data': {'account': account}, 'msg': ''}), 200)
        else:
            ret, newaccount = userservice.register(username, password)
            return finalMakeResponse(0, {'account': newaccount}, 200)
            # return make_response(jsonify({'code': 1, 'data': {'account': account}, 'msg': '账号不存在'}), 200)
    except:
        traceback.print_exc()
        return finalMakeResponse(1, {}, 500)

@app.route("/app/register", methods=['post', 'get'])
def register():
    username = request.values.get("username")
    password = request.values.get("password")
    res, msg = userservice.register(username, password)
    if res:
        return finalMakeResponse(0, {}, 200)
    else:
        return finalMakeResponse(1, {}, 200)


@app.route("/app/deploy/contract", methods=['post', 'get'])
def deploy_contract():
    Title = request.values.get("title", "")
    options = request.values.get("options", "")
    account = request.values.get("account", "")
    username = request.values.get("username", "")
    ret, msg = blockchainservice.create_vote(Title, username, account, options)
    if ret:
        return finalMakeResponse(0, {}, 200)
        # return make_response(jsonify({'code': 0, 'data': {}, 'msg': '发起投票成功'}), 200)
    else:
        return finalMakeResponse(1, {}, 200)
        # return make_response(jsonify({'code': 1, 'data': {}, 'msg': '发起投票失败'}), 200)

@app.route("/app/contract/info", methods=['post', 'get'])
def contractInfo():
    address = request.values.get("address", "")
    contractInfo = blockchainservice.getVoteInfo(address)
    # return make_response(jsonify({'code': 0, 'data': {'info': contractInfo}, 'msg': ''}), 200)
    return finalMakeResponse(0,  {'info': contractInfo}, 200)


@app.route("/app/contract/list", methods=['post', 'get'])
def getContracts():
    contractslist = blockchainservice.getContracts()
    # return make_response(jsonify({'code': 0, 'data': {'list': contractslist}, 'msg': ''}), 200)
    return finalMakeResponse(0,  {'list': contractslist}, 200)


@app.route("/app/blocks/list", methods=['post', 'get'])
def getBlocks():
    pagesize = request.values.get("pagesize", 10)
    currentpage = request.values.get("currentpage", 1)
    res, blockslist = blockchainservice.getBlocks(pagesize, currentpage)
    if res:
        return finalMakeResponse(0, {'list': blockslist}, 200)
        # return make_response(jsonify({'code': 0, 'data': {'list': blockslist}, 'msg': ''}), 200)
    else:
        return finalMakeResponse(1,  {'list': blockslist}, 200)
        # return make_response(jsonify({'code': 1, 'data': {'list': blockslist}, 'msg': ''}), 200)

# address, option, account
@app.route("/app/contract/vote", methods=['post', 'get'])
def vote():
    address = request.values.get("address", '')
    option = request.values.get("option", '')
    username = request.values.get("username", '')
    ret, hash = blockchainservice.vote(address, option, username)
    if ret:
        return finalMakeResponse(0, {'hash': hash}, 200)
        # return make_response(jsonify({'code': 0, 'data': {'hash': hash}, 'msg': ''}), 200)
    else:
        return finalMakeResponse(1, {'hash': hash}, 200)
        # return make_response(jsonify({'code': 1, 'data': {'hash': hash}, 'msg': ''}), 200)

@app.route("/app/contract/voterecord", methods=['post', 'get'])
def getVoteRecords():
    address = request.values.get("address", '')
    ret, voterecords = blockchainservice.getVoteRecords(address)
    if ret:
        return finalMakeResponse(0, {'list': voterecords}, 200)
        # return make_response(jsonify({'code': 0, 'data': {'hash': hash}, 'msg': ''}), 200)
    else:
        return finalMakeResponse(1, {'list': voterecords}, 200)

@app.route("/app/transaction/list", methods=['post', 'get'])
def getTransactions():
    index = request.values.get("index", 1)
    info = blockchainservice.getTransactions(index)
    return finalMakeResponse(0, {'info': info}, 200)

@app.route("/app/transaction/info", methods=['post', 'get'])
def getTransactionInfo():
    tx_hash = request.values.get("txhash", '')
    info = blockchainservice.getTransactionInfo(tx_hash)
    return finalMakeResponse(0, {'info': info}, 200)


def finalMakeResponse(code, data, ResCode):
    response = make_response(jsonify({'code': code, 'data': data, 'msg': ''}), ResCode)
    return response



if __name__ == '__main__':
    app.run(host = "0.0.0.0", port=5000, debug=True)



