function stonePick(arr) {

    let sticks = 0;
    let cobbles = 0;

    for (const i in arr) {
        if (i === "Sticks") {
            sticks ++;
        } else if (i === "Cobblestone") {
            cobbles ++;
        } else if (i === "Wood") {
            sticks += 4;
        }
    }

    return Math.max(Math.floor(sticks / 2), Math.floor(cobbles / 3));

}

console.log(stonePick(["Sticks", "Sticks", "Sticks", "Cobblestone", "Cobblestone", "Cobblestone", "Cobblestone"]));