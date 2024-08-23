package Q3;

import java.util.*;

public class TarjanSCC {
    private static int index = 0;
    private static Stack<Integer> stack = new Stack<>();
    private List<List<Integer>> graph; // Remove static keyword
    private static int[] indices, lowLink;
    private static boolean[] onStack;
    private static List<List<Integer>> sccList = new ArrayList<>();

    public TarjanSCC(List<List<Integer>> graph) {
        this.graph = graph;
        indices = new int[graph.size()];
        lowLink = new int[graph.size()];
        onStack = new boolean[graph.size()];
        Arrays.fill(indices, -1);
    }

    public List<List<Integer>> findSCC() {
        for (int v = 0; v < graph.size(); v++) {
            if (indices[v] == -1) {
                strongConnect(v);
            }
        }
        return sccList;
    }

    private void strongConnect(int v) {
        indices[v] = lowLink[v] = index++;
        stack.push(v);
        onStack[v] = true;

        for (int w : graph.get(v)) {
            if (indices[w] == -1) {
                strongConnect(w);
                lowLink[v] = Math.min(lowLink[v], lowLink[w]);
            } else if (onStack[w]) {
                lowLink[v] = Math.min(lowLink[v], indices[w]);
            }
        }

        if (lowLink[v] == indices[v]) {
            List<Integer> scc = new ArrayList<>();
            int w;
            do {
                w = stack.pop();
                onStack[w] = false;
                scc.add(w);
            } while (w != v);
            sccList.add(scc);
        }
    }

    public static void main(String[] args) {
        // Test with an example graph
        List<List<Integer>> graph = Arrays.asList(
            Arrays.asList(1),
            Arrays.asList(2),
            Arrays.asList(0, 3),
            Arrays.asList(4),
            Arrays.asList(5),
            Arrays.asList(4)
        );

        TarjanSCC tarjan = new TarjanSCC(graph);
        List<List<Integer>> sccs = tarjan.findSCC();
        System.out.println("SCCs: " + sccs);
    }
}
