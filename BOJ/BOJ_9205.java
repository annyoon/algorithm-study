import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;

/**
 * BOJ 9205 맥주 마시면서 걸어가기
 * 1. 총 거리를 계산할 필요가 없고 가능 여부를 구해야 하기 때문에 완전 탐색을 수행한다
 * 2. 50미터를 가려면 맥주 한 병을 마셔야 하고 맥주는 20개이기 때문에 최대 1000미터를 갈 수 있다
 * 3. 주어진 각 정점(집, 편의점, 페스티벌) 사이의 거리를 계산한다
 * 4. 거리가 1000미터 이하면 서로 연결되어 있다고 간주하고 인접 행렬로 저장한다
 * 5. 페스티벌 장소에 도착하면 바로 문제의 답이 결정되기 때문에 BFS로 최단 거리를 탐색한다
 */

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder sb = new StringBuilder();

	static int n;
	static int[][] posArr;
	static boolean[] visited;
	static boolean[][] check;
	static Queue<Integer> q;
	static String answer;

	public static void main(String[] args) throws IOException {
		int t = Integer.parseInt(br.readLine().trim());

		while (0 < t--) {
			n = Integer.parseInt(br.readLine().trim());
			posArr = new int[n + 2][2]; // 좌표 저장
			check = new boolean[n + 2][n + 2];

			for (int pos = 0; pos < n + 2; pos++) {
				String[] input = br.readLine().trim().split(" ");
				posArr[pos][0] = Integer.parseInt(input[0]);
				posArr[pos][1] = Integer.parseInt(input[1]);

				for (int idx = 0; idx < pos; idx++) {
					// 거리 = x 좌표의 차이 + y 좌표의 차이
					int dist = Math.abs(posArr[idx][0] - posArr[pos][0]) + Math.abs(posArr[idx][1] - posArr[pos][1]);

					if (dist <= 1000)
						check[pos][idx] = check[idx][pos] = true;
				}
			}
			visited = new boolean[n + 2];
			q = new ArrayDeque<>();
			q.add(0);
			answer = "sad";
			bfs();

			sb.append(answer).append("\n");
		}
		System.out.println(sb);
	}

	static void bfs() {
		while (!q.isEmpty()) {
			int cur = q.poll();

			if (cur == n + 1) {
				answer = "happy";
				break;
			}

			for (int next = 0; next < n + 2; next++)
				if (check[cur][next] && !visited[next]) {
					visited[next] = true;
					q.add(next);
				}
		}
	}
}
