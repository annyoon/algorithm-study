import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

/**
 * SWEA 5643 키 순서
 * 1. 입력을 받아 아래와 같이 두 개의 인접 리스트로 표현한다
 * 2. 자신보다 키가 큰(뒤에 있는) 학생을 가리키는 리스트와 키가 작은(앞에 있는) 학생을 가리키는 리스트
 * 3. DFS로 완전 탐색을 하며 방문하는 학생을 카운트한다
 * 4. 카운트 수가 전체 학생 수보다 1 작으면 자신의 키가 몇 번째인지 알 수 있는 학생이다
 */

public class Solution {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder sb = new StringBuilder();

	static int N, M, count = 0;
	static boolean[] visited;

	public static void main(String[] args) throws NumberFormatException, IOException {
		int T = Integer.parseInt(br.readLine().trim());
		int a, b; // 비교할 두 학생의 번호 저장

		for (int testCase = 1; testCase <= T; testCase++) {
			N = Integer.parseInt(br.readLine().trim());
			M = Integer.parseInt(br.readLine().trim());

			ArrayList<Integer>[] studentList1 = new ArrayList[N + 1];
			ArrayList<Integer>[] studentList2 = new ArrayList[N + 1];
			int answer = 0;

			for (int idx = 0; idx <= N; idx++) {
				// 리스트 초기화
				studentList1[idx] = new ArrayList<Integer>();
				studentList2[idx] = new ArrayList<Integer>();
			}

			for (int idx = 0; idx < M; idx++) {
				// 비교를 입력받아 두 개의 인접 리스트에 저장
				String[] input = br.readLine().trim().split(" ");
				a = Integer.parseInt(input[0]);
				b = Integer.parseInt(input[1]);

				studentList1[a].add(b);
				studentList2[b].add(a);
			}

			for (int student = 1; student <= N; student++) {
				// 방문 배열과 카운트 초기화하고 완전 탐색
				visited = new boolean[N + 1];
				count = 0;

				dfs(student, studentList1);
				dfs(student, studentList2);

				if (count == N - 1)
					answer++;
			}

			sb.append("#").append(testCase).append(" ");
			sb.append(answer).append("\n");

		}
		System.out.println(sb);
	}

	static void dfs(int cur, ArrayList<Integer>[] studentList) {
		for (int nextIdx = 0; nextIdx < studentList[cur].size(); nextIdx++) {
			int nCur = studentList[cur].get(nextIdx);

			if (!visited[nCur]) {
				// 방문하지 않은 학생인 경우
				visited[nCur] = true;
				count++;
				dfs(nCur, studentList);
			}
		}
	}
}
