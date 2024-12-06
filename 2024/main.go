package main

import "fmt"

type dayFunc func(string) (int, int, error)

func main() {
	days := []dayFunc{
		day1,
		day2,
		day3,
	}
	for n, day := range days {
		path := fmt.Sprintf("day%d.in", n + 1)
		answer1, answer2, err := day(path)
		if err != nil {
			fmt.Printf("day% 2d: %s\n", n + 1, err)
		} else {
			fmt.Printf("day% 2d: %d %d\n", n + 1, answer1, answer2)
		}
	}
}
