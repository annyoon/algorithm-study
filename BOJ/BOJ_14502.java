import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

/* BOJ 14502 연구소 */

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;

	static int N, M, answer = 0;
	static int[][] board;
	static boolean[][] visited;
	static ArrayList<int[]> virusList = new ArrayList<>();
	static int[] dx = { 1, 0, -1, 0 }, dy = { 0, 1, 0, -1 };
	static Queue<int[]> q = new LinkedList<>();

	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(br.readLine().trim());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		board = new int[N][M];

		for (int row = 0; row < N; row++) {
			st = new StringTokenizer(br.readLine().trim());
			for (int col = 0; col < M; col++) {
				board[row][col] = Integer.parseInt(st.nextToken());
				if (board[row][col] == 2)
					virusList.add(new int[] { row, col });
			}
		}

		getPos(0, 0, new int[3][2]);
		System.out.println(answer);
	}

	// 3개의 벽의 위치의 조합
	static void getPos(int depth, int start, int[][] posArr) {
		if (depth == 3) {
			// visited 배열 초기화 & 벽 위치 표시
			visited = new boolean[N][M];
			for (int[] pos : posArr)
				visited[pos[0]][pos[1]] = true;

			// BFS로 바이러스가 퍼진 상태 표시
			for (int[] virus : virusList) {
				q.add(new int[] { virus[0], virus[1] });
				bfs(virus[0], virus[1]);
			}

			answer = Math.max(answer, countArea());
			return;
		}

		for (int idx = start; idx < N * M; idx++) {
			// 벽을 세울 위치에 바이러스나 다른 벽이 있지 않아야 한다
			if (board[idx / M][idx % M] == 0) {
				posArr[depth] = new int[] { idx / M, idx % M };
				getPos(depth + 1, idx + 1, posArr);
			}
		}
	}

	static void bfs(int row, int col) {
		while (!q.isEmpty()) {
			int[] cur = q.poll();

			for (int dir = 0; dir < 4; dir++) {
				int nRow = cur[0] + dx[dir];
				int nCol = cur[1] + dy[dir];

				if (inRange(nRow, nCol) && !visited[nRow][nCol])
					if (board[nRow][nCol] == 0) {
						visited[nRow][nCol] = true;
						q.add(new int[] { nRow, nCol });
					}
			}
		}
	}

	static boolean inRange(int row, int col) {
		return 0 <= row && row < N && 0 <= col && col < M;
	}

	// 안전 영역의 크기 카운트
	static int countArea() {
		int cnt = 0;

		for (int row = 0; row < N; row++)
			for (int col = 0; col < M; col++)
				if (board[row][col] == 0 && visited[row][col] == false)
					cnt++;
		return cnt;
	}
}
