fun twoOldestAges(ages: List<Int>): List<Int> {

    var max_age = 0
    var second_max_age = 0

    for (age in ages) {
        if (age > max_age) {
            second_max_age = max_age
            max_age = age
        } else if (age > second_max_age) {
            second_max_age = age
        }
    }

    return listOf(second_max_age, max_age)

}

fun main() {
    println(twoOldestAges(listOf(1,5,45,87,8,8)))
}