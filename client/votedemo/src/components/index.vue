<template>

  <div class="container" >
    <div class="container">
      <h1>投票列表</h1>
      <div class="container">
        <div class="row">
          <div class="col-xs-12 col-sm-12" >
            <div class="box">
              <!-- /.box-header -->
              <div class="box-body no-padding">
                <table class="table table-striped">
                  <thead>
                  <tr>
                    <th>投票名称</th>
                    <th>发起人</th>
                    <th>智能合约</th>
                    <th>操作</th>
                  </tr>
                  </thead>
                  <tbody>
                    <tr v-for="contractInfo in contractslist">
                      <td>{{contractInfo.title}}</td>
                      <td>{{contractInfo.username}}</td>
                      <td>{{contractInfo.address}}</td>
                      <!--<td><a href="./VoteInfo.html" @click="JumpToVoteInfo(contractInfo.contractHashId)">查看投票详情</a></td>-->
                      <td><a src="#" @click="JumpToVoteInfo(contractInfo.address)">查看投票详情</a></td>
                    </tr>
                  </tbody>

                </table>
              </div>
              <div class="box-footer">
                <button type="button" class="btn btn-primary pull-right" data-toggle="modal" data-target="#myModal">发起投票</button>
              </div>
            </div>
          </div>
        </div>

      </div>
    </div>

    <div class="modal fade" id="myModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
            <h4 class="modal-title" id="myModalLabel">创建投票</h4>
          </div>
          <div class="modal-body">

            <div class="container" style="width: inherit">
              <div class="row" style="margin-bottom: 10px;">
                <div class="col-lg-6">
                  <div class="input-group">
                    <span class="input-group-addon">投票标题</span>
                    <input type="text" class="form-control" placeholder="输入投票标题" v-model="createTitle">
                  </div>
                </div>

                <div class="col-lg-6">
                  <div class="input-group">
                    <span class="input-group-addon">选项数</span>
                    <input type="number" class="form-control" placeholder="0" v-model="optionsnum">
                  </div>
                </div>
              </div>
              <div class="row" style="margin-bottom: 10px;" v-for="num in parseInt(optionsnum)">
                <div class="col-lg-12">
                  <div class="input-group">
                    <span class="input-group-addon">选项{{num}}</span>
                    <input type="text" class="form-control" name="voteoptions">
                  </div>
                </div>
              </div>
            </div>

          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-default" data-dismiss="modal">关闭</button>
            <button type="button" class="btn btn-primary" @click="createVote()" data-dismiss="modal">提交更改</button>
          </div>
        </div><!-- /.modal-content -->
      </div><!-- /.modal -->
    </div>
  </div>

</template>

<script>

  import * as API from '../api/index'

export default {
  name: 'HelloWorld',
  created: function () {
    if (!sessionStorage.getItem('username')) {
      this.$router.push({path: '/login'})
    }
    this.getBlocksInfo()
  },
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
      contractslist: [],
      createTitle: '',
      optionsnum: 0,
      options: []
    }
  },
  methods: {
    getBlocksInfo: function () {
      const self = this
      API.request('post', '/app/contract/list', null).then(function (res) {
        console.log(res)
        self.contractslist = res.data.data.list
      })
    },
    createVote: function () {
      const self = this
      var values = document.getElementsByName('voteoptions')
      for (var i = 0; i < values.length; i++) {
        this.options.unshift(values[i].value)
      }
      var optionsStr = this.options.join(',')
      var account = '0xd620263816f80f7b399b39b5a53d5290f1014a77'
      var username = sessionStorage.getItem('username')
      var data = `title=${this.createTitle}&options=${optionsStr}&account=${account}&username=${username}`
      API.request('post', '/app/deploy/contract', data).then(function (res) {
        if (res.data.code === 0) {
          self.getBlocksInfo()
        }
      })
    },
    JumpToVoteInfo: function (address) {
      this.$router.push({
        path: '/voteinfo',
        name: 'voteinfo',
        query: {
          address: address
        }
      })
    }
  }
}
</script>

<style scoped>

  .table-striped-warner > tbody > tr:nth-of-type(odd) {
    background-color: #cbc8c7;
  }

  body {
    margin-left: 20%;
    margin-right: 25%;
    margin-top: 3%;
    font-family: "Open Sans", sans-serif;
  }

  label {
    display: inline-block;
    width: 100px;
  }

  input {
    width: 500px;
    padding: 5px;
    font-size: 16px;
  }

  button {
    font-size: 16px;
    padding: 5px;
  }

  h1, h2 {
    display: inline-block;
    vertical-align: middle;
    margin-top: 0px;
    margin-bottom: 10px;
  }

  h2 {
    color: #AAA;
    font-size: 32px;
  }

  h3 {
    font-weight: normal;
    color: #AAA;
    font-size: 24px;
  }

  .black {
    color: black;
  }

  #balance {
    color: black;
  }

  .hint {
    color: #666;
  }


</style>

