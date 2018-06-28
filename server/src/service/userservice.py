# coding=utf-8

import sys
sys.path.append("..")


from db import opDBP
from blockchain import blockchainManager

def insertUserlib(username, password, account):
    sql = "insert into user(account, username, password) VALUES ('%s', '%s', '%s')"%(account, username, password)
    print(sql)
    sys.stdout.flush()
    ret,msg = opDBP.OpExecWrite(sql)
    return ret

def selectUserlib(username, password):
    sql = "select account from user where username = '%s' and password = '%s'"%(username, password)
    res = opDBP.OpExecRead(sql)
    if len(res) > 0:
        return True, res[0][0]
    else:
        return False, ''

def register(username, password):
    account = blockchainManager.getBlockchainManager().register(password)
    if insertUserlib(username, password, account):
        return True, account
    else:
        return False, ''


def login(username, password):
    # web3.personal.unlockAccount(account, "password", 15000);
    ret, account = selectUserlib(username, password)
    # if ret:
    #     w3 = blockchainManager.getWeb3()
    #     w3.personal.unlockAccount(account, password, 15000)
    return ret, account
