import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;

/**
 * SWEA 4013 Ư���� �ڼ�
 * 1. �ٸ� �ڼ��� �پ� �ִ� ���� �ε����� ([0][2], [1][6]), ([1][2], [2][6]), ([2][2], [3][6])
 * 2. �ð� �������� ȸ���ϸ� �ε��� -1, �ݽð� ������ +1
 * 3. �� �ڼ��� �´�� �־ ���� Ȯ���ؾ� �ϴ� �ڼ��� �ֱ� ������ ���� ����Ʈ�� ǥ���ϰ� BFS�� ���� ȸ����ų �ڼ��� Ž���Ѵ�
 */

public class Solution {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder sb = new StringBuilder();

	static int K;
	static char[][] board;
	static boolean[] visited;
	static int[] start; // ȭ��ǥ�� ����Ű�� ���� �ε���(���� ��ġ) ����
	static int[][] rel = { { 1 }, { 0, 2 }, { 1, 3 }, { 2 } };
	static Queue<int[]> q;

	public static void main(String[] args) throws NumberFormatException, IOException {
		int T = Integer.parseInt(br.readLine().trim());

		for (int testCase = 1; testCase <= T; testCase++) {
			K = Integer.parseInt(br.readLine().trim());
			board = new char[4][8];
			start = new int[4];
			
			int score = 0;

			for (int num = 0; num < 4; num++)
				board[num] = br.readLine().trim().replaceAll(" ", "").toCharArray();

			for (int idx = 0; idx < K; idx++) {
				String[] input = br.readLine().trim().split(" ");
				int num = Integer.parseInt(input[0]) - 1;
				int dir = Integer.parseInt(input[1]);

				q = new ArrayDeque<>();
				q.add(new int[] { num, dir });
				visited = new boolean[4];
				bfs();
			}

			// ��� ȸ�� ��ģ �� ���� ���
			for (int num = 0; num < 4; num++)
				if (board[num][start[num]] == '1')
					score += Math.pow(2, num);

			sb.append("#").append(testCase).append(" ");
			sb.append(score).append("\n");
		}
		System.out.println(sb);
	}

	static void bfs() {
		while (!q.isEmpty()) {
			int[] cur = q.poll();
			visited[cur[0]] = true;

			for (int idx = 0; idx < rel[cur[0]].length; idx++) {
				int next = rel[cur[0]][idx];

				if (!visited[next]) {
					// ���� ���� ���� ���� ��ȣ�� ���� ���� �ε����� �޶���
					if (cur[0] < next) {
						if (board[cur[0]][(start[cur[0]] + 2) % 8] != board[next][(start[next] + 6) % 8])
							q.add(new int[] { next, -cur[1] });
					} else if (cur[0] > next)
						if (board[cur[0]][(start[cur[0]] + 6) % 8] != board[next][(start[next] + 2) % 8])
							q.add(new int[] { next, -cur[1] });
				}
			}
			// �´��� ���� ���� ���¸� ť�� ���� �� ���� ���� ���� ����
			change(cur[0], cur[1]);
		}
	}

	// �ڼ��� ��ȣ�� ȸ�� ������ �޾Ƽ� ȭ��ǥ�� ����Ű�� �� ���ϱ�
	// ������ �迭�� �ٲٴ� ���� �ƴ϶� �����ϴ� �ε����� �����ؼ� ȸ���ߴٰ� ����
	static void change(int num, int dir) {
		start[num] = start[num] < dir ? start[num] - dir + 8 : (start[num] - dir) % 8;
	}
}
