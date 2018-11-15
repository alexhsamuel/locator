export function date(time) {
  return new Date(time.getFullYear(), time.getMonth(), time.getDate())
}
  
export function formatDate(date) {
  return date ? (
    date.getFullYear() 
    + '-' + (date.getMonth() + '').padStart(2, '0')
    + '-' + (date.getDate() + '').padStart(2, '0')
  ) : ''
}
