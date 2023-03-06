include<iostream>
using namespace std;

class Goomba {
private:
	int xpos;
	int ypos;
	int isAlive;
	char gColor;
public:
	Goomba();
	Goomba(int x, int y);
	void walk();
	void printInfo();
	void kill();
	void setPosition(int x, int y);
	bool CheckisDead();
};

int main() {
	Goomba Lary(300, 400);//uses par
	Goomba Bob;
	Lary.printInfo();
	Lary.walk();
	Lary.printInfo();
	Bob.printInfo();
};

Goomba::Goomba() {
	xpos = 0;
	ypos = 0;
	isAlive = false;
	gColor = 'b';
}
Goomba::Goomba(int x, int y) {
	xpos = x;
	ypos = y;
	isAlive = true;
	gColor = 'l';
}

void Goomba::walk() { xpos += 1; }

void Goomba::kill() { isAlive = false; }

void Goomba::setPosition(int x, int y) {
	xpos = x;
	ypos = y;
	isAlive = true;
}

bool Goomba::CheckisDead() { 
	if (isAlive == false)
		return 0;
	else
		return 1;

}



void Goomba::printInfo() {
	cout << "Hi, I'm a goomba and my position is " << xpos << "," << ypos << endl;
	
	if (gColor == 'b')
		cout << "My color is Brown." << endl;
	else
		cout << "My color is Blue" << endl;
	
	if (isAlive == true)
		cout << "I am currently alive." << endl;
	else
		cout << "I am currently dead." << endl;

}
