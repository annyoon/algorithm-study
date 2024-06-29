import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

/**
 * SWEA 7465 창용 마을 무리의 개수
 * 1. 마을 사람들의 관계를 인접 리스트로 표현한다
 * 2. 한 번 탐색한 사람은 다시 방문하지 않아도 되므로 서로 알고 있는 관계를 DFS 탐색한다
 * 3. DFS가 한 번 수행될 때마다 무리의 수를 1 증가시킨다
 */

public class Solution {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder sb = new StringBuilder();

	static int N, M, count; // 사람 수, 관계 수, 무리 수
	static ArrayList<Integer>[] relation; // 인접 리스트
	static boolean[] visited;

	public static void main(String[] args) throws NumberFormatException, IOException {
		int T = Integer.parseInt(br.readLine().trim());

		for (int testCase = 1; testCase <= T; testCase++) {
			String[] input = br.readLine().trim().split(" ");
			N = Integer.parseInt(input[0]);
			M = Integer.parseInt(input[1]);
			count = 0;

			relation = new ArrayList[N + 1];
			visited = new boolean[N + 1];

			for (int idx = 0; idx <= N; idx++)
				relation[idx] = new ArrayList<Integer>();

			for (int i = 0; i < M; i++) {
				input = br.readLine().trim().split(" ");
				int num1 = Integer.parseInt(input[0]);
				int num2 = Integer.parseInt(input[1]);

				// 리스트에 관계 추가
				relation[num1].add(num2);
				relation[num2].add(num1);
			}

			for (int person = 1; person <= N; person++)
				// 방문하지 않은 사람이면 DFS로 아는 관계 모두 탐색
				if (!visited[person]) {
					dfs(person);
					count++;
				}

			sb.append("#").append(testCase).append(" ");
			sb.append(count).append("\n");
		}
		System.out.println(sb);
	}

	static void dfs(int cur) {
		visited[cur] = true;

		for (int person : relation[cur])
			if (!visited[person])
				dfs(person);
	}
}
