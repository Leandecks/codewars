function order(words){

    let result = "";
    const w = words.split(" ");

    let j = 0;

    while (result.length < words.length) {
        for (j; j < w.length; j++) {
            if (w[j].includes(j)) {
                result += w[j];
            } else {
                -- j;
            }
        }
    }

    // let j = 0
    // while (result.length < words.length) {
    //     j ++;
    //     if (w[j].includes(j)) {
    //         result += w[j];
    //     }
    // }

    return result;

}

console.log(order("is2 Thi1s T4est 3a"));