package Q3;

import java.util.*;

public class Dijkstra {
    private static final int INF = Integer.MAX_VALUE;

    public static int[] dijkstra(List<List<int[]>> graph, int source) {
        int n = graph.size();
        int[] dist = new int[n];
        Arrays.fill(dist, INF);
        dist[source] = 0;

        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[1]));
        pq.add(new int[]{source, 0});

        while (!pq.isEmpty()) {
            int[] curr = pq.poll();
            int u = curr[0], d = curr[1];

            if (d > dist[u]) continue;

            for (int[] edge : graph.get(u)) {
                int v = edge[0], weight = edge[1];
                if (dist[u] + weight < dist[v]) {
                    dist[v] = dist[u] + weight;
                    pq.add(new int[]{v, dist[v]});
                }
            }
        }
        return dist;
    }

    public static void main(String[] args) {
        // Example graph with non-negative weights
        List<List<int[]>> graph = Arrays.asList(
            Arrays.asList(new int[]{1, 4}, new int[]{2, 1}),
            Arrays.asList(new int[]{2, 2}),
            Arrays.asList(new int[]{3, 5}),
            Arrays.asList()
        );

        int[] dist = dijkstra(graph, 0);
        System.out.println("Distances from source 0: " + Arrays.toString(dist));
    }
}
