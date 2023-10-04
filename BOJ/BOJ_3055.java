import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;

/**
 * BOJ 3055 탈출
 * 1. 최단 시간을 구해야 하기 때문에 BFS로 탐색한다
 * 2. 새로 물이 찬 곳의 좌표를 큐에 저장해놓고 매 분마다 업데이트한다
 */

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

	static int R, C, answer = -1;
	static char[][] board;
	static int[][] dist;
	static Queue<int[]> q = new ArrayDeque<>(); // 고슴도치 좌표 저장
	static Queue<int[]> waterQ = new ArrayDeque<>(); // 새로 물이 찬 곳의 좌표 저장
	static int[] dx = { 1, 0, -1, 0 }, dy = { 0, 1, 0, -1 };

	public static void main(String[] args) throws IOException {
		String[] input = br.readLine().trim().split(" ");
		R = Integer.parseInt(input[0]);
		C = Integer.parseInt(input[1]);
		board = new char[R][C];
		dist = new int[R][C];

		int[] cur = new int[] { 0, 0 }; // 고슴도치 처음 위치

		for (int row = 0; row < R; row++) {
			board[row] = br.readLine().trim().toCharArray();
			for (int col = 0; col < C; col++)
				if (board[row][col] == 'S') {
					// 고슴도치의 처음 위치 초기화
					board[row][col] = '.';
					cur[0] = row;
					cur[1] = col;
				} else if (board[row][col] == '*') {
					// 처음 물이 있는 곳의 좌표 저장
					waterQ.add(new int[] { row, col });
				}
		}

		q.add(cur);
		dist[cur[0]][cur[1]] = 1;
		bfs();

		System.out.println(answer == -1 ? "KAKTUS" : answer);
	}

	static void bfs() {
		int row, col;
		int nRow, nCol;
		int depth = 0;

		while (!q.isEmpty()) {
			int[] cur = q.poll();
			row = cur[0];
			col = cur[1];

			if (board[row][col] == 'D') {
				// 비버 굴에 도착한 경우
				answer = dist[row][col] - 1;
				break;
			}

			if (dist[row][col] != depth) {
				// 깊이가 바뀌어서(1분이 지나서) 물이 찬 경우
				moveWater();
				depth = dist[row][col];
			}

			for (int dir = 0; dir < 4; dir++) {
				nRow = row + dx[dir];
				nCol = col + dy[dir];

				if (inRange(nRow, nCol) && dist[nRow][nCol] == 0) {
					if (board[nRow][nCol] == '.' || board[nRow][nCol] == 'D') {
						dist[nRow][nCol] = dist[row][col] + 1; // 최단 시간 저장
						q.add(new int[] { nRow, nCol });
					}
				}
			}
		}
	}

	// 물 상태 업데이트
	static void moveWater() {
		int length = waterQ.size(); // 물인 위치의 수만큼 반복
		for (int idx = 0; idx < length; idx++) {
			int[] pos = waterQ.poll();

			for (int dir = 0; dir < 4; dir++) {
				int[] nPos = new int[] { pos[0] + dx[dir], pos[1] + dy[dir] };

				if (inRange(nPos[0], nPos[1]) && board[nPos[0]][nPos[1]] == '.') {
					board[nPos[0]][nPos[1]] = '*';
					waterQ.add(nPos); // 새로 물이 찬 곳의 좌표 추가
				}
			}
		}
	}

	static boolean inRange(int row, int col) {
		return 0 <= row && row < R && 0 <= col && col < C;
	}
}
