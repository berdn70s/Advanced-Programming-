#include <iostream>

int main() {
    std::cout << " What is your name?\n"
                 "Ege\n"
                 "Hello Ege.\n"
                 "What is your Student ID? 20190120023\n"
                 "Your ID is 20190120023.";
    std::cout <<"\n";

    //2nd question
    int var1;
    std::cin >> var1;
    int var2;
    std::cin >> var2;
    int sum = var1+ var2;
    int diff = var1 > var2 ?  var1-var2 : var2- var1;
    int prod = var1 * var2;
    std::cout << sum  ;
    std::cout << " "  ;
    std::cout << diff ;
    std::cout << " "  ;

    std::cout << prod ;

    //3rd question
    std::cout <<"\n ";

    std::string name;
    double lab_grade, midterm_grade, final_grade, final_score;
    std::cout << "Enter the student's name: ";
    std::cin >> name;

    std::cout << "Enter the lab grade (out of 100): ";
    std::cin >> lab_grade;

    std::cout << "Enter the midterm grade (out of 100): ";
    std::cin >> midterm_grade;

    std::cout << "Enter the final grade (out of 100): ";
    std::cin >> final_grade;

    final_score = lab_grade * 0.25 + midterm_grade * 0.35 + final_grade * 0.4;

    std::cout << "The final score for " << name << " is: " << final_score;
//4th question
    std::cout <<"\n ";

    std::cout <<"*\n **\n ***\n **\n *";

    return 0;
}
