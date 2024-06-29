import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * BOJ 16395 파스칼의 삼각형
 * 1. n개 중에 r개를 순서 없이 뽑는 조합을 계산한다
 * 2. 파스칼의 삼각형을 통해 n-1Cr-1 + n-1Cr = nCr임을 알 수 있다
 */

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

	static int N, K; // N개 중에 순서 없이 K개 뽑기

	public static void main(String[] args) throws IOException {
		String[] input = br.readLine().trim().split(" ");
		int N = Integer.parseInt(input[0]);
		int K = Integer.parseInt(input[1]);

		int[][] dp = new int[N + 1][K + 1];

		// 초기화
		for (int n = 0; n <= N; n++)
			dp[n][0] = 1;
		dp[1][1] = 1;

		for (int n = 2; n <= N; n++)
			for (int r = 1; r <= K; r++)
				dp[n][r] = dp[n - 1][r - 1] + dp[n - 1][r];

		System.out.println(dp[N - 1][K - 1]);
	}
}
