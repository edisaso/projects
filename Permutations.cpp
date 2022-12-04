#include <iostream>
#include <vector>
using namespace std;
vector<int> a[1024];
int vis[1024];
int n, m, k;
void start()
{
	cin >> n >> m;
	int u, v;

	for (int i = 1; i <= m; i++)
	{
		cin >> u >> v;
		a[u].push_back(v); 
		a[v].push_back(u); 
	}
}

void dfs(int u) 
{
	vis[u] = 1; k++;

	for (int i = 0; i<a[u].size(); i++) 
	{
		int v = a[u][i];
		if (vis[v]==0) 
			dfs(v);
	}
}
int main() //Main program
{
	start();
	int v = 0;
	int brcomp = m;
	cout << brcomp << endl;
	while (v<n) 
	{
		if (vis[v]==0)
		{
			k = 0; dfs(v);
			cout <<  k << "  ";
		}
		v++;
	}
	system("pause");
	return 0;
}
