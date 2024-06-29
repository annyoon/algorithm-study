import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * BOJ 16395 �Ľ�Į�� �ﰢ��
 * 1. n�� �߿� r���� ���� ���� �̴� ������ ����Ѵ�
 * 2. �Ľ�Į�� �ﰢ���� ���� n-1Cr-1 + n-1Cr = nCr���� �� �� �ִ�
 */

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

	static int N, K; // N�� �߿� ���� ���� K�� �̱�

	public static void main(String[] args) throws IOException {
		String[] input = br.readLine().trim().split(" ");
		int N = Integer.parseInt(input[0]);
		int K = Integer.parseInt(input[1]);

		int[][] dp = new int[N + 1][K + 1];

		// �ʱ�ȭ
		for (int n = 0; n <= N; n++)
			dp[n][0] = 1;
		dp[1][1] = 1;

		for (int n = 2; n <= N; n++)
			for (int r = 1; r <= K; r++)
				dp[n][r] = dp[n - 1][r - 1] + dp[n - 1][r];

		System.out.println(dp[N - 1][K - 1]);
	}
}
