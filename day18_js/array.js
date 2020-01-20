function comp(array1, array2){
  const array3 = array1.map(number => number * number).sort();
  if (array2 == []) {
    return False;
  } else {
    return array2.sort().join("") === array3.join("");
  }

array1 = [42, 74]
array2 = [1764, 5476]
console.log(comp(array1,array2))
