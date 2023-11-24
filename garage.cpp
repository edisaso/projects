#define _CRT_SECURE_NO_WARNINGS


#include <iostream>
#include <vector>
#include <ctime>
#include <string>

using namespace std;

class ParkingUser {
public:
	string username;
	time_t entryTime;
	bool isCardUser;

	ParkingUser(string name, bool cardUser) : username(name), isCardUser(cardUser) {
		time(&entryTime); // Set entry time to current time using time() function
	}
};

class ParkingGarage {
private:
	vector<ParkingUser> users;

public:
	void addUser(string username, bool isCardUser) {
		ParkingUser newUser(username, isCardUser);
		users.push_back(newUser);
		cout << "User " << username << " entered the parking at " << ctime(&newUser.entryTime);
	}

	void removeUser(string username) {
		for (auto it = users.begin(); it != users.end(); ++it) {
			if (it->username == username) {
				users.erase(it);
				cout << "User " << username << " exited the parking." << endl;
				break;
			}
		}
	}

	void displayUsers() {
		cout << "Users inside the parking:" << endl;
		for (const auto& user : users) {
			cout << user.username << " - Entry Time: " << ctime(&user.entryTime);
		}
	}

	double calculateStayCost(const ParkingUser& user) {
		time_t exitTime = time(0);
		double minutes = difftime(exitTime, user.entryTime) / 60.0;
		double cost = minutes * 0.10;
		return cost;
	}

	void processExit(string username) {
		for (const auto& user : users) {
			if (user.username == username) {
				double cost = calculateStayCost(user);
				if (user.isCardUser && !isWithinOperatingHours()) {
					cost += 10.0; // Penalty for card users outside 9:00 - 18:00
				}
				cout << "Amount to be paid by " << username << ": " << cost << " BGN" << endl;
				removeUser(username);
				break;
			}
		}
	}

	bool isWithinOperatingHours() {
		time_t now = time(0);
		tm* current_time = localtime(&now);
		int hour = current_time->tm_hour;
		return (hour >= 9 && hour < 18);
	}
};

int main() {
	ParkingGarage garage;

	while (true) {
		cout << "\n1. User login with ticket\n";
		cout << "2. User login with card\n";
		cout << "3. User exit with ticket\n";
		cout << "4. User exit with card\n";
		cout << "5. Show all users inside the parking\n";
		cout << "6. Exit\n";
		cout << "Enter your choice: ";

		int choice;
		cin >> choice;

		switch (choice) {
		case 1: {
					string username;
					cout << "Enter username: ";
					cin >> username;
					garage.addUser(username, false);
					break;
		}
		case 2: {
					string username;
					cout << "Enter username: ";
					cin >> username;
					garage.addUser(username, true);
					break;
		}
		case 3: {
					string username;
					cout << "Enter username: ";
					cin >> username;
					garage.processExit(username);
					break;
		}
		case 4: {
					string username;
					cout << "Enter username: ";
					cin >> username;
					garage.processExit(username);
					break;
		}
		case 5:
			garage.displayUsers();
			break;
		case 6:
			return 0;
		default:
			cout << "Invalid choice. Please try again.\n";
		}
	}

	return 0;
}
