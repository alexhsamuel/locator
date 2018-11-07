function status_ok(status) {
  return 200 <= status && status < 300;
}

async function get(url, args={}) {
  url = '/api/v1' + url
  const rsp = await fetch(url, args)
  // FIXME: Do something more useful on failure.
  if (!status_ok(rsp.status)) {
    console.log('fetch', url, 'failed:', rsp)
    return
  }
  const jso = await rsp.json()
  if (!status_ok(jso.status_code)) {
    console.log('fetch', url, 'failed:', jso)
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

export async function postEvent(event) {
  // FIXME: Validate event.
  return (await get('/events', {
    method: 'POST',
    body: JSON.stringify(event),
    headers:{
      'Content-Type': 'application/json'
    },
  })).event
}

