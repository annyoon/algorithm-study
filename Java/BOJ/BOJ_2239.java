import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

/**
 * BOJ 2239 ������
 * 1. ä������ ���� ĭ�� ���� �Ʒ� ������ �˻��Ѵ�
 * 2. ĭ�� �߽����� ���� ���� ���ο� 3*3 �簢���� ���� ���ڰ� ���� �Ѵ�
 * 3. ä������ ���� ĭ�� ��ǥ�� ����Ʈ�� �����ϰ� ��������� Ž���Ѵ�
 * 4. ������ ������ �� ���� ĭ�� ������ ��͸� Ż���Ѵ�
 * 5. ����� ���̰� ä������ ���� ĭ ���� �������� ��� ĭ�� ä�� ���̹Ƿ� ����Ѵ�
 */

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

	static int[][] board = new int[9][9];
	static ArrayList<int[]> blankList = new ArrayList<>();
	static boolean filled = false;

	public static void main(String[] args) throws IOException {
		// ���� �Է¹ް� ���� 0�� ��� �� ��ǥ ����
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
			filled = true; // ���带 �� ä������ ǥ��
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

	// ä���� ������ ���� üũ
	static boolean checkNum(int row, int col, int num) {
		// ���� ���� Ȯ��
		for (int pos = 0; pos < 9; pos++)
			if (board[row][pos] == num || board[pos][col] == num)
				return false;

		// ���� ĭ�� ���Ե� �簢���� ���� ��ǥ
		int sRow = 3 * (row / 3);
		int sCol = 3 * (col / 3);

		// �簢�� Ȯ��
		for (int height = sRow; height < sRow + 3; height++)
			for (int width = sCol; width < sCol + 3; width++)
				if (board[height][width] == num)
					return false;

		return true;
	}
}
