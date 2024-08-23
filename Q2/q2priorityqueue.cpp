#include <iostream>
#include <vector>
#include <queue>
#include <climits>
#include <functional> // Include the functional header for the function template
#include <chrono>     // Include the chrono header for measuring time

using namespace std;

// Structure to represent a node in the graph
struct Node
{
    int id;
    int distance;
};

// Function to implement Dijkstra's algorithm
void dijkstra(vector<vector<pair<int, int>>> &graph, int source)
{
    int n = graph.size();
    vector<int> distances(n, INT_MAX); // Initialize distances to infinity
    vector<bool> visited(n, false);    // Initialize visited array

    // Create a priority queue to store nodes
    priority_queue<Node, vector<Node>, function<bool(Node, Node)>> pq([](Node a, Node b)
                                                                      { return a.distance > b.distance; });

    // Set distance of source node to 0 and push it to the priority queue
    distances[source] = 0;
    pq.push({source, 0});

    while (!pq.empty())
    {
        // Extract the node with minimum distance from the priority queue
        Node curr = pq.top();
        pq.pop();

        int u = curr.id;

        // If the node is already visited, skip it
        if (visited[u])
        {
            continue;
        }

        visited[u] = true;

        // Iterate through all the adjacent nodes of the current node
        for (auto neighbor : graph[u])
        {
            int v = neighbor.first;
            int weight = neighbor.second;

            // If the distance to v through u is shorter than the current distance to v, update it
            if (distances[u] + weight < distances[v])
            {
                distances[v] = distances[u] + weight;
                pq.push({v, distances[v]});
            }
        }
    }

    // Print the shortest distances from the source node to all other nodes
    cout << "Shortest distances from source node " << source << ":\n";
    for (int i = 0; i < n; i++)
    {
        cout << "Node " << i << ": " << distances[i] << "\n";
    }
}

int main()
{
    // Generate a large graph with random edges and nodes
    int numNodes = 100; // Specify the number of nodes
    vector<vector<pair<int, int>>> graph(numNodes);
    
    // Randomly assign edges between nodes
    for (int i = 0; i < numNodes; i++)
    {
        int numEdges = rand() % (numNodes - 1) + 1; // Randomly assign a number of edges between 1 and numNodes-1
        for (int j = 0; j < numEdges; j++)
        {
            int neighbor = rand() % numNodes; // Randomly select a neighbor node
            int weight = rand() % 10 + 1;     // Randomly assign a weight between 1 and 10
            graph[i].push_back({neighbor, weight});
        }
    }

    int source = 0;

    auto start = chrono::high_resolution_clock::now(); // Start measuring time

    dijkstra(graph, source);

    auto end = chrono::high_resolution_clock::now();                          // Stop measuring time
    auto duration = chrono::duration_cast<chrono::microseconds>(end - start); // Calculate the duration in microseconds

    cout << "Execution time: " << duration.count() << " microseconds\n"; // Print the execution time

    return 0;
}