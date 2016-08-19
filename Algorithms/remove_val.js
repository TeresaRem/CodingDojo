// REMOVE
function removeVal(list, value)
{
  if (!list) return null;
  if (list.val === value) return list.next;

  var runner = list;
  while (runner.next) {
    if (runner.next.val === value) {
      runner.next = runner.next.next;
      break;
    }
    runner = runner.next;
  }
  return list;
}