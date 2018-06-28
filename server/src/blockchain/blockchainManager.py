
from web3 import Web3
from web3.providers.tester import EthereumTesterProvider
from solc import compile_source
import traceback

w3 = Web3(Web3.HTTPProvider("http://localhost:8545"))

class blockchainManager:
    def __init__(self):
        contract_source_path = '../contract/contract.sol'
        # contract_source_path = '../../contract/contract.sol'
        compiled_sol = self.compile_source_file(contract_source_path)
        contract_id, contract_interface = compiled_sol.popitem()

        # 暂时默认是accounts[0]来创建的吧，用数据库记录另外一个信息
        self.Contract = w3.eth.contract(
            abi=contract_interface['abi'],
            bytecode=contract_interface['bin']
        )


    def bytesToUtf8(self, bytes32Str):
        bytes32Str = bytes32Str.hex().rstrip("0")
        if len(bytes32Str) % 2 != 0:
            bytes32Str = bytes32Str + '0'
        bytes32Str = bytes.fromhex(bytes32Str).decode('utf8')
        return bytes32Str

    def compile_source_file(self, file_path):
       with open(file_path, 'r') as f:
          source = f.read()
       return compile_source(source)

    def register(self, password):
        return w3.personal.newAccount(password)

    def getMaxBlockNum(self):
        return w3.eth.blockNumber

    def getOptions(self, contractinfo):
        candidateList = contractinfo.functions.getCandidateList().call()
        options = []
        for option in candidateList:
            optionCnt = contractinfo.functions.totalVotesFor(option).call()
            # options.append({'option': w3.toText(option), 'cnt': optionCnt})
            options.append({'option': self.bytesToUtf8(option), 'cnt': optionCnt})
        return options

    def getContractInfo(self, address):
        return self.Contract(address=address)

    def getTitle(self, contractinfo):
        return contractinfo.functions.getTitle().call()

    def vote(self, address, option, username):
        try:
            contractinfo = self.getContractInfo(address)
            tx_hash = self.make_vote(contractinfo, option, username)
            return True, tx_hash.hex()
        except:
            traceback.print_exc()
            return False, ''

    def getTransactionReceipt(self, txHash):
        ReceiptInfo = w3.eth.getTransactionReceipt(txHash)
        return ReceiptInfo

    def getTransaction(self, tx_hash):
        txInfo = w3.eth.getTransaction(tx_hash)
        TxInfo = {
            'hash': txInfo['hash'].hex(),
            'nonce': txInfo['nonce'],
            'blockHash': txInfo['blockHash'].hex(),
            'blockNumber': txInfo['blockNumber'],
            'transactionIndex': txInfo['transactionIndex'],
            'from': txInfo['from'],
            'to': txInfo['to'],
            'value': txInfo['value'],
            'gas': txInfo['gas'],
            'gasPrice': txInfo['gasPrice'],
            'input': txInfo['input'],
            'votingPromoter': '',
            'votingFrom': '',
            'votingTo': ''
        }
        return TxInfo

    def getVotesRecords(self, address):
        try:
            contractinfo = self.getContractInfo(address)
            voterecords = contractinfo.functions.getVotesReceived().call()
            newrecord = []
            for record in voterecords:
                newrecord.append(self.bytesToUtf8(record))
            return True, newrecord
        except:
            return False, []


    def make_vote(self, contractinfo, option, username):
        record = "%s->%s"%(username, option)
        tx_hash = contractinfo.functions.voteForCandidate(w3.toBytes(text=option),w3.toBytes(text=record)).transact(
                transaction={
                    'from': w3.eth.accounts[0],
                    'gas': 120000
                }
            )

        return tx_hash

    def getBlockInfoByIndex(self, index):
        return w3.eth.getBlock(index)

    def deploy_contract(self, originaltor,  args=()):
        tx_hash = self.Contract.deploy(
            transaction={
                'from': w3.eth.accounts[0],
                'gas': 200000000
            },
            # args=('test Title', 'shanxuan', [w3.toBytes(text='Sam'), w3.toBytes(text='Leslie'), w3.toBytes(text='Jetty'), w3.toBytes(text='Arkila'), w3.toBytes(text='Piu')])
            args=args
        )
        address = w3.eth.getTransactionReceipt(tx_hash)['contractAddress']
        return address


__blockchainmanager = blockchainManager()


def getWeb3():
    return w3

def getBlockchainManager():
    return __blockchainmanager


if __name__ == "__main__":
    blockmanager = getBlockchainManager()
    info = blockmanager.getBlockInfoByIndex(1)
    print('---- info ----')
    print(info)
    # address = '0x1fB403B67c8f548d0eAbd8D62757a58ec4f0b6EF'
    # ret, recoreds = blockmanager.getVotesRecords(address)
    # print('----- recoreds -----')
    # print(recoreds)

#     transaction
#     tx_hash = contractinfo.functions.voteForCandidate(w3.toBytes(text='A')).transact(
#         transaction={
#             'from': w3.eth.accounts[0],
#             'gas': 67000
#         }
#     )
#     print(tx_hash)
    # w3.eth.waitForTransactionReceipt(tx_hash)
# #     check transaction
#     result = contractinfo.functions.totalVotesFor(w3.toBytes(text='A')).call()
#     print(result)





















