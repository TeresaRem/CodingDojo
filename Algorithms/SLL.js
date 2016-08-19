// NODE CONSTRUCTOR
function listNode(value)
{
  this.val = value;
  this.next = null;
}

// LINKED LIST CONSTRUCTOR
function singlyLinkedList(){
  this.head = null;
}

// PUSH TO FRONT
function pushFront(firstNode, value)
{
  var newHead = new listNode(value);
  newHead.next = firstNode;
  return newHead;
}

// REMOVE FROM FRONT
function removeFront(firstNode)
{
  if (firstNode) {
    firstNode = firstNode.next;
  }
  return firstNode;
}

// COINTAINS
function contains(list, value)
{
  while (list)
  {
// Note: 1 == true == [1] == "1",
// which is NOT really what we want. 
// Instead use ===, to be very specific.
    if (list.val === value)
    {

// Leave immediately as soon as we find it!
      return true;
    }
    list = list.next;
  }

// If we got this far, we didn't find it!
  return false;
}

// DISPLAY
function display(list) {
  var displayStr = "List values: (";

  while (list) {
    if (typeof list.val === "string") { 
      displayStr += "'" + list.val + "'"; 
    } else if (typeof list.val === "object" 
           && list.val instanceof Array) {
      displayStr += "[" + list.val + "]";
    } else {
      displayStr += list.val;
    }

    list = list.next;
    if (list) {
      displayStr += ", ";
    }
  }

  displayStr += ")";
  return displayStr;
}

// MIN AND MAX
function min(list) {
  if (!list) { return null; }
  var lowVal = list.val;
  list = list.next;
  while (list) {
    if (list.val<lowVal) lowVal = list.val;
    list = list.next;
  }
  return lowVal;
}

function max(list) {
  if (!list) { return null; }
  var highVal = list.val;
  list = list.next;
  while (list) {
    if (list.val>highVal) highVal=list.val;
    list = list.next;
  }
  return highVal;
}

// APPEND
function appendVal(list, value, after)
{
  var newNode = new listNode(value);
  if (!list) return newNode;

  var runner = list;
  while (runner.next) {
    if (runner.val === after) { break; }
    runner = runner.next;
  }
  newNode.next = runner.next;
  runner.next = newNode;
  return list;
}

// PREPEND
function prependVal(list, value, before)
{
  var newNode = new listNode(value);
  if (!list || list.val === before) {
    newNode.next = list;
    return newNode;
  }

  var runner = list;
  while (runner.next) {
    if (runner.next.val===before) { break;}
    runner = runner.next;
  }
  newNode.next = runner.next;
  runner.next = newNode;
  return list;
}