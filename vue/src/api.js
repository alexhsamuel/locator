async function get(url) {
  url = '/api/v1' + url
  const rsp = await fetch(url)
  if (rsp.status != 200) {
    console.log('get', url, 'failed:', rsp)
    return
  }
  const jso = await rsp.json()
  if (jso.status_code != 200) {
    console.log('get', url, 'failed:', jso)
    return
  }
  return jso
}

export async function getStatuses() {
  return (await get('/statuses')).statuses
}

export async function getUsers() {
  return (await get('/users')).users
}

export async function searchEvents() {
  return (await get('/events')).events
}

