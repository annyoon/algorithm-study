import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

/* BOJ 1644 소수의 연속합 */

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

	static int N;
	static ArrayList<Integer> prime;

	public static void main(String[] args) throws IOException {
		N = Integer.parseInt(br.readLine().trim());
		prime = new ArrayList<>();

		getPrime();

		int count = 0, left = 0, right = 0;
		int cur = 2;

		while (left < prime.size() && right < prime.size()) {
			if (cur == N) {
				count++;
				cur -= prime.get(left++);
			} else if (cur < N) {
				if (++right >= prime.size())
					break;
				cur += prime.get(right);
			} else {
				cur -= prime.get(left++);
			}
		}

		System.out.println(count);
	}

	static void getPrime() {
		boolean[] isPrime = new boolean[N + 1];
		isPrime[0] = isPrime[1] = true;

		for (int i = 2; i * i <= N; i++)
			if (!isPrime[i])
				for (int j = i; i * j <= N; j++)
					isPrime[i * j] = true;

		for (int i = 0; i <= N; i++)
			if (!isPrime[i])
				prime.add(i);
	}
}
