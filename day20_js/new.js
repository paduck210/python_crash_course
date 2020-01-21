function sumArray(array) {
  if ((array === null) || (array === None)){
    return 0
  } else if (array.length === 1){
    return 0
  } else if (array.length > 2) {
    array.sort((a, b) => {
      return a - b
    })
    array.pop()
    array.shift()
    return array.reduce((a, b) => a + b, 0)
  } else {
    return array.reduce((a, b) => a + b, 0)
  }
}
