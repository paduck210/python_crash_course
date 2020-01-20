function descendingOrder(n){
  const list = n.toString().split("");
  let new_list = list.map(number => parseInt(number)).sort().reverse().join("");
  return parseInt(new_list);
}


function descendingOrder(n){
  return parseInt(String(n).split('').sort().reverse().join(''))
}

console.log(descendingOrder(392928));


// Integer, String
// parseInt(n) -> String to Integer
// Str(n) -> Integer to String
// n.toString()

// Array to String
// array.join("")

// String to Array
// String.split(" ")
