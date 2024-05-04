// function friend(friends){
//
//     const fr = [];
//
//     for (const friend of friends) {
//         if (friend.length === 4) {
//             fr.push(friend);
//         }
//     }
//
//     return fr;
//
// }

function friend(friends) {
    return friends.filter(friend => friend.length === 4);
}

console.log(friend(["Ryan", "Kieran", "Mark"]));