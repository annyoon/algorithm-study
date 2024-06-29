import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

/**
 * SWEA 7465 â�� ���� ������ ����
 * 1. ���� ������� ���踦 ���� ����Ʈ�� ǥ���Ѵ�
 * 2. �� �� Ž���� ����� �ٽ� �湮���� �ʾƵ� �ǹǷ� ���� �˰� �ִ� ���踦 DFS Ž���Ѵ�
 * 3. DFS�� �� �� ����� ������ ������ ���� 1 ������Ų��
 */

public class Solution {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder sb = new StringBuilder();

	static int N, M, count; // ��� ��, ���� ��, ���� ��
	static ArrayList<Integer>[] relation; // ���� ����Ʈ
	static boolean[] visited;

	public static void main(String[] args) throws NumberFormatException, IOException {
		int T = Integer.parseInt(br.readLine().trim());

		for (int testCase = 1; testCase <= T; testCase++) {
			String[] input = br.readLine().trim().split(" ");
			N = Integer.parseInt(input[0]);
			M = Integer.parseInt(input[1]);
			count = 0;

			relation = new ArrayList[N + 1];
			visited = new boolean[N + 1];

			for (int idx = 0; idx <= N; idx++)
				relation[idx] = new ArrayList<Integer>();

			for (int i = 0; i < M; i++) {
				input = br.readLine().trim().split(" ");
				int num1 = Integer.parseInt(input[0]);
				int num2 = Integer.parseInt(input[1]);

				// ����Ʈ�� ���� �߰�
				relation[num1].add(num2);
				relation[num2].add(num1);
			}

			for (int person = 1; person <= N; person++)
				// �湮���� ���� ����̸� DFS�� �ƴ� ���� ��� Ž��
				if (!visited[person]) {
					dfs(person);
					count++;
				}

			sb.append("#").append(testCase).append(" ");
			sb.append(count).append("\n");
		}
		System.out.println(sb);
	}

	static void dfs(int cur) {
		visited[cur] = true;

		for (int person : relation[cur])
			if (!visited[person])
				dfs(person);
	}
}
