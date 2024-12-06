package main

import "regexp"
import "strconv"
import "os"

var mul = regexp.MustCompile(`mul\((\d{1,3}),(\d{1,3})\)`)
var dont = regexp.MustCompile(`(?s)don't\(\).*?(do\(\)|$)`)

func mul_sum(memory string) (sum int) {
	for _, subs := range mul.FindAllStringSubmatch(memory, -1) {
		x, _ := strconv.Atoi(subs[1])
		y, _ := strconv.Atoi(subs[2])
		sum += x * y
	}
	return
}

func day3(path string) (answer1, answer2 int, err error) {
	memory, err := os.ReadFile(path)
	if err != nil {
		return
	}
	answer1 = mul_sum(string(memory))
	answer2 = mul_sum(dont.ReplaceAllString(string(memory), "#"))
	return
}
