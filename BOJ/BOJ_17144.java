import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * BOJ 17144 �̼����� �ȳ�!
 */

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;

	static int R, C, T, count = 2;
	static int top, bottom; // ���� û���� ���ʰ� �Ʒ����� �� ��ǥ
	static int[][] board;

	public static void main(String[] args) throws IOException {
		String[] input = br.readLine().trim().split(" ");
		R = Integer.parseInt(input[0]);
		C = Integer.parseInt(input[1]);
		T = Integer.parseInt(input[2]);
		board = new int[R][C];

		for (int row = 0; row < R; row++) {
			st = new StringTokenizer(br.readLine().trim());
			for (int col = 0; col < C; col++) {
				board[row][col] = Integer.parseInt(st.nextToken());
				if (board[row][col] == -1 && top == 0) {
					top = row;
					bottom = row + 1;
				}
			}
		}

		// T�� ���� �ݺ�
		while (0 < T--) {
			diffuse();
			clean();
		}
		countDust();
		System.out.println(count);
	}

	// �̼������� 1�� ���� Ȯ��� ���� �� ����
	static void diffuse() {
		int[] dx = { 1, 0, -1, 0 }, dy = { 0, 1, 0, -1 };
		int[][] tmpBoard = new int[R][C];

		for (int row = 0; row < R; row++)
			for (int col = 0; col < C; col++) {
				if (board[row][col] > 0) {
					int dust = board[row][col] / 5;
					// ������ �� �������� Ȯ��
					for (int dir = 0; dir < 4; dir++) {
						int nRow = row + dx[dir];
						int nCol = col + dy[dir];

						if (inRange(nRow, nCol) && board[nRow][nCol] >= 0) {
							tmpBoard[nRow][nCol] += dust;
							tmpBoard[row][col] -= dust;
						}
					}
				}
			}

		for (int row = 0; row < R; row++)
			for (int col = 0; col < C; col++) {
				board[row][col] += tmpBoard[row][col];
			}
	}

	// ����û���Ⱑ 1�� ���� �۵��� ���� �� ����
	static void clean() {
		// ����û���� ����
		int[] cur1 = { top - 1, 0 };
		int[] dx1 = { -1, 0, 1, 0 }, dy1 = { 0, 1, 0, -1 };
		int dir = 0;
		while (dir < 4) {
			int[] next = { cur1[0] + dx1[dir], cur1[1] + dy1[dir] };

			if (inRange(next[0], next[1]) && next[0] <= top)
				if (board[next[0]][next[1]] != -1) {
					board[cur1[0]][cur1[1]] = board[next[0]][next[1]];
					cur1[0] = next[0];
					cur1[1] = next[1];
				} else {
					board[cur1[0]][cur1[1]] = 0; // ����û���⿡�� ������ ����
					break;
				}
			else
				dir++;
		}

		// ����û���� �Ʒ���
		int[] cur2 = { bottom + 1, 0 };
		int[] dx2 = { 1, 0, -1, 0 }, dy2 = { 0, 1, 0, -1 };
		dir = 0;
		while (dir < 4) {
			int[] next = { cur2[0] + dx2[dir], cur2[1] + dy2[dir] };

			if (inRange(next[0], next[1]) && next[0] >= bottom)
				if (board[next[0]][next[1]] != -1) {
					board[cur2[0]][cur2[1]] = board[next[0]][next[1]];
					cur2[0] = next[0];
					cur2[1] = next[1];
				} else {
					board[cur2[0]][cur2[1]] = 0; // ����û���⿡�� ������ ����
					break;
				}
			else
				dir++;
		}
	}

	// ���� �̼����� ī��Ʈ
	static void countDust() {
		for (int row = 0; row < R; row++)
			for (int col = 0; col < C; col++)
				count += board[row][col];
	}

	static boolean inRange(int row, int col) {
		return 0 <= row && row < R && 0 <= col && col < C;
	}
}
