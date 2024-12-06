package main

import "strings"
import "strconv"
import "bufio"
import "os"

func report_is_safe(report []int) bool {
	prev := report[0]
	if report[1] > report[0] {
		for _, level := range report[1:] {
			if level - prev > 3 || level - prev < 1 {
				return false
			}
			prev = level
		}
	} else {
		for _, level := range report[1:] {
			if prev - level > 3 || prev - level < 1 {
				return false
			}
			prev = level
		}
	}
	return true
}

func dampened_report_is_safe(report []int) bool {
	for i := range report {
		if report_is_safe(append(append([]int{}, report[:i]...), report[i+1:]...)) {
			return true
		}
	}
	return false
}

func day2(path string) (answer1, answer2 int, err error) {
	file, err := os.Open(path)
	if err != nil {
		return
	}
	defer file.Close()
	lines := bufio.NewScanner(file)
	for lines.Scan() {
		words := bufio.NewScanner(strings.NewReader(lines.Text()))
		words.Split(bufio.ScanWords)
		var report []int
		for words.Scan() {
			var num int
			num, err = strconv.Atoi(words.Text())
			if err != nil {
				return
			}
			report = append(report, num)
		}
		if report_is_safe(report) {
			answer1 += 1
		}
		if dampened_report_is_safe(report) {
			answer2 += 1
		}
	}
	return
}
