function createPhoneNumber(numbers){

    const x =  numbers.reduce((acc, cur) => acc.toString() + cur.toString());
    return `(${x.slice(0, 3)}) ${x.slice(3, 6)}-${x.slice(6, 10)}`;

}

console.log(createPhoneNumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]));