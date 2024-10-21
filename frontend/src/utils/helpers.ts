//DD.MM
export const formatDateForWeekLabel = (date: any) => {
  let day = date.getDate() - 1;
  let month = date.getMonth() + 1;
  return `${day < 10 ? "0" : ""}${day}.${month < 10 ? "0" : ""}${month}`;
};

// YYYY-MM-DD hh:mm:ss
export function formatDate(date: any) {
  let year = date.getFullYear();
  let month = ("0" + (date.getMonth() + 1)).slice(-2);
  let day = ("0" + date.getDate()).slice(-2);
  let hours = ("0" + date.getHours()).slice(-2);
  let minutes = ("0" + date.getMinutes()).slice(-2);
  let seconds = ("0" + date.getSeconds()).slice(-2);
  return `${year}-${month}-${day} ${hours}:${minutes}:${seconds}`;
}
