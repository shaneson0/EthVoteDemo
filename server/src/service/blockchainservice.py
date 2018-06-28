# coding=utf-8

import sys
sys.path.append("..")
import json

from db import opDBP
from blockchain import blockchainManager
from util import pageUtil

def insertVoteInfo(title, address, username):
    sql = "insert into vote(title, address, username) VALUES ('%s', '%s', '%s')"%(title, address, username)
    return opDBP.OpExecWrite(sql)

def getSqlVoteInfo(address):
    queryfiles = ['title', 'address', 'username']
    sql = "select title, address, username from vote where address = '%s'"%(address)
    res = opDBP.OpExecRead(sql)
    r = [dict(zip(queryfiles, re)) for re in res]
    return r[0]

def getVoteRecordInfo(address):
    queryfiles = ['txHash', 'option', 'username']
    sql = "select txHash, `option`, username from voteRecord where txHash = '%s'"%(address)
    res = opDBP.OpExecRead(sql)
    r = [dict(zip(queryfiles, re)) for re in res]
    return r[0]

def insertVoteRecord(txHash, option, username):
    sql = "insert into voteRecord(txHash, `option`, username) VALUES ('%s', '%s', '%s')"%(txHash, option, username)
    return opDBP.OpExecWrite(sql)

def create_vote(Title, username, originaltorAccount, options):
    options = options.split(",")
    w3 = blockchainManager.getWeb3()
    options = [w3.toBytes(text=option) for option in options]
    # options = [option for option in options]
    args = (Title, username, options)
    address = blockchainManager.getBlockchainManager().deploy_contract(originaltorAccount, args)
    return insertVoteInfo(Title, address, username)

def getVoteInfo(address):
    blockchainmanager = blockchainManager.getBlockchainManager()
    contractInfo = blockchainmanager.getContractInfo(address)
    title = blockchainmanager.getTitle(contractInfo)
    options = blockchainmanager.getOptions(contractInfo)
    return {'title': title, 'options': options}


def vote(address, option, account):
    blockchainmanager = blockchainManager.getBlockchainManager()
    ret, hash = blockchainmanager.vote(address, option, account)
    if ret:
        insertVoteRecord(hash, option, account)
    return ret, hash


def getVoteRecords(address):
    blockmanager = blockchainManager.getBlockchainManager()
    return blockmanager.getVotesRecords(address)

def getTransactionInfo(txhash):
    blockchainmanager = blockchainManager.getBlockchainManager()
    info = blockchainmanager.getTransaction(txhash)
    print('---- info -----')
    print(info)
    # 投票
    if info['to'] == '0x0':
        txaddress = info['hash']
        txreceipt = blockchainmanager.getTransactionReceipt(txaddress)
        transactionRecord = getSqlVoteInfo(txreceipt['contractAddress'])
        info['votingTo'] = transactionRecord['title']
        info['votingPromoter'] = transactionRecord['username']
    else:
        txHash = info['hash']
        voteRecord = getVoteRecordInfo(txHash)
        info['votingTo'] = voteRecord['option']
        info['votingFrom'] = voteRecord['username']

    return info

def getBlocks(pagesize, currentpage):
    blockchainmanager = blockchainManager.getBlockchainManager()
    maxBlockNum = blockchainmanager.getMaxBlockNum()
    ret, ffrom, llimit = pageUtil.pageing(maxBlockNum, pagesize, currentpage)
    if not ret:
        return False, []
    res = []
    for index in range(ffrom+1, ffrom + llimit):
        print(index)
        info = blockchainmanager.getBlockInfoByIndex(index)
        if info != None:
            newTransactions = []
            for transaction in info['transactions']:
                newTransactions.append(transaction.hex())
            temp = {
                'number': info['number'],
                'transactionnum': len(info['transactions']),
                'transactions': newTransactions,
                'hash': info['hash'].hex()
            }
            res.append(temp)
        else:
            break
    return True, res


def getTransactions(index):
    blockchainmanager = blockchainManager.getBlockchainManager()
    info = blockchainmanager.getBlockInfoByIndex(index)
    return info['transactions']


def getContracts():
    queryfiles = ['title', 'address', 'username']
    sql = "select title, address, username from vote"
    res = opDBP.OpExecRead(sql)
    r = [dict(zip(queryfiles, re)) for re in res]
    return r

if __name__ == "__main__":
    ret, list = getBlocks(10, 1)
    print('--- list ---')
    print(list)
    # res = getVoteInfo('0x1e4132D64Ee901Fa09459ecECCfA9c0980eA037f')
    # print(res)











