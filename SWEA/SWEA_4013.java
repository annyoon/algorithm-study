import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;

/**
 * SWEA 4013 특이한 자석
 * 1. 다른 자석과 붙어 있는 날의 인덱스는 ([0][2], [1][6]), ([1][2], [2][6]), ([2][2], [3][6])
 * 2. 시계 방향으로 회전하면 인덱스 -1, 반시계 방향은 +1
 * 3. 각 자석은 맞닿아 있어서 먼저 확인해야 하는 자석이 있기 때문에 인접 리스트로 표현하고 BFS로 다음 회전시킬 자석을 탐색한다
 */

public class Solution {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder sb = new StringBuilder();

	static int K;
	static char[][] board;
	static boolean[] visited;
	static int[] start; // 화살표가 가리키는 날의 인덱스(시작 위치) 저장
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

			// 모든 회전 마친 후 점수 계산
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
					// 현재 날과 다음 날의 번호에 따라 비교할 인덱스가 달라짐
					if (cur[0] < next) {
						if (board[cur[0]][(start[cur[0]] + 2) % 8] != board[next][(start[next] + 6) % 8])
							q.add(new int[] { next, -cur[1] });
					} else if (cur[0] > next)
						if (board[cur[0]][(start[cur[0]] + 6) % 8] != board[next][(start[next] + 2) % 8])
							q.add(new int[] { next, -cur[1] });
				}
			}
			// 맞닿은 날의 다음 상태를 큐에 삽입 후 현재 날의 상태 변경
			change(cur[0], cur[1]);
		}
	}

	// 자석의 번호와 회전 방향을 받아서 화살표가 가리키는 날 구하기
	// 실제로 배열을 바꾸는 것이 아니라 시작하는 인덱스만 저장해서 회전했다고 가정
	static void change(int num, int dir) {
		start[num] = start[num] < dir ? start[num] - dir + 8 : (start[num] - dir) % 8;
	}
}
