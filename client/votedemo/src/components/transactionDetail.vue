<template>
  <div class="modal fade" id="myModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
    <div class="modal-dialog" style=" width: auto;">
      <div class="modal-content">
        <div class="modal-header">
          <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
          <h4 class="modal-title" id="myModalLabel">
            <small>交易详情
              <span style="color: red" v-show="Info.to === '0x0'">（创建投票）</span>
              <span style="color: red" v-show="Info.to !== '0x0'">（投票详情）</span>
            </small>
          </h4>
        </div>
        <div class="modal-body">
          <div class="row" style="width: inherit">
            <div class="col-xs-12 col-sm-12" >
              <div class="box">
                <!-- /.box-header -->
                <div class="box-body no-padding">
                  <table class="table table-striped">
                    <thead>
                    </thead>
                    <tbody>
                    <tr v-show="Info.to === '0x0'">
                      <th>发起人</th>
                      <th>{{Info.votingPromoter}}</th>
                    </tr>
                    <tr v-show="Info.to !== '0x0'">
                      <th>投票人</th>
                      <th>{{Info.votingFrom}}</th>
                    </tr >
                    <tr v-show="Info.to !== '0x0'">
                      <th>投票选项</th>
                      <th>{{Info.votingTo}}</th>
                    </tr>
                    <tr>
                      <th>hash</th>
                      <th>{{Info.hash}}</th>
                    </tr>
                    <tr>
                      <th>nonce</th>
                      <th>{{Info.nonce}}</th>
                    </tr>
                    <tr>
                      <th>blockHash</th>
                      <th>{{Info.blockHash}}</th>
                    </tr>
                    <tr>
                      <th>blockNumber</th>
                      <th>{{Info.blockNumber}}</th>
                    </tr>
                    <tr>
                      <th>transactionIndex</th>
                      <th>{{Info.transactionIndex}}</th>
                    </tr>
                    <tr>
                      <th>from</th>
                      <th>{{Info.from}}</th>
                    </tr>
                    <tr>
                      <th>to</th>
                      <th>{{Info.to}}</th>
                    </tr>
                    <tr>
                      <th>value</th>
                      <th>{{Info.value}}</th>
                    </tr>
                    <tr>
                      <th>gas</th>
                      <th>{{Info.gas}}</th>
                    </tr>
                    <tr>
                      <th>input</th>
                      <th>{{Info.input}}</th>
                    </tr>


                    </tbody>

                  </table>
                </div>
                <!-- /.box-body -->
              </div>
            </div>
          </div>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-default" data-dismiss="modal">关闭</button>
          <button type="button" class="btn btn-primary" >确定</button>
        </div>
      </div><!-- /.modal-content -->
    </div><!-- /.modal -->
  </div>
</template>

<script>
  import * as API from '../api/index'

  export default {
    name: 'transactionDetail',
    props: ['Info'],
    data: function () {
      return {}
    },
    created: function () {
    }
  }
</script>
