import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Collections;
import java.util.TreeSet;

/**
 * SWEA 5658 보물상자 비밀번호
 * 1. 중복없이 정렬이 필요하기 때문에 Tree Set을 사용한다
 * 2. 보물상자는 사각형이므로 숫자 개수/4 만큼 회전한다
 * 3. 입력을 담은 배열의 인덱스를 하나씩 증가시키면서 회전한다고 가정한다
 */

public class Solution {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder sb = new StringBuilder();

	static int N, K;
	static char[] numberArr;
	static TreeSet<Integer> set;

	public static void main(String[] args) throws NumberFormatException, IOException {
		int T = Integer.parseInt(br.readLine().trim());

		for (int testCase = 1; testCase <= T; testCase++) {
			String[] input = br.readLine().trim().split(" ");
			N = Integer.parseInt(input[0]);
			K = Integer.parseInt(input[1]);
			numberArr = br.readLine().trim().toCharArray();

			set = new TreeSet<>(Collections.reverseOrder()); // 내림차순 정렬

			int rotate = N / 4; // 16진수의 자릿수
			// = 다른 숫자를 만들 수 있는 회전 수(처음 상태 포함)

			for (int start = 0; start < rotate; start++) {
				// 배열 인덱스를 하나씩 증가시키면서 회전한다고 가정
				String number = "";
				for (int idx = start; idx <= start + N; idx++) {
					int nIdx = idx < N ? idx : idx - N;

					if (number.length() < rotate) {
						// 16진수의 길이(자릿수)보다 작은 경우
						number += numberArr[nIdx];
					} else {
						set.add(Integer.parseInt(number, 16)); // 10진수로 변환해서 set에 저장
						number = "" + numberArr[nIdx];
					}
				}
			}
			Object[] setArr = set.toArray();
			int answer = (int) setArr[K - 1];

			sb.append("#").append(testCase).append(" ");
			sb.append(answer).append("\n");
		}
		System.out.println(sb);
	}
}
