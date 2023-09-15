import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/* BOJ 10971 외판원 순회2 */

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;

	static int N, answer;
	static int[][] board;
	static boolean[] visited;
	static int[] dp;

	public static void main(String[] args) throws IOException {
		N = Integer.parseInt(br.readLine().trim());
		board = new int[N][N];
		visited = new boolean[N];
		answer = (int) 1e9;

		for (int row = 0; row < N; row++) {
			st = new StringTokenizer(br.readLine().trim());
			for (int col = 0; col < N; col++)
				board[row][col] = Integer.parseInt(st.nextToken());
		}

		permu(0, new int[N]);
		System.out.println(answer);
	}

	static void permu(int depth, int[] cityArr) {
		if (depth == N) {
			// 마지막 도시에서 처음 도시로 돌아가는 길이 있는 경우
			if (board[cityArr[N - 1]][cityArr[0]] != 0)
				answer = Math.min(answer, getCost(cityArr));
			return;
		}

		for (int idx = 0; idx < N; idx++)
			if (!visited[idx])
				if (depth == 0 || board[cityArr[depth - 1]][idx] != 0) {
					// 다음 도시로 가는 길이 있는 경우
					visited[idx] = true;
					cityArr[depth] = idx;
					permu(depth + 1, cityArr);
					visited[idx] = false;
				}
	}

	static int getCost(int[] cityArr) {
		int sum = board[cityArr[N - 1]][cityArr[0]]; // 마지막 도시에서 처음 도시로 가는 비용

		for (int idx = 0; idx < N - 1; idx++)
			sum += board[cityArr[idx]][cityArr[idx + 1]]; // 다음 도시로 가는 비용

		return sum;
	}
}
