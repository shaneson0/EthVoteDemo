import axios from 'axios'
import config from '../config/index'

export const request = (method, uri, data = null) => {
  if (!method) {
    console.error('API function call requires method argument')
    return
  }

  if (!uri) {
    console.error('API function call requires uri argument')
    return
  }
  data = encodeURI(data)
  var url = config.serverURI + uri
  return axios({ method, url, data })
}

