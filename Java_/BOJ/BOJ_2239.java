import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

/**
 * BOJ 2239 스도쿠
 * 1. 채워지지 않은 칸에 대해 아래 조건을 검사한다
 * 2. 칸을 중심으로 각각 가로 세로와 3*3 사각형에 같은 숫자가 없게 한다
 * 3. 채워지지 않은 칸의 좌표를 리스트에 저장하고 재귀적으로 탐색한다
 * 4. 조건을 만족할 수 없는 칸이 나오면 재귀를 탈출한다
 * 5. 재귀의 깊이가 채워지지 않은 칸 수와 같아지면 모든 칸을 채운 것이므로 출력한다
 */

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

	static int[][] board = new int[9][9];
	static ArrayList<int[]> blankList = new ArrayList<>();
	static boolean filled = false;

	public static void main(String[] args) throws IOException {
		// 보드 입력받고 값이 0일 경우 그 좌표 저장
		for (int row = 0; row < 9; row++) {
			String input = br.readLine().trim();
			for (int col = 0; col < 9; col++) {
				board[row][col] = input.charAt(col) - '0';
				if (board[row][col] == 0)
					blankList.add(new int[] { row, col });
			}
		}

		fillBlank(0);

		for (int row = 0; row < 9; row++) {
			for (int col = 0; col < 9; col++)
				System.out.print(board[row][col]);
			System.out.println();
		}
	}

	static void fillBlank(int depth) {
		if (depth == blankList.size()) {
			filled = true; // 보드를 다 채웠음을 표시
			return;
		}

		int row = blankList.get(depth)[0];
		int col = blankList.get(depth)[1];

		for (int num = 1; num <= 9; num++) {
			if (checkNum(row, col, num)) {
				board[row][col] = num;
				fillBlank(depth + 1);

				if (filled)
					return;

				board[row][col] = 0;
			}
		}
	}

	// 채워질 숫자의 조건 체크
	static boolean checkNum(int row, int col, int num) {
		// 가로 세로 확인
		for (int pos = 0; pos < 9; pos++)
			if (board[row][pos] == num || board[pos][col] == num)
				return false;

		// 현재 칸이 포함된 사각형의 시작 좌표
		int sRow = 3 * (row / 3);
		int sCol = 3 * (col / 3);

		// 사각형 확인
		for (int height = sRow; height < sRow + 3; height++)
			for (int width = sCol; width < sCol + 3; width++)
				if (board[height][width] == num)
					return false;

		return true;
	}
}
