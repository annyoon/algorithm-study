import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;

/**
 * BOJ 9205 ���� ���ø鼭 �ɾ��
 * 1. �� �Ÿ��� ����� �ʿ䰡 ���� ���� ���θ� ���ؾ� �ϱ� ������ ���� Ž���� �����Ѵ�
 * 2. 50���͸� ������ ���� �� ���� ���ž� �ϰ� ���ִ� 20���̱� ������ �ִ� 1000���͸� �� �� �ִ�
 * 3. �־��� �� ����(��, ������, �佺Ƽ��) ������ �Ÿ��� ����Ѵ�
 * 4. �Ÿ��� 1000���� ���ϸ� ���� ����Ǿ� �ִٰ� �����ϰ� ���� ��ķ� �����Ѵ�
 * 5. �佺Ƽ�� ��ҿ� �����ϸ� �ٷ� ������ ���� �����Ǳ� ������ BFS�� �ִ� �Ÿ��� Ž���Ѵ�
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
			posArr = new int[n + 2][2]; // ��ǥ ����
			check = new boolean[n + 2][n + 2];

			for (int pos = 0; pos < n + 2; pos++) {
				String[] input = br.readLine().trim().split(" ");
				posArr[pos][0] = Integer.parseInt(input[0]);
				posArr[pos][1] = Integer.parseInt(input[1]);

				for (int idx = 0; idx < pos; idx++) {
					// �Ÿ� = x ��ǥ�� ���� + y ��ǥ�� ����
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
