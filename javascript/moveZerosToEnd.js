function moveZeros(arr) {
    return arr.filter(n => n !== 0).concat(arr.filter(n => n === 0));
}

console.log(moveZeros([1, 2, 3, 0, 0, 4, 5, 0]));