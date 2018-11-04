export async function searchEvents() {
  const rsp = await fetch('/api/v1/events')
  const jso = await rsp.json()
  if (jso.status_code == 200)
    return jso.events
  else
    console.log('fail', rsp)
}

