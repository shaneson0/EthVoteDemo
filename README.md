# EthVoteDemo
本人学习solidity的投票demo http://114.215OB.132.245/?#/，使用python编写dapp的服务端代码，采用的是flask+web3框架；前端使用的是vue.js


![image.png](https://upload-images.jianshu.io/upload_images/5786775-3ac7b77237c01dbd.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![image.png](https://upload-images.jianshu.io/upload_images/5786775-cffdba78c6da5f1b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

-----------

### 部署方案

```

git clone git@github.com:shanxuanchen/EthVoteDemo.git

# install truffle and testrpc
npm install -g truffle
npm install -g testrpc

# serve test network at localhost:8545 in a separate terminal
testrpc

# client
cd EthVoteDemo/client/votedemo/

# 先安装前端的包
npm install --save

npm run dev

# 访问localhost:8080

# server
# 先找个干净的目录安装一个python的虚拟环境，需要python3.6

cd ../../
virtualenv -p python3.6 env
source env/bin/activate

# install package
pip install flask
pip install DBUtils
pip install pymysql


# install web3
# 如果有环境的话，很简单pip install web3就可以了，但是环境没有齐全的话就估计比较麻烦(自行google，如何安装web3和py-solc)

pip install web3
pip install py-solc


# 进入目录
cd EthVoteDemo/server/src
pythpn app.py

#如果发生了报错，检查一下sol的路径问题




```