import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * SWEA 5656 벽돌 깨기
 * 1. 열의 최대 개수(W)가 12이고 구슬을 최대로 쏠 수 있는 횟수(N)는 4이기 때문에 완전 탐색이 가능하다
 * 2. 구슬을 쏘는 위치의 경우의 수를 구하고 경우의 수마다 보드를 변경하기 위해 새로 복사한다
 * 3. 연쇄적으로 벽돌이 깨지는 것은 재귀로 구현한다
 * 4. 복사된 보드를 마지막 행부터 탐색하면서 빈 칸을 채운다
 * 5. 경우의 수마다 이를 반복하면서 벽돌을 가장 많이 깰 수 있는 위치를 구한다
 */

public class Solution {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static StringBuilder sb = new StringBuilder();

	static int N, W, H;
	static int count, maxCount;
	static int[][] board;
	static int[][] nBoard;
	static int[] dx = { 1, 0, -1, 0 }, dy = { 0, 1, 0, -1 };

	public static void main(String[] args) throws NumberFormatException, IOException {
		int T = Integer.parseInt(br.readLine().trim());

		for (int testCase = 1; testCase <= T; testCase++) {
			String[] input = br.readLine().trim().split(" ");
			N = Integer.parseInt(input[0]);
			W = Integer.parseInt(input[1]);
			H = Integer.parseInt(input[2]);
			count = 0;
			maxCount = 0;

			board = new int[H][W];
			nBoard = new int[H][W];
			int bricks = 0; // 처음 전체 벽돌의 수

			for (int row = 0; row < H; row++) {
				st = new StringTokenizer(br.readLine().trim());
				for (int col = 0; col < W; col++) {
					board[row][col] = Integer.parseInt(st.nextToken());
					if (board[row][col] != 0)
						bricks++;
				}
			}

			getMarblePos(0, new int[N]);

			sb.append("#").append(testCase).append(" ");
			sb.append(bricks - maxCount).append("\n");
		}
		System.out.println(sb);
	}

	// 구슬을 쏘는 위치의 경우의 수 구하기
	static void getMarblePos(int depth, int[] posArr) {
		// idxArr 배열에 구슬을 쏘는 위치들이 순서대로 저장됨
		if (depth == N) {
			countBrick(posArr);
			maxCount = Math.max(maxCount, count);
			return;
		}
		for (int idx = 0; idx < W; idx++) {
			posArr[depth] = idx;
			getMarblePos(depth + 1, posArr);
		}
	}

	// 깰 수 있는 벽돌 세기
	static void countBrick(int[] posArr) {
		count = 0; // 벽돌 수 초기화
		for (int row = 0; row < H; row++)
			nBoard[row] = board[row].clone(); // 보드 복사

		for (int pos : posArr)
			for (int row = 0; row < H; row++)
				if (nBoard[row][pos] != 0) {
					// 맨 위의 벽돌인 경우
					breakBrick(new int[] { row, pos }); // 벽돌 깨기
					fillBlank(); // 공백 채우기
					break;
				}
	}

	// 벽돌 깨기 시뮬레이션
	static void breakBrick(int[] brick) {
		int power = nBoard[brick[0]][brick[1]]; // 벽돌의 적힌 숫자
		nBoard[brick[0]][brick[1]] = 0; // 폭발
		count++; // 깨진 벽돌 수 카운트

		for (int dir = 0; dir < 4; dir++)
			for (int i = 1; i < power; i++) {
				// 폭발 범위만큼 상하좌우로 탐색
				int row = brick[0] + dx[dir] * i;
				int col = brick[1] + dy[dir] * i;

				if (inRange(row, col)) {
					// 벽돌 숫자가 1보다 큰 경우
					// 재귀 호출해서 현재 벽돌 위치부터 연쇄 폭발
					if (nBoard[row][col] > 1) {
						breakBrick(new int[] { row, col });
					} else if (nBoard[row][col] == 1) {
						nBoard[row][col] = 0; // 1인 경우 제자리만 폭발
						count++;
					}
				}
			}
	}

	// 폭발 후 공백 채우기
	static void fillBlank() {
		for (int col = 0; col < W; col++) {
			int blank = 0; // 공백의 개수 카운트
			for (int row = H - 1; row > -1; row--)
				if (blank > 0 && nBoard[row][col] != 0) {
					// 벽돌을 공백 개수만큼 아래로 내리기
					int tmp = nBoard[row][col];
					nBoard[row + blank][col] = tmp;
					nBoard[row][col] = 0;
				} else if (nBoard[row][col] == 0) {
					blank++;
				}
		}
	}

	static boolean inRange(int row, int col) {
		return 0 <= row && row < H && 0 <= col && col < W;
	}
}
