package _03_21

func winnerOfGame(colors string) bool {
	s, n := 0, len(colors)
	for i, j := 0, 0; i < n; i = j {
		for j < n && colors[i] == colors[j] {
			j++
		}
		if v := j - i - 2; v > 0 {
			if colors[i] == 'A' {
				s += v
			} else {
				s -= v
			}
		}
	}
	return s > 0
}
