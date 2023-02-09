#include<SFML/Graphics.hpp>
#include<iostream>
using namespace std;
int main() {
	int size;
	cout << "Enter circle size: " << endl;
	cin >> size;


	int color;
	int color2;
	int color3;
	cout << "Enter RGB color values : " << endl;
	cin >> color;
	cin >> color2;
	cin >> color3;

	int xvalue;
	int yvalue;
	cout << "Enter x and y value : " << endl;
	cin >> xvalue;
	cin >> yvalue;


	sf:: RenderWindow window(sf::VideoMode (800, 800), "SFML CIRCLES");
	sf::CircleShape circle;

	while (window.isOpen()) {
		sf::Event event;
		while (window.pollEvent(event))
		{
			if (event.type == sf::Event::Closed)
				window.close();
		}
		//render section------
		//circle settings---
		circle.setRadius(size);
		circle.setFillColor(sf::Color(color, color2, color3));
		circle.setPosition(xvalue, yvalue);

		window.draw(circle);
		window.display(); //flip buffer
	}
}
