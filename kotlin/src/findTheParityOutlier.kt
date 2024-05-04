fun find(integers: Array<Int>): Int {

    val odd: MutableList<Int> = mutableListOf()
    val even: MutableList<Int> = mutableListOf()
    for (i in integers) if (i % 2 == 0) even.add(i) else odd.add(i)
    return if (odd.size == 1) odd[0] else even[0]

}

fun main() {
    println(find(arrayOf(2,6,8,-10,3)))
}