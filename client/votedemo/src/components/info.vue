<template>
  <div>
    <div class="container">
      <h1><a>{{Title}}</a></h1>
      <div id="address"></div>
      <div class="table-responsive">
        <table class="table table-bordered">
          <thead>
          <tr>
            <th>Candidate</th>
            <th>Votes</th>
          </tr>
          </thead>
          <tbody>
          <tr v-for="(option, index) in options">
            <td>{{option.option}}</td>
            <td :id="index">{{option.cnt}}</td>
          </tr>
          </tbody>
        </table>
        <div id="msg"></div>
      </div>
      <input type="text" id="candidate" v-model="option"/>
      <a @click="voteForCandidate()" class="btn btn-primary">Vote</a>
    </div>
    <div class="container">
      <div class="row">
        <div class="col-xs-12 col-sm-12" >
          <div class="box">
            <div class="box-header">
              <h3 class="box-title">投票列表</h3>
            </div>
            <!-- /.box-header -->
            <div class="box-body no-padding">
              <table class="table table-striped">
                <thead>
                <tr>
                  <th width="30%">from</th>
                  <th width="30%">-></th>
                  <th width="30%">to</th>
                </tr>
                </thead>
                <tbody>
                <tr v-for="x in voteRecordList">
                  <td>{{x[0]}}</td>
                  <td>-></td>
                  <td>{{x[1]}}</td>
                </tr>
                </tbody>

              </table>
            </div>
            <!-- /.box-body -->
          </div>
        </div>
        <div class="col-xs-12 col-sm-12" >
          <div class="box">
            <div class="box-header">
              <h3 class="box-title">区块列表</h3>
            </div>
            <!-- /.box-header -->
            <div class="box-body no-padding">
              <table class="table table-striped">
                <thead>
                <tr>
                  <th>区块高度</th>
                  <th>交易数量</th>
                  <th>区块哈希</th>
                  <th>操作</th>
                </tr>
                </thead>
                <tbody>
                <tr v-for="(block, index) in BlocksInfo">
                  <td>{{block.number}}</td>
                  <td>{{block.transactionnum}}</td>
                  <td><a href="#">{{block.hash}}</a></td>
                  <td><a href="#" @click="getTransactions(index)">查看交易</a></td>
                </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
        <div class="col-xs-12 col-sm-12" >
          <div class="box">
            <div class="box-header">
              <h3 class="box-title">交易列表</h3>
            </div>
            <!-- /.box-header -->
            <div class="box-body no-padding">
              <table class="table table-striped">
                <thead>
                <tr>
                  <th>交易ID</th>
                  <th>操作</th>
                </tr>
                </thead>
                <tbody>
                <tr v-for="x in transactions">
                  <td>{{x}}</td>
                  <td><a href="#" data-toggle="modal" data-target="#myModal" v-on:click="getTransactionDetail(x)">查看详情</a></td>
                </tr>
                </tbody>

              </table>
            </div>
            <!-- /.box-body -->
          </div>
        </div>
      </div>

    </div>

    <transaction-detail :Info="Info"></transaction-detail>
  </div>
</template>

<script>
  import * as API from '../api/index'
  import TransactionDetail from './transactionDetail.vue'

  export default {
    name: 'voteinfo',
    components: {TransactionDetail},
    created: function () {
      if (!sessionStorage.getItem('username')) {
        this.$router.push({path: '/login'})
      }

      this.address = this.$route.query.address
      this.getContractInfo(this.address)
      this.voteRecord()
      this.getBlockslist()
    },
    data () {
      return {
        Title: '测试',
        options: [],
        BlocksInfo: [],
        transactions: [],
        voteRecordList: [],
        address: '',
        option: '',
        transcationId: 0,
        Info: {
          hash: '',
          nonce: '',
          blockHash: '',
          blockNumber: '',
          transactionIndex: 0,
          from: '',
          to: '',
          value: '',
          gas: '',
          input: '',
          votingPromoter: '',
          votingFrom: '',
          votingTo: ''
        }
      }
    },
    methods: {
      flushTransaction: function (transcationId) {
        const self = this
        const data = `txhash=${transcationId}`
        API.request('post', '/app/transaction/info', data).then(function (res) {
          if ( res.data.code === 0 ) {
            console.log(res.data.data.info)
            self.Info = res.data.data.info
          }
        })
      },
      getContractInfo: function (address) {
        var data = `address=${address}`
        const self = this
        API.request('post', '/app/contract/info', data).then(function (res) {
            if (res.data.code === 0) {
              self.options = res.data.data.info.options
              self.Title = res.data.data.info.title
            }
        })
      },
      voteRecord: function () {
        const self = this
        const data = `address=${this.address}`
        API.request('post', '/app/contract/voterecord', data).then(function (res) {
          if ( res.data.code === 0 ) {
            var list = res.data.data.list
            console.log('---- list ----')
            console.log(list)
            var templist = []
            for (var i = 0; i < list.length; i++) {
              var item = list[i]
              var temp = item.split("->")
              templist.unshift(temp)
            }
            self.voteRecordList = templist
          }
        })
      },
      getBlockslist: function () {
          const self = this
          API.request('post', '/app/blocks/list', null).then(function (res) {
              if (res.data.code === 0) {
                self.BlocksInfo = res.data.data.list
                self.BlocksInfo.reverse()
              }
          })
      },
      getTransactionDetail: function (Txid) {
        this.transcationId = Txid
        this.flushTransaction(Txid)
      },
      getTransactions: function (index) {
        this.transactions = this.BlocksInfo[index]['transactions']
      },
      voteForCandidate: function () {
          const self = this
          const username = sessionStorage.getItem('username')
          var data = `address=${this.address}&option=${this.option}&username=${username}`
          API.request('post', '/app/contract/vote', data).then(function (res) {
              if (res.data.code === 0 ) {
                self.getContractInfo(self.address)
                self.voteRecord()
                self.getBlockslist()
              }
          })
//        address = request.values.get("address", '')
//        option = request.values.get("option", '')
//        account = request.values.get("account", '')
      }
    }
  }
</script>
