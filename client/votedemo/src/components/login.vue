<template>
  <div class="login-form">
    <h2 class="text-center">基于区块链的投票系统</h2>
    <form>
      <div class="avatar">
        <img src="/static/image/avatar.png" alt="Avatar">
      </div>
      <div class="form-group">
        <input type="text" class="form-control input-lg"   required="required" v-model="username">
      </div>
      <div class="form-group">
        <input type="password" class="form-control input-lg"  required="required" v-model="password">
      </div>
      <div class="form-group clearfix">
        <label class="pull-left checkbox-inline"><input type="checkbox"> Remember me</label>
        <button class="btn btn-primary btn-lg pull-right" @click="login()">Sign in</button>
      </div>
    </form>
    <div class="hint-text">如果之前没有注册会自动注册然后分配accountId</div>
  </div>
</template>


<script>
  import * as API from '../api/index'

  export default {
    name: 'login',
    data: function () {
      return {
        username: '',
        password: ''
      }
    },
    methods: {
      login: function () {
        const self = this
        const data = `username=${this.username}&password=${this.password}`
        API.request('post', '/app/login', data).then(function (res) {
          console.log(res)
          if (res.data.code === 0) {
            console.log(res.data.data.account)
            sessionStorage.setItem('username', self.username)
            self.$router.push({
              path: '/'
            })
          }
        })
      }
    }
  }
</script>

<style type="text/css" scoped>
  body {
    color: #4e4e4e;
    background: #e2e2e2;
    font-family: 'Roboto', sans-serif;
  }
  .form-control {
    background: #f2f2f2;
    font-size: 16px;
    border-color: transparent;
    box-shadow: none !important;
  }
  .form-control:focus {
    border-color: #91d5a8;
    background: #e9f5ee;
  }
  .form-control, .btn {
    border-radius: 2px;
  }
  .login-form {
    width: 380px;
    margin: 0 auto;
  }
  .login-form h2 {
    margin: 0;
    padding: 30px 0;
    font-size: 34px;
  }
  .login-form .avatar {
    margin: 0 auto 30px;
    width: 100px;
    height: 100px;
    border-radius: 50%;
    z-index: 9;
    background: #4aba70;
    padding: 15px;
    box-shadow: 0px 2px 2px rgba(0, 0, 0, 0.1);
  }
  .login-form .avatar img {
    width: 100%;
  }
  .login-form form {
    color: #7a7a7a;
    border-radius: 4px;
    margin-bottom: 20px;
    background: #fff;
    box-shadow: 0px 2px 2px rgba(0, 0, 0, 0.3);
    padding: 30px;
  }
  .login-form .btn {
    font-size: 16px;
    line-height: 26px;
    min-width: 120px;
    font-weight: bold;
    background: #4aba70;
    border: none;
  }
  .login-form .btn:hover, .login-form .btn:focus{
    background: #40aa65;
    outline: none !important;
  }
  .checkbox-inline {
    margin-top: 14px;
  }
  .checkbox-inline input {
    margin-top: 3px;
  }
  .login-form a {
    color: #4aba70;
  }
  .login-form a:hover {
    text-decoration: underline;
  }
  .hint-text {
    color: #999;
    text-align: center;
    padding-bottom: 15px;
  }
</style>
