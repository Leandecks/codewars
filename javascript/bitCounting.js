let countBits = function(n) {
    let counter = 0;
    const bits = n.toString(2)

    for (const char in bits) {
        if (bits[char] === "1") {
            counter ++;
        }
    }

    return counter;
};

console.log(countBits(1234));