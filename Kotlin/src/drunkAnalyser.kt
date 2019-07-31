fun main(){
    var drunkScore = 0
    println("Hi, Im Kotlin! Im a machine learning algorithm to tell if people are drunk!")
    println("I will ask you a few questions to tell if you are drunk is that ok? [Y/n]")
    var answer = readLine()
    if (answer == "y" || answer == "Y"){
        println("Ok, lets begin!")
    } else if (answer == "n" || answer == "N"){
        drunkScore += 1
        println("Well, were doing it anyway!")
    } else {
        drunkScore += 5
        println("What was *that*? Well, im going to ignore that and go to the questions!")
    }
    println("Question 1: Whats 9 + 10?")
    answer = readLine()
    if (answer == "19"){
        drunkScore += 0
        println("Correct!")
    } else if (answer == "21"){
        drunkScore += 2
        println("Correct!!")
    } else {
        drunkScore += 5
        println("Not even close!")
    }

    //TODO: Add more questions

    if (drunkScore > 10) {
        println("You are definitely ")
    } else if (drunkScore > 2){
        println("You're a little tipsy")
    } else {
        println("You're not drunk at all! You got a drunk score of $drunkScore")
    }

}