package Q3;

import java.util.*;

public class Boruvka {
    private static class Edge {
        int u, v, weight;
        Edge(int u, int v, int weight) {
            this.u = u;
            this.v = v;
            this.weight = weight;
        }
    }

    public static List<Edge> boruvka(List<Edge> edges, int n) {
        UnionFind uf = new UnionFind(n);
        List<Edge> mst = new ArrayList<>();
        int numTrees = n;
        int[] cheapest = new int[n];

        while (numTrees > 1) {
            Arrays.fill(cheapest, -1);

            for (int i = 0; i < edges.size(); i++) {
                Edge edge = edges.get(i);
                int set1 = uf.find(edge.u);
                int set2 = uf.find(edge.v);

                if (set1 != set2) {
                    if (cheapest[set1] == -1 || edge.weight < edges.get(cheapest[set1]).weight) {
                        cheapest[set1] = i;
                    }
                    if (cheapest[set2] == -1 || edge.weight < edges.get(cheapest[set2]).weight) {
                        cheapest[set2] = i;
                    }
                }
            }

            for (int i = 0; i < n; i++) {
                if (cheapest[i] != -1) {
                    Edge edge = edges.get(cheapest[i]);
                    int set1 = uf.find(edge.u);
                    int set2 = uf.find(edge.v);

                    if (set1 != set2) {
                        mst.add(edge);
                        uf.union(set1, set2);
                        numTrees--;
                    }
                }
            }
        }

        return mst;
    }

    private static class UnionFind {
        private int[] parent, rank;

        UnionFind(int size) {
            parent = new int[size];
            rank = new int[size];
            for (int i = 0; i < size; i++) {
                parent[i] = i;
            }
        }

        int find(int u) {
            if (parent[u] != u) {
                parent[u] = find(parent[u]);
            }
            return parent[u];
        }

        void union(int u, int v) {
            int rootU = find(u);
            int rootV = find(v);
            if (rootU != rootV) {
                if (rank[rootU] > rank[rootV]) {
                    parent[rootV] = rootU;
                } else if (rank[rootU] < rank[rootV]) {
                    parent[rootU] = rootV;
                } else {
                    parent[rootV] = rootU;
                    rank[rootU]++;
                }
            }
        }
    }

    public static void main(String[] args) {
        // Example graph
        List<Edge> edges = Arrays.asList(
            new Edge(0, 1, 4),
            new Edge(0, 2, 1),
            new Edge(1, 2, 2),
            new Edge(1, 3, 5),
            new Edge(2, 3, 8)
        );

        List<Edge> mst = boruvka(edges, 4);
        System.out.println("MST Edges: ");
        for (Edge edge : mst) {
            System.out.println(edge.u + " - " + edge.v + " : " + edge.weight);
        }
    }
}
