function isIsogram(str){

    for (const i in str) {
        return (str.length - str.replaceAll(i, "").length) > 2 ? false : true;
    }

}

console.log(isIsogram("aba"));

