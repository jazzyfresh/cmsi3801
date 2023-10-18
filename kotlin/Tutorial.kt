import java.util.*

const val COURSE_NUMBER = 3801
// - const val can only be immutable string or primitive
// - val is known at runtime
// - const val is known at compile time
// - this allows the compiler to do optimizations and 
//   substitute the value literal directly in the bytecode
// - const val cannot be declared inside a function
//   because functions are called at runtime.

// the root of your program execution happens in main()
// the compiler knows to look for the main function
// the runtime knows to start executing at the main function()
fun main() {

    // VARIABLES
    val myInt: Int = 444 // explicitly declare type
    val myString = "a string" // type inference

    val immutableString = "kotlin" // val is READ ONLY
    var mutableString = "kotlin" // var is mutable
    mutableString += "is cool"

    // print to stdout
    println(myString)

    // you can index strings like arrays
    println(myString[0])
    println(myString[1])

    // String interpolation
    println("the string is $myString")

    // IF STATEMENTS
    val number = Math.random() * 1000
    if (number != 100.0) {
        println("perfect match")
    } else {
        println("nope")
    }

    // Collections
    val names = listOf<String>("Jazzy", "Dr Toal", "Dondi", "BJ", "Dr Forney")
    //                              ^^^ Generics says this is a list of only String types
    val immutableList = listOf<String>("Jazzy", "Dr Toal", "Dondi", "BJ", "Dr Forney")
    val mutableList = mutableListOf<Int>(100)
    mutableList.add(10)
    immutableList.add(10) // immutable lists don't have an add method

    // FOR LOOPS
    for (name in names) {
        println(name)
    }

    // the .. operator creates a range, including 5
    for (i in 1..5) {
        println(i)
    }
    // the `until` operator creates a range, not including 5
    for (i in 1 until 5) {
        println(i)
    }

    // FUNCTIONS
    // see function definition below
    myFunction("jazzyfresh")

    // OPTIONALS
    // NullPointerExceptions in Java
    /*
        myObject = new Object();

        callAFunction(null);
        // then later inside the function you called...
        thisPassedObject.toString() // =>NullPointerException
     */
    // Here, the java runtime throws an exception (critical error)
    // because we tried to call .toString() on a variable
    // that was actually null. In Java, that is a no no.

    // To avoid this scenario, Kotlin has Optionals

    // How to create an Optional
    val optionalValue: String? = null
    //                       ^ question mark makes it Optional

    // How to use an Optional
    val instagramBio: String? = "null"
    if (instagramBio != null) {
        println(instagramBio.uppercase())
    }
    // Equivalent to the above if-statement:
    // Only execute this line if instagramBio is non-null
    println(instagramBio?.uppercase())


    // CLASSES & OBJECT
    // see class definition below
    var user = Person("Linda", 42, doesSmile = true)
    println(user.description())

    // OBJECT COMPARISON
    // in java
    /*
        "hi" == new String("hi") // false >> because they are two different objects
        "hi".equals(new String("hi"))
    */

    // in kotlin
    println("hi" == "hi")  // == compares the data, not the object reference
    println("hi".equals("HI", ignoreCase = true)) // returns true
    // === does referential comparison: compares object points
    println("hi" === "hi")
    println("" === String(CharArray(0)))
    //      ^^^two different String objects representing empty strings

}

class Person(private val name: String, private var age: Int, doesSmile: Boolean) {
    private val nickname: String

    init {
        val smiley = if (doesSmile) ":)" else ":<"
        nickname = "$name $smiley"
    }

    fun description(): String {
        return "Name: $nickname, age: $age"
    }

    fun hadBirthday() {
        age += 1
    }
}

private fun myFunction(name: String) {
    println("hello!")
}