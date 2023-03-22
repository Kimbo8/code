#include<iostream>
using namespace std;

class cutlery {

private:
	int type;
	bool isClean;

public:
	cutlery();
	void printInfo();
	void use();
	void wash();
};

int main() {
	cutlery kim;
	cutlery kimbo;
	kim.printInfo();
	kim.use();
	kim.printInfo();
	kim.wash();
	kim.printInfo();
	kimbo.printInfo();
	kimbo.use();
	kimbo.printInfo();
	kimbo.wash();
	kimbo.printInfo();
}
void cutlery::printInfo() {
	if (type == 1)
		cout << "You have a fork" << endl;

	else if (type == 2)
		cout << "You have a spoon" << endl;

	else
		cout << "You have a knife" << endl;
}


cutlery::cutlery() {
	isClean = true;
	type = rand() % 3;
}

void cutlery::use() {
	if (isClean == true)
		cout << "your silverware is dirty since you used it you need to wash it" << endl;
		isClean = false;
}

void cutlery::wash() {
	if (isClean == false);
		cout << " your utensil is diry, wash wash wash nice and clean, ouuu shiny now its clean" << endl;
		isClean = true;
}
