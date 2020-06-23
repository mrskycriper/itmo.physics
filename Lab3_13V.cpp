#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>

#define M0 0.00000125663
#define I 1
using namespace std;

class Data
{
public:
	double X {};
	double Y {};
	double Z {};
	double Bx {};
	double By {};
	double Bz {};

	Data(double x, double y, double z, double bx, double by, double bz) : X(x), Y(y), Z(z), Bx(bx), By(by), Bz(bz) {};
	Data() = default;;
};

bool compareZ(Data x, Data y)
{
	return x.Z < y.Z;
}

bool compare(double X, double Y)
{
	{
		return X < Y;
	}
}

void printData(const vector <Data>& array)
{
	for (const auto& i : array)
	{
		cout << i.X << '\t' << i.Y << '\t' << i.Z << '\t' << i.X << '\t' << i.Bx << '\t' << i.By << '\t' << i.Bz;
	}
}

string convertToExcel(double value)
{
	string buffer = to_string(value);
	auto it = find(buffer.begin(), buffer.end(), '.');
	if (it != buffer.end())
	{
		*it = ',';
	}
	return buffer;
}

int main()
{
	string input;
	vector <Data> array;
	double R;
	double distance;

	cout << "File name: ";
	cin >> input;
	cout << "Radius: ";
	cin >> R;
	cout << "Distance between: ";
	cin >> distance;

	ifstream input_file(input + ".txt");
	ofstream output_file_Bz(input + "_Bz.txt");
	ofstream output_file_grad_Bz(input + "_grad_Bz.txt");
	ofstream output_file_grad_Bxy(input + "_grad_Bxy.txt");
	ofstream output_file_check_Bz(input + "_check_Bz.txt");

	for (int i = 0; i < 9; ++i)
	{
		string buffer;
		getline(input_file, buffer);
	}

	double X, Y, Z, Bx, By, Bz;
	while (input_file >> X >> Y >> Z >> Bx >> By >> Bz)
	{
		array.emplace_back(X, Y, Z, Bx * M0, By * M0, Bz * M0);
	}

	cout << "Size: " << array.size() << endl;
	printData(array);

	for (auto& i : array)
	{
		output_file_Bz << convertToExcel(i.Z) << '\t' << convertToExcel(sqrt(pow(i.Bx, 2.0) + pow(i.By, 2.0) + pow(i.Bz, 2.0))) << endl;
	}

	sort(array.begin(), array.end(), compareZ);

	for (int i = 0; i < array.size() - 1; i++)
	{
		output_file_grad_Bz << convertToExcel(array[i].Bz / array[i + 1].Bz) << endl;
	}

	vector <double> array_Bxy;
	array_Bxy.reserve(array.size());
	for (auto& i : array)
	{
		array_Bxy.push_back(sqrt(pow(i.Bx, 2.0) + pow(i.By, 2.0)));
	}

	sort(array_Bxy.begin(), array_Bxy.end(), compare);

	for (int i = 0; i < array.size() - 1; i++)
	{
		output_file_grad_Bxy << convertToExcel(array_Bxy[i] / array_Bxy[i + 1]) << endl;
	}

	for (auto& i : array)
	{
		output_file_check_Bz << i.Bz << '\t' << ((M0 * I * R * R) / 2.0) * ((1.0 / (pow(i.Z * i.Z + R * R, 1.5)) + (1.0 / (pow(pow(i.Z - distance, 2) + R * R, 1.5))))) << endl;
	}

	return 0;
}
