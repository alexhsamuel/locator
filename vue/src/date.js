export function date(time) {
  return new Date(time.getFullYear(), time.getMonth(), time.getDate())
}
  
export function formatDate(date) {
  return date ? (
    date.getFullYear() 
    + '-' + (date.getMonth() + 1 + '').padStart(2, '0')
    + '-' + (date.getDate() + '').padStart(2, '0')
  ) : ''
}

export function inRange(date, start, end) {
  return (!start || start <= date) && (!end || date <= end)
}

export function overlap(start0, end0, start1, end1) {
  return (!start0 || !end1 || start0 <= end1)
    && (!start1 || !end0 || start1 <= end0)
}

